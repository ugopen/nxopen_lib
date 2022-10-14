'=============================================================================
'
'                   Copyright (c) 2008 Siemens PLM Software
'                    Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for Block Styler
'===============================================================================
'

'==============================================================================
'  Purpose:  This TEMPLATE file contains VB.NET source to guide you in the
'  construction of your Block application dialog. The generation of your
'  dialog file (.dlx extension) is the first step towards dialog construction
'  within NX.  You must now create a NX Open application that
'  utilizes this file (.dlx).
'
'  The information in this file provides you with the following:
'
'  1.  Help on how to load and display your Block Styler dialog in NX
'      using APIs provided in NXOpen.BlockStyler namespace
'  2.  The empty callback methods (stubs) associated with your dialog items
'      have also been placed in this file. These empty methods have been
'      created simply to start you along with your coding requirements.
'      The method name, argument list and possible return values have already
'      been provided for you.
'==============================================================================

'------------------------------------------------------------------------------
'These imports are needed for the following template code
'------------------------------------------------------------------------------
Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.BlockStyler

'NEW CODE
Imports NXOpen.Features

'------------------------------------------------------------------------------
'Represents Block Styler application class
'------------------------------------------------------------------------------
Public Class SelectionExample
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Public Shared theSelectionExample As SelectionExample
    Private theDialogName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private group0 As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private edgeSelect As NXOpen.BlockStyler.UIBlock ' Block type: Curve Collector
    Private faceToggle As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private angleDouble As NXOpen.BlockStyler.UIBlock ' Block type: Double
    Private group01 As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private chamferSelect As NXOpen.BlockStyler.UIBlock ' Block type: Select Feature
    Private angleToggle As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private angleLimitDouble As NXOpen.BlockStyler.UIBlock ' Block type: Double

    'NEW CODE
    Private limitingFace As Face = Nothing 'face to limit edge selection

    
