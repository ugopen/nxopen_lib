/*=================================================================================================
                      Copyright (c) 2022 Siemens PLM 

                    Unpublished - All rights reserved

==================================================================================================*/
using System;
using NXOpen;

namespace AddFaceUserAttribute
{
    public class NXJournal
    {
        public static void Main()
        {
            var theSession = Session.GetSession();
            var theUI = UI.GetUI();
            var workPart = theSession.Parts.Work;

            NXOpen.Body[] bodiesInPart = workPart.Bodies.ToArray();

            foreach (NXOpen.Body body in bodiesInPart)
            {
                var faces = body.GetFaces();
                foreach (var face in faces)
                {
                    face.SetUserAttribute("Surface Finish", -1, "Bead Blasted", Update.Option.Now);
                }
            }

        }
    }
}
