//----------------------------------------------------------------------------
//                  Copyright (c) 2023 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
// 
//----------------------------------------------------------------------------


import nxopen.*;


public class JavaToBeExecuted
{
    public static void ExecuteMe(int arg1, double arg2, boolean arg3, String arg4, nxopen.TaggedObject arg5)  throws Exception
    {
        nxopen.Session theSession = null;
        theSession = (nxopen.Session)SessionFactory.get("Session");
        try
        {
            theSession.listingWindow().writeLine("    From JavaToBeExecuted");
            theSession.listingWindow().writeLine("        Integer argument " + String.valueOf(arg1));
            theSession.listingWindow().writeLine("        float argument " + String.valueOf(arg2));
            theSession.listingWindow().writeLine("        bool argument " + String.valueOf(arg3));
            theSession.listingWindow().writeLine("        string argument " + String.valueOf(arg4));
            nxopen.Part part = (nxopen.Part)arg5;
            theSession.listingWindow().writeLine("        TaggedObject argument (returning WorkPart's Name) " + part.name());
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
