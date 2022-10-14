#===================================================================================================
#                                       Copyright 2021 Siemens
#===================================================================================================
#
#    NOTE:  NX Development provides programming examples for illustration only.
#    NX Development assumes you are familiar with the programming language
#    demonstrated in these examples, and the tools used to create and debug NX/Open
#    programs. GTAC support professionals can help explain the functionality of
#    a particular procedure, but neither GTAC nor NX Development will modify
#    these examples to provide added functionality or construction procedures.
#
#File description:
#
#    An example program that exports Cableway data from the work part and imports it into a Teamcenter dataset.
#
#
#===================================================================================================
import NXOpen
import NXOpen.PDM
import NXOpen.MechanicalRouting
import NXOpen.UF
import os

#---------------------------------------------------------------------------------------------------
# Splits the work part's name into its item and revision.
def getWorkPartItemAndRevision():

    session   = NXOpen.Session.GetSession()
    workPart  = session.Parts.Work
    
    #- In managed mode, the work part name is the item/revision in the form "Zone/A1".
    nameParts     = workPart.Name.split( "/" )
    revisionParts = nameParts[1].split( ";" )
    
    item     = nameParts[0]
    revision = revisionParts[0]
    
    return item, revision

#---------------------------------------------------------------------------------------------------
# Exports any cableway and device data from the work part and below to the XML file.
def exportCablewaysData( cablewayXmlFile ):
    
    session         = NXOpen.Session.GetSession()
    workPart        = session.Parts.Work
    routingMgr      = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager( session )
    maxSearchLevels = 0 #- Zero means search all levels of the assembly under the work part.
    
    routingMgr.ExportCablewayToFile( workPart, cablewayXmlFile, "none", NXOpen.MechanicalRouting.RoutingManager.DataType.All, maxSearchLevels )
    

#-------------------------------------------------------------------------------------------
# Imports the XML file into a dataset under the work part's item revision.
def importIntoDataset( cablewayXmlFile ):

    item, revision = getWorkPartItemAndRevision()

    folder = '\\'.join(cablewayXmlFile.split('\\')[0:-1])

    # TODO: Fill these values in to match your Teamcenter configuration.
    itemIDs                  = [ item  ]
    itemRevisions            = [ revision ]
    datesetNames             = [ "CapitalRouterData"  ]
    datesetTypeNames         = [ "NXRouting"          ]
    datesetRelationTypeNames = [ "IMAN_manifestation" ]
    datasetToolNames         = [ "" ]
    fileTypes                = [ True ]
    namedReferenceNames      = [ "NXRout" ]
    fileNames                = [ folder ]
    directoryNames           = [ cablewayXmlFile ]
    
    session        = NXOpen.Session.GetSession()
    fileManagement = session.PdmSession.NewFileManagement()
    
    results = fileManagement.ImportFilesAndCreateDatasets( itemIDs, itemRevisions, datesetNames,
                                                           datesetTypeNames, datesetRelationTypeNames,
                                                           datasetToolNames, fileTypes, namedReferenceNames,
                                                           fileNames, directoryNames )
    if results[0] != 0:
        raise NXOpen.NXException( results[0] )

#---------------------------------------------------------------------------------------------------
def main():

    try:
        session   = NXOpen.Session.GetSession()
        ufSession = NXOpen.UF.UFSession.GetUFSession()

        # Use the Teamcenter export directory to temporarily store the XML file.
        exportFolder = ufSession.Ugmgr.AskExportDirectory( session.Parts.BaseWork.Tag )

        item, revision = getWorkPartItemAndRevision()
        item = item.replace( " ", "_" )

        cablewayXmlFile = exportFolder + "\\" + item + "_" + revision + "_cablewayData.xml"

        # Write out the cableway data to the temporary XML file.
        exportCablewaysData( cablewayXmlFile )

        # Then import that XML file into Teamcenter under the work part.
        importIntoDataset( cablewayXmlFile )
    
    except NXOpen.NXException as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Error", NXOpen.NXMessageBox.DialogType.Error, str(ex) )
    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Error", NXOpen.NXMessageBox.DialogType.Error, str(ex) )

    # Finally, delete the temporary XML file.
    if os.path.exists( cablewayXmlFile ):
        os.remove( cablewayXmlFile )

if __name__ == "__main__":
    main()
