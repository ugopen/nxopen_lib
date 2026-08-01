'''=================================================================================================
                                    Copyright 2022 Siemens
====================================================================================================
File description:
        Sample script for SCD5 files. Merge the distributed scd5 files created by the split scripts.

===================================================================================================='''

import h5py
import os
import subprocess
import sys

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

def printHelp():
    print('Script for merging scd5 files.')
    print('Receives two scd5 files as input, a head scd5 file (the file which references the other split files) and the result file, which will contain the merged content of the split files.')
    print('Expected to run in the directory containing the split scd5 files.')
    print('Usage: ' + sys.argv[0] + ' <head scd5 file to merge> <output scd5 file>')

def getResultGroup(h5File):
    return h5File.visititems(lambda name, obj:  obj if obj.attrs.get('ContentType') == b'Results' else None)  

def isAttributeGroup(name):
    return(name.split('/')[-1] == '__attributes__')

def getResultAttributeGroups(h5File) :

    resultGroup =  getResultGroup(h5File)

    results = []

    # lambda function must return None on both branches to continue the iterations
    resultGroup.visititems(lambda name, obj: results.append(obj) and None if isAttributeGroup(name) and obj.parent.attrs.get('ContentType') == b'SCData' else None)

    return results

def main() :
    if len(sys.argv) != 3 :
        printHelp()
        return 1
    
    splittedFileName = sys.argv[1]
    mergedFileName = sys.argv[2]

    #merge the splitted files
    subprocess.run([getH5Repack(),'--merge','--prune','-f','GZIP=0', splittedFileName, mergedFileName], capture_output=True)

    #after the files are merged we need to remove the "ResultFiles" attribute from each result in the merged file
    with h5py.File(mergedFileName, 'a') as h5File:
        resultsAttrs = [res for res in getResultAttributeGroups(h5File)]
        for resultAttrs in resultsAttrs :
            resultAttrs.attrs.pop("ResultFiles", None)

if __name__ == '__main__':
    main()
