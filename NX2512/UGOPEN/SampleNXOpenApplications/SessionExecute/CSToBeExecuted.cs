//----------------------------------------------------------------------------
//                  Copyright (c) 2023 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//----------------------------------------------------------------------------


using System;
using NXOpen;

public class CSToBeExecuted
{
    public static void ExecuteMe(int arg1, double arg2, bool arg3, string arg4, NXOpen.TaggedObject arg5)
    {


        Session theSession = NXOpen.Session.GetSession();
        try
        {

            theSession.ListingWindow.WriteLine("    From CSToBeExecuted");
            theSession.ListingWindow.WriteLine("        Integer argument " + arg1.ToString());
            theSession.ListingWindow.WriteLine("        float argument " + arg2.ToString());
            theSession.ListingWindow.WriteLine("        bool argument " + arg3.ToString());
            theSession.ListingWindow.WriteLine("        string argument " + arg4.ToString());
            NXOpen.Part part = (NXOpen.Part)arg5;
            theSession.ListingWindow.WriteLine("        TaggedObject argument (returning WorkPart's Name) " + part.Name);
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            throw ex;
        }

        return;
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

