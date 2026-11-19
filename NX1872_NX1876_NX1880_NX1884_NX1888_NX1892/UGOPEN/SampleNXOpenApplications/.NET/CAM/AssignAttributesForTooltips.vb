'=============================================================================
'
'   Copyright 2012 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION
'
'     This program will cycle through all the CAM objects in the part and
'     assign the attributes required for picture tooltips in the create
'     object dialog.
'
'     The object names and attribute values are read from an Excel spreadsheet.
'     The row 1 headings for each column are:
'     Type,Name,Comment,CAM_ICON,CAM_TOOLTIP,CAM_PICTURE,CAM_TEXT,CAM_TEXT2,CAM_TEXT3
'     The following rows contain values.
'
'     If a cell is empty, that attribute will be deleted if it is found.
'
' ============================================================================
'   HOW TO RUN
'
'     Edit this file below for the path to the spreadsheet.
'     In the spreadsheet, enter attributes for each object name.
'     Open the template part, and run the journal.
'
' ============================================================================

Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module AssignMyAttributes

    '' The Excel filename (including path) that contains the object names and attributes.
    Private theExcelFile As String = "D:\Projects\NX CAM OOTB Content\AssignAttributesForTooltips_sample.xlsx"

    ' Category of attributes
    Private theAttributeCategory As String = "NX$CAM_TEMPLATE"

    ' Location of images
    Private thePictureFolder As String = "$UGII_CAM_TEMPLATE_IMAGE_DIR/"

    ' File type for images
    Private thePictureFileType As String = ".bmp"

    'class members
    Private theSession As Session
    Private theUfSession As UFSession

    Structure TooltipData
        Dim objType    As String
        Dim objName    As String
        Dim camIcon    As String
        Dim camTooltip As String
        Dim camPicture As String
        Dim camText    As String
        Dim camText2   As String
        Dim camText3   As String
    End Structure

' -------------------------------------------------------------------------------------------------
    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim WorkPart As Part = TheSession.Parts.Work

        ' Only continue if we have a work part
        If WorkPart IsNot Nothing Then
            ' Load setup
            Dim setupTag As Tag
            theUfSession.Cam.InitSession()
            theUfSession.Setup.AskSetup(setupTag)

            ' Only continue if we have a CAM setup
            If setupTag <> 0 Then
                ' Do attribute assignments
                LoadAndAssignAttributes (theExcelFile)
            Else
                PrintSimpleMessage ("The current part does not contain a CAM setup. Exiting.")
            End If

        Else
            PrintSimpleMessage("No part is open. Exiting.")
        End If

    End Sub

' -------------------------------------------------------------------------------------------------
    Function LoadAndAssignAttributes (ByVal excelFileName As String)

        theSession.ListingWindow().Open()
        theSession.ListingWindow().WriteLine("Reading Attributes from Spreadsheet.")

        ' Check if the Excel filename is given
        If Not String.IsNullOrWhiteSpace(excelFileName)

            ' Try to access Excel
            Dim objExcel = CreateObject("Excel.Application")
            If objExcel Is Nothing
                PrintSimpleMessage("Failed to access Excel. Exiting.")
                Return 0
            End If

            ' Open Excel workbook (filename, confirm conversion = false, open read-only = true)
            Dim objWorkbook = objExcel.Workbooks.Open (excelFileName, false, true)
            If objWorkbook Is Nothing
                Dim message As String
                message = "Failed to open Excel file: " + excelFileName + vbLF + "Exiting."
                PrintSimpleMessage(message)
                Return 0
            End If

            Dim row As Integer
            row = 2            ' we skip the first row, as we assume this contains the column headings.

            Dim rowData As TooltipData
            ' Loop over all data in the spreadsheet
            Do
                ' Read data from spreadsheet
                rowData.objType    = objExcel.Cells(row, 1).Value
                rowData.objName    = objExcel.Cells(row, 2).Value
                theSession.ListingWindow().WriteLine("Object: " + rowData.objName + " read data.")
                ' Column number 3 is expected to contain a comment. No need to read that.
                rowData.camIcon    = objExcel.Cells(row, 4).Value
                rowData.camTooltip = objExcel.Cells(row, 5).Value
                rowData.camPicture = objExcel.Cells(row, 6).Value
                rowData.camText    = objExcel.Cells(row, 7).Value
                rowData.camText2   = objExcel.Cells(row, 8).Value
                rowData.camText3   = objExcel.Cells(row, 9).Value

                ' If the objType is not empty, call function to assign the attributes for the object
                If Not String.IsNullOrWhiteSpace(rowData.objType)
                    FindObjectAndAssignAttribute(rowData)
                End If

                row = row + 1  ' next row until we find an empty one

            Loop Until String.IsNullOrWhiteSpace(rowData.objType)

            ' Close Excel
            objExcel.Quit
        Else
            PrintSimpleMessage("No Excel filename specified.")
        End If
    End Function

