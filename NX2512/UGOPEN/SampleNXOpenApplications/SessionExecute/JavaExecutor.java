//----------------------------------------------------------------------------
//                  Copyright (c) 2023 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
// 
//----------------------------------------------------------------------------


import nxopen.*;
import java.io.*;

    class ProgramToExecuteEntry
    {
        public ProgramToExecuteEntry ( String pathToBinary, String className)
        {
            this.pathToBinary = pathToBinary;
            this.className = className;
        }
        public String pathToBinary;
        public String className;
    }

public class JavaExecutor
{

    public static Session theSession = null;



    public static void executeProgram(ProgramToExecuteEntry programsToExecute,Object args[]) throws Exception
    {

        theSession.listingWindow().writeLine("\nAttempting to execute " + programsToExecute.pathToBinary);
        File program = new File(programsToExecute.pathToBinary);

        if(program.exists())
        {
            theSession.execute(programsToExecute.pathToBinary, programsToExecute.className, "ufusr", args);
        }
        else
        {
            theSession.listingWindow().writeLine(programsToExecute.pathToBinary + " does not exist --- skipping");
        }
           

    }

    public static void callExecutor(String pathToBinaries) throws Exception
    {
        
        theSession.listingWindow().writeLine("CallExecute from Java Executor Program.");

        // Pass in five different arguments
        Object args[] = {1,3.14, false, "A String Argument", theSession.parts().work() };


        ProgramToExecuteEntry programsToExecute[] = { new ProgramToExecuteEntry(pathToBinaries + "\\CPPToBeExecuted.dll", null),
                             new ProgramToExecuteEntry(pathToBinaries + "\\CSToBeExecuted.dll", "CSToBeExecuted"), 
                             new ProgramToExecuteEntry(pathToBinaries + "\\JavaToBeExecuted.class", "JavaToBeExecuted"), 
                             new ProgramToExecuteEntry(pathToBinaries + "\\PythonToBeExecuted.py", null)};

        for (ProgramToExecuteEntry p : programsToExecute)
        {
            executeProgram(p, args);
        }
           

    }

    public static void main(String[] args) throws Exception
    {
        theSession = null;
        try
        {
            theSession = (Session)SessionFactory.get("Session");
            theSession.listingWindow().open();

            if (args == null || args[0].equals(""))
            {
                theSession.listingWindow().writeLine("No argument passed to the Java executor, unable to find the programs to execute");
            }
            else
            {
                callExecutor(args[0]);
            }
        }
        catch (Exception ex)
        {
            // ---- Enter your exception handling code here -----
            throw ex;
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
