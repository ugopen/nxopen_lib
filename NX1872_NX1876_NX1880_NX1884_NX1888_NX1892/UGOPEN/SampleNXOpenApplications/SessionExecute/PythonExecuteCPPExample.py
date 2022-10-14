#============================================================================
#                  Copyright (c) 2018 Siemens
#                      All rights reserved
#============================================================================
# 
#
# PythonCPPToBeExecuted.py
#
# Description:
#   This is an example of running a C++ DLL using Session.Execute. 
#
#   This source file is the only file required for this example, however this example also requires 
#   the DLL from the project "CPPToBeExecuted" to run.
#   
#
#   Additional information on MenuScript can be found in:
#     - the NXOpen Programmer's Guide
#     - the NX Open for Python Reference Guide
#============================================================================

import NXOpen

def main(args):
    theSession = NXOpen.Session.GetSession()
    
    if (args == None or args[0] == ""):
        theSession.LogFile.WriteLine("No argument passed to the Python example, unable to find the shared library");
    else:
        # This should be the directory of the built CPP DLL
        DllToExecute = args[0]

        # Arguments for C++ dlls must only be strings
        args = ["Python", "Args"]

        # CPP dlls must have the entry point ufusr and class name null.
        theSession.Execute(DllToExecute, None, "ufusr", args)



if __name__ == "__main__":
    main(sys.argv[1:])
