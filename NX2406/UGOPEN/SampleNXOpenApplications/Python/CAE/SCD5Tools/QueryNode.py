'''=================================================================================================
                                    Copyright 2022 Siemens
====================================================================================================
File description:
        Sample script for SCD5 files. Plot a Graph for a specified Node and Measure.

===================================================================================================='''
from os import times
import h5py
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import math
import time


def getResultName(fullPath):
    return fullPath.split('/')[-2]

def getResultGroup(h5File):
    return h5File.visititems(lambda name, obj:  obj if obj.attrs.get('ContentType') == b'Results' else None)

def getLegendGroup(h5file):
    return h5file.visititems(lambda name, obj: obj if obj.attrs.get('ContentType') == b'Legends' else None)

def getNodeGroup(h5file):
    return h5file.visititems(lambda name, obj: obj if obj.attrs.get('ContentType') == b'Node' else None)

def extractDataSet(hsFile, dataSet, nodeId,  index, resultFile) :
    
    resultShape = dataSet.shape
    resultDtype = dataSet.dtype

    if len(resultShape) < 2:
        print("Skipped. ")
        return
    
    # assume the first iteration data set contains the iteration values: time steps or frequencies
    iterationDataSet = getIterationDataSet(hsFile, dataSet)
    
    # create the destination data set files that contains the slice of this data set
    with h5py.File(resultFile,'a') as resFile:
        resDataSet = resFile.create_dataset(dataSet.name, resultShape[0:1], resultDtype)
        resDataSet[...] = dataSet[:,index,...] 

        # the iteration data set might be already in the file if muliple data sets with the same name / quantity were found
        if iterationDataSet.name not in resFile:
            iterDataSet = resFile.create_dataset(iterationDataSet.name, iterationDataSet.shape, iterationDataSet.dtype)
            iterDataSet[...] = iterationDataSet
        
    
    valueLen = len(dataSet[0,index])
    m = []
    if valueLen == 3:
        # Values are vectors of 3 components
        for resultValues in dataSet[:,index,...]:
            m.append(math.sqrt(resultValues[0] ** 2 + resultValues[1] ** 2 + resultValues[2] ** 2))

    iterationsForPlot = [iter for iter in iterationDataSet]

    if valueLen == 3:
        # vector of 3 components
        fig, axs = plt.subplots(2,2)
        fig.set_figwidth(17)
        fig.set_figheight(8)
        resultName = getResultName(dataSet.name)
        quantityName = getQuantityAttr(dataSet.parent['__attributes__'])
        fig.suptitle(f'{resultName}: {quantityName} on node {nodeId}')
        
        axs[0,0].plot(iterationsForPlot, m, )
        axs[0,0].set_title('Magnitude')
        axs[0,1].plot(iterationsForPlot, dataSet[:,index,...][:,0])
        axs[0,1].set_title('X')
        axs[1,0].plot(iterationsForPlot, dataSet[:,index,...][:,1])
        axs[1,0].set_title('Y')
        axs[1,1].plot(iterationsForPlot, dataSet[:,index,...][:,2])
        axs[1,1].set_title('Z')

    if valueLen == 6:
        # Symmetric stress with 6 components
        fig, axs = plt.subplots(3, 2)
        fig.set_figwidth(17)
        fig.set_figheight(8)
        resultName = getResultName(dataSet.name)
        quantityName = getQuantityAttr(dataSet.parent['__attributes__'])
        fig.suptitle(f'{resultName}: {quantityName} on node {nodeId}')
        
        compNames = ('XX', 'YY', 'ZZ', 'XY', 'YZ', 'XZ')
        for i in range(3):
            for j in range(2):
                comp = i * 2 + j
                axs[i, j].set_title(compNames[comp])
                axs[i,j].plot(iterationsForPlot, dataSet[:,index,...][:,comp])

        
        
    elif valueLen == 1:
        # Scalar Value
        plt.plot(iterationsForPlot, dataSet[:,index,...])

    plt.tight_layout()



def getResultDataSets(h5File) :
    resultGroup =  getResultGroup(h5File)
    dataSets = []
    # lambda function must return None on both branches to continue the iterations
    resultGroup.visititems(lambda name, obj: dataSets.append(obj) and None if isinstance(obj, h5py.Dataset) and obj.parent.attrs.get('ContentType') == b'SCData' else None)
    
    return dataSets

