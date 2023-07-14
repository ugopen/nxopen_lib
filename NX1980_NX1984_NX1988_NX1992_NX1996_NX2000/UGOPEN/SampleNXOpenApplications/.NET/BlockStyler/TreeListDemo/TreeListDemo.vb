'=============================================================================
'
'                   Copyright (c) 2009 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for Block Styler
'===============================================================================
'

'  WARNING!!  This file is overwritten by the Block Styler while generating
'  the automation code. Any modifications to this file will be lost after
'  generating the code again.

'==============================================================================

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

'------------------------------------------------------------------------------
'Represents Block Styler application class
'------------------------------------------------------------------------------
Public Class TreeListDemo
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Public Shared theTreeListDemo As TreeListDemo
    Private theDialogName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private group0 As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private tree_control0 As NXOpen.BlockStyler.Tree' Block type: Tree Control
    Private addDeleteNodeGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private nodeString As NXOpen.BlockStyler.UIBlock' Block type: String
    Private addNodeButton As NXOpen.BlockStyler.UIBlock' Block type: Button
    Private deleteNodeButton As NXOpen.BlockStyler.UIBlock' Block type: Button
    Private stateIconGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private stateIconOptions As NXOpen.BlockStyler.UIBlock' Block type: Enumeration
    Private nodeToolTip As NXOpen.BlockStyler.UIBlock' Block type: String
    Private NodeEditGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private nodeEditOptions As NXOpen.BlockStyler.UIBlock' Block type: Enumeration
    Private menuGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private showMenuToggle As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private dragDropGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private disallowDragToggle As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private dropOptions As NXOpen.BlockStyler.UIBlock ' Block type: Enumeration
    Private defaultActionGroup As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private defaultActionToggle As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private nodeDataGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private instructions As NXOpen.BlockStyler.UIBlock' Block type: Multiline String
    Private selection0 As NXOpen.BlockStyler.UIBlock' Block type: Selection
    Private addCrossSelectionNodeButton As NXOpen.BlockStyler.UIBlock' Block type: Button
    Private redrawGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private redrawInstruction As NXOpen.BlockStyler.UIBlock' Block type: Multiline String
    Private redrawToggle As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private listingWindowGroup As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private listingWindowToggle As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    '------------------------------------------------------------------------------
    'Bit Option for Property: SnapPointTypesEnabled
    '------------------------------------------------------------------------------
    Public Shared ReadOnly              SnapPointTypesEnabled_UserDefined =     1
    Public Shared ReadOnly                 SnapPointTypesEnabled_Inferred =     2
    Public Shared ReadOnly           SnapPointTypesEnabled_ScreenPosition =     4
    Public Shared ReadOnly                 SnapPointTypesEnabled_EndPoint =     8
    Public Shared ReadOnly                 SnapPointTypesEnabled_MidPoint =    16
    Public Shared ReadOnly             SnapPointTypesEnabled_ControlPoint =    32
    Public Shared ReadOnly             SnapPointTypesEnabled_Intersection =    64
    Public Shared ReadOnly                SnapPointTypesEnabled_ArcCenter =   128
    Public Shared ReadOnly            SnapPointTypesEnabled_QuadrantPoint =   256
    Public Shared ReadOnly            SnapPointTypesEnabled_ExistingPoint =   512
    Public Shared ReadOnly             SnapPointTypesEnabled_PointonCurve =  1024
    Public Shared ReadOnly           SnapPointTypesEnabled_PointonSurface =  2048
    Public Shared ReadOnly         SnapPointTypesEnabled_PointConstructor =  4096
    Public Shared ReadOnly     SnapPointTypesEnabled_TwocurveIntersection =  8192
    Public Shared ReadOnly             SnapPointTypesEnabled_TangentPoint = 16384
    Public Shared ReadOnly                    SnapPointTypesEnabled_Poles = 32768
    Public Shared ReadOnly         SnapPointTypesEnabled_BoundedGridPoint = 65536
    '------------------------------------------------------------------------------
    'Bit Option for Property: SnapPointTypesOnByDefault
    '------------------------------------------------------------------------------
    Public Shared ReadOnly             SnapPointTypesOnByDefault_EndPoint =     8
    Public Shared ReadOnly             SnapPointTypesOnByDefault_MidPoint =    16
    Public Shared ReadOnly         SnapPointTypesOnByDefault_ControlPoint =    32
    Public Shared ReadOnly         SnapPointTypesOnByDefault_Intersection =    64
    Public Shared ReadOnly            SnapPointTypesOnByDefault_ArcCenter =   128
    Public Shared ReadOnly        SnapPointTypesOnByDefault_QuadrantPoint =   256
    Public Shared ReadOnly        SnapPointTypesOnByDefault_ExistingPoint =   512
    Public Shared ReadOnly         SnapPointTypesOnByDefault_PointonCurve =  1024
    Public Shared ReadOnly       SnapPointTypesOnByDefault_PointonSurface =  2048
    Public Shared ReadOnly     SnapPointTypesOnByDefault_PointConstructor =  4096
    Public Shared ReadOnly     SnapPointTypesOnByDefault_BoundedGridPoint = 65536
    
