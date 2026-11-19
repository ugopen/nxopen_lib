"""
===================================================================================
                
                Unpublished work Copyright 2021 Siemens
                
===================================================================================
ReportGeneratorCmdLineParser.py

Description:
    this program construct a command line parser for report generator.





"""
import argparse
import sys


class CommandLineParser():

    def __init__(self):
        self.__parser = argparse.ArgumentParser(description="Report Writer Parser : Generates report documents for reports in input simulation parts. "
                                                            "The report document name would be \"part name + solution name + report name.docx\"")
        self.__Add_argument()

    def __Add_argument(self):
        """
        Description:
            add options or paramters for parsing
        Inputs:
            sim_part_names:       - main parameter, not necessary to provide
            -d                    - Optional. When it is specified, it is to generate report documents for simulation parts in this folder
            -sw                   - Optional. The wildcard of filtered solution name
            -rw                   - Optional. The wildcard of filtered report name 
            -o                    - Optional. The output folder of published report documents. If it is not provided, the report documents will be generated in same location of simulation part
            -or                   - Optional. The option tells the tool how to generate report document if the document with default name is existing. If it is not specified, the default option is \"skip“
        Outputs:
             
        """
        self.__parser.add_argument("sim_part_names", nargs='*',
                                 help="The input simulation part names which must be full name.")   # the main parameter for the command line
        self.__parser.add_argument("-d",
                                 help="Optional. When it is specified, it is to generate report documents for simulation parts in this folder")
        self.__parser.add_argument("-sw",
                                 help=" Optional. The wildcard of filtered solution name ")
        self.__parser.add_argument("-rw",
                                 help=" Optional. The wildcard of filtered report name ")
        self.__parser.add_argument("-o",
                                 help="Optional. The output folder of published report documents. If it is not provided, the report documents will be generated in same location of simulation part")
        self.__parser.add_argument("-or",choices=["skip","replace","new"],
                                 help="Optional. The option tells the tool how to generate report document if the document with default name is existing. If it is not specified, the default option is \"skip“")
    
    def ParseArgs(self, command_list):
        """
        Description:
            use the argparse to parse the command string
        Inputs:
            command_list:         - the list of the command , like ["-h","-o","D:\\outputdir","-d","D:\\targetSimFolder"]
        Outputs:
             map                  - a map, like {"or":new,"d","D:\\test","h":None...}
        """
        return vars(self.__parser.parse_args(command_list))

if __name__ == "__main__":
    writer = CommandLineParser()
    hh = sys.argv
    res = writer.ParseArgs(hh[1:])
    print(res)

