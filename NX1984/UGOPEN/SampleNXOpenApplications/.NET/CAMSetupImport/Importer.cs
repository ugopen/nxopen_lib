/*
==============================================================================
 
        Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc.
                         Unpublished - All rights reserved

==============================================================================

 Description
    This class contains methods to import a simulation setup defined in a xml file.


==============================================================================*/

using System.IO;
using System.Xml.Serialization;

namespace CAMSetupImport
{
    public class Importer
    {
        public void CreateSetup(string xmlFile)
        {
            MessageUtils.AddToLogfile("Load File");
            Resources data = LoadDataFromFile(xmlFile);

            if (data == null)
                return;

            data.ResolveRelativePaths(Path.GetDirectoryName(xmlFile));

            MessageUtils.AddToLogfile("Start Import");
            Utils.CreateNewCAMSetupPart();
            MessageUtils.AddToLogfile("Setup created");
            data.LoadMachine();
            MessageUtils.AddToLogfile("Machine loaded");
            data.LoadPrograms();
            MessageUtils.AddToLogfile("Programs added");
            data.LoadPartsAndClamps();
            MessageUtils.AddToLogfile("Geometry added");
            data.LoadTools();
            MessageUtils.AddToLogfile("Tools loaded");
        }

        private Resources LoadDataFromFile(string xmlFile)
        {
            TextReader textReader = null;
            textReader = new StreamReader(xmlFile);

            XmlSerializer xmlSerializer = new XmlSerializer(typeof(Resources));
            Resources result = null;
            try
            {
                result = (Resources)xmlSerializer.Deserialize(textReader);
            }
            finally
            {
                textReader.Close();
            }
            return result;
        }
    }
}
