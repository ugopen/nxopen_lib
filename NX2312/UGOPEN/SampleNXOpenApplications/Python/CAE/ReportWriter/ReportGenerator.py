"""
===================================================================================
                
                Unpublished work Copyright 2021 Siemens
                

===================================================================================
ReportGenerator.py

Description:
    Generates report documents for reports in input simulation parts.
    The report document name would be "part name + solution name + report name.docx"

Usage:

    ReportGenerator
  <-h or -help> [sim part names]
  [-d= input folder] <-sw= "xxxx"> <-rw= "yyy"> <-o= folder> <-or= skip|replace|new>
  
        -h or - help
  -- Prints the command help information.
  
        Simulation part names
  
  – The input simulation part names which must be full name.
  
        -d
  – Optional. When it is specified, it is to generate report documents for simulation parts in this folder
  
        -sw
  – Optional. The wildcard of filtered solution name
  
        -rw
  – Optional. The wildcard of filtered report name
  
       -o
  – Optional. The output folder of published report documents. If it is not provided, the report documents will be generated in same location of simulation part.
  
       -or
  --Optional. The option tells the tool how to generate report document if the document with default name is existing. If it is not specified, the default option is "skip“
  
       There are 3 options:
  
                       skip - Not generate report document
  
                       replace - replace the existing one by a new document with same name
  
                       new - generate a new document which name appends index number in the default name
  

Notes:

     If part name or folder name contains white spaces,
  quotation marks must be used.
  
   Example Usage:
   1, Generates for all reports in my part.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim"
  
   2, Generates for all reports in my part.sim and my_part2.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim" "c:\my folder\my part2.sim"
  
   3, Generates for report in solutions which name is matched to the wildcard "*mysol" in my part.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim" -sw="*mysol"
  
   4, Generates for report which name is matched to the wildcard "*myreport" in my part.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim" -rw="*myreport"
  
   5, Generates for report which name is matched to the wildcard "*myreport"
    and which solution name is matched to wildcard "*mysol" in my part.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim" -rw= "*myreport"  -sw= "*mysol"
  
   6, Generates documents in folder myreports for all reports in my part.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim"   -o=myreports
  
   7 ,Generates all reports in my part.sim, if the document with default name existing, replace it with new docu
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim"   -or=replace
  
   8, Generates report documents to output folder myreports for all simulation parts in "my simparts" folder,
    , only those report which name is matched to the wildcard will be exported. If the report document in output
    folder is existing, skip it.
    run_journal.exe ReportGenerator.py -args -d="c:\my simparts"   -o=myreports -rw= "*myreport" -or=skip
  



"""


import os.path
import sys

import ReportGeneratorCmdLineParser

import NXOpen
import NXOpen.CAE
import NXOpen.Gateway
import NXOpen.OpenXml
import NXOpen.Preferences
import NXOpen.Report

import re

