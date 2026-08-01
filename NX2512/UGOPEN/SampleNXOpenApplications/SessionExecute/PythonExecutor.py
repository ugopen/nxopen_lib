#============================================================================
#                  Copyright (c) 2018 Siemens
#                      All rights reserved
#============================================================================
# 
#============================================================================

import NXOpen
import os.path

class ProgramToExecuteEntry:
  def __init__(self, pathToBinary, className):
    self.pathToBinary = pathToBinary
    self.className = className

def executeProgram(programsToExecute, args):
    theSession = NXOpen.Session.GetSession()
    theSession.ListingWindow.WriteLine("\nAttempting to execute " + programsToExecute.pathToBinary)

    if(os.path.exists(programsToExecute.pathToBinary)):
        theSession.Execute(programsToExecute.pathToBinary, programsToExecute.className, "ExecuteMe", args)
    else :
        theSession.ListingWindow.WriteLine(programsToExecute.pathToBinary + " does not exist --- skipping");

          


def callExecutor(pathToBinaries):
    theSession = NXOpen.Session.GetSession()
    theSession.ListingWindow.WriteLine("CallExecute from Python Executor Program.");

    # Pass in five different arguments
    args = [1, 3.14, False, "A String Argument", theSession.Parts.Work]

    programsToExecute = [ ProgramToExecuteEntry(pathToBinaries + "\\CPPToBeExecuted.dll", None), 
                         ProgramToExecuteEntry(pathToBinaries + "\\CSToBeExecuted.dll", "CSToBeExecuted"), 
                         ProgramToExecuteEntry(pathToBinaries + "\\JavaToBeExecuted.class", "JavaToBeExecuted"), 
                         ProgramToExecuteEntry(pathToBinaries + "\\PythonToBeExecuted.py", None)]

    for p in programsToExecute:
       executeProgram(p, args)


def main(args):
    theSession = NXOpen.Session.GetSession()
    theSession.ListingWindow.Open()
    if (args == None or args[0] == ""):
        theSession.ListingWindow.WriteLine("No argument passed to the Python executor, unable to find the programs to execute");
    else:
       callExecutor(args[0])

if __name__ == '__main__':
    main(sys.argv[1:])
