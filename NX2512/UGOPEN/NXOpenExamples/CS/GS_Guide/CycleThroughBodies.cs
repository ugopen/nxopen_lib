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
            var theUI = UI.GetUI();
            Guide.InfoWriteLine("Session and UI are created.");
            Guide.InfoWriteLine("");

            var workPart = theSession.Parts.Work;
            Guide.InfoWriteLine("Outputting list of bodies in work part:");
            NXOpen.Body[] bodies = workPart.Bodies.ToArray();
            foreach (NXOpen.Body body in bodies)
            {
                Guide.InfoWriteLine("Body: " + body.Name);
            }
            Guide.InfoWriteLine("");

            Guide.InfoWriteLine("Outputting list of user attributes in each body in the work part:");
            foreach (NXOpen.Body body in bodies)
            {
                var attributes = body.GetUserAttributes();
                foreach (var attribute in attributes)
                {
                    Guide.InfoWriteLine(attribute.Title + " = " + attribute.StringValue);
                }
            }
            Guide.InfoWriteLine("");
        }
}