class Generator():

    def __init__(self):
        self.__sim_list = []
        
        # store the paramters from command line
        self.__prw = ""
        self.__psw = ""
        self.__por = ""
        self.__po = ""
        self.__pd = ""

        self.theSession =  NXOpen.Session.GetSession()
        self.workSimPart = None
        self.displaySimPart = None
        

    def Execute(self, argv):
        """
        Description:
            execute the report writer.
        Inputs:
            argv              - the args list, like ["-h","-d","D:\\test","-or","new"]
        Outputs:
            will publish all the reports in the sims.
        """
        print("reportGenerator is starting...")
        if argv==None or len(argv)==0:
            argv = ["-h"]
        
        ## parse the argv
        argvMap = self.__ParseArgv(argv)
        if argvMap == None:  ## terminate processing
            print("reportGenerator get nothings from the parse")
            return

        ## configure the sim, solution, report
        self.__Config(argvMap)
        self.__ValidateConfig()

        ## collect all the sims
        self.__CollectSimsFromFolder()
        
        ## publish reports 
        for sim_file in self.__sim_list:
            try:
                self.__PublishReportsOfSingleSim(sim_file)
            except Exception as e:
                print("        executing sim file \" %s \"  failed due to "%sim_file,"\"",e,"\"")
                pass

    def __ParseArgv(self, argv):
        """
        Description:
            parse the argv list into a map.
        Inputs:
            argv              - the args list, like ["-h","-d","D:\\test","-or","new"]
        Outputs:
            argvMap           - store the options into a map, like {"or":new, "d":"D:\\test", "h":None...}. this map will
            be used during the whole process
        """
        print("reportGenerator is parsering arguments to a map...")
        argvMap = None
        
        rw_cml_parse = ReportGeneratorCmdLineParser.CommandLineParser()
        try:
            argvMap = rw_cml_parse.ParseArgs(argv)
        except SystemExit as ex:
            print("reportGenerator exits %s "%ex)
            pass
            
        print("Arguments: " )
        print(argvMap)
        return argvMap
    
    ## set the properties to the Generator
    def __Config(self, argvMap):
        """
        Description:
            config the map information into the generator class
        Inputs:
            argvMap           - a map, like {"or":new,"d","D:\\test","h":None...}
        Outputs:
            
        """
        if argvMap==None:
            return
        print(" reportGenerate  configure the argvmap to Generator... ")
        
        self.__pd   = argvMap["d"] if argvMap["d"]!=None else ""
        self.__prw  = argvMap["rw"] if argvMap["rw"] !=None else ""
        self.__po   = argvMap["o"] if argvMap["o"] !=None else ""
        self.__por  = argvMap["or"] if argvMap["or"] !=None else ""
        self.__psw  = argvMap["sw"] if argvMap["sw"] !=None else ""
        self.__sim_list = argvMap["sim_part_names"] if argvMap["sim_part_names"] !=None else []

    ### verify the configuration
    #  1, no sim file,and -d is empty
    #  2,
    #
    def __ValidateConfig(self):
        """
        Description:
            validate confliction to make sure that all the necessary information are provided.
        Inputs:
            
        Outputs:
            
        """
        print(" reportGenerate is validating arguments...")
        # no sim and folder is indicated
        if (self.__pd == None or len(self.__pd)==0) and len(self.__sim_list)==0:
            raise Exception("No sim file or sim folder detected in the args, please check your input command line")

    ## collect the sim file iteratively
    def __CollectSimsFromFolder(self):
        """
        Description:
            collect the sims iteratively under folders from the -d options.
        Inputs:
            
        Outputs:
            
        """
        print(" reportGenerate is collecting sims from folder...")
        if len(self.__pd)> 0 :
            
            #check if it is a folder
            if os.path.isdir(self.__pd):
            
                # iterate the folder 
                for root, dirs , files in os.walk(self.__pd):
                    for file in files:
                        
                        #check if the file is a sim
                        if file.endswith(".sim"):
                            
                            # add the path string of the sim to the list
                            self.__sim_list.append(os.path.join(root, file))

    ## publish reports in the sim
    #  simName: str
    #
    #  things will be checked :
    #  1, whether the solution names accords with the option -sw
    #  2, the report names accords with the option -rw
    #
    def __PublishReportsOfSingleSim(self, simName):
        """
        Description:
            publish all the reports in the sim. In this function, -sw , -rw options will be checked.
            general workflow is :
                1, open sim
                2, iter the solutions in the sim
                3,      make the solution active
                4,      check if the solution satisfy the sw options
                5,      iter the reports in the solution
                6,              check if the solution satisfy the rw options
                7,               publish report
                8, close sim
        Inputs:
            sinName: str, the complete path of the sim file.
        Outputs:
            
        """
        print("    " + simName)
        
        basePart1, partLoadStatus1 = self.theSession.Parts.OpenActiveDisplay(simName, NXOpen.DisplayPartOption.AllowAdditional)

        self.workSimPart = self.theSession.Parts.BaseWork
        self.displaySimPart = self.theSession.Parts.BaseDisplay
        partLoadStatus1.Dispose()
        self.theSession.ApplicationSwitchImmediate("UG_APP_SFEM")

        print("        sim file is loaded...")
        
        # fix issue that the sim is a motion sim
        try:
            simSimulation1 = self.workSimPart.FindObject("Simulation")
        except:
            print("        sim file %s has no \" Simulation \" "%simName)
            self.theSession.Parts.CloseAll(NXOpen.BasePart.CloseModified.CloseModified, None)
            workSimPart = NXOpen.BasePart.Null
            displaySimPart = NXOpen.BasePart.Null
            self.theSession.ApplicationSwitchImmediate("UG_APP_NOPART")
            return
        
        solutions = simSimulation1.Solutions  #solutions
        simPart1 = self.workSimPart
        self.theSession.Post.UpdateUserGroupsFromSimPart(simPart1)

        for solution in solutions:
            
            simSimulation1.ActiveSolution = solution   # set the active solution
            print("            solution name:  "+ solution.Name)

            # check the solution names expressed in wildcard
            if(len(self.__psw) > 0):
                patter1 = self.__psw.replace("*", ".*")
                if "*" in patter1:   # there is wild-space
                    isMatched1 = re.match(patter1, solution.Name)
                else:
                    isMatched1 = patter1 == solution.Name
                    
                # the solution name is filtered out by the wildcard rule
                if not isMatched1:
                    continue
            
            #generate the reports
            for report in solution.GetReports():
                print("                 report name:  "+report.Name)
                ## check the report names expressed in wildcard
                if len(self.__prw)>0:
                    
                    #replace '*' with '.*', in line with regular
                    pattern2 = self.__prw.replace("*",".*")  
                    if "*" in pattern2:
                        isMatched2 = re.match(pattern2, report.Name)
                    else:
                        isMatched2 = report.Name == pattern2
                        
                    # the report name is filtered out by the wildcard rule
                    if not isMatched2:
                        continue
                
                self.__PublishReport(report,simName,solution.Name)

        ## close sim part
        self.theSession.Parts.CloseAll(NXOpen.BasePart.CloseModified.CloseModified, None)
        workSimPart = NXOpen.BasePart.Null
        displaySimPart = NXOpen.BasePart.Null
        self.theSession.ApplicationSwitchImmediate("UG_APP_NOPART")

    # report : NXOpen.Report.Report
    # simName: str
    # solutionName: str
    #
    #  things will be checked :
    #  1, whether the folder names is provided with the option -o
    #  2, what option is  to generate report document if the document with default name is existing.
    #
    def __PublishReport(self, report, simName, solutionName):
        """
        Description:
            publish the report. This function mainly deal with the output rules.
            -o -or options are checked here.
            
        Inputs:
            report:   NXOpen.Report.Report
            simName:  str , the complete path of a sim file
            solutionName:  the solutionName , which the report belongs to.
        Outputs:
            
        """
        simFolder,simulationName = self.__GetAbsoluteFolder(simName)
        newFile = ""
        reportDoc  = simulationName+"_"+solutionName + "_" + report.Name + ".docx"
        
        # -o  check option
        if len(self.__po)>0:
            
            # complete folder
            if os.path.isdir(self.__po):  
                newFile = os.path.join(self.__po,reportDoc)
            else:
                if not os.path.exists(os.path.join(simFolder,self.__po)):
                
                    # make a new directory
                    os.mkdir(os.path.join(simFolder,self.__po))   
                
                #
                newFolder = os.path.join(simFolder,self.__po) # folder
                newFile = os.path.join(newFolder,reportDoc)

        else:   # same folder as sim file
            newFile = os.path.join(simFolder,reportDoc)

        ## check option -or
        if os.path.exists(newFile):
            
            # will not publish the report, skip the case
            if self.__por == "skip":   
                return
            
            # verify if a new file will be created
            if self.__por == "replace":   
                os.remove(newFile)   # remove the old file
                
            if self.__por == "new":
                i = 1
                while os.path.exists(newFile):
                    if i == 1:
                        newFile = newFile.replace(r".docx","_new%s.docx"%i)
                    else:
                        newFile = newFile.replace(r"_new%s.docx"%(i-1),"_new%s.docx"%i)
                    i =  i+1

        report.Export(newFile, False)

   # linux and windows
   # /plm/shnas/dsf/asdf/a.sim
   # c:\\sdf\adfa\adfa\xx.sim
    def __GetAbsoluteFolder(self,pathString):
        """
        Description:
            get the folder and sim file from the sim path.
        Inputs:
            pathString:         - the complete path of a sim file
        Outputs:
            folderName:        - the folder of the sim file
            simulationName:    - the sim file name
        """
        
        if sys.platform == "win32":
            pattern = r"(.*\\)?(.*)\.sim"
        else:
            pattern = r"(.*/)?(.*)\.sim"
        
        #seperate folder and file from the path string
        folderName = re.match(pattern, pathString).group(1)   #   c:\\sdf\adfa\adfa\
        simulationName = re.match(pattern, pathString).group(2)#  xx.sim
        
        return folderName, simulationName


if __name__ == "__main__":

    generator = Generator()
    generator.Execute(sys.argv[1:])