def getIterationDataSet(h5File, dataSet) :

    dataLegends = dataSet.attrs['DataLegends']
    
    # Assume the first legend is the iteration daata legend
    # index 3 srores a hdf reference to the group conaining the legend data sets. 
    firstLegendGroup = h5File[dataLegends[0][3]]

    iterationDataSets = []
    
    legendTypes = {b'SCSimpleData', b'SCTimeStep', b'SCFrequencyStep', b'SCMode'}
    # lambda function must return None on both branches to continue the iterations
    firstLegendGroup.visititems(lambda name, obj: iterationDataSets.append(obj) and None if isinstance(obj, h5py.Dataset) and obj.parent.attrs.get('ContentType') in  legendTypes else None)
    
    return iterationDataSets[0] if len(iterationDataSets) > 0 else None


def getMeshNodeUserNumbers(h5File):
    nodeGroup = getNodeGroup(h5File)
    dataSet = nodeGroup['UserNumber']
    return dataSet[...]

def getMeshNodeIndex(nodeId, file):
    userNumbers = getMeshNodeUserNumbers(file)
    nodeIndices = np.where(userNumbers == nodeId) # returns a tuple storing at index 0 an array with found indices
    if len(nodeIndices[0]) == 0:
        return None

    # user numbers should be unique
    return nodeIndices[0][0]

def getQuantityAttr(attrGroup):
    return attrGroup.attrs.get('SCID_ResultQuantity')

def getNodeValueIndex(srcFile, nodeDataLegend, nodeIndex):
    # node data legend stores at index 3 a reference to the group storing the nodes
    nodeSet = srcFile[nodeDataLegend[3]]

    # legend nodes group can be a mesh nodes group or a node set stroing indices from a nodes mesh group
    if 'DATA' not in nodeSet.keys():
        # legend nodes group is a mesh nodes group. The node value index in the data set is the same as the mesho node index
        return nodeIndex

    # legend nodes group is a node set storing indices from the mesh nodes group. 
    nodesIndices = nodeSet['DATA'] [...]
    inputNodeIndices = np.where(nodesIndices == nodeIndex) # returns a tuple storing at index 0 an array with found indices
    if len(inputNodeIndices[0]) == 0:
        # input node index is not in the nodes set indices for this data set
        return None

    # a node index can appear at most once in a nodes set
    return inputNodeIndices[0][0]

def printHelp():
    print('Script for querying a scd5 file on nodes and measures. The result is a h5 file containing the data corresponding to the measure and node given as arguments.')
    print('RAs input it receives: the input scd5 file, the id of the node, name of the measure, name of the output file.')
    print('Expected to run in the directory containing the input scd5 file.')
    print('Usage: ' + sys.argv[0] + ' <input scd5 file> <node id> <measure name> <output file name>')

def main() :
    start = time.time()
    if(len(sys.argv) != 5) :
        printHelp()
        return 1
    srcFileName = sys.argv[1]
    nodeId = int(sys.argv[2])
    result = sys.argv[3]
    resultFile = sys.argv[4]

    if(os.path.exists(resultFile)):
        os.remove(resultFile)

    with h5py.File(srcFileName, 'r') as srcFile:

        resultDataSets =  getResultDataSets(srcFile)
        nodeIndex = getMeshNodeIndex(nodeId, srcFile)
        if  nodeIndex is None:
            print(f'Node Id {nodeId} not found.')
            exit(1)

        for ds in resultDataSets:

            # attributes of a data set are stored in the __attributes__ group of the data set parent group.
            attrGroup = ds.parent['__attributes__']
            resultQuantity = getQuantityAttr(attrGroup)
            resultName = getResultName(ds.name)
            if result == resultQuantity or result == resultName:

                dataLegends = ds.attrs['DataLegends']
                if len(dataLegends) != 2:
                    print(f'"{resultName}" skipped: Data set should have 2 legends (iteration and  node).')
                    continue

                legendName = dataLegends[1][4]
                if legendName != b'Node':
                    print(f'"{resultName}"  skipped. Data set does not have a node legend.')
                    continue

                nodeValueIndex = getNodeValueIndex(srcFile, dataLegends[1], nodeIndex)
                if nodeValueIndex is None:
                    print(f'"{resultName}" skipped: no data available for node {nodeId}.')
                    continue
                
                print( f'Extracting Data Set "{resultName}" with quantity "{resultQuantity}" ...', end = ' ')
                sys.stdout.flush()
                extractDataSet(srcFile, ds, nodeId, nodeIndex, resultFile)
                print('Done.')

    print('Split file complete.')
    end = time.time()
    print(end - start)
    plt.show()
    return 0

if __name__ == '__main__':
    main()
