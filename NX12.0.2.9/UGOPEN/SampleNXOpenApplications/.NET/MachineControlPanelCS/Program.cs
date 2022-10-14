/*
 ==============================================================================

             Copyright (c) 2013  UGS PLM Solutions
               Unpublished - All rights reserved

 ==============================================================================
 ******************************************************************************
  Description
    Class that provides the Winforms UI for the Machine Control Panel example

 */
using System;
using NXOpen;
using System.Windows.Forms;
using MCP_CSharp;

public class Program
{
    // class members
    public static Form theForm;

    //------------------------------------------------------------------------------
    // Constructor
    //------------------------------------------------------------------------------
    
    //------------------------------------------------------------------------------
    //  Explicit Activation
    //      This entry point is used to activate the application explicitly
    //------------------------------------------------------------------------------
    public static int Main(string[] args)
    {
        int retValue = 0;
        
        theForm = new MCP();
        theForm.Show();

        return retValue;
    }

    public static int GetUnloadOption(string arg)
    {
        //Unloads the image explicitly, via an unload dialog
        return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);

        //Unloads the image immediately after execution within NX
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);

        //Unloads the image when the NX session terminates
        //return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
    }
}
