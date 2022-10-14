'=============================================================================
'
'                   Copyright (c) 2006 UGS PLM Solutions
'                    Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for UIStyler
'===============================================================================
'
'=============================================================================

'==============================================================================
'Following example demonstrates the Selection capability within UIStyler
'==============================================================================

'==============================================================================
'   WARNING!!  This file is overwritten by the UIStyler each time the Styler
'   file is saved.
'
'       Filename:  UistylerselectionExample.vb
'
'        This file was generated by the NX User Interface Styler
'        Created by: hanmante
'        Version: NX 5
'              Date: 12-13-2006
'              Time: 11:56
'
'   This template file is overwritten each time the UIStyler dialog is
'   saved.  Any modifications to this file will be lost.
'==============================================================================


'==============================================================================
'  Purpose:  This TEMPLATE file contains VB.NET source to guide you in the
'  construction of your NX Open application dialog. The generation of your
'  dialog file (.dlg extension) is the first step towards dialog construction
'  within NX.  You must now create a NX Open application that
'  utilizes this file (.dlg).


'  The information in this file provides you with the following:
'
'  1.  Help on how to load and display your UIStyler dialog in NX
'      using APIs provided in NXOpen.UIStyler namespace
'  2.  The empty callback methods (stubs) associated with your dialog items
'      have also been placed in this file. These empty methods have been
'      created simply to start you along with your coding requirements.
'      The method name, argument list and possible return values have already
'      been provided for you.
'==============================================================================


'------------------------------------------------------------------------------
' These imports are needed for the following template code
'------------------------------------------------------------------------------
Option Strict Off
Imports System
Imports System.Collections
Imports NXOpen
Imports NXOpen.UIStyler


'------------------------------------------------------------------------------
' Represents UI Styler application class
'------------------------------------------------------------------------------
Public Class UistylerselectionExample
    ' class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Public Shared theUistylerselectionExample As UistylerselectionExample
    Private theDialog As Dialog
    Private changeDialog As NXOpen.UIStyler.DialogItem
    Private changeGrBeg1 As NXOpen.UIStyler.GroupBox
    Private changeBitmap1 As NXOpen.UIStyler.BitMap
    Private changeLabel1 As NXOpen.UIStyler.LabelItem
    Private changeStr0 As NXOpen.UIStyler.StringItem
    Private changeCgBeg5 As NXOpen.UIStyler.CollapsibleGroup
    Private changeToggle6 As NXOpen.UIStyler.Toggle
    Private changeReal6 As NXOpen.UIStyler.RealItem
    Public Shared isDisposeCalled As Boolean
    'Following is Hash table which collectes all selected edges of the block
	Dim htEdges As New Hashtable() 


#Region " UI Styler Dialog Designer generator code "
    '------------------------------------------------------------------------------
    ' Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDialog = theUI.Styler.CreateStylerDialog("UistylerselectionExample.dlg")
            InitializeUIStylerDialog()
            isDisposeCalled = False
        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    ' This method is required for UI styler dialog creation
    '------------------------------------------------------------------------------
    Private Sub InitializeUIStylerDialog()
        '------------------------------------------------------------------------------
        ' The following code snippets initializes all the styler items and associate
        ' respective callbacks. Attributes of the styler item can be accessed and
        ' modified only after calling Show() or RegisterWithUiMenu().
        '------------------------------------------------------------------------------
        Try
            changeDialog = theDialog.GetStylerItem("UF_STYLER_DIALOG_INDEX", NXOpen.UIStyler.Dialog.ItemType.DialogItem)
            changeDialog.AddConstructHandler(AddressOf constructor_cb, False)
            changeDialog.AddOkayHandler(AddressOf ok_cb, False)
            changeDialog.AddApplyHandler(AddressOf apply_cb, False)
            changeGrBeg1 = theDialog.GetStylerItem("GR_BEG_1", NXOpen.UIStyler.Dialog.ItemType.GroupBox)
            changeBitmap1 = theDialog.GetStylerItem("BITMAP_1", NXOpen.UIStyler.Dialog.ItemType.Bitmap)
            changeLabel1 = theDialog.GetStylerItem("LABEL_1", NXOpen.UIStyler.Dialog.ItemType.LabelItem)
            changeStr0 = theDialog.GetStylerItem("STR_0", NXOpen.UIStyler.Dialog.ItemType.StringItem)
            changeStr0.AddActivateHandler(AddressOf bend_radius_cb, False)
            changeCgBeg5 = theDialog.GetStylerItem("CG_BEG_5", NXOpen.UIStyler.Dialog.ItemType.CollapsibleGroup)
            changeToggle6 = theDialog.GetStylerItem("TOGGLE_6", NXOpen.UIStyler.Dialog.ItemType.Toggle)
            changeToggle6.AddValueChangedHandler(AddressOf remove_surface_self_intersections_cb, False)
            changeReal6 = theDialog.GetStylerItem("REAL_6", NXOpen.UIStyler.Dialog.ItemType.RealItem)
            changeReal6.AddActivateHandler(AddressOf tolerance_cb, False)
        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
    End Sub