' -------------------------------------------------------------------------------------------------
    Function FindObjectAndAssignAttribute (ByVal rowData As TooltipData)

        Dim WorkPart As Part = TheSession.Parts.Work
        Dim camObject As CAM.CamObject = Nothing

        ' Try to find the object in the current CAM setup
        Try
            If String.Compare(rowData.objType, "OPERATION", true) = 0 Then
                camObject = CType(WorkPart.CAMSetup.CAMOperationCollection.FindObject(rowData.objName), CAM.CamObject)
            Else
                ' For non operation object, find the object in the corresponding view
                Dim rootNode As CAM.NCGroup = Nothing

                If String.Compare(rowData.objType, "TOOL", true) = 0 Then
                    rootNode = CType(WorkPart.CAMSetup.GetRoot(CAMSetup.View.MachineTool), CAM.NCGroup)
                Else If String.Compare(rowData.objType, "METHOD", true) = 0 Then
                    rootNode = CType(WorkPart.CAMSetup.GetRoot(CAMSetup.View.MachineMethod), CAM.NCGroup)
                Else If String.Compare(rowData.objType, "GEOMETRY", true) = 0 Then
                    rootNode = CType(WorkPart.CAMSetup.GetRoot(CAMSetup.View.Geometry), CAM.NCGroup)
                Else
                    rootNode = CType(WorkPart.CAMSetup.GetRoot(CAMSetup.View.ProgramOrder), CAM.NCGroup)
                End If

                If rootNode IsNot Nothing Then
                    camObject = CType(rootNode.FindObject(rowData.objName), CAM.CamObject)
                End If
            End If
        Catch ex As Exception
            '---- Enter your exception handling code here -----
            'Throw ex
        End Try

        ' If we found the object, assign the individual attributes
        If camObject IsNot Nothing Then
            AssignAttribute (camObject, "CAM_ICON", rowData.camIcon)
            AssignAttribute (camObject, "CAM_TOOLTIP", rowData.camTooltip)

            ' If the picture name is defined, add location and file type.
            If Not String.IsNullOrWhiteSpace(rowData.camPicture) Then
            AssignAttribute (camObject, "CAM_PICTURE", thePictureFolder + rowData.camPicture + thePictureFileType)
            Else
            ' Still call to delete old attributes
            AssignAttribute (camObject, "CAM_PICTURE", rowData.camPicture)
            End If

            AssignAttribute (camObject, "CAM_TEXT", rowData.camText)
            AssignAttribute (camObject, "CAM_TEXT2", rowData.camText2)
            AssignAttribute (camObject, "CAM_TEXT3", rowData.camText3)
        Else
            theSession.ListingWindow().WriteLine("Object: " + rowData.objName + " not found.")

        End If
    End Function

' -------------------------------------------------------------------------------------------------
    Function AssignAttribute (ByVal camObject As CAM.CamObject, ByVal attributeName As String, ByVal attributeValue As String)

        ' Only continue if we have an object and an attribute name
        If Not String.IsNullOrWhiteSpace(attributeName) And camObject IsNot Nothing Then

            ' We do not want to assign empty attributes
            If Not String.IsNullOrWhiteSpace(attributeValue) Then

                ' Set attribute without category
                ' camObject.SetAttribute (attributeName, attributeValue)

                'Set attribute with category
                Dim theSession As Session = Session.GetSession()
                Dim workPart As Part = theSession.Parts.Work
                Dim objects(0) As NXObject
                objects(0) = camObject
                Dim attributePropertiesBuilder1 As AttributePropertiesBuilder
                attributePropertiesBuilder1 = workPart.PropertiesManager.CreateAttributePropertiesBuilder(objects)

                attributePropertiesBuilder1.Category = theAttributeCategory
                attributePropertiesBuilder1.Title = attributeName
                attributePropertiesBuilder1.IsArray = False
                'NX 8.5 requires this
                attributePropertiesBuilder1.DataType = AttributePropertiesBaseBuilder.DataTypeOptions.String

                attributePropertiesBuilder1.StringValue = attributeValue
                Dim changed1 As Boolean
                changed1 = attributePropertiesBuilder1.CreateAttribute()

                theSession.ListingWindow().Open()
                theSession.ListingWindow().WriteLine("Object: " + camObject.Name() + " --> " + attributeName + " = " + attributeValue)

            Else
                ' If value not defined, remove existing attribute
                camObject.DeleteAttributeByTypeAndTitle(NXObject.AttributeType.String, attributeName)
                theSession.ListingWindow().WriteLine("Object: " + camObject.Name() + " --> " + attributeName + " Deleted.")
            End If
        End If
    End Function

' -------------------------------------------------------------------------------------------------
    Function PrintSimpleMessage (byVal message As String)
        Dim theUI As UI = UI.GetUI()

        If Not String.IsNullOrWhiteSpace(message)
            theUI.NXMessageBox.Show("Assign Tooltip Attributes", NXMessageBox.DialogType.Error, message)
        End If

    End Function

' -------------------------------------------------------------------------------------------------

End Module
