' ===================================================================
'
'             Copyright (c) 2011  Siemens PLM Solutions
'               Unpublished - All rights reserved
'
' ===================================================================
' *******************************************************************
'  Description
'    Example demostrating DraftingImage object 
'    and DraftingImageCollection object
' *******************************************************************

Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.Annotations
Imports System.Windows.Forms

Module NXJournal
Sub Main

Dim theSession As Session = Session.GetSession()
Dim workPart As Part = theSession.Parts.Work

Dim displayPart As Part = theSession.Parts.Display

' ---------------------------------------------------
'   Retrieve the DraftingImageCollection object.
' ---------------------------------------------------
Dim annotationManager As Annotations.AnnotationManager = displayPart.Annotations()

Dim images As Annotations.DraftingImageCollection = annotationManager.DraftingImages()

' ---------------------------------------------------
'   Use DraftingImage object's GetFileType
'   and use DraftingImage.FileType enum to
'   Determine the file type of the image.
' ---------------------------------------------------
Dim image As Annotations.DraftingImage = CType(images.FindObject("HANDLE R-6972"), Annotations.DraftingImage)

Dim type As Integer = image.GetFileType()

If type = Annotations.DraftingImage.FileType.JPG Then
    MessageBox.Show("Image HANDLE R-6972 is a JPG")
ElseIf type = Annotations.DraftingImage.FileType.PNG Then
    MessageBox.Show("Image HANDLE R-6972 is a PNG")
ElseIf type = Annotations.DraftingImage.FileType.TIF Then
    MessageBox.Show("Image HANDLE R-6972 is a TIF")
End If

' ---------------------------------------------------
'   Use iterator to retrieve all DraftingImage
'   and for each image, use DraftingImage's
'   ExportFile to export image to disk.
' ---------------------------------------------------
For Each i As Annotations.DraftingImage In images
    Dim fileExist as Boolean
    Dim filename As String = i.ExportFile(fileExist)
    If fileExist
        MessageBox.Show("Image cannot be exported because '" + filename + "' already exists.")
    Else
        MessageBox.Show("Export image to file '" + filename + "'")
    End If
Next i

' ---------------------------------------------------
'   End Example
' ---------------------------------------------------

End Sub
End Module








