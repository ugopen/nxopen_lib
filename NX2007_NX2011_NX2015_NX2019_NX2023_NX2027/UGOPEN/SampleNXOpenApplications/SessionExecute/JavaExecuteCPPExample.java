//----------------------------------------------------------------------------
//                  Copyright (c) 2018 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
// 
// JavaCPPToBeExecuted.java
//
// Description:
//   This is an example of running a C++ DLL using Session.Execute. 
//
//   This source file is the only file required for this project, however this project also requires 
//   the DLL from the project "CPPToBeExecuted" to run.
//   
//
//   Additional information on MenuScript can be found in:
//     - the MenuScript User's Guide
//     - the NXOpen Programmer's Guide
//     - the NX Open for Java Reference Guide
//----------------------------------------------------------------------------


import nxopen.*;


public class JavaExecuteCPPExample
{
    public static void main(String[] args) throws Exception
    {
        Session theSession = null;
        try
        {
            theSession = (Session)SessionFactory.get("Session");
            Boolean tst = args[0].equals("");
            theSession.logFile().writeLine("tst value is: " + tst.toString());
            if (args == null || args[0].equals(""))
            {
                theSession.logFile().writeLine("No argument passed to the Java example, unable to find the shared library");
            }
            else
            {
                // This should be the directory of the built CPP shared library
                String dllToExecute = args[0]; 
                theSession.logFile().writeLine("Inside Java Session Execute Example with argument: " + args[0] + "of length: " + Integer.toString(args[0].length()));
                // Arguments for C++ shared libraries must only be strings
                Object [] argsOut = {"Java", "Args"};

                // CPP dlls must have the entry point ufusr and class name null.
                theSession.execute(dllToExecute, null, "ufusr", argsOut);
            }
        }
        catch (Exception ex)
        {
            // ---- Enter your exception handling code here -----
        }

    }

    //------------------------------------------------------------
    //
    //  GetUnloadOption()
    //
    //     Used to tell NX when to unload this library
    //
    //     Available options include:
    //       Session.LibraryUnloadOption.IMMEDIATELY
    //       Session.LibraryUnloadOption.EXPLICITLY
    //       Session.LibraryUnloadOption.ATTERMINATION
    //
    //     Any programs that register callbacks must use 
    //     AtTermination as the unload option.
    //------------------------------------------------------------
    public static int getUnloadOption() 
    { 
        //Unloads the image explicitly, via an unload dialog
        //return BaseSession.LibraryUnloadOption.EXPLICITLY;

        //Unloads the image when the NX session terminates
        //return BaseSession.LibraryUnloadOption.ATTERMINATION;

        //Unloads the image immediately after execution within NX
        return BaseSession.LibraryUnloadOption.IMMEDIATELY; 
    }
}