#End Region



    '---------------- DIALOG CREATION FROM A USER EXIT HELP Example ---------------
    ' An example is shown below to create this dialog from a user exit.
    ' All dialog files must be located in
    '             $UGII_USER_DIR/application or
    '             $UGII_SITE_DIR/application or
    '             $UGII_VENDOR_DIR/application directory


    '      1)Add a user exit to the method name below, for example, Main().
    '      2)Consider how your shared library will be unloaded.  Take a look
    '        at the method GetUnloadOption().
    '------------------------------------------------------------------------------
    Public Shared Sub Main()
        Try
            Dim response As NXOpen.UIStyler.DialogResponse
            ' For Journal play back uncommet calls for LockAccess and UnlockAccess
            ' UI.GetUI().LockAccess()
            theUistylerselectionExample = New UistylerselectionExample()
            ' The following method shows the dialog immediately
            response = theUistylerselectionExample.Show()
            theUistylerselectionExample.Dispose()
        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        Finally
            ' theUI.UnlockAccess()
        End Try
    End Sub ' User exit ends

    '------------------------------------------------------------------------------
    ' This method specifies how a shared image is unloaded from memory
    ' within NX. This method gives you the capability to unload an
    ' internal NX Open application or user  exit from NX. Specify any
    ' one of the three constants as a return value to determine the type
    ' of unload to perform:


    '    Immediately : unload the library as soon as the automation program has completed
    '    Explicitly  : unload the library from the "Unload Shared Image" dialog
    '    AtTermination : unload the library when the NX session terminates


    ' NOTE:  A program which associates NX Open applications with the menubar
    ' MUST NOT use this option since it will UNLOAD your NX Open application image
    ' from the menubar.
    '------------------------------------------------------------------------------
    Public Shared Function GetUnloadOption(ByVal arg As String) As Integer
        ' Return code to indicate this library can be unloaded
        ' by the user.
        ' Return CType(Session.LibraryUnloadOption.Explicitly, Integer)
        Return CType(Session.LibraryUnloadOption.Immediately, Integer)
        ' Return CType(Session.LibraryUnloadOption.AtTermination, Integer)
    End Function

    '------------------------------------------------------------------------------
    ' Following method cleanup any housekeeping chores that may be needed.
    ' This method is automatically called by NX.
    '------------------------------------------------------------------------------
    Public Shared Function UnloadLibrary(ByVal arg As String) As Integer
        Try
            theUistylerselectionExample.Dispose()
            Return 0
        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
    End Function

    '------------------------------------------------------------------------------
    ' This method shows the dialog on the screen
    '------------------------------------------------------------------------------
    Public Function Show() As NXOpen.UIStyler.DialogResponse
        Try
            Show = theDialog.Show()
        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
    End Function


    '------------------------------------------------------------------------------
    ' Following method disposes all the class members
    '------------------------------------------------------------------------------
    Sub Dispose()
        Try
            If (isDisposeCalled = False) Then
                changeDialog.Dispose()
                changeGrBeg1.Dispose()
                changeBitmap1.Dispose()
                changeLabel1.Dispose()
                changeStr0.Dispose()
                changeCgBeg5.Dispose()
                changeToggle6.Dispose()
                changeReal6.Dispose()
                theDialog.Dispose()
            End If
            isDisposeCalled = True
        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    '------------------------- UIStyler Callback Functions ------------------------
    '------------------------------------------------------------------------------

    'Following is Selection Callback - This function gets invoked whenever all the selected edges are stored in Hash table.

    Public Function sel_cb(ByVal selectedObjects As NXObject(), ByVal deselectedObjects() As NXObject, ByVal selectHandle As SelectionHandle) As Integer
        Try

            For Each selObj As NXObject In selectedObjects
                htEdges.Add(selObj.JournalIdentifier, selObj)
            Next
            For Each deselObj As NXObject In deselectedObjects
                htEdges.Remove(deselObj.JournalIdentifier)
            Next

            changeLabel1.SetLabel("Select Edges (" & htEdges.Count & ")")

        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            MsgBox(ex.Message)
        End Try
        sel_cb = NXOpen.UIStyler.DialogState.ContinueDialog
    End Function

    'Following is Filter Callback - This function gets invoked during selection. 
	'Here, we can put a logic to accept or reject the selected entities. In this example "Edge * 6 *1" is rejected.

    Public Function filter_cb(ByVal selectedObject As NXOpen.NXObject, ByVal selectionMask_array As NXOpen.Selection.MaskTriple, ByVal selectHandle As SelectionHandle) As Integer
        Try
            If String.Compare(selectedObject.JournalIdentifier, "EDGE * 6 * 1") = 0 Then
                filter_cb = NXOpen.UF.UFConstants.UF_UI_SEL_REJECT
            Else
                filter_cb = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
            End If
        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            MsgBox(ex.Message)
        End Try
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: constructor_cb
    ' Following callback is associated with the "changeDialog" Styler item.
    ' Input: eventObject - object of UIStyler.StylerEvent class
    '------------------------------------------------------------------------------
    Public Function constructor_cb(ByVal eventObject As NXOpen.UIStyler.StylerEvent) As NXOpen.UIStyler.DialogState
        Try


            'Get the selection handle
            Dim selectH As SelectionHandle
            selectH = changeDialog.GetSelectionHandle()

            Dim selectionMask_array(0) As NXOpen.Selection.MaskTriple
            With selectionMask_array(0)
                .Type = NXOpen.UF.UFConstants.UF_solid_type
                .Subtype = NXOpen.UF.UFConstants.UF_solid_edge_subtype
                .SolidBodySubtype = NXOpen.UF.UFConstants.UF_UI_SEL_FEATURE_ANY_EDGE
            End With

            'Following sets the Selection mask for Edge
            UI.GetUI().SelectionManager.SetSelectionMask(selectH, NXOpen.Selection.SelectionAction.ClearAndEnableSpecific, selectionMask_array)

            'Following sets the Selection and Filter callbacks which are invoked during selection			
            UI.GetUI().SelectionManager.SetSelectionCallbacks(selectH, AddressOf filter_cb, AddressOf sel_cb)

            'UI.GetUI().SelectionManager.SetSelectProcedures(selectH, Nothing, AddressOf sel_cb)
            'Remove Surface Self-Intersections
            changeToggle6.ItemValue = True
            '****************************************************************
            'New .NET generated code to "Set the default Blend radius"
            '****************************************************************
            changeStr0.ItemValue = "5.0"
            '****************************************************************
            'Equivalent C code to "Set the default Blend radius"
            '****************************************************************
            'UF_STYLER_item_value_type_t data;
            'data.item_id="String_1";
            'data.item_attr=UF_STYLER_VALUE;
            'data.value.string = "5.0";
            'retcode =UF_STYLER_set_value(dialog_id,&data); 
            '****************************************************************
            'Set the Default lable
            changeLabel1.SetLabel("Select Edges (0)")
            constructor_cb = UIStyler.DialogState.ContinueDialog


        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
        ' Callback acknowledged, do not terminate dialog
        constructor_cb = NXOpen.UIStyler.DialogState.ContinueDialog
        ' A return value of NXOpen.UIStyler.DialogState.ExitDialog will not be accepted
        ' for this callback type. You must continue dialog construction.
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: ok_cb
    ' Following callback is associated with the "changeDialog" Styler item.
    ' Input: eventObject - object of UIStyler.StylerEvent class
    '------------------------------------------------------------------------------
    Public Function ok_cb(ByVal eventObject As NXOpen.UIStyler.StylerEvent) As NXOpen.UIStyler.DialogState
        Try


            apply_cb(eventObject)



        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
        ' Callback acknowledged, terminate dialog
        ' It is STRONGLY recommanded that you exit your
        ' callback with NXOpen.UIStyler.DialogState.ExitDialog in a ok callback.
        ok_cb = NXOpen.UIStyler.DialogState.ExitDialog
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: apply_cb
    ' Following callback is associated with the "changeDialog" Styler item.
    ' Input: eventObject - object of UIStyler.StylerEvent class
    '------------------------------------------------------------------------------

    'Following is Apply Callback - This function is responsible for creating Edge Blend.

    Public Function apply_cb(ByVal eventObject As NXOpen.UIStyler.StylerEvent) As NXOpen.UIStyler.DialogState
        Try

            Dim workPart As Part = theSession.Parts.Work
            Dim displayPart As Part = theSession.Parts.Display

            ' ----------------------------------------------
            '   Menu: Insert->Detail Feature->Edge Blend...
            ' ----------------------------------------------
            Dim markId1 As Session.UndoMarkId
            markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

            Dim nullFeatures_Feature As Features.Feature = Nothing

            Dim edgeBlendBuilder1 As Features.EdgeBlendBuilder
            edgeBlendBuilder1 = workPart.Features.CreateEdgeBlendBuilder(nullFeatures_Feature)

            theSession.SetUndoMarkName(markId1, "Edge Blend")

            Dim featureAlerts1 As Boolean
            featureAlerts1 = theSession.Preferences.Modeling.FeatureAlerts

            Dim scCollector1 As ScCollector
            scCollector1 = workPart.ScCollectors.CreateCollector()

            Dim block1 As Features.Block = CType(workPart.Features.FindObject("BLOCK(1)"), Features.Block)

            Dim featureAlerts2 As Boolean
            featureAlerts2 = theSession.Preferences.Modeling.FeatureAlerts

            Dim featureAlerts3 As Boolean
            featureAlerts3 = theSession.Preferences.Modeling.FeatureAlerts

            Dim seedEdges1(htEdges.Count - 1) As Edge
            Dim en As IDictionaryEnumerator = htEdges.GetEnumerator
            Dim EdgeIndex As Integer
            EdgeIndex = 0
            While en.MoveNext
                Dim edgeVar As Edge = CType(en.Value, Edge)
                seedEdges1(EdgeIndex) = edgeVar
                EdgeIndex += 1
            End While



            Dim edgeMultipleSeedTangentRule2 As EdgeMultipleSeedTangentRule
            edgeMultipleSeedTangentRule2 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges1, 0.5, True)
            Dim rules2(0) As SelectionIntentRule
            rules2(0) = edgeMultipleSeedTangentRule2
            scCollector1.ReplaceRules(rules2, False)
            Dim featureAlerts4 As Boolean
            featureAlerts4 = theSession.Preferences.Modeling.FeatureAlerts
            Dim featureAlerts5 As Boolean
            featureAlerts5 = theSession.Preferences.Modeling.FeatureAlerts
            Dim markId2 As Session.UndoMarkId
            markId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Edge Blend")
			'Following can set the Tolerance for Edge Blend.
			edgeBlendBuilder1.Tolerance = changeReal6.ItemValue 
            edgeBlendBuilder1.AllInstancesOption = False
			'Following can set the Remove Self Intersection option for the Edge Blend.
			edgeBlendBuilder1.RemoveSelfIntersection = changeToggle6.ItemValue
            edgeBlendBuilder1.ConvexConcaveY = False
            edgeBlendBuilder1.RollOverSmoothEdge = True
            edgeBlendBuilder1.RollOntoEdge = True
            edgeBlendBuilder1.MoveSharpEdge = True
            edgeBlendBuilder1.OverlapOption = Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
            edgeBlendBuilder1.BlendOrder = Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
            edgeBlendBuilder1.SetbackOption = Features.EdgeBlendBuilder.Setback.SeparateFromCorner

            'Following sets the value for Blend Radius.
			Dim csIndex1 As Integer
            csIndex1 = edgeBlendBuilder1.AddChainset(scCollector1, changeStr0.ItemValue)

            Dim feature1 As Features.Feature
            feature1 = edgeBlendBuilder1.CommitFeature()

            theSession.DeleteUndoMark(markId2, Nothing)
            edgeBlendBuilder1.Destroy()
            htEdges.Clear()

            changeLabel1.SetLabel("Select Edges (0)")

        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
        ' Callback acknowledged, do not terminate dialog
        ' A return value of NXOpen.UIStyler.DialogState.ExitDialog will not be accepted
        ' for this callback type. You must respond to your apply button.
        apply_cb = NXOpen.UIStyler.DialogState.ContinueDialog
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: bend_radius_cb
    ' Following callback is associated with the "changeStr0" Styler item.
    ' Input: eventObject - object of UIStyler.StylerEvent class
    '------------------------------------------------------------------------------
    Public Function bend_radius_cb(ByVal eventObject As NXOpen.UIStyler.StylerEvent) As NXOpen.UIStyler.DialogState
        Try


            ' ---- Enter your callback code here -----


        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
        ' Callback acknowledged, do not terminate dialog
        bend_radius_cb = NXOpen.UIStyler.DialogState.ContinueDialog
        ' or Callback acknowledged, terminate dialog.
        ' bend_radius_cb = NXOpen.UIStyler.DialogState.ExitDialog
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: remove_surface_self_intersections_cb
    ' Following callback is associated with the "changeToggle6" Styler item.
    ' Input: eventObject - object of UIStyler.StylerEvent class
    '------------------------------------------------------------------------------
    Public Function remove_surface_self_intersections_cb(ByVal eventObject As NXOpen.UIStyler.StylerEvent) As NXOpen.UIStyler.DialogState
        Try


            ' ---- Enter your callback code here -----


        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
        ' Callback acknowledged, do not terminate dialog
        remove_surface_self_intersections_cb = NXOpen.UIStyler.DialogState.ContinueDialog
        ' or Callback acknowledged, terminate dialog.
        ' remove_surface_self_intersections_cb = NXOpen.UIStyler.DialogState.ExitDialog
    End Function

    '------------------------------------------------------------------------------
    ' Callback Name: tolerance_cb
    ' Following callback is associated with the "changeReal6" Styler item.
    ' Input: eventObject - object of UIStyler.StylerEvent class
    '------------------------------------------------------------------------------
    Public Function tolerance_cb(ByVal eventObject As NXOpen.UIStyler.StylerEvent) As NXOpen.UIStyler.DialogState
        Try


            ' ---- Enter your callback code here -----


        Catch ex As NXException
            ' ---- Enter your exception handling code here -----
            ' theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message)
        End Try
        ' Callback acknowledged, do not terminate dialog
        tolerance_cb = NXOpen.UIStyler.DialogState.ContinueDialog
        ' or Callback acknowledged, terminate dialog.
        ' tolerance_cb = NXOpen.UIStyler.DialogState.ExitDialog
    End Function

End Class