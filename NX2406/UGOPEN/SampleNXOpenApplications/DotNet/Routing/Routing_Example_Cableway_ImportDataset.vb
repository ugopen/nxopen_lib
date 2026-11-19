'===================================================================================================
'                                       Copyright 2021 Siemens
'===================================================================================================
'
'    NOTE:  NX Development provides programming examples for illustration only.
'    NX Development assumes you are familiar with the programming language
'    demonstrated in these examples, and the tools used to create and debug NX/Open
'    programs. GTAC support professionals can help explain the functionality of
'    a particular procedure, but neither GTAC nor NX Development will modify
'    these examples to provide added functionality or construction procedures.
'
'File description:
'
'    An example program that exports Cableway data from the work part and imports it into a Teamcenter dataset.
'
'
'===================================================================================================
Option Strict On
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.PDM
Imports NXOpen.MechanicalRouting
Imports NXOpen.UF

Module ImportDataSet

    '-----------------------------------------------------------------------------------------------
    Sub Main()

        Dim cablewayXmlFile As String = Nothing

        Try
            Dim session As Session = Session.GetSession()
            Dim ufSession As UFSession = UFSession.GetUFSession()

            '- Use the Teamcenter export directory to temporarily store the XML file.
            Dim exportFolder As String = Nothing
            ufSession.Ugmgr.AskExportDirectory(session.Parts.BaseWork.Tag, exportFolder)

            Dim item As String = Nothing
            Dim revision As String = Nothing
            getWorkPartItemAndRevision(item, revision)
            item = Replace(item, " ", "_")

            cablewayXmlFile = exportFolder + "\\" + item + "_" + revision + "_cablewayData.xml"

            '- Write out the cableway data to the temporary XML file.
            exportCablewaysData(cablewayXmlFile)

            '- Then import that XML file into Teamcenter under the work part.
            importIntoDataset(cablewayXmlFile)

        Catch ex As NXException
            UI.GetUI().NXMessageBox.Show("Error", NXMessageBox.DialogType.Error, ex.Message)
        Catch ex As Exception
            UI.GetUI().NXMessageBox.Show("Error", NXMessageBox.DialogType.Error, ex.Message)
        End Try

        ' Finally, delete the temporary XML file.
        If (File.Exists(cablewayXmlFile)) Then

            File.Delete(cablewayXmlFile)
        End If

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Exports any cableway And device data from the work part And below to the XML file.
    Sub exportCablewaysData(cablewayXmlFile As String)

        Dim session As Session = Session.GetSession()
        Dim workPart As Part = session.Parts.Work
        Dim routingMgr As RoutingManager = RoutingManager.GetRoutingManager(session)
        Dim maxSearchLevels As Integer = 0 '- Zero means search all levels Of the assembly under the work part.

        routingMgr.ExportCablewayToFile(workPart, cablewayXmlFile, "none", RoutingManager.DataType.All, maxSearchLevels)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Imports the XML file into a dataset under the work part's item revision.
    Sub importIntoDataset(cablewayXmlFile As String)

        Dim item As String = Nothing
        Dim revision As String = Nothing
        getWorkPartItemAndRevision(item, revision)

        ' TODO: Fill these values In To match your Teamcenter configuration.
        Dim itemIDs() As String = {item}
        Dim itemRevisions() As String = {revision}
        Dim datesetNames() As String = {"CapitalRouterData"}
        Dim datesetTypeNames() As String = {"NXRouting"}
        Dim datesetRelationTypeNames() As String = {"IMAN_manifestation"}
        Dim datasetToolNames() As String = {""}
        Dim fileTypes() As Boolean = {True}
        Dim namedReferenceNames() As String = {"NXRout"}
        Dim fileNames() As String = {Path.GetFileName(cablewayXmlFile)}
        Dim directoryNames() As String = {cablewayXmlFile}

        Dim session As Session = Session.GetSession()
        Dim fileManagement As FileManagement = session.PdmSession.NewFileManagement()

        Dim results() As Integer = fileManagement.ImportFilesAndCreateDatasets(itemIDs, itemRevisions, datesetNames,
                                                                                datesetTypeNames, datesetRelationTypeNames,
                                                                                datasetToolNames, fileTypes, namedReferenceNames,
                                                                                fileNames, directoryNames)
        If results(0) <> 0 Then
            Throw (NXException.Create(results(0)))
        End If

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Splits the work part's name into its item and revision.
    Sub getWorkPartItemAndRevision(item As String, revision As String)

        Dim session As Session = Session.GetSession()
        Dim ufSession As UFSession = UFSession.GetUFSession()
        Dim workPart As Part = session.Parts.Work

        ' In managed mode, the work part name Is the item/revision in the form "Zone/A1".
        Dim nameParts() As String = workPart.Name.Split(CType("/", Char()))
        Dim revisionParts() As String = nameParts(1).Split(CType(";", Char()))

        item = nameParts(0)
        revision = revisionParts(0)
    End Sub

    '-----------------------------------------------------------------------------------------------
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        ' Unloads the image immediately after execution within NX
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination
    End Function

End Module
