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

        var workPart = theSession.Parts.Work;
        
        int numCurves = 0;
        double curveLength = 0;
        foreach (Curve cur in workPart.Curves)
        {
            numCurves = numCurves + 1;
            curveLength = cur.GetLength();
            Guide.InfoWriteLine("Curve " + numCurves + " has length " + curveLength);
        }
        Guide.InfoWriteLine("Work part has " + numCurves + " curves.");
    }
}
