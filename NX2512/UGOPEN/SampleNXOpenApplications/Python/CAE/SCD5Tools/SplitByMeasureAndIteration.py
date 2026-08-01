'''=================================================================================================
                                    Copyright 2022 Siemens
====================================================================================================
File description:
        Sample script for SCD5 files. Split the SDC5 file by Iteration and Measure.

===================================================================================================='''

import h5py
import glob
import os
import subprocess
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

def getFileTitle(srcFileName):
    path = os.path.normpath(srcFileName)
    tokens = path.split(os.sep)
    return tokens[-1].split('.')[0]

def getDstFileName(prefix) :
    dstFileName = prefix  + '.' + scdExt
    return dstFileName

def getResultFileName(prefix, resultName, iterationIndex) :
    return prefix + f'_{resultName}' + f'_{iterationIndex:02d}.' + h5Ext

def removeResultFiles(prefix) :
    for f in glob.glob(prefix +'*.' + h5Ext):
        os.remove(f)

def getResultGroup(h5File):
    return h5File.visititems(lambda name, obj:  obj if obj.attrs.get('ContentType') == b'Results' else None)

def getQuantityAttr(attrGroup):
    return attrGroup.attrs.get('SCID_ResultQuantity')

def getDisplayNameAttr(attrGroup):
    return attrGroup.attrs.get('SCID_DisplayName')

def getQuantityQualifiersAttr(attrGroup):
    return  attrGroup.attrs.get('SCID_ResultQuantityQualifiers')

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


def hasIterationLegend(dataSet) :
    # name of legends that should be considered itreation legends and therefore allow split by iteration
    iterationLegends = {'Frequency', 'Time', 'Mode'}
    legends = dataSet.attrs['DataLegends']
    if(len(legends) < 1):
        # not really possible
        return False
    
    # iteration legend should always be the first one
    firstLagendName = legends[0][4].decode('utf8')
    return firstLagendName in iterationLegends

def extractDataSet(hsFile, resultName, resultFilePrefix) :
    dataSet = hsFile[resultName]
    
    resultShape = dataSet.shape
    resultDtype = dataSet.dtype

    if hasIterationLegend(dataSet):
        for i in range(dataSet.shape[0]):
            # create the destination data set files that contains the slice of this data set
            with h5py.File(getResultFileName(resultFilePrefix, getResultQuantityId(dataSet), i),'a') as resFile:
                resDataSet = resFile.create_dataset(resultName, resultShape[1:], resultDtype)
                resDataSet[...] = dataSet[i]
    else:
        # create the destination data set files that contains the entire data set
        with h5py.File(getResultFileName(resultFilePrefix, getResultQuantityId(dataSet), 0),'a') as resFile:
            resDataSet = resFile.create_dataset(resultName, resultShape, resultDtype)
            resDataSet[...] = dataSet[...]

    # delete the result data set from destination file. It will be replaced by a virtual data set
    del hsFile[resultName]

def createVirtualDataSet(h5SrcFile, hsDstFile, resultName, prefix) :
    dataSet = h5SrcFile[resultName]

    resultShape = dataSet.shape
    resultDtype = dataSet.dtype
    
    resultShortName = getResultQuantityId(dataSet)
    
    # create a virtual layout with result external files as virtual sources
    # Shape and data type of the Virtual Data Set are the same as those from the original data set
    layout = h5py.VirtualLayout(resultShape, resultDtype)
    if hasIterationLegend(dataSet):
        for i in range(resultShape[0]):
            vsource = h5py.VirtualSource(getResultFileName(prefix, resultShortName, i), resultName, resultShape[1:])
            layout[i] = vsource
    else:
        layout[...] = h5py.VirtualSource(getResultFileName(prefix, resultShortName, 0), resultName, resultShape)

    virtualSet = hsDstFile.create_virtual_dataset(resultName, layout)

    # copy the attributes from the original data set       
    for name, value in dataSet.attrs.items():
        virtualSet.attrs[name] = value
        
    # add additional attribures allowing to identify the result files 
    if hasIterationLegend(dataSet):
        resultFiles = [getResultFileName(prefix,resultShortName, i) for i in range(resultShape[0])]
    else:
        resultFiles = [getResultFileName(prefix,resultShortName, 0)]

    # The pithos attributes of a data set are stored as attributes on a group called '__attributes__' 
    # having the same parent as the data set. 
    virtualSet.parent['__attributes__'].attrs[RESULT_FILES] = resultFiles    

def printDataSet(dataSet) :

    # Data Set Properties
    print(dataSet.name + ":")
    print("  ndim: " + str(dataSet.ndim))
    print("  shape: " + str(dataSet.shape))
    print("  dtype: " + str(dataSet.dtype))
    print("  size: " + str(dataSet.size))
    print("  nbytes: " + str(dataSet.nbytes))
    print("")

def getResultDataSets(h5File) :

    resultGroup =  getResultGroup(h5File)

    dataSets = []

    # lambda function must return None on both branches to continue the iterations
    resultGroup.visititems(lambda name, obj: dataSets.append(obj) and None if isinstance(obj, h5py.Dataset) and obj.parent.attrs.get('ContentType') == b'SCData' else None)
    
    return dataSets

# depending on how to hdf5 file was created, unused space might not be removed from the file when removing a data set.
# to really free the unused space, h5repack tool should be used to copy the file into a new one.
def repack(fileName):
    packedFileName = fileName + '.tmp'
    subprocess.run([getH5Repack(), fileName, packedFileName], capture_output=True)
    
    # if there is no free space in the file, h5repack does not create a new file
    if os.path.isfile(packedFileName):
        os.remove(fileName)
        os.rename(packedFileName, fileName)    

def printHelp():
    print('Script for splitting a scd5 file into multiple hdf5 files by creating a separate hdf5 file for each iteration result.')
    print('Receives a scd5 file as input. Creates a copy of the scd5 file referencing the results as virtual Data Sets from external files.')
    print('Usage: ' + sys.argv[0] + ' <scd5 file to split>')
    

def main() :

    if(len(sys.argv) != 2) :
        printHelp()
        return 1
    
    srcFileName = sys.argv[1]
    
    # common prefix to all files created by split
    prefix = getFileTitle(srcFileName) + "_s1"

    # remove the Result files from a previous run
    print ('Removing previous result files ...', end = ' ')
    sys.stdout.flush()
    removeResultFiles(prefix)
    print ('Done.')

    dstFileName = getDstFileName(prefix)

    # copy source file name into a different file, just to keep the original file unchanges
    print ('Copying source file ...', end = ' ')
    sys.stdout.flush()
    copyfile(srcFileName, dstFileName)
    print ('Done.')
    
    # copy results data set in separate files sliced by first data set dimension (usually iteration: time step or frequency)
    with h5py.File(dstFileName, 'r+') as dstFile:

        resultNameToExtract = [ds.name for ds in getResultDataSets(dstFile)]
        
        for resultName in resultNameToExtract :
            print('Extracting data Set ' + resultName + ' ...', end = ' ')
            sys.stdout.flush()
            extractDataSet(dstFile, resultName, prefix)
            print('Done.')
    
        with h5py.File(srcFileName, 'r') as srcFile:
            print('Creating virtual data sets ...', end = ' ')
            sys.stdout.flush()
            for resultName in resultNameToExtract :
                createVirtualDataSet(srcFile, dstFile, resultName, prefix)
            print('Done.')    

    print('Repacking destination file ...', end = ' ')
    sys.stdout.flush()
    repack(dstFileName)
    print('Done.')

    print('Split file complete.')
    return 0


if __name__ == '__main__':
    main()
