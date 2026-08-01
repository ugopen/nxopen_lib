/*==================================================================================================
  
                      Copyright (c) 2022 Siemens PLM 
                   Unpublished - All rights reserved

==================================================================================================*/

using System;
using NXOpen;

public class NXJournal
{
    public static void Main()
    {
        Session theSession = Session.GetSession();

        Guide.InfoWriteLine("Outputting list of user attributes on each body in the work part:");
        Body[] bodies = theSession.Parts.Work.Bodies.ToArray();
        foreach (Body aBody in bodies)
        {
            NXObject.AttributeInformation[] attributes = aBody.GetUserAttributes();
            foreach (NXObject.AttributeInformation attribute in attributes)
            {
                Guide.InfoWriteLine(attribute.Title + " = " + attribute.StringValue);
            }
        }
        Guide.InfoWriteLine("");
    }
}