#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
        
            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDialogName = "TreeListDemo.dlx"
            theDialog = theUI.CreateDialog(theDialogName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddOkHandler(AddressOf ok_cb)
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
    '            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
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
        
            theTreeListDemo = New TreeListDemo()
            ' The following method shows the dialog immediately
            theTreeListDemo.Show()
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            theTreeListDemo.Dispose()
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
    Dim nodeBaseString As String = Nothing
    Dim nodeSuffixNumber As Integer = 0
    Public Sub initialize_cb()
        Try
        
            group0 = CType(theDialog.TopBlock.FindBlock("group0"), NXOpen.BlockStyler.UIBlock)
            tree_control0 = CType(theDialog.TopBlock.FindBlock("tree_control0"), NXOpen.BlockStyler.Tree)
            addDeleteNodeGroup = CType(theDialog.TopBlock.FindBlock("addDeleteNodeGroup"), NXOpen.BlockStyler.UIBlock)
            nodeString = CType(theDialog.TopBlock.FindBlock("nodeString"), NXOpen.BlockStyler.UIBlock)
            addNodeButton = CType(theDialog.TopBlock.FindBlock("addNodeButton"), NXOpen.BlockStyler.UIBlock)
            deleteNodeButton = CType(theDialog.TopBlock.FindBlock("deleteNodeButton"), NXOpen.BlockStyler.UIBlock)
            stateIconGroup = CType(theDialog.TopBlock.FindBlock("stateIconGroup"), NXOpen.BlockStyler.UIBlock)
            stateIconOptions = CType(theDialog.TopBlock.FindBlock("stateIconOptions"), NXOpen.BlockStyler.UIBlock)
            nodeToolTip = CType(theDialog.TopBlock.FindBlock("nodeToolTip"), NXOpen.BlockStyler.UIBlock)
            NodeEditGroup = CType(theDialog.TopBlock.FindBlock("NodeEditGroup"), NXOpen.BlockStyler.UIBlock)
            nodeEditOptions = CType(theDialog.TopBlock.FindBlock("nodeEditOptions"), NXOpen.BlockStyler.UIBlock)
            menuGroup = CType(theDialog.TopBlock.FindBlock("menuGroup"), NXOpen.BlockStyler.UIBlock)
            showMenuToggle = CType(theDialog.TopBlock.FindBlock("showMenuToggle"), NXOpen.BlockStyler.UIBlock)
            dragDropGroup = CType(theDialog.TopBlock.FindBlock("dragDropGroup"), NXOpen.BlockStyler.UIBlock)
            disallowDragToggle = CType(theDialog.TopBlock.FindBlock("disallowDragToggle"), NXOpen.BlockStyler.UIBlock)
            dropOptions = CType(theDialog.TopBlock.FindBlock("dropOptions"), NXOpen.BlockStyler.UIBlock)
            defaultActionGroup = theDialog.TopBlock.FindBlock("defaultActionGroup")
            defaultActionToggle = theDialog.TopBlock.FindBlock("defaultActionToggle")
            nodeDataGroup = CType(theDialog.TopBlock.FindBlock("nodeDataGroup"), NXOpen.BlockStyler.UIBlock)
            instructions = CType(theDialog.TopBlock.FindBlock("instructions"), NXOpen.BlockStyler.UIBlock)
            selection0 = CType(theDialog.TopBlock.FindBlock("selection0"), NXOpen.BlockStyler.UIBlock)
            addCrossSelectionNodeButton = CType(theDialog.TopBlock.FindBlock("addCrossSelectionNodeButton"), NXOpen.BlockStyler.UIBlock)
            redrawGroup = CType(theDialog.TopBlock.FindBlock("redrawGroup"), NXOpen.BlockStyler.UIBlock)
            redrawInstruction = CType(theDialog.TopBlock.FindBlock("redrawInstruction"), NXOpen.BlockStyler.UIBlock)
            redrawToggle = CType(theDialog.TopBlock.FindBlock("redrawToggle"), NXOpen.BlockStyler.UIBlock)
            listingWindowGroup = theDialog.TopBlock.FindBlock("listingWindowGroup")
            listingWindowToggle = theDialog.TopBlock.FindBlock("listingWindowToggle")
            '------------------------------------------------------------------------------
            'Registration of Treelist specific callbacks
            '------------------------------------------------------------------------------
            'tree_control0.SetOnExpandHandler( AddressOf OnExpandCallback )
            
            'tree_control0.SetOnInsertColumnHandler( AddressOf OnInsertColumnCallback )

            tree_control0.SetOnInsertNodeHandler(AddressOf OnInsertNodeCallback)
            
            tree_control0.SetOnDeleteNodeHandler(AddressOf OnDeleteNodeCallback)
            
            'tree_control0.SetOnPreSelectHandler( AddressOf OnPreSelectCallback )
            
            tree_control0.SetOnSelectHandler(AddressOf OnSelectcallback)
            
            tree_control0.SetOnStateChangeHandler(AddressOf OnStateChangecallback)
            
            tree_control0.SetToolTipTextHandler(AddressOf ToolTipTextCallback)
            
            'tree_control0.SetColumnSortHandler( AddressOf ColumnSortCallback )
            
            tree_control0.SetStateIconNameHandler(AddressOf StateIconNameCallback)
            
            tree_control0.SetOnBeginLabelEditHandler(AddressOf OnBeginLabelEdit)
            
            tree_control0.SetOnEndLabelEditHandler(AddressOf OnEndLabelEdit)
            
            tree_control0.SetOnEditOptionSelectedHandler(AddressOf OnEditOptionSelected)
            
            tree_control0.SetAskEditControlHandler(AddressOf AskEditControl)
            
            tree_control0.SetOnMenuHandler(AddressOf OnMenuCallback)
            
            tree_control0.SetOnMenuSelectionHandler(AddressOf OnMenuCommandCallback)
            
            tree_control0.SetIsDropAllowedHandler(AddressOf IsDropAllowedCallback)
            
            tree_control0.SetIsDragAllowedHandler(AddressOf IsDragAllowedCallback)
            
            tree_control0.SetOnDropHandler(AddressOf OnDropCallback)
            
            'tree_control0.SetOnDropMenuHandler(AddressOf OnDropMenuCallback)

            tree_control0.SetOnDefaultActionHandler(AddressOf OnDefaultActionCallback)
            
            '------------------------------------------------------------------------------
            Dim stringPropList As BlockStyler.PropertyList = nodeString.GetProperties()
            nodeBaseString = stringPropList.GetString("Value")
            stringPropList.SetString("Value", nodeBaseString + nodeSuffixNumber.ToString())
            stringPropList.Dispose()


        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    Enum Columns
        ColumnFirst = 0
        ColumnSecond = 1
        ColumnThird = 2
    End Enum

    Private previousAddedNode As BlockStyler.Node = Nothing
    Dim randomIcon As Integer = 0
    Dim randomIconString() As String = {"extrude", "cone", "block", "blend"}

    '------------------------------------------------------------------------------
    'Callback Name: dialogShown_cb
    'This callback is executed just before the dialog launch. Thus any value set 
    'here will take precedence and dialog will be launched showing that value. 
    '------------------------------------------------------------------------------
    Public Sub dialogShown_cb()
        Try
        
            '---- Enter your callback code here -----
            'Insert Columns
            tree_control0.InsertColumn(Columns.ColumnFirst, "First Column", 80)
            tree_control0.InsertColumn(Columns.ColumnSecond, "Second Column", 80)
            tree_control0.InsertColumn(Columns.ColumnThird, "Third Column", 80)

            'Set resize policy for columns
            tree_control0.SetColumnResizePolicy(Columns.ColumnFirst, Tree.ColumnResizePolicy.ConstantWidth)
            tree_control0.SetColumnResizePolicy(Columns.ColumnSecond, Tree.ColumnResizePolicy.ConstantWidth)
            tree_control0.SetColumnResizePolicy(Columns.ColumnThird, Tree.ColumnResizePolicy.ConstantWidth)

            'Let the second column interpret the text as icon
            tree_control0.SetColumnDisplayType(Columns.ColumnSecond, Tree.ColumnDisplay.Icon)
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'Callback Name: apply_cb
    '------------------------------------------------------------------------------
    Public Function apply_cb() As Integer
        Try
        
            '---- Enter your callback code here -----
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        apply_cb = 0
    End Function

    Function CreateAndAddNode(ByVal afterNode As BlockStyler.Node) As BlockStyler.Node

        Dim parentNode As BlockStyler.Node = Nothing
        'Get node display string from the block
        Dim stringPropList As BlockStyler.PropertyList = nodeString.GetProperties()
        Dim nodeDisplayString As String = stringPropList.GetString("Value")
        stringPropList.Dispose()

        Dim node As BlockStyler.Node = tree_control0.CreateNode(nodeDisplayString)

        'Set few properties of node
        node.ForegroundColor = 198
        node.DisplayIcon = randomIconString(randomIcon)
        node.SelectedIcon = "draft"

        'Take first selected node as parent node
        Dim selectedNodes() As BlockStyler.Node = tree_control0.GetSelectedNodes()
        If selectedNodes.Length > 0 Then
            parentNode = selectedNodes(0)
        End If

        'Insert Node
        tree_control0.InsertNode(node, parentNode, afterNode, Tree.NodeInsertOption.Sort)
        node.ScrollTo(Columns.ColumnFirst, BlockStyler.Node.Scroll.Center)

        'Change the last node color. Making sure that new node color is distinct
        If Not previousAddedNode Is Nothing Then
            previousAddedNode.ForegroundColor = 211
        End If
        previousAddedNode = node

        'Assign return value
        CreateAndAddNode = node

    End Function

    Sub WriteCallbackToListingWindow(ByVal callbackName As String)

        Try
            If listingWindowToggle IsNot Nothing Then
                Dim listingWindowToggleProps As BlockStyler.PropertyList = listingWindowToggle.GetProperties()
                Dim listingWindow As Boolean = listingWindowToggleProps.GetLogical("Value")
                listingWindowToggleProps.Dispose()

                If listingWindow Then
                    theSession.ListingWindow().Open()
                    Dim nullString As String = Nothing
                    theSession.ListingWindow().WriteLine(nullString)
                    theSession.ListingWindow().WriteLine(callbackName)
                End If

            End If


        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

    End Sub


    Sub DeleteSelectedNodes()

        Dim selectedNodes() As BlockStyler.Node = tree_control0.GetSelectedNodes()

        While selectedNodes.Length > 0
            tree_control0.DeleteNode(selectedNodes(0))
            selectedNodes = tree_control0.GetSelectedNodes()
        End While

    End Sub
    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try

            If block Is nodeString Then
                '---- Enter your code here -----

            ElseIf block Is addNodeButton Then
                '---- Enter your code here -----

                Dim afterNode As BlockStyler.Node = Nothing

                Dim node As BlockStyler.Node = CreateAndAddNode(afterNode)

                'State Icon
                Dim prop As PropertyList = stateIconOptions.GetProperties()
                Dim enumValue As Integer = prop.GetEnum("Value")
                prop.Dispose()

                If enumValue = 0 Then
                    'Ignore
                ElseIf enumValue = 1 Then
                    node.SetState(1)
                ElseIf enumValue = 2 Then
                    node.SetState(3) 'Set Value other than 1 or 2
                End If

            ElseIf block Is deleteNodeButton Then
                '---- Enter your code here -----
                DeleteSelectedNodes()

            ElseIf block Is stateIconOptions Then
                '---- Enter your code here -----

            ElseIf block Is nodeToolTip Then
                '---- Enter your code here -----

            ElseIf block Is nodeEditOptions Then
                '---- Enter your code here -----
                If defaultActionToggle IsNot Nothing Then

                    Dim nodeEditOptionsProps As BlockStyler.PropertyList = nodeEditOptions.GetProperties()
                    Dim nodeEditOption As String = nodeEditOptionsProps.GetEnumAsString("Value")
                    nodeEditOptionsProps.Dispose()

                    Dim defaultActionToggleProps As BlockStyler.PropertyList = defaultActionToggle.GetProperties()

                    If nodeEditOption.ToString = "Combo Box Edit" Or nodeEditOption.ToString = "Listbox Edit" Then
                        defaultActionToggleProps.SetLogical("Enable", False)
                        defaultActionToggleProps.SetLogical("Value", False)
                    Else
                        defaultActionToggleProps.SetLogical("Enable", True)
                    End If

                    defaultActionToggleProps.Dispose()

                End If

            ElseIf block Is showMenuToggle Then
                '---- Enter your code here -----

            ElseIf block Is disallowDragToggle Then
                '---- Enter your code here -----

            ElseIf block Is dropOptions Then
                '---- Enter your code here -----

            ElseIf block Is defaultActionToggle Then
                '---- Enter your code here -----

            ElseIf block Is instructions Then
                '---- Enter your code here -----

            ElseIf block Is selection0 Then
                '---- Enter your code here -----

            ElseIf block Is addCrossSelectionNodeButton Then
                '---- Enter your code here -----
                'Get the selected object
                Dim prop As PropertyList = selection0.GetProperties()
                Dim objects() As TaggedObject = prop.GetTaggedObjectVector("SelectedObjects")

                If objects.Length > 0 Then
                    'Create node and node data
                    Dim node As BlockStyler.Node = tree_control0.CreateNode("CrossSelection-NodeData")
                    Dim nodeData As DataContainer = node.GetNodeData()
                    nodeData.AddTaggedObject("Data", objects(0))
                    nodeData.Dispose()
                    tree_control0.InsertNode(node, Nothing, Nothing, Tree.NodeInsertOption.AlwaysLast)

                    'Reset Selection block
                    Dim blank(-1) As TaggedObject
                    prop.SetTaggedObjectVector("SelectedObjects", blank)
                End If

                prop.Dispose()

            ElseIf block Is redrawInstruction Then
                '---- Enter your code here -----

            ElseIf block Is redrawToggle Then
                '---- Enter your code here -----
                Dim prop As PropertyList = redrawToggle.GetProperties()
                Dim isRedraw As Boolean = prop.GetLogical("Value")
                prop.Dispose()

                tree_control0.Redraw(isRedraw)

            End If

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
        Try

            '---- Enter your callback code here -----
            apply_cb()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        ok_cb = 0
    End Function

    '------------------------------------------------------------------------------
    'Treelist specific callbacks
    '------------------------------------------------------------------------------
    'Public Sub OnExpandCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node as NXOpen.BlockStyler.Node )
    'End Sub

    'Public Sub OnInsertColumnCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal columnID As Integer)
    'End Sub

    Public Sub OnInsertNodeCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node)
        Try
            WriteCallbackToListingWindow("OnInsertNodeCallback Invoked")

            'Setting random icon
            If randomIcon = 0 Then
                node.SetColumnDisplayText(Columns.ColumnSecond, randomIconString(randomIcon))
            ElseIf randomIcon = 1 Then
                node.SetColumnDisplayText(Columns.ColumnSecond, randomIconString(randomIcon))
            ElseIf randomIcon = 2 Then
                node.SetColumnDisplayText(Columns.ColumnSecond, randomIconString(randomIcon))
            ElseIf randomIcon = 3 Then
                node.SetColumnDisplayText(Columns.ColumnSecond, randomIconString(randomIcon))
            End If

            randomIcon = randomIcon + 1

            If randomIcon > 3 Then
                randomIcon = 0
            End If

            node.SetColumnDisplayText(Columns.ColumnThird, "Column Text - " + randomIcon.ToString())

            If nodeSuffixNumber = 15000 Then
                nodeSuffixNumber = 0
            Else
                nodeSuffixNumber = nodeSuffixNumber + 1
            End If

            'New node text for the next node
            Dim prop As BlockStyler.PropertyList = nodeString.GetProperties()
            prop.SetString("Value", nodeBaseString + nodeSuffixNumber.ToString())
            prop.Dispose()


        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)

        End Try
    End Sub

    Public Sub OnDeleteNodeCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node)
        Try
            WriteCallbackToListingWindow("OnDeleteNodeCallback Invoked")
            If node Is previousAddedNode Then
                'Set the previous node to Nothing. Done for safe execution.
                previousAddedNode = Nothing
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)

        End Try
    End Sub

    'Public Sub OnPreSelectcallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node as NXOpen.BlockStyler.Node , ByVal columnID As Integer, ByVal selected As Boolean)
    'End Sub

    Public Sub OnSelectcallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal columnID As Integer, ByVal selected As Boolean)

        Dim text As String

        If selected = True Then
            text = "OnSelectCallback Invoked: Node """ + node.DisplayText() + """ " + "Selected at column :" + columnID.ToString
        Else
            text = "OnSelectCallback Invoked: Node """ + node.DisplayText() + """ " + "Deselected"
        End If

        WriteCallbackToListingWindow(text)

    End Sub

    Public Sub OnStateChangecallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal State As Integer)
        Try
            WriteCallbackToListingWindow("OnStateChangeCallback Invoked")
            If State = 1 Then
                node.SetState(2)
            ElseIf State = 2 Then
                node.SetState(1)
            ElseIf State = 3 Then
                node.SetState(4)
            ElseIf State = 4 Then
                node.SetState(3)
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    Public Function ToolTipTextcallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal columnID As Integer) As String
        Try
            Dim prop As PropertyList = nodeToolTip.GetProperties()
            ToolTipTextcallback = prop.GetString("Value")
            prop.Dispose()

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

    End Function
	'The possible return values are 0, positive and negative value, suggesting respectively that both nodes are same, first node greater than second, and first node smaller than second.
    'Public Function ColumnSortcallback(ByVal tree as NXOpen.BlockStyler.Tree, ByVal columnID As Integer, ByVal node1 as NXOpen.BlockStyler.Node, ByVal node2 as NXOpen.BlockStyler.Node) As Integer
    'End Function

    'This is called when Node is set with state other than 1 and 2
    Public Function StateIconNameCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal state As Integer) As String
        Dim stateIcon As String = Nothing

        Try
            WriteCallbackToListingWindow("StateIconNameCallback Invoked")

            If state = 3 Then
                stateIcon = "hole"
            ElseIf state = 4 Then
                stateIcon = "boss"
            ElseIf state = 5 Then
                stateIcon = "revolve"
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

        StateIconNameCallback = stateIcon

    End Function

    Public Function OnBeginLabelEdit(ByVal tree As Tree, ByVal node As Node, ByVal columnId As Integer) As NXOpen.BlockStyler.Tree.BeginLabelEditState
        Try
            WriteCallbackToListingWindow("OnBeginLabelEditCallback Invoked")
            Dim prop As PropertyList = nodeEditOptions.GetProperties()
            Dim labelEditOption As Integer = prop.GetEnum("Value")
            prop.Dispose()

            If labelEditOption = 1 Then
                OnBeginLabelEdit = tree.BeginLabelEditState.Allow
            Else
                OnBeginLabelEdit = tree.BeginLabelEditState.Disallow
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Function

    Public Function OnEndLabelEdit(ByVal tree As Tree, ByVal node As Node, ByVal columnId As Integer, ByVal editedText As String) As NXOpen.BlockStyler.Tree.EndLabelEditState
        Try
            WriteCallbackToListingWindow("OnEndLabelEditCallback Invoked")

            If editedText = "Reject" Then
                OnEndLabelEdit = tree.EndLabelEditState.RejectText
            Else
                OnEndLabelEdit = tree.EndLabelEditState.AcceptText
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Function

    Public Function OnEditOptionSelected(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal columnID As Integer, ByVal selectedOptionID As Integer, ByVal selectedOptionText As String, ByVal type As NXOpen.BlockStyler.Tree.ControlType) As NXOpen.BlockStyler.Tree.EditControlOption
        Try
            If type = BlockStyler.Tree.ControlType.ComboBox Then
                If selectedOptionText = "ComboBox-RejectText" Then
                    OnEditOptionSelected = BlockStyler.Tree.EditControlOption.Reject
                Else
                    OnEditOptionSelected = BlockStyler.Tree.EditControlOption.Accept
                End If
            ElseIf type = BlockStyler.Tree.ControlType.ListBox Then
                If selectedOptionText = "ListBox-RejectText" Then
                    OnEditOptionSelected = BlockStyler.Tree.EditControlOption.Reject
                Else
                    OnEditOptionSelected = BlockStyler.Tree.EditControlOption.Accept
                End If

            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Function

    Public Function AskEditControl(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal columnID As Integer) As NXOpen.BlockStyler.Tree.ControlType
        Try
            Dim prop As PropertyList = nodeEditOptions.GetProperties()
            Dim labelEditOption As Integer = prop.GetEnum("Value")
            prop.Dispose()

            If labelEditOption = 2 Then
                AskEditControl = tree.ControlType.ComboBox
                Dim options() As String = {"ComboBox-AcceptText", "ComboBox-DefaultText", "ComboBox-RejectText"}
                'The option must be set here else there would be no options available to edit
                tree.SetEditOptions(options, 1)
            ElseIf labelEditOption = 3 Then
                AskEditControl = tree.ControlType.ListBox
                Dim options() As String = {"ListBox-AcceptText", "ListBox-DefaultText", "ListBox-RejectText"}
                'The option must be set here else there would be no options available to edit
                tree.SetEditOptions(options, 1)
            Else
                AskEditControl = tree.ControlType.None
            End If


        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Function
    Enum MenuID
        AddNode = 0
        DeleteNode
        CheckedMenuItem
        DefaultMenuItem
        DialogLaunchMenuItem
        DisableMenuItem
        HiddenMenuItem
        IconMenuItem

        SubMenu1
        SubMenu2
        SubMenuItem1
        SubMenuItem2
        SubMenuItem3
        SubMenuItem4

        TreeMenuItem
    End Enum

    Public Sub OnMenuCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal columnID As Integer)
        Try
            WriteCallbackToListingWindow("OnMenuCallback Invoked")

            Dim prop As PropertyList = showMenuToggle.GetProperties()
            Dim value As Boolean = prop.GetLogical("Value")
            prop.Dispose()
            If value = False Then
                Return
            End If
            Dim prop1 As PropertyList = redrawToggle.GetProperties()
            Dim isRedraw As Boolean = prop1.GetLogical("Value")
            prop1.Dispose()
            If isRedraw = True Then

                'Create Menu
                Dim menu As TreeListMenu = tree.CreateMenu()
                Dim SubMenu1 As TreeListMenu = tree.CreateMenu()
                Dim SubMenu2 As TreeListMenu = tree.CreateMenu()

                If node Is Nothing Then 'Menu request attempted on some part of the tree and not on node

                    menu.AddMenuItem(MenuID.AddNode, "Add Node")
                    menu.AddSeparator()
                    menu.AddMenuItem(MenuID.TreeMenuItem, "Tree menu item")

                Else 'Menu request for Node

                    menu.AddMenuItem(MenuID.AddNode, "Add Node")
                    menu.AddMenuItem(MenuID.DeleteNode, "Delete Node")

                    menu.AddSeparator()
                    menu.AddMenuItem(MenuID.CheckedMenuItem, "Checked Menu Item")
                    menu.AddMenuItem(MenuID.DefaultMenuItem, "Default Menu Item")
                    menu.AddMenuItem(MenuID.DialogLaunchMenuItem, "Dialog Launch Menu Item")
                    menu.AddMenuItem(MenuID.DisableMenuItem, "Disable Menu Item")
                    menu.AddMenuItem(MenuID.HiddenMenuItem, "Hidden Menu Item")
                    menu.AddMenuItem(MenuID.IconMenuItem, "Icon Menu Item")

                    menu.AddSeparator()
                    menu.AddMenuItem(MenuID.SubMenu1, "Sub Menu 1")
                    menu.AddMenuItem(MenuID.SubMenu2, "Sub Menu 2")

                    'Sub menu
                    SubMenu1.AddMenuItem(MenuID.SubMenuItem1, "Sub Menu Item 1")
                    SubMenu1.AddMenuItem(MenuID.SubMenuItem2, "Sub Menu Item 2")

                    SubMenu2.AddMenuItem(MenuID.SubMenuItem3, "Sub Menu Item 3")
                    SubMenu2.AddMenuItem(MenuID.SubMenuItem4, "Sub Menu Item 4")

                    'Set submenu
                    menu.SetSubMenu(MenuID.SubMenu1, SubMenu1)
                    menu.SetSubMenu(MenuID.SubMenu2, SubMenu2)

                    'Edit Menu Items
                    menu.SetItemChecked(MenuID.CheckedMenuItem, True)
                    menu.SetItemDefault(MenuID.DefaultMenuItem, True)
                    menu.SetItemDialogLaunching(MenuID.DialogLaunchMenuItem, True)
                    menu.SetItemDisable(MenuID.DisableMenuItem, True)
                    menu.SetItemHidden(MenuID.HiddenMenuItem, True)
                    menu.SetItemIcon(MenuID.IconMenuItem, True)
                    menu.SetItemIcon(MenuID.IconMenuItem, "sketch")

                End If

                'Set menu on tree
                tree.SetMenu(menu)

                'Dispose the menu only after setting the menu on tree
                menu.Dispose()
                SubMenu1.Dispose()
                SubMenu2.Dispose()
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)

        End Try

    End Sub

    Public Sub OnMenuCommandCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal menu_item_id As Integer)
        Try
            WriteCallbackToListingWindow("OnMenuSelectionCallback Invoked")
            If node Is Nothing Then 'Menu request was attempted on some part of the tree and not on node follwed by menu selection
                If menu_item_id = MenuID.AddNode Then
                    CreateAndAddNode(Nothing)
                End If
            Else 'Menu request for Node was attempted followed by menu selection
                If menu_item_id = MenuID.AddNode Then
                    CreateAndAddNode(Nothing)
                ElseIf menu_item_id = MenuID.DeleteNode Then
                    Dim selectedNodes() As BlockStyler.Node = tree_control0.GetSelectedNodes()
                    If selectedNodes.Length > 0 Then
                        DeleteSelectedNodes()
                    Else
                        tree.DeleteNode(node)
                    End If
                End If
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    Public Function IsDropAllowedCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal columnID As Integer, ByVal targetNode As NXOpen.BlockStyler.Node, ByVal targetColumnID As Integer) As NXOpen.BlockStyler.Node.DropType
        Try

            Dim prop As PropertyList = dropOptions.GetProperties()
            Dim dropOption As Integer = prop.GetEnum("Value")
            prop.Dispose()

            ' This will just show iconic representation that drop is allowed. No default action is performed after drop.
            ' OnDropCallback should be implemented for specific drop behaviour

            If dropOption = 0 Then
                IsDropAllowedCallback = BlockStyler.Node.DropType.None
            ElseIf dropOption = 1 Then
                IsDropAllowedCallback = BlockStyler.Node.DropType.After
            ElseIf dropOption = 2 Then
                IsDropAllowedCallback = BlockStyler.Node.DropType.Before
            ElseIf dropOption = 3 Then
                IsDropAllowedCallback = BlockStyler.Node.DropType.BeforeAndAfter
            ElseIf dropOption = 4 Then
                IsDropAllowedCallback = BlockStyler.Node.DropType.On
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

    End Function

    Public Function IsDragAllowedCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal columnID As Integer) As NXOpen.BlockStyler.Node.DragType
        Try
            Dim prop As PropertyList = disallowDragToggle.GetProperties()
            Dim isDragDisallowed As Boolean = prop.GetLogical("Value")
            prop.Dispose()

            If isDragDisallowed = True Then
                IsDragAllowedCallback = BlockStyler.Node.DragType.None
            Else
                IsDragAllowedCallback = BlockStyler.Node.DragType.All
            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Function
    'dropType indicates whether the node will be dropped Before, After or On target node
    Public Function OnDropCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node() As NXOpen.BlockStyler.Node, ByVal columnID As Integer, ByVal targetNode As NXOpen.BlockStyler.Node, ByVal targetColumnID As Integer, ByVal dropType As NXOpen.BlockStyler.Node.DropType, ByVal dropMenuItemId As Integer) As Boolean
        Try
            WriteCallbackToListingWindow("OnDropCallback Invoked")

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

    End Function

    'Public Sub OnDropMenuCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal columnID As Integer, ByVal targetNode As NXOpen.BlockStyler.Node, ByVal targetColumnID As Integer)
    'End Sub

    Public Sub OnDefaultActionCallback(ByVal tree As NXOpen.BlockStyler.Tree, ByVal node As NXOpen.BlockStyler.Node, ByVal columnID As Integer)

        Try
            WriteCallbackToListingWindow("OnDefaultAction Invoked")
            If defaultActionToggle IsNot Nothing Then

                Dim defaultActionToggleProps As BlockStyler.PropertyList = defaultActionToggle.GetProperties()
                Dim defaultActionToggle1 As Boolean = defaultActionToggleProps.GetLogical("Value")
                defaultActionToggleProps.Dispose()

                If defaultActionToggle1 = True Then
                    Dim selectedNode() As BlockStyler.Node = tree_control0.GetSelectedNodes()
                    selectedNode(0).SetColumnDisplayText(2, "Default Action")
                    theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Information, "Default Action: Third column text is changed")
                    selectedNode = Nothing
                End If

            End If

        Catch ex As Exception
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

    End Sub

End Class
