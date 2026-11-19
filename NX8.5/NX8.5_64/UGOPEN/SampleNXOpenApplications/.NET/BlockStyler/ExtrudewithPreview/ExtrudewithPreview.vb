'=============================================================================
'
'                   Copyright (c) 2008 UGS PLM Solutions
'                    Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for Block Styler
'===============================================================================
'

'==============================================================================
'  WARNING!!  This file is overwritten by the Block Styler while generating
'  the automation code. Any modifications to this file will be lost after
'  generating the code again.
'
'==============================================================================

Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.BlockStyler

'------------------------------------------------------------------------------
'Represents Block Styler application class
'------------------------------------------------------------------------------
Public Class extrudewithpreview
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Public Shared theextrudewithpreview As extrudewithpreview
    Private theDialogName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private SectionGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private SectionToExtrude As NXOpen.BlockStyler.UIBlock' Block type: Section Builder
    Private DirectionGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private DirectionToExtrude As NXOpen.BlockStyler.UIBlock' Block type: Specify Vector
    Private LimitsGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private StartLimit As NXOpen.BlockStyler.UIBlock' Block type: Double
    Private EndLimit As NXOpen.BlockStyler.UIBlock' Block type: Double
    Private PreviewGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private PreviewToggle As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private ResultButton As NXOpen.BlockStyler.UIBlock ' Block type: Button

    Dim workPart As Part
    Dim displayPart As Part
    Dim vectCol(-1) As TaggedObject
    Dim extrudedirection As Direction
    Dim tagobjarray(-1) As TaggedObject
    Dim feature1 As Features.Feature
    Dim isfeaturecreated As Boolean
    Dim preview As Boolean
    Dim markId1 As Session.UndoMarkId
    Dim startvalueofext As Double
    Dim endvalueofext As Double
    Dim directiontoset As Direction
    Dim value As Boolean
	Dim Translucency1 As Boolean
 
