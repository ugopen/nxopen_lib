//----------------------------------------------------------------------------
//                  Copyright (c) 2018 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//
// DotNetExecuteCPPExample.cs
//
// Description:
//   This is an example of running a C++ DLL using Session.Execute. 
//
//   This source file is the only file required for this project, however this project also requires 
//   the DLL from the project "CPPToBeExecuted" to run.
//   
//
//----------------------------------------------------------------------------


using System;
using NXOpen;

public class DotNetExecuteCPPExample
{
    // class members
    private static Session theSession;
    public static DotNetExecuteCPPExample theProgram;
    public static bool isDisposeCalled;

    //------------------------------------------------------------------------------
    // Constructor
    //------------------------------------------------------------------------------
    public DotNetExecuteCPPExample(String args)
    {
        try
        {
            isDisposeCalled = false;
            CallExecute(args);
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            // UI.GetUI().NXMessageBox.Show("Message", NXMessageBox.DialogType.Error, ex.Message);
        }
    }

    // Calls the session execute method on the C++ DLL.
    private void CallExecute(String DllToExecute)
    {
        // This should be the directory of the built CPP DLL

        // Arguments for C++ dlls must only be strings
        object[] args = new Object[2];
        args[0] = "C#";
        args[1] = "Args";

        // CPP dlls must have the entry point ufusr and class name null.
        theSession.Execute(DllToExecute, null, "ufusr", args);
    }

    //------------------------------------------------------------------------------
    //  Explicit Activation
    //      This entry point is used to activate the application explicitly
    //------------------------------------------------------------------------------
    public static int Main(string[] args)
    {
        int retValue = 0;
        try
        {
            theSession = Session.GetSession();
            if (args[0] == "")
            {
                retValue = 1;
                theSession.LogFile.WriteLine("No argument passed to the C# example, unable to find the shared library");
            }
            else
            {
                theProgram = new DotNetExecuteCPPExample(args[0]);
                theProgram.Dispose();
            }
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            retValue = 1;
        }
        return retValue;
    }

    //------------------------------------------------------------------------------
    // Following method disposes all the class members
    //------------------------------------------------------------------------------
    public void Dispose()
    {
        try
        {
            if (isDisposeCalled == false)
            {
                //TODO: Add your application code here 
            }
            isDisposeCalled = true;
        }
        catch (NXOpen.NXException ex)
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
    //       Session.LibraryUnloadOption.Immediately
    //       Session.LibraryUnloadOption.Explicitly
    //       Session.LibraryUnloadOption.AtTermination
    //
    //     Any programs that register callbacks must use 
    //     AtTermination as the unload option.
    //------------------------------------------------------------
    public static int GetUnloadOption(string arg)
    {
        //Unloads the image explicitly, via an unload dialog
        //return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);

        //Unloads the image when the NX session terminates
        //return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);

        //Unloads the image immediately after execution within NX
        return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);
    }

}

