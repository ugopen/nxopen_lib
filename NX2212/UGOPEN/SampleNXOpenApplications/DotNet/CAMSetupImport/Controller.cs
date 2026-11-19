/*
==============================================================================
 
        Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc.
                         Unpublished - All rights reserved

==============================================================================

 Description
    This file contains the main entry point for the simulation setup importer


==============================================================================*/
using System;
using System.IO;
using System.Windows.Forms;
using System.Xml.Serialization;

namespace CAMSetupImport
{
    public class Controller
    {
        public static void Main()
        {
            NXOpen.Session session = NXOpen.Session.GetSession();

            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Filter = "CAM Setup XML File (*xml)|*.xml" ;
            openFileDialog1.Multiselect = false;

            if (openFileDialog1.ShowDialog() != DialogResult.OK)
                return;

            string xmlfile = openFileDialog1.FileName;

            try
            {
                Importer importer = new Importer();
                importer.CreateSetup(xmlfile);
            }
            catch(System.InvalidOperationException e)
            {
                String message = e.Message;
                if(e.InnerException != null)
                    message += e.InnerException.Message;
                MessageUtils.ShowError(message);
            }
            catch(Exception e)
            {
                MessageUtils.ShowError(e.Message);
            }

        }

        public static int GetUnloadOption(string dummy) { return (int)NXOpen.Session.LibraryUnloadOption.Immediately; }
    }
}
