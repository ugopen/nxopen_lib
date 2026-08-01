'''=================================================================================================
                                    Copyright 2022 Siemens
====================================================================================================
File description:
        Sample script for SCD5 files. Split SDC5 file by Subcase.

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
    dstFileName = prefix  + '_byStep.' + scdExt
    return dstFileName

def removeResultFiles(prefix) :
    for f in glob.glob(prefix +'_*.' + h5Ext):
        os.remove(f)

def getResultGroup(h5File):
    return h5File.visititems(lambda name, obj:  obj if obj.attrs.get('ContentType') == b'Results' else None)

def getResultSteps(resultGroup) :

    resultSteps = []
    # lambda function must return None on both branches to continue the iterations
    resultGroup.visititems(lambda name, obj: resultSteps.append(obj) and None if obj.attrs.get('ContentType') == b'SCSolutionStepGroup' else None)
    
    return resultSteps

def getResultDataSets(resultGroup) :

    dataSets = []
    # lambda function must return None on both branches to continue the iterations
    resultGroup.visititems(lambda name, obj: dataSets.append(obj) and None if isinstance(obj, h5py.Dataset) and obj.parent.attrs.get('ContentType') == b'SCData' else None)
    
    return dataSets

def getResultFileName(resultGroup, resultStep, prefix):
    relativeStepName = resultStep.name[len(resultGroup.name) : ]
    uniqueName = relativeStepName.replace('/', '_')
    resultFileName = prefix + uniqueName + '.' +h5Ext
    return resultFileName


def getResultDataSetName(resultGroup, dataSet):
    # remove the group name prefix from the source data set name 
    shortName = dataSet.name[len(resultGroup.name):]
    return shortName

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
    print('Script for splitting a scd5 file into multiple hdf5 files by creating a separate hdf5 file for result steps.')
    print('Receives a scd5 file as input. Creates a copy of the scd5 file referencing the results as virtual Data Sets from external files.')
    print('Usage: ' + sys.argv[0] + ' <scd5 file to split>')

def main() :

    if(len(sys.argv) != 2):
        printHelp()
        return 1

    srcFileName = sys.argv[1]

    # prefix common to all files created by split 
    prefix = getFileTitle(srcFileName) + '_s'

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

        resultSteps = getResultSteps(resultGroup)

        for step in resultSteps:
            resultFileName = getResultFileName(resultGroup, step, prefix)
            with h5py.File(resultFileName, 'a') as resFile:
                dataSets = getResultDataSets(step)
                for sourceDataSet in dataSets:
                    print('Copying data set ' + sourceDataSet.name + ' into a new file ...' , end = ' ')
                    dstDataSetName = getResultDataSetName(resultGroup, sourceDataSet)
                    resFile.copy(sourceDataSet, dstDataSetName)
                    print ('Done.')

                    # the sourceDataSet name is no longe valid after removing it from the source file
                    # It should be stored before deletion 
                    sourceDataSetName = sourceDataSet.name

                    # delete the result data set from destination file
                    del dstFile[sourceDataSetName]

                    # create a virtual layout with result external files as virtual sources
                    # Shape and data type of the Virtual Data Set are the same as those from the original data set
                    layout = h5py.VirtualLayout(sourceDataSet.shape, sourceDataSet.dtype)
                    layout[...] = h5py.VirtualSource(resultFileName, dstDataSetName, sourceDataSet.shape)

                    # create virtual data set referncing the data set from an external file
                    virtualSet = dstFile.create_virtual_dataset(sourceDataSetName, layout)
            
                    # copy the attributes from the original data set       
                    for name, value in sourceDataSet.attrs.items():
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