#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
        
            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDialogName = "SelectionExample.dlx"
            theDialog = theUI.CreateDialog(theDialogName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddOkHandler(AddressOf ok_cb)
            theDialog.AddUpdateHandler(AddressOf update_cb)
            theDialog.AddFilterHandler(AddressOf filter_cb)
            theDialog.AddInitializeHandler(AddressOf initialize_cb)
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            Throw ex
        End Try
    End Sub
#End Region
    
    '------------------------------- DIALOG LAUNCHING ---------------------------------
    '
    '    Before invoking this application one needs to open any part/empty part in NX
    '    because of the behavior of the blocks.
    '
    '    Make sure the dlx file is in one of the following locations:
    '        1.) From where NX session is launched
    '        2.) $UGII_USER_DIR/application
    '        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    '            recommended. This variable is set to a full directory path to a file 
    '            containing a list of root directories for all custom applications.
    '            e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
    '
    '    You can create the dialog using one of the following way:
    '
    '    1. Journal Replay
    '
    '        1) Replay this file through Tool->Journal->Play Menu.
    '
    '    2. USER EXIT
    '
    '        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
    '        2) Invoke the Shared Library through File->Execute->NX Open menu.
    '
    '------------------------------------------------------------------------------
    Public Shared Sub Main()
        Try
        
            theSelectionExample = New SelectionExample()
            ' The following method shows the dialog immediately
            theSelectionExample.Show()
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            theSelectionExample.Dispose()
        End Try
    End Sub
    '------------------------------------------------------------------------------
    ' This method specifies how a shared image is unloaded from memory
    ' within NX. This method gives you the capability to unload an
    ' internal NX Open application or user  exit from NX. Specify any
    ' one of the three constants as a return value to determine the type
    ' of unload to perform:
    '
    '
    '    Immediately : unload the library as soon as the automation program has completed
    '    Explicitly  : unload the library from the "Unload Shared Image" dialog
    '    AtTermination : unload the library when the NX session terminates
    '
    '
    ' NOTE:  A program which associates NX Open applications with the menubar
    ' MUST NOT use this option since it will UNLOAD your NX Open application image
    ' from the menubar.
    '------------------------------------------------------------------------------
    Public Shared Function GetUnloadOption(ByVal arg As String) As Integer
        'Return CType(Session.LibraryUnloadOption.Explicitly, Integer)
         Return CType(Session.LibraryUnloadOption.Immediately, Integer)
        ' Return CType(Session.LibraryUnloadOption.AtTermination, Integer)
    End Function
    '------------------------------------------------------------------------------
    ' Following method cleanup any housekeeping chores that may be needed.
    ' This method is automatically called by NX.
    '------------------------------------------------------------------------------
    Public Shared Sub UnloadLibrary(ByVal arg As String)
        Try


        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'This method shows the dialog on the screen
    '------------------------------------------------------------------------------
    Public Sub Show()
        Try
        
            theDialog.Show
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'Method Name: Dispose
    '------------------------------------------------------------------------------
    Public Sub Dispose()
        If theDialog IsNot Nothing Then 
            theDialog.Dispose()
            theDialog = Nothing
        End If
    End Sub
    
    '------------------------------------------------------------------------------
    '---------------------Block Styler Callback Functions--------------------------
    '------------------------------------------------------------------------------
    
    '------------------------------------------------------------------------------
    'Callback Name: initialize_cb
    '------------------------------------------------------------------------------
    Public Sub initialize_cb()
        Try
        
            group0 = theDialog.TopBlock.FindBlock("group0")
            edgeSelect = theDialog.TopBlock.FindBlock("edge_select0")
            faceToggle = theDialog.TopBlock.FindBlock("toggle0")
            angleDouble = theDialog.TopBlock.FindBlock("double0")
            group01 = theDialog.TopBlock.FindBlock("group01")
            chamferSelect = theDialog.TopBlock.FindBlock("select_feature0")
            angleToggle = theDialog.TopBlock.FindBlock("toggle01")
            angleLimitDouble = theDialog.TopBlock.FindBlock("double01")

            'NEW CODE
            limitingFace = Nothing

        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'Callback Name: apply_cb
    '------------------------------------------------------------------------------
    Public Function apply_cb() As Integer

        Dim errorCode As Integer = 0

        Try
            '*****************************************************************************************
            'Add Chamfers to Selected Edges

            'Get the chamfer angle and edge selection list from the dialog
            Dim angleDoubleProps As PropertyList = angleDouble.GetProperties()
            Dim creationAngle = angleDoubleProps.GetDouble("Value")
            angleDoubleProps.Dispose()
            angleDoubleProps = Nothing

            Dim edgeSelectProps As PropertyList = edgeSelect.GetProperties()
            Dim edges() As TaggedObject = edgeSelectProps.GetTaggedObjectVector("SelectedObjects")
            edgeSelectProps.Dispose()
            edgeSelectProps = Nothing

            'Add a chamfer to each selected edge
            For Each selectedEdge As TaggedObject In edges
                addChamfer(CType(selectedEdge, Edge), creationAngle)
            Next selectedEdge

            '*****************************************************************************************
            'Remove Selected Chamfers

            'Get the selected chamfers from the dialog
            Dim chamferSelectProps As PropertyList = chamferSelect.GetProperties()
            Dim chamfers() As TaggedObject = chamferSelectProps.GetTaggedObjectVector("SelectedObjects")
            chamferSelectProps.Dispose()
            chamferSelectProps = Nothing

            'Set an undo mark for update
            Dim undoMark As Session.UndoMarkId
            undoMark = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Remove Chamfers")

            'Add the selected chamfers to the delete list
            For Each chamferObject As TaggedObject In chamfers
                errorCode = deleteObject(CType(chamferObject, Features.Chamfer))
            Next chamferObject

            'Update the model to delete the chamfers
            Dim nErrs As Integer = theSession.UpdateManager.DoUpdate(undoMark)

            'Report any errors - normally the error list should be scanned and each error processed
            If nErrs > 0 Then
                errorCode = 1
                theUI.NXMessageBox.Show("Update Errors", NXMessageBox.DialogType.Error, "nErrs = " & nErrs.ToString)
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Apply Error", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

        apply_cb = errorCode

    End Function
    
    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try
            Dim faceToggleProps As PropertyList = faceToggle.GetProperties()
            Dim edgeSelectProps As PropertyList = edgeSelect.GetProperties()
            Dim chamferSelectProps As PropertyList = chamferSelect.GetProperties()
            Dim angleLimitDoubleProps As PropertyList = angleLimitDouble.GetProperties()
            Dim angleToggleProps As PropertyList = angleToggle.GetProperties()

            If block Is edgeSelect Then
                'When face filtering is on, establish a limiting face after two edges are selected

                If faceToggleProps.GetLogical("Value") Then
                    Dim edges() As TaggedObject = edgeSelectProps.GetTaggedObjectVector("SelectedObjects")
                    If (edges.Length = 2) Then
                        limitingFace = sharedFace(CType(edges(0), Edge), CType(edges(1), Edge))
                    End If
                End If

            ElseIf block Is faceToggle Then

                'When the face filter is turned on...
                '  Clear the current edge selection list

                If faceToggleProps.GetLogical("Value") Then
                    Dim edges(-1) As TaggedObject
                    edgeSelectProps.SetTaggedObjectVector("SelectedObjects", edges)
                    limitingFace = Nothing
                End If

            ElseIf block Is angleDouble Then
                '---- Enter your code here -----

            ElseIf block Is chamferSelect Then
                '---- Enter your code here -----

            ElseIf block Is angleToggle Then

                'When the angle fileter is turned on...
                '  1. Clear the current chamfer selection list
                '  2. Also, enable/disable the angle limit entry field

                If angleToggleProps.GetLogical("Value") Then
                    Dim chamfers(-1) As TaggedObject
                    chamferSelectProps.SetTaggedObjectVector("SelectedObjects", chamfers)
                    angleLimitDoubleProps.SetLogical("Enable", True)
                Else
                    angleLimitDoubleProps.SetLogical("Enable", False)
                End If

            ElseIf block Is angleLimitDouble Then

                ' When the angle limit value changes...
                '    Clear the current chamfer selection list
                Dim chamfers(-1) As TaggedObject
                chamferSelectProps.SetTaggedObjectVector("SelectedObjects", chamfers)

            End If

            faceToggleProps.Dispose()
            faceToggleProps = Nothing
            edgeSelectProps.Dispose()
            faceToggleProps = Nothing
            chamferSelectProps.Dispose()
            chamferSelectProps = Nothing
            angleLimitDoubleProps.Dispose()
            angleLimitDoubleProps = Nothing
            angleToggleProps.Dispose()
            angleToggleProps = Nothing

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

        update_cb = 0
    End Function
    
    '------------------------------------------------------------------------------
    'Callback Name: ok_cb
    '------------------------------------------------------------------------------
    Public Function ok_cb() As Integer

        Dim errorCode As Integer = 0

        Try

            '---- Enter your callback code here -----
            errorCode = apply_cb()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

        ok_cb = errorCode

    End Function
    
    '------------------------------------------------------------------------------
    'Callback Name: filter_cb
    '------------------------------------------------------------------------------
    Public Function filter_cb(ByVal block As NXOpen.BlockStyler.UIBlock, ByVal selectedObject As NXOpen.TaggedObject) As Integer

        Dim accept As Integer = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT

        Try

            If block Is edgeSelect Then

                'Edge Select Filter
                If faceToggle.GetProperties().GetLogical("Value") Then
                    accept = faceFilter(CType(selectedObject, Edge))
                End If

            ElseIf block Is chamferSelect Then

                'Feature Selection Filter - limit selection to chamfer features
                Dim featureObject As Feature = CType(selectedObject, Feature)

                If featureObject.FeatureType = "CHAMFER" Then
                    accept = angleFilter(CType(featureObject, Features.Chamfer))
                Else
                    accept = NXOpen.UF.UFConstants.UF_UI_SEL_REJECT
                End If

            End If

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)

        End Try
        filter_cb = accept
    End Function


    '**********************************************************************************************************
    'FACE FILTER

    Function faceFilter(ByVal selectedEdge As Edge) As Integer
        Dim accept As Integer = NXOpen.UF.UFConstants.UF_UI_SEL_REJECT

        'If a limiting face has not been established...
        '  then use the first two selected edges to establish the limiting face 
        '  otherwise use the limiting face

        If limitingFace Is Nothing Then

            Dim edgeSelectProps As PropertyList = edgeSelect.GetProperties()
            'Limit faces to those of the first selected edge
            Dim edges() As TaggedObject = edgeSelectProps.GetTaggedObjectVector("SelectedObjects")
            edgeSelectProps.Dispose()
            edgeSelectProps = Nothing

            If edges.Length < 1 Then
                accept = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
            ElseIf edges.Length = 1 Then
                If sharedFace(CType(edges(0), Edge), selectedEdge) IsNot Nothing Then
                    accept = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
                End If
            End If

        Else

            'Limit the edges to just those of the limiting face
            For Each faceObject As Face In selectedEdge.GetFaces()
                If faceObject Is limitingFace Then
                    accept = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
                    Exit For
                End If
            Next faceObject

        End If

        faceFilter = accept
    End Function

    '**********************************************************************************************************
    'ANGLE FILTER

    Function angleFilter(ByVal chamferFeature As Features.Chamfer) As Integer
        Dim accept As Integer = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT

        'If the angle filter toggle is ON...
        '  then only accept chamfers of the limiting angle

        If angleToggle.GetProperties().GetLogical("Value") Then
            Dim workPart As Part = theSession.Parts.Work
            Dim chamferBuilder As Features.ChamferBuilder

            chamferBuilder = workPart.Features.CreateChamferBuilder(chamferFeature)

            If chamferBuilder.AngleExp.Value <> angleLimitDouble.GetProperties().GetDouble("Value") Then
                accept = NXOpen.UF.UFConstants.UF_UI_SEL_REJECT
            End If

            chamferBuilder.Destroy()
        End If

        angleFilter = accept
    End Function

    '**********************************************************************************************************
    'SHARED FACE - return face shared between two edges
    Function sharedFace(ByVal edge1 As Edge, ByVal edge2 As Edge) As Face
        Dim foundFace As Face = Nothing

        For Each face1 As Face In edge1.GetFaces()

            For Each face2 As Face In edge2.GetFaces()
                If face1 Is face2 Then
                    foundFace = face1
                    Exit For
                End If
            Next face2

            If foundFace IsNot Nothing Then Exit For
        Next face1

        Return foundFace
    End Function

    '**********************************************************************************************************
    'ADD CHAMFER FEATURE of given angle to given edge

    Sub addChamfer(ByVal selectedEdge As Edge, ByVal angle As Double)

        Dim chamferBuilder1 As Features.ChamferBuilder = Nothing

        Try
            Dim workPart As Part = theSession.Parts.Work
            Dim nullFeatures_Feature As Features.Feature = Nothing

            chamferBuilder1 = workPart.Features.CreateChamferBuilder(nullFeatures_Feature)

            chamferBuilder1.Option = Features.ChamferBuilder.ChamferOption.OffsetAndAngle
            chamferBuilder1.Method = Features.ChamferBuilder.OffsetMethod.EdgesAlongFaces

            chamferBuilder1.FirstOffset = "15"
            chamferBuilder1.SecondOffset = "15"
            chamferBuilder1.Angle = angle.ToString
			chamferBuilder1.Tolerance = 0.0254

            Dim nullEdge As Edge = Nothing
            Dim edgeTangentRule1 As EdgeTangentRule

            edgeTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeTangent(selectedEdge, nullEdge, False, 0.5, False)

            Dim rules1(0) As SelectionIntentRule
            rules1(0) = edgeTangentRule1

            Dim scCollector1 As ScCollector
            scCollector1 = workPart.ScCollectors.CreateCollector()

            scCollector1.ReplaceRules(rules1, False)

            chamferBuilder1.SmartCollector = scCollector1

            Dim feature1 As Features.Feature
            feature1 = chamferBuilder1.CommitFeature()

        Catch ex As Exception
            Throw ex
        Finally
            If Not chamferBuilder1 Is Nothing Then
                chamferBuilder1.Destroy()
            End If
        End Try

    End Sub

    '**********************************************************************************************************
    'DELETE OBJECT - add the given object to the delete list

    Private Function deleteObject(ByVal selectedObject As NXObject) As Integer

        deleteObject = 0

        Try
            Dim obj(0) As NXObject

            obj(0) = selectedObject

            Dim nErrs As Integer = theSession.UpdateManager.AddToDeleteList(obj)

            'Report any errors - normally the error list should be scanned and each error processed
            If nErrs > 0 Then
                deleteObject = 1
                theUI.NXMessageBox.Show("Add To Delete Errors", NXMessageBox.DialogType.Error, "nErrs = " & nErrs.ToString)
            End If
        Catch ex As Exception
            Throw ex
        End Try

    End Function


End Class
