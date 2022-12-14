'=============================================================================
'
'                   Copyright (c) 2008 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for Block Styler
'===============================================================================
'

'==============================================================================
'  WARNING!!  This file is overwritten by the Block Styler while generating
'  the automation code. Any modifications to this file will be lost after
'  generating the code again.
'==============================================================================
'------------------------------------------------------------------------------
'These imports are needed for the following template code
'------------------------------------------------------------------------------
Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.BlockStyler

'------------------------------------------------------------------------------
'Represents Block Styler application class
'------------------------------------------------------------------------------
Public Class EditExpression
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Public Shared theEditExpression As EditExpression
    Private theDialogName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private GroupFeatureSelection As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private FeatureList As NXOpen.BlockStyler.SetList' Block type: Set List
    Private GroupExpressionList As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private ButtonGetExpressions As NXOpen.BlockStyler.UIBlock' Block type: Button
    Private ExpressionList As NXOpen.BlockStyler.ListBox' Block type: List Box
    Private GroupExpression As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private ExpressionName As NXOpen.BlockStyler.UIBlock' Block type: String
    Private ExpressionValue As NXOpen.BlockStyler.UIBlock' Block type: Double
    Dim newBlock As BlockStyler.CompositeBlock
    Dim newfeatcol(0) As TaggedObject
    Dim workPart As Part
    Dim exptoedit As Expression
    
