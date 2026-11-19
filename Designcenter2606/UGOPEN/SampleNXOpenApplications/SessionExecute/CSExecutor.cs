//----------------------------------------------------------------------------
//                  Copyright (c) 2023 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//----------------------------------------------------------------------------


using System;
using System.IO;
using NXOpen;

public class CSExecutor
{
    // class members
    private static Session theSession;
    public static CSExecutor theProgram;
    public static bool isDisposeCalled;

    //------------------------------------------------------------------------------
    // Constructor
    //------------------------------------------------------------------------------
    public CSExecutor()
    {
        isDisposeCalled = false;

    }

    private void ExecuteProgram(ProgramToExecuteEntry programsToExecute, object[] args)
    {
        theSession.ListingWindow.WriteLine("\nAttempting to execute " + programsToExecute.pathToBinary);

        if(File.Exists(programsToExecute.pathToBinary))
        {
            try
            {
                theSession.Execute(programsToExecute.pathToBinary, programsToExecute.className, "ExecuteMe", args);
            }
            catch(NXException ex)
            {
                theSession.ListingWindow.WriteLine(ex.Message);
            }
            
        }
        else
        {
            theSession.ListingWindow.WriteLine(programsToExecute.pathToBinary + " does not exist --- skipping");
        }
        
    }

    struct ProgramToExecuteEntry
    {
        public String pathToBinary;
        public String className;
    };

    // Calls the session execute method on the C++ DLL.
    private void CallExecutor(String PathToBinaries)
    {
        theSession.ListingWindow.Open();
        theSession.ListingWindow.WriteLine("CallExecute from C# Executor Program.");

        // Pass in five different arguments
        object[] args = new Object[5];
        args[0] = 1;
        args[1] = 3.14;
        args[2] = true;
        args[3] = "A String Argument";
        args[4] = theSession.Parts.Work;

        ProgramToExecuteEntry[] programsToExecute = new ProgramToExecuteEntry[4];
        programsToExecute[0].pathToBinary = PathToBinaries + "\\CPPToBeExecuted.dll";
        programsToExecute[0].className = null;
        programsToExecute[1].pathToBinary = PathToBinaries + "\\CSToBeExecuted.dll";
        programsToExecute[1].className = "CSToBeExecuted";
        programsToExecute[2].pathToBinary = PathToBinaries + "\\JavaToBeExecuted.class";
        programsToExecute[2].className = "JavaToBeExecuted";
        programsToExecute[3].pathToBinary = PathToBinaries + "\\PythonToBeExecuted.py";
        programsToExecute[3].className = null;

        foreach (ProgramToExecuteEntry program in programsToExecute)
        {
            ExecuteProgram(program, args);
        }

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
                theSession.LogFile.WriteLine("No argument passed to the C# executor, unable to find the programs to execute");
            }
            else
            {
                theProgram = new CSExecutor();
                theProgram.CallExecutor(args[0]);
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

