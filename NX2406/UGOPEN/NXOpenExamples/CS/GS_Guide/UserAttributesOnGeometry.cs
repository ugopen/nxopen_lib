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

        Guide.InfoWriteLine("Outputting list of user attributes on geometry in the work part:");
        Body[] bodies = theSession.Parts.Work.Bodies.ToArray();
        foreach (Body aBody in bodies)
        {
            PrintAttributes(aBody);
            var edges = aBody.GetEdges();
            foreach (Edge edg in edges)
            {
                PrintAttributes(edg);
            }
            var faces = aBody.GetFaces();
            foreach (Face f in faces)
            {
                PrintAttributes(f);
            }
        }
        Guide.InfoWriteLine("");
    }
    static void PrintAttributes(NXObject obj)
    {
        var attributes = obj.GetUserAttributes();
        foreach (NXObject.AttributeInformation attribute in attributes)
        {
            Guide.InfoWriteLine(attribute.Title + " = " + attribute.StringValue);
        }
    }
}