#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
        
            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDialogName = "ExtrudewithPreview.dlx"
            theDialog = theUI.CreateDialog(theDialogName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddUpdateHandler(AddressOf update_cb)
            theDialog.AddInitializeHandler(AddressOf initialize_cb)
            theDialog.AddDialogShownHandler(AddressOf dialogShown_cb)
        
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
        
            theextrudewithpreview = New extrudewithpreview()
            ' The following method shows the dialog immediately
            theextrudewithpreview.Show()
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            theextrudewithpreview.Dispose()
        End Try
    End Sub

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
			theUI.VisualizationVisualPreferences.Translucency = Translucency1
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
        
            SectionGroup = theDialog.TopBlock.FindBlock("SectionGroup")
            SectionToExtrude = theDialog.TopBlock.FindBlock("SectionToExtrude")
            DirectionGroup = theDialog.TopBlock.FindBlock("DirectionGroup")
            DirectionToExtrude = theDialog.TopBlock.FindBlock("DirectionToExtrude")
            LimitsGroup = theDialog.TopBlock.FindBlock("LimitsGroup")
            StartLimit = theDialog.TopBlock.FindBlock("StartLimit")
            EndLimit = theDialog.TopBlock.FindBlock("EndLimit")
            PreviewGroup = theDialog.TopBlock.FindBlock("PreviewGroup")
            PreviewToggle = theDialog.TopBlock.FindBlock("PreviewToggle")
            ResultButton = theDialog.TopBlock.FindBlock("ResultButton")

            Dim Endlimitproplist As PropertyList = EndLimit.GetProperties
            Endlimitproplist.SetDouble("Value", 36.0)
            Endlimitproplist.Dispose()
            Endlimitproplist = Nothing

            feature1 = Nothing
            isfeaturecreated = False
            Array.Resize(tagobjarray, 0)
            Array.Resize(vectCol, 0)

            workPart = theSession.Parts.Work
            displayPart = theSession.Parts.Display
            value = True
			
			Translucency1 = theUI.VisualizationVisualPreferences.Translucency
            theUI.VisualizationVisualPreferences.Translucency = True

        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'Callback Name: dialogShown_cb
    'This callback is executed just before the dialog launch. Thus any value set 
    'here will take precedence and dialog will be launched showing that value. 
    '------------------------------------------------------------------------------
    Public Sub dialogShown_cb()
        Try
        
            '---- Enter your callback code here -----
        
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

            '---- Enter your callback code here -----
            showOrCreate(0)

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

        apply_cb = errorCode

    End Function
    
    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try
        
            If block Is SectionToExtrude Then
                '---- Enter your code here -----

                Dim SectionToExtrudeproplist As PropertyList = SectionToExtrude.GetProperties
                tagobjarray = SectionToExtrudeproplist.GetTaggedObjectVector("SelectedObjects")
                SectionToExtrudeproplist.Dispose()
                SectionToExtrudeproplist = Nothing

                Dim PreviewToggleproplist As PropertyList = PreviewToggle.GetProperties
                preview = PreviewToggleproplist.GetLogical("Value")
                PreviewToggleproplist.Dispose()
                PreviewToggleproplist = Nothing

                createextrude()
            
            ElseIf block Is DirectionToExtrude Then
                '---- Enter your code here -----
                Dim DirectionToExtrudeproplist As PropertyList = DirectionToExtrude.GetProperties
                vectCol = DirectionToExtrudeproplist.GetTaggedObjectVector("SelectedObjects")
                DirectionToExtrudeproplist.Dispose()
                DirectionToExtrudeproplist = Nothing

                Dim PreviewToggleproplist As PropertyList = PreviewToggle.GetProperties
                preview = PreviewToggleproplist.GetLogical("Value")
                PreviewToggleproplist.Dispose()
                PreviewToggleproplist = Nothing

                extrudedirection = CType(vectCol(0), Direction)

                directiontoset = extrudedirection

                createextrude()
            
            ElseIf block Is StartLimit Then
                '---- Enter your code here -----

                Dim PreviewToggleproplist As PropertyList = PreviewToggle.GetProperties
                preview = PreviewToggleproplist.GetLogical("Value")
                PreviewToggleproplist.Dispose()
                PreviewToggleproplist = Nothing

                Dim StartLimitproplist As PropertyList = StartLimit.GetProperties
                startvalueofext = StartLimitproplist.GetDouble("Value").ToString
                StartLimitproplist.Dispose()
                StartLimitproplist = Nothing

                createextrude()
            
            ElseIf block Is EndLimit Then
                '---- Enter your code here -----

                Dim PreviewToggleproplist As PropertyList = PreviewToggle.GetProperties
                preview = PreviewToggleproplist.GetLogical("Value")
                PreviewToggleproplist.Dispose()
                PreviewToggleproplist = Nothing

                Dim EndLimitproplist As PropertyList = EndLimit.GetProperties
                endvalueofext = EndLimitproplist.GetDouble("Value").ToString
                EndLimitproplist.Dispose()
                EndLimitproplist = Nothing

                createextrude()
            
            ElseIf block Is PreviewToggle Then
                '---- Enter your code here -----

                Dim PreviewToggleproplist As PropertyList = PreviewToggle.GetProperties
                preview = PreviewToggleproplist.GetLogical("Value")
                PreviewToggleproplist.Dispose()
                PreviewToggleproplist = Nothing

                createextrude()
            
            ElseIf block Is ResultButton Then
                '---- Enter your code here -----

                createextrude()

                If value = True Then

                    setboolean(False)
                    Dim ResultButtonproplist As PropertyList = ResultButton.GetProperties
                    ResultButtonproplist.SetString("Bitmap", "undo")
                    ResultButtonproplist.SetString("Label", "Undo result")
                    ResultButtonproplist.Dispose()
                    ResultButtonproplist = Nothing

                    showOrCreate(0)

                End If

                If value = False Then
                    setboolean(True)
                    Dim ResultButtonproplist As PropertyList = ResultButton.GetProperties
                    ResultButtonproplist.SetString("Bitmap", "general_preview")
                    ResultButtonproplist.SetString("Label", "Show Result")
                    ResultButtonproplist.dispose()
                    ResultButtonproplist = Nothing

                    If Not feature1 Is Nothing Then

                        visibility()

                    End If

                End If
                value = Not value
            End If


        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        update_cb = 0
    End Function

    Public Sub createextrude()

        If tagobjarray.Length > 0 And vectCol.Length > 0 Then

            If isfeaturecreated = True Then
                redefinefeature()
                Exit Sub
            End If

            Dim nullFeatures_Feature As Features.Feature = Nothing

            Dim extrudeBuilder1 As Features.ExtrudeBuilder
            extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(nullFeatures_Feature)

            extrudeBuilder1.DistanceTolerance = 0.0254

            extrudeBuilder1.Direction = extrudedirection

            Dim StartLimitproplist As PropertyList = StartLimit.GetProperties
            Dim starvalueofext As Integer = StartLimitproplist.GetDouble("Value")
            StartLimitproplist.Dispose()
            StartLimitproplist = Nothing

            extrudeBuilder1.Limits.StartExtend.Value.RightHandSide = (starvalueofext.ToString)

            Dim EndLimitproplist As PropertyList = EndLimit.GetProperties
            Dim endvalueofext As Integer = EndLimitproplist.GetDouble("Value")
            EndLimitproplist.Dispose()
            EndLimitproplist = Nothing

            extrudeBuilder1.Limits.EndExtend.Value.RightHandSide = (endvalueofext.ToString)

            extrudeBuilder1.Section = CType(tagobjarray(0), Section)

            feature1 = extrudeBuilder1.CommitFeature()

            extrudeBuilder1.Destroy()

            workPart.FacetedBodies.DeleteTemporaryFacesAndEdges()

            isfeaturecreated = True

            visibility()

        End If

    End Sub

    Public Sub redefinefeature()

        Dim extrude1 As Features.Extrude = CType(feature1, Features.Extrude)

        Dim extrudeBuilder2 As Features.ExtrudeBuilder
        extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(extrude1)

        extrudeBuilder2.DistanceTolerance = 0.0254

        extrudeBuilder2.Direction = extrudedirection

        Dim StartLimitproplist As PropertyList = StartLimit.GetProperties
        Dim starvalueofext As Integer = StartLimitproplist.GetDouble("Value")
        StartLimitproplist.Dispose()
        StartLimitproplist = Nothing

        extrudeBuilder2.Limits.StartExtend.Value.RightHandSide = (starvalueofext.ToString)

        Dim EndLimitproplist As PropertyList = EndLimit.GetProperties
        Dim endvalueofext As Integer = EndLimitproplist.GetDouble("Value")
        EndLimitproplist.Dispose()
        EndLimitproplist = Nothing

        extrudeBuilder2.Limits.EndExtend.Value.RightHandSide = (endvalueofext.ToString)

        extrudeBuilder2.Section = CType(tagobjarray(0), Section)

        markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start Extrude")

        feature1 = extrudeBuilder2.CommitFeature()

        extrudeBuilder2.Destroy()

        workPart.FacetedBodies.DeleteTemporaryFacesAndEdges()

        theSession.UpdateManager.DoUpdate(markId1)

        theSession.DeleteUndoMark(markId1, Nothing)

        visibility()

    End Sub

    Public Sub visibility()

        If preview = True Then

            Dim bodyfeat As Features.BodyFeature = CType(feature1, Features.BodyFeature)
            Dim numofbodies() As Body = bodyfeat.GetBodies()

            Dim displayModification1 As DisplayModification
            displayModification1 = theSession.DisplayManager.NewDisplayModification()

            displayModification1.ApplyToAllFaces = True

            displayModification1.NewTranslucency = 80

            Dim objects1(numofbodies.Length - 1) As DisplayableObject

            For i As Integer = 0 To numofbodies.Length - 1
                objects1(i) = numofbodies(i)
            Next

            displayModification1.Apply(objects1)
            workPart.ModelingViews.WorkView.RenderingStyle = View.RenderingStyleType.ShadedWithEdges
        End If

        If preview = False Then

            Dim bodyfeat As Features.BodyFeature = CType(feature1, Features.BodyFeature)
            Dim numofbodies() As Body = bodyfeat.GetBodies()

            Dim displayModification1 As DisplayModification

            displayModification1 = theSession.DisplayManager.NewDisplayModification()

            displayModification1.ApplyToAllFaces = True

            displayModification1.NewTranslucency = 100

            Dim objects1(numofbodies.Length - 1) As DisplayableObject

            For i As Integer = 0 To numofbodies.Length - 1
                objects1(i) = numofbodies(i)
            Next

            displayModification1.Apply(objects1)
            workPart.ModelingViews.WorkView.RenderingStyle = View.RenderingStyleType.Shaded
        End If
    End Sub

    Public Sub showOrCreate(ByRef transperencyvalue As Integer)

        If Not feature1 Is Nothing Then

            Dim bodyfeat As Features.BodyFeature = CType(feature1, Features.BodyFeature)
            Dim numofbodies() As Body = bodyfeat.GetBodies()

            Dim displayModification1 As DisplayModification
            displayModification1 = theSession.DisplayManager.NewDisplayModification()

            displayModification1.ApplyToAllFaces = True

            displayModification1.NewTranslucency = transperencyvalue

            Dim objects1(numofbodies.Length - 1) As DisplayableObject

            For i As Integer = 0 To numofbodies.Length - 1
                objects1(i) = numofbodies(i)
            Next

            displayModification1.Apply(objects1)
        End If

    End Sub

    Public Sub setboolean(ByRef value As Boolean)

        Dim SectionToExtrudeproplist As PropertyList = SectionToExtrude.GetProperties
        SectionToExtrudeproplist.SetLogical("Enable", value)
        SectionToExtrudeproplist.Dispose()
        SectionToExtrudeproplist = Nothing

        Dim DirectionToExtrudeproplist As PropertyList = DirectionToExtrude.GetProperties
        DirectionToExtrudeproplist.SetLogical("Enable", value)
        DirectionToExtrudeproplist.Dispose()
        DirectionToExtrudeproplist = Nothing

        Dim StartLimitproplist As PropertyList = StartLimit.GetProperties
        StartLimitproplist.SetLogical("Enable", value)
        StartLimitproplist.Dispose()
        StartLimitproplist = Nothing

        Dim EndLimitproplist As PropertyList = EndLimit.GetProperties
        EndLimitproplist.SetLogical("Enable", value)
        EndLimitproplist.Dispose()
        EndLimitproplist = Nothing

        Dim PreviewToggleproplist As PropertyList = PreviewToggle.GetProperties
        PreviewToggleproplist.SetLogical("Enable", value)
        PreviewToggleproplist.Dispose()
        PreviewToggleproplist = Nothing

    End Sub
    
End Class