#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
        
            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDialogName = "EditExpression.dlx"
            theDialog = theUI.CreateDialog(theDialogName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddUpdateHandler(AddressOf update_cb)
            theDialog.AddInitializeHandler(AddressOf initialize_cb)
            theDialog.AddDialogShownHandler(AddressOf dialogShown_cb)
        
        Catch ex As Exception
        

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

            theEditExpression = New EditExpression()
            ' The following method shows the dialog immediately
            theEditExpression.Show()

        Catch ex As Exception


            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            theEditExpression.Dispose()
        End Try
    End Sub

    Public Shared Function GetUnloadOption(ByVal arg As String) As Integer

        Return CType(Session.LibraryUnloadOption.Immediately, Integer)

    End Function
    '------------------------------------------------------------------------------
    ' Following method cleanup any housekeeping chores that may be needed.
    ' This method is automatically called by NX.
    '------------------------------------------------------------------------------
    Public Shared Function UnloadLibrary(ByVal arg As String) As Integer
        Try

            Return 0

        Catch ex As Exception


            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Function

    '------------------------------------------------------------------------------
    'This method shows the dialog on the screen
    '------------------------------------------------------------------------------
    Public Sub Show()
        Try

            theDialog.Show()

        Catch ex As Exception


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
            workPart = theSession.Parts.Work
            GroupFeatureSelection = theDialog.TopBlock.FindBlock("GroupFeatureSelection")
            FeatureList = CType(theDialog.TopBlock.FindBlock("FeatureList"), NXOpen.BlockStyler.SetList)
            GroupExpressionList = theDialog.TopBlock.FindBlock("GroupExpressionList")
            ButtonGetExpressions = theDialog.TopBlock.FindBlock("ButtonGetExpressions")
            ExpressionList = CType(theDialog.TopBlock.FindBlock("ExpressionList"), NXOpen.BlockStyler.ListBox)
            GroupExpression = theDialog.TopBlock.FindBlock("GroupExpression")
            ExpressionName = theDialog.TopBlock.FindBlock("ExpressionName")
            ExpressionValue = theDialog.TopBlock.FindBlock("ExpressionValue")
            'user defined code
            newBlock = FeatureList.AddNewSet(True)
            FeatureList.SetAddHandler(AddressOf add_handler)
            FeatureList.SetDeleteHandler(AddressOf delete_handler)
            FeatureList.SetReorderObserver(AddressOf reorder_handler)

        Catch ex As Exception


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
        Catch ex As Exception
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'Callback Name: apply_cb
    '------------------------------------------------------------------------------
    Public Function apply_cb() As Integer
        Try


            Dim ExpressionValueProperties As PropertyList = ExpressionValue.getProperties()
            Dim editedvalue As Double = ExpressionValueProperties.GetDouble("Value")
            deletePropertyList(ExpressionValueProperties)

            Dim unit1 As Unit = CType(workPart.UnitCollection.FindObject("MilliMeter"), Unit)

            Dim markId2 As Session.UndoMarkId
            markId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Update Expression Data")

            workPart.Expressions.EditWithUnits(exptoedit, unit1, editedvalue.ToString)

            Dim nErrs1 As Integer
            nErrs1 = theSession.UpdateManager.DoUpdate(markId2)

            theSession.DeleteUndoMark(markId2, "Update Expression Data")

        Catch ex As Exception
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        apply_cb = 0
    End Function

    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try

            If block Is FeatureList Then


                Dim updatedBlock As BlockStyler.CompositeBlock = FeatureList.FindUpdated()

                If Not updatedBlock Is Nothing Then

                    Dim subblock As BlockStyler.UIBlock

                    subblock = updatedBlock.FindBlock("select_feature0")

                    Dim subblockProperties As PropertyList = subblock.GetProperties()

                    If Not subblock Is Nothing Then

                        Dim featcol() As TaggedObject = subblockProperties.GetTaggedObjectVector("SelectedObjects")

                        If featcol.Length > 1 Then

                            newfeatcol(0) = featcol(featcol.Length - 1)
                            subblockProperties.SetTaggedObjectVector("SelectedObjects", newfeatcol)

                        ElseIf featcol.Length = 1 Then

                            newfeatcol(0) = featcol(featcol.Length - 1)

                        End If

                        Dim feature1 As Features.Feature = CType(newfeatcol(0), Features.Feature)
                        Dim str(0) As String

                        str(0) = feature1.JournalIdentifier

                        FeatureList.SetItemText(updatedBlock, str)

                    End If
                    deletePropertyList(subblockProperties)
                End If


            ElseIf block Is ButtonGetExpressions Then


                Dim selectedBlocks() As BlockStyler.UIBlock = FeatureList.GetSelected()
                Dim updatedBlock As BlockStyler.CompositeBlock = selectedBlocks(0)

                If Not updatedBlock Is Nothing Then

                    Dim strings() As String = FeatureList.GetItemText(updatedBlock)
                    Dim feat As Features.Feature = workPart.Features.FindObject(strings(0))
                    Dim allexp() As Expression = feat.GetExpressions()
                    Dim allexpstr(allexp.Length - 1) As String
                    Dim i As Integer = 0

                    For Each exp As Expression In allexp
                        allexpstr(i) = exp.Name & " = " & exp.Value.ToString & " - " & exp.GetDescriptor
                        i = i + 1
                    Next

                    Dim ExpressionListProperties As PropertyList = ExpressionList.getProperties()
                    ExpressionListProperties.SetStrings("ListItems", allexpstr)
                    deletePropertyList(ExpressionListProperties)

                    FeatureList.SetItemText(updatedBlock, strings)
                End If

            ElseIf block Is ExpressionList Then


                Dim ExpressionListProperties As PropertyList = ExpressionList.getProperties()
                Dim str() As String = ExpressionListProperties.GetStrings("ListItems")
                Dim index() As Integer = ExpressionListProperties.GetIntegerVector("SelectedItems")
                deletePropertyList(ExpressionListProperties)

                Dim splitstr() As String = str(index(0)).Split(" ")

                Dim ExpressionNameProperties As PropertyList = ExpressionName.getProperties()
                ExpressionNameProperties.SetString("Value", splitstr(0))
                deletePropertyList(ExpressionNameProperties)

                exptoedit = workPart.Expressions.FindObject(splitstr(0))

                Dim ExpressionValueProperties As PropertyList = ExpressionValue.getProperties()
                ExpressionValueProperties.SetDouble("Value", exptoedit.Value)
                deletePropertyList(ExpressionValueProperties)


            End If

        Catch ex As Exception
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        update_cb = 0
    End Function
    '------------------------------------------------------------------------------
    '----------------------------User defined Functions----------------------------
    '------------------------------------------------------------------------------
    Private Function add_handler(ByVal list As SetList) As Integer

        Dim newItem As UIBlock = list.AddNewSet(True)
        Return 0

    End Function
    
    Private Function delete_handler(ByVal list As SetList, ByVal doomed As UIBlock) As Integer

        MsgBox("Control is in delete_handler function")
        Return 0

    End Function

    Private Function reorder_handler(ByVal list As SetList, ByVal moved As UIBlock, ByVal oldPos As Integer, ByVal newPos As Integer) As Integer

        MsgBox("Moved list item no." & oldPos + 1 & " from " & oldPos + 1 & " to " & newPos + 1 & ".")
        Return 0

    End Function
    Private Sub deletePropertyList(ByRef prop As PropertyList)

        prop.Dispose()
        prop = Nothing

    End Sub
End Class

