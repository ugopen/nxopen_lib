'''=================================================================================================
                                    Copyright 2022 Siemens
====================================================================================================
File description:
        Sample script for SCD5 files. Print the content of an SCD5 file in the terminal.

===================================================================================================='''
import sys
import numpy as np
import h5py
from prettytable import PrettyTable


def getAttributeInfo(node):
    attributes = []
    attributeNames = ['SCID_ResultQuantity', 'SCID_DisplayName',
                      'SCID_ResultQuantityQualifiers', 'SCID_Component']
    for attr in attributeNames:
        if attr in node.attrs:
            value = node.attrs[attr]
            attributes.append(', '.join(value) if isinstance(
                value, np.ndarray) else value)
        else:
            attributes.append("")
    return attributes


def getDataInfo(data):
    return data.dtype.shape[0] if len(data.dtype.shape) > 0 else 1


def getContent(obj, loadCaseId, token, table):
    dataTypeMap = {
        1: "Scalar",
        3: "Vector",
        6: "Symmetric Tensor", 
        9: "Tensor"
    }
    
    iterationLegendTypes = { 
        b'SCTimeStep' : 'Time',
        b'SCFrequencyStep' : 'Frequency', 
        b'SCMode' : 'Mode'
    }

    if obj.attrs.get('ContentType') in  iterationLegendTypes:
        dataObject = obj['DATA']
        iterations = np.array(dataObject)
        print("Number of Iterations:", iterations.size)
        print("Iteration Type:", iterationLegendTypes[obj.attrs.get('ContentType')])
        
    if obj.attrs.get('ContentType') == b'SCData':
        legends = list(obj.attrs['DataLegends'])
        attributes = getAttributeInfo(obj["__attributes__"])
        dataType = getDataInfo(obj["DATA"])
        attributes.append(dataTypeMap[dataType]
                          if dataType in dataTypeMap else dataType)
        attributes.insert(0, loadCaseId+chr(token[0]))
        attributes.insert(1, obj.name.split('/')[-1])
        legendNames = [l[4].decode('utf8') for l in legends]
        attributes.append(', '.join(legendNames))
        attributes.append(obj["DATA"].is_virtual)
        table.add_row(attributes)
        token[0] += 1

def printHelp():
    print('Script for printing information about the content of a scd5 file.')
    print('Expected to run in the directory containing the input scd5 file.')
    print('Usage: ' + sys.argv[0] + ' <scd5 file>')

def main():

    if(len(sys.argv) != 2) :
        printHelp()
        return 1

    srcFileName = sys.argv[1]

    with h5py.File(srcFileName, 'r') as file:
        solutionSteps = []
        file.visititems(lambda name, obj: solutionSteps.append(
            obj) if obj.parent.attrs.get('ContentType') == b'SCSolutionStep' else None)
        if solutionSteps:
            steps = np.array(solutionSteps)
            for i in range(steps.shape[1]):
                step = steps[:, i]
                print("\nStep Name:", step[1].decode('utf-8'))
                result = file.get(step[2])
                loadCaseId = step[0].decode('utf-8')
                token = [65]  # ascii for 'A'
                table = PrettyTable()
                table.field_names = ["Index", "Result Name", "Result Quantity", "Display Name",
                             "Result Quantity Qualifiers", "Component", "Data Type", "Legends", "Virtual Dataset"]
                result.visititems(lambda name, obj: getContent(
                    obj, loadCaseId, token, table))

                table.align = "l"
                print(table)


if __name__ == '__main__':
    main()
