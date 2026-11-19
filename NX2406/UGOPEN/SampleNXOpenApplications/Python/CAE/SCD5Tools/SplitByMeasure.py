'''=================================================================================================
                                    Copyright 2022 Siemens
====================================================================================================
File description:
        Sample script for SCD5 files. Split SDC5 file by Measure.

===================================================================================================='''

import subprocess
import h5py
import glob
import os
import sys
from shutil import copyfile

# Get the Path to the h5repack utility from HDF Tools.
# It is required to repack (aka copy) the modified scd5 file to reclaim the file space used by the replaced data sets.
def getH5Repack():

    if os.name == 'nt':
        # On Windows, assume h5repack.exe is in the %PATH% environment
        # Otherwise specify Full Path to h5repack.exe. For ex:
        # return 'C:\\Program Files\\HDF_Group\\HDF5\\1.12.2\\bin\\h5repack.exe'
        return  'h5repack.exe'
    else:
        # On Linux, assume h5repack is in the $PATH environment
        return 'h5repack'

# file extesnions for the hdf5 files created by the script
scdExt = 'scd5'
h5Ext = 'h5'

# adiitional attributes added to identify external files used by VDS
RESULT_FILES = "ResultFiles"

# End of configuration parameters.

def getFileTitle(srcFileName) :
    path = os.path.normpath(srcFileName)
    tokens = path.split(os.sep)
    return tokens[-1].split('.')[0]

def getDstFileName(prefix) :
    dstFileName = prefix  + '_byMeasure.' + scdExt
    return dstFileName

def removeResultFiles(prefix) :
    for f in glob.glob(prefix +'_*.' + h5Ext):
        os.remove(f)

def getResultGroup(h5File):
    return h5File.visititems(lambda name, obj:  obj if obj.attrs.get('ContentType') == b'Results' else None)

def getQuantityAttr(attrGroup):
    return attrGroup.attrs.get('SCID_ResultQuantity')

def getDisplayNameAttr(attrGroup):
    return attrGroup.attrs.get('SCID_DisplayName')

def getQuantityQualifiersAttr(attrGroup):
    return attrGroup.attrs.get('SCID_ResultQuantityQualifiers')

def getParablicOptionAttr(attrGroup):
    return attrGroup.attrs.get('SCID_ParabolicOption')

def getResultQuantityId(resultDataSet) :
    # quantity stored as attribute on the __attributes__ group from the parent group of the result data set
    attrGroup = resultDataSet.parent['__attributes__']
    quantityId = getQuantityAttr(attrGroup)
    
    if quantityId is None:
        # For data sets that do not have a quantity id, use display name as quantity unique identifier
        quantityId = getDisplayNameAttr(attrGroup)

    quantityQualifiers = getQuantityQualifiersAttr(attrGroup)
    if quantityQualifiers is not None:
        for qualifier in quantityQualifiers:
            quantityId += f'_{qualifier}'

    parabOption = getParablicOptionAttr(attrGroup)
    if parabOption is not None:
        quantityId += f'_{parabOption}'

    return quantityId


# Builds the list of tuples(3) from the list of data sets name to extract
#   1. h5 internal path to the group / data set to extract
#   2. the name of the external h5 file containing the extracted path.
#   3. The h5 internal path of the group / data set in the extracted file
def getObjectsToExtractData(parentGroupName, resultDataSets, prefix) :
    tuples = [] 
    for ds in resultDataSets:
        resultName =  ds.name
        resultFileName = prefix + '_' + getResultQuantityId(ds) + '.' +h5Ext

        #remove the prefix common to all results from destination result file
        dstResultName = resultName[len(parentGroupName) :]
        tuples.append((resultName, resultFileName, dstResultName))

    return tuples

def getResultDataSets(resultGroup) :

    dataSets = []
    # lambda function must return None on both branches to continue the iterations
    resultGroup.visititems(lambda name, obj: dataSets.append(obj) and None if isinstance(obj, h5py.Dataset) and obj.parent.attrs.get('ContentType') == b'SCData' else None)
    
    return dataSets

# depending on how to hdf5 file was created, unused space might not be removed from the file when removing a data set.
# to really free the unused space, h5repack tool should be used to copy the file into a new one.
def repack(fileName):
    tokens = fileName.split('.') 
    packedFileName = tokens[0] + '_packed.' + tokens[1]
    subprocess.run([getH5Repack(), fileName, packedFileName], capture_output=True)
    
    # if there is no free space in the file, h5repack does not create a new file
    if os.path.isfile(packedFileName):
        os.remove(fileName)
        os.rename(packedFileName, fileName)

def printHelp():
    print('Script for splitting a scd5 file into multiple hdf5 files by creating a separate hdf5 file for result measure.')
    print('Receives a scd5 file as input. Creates a copy of the scd5 file referencing the results as virtual Data Sets from external files.')
    print('Usage: ' + sys.argv[0] + ' <scd5 file to split>')

def main() :

    if(len(sys.argv) != 2):
        printHelp()
        return 1

    srcFileName = sys.argv[1]

    # prefix common to all files created by split 
    prefix = getFileTitle(srcFileName) + '_m'

    # remove results from a previous run
    removeResultFiles(prefix)

    dstFileName = getDstFileName(prefix)

    # copy source file name into a different file
    print ('Copying source file ...', end = ' ')
    sys.stdout.flush()
    copyfile(srcFileName, dstFileName)
    print ('Done.')

    # extract the results into separate files and remove them from destination files
    with h5py.File(dstFileName, 'r+') as dstFile:

        resultGroup =  getResultGroup(dstFile)

        resultDataSets = getResultDataSets(dstFile)
        objectsToExtractData = getObjectsToExtractData(resultGroup.name, resultDataSets, prefix)

        for srcObjectName, resultFileName, dstObjectName in objectsToExtractData:
            sourceObject = dstFile[srcObjectName]
        
            # create the destination file that contains the results data set
            # open with append because the file file might exist if the input file contains multiple steps with the same result
            print('Copying data set ' + srcObjectName + ' into a new file ...' , end = ' ')
            sys.stdout.flush() 
            with h5py.File(resultFileName, 'a') as resFile:
                resFile.copy(sourceObject, dstObjectName)
            print ('Done.')

            # delete the result data set from destination file
            del dstFile[srcObjectName]

            # create a virtual layout with result external files as virtual sources
            # Shape and data type of the Virtual Data Set are the same as those from the original data set
            layout = h5py.VirtualLayout(sourceObject.shape, sourceObject.dtype)
            layout[...] = h5py.VirtualSource(resultFileName, dstObjectName, sourceObject.shape)

            # create virtual data set referncing the data set from an external file
            virtualSet = dstFile.create_virtual_dataset(srcObjectName, layout)
            
            # copy the attributes from the original data set       
            for name, value in sourceObject.attrs.items():
                virtualSet.attrs[name] = value

            # The pithos attributes of a data set are stored as attributes on a group called '__attributes__' 
            # having the same parent as the data set. 
            virtualSet.parent['__attributes__'].attrs[RESULT_FILES] = [resultFileName]
            
    print('Repacking destination file ...', end = ' ')
    sys.stdout.flush()
    repack(dstFileName)
    print('Done.')

    print('Split file complete.')
    return 0


if __name__ == '__main__':
    main()
