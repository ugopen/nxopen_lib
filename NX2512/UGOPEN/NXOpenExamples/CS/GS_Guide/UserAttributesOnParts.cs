/*=================================================================================================
                      Copyright (c) 2022 Siemens PLM 

                    Unpublished - All rights reserved

==================================================================================================*/
using System;
using NXOpen;

public class NXJournal
{
    public static void Main()
    {
        var theSession = Session.GetSession();
        Guide.InfoWriteLine("Outputting list of user attributes on the work part:");
        var attributes = theSession.Parts.Work.GetUserAttributes();
        foreach(var attribute in attributes)
        {
            Guide.InfoWriteLine(attribute.Title + " = " + attribute.StringValue);
        }
        Guide.InfoWriteLine("");
    }
}
