#=============================================================================
#
#      Copyright 2014 Siemens Product Lifecycle Management Software Inc. 
#                          All Rights Reserved.
#
#===============================================================================
#File description: Sample NX/Open Application for Block Styler
#===============================================================================
#

#  WARNING!!  This file is overwritten by the Block Styler while generating
#  the automation code. Any modifications to this file will be lost after
#  generating the code again.

#==============================================================================

#==============================================================================
#  Purpose:  This TEMPLATE file contains Python source to guide you in the
#  construction of your Block application dialog. The generation of your
#  dialog file (.dlx extension) is the first step towards dialog construction
#  within NX.  You must now create a NX Open application that
#  utilizes this file (.dlx).
#
#  The information in this file provides you with the following:
#
#  1.  Help on how to load and display your Block Styler dialog in NX
#      using APIs provided in NXOpen.BlockStyler namespace
#  2.  The empty callback methods (stubs) associated with your dialog items
#      have also been placed in this file. These empty methods have been
#      created simply to start you along with your coding requirements.
#      The method name, argument list and possible return values have already
#      been provided for you.
#==============================================================================

#------------------------------------------------------------------------------
# These imports are needed for the following template code
#------------------------------------------------------------------------------
import os.path
import sys
import traceback
import NXOpen
import NXOpen.BlockStyler

# Type definition to support automatic enumeration
# (StackOverflow answer to the question "How can I represent an 'enum' in Python?")

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

MenuID = enum('AddNode', 'DeleteNode', 'CheckedMenuItem', 'DefaultMenuItem', 'DialogLaunchMenuItem',
              'DisableMenuItem', 'HiddenMenuItem', 'IconMenuItem', 'SubMenu1', 'SubMenu2', 'SubMenuItem1', 
              'SubMenuItem2', 'SubMenuItem3', 'SubMenuItem4', 'TreeMenuItem')
    
     #Enum MenuID
     #    AddNode = 0
     #    DeleteNode
     #    CheckedMenuItem
     #    DefaultMenuItem
     #    DialogLaunchMenuItem
     #    DisableMenuItem
     #    HiddenMenuItem
     #    IconMenuItem

     #    SubMenu1
     #    SubMenu2
     #    SubMenuItem1
     #    SubMenuItem2
     #    SubMenuItem3
     #    SubMenuItem4

     #    TreeMenuItem
     #End Enum

#------------------------------------------------------------------------------
# Represents Block Styler application class
#------------------------------------------------------------------------------
class TreeListDemo:
    # static class members
    #------------------------------------------------------------------------------
    # Bit Option for Property: SnapPointTypesEnabled
    #------------------------------------------------------------------------------
    SnapPointTypesEnabled_UserDefined = 1
    SnapPointTypesEnabled_Inferred = 2
    SnapPointTypesEnabled_ScreenPosition = 4
    SnapPointTypesEnabled_EndPoint = 8
    SnapPointTypesEnabled_MidPoint = 16
    SnapPointTypesEnabled_ControlPoint = 32
    SnapPointTypesEnabled_Intersection = 64
    SnapPointTypesEnabled_ArcCenter = 128
    SnapPointTypesEnabled_QuadrantPoint = 256
    SnapPointTypesEnabled_ExistingPoint = 512
    SnapPointTypesEnabled_PointonCurve = 1024
    SnapPointTypesEnabled_PointonSurface = 2048
    SnapPointTypesEnabled_PointConstructor = 4096
    SnapPointTypesEnabled_TwocurveIntersection = 8192
    SnapPointTypesEnabled_TangentPoint = 16384
    SnapPointTypesEnabled_Poles = 32768
    SnapPointTypesEnabled_BoundedGridPoint = 65536
    #------------------------------------------------------------------------------
    # Bit Option for Property: SnapPointTypesOnByDefault
    #------------------------------------------------------------------------------
    SnapPointTypesOnByDefault_EndPoint = 8
    SnapPointTypesOnByDefault_MidPoint = 16
    SnapPointTypesOnByDefault_ControlPoint = 32
    SnapPointTypesOnByDefault_Intersection = 64
    SnapPointTypesOnByDefault_ArcCenter = 128
    SnapPointTypesOnByDefault_QuadrantPoint = 256
    SnapPointTypesOnByDefault_ExistingPoint = 512
    SnapPointTypesOnByDefault_PointonCurve = 1024
    SnapPointTypesOnByDefault_PointonSurface = 2048
    SnapPointTypesOnByDefault_PointConstructor = 4096
    SnapPointTypesOnByDefault_BoundedGridPoint = 65536
    
    ColumnFirst = 0
    ColumnSecond = 1
    ColumnThird = 2

    nodeBaseString = ''
    nodeSuffixNumber = 0
    previousAddedNode = None
    randomIcon = 0
    randomIconString = ["extrude", "cone", "block", "blend"]

    #------------------------------------------------------------------------------
    # Constructor for NX Styler class
    #------------------------------------------------------------------------------
    def __init__(self):
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.theDialogName = "TreeListDemo.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDialogName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)
            self.group0 = None # Block type: Group
            self.tree_control0 = None # Block type: Tree Control
            self.addDeleteNodeGroup = None # Block type: Group
            self.nodeString = None # Block type: String
            self.addNodeButton = None # Block type: Button
            self.deleteNodeButton = None # Block type: Button
            self.stateIconGroup = None # Block type: Group
            self.stateIconOptions = None # Block type: Enumeration
            self.nodeToolTip = None # Block type: String
            self.NodeEditGroup = None # Block type: Group
            self.nodeEditOptions = None # Block type: Enumeration
            self.menuGroup = None # Block type: Group
            self.showMenuToggle = None # Block type: Toggle
            self.dragDropGroup = None # Block type: Group
            self.disallowDragToggle = None # Block type: Toggle
            self.dropOptions = None # Block type: Enumeration
            self.defaultActionGroup = None # Block type: Group
            self.defaultActionToggle = None # Block type: Toggle
            self.nodeDataGroup = None # Block type: Group
            self.instructions = None # Block type: Multiline String
            self.selection0 = None # Block type: Selection
            self.addCrossSelectionNodeButton = None # Block type: Button
            self.redrawGroup = None # Block type: Group
            self.redrawInstruction = None # Block type: Multiline String
            self.redrawToggle = None # Block type: Toggle
            self.listingWindowGroup = None # Block type: Group
            self.listingWindowToggle = None # Block type: Toggle
        
        except Exception as ex:
            #---- Enter your exception handling code here -----
            raise ex

    #------------------------------------------------------------------------------
    # This method shows the dialog on the screen
    #------------------------------------------------------------------------------
    def Show(self):
        try:
            self.theDialog.Show()
        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    
    #------------------------------------------------------------------------------
    # Method Name: Dispose
    #------------------------------------------------------------------------------
    def Dispose(self):
        if self.theDialog != None:
            self.theDialog.Dispose()
            self.theDialog = None
    
    #------------------------------------------------------------------------------
    #---------------------Block Styler Callback Functions--------------------------
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Callback Name: initialize_cb
    #------------------------------------------------------------------------------
    def initialize_cb(self):
        try:
            self.group0 = self.theDialog.TopBlock.FindBlock("group0")
            self.tree_control0 = self.theDialog.TopBlock.FindBlock("tree_control0")
            self.addDeleteNodeGroup = self.theDialog.TopBlock.FindBlock("addDeleteNodeGroup")
            self.nodeString = self.theDialog.TopBlock.FindBlock("nodeString")
            self.addNodeButton = self.theDialog.TopBlock.FindBlock("addNodeButton")
            self.deleteNodeButton = self.theDialog.TopBlock.FindBlock("deleteNodeButton")
            self.stateIconGroup = self.theDialog.TopBlock.FindBlock("stateIconGroup")
            self.stateIconOptions = self.theDialog.TopBlock.FindBlock("stateIconOptions")
            self.nodeToolTip = self.theDialog.TopBlock.FindBlock("nodeToolTip")
            self.NodeEditGroup = self.theDialog.TopBlock.FindBlock("NodeEditGroup")
            self.nodeEditOptions = self.theDialog.TopBlock.FindBlock("nodeEditOptions")
            self.menuGroup = self.theDialog.TopBlock.FindBlock("menuGroup")
            self.showMenuToggle = self.theDialog.TopBlock.FindBlock("showMenuToggle")
            self.dragDropGroup = self.theDialog.TopBlock.FindBlock("dragDropGroup")
            self.disallowDragToggle = self.theDialog.TopBlock.FindBlock("disallowDragToggle")
            self.dropOptions = self.theDialog.TopBlock.FindBlock("dropOptions")
            self.defaultActionGroup = self.theDialog.TopBlock.FindBlock("defaultActionGroup")
            self.defaultActionToggle = self.theDialog.TopBlock.FindBlock("defaultActionToggle")
            self.nodeDataGroup = self.theDialog.TopBlock.FindBlock("nodeDataGroup")
            self.instructions = self.theDialog.TopBlock.FindBlock("instructions")
            self.selection0 = self.theDialog.TopBlock.FindBlock("selection0")
            self.addCrossSelectionNodeButton = self.theDialog.TopBlock.FindBlock("addCrossSelectionNodeButton")
            self.redrawGroup = self.theDialog.TopBlock.FindBlock("redrawGroup")
            self.redrawInstruction = self.theDialog.TopBlock.FindBlock("redrawInstruction")
            self.redrawToggle = self.theDialog.TopBlock.FindBlock("redrawToggle")
            self.listingWindowGroup = self.theDialog.TopBlock.FindBlock("listingWindowGroup")
            self.listingWindowToggle = self.theDialog.TopBlock.FindBlock("listingWindowToggle")
            #------------------------------------------------------------------------------
            # Registration of Treelist specific callbacks
            #------------------------------------------------------------------------------
            #self.tree_control0.SetOnExpandHandler( self.OnExpandCallback )
            
            #self.tree_control0.SetOnInsertColumnHandler( self.OnInsertColumnCallback )
            
            self.tree_control0.SetOnInsertNodeHandler(self.OnInsertNodeCallback)
            
            self.tree_control0.SetOnDeleteNodeHandler(self.OnDeleteNodeCallback)
            
            #self.tree_control0.SetOnPreSelectHandler( self.OnPreSelectCallback )
            
            self.tree_control0.SetOnSelectHandler(self.OnSelectCallback)
            
            self.tree_control0.SetOnStateChangeHandler(self.OnStateChangeCallback)
            
            self.tree_control0.SetToolTipTextHandler(self.ToolTipTextCallback)
            
            #self.tree_control0.SetColumnSortHandler( self.ColumnSortCallback )
            
            self.tree_control0.SetStateIconNameHandler(self.StateIconNameCallback)
            
            self.tree_control0.SetOnBeginLabelEditHandler(self.OnBeginLabelEdit)
            
            self.tree_control0.SetOnEndLabelEditHandler(self.OnEndLabelEdit)
            
            self.tree_control0.SetOnEditOptionSelectedHandler(self.OnEditOptionSelected)
            
            self.tree_control0.SetAskEditControlHandler(self.AskEditControl)
            
            self.tree_control0.SetOnMenuHandler(self.OnMenuCallback)
            
            self.tree_control0.SetOnMenuSelectionHandler(self.OnMenuCommandCallback)
            
            self.tree_control0.SetIsDropAllowedHandler(self.IsDropAllowedCallback)
            
            self.tree_control0.SetIsDragAllowedHandler(self.IsDragAllowedCallback)
            
            self.tree_control0.SetOnDropHandler(self.OnDropCallback)
            
            #self.tree_control0.SetOnDropMenuHandler(self.OnDropMenuCallback)

            self.tree_control0.SetOnDefaultActionHandler(self.OnDefaultActionCallback)
            
            #------------------------------------------------------------------------------
            TreeListDemo.nodeBaseString = self.nodeString.Value

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    #------------------------------------------------------------------------------
    # Callback Name: dialogShown_cb
    # This callback is executed just before the dialog launch. Thus any value set 
    # here will take precedence and dialog will be launched showing that value. 
    #------------------------------------------------------------------------------
    def dialogShown_cb(self):
        try:
            #---- Enter your callback code here -----
            # Insert Columns
            self.tree_control0.InsertColumn(TreeListDemo.ColumnFirst, "First Column", 80)
            self.tree_control0.InsertColumn(TreeListDemo.ColumnSecond, "Second Column", 80)
            self.tree_control0.InsertColumn(TreeListDemo.ColumnThird, "Third Column", 80)

            # Set resize policy for columns
            self.tree_control0.SetColumnResizePolicy(TreeListDemo.ColumnFirst, NXOpen.BlockStyler.Tree.ColumnResizePolicy.ConstantWidth)
            self.tree_control0.SetColumnResizePolicy(TreeListDemo.ColumnSecond, NXOpen.BlockStyler.Tree.ColumnResizePolicy.ConstantWidth)
            self.tree_control0.SetColumnResizePolicy(TreeListDemo.ColumnThird, NXOpen.BlockStyler.Tree.ColumnResizePolicy.ConstantWidth)

            # Let the second column interpret the text as icon
            self.tree_control0.SetColumnDisplayType(TreeListDemo.ColumnSecond, NXOpen.BlockStyler.Tree.ColumnDisplay.Icon)
        
        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    
    #------------------------------------------------------------------------------
    # Callback Name: apply_cb
    #------------------------------------------------------------------------------
    def apply_cb(self):
        try:
            #---- Enter your callback code here -----
            pass
        except Exception as ex:
        
            #---- Enter your exception handling code here -----
            traceback.print_exc()
        return 0
        
    def CreateNode(self):
        # Get node display string from the block
        nodeDisplayString = self.nodeString.Value

        node = self.tree_control0.CreateNode(nodeDisplayString)

        # Set few properties of node
        node.ForegroundColor = 198
        node.DisplayIcon = TreeListDemo.randomIconString[TreeListDemo.randomIcon]
        node.SelectedIcon = "draft"
        return node
    
    def AddNodeToTree(self, node, parentNode, afterNode):
        # Insert Node
        self.tree_control0.InsertNode(node, parentNode, afterNode, NXOpen.BlockStyler.Tree.NodeInsertOption.Sort)
        node.ScrollTo(TreeListDemo.ColumnFirst, NXOpen.BlockStyler.Node.Scroll.Center)

        # Change the last node color. Making sure that new node color is distinct
        if TreeListDemo.previousAddedNode != None:
            TreeListDemo.previousAddedNode.ForegroundColor = 211
        
        TreeListDemo.previousAddedNode = node        

    def CreateAndAddNode(self, afterNode):
        parentNode = NXOpen.BlockStyler.Node.Null
        node = self.CreateNode()

        # Take first selected node as parent node
        selectedNodes = self.tree_control0.GetSelectedNodes()
        if len(selectedNodes) > 0:
            parentNode = selectedNodes[0]
        self.AddNodeToTree(node, parentNode, afterNode)

        # Assign return value
        return node

    def CreateChildNode(self, parentNode, afterNode):
        node = self.CreateNode()
        self.AddNodeToTree(node, parentNode, afterNode)
        return node

    def WriteCallbackToListingWindow(self, callbackName):
        try:
            if self.listingWindowToggle != None:
                if self.listingWindowToggle.Value:
                    self.theSession.ListingWindow.Open()
                    nullString = ""
                    self.theSession.ListingWindow.WriteLine(nullString)
                    self.theSession.ListingWindow.WriteLine(callbackName)

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def DeleteSelectedNodes(self):
        selectedNodes = self.tree_control0.GetSelectedNodes()
        while len(selectedNodes) > 0:
            self.tree_control0.DeleteNode(selectedNodes[0])
            selectedNodes = self.tree_control0.GetSelectedNodes()
    
    #------------------------------------------------------------------------------
    # Callback Name: update_cb
    #------------------------------------------------------------------------------
    def update_cb(self, block):
        try:
            if block == self.nodeString:
                #---- Enter your code here -----
                pass
            elif block == self.addNodeButton:
                afterNode = NXOpen.BlockStyler.Node.Null
                node = self.CreateAndAddNode(afterNode)

                # State Icon
                prop = self.stateIconOptions.GetProperties()
                enumValue = prop.GetEnum("Value")
                prop.Dispose()
                #enumValue = self.stateIconOptions.ValueAsString

                if enumValue == 0:
                    # Ignore
                    pass
                elif enumValue == 1:
                    node.SetState(1)
                elif enumValue == 2:
                    node.SetState(3) # Set Value other than 1 or 2

            elif block == self.deleteNodeButton:
                self.DeleteSelectedNodes()

            elif block == self.stateIconOptions:
                #---- Enter your code here -----
                pass
            elif block == self.nodeToolTip:
                #---- Enter your code here -----
                pass
            elif block == self.nodeEditOptions:
                #---- Enter your code here -----
                if self.defaultActionToggle != None:
                    nodeEditOption = self.nodeEditOptions.ValueAsString
                    if nodeEditOption == "Combo Box Edit" or nodeEditOption == "Listbox Edit":
                        self.defaultActionToggle.Enable = False
                        self.defaultActionToggle.Value = False
                    else:
                        self.defaultActionToggle.Enable = True

            elif block == self.showMenuToggle:
                #---- Enter your code here -----
                pass
            elif block == self.disallowDragToggle:
                #---- Enter your code here -----
                pass
            elif block == self.dropOptions:
                #---- Enter your code here -----
                pass
            elif block == self.defaultActionToggle:
                #---- Enter your code here -----
                pass
            elif block == self.instructions:
                #---- Enter your code here -----
                pass
            elif block == self.selection0:
                #---- Enter your code here -----
                pass
            elif block == self.addCrossSelectionNodeButton:
                objects = self.selection0.GetSelectedObjects()

                if len(objects) > 0:
                    # Create node and node data
                    node = self.tree_control0.CreateNode("CrossSelection-NodeData")
                    nodeData = node.GetNodeData()
                    nodeData.AddTaggedObject("Data", objects[0])
                    nodeData.Dispose()
                    self.tree_control0.InsertNode(
                        node, NXOpen.BlockStyler.Node.Null, NXOpen.BlockStyler.Node.Null,
                        NXOpen.BlockStyler.Tree.NodeInsertOption.AlwaysLast)

                    # Reset Selection block
                    blank = []
                    self.selection0.SetSelectedObjects(blank)

            elif block == self.redrawInstruction:
                #---- Enter your code here -----
                pass
            elif block == self.redrawToggle:
                self.tree_control0.Redraw(self.redrawToggle.Value)

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return 0

    #------------------------------------------------------------------------------
    # Callback Name: ok_cb
    #------------------------------------------------------------------------------
    def ok_cb(self):
        try:
            #---- Enter your callback code here -----
            self.apply_cb()

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return 0

    #------------------------------------------------------------------------------
    # Treelist specific callbacks
    #------------------------------------------------------------------------------
    #def OnExpandCallback(self, tree, node)
    #

    #def OnInsertColumnCallback(self, tree, node, columnID)
    #

    def OnInsertNodeCallback(self, tree, node):
        try:
            self.WriteCallbackToListingWindow("OnInsertNodeCallback Invoked")

            #Setting random icon
            if TreeListDemo.randomIcon == 0:
                node.SetColumnDisplayText(TreeListDemo.ColumnSecond, TreeListDemo.randomIconString[TreeListDemo.randomIcon])
            elif TreeListDemo.randomIcon == 1:
                node.SetColumnDisplayText(TreeListDemo.ColumnSecond, TreeListDemo.randomIconString[TreeListDemo.randomIcon])
            elif TreeListDemo.randomIcon == 2:
                node.SetColumnDisplayText(TreeListDemo.ColumnSecond, TreeListDemo.randomIconString[TreeListDemo.randomIcon])
            elif TreeListDemo.randomIcon == 3:
                node.SetColumnDisplayText(TreeListDemo.ColumnSecond, TreeListDemo.randomIconString[TreeListDemo.randomIcon])

            TreeListDemo.randomIcon = TreeListDemo.randomIcon + 1

            if TreeListDemo.randomIcon > 3:
                TreeListDemo.randomIcon = 0

            node.SetColumnDisplayText(TreeListDemo.ColumnThird, "Column Text - " + str(TreeListDemo.randomIcon))

            if TreeListDemo.nodeSuffixNumber == 15000:
                TreeListDemo.nodeSuffixNumber = 0
            else:
                TreeListDemo.nodeSuffixNumber = TreeListDemo.nodeSuffixNumber + 1

            # New node text for the next node
            self.nodeString.Value = TreeListDemo.nodeBaseString + str(TreeListDemo.nodeSuffixNumber)

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def OnDeleteNodeCallback(self, tree, node):
        try:
            self.WriteCallbackToListingWindow("OnDeleteNodeCallback Invoked")
            if node == TreeListDemo.previousAddedNode:
                # Set the previous node to None. Done for safe execution.
                TreeListDemo.previousAddedNode = None

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    #def OnPreSelectCallback(self, tree, node as NXOpen.BlockStyler.Node , columnID, selected)
    #

    def OnSelectCallback(self, tree, node, columnID, selected):
        try:
            text = ""

            if selected == True:
                text = "OnSelectCallback Invoked: Node \"" + node.DisplayText + "\" Selected at column :" + str(columnID)
            else:
                text = "OnSelectCallback Invoked: Node \"" + node.DisplayText + "\" Deselected"

            self.WriteCallbackToListingWindow(text)
        
        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def OnStateChangeCallback(self, tree, node, State):
        try:
            self.WriteCallbackToListingWindow("OnStateChangeCallback Invoked")
            if State == 1:
                node.SetState(2)
            elif State == 2:
                node.SetState(1)
            elif State == 3:
                node.SetState(4)
            elif State == 4:
                node.SetState(3)

        except Exception as ex:
            #---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def ToolTipTextCallback(self, tree, node, columnID):
        toolTipText = ''
        try:
            toolTipText = self.nodeToolTip.Value
        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return toolTipText
    
    # The possible return values are 0, positive and negative value, suggesting respectively that both nodes are same, first node greater than second, and first node smaller than second.
    #def ColumnSortCallback(tree as NXOpen.BlockStyler.Tree, columnID, node1 as NXOpen.BlockStyler.Node, node2 as NXOpen.BlockStyler.Node)
    #

    # This is called when Node is set with state other than 1 and 2
    def StateIconNameCallback(self, tree, node, state):
        stateIcon = None
        try:
            self.WriteCallbackToListingWindow("StateIconNameCallback Invoked")
            if state == 3:
                stateIcon = "hole"
            elif state == 4:
                stateIcon = "boss"
            elif state == 5:
                stateIcon = "revolve"
        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return stateIcon

    def OnBeginLabelEdit(self, tree, node, columnId): 
        try:
            self.WriteCallbackToListingWindow("OnBeginLabelEditCallback Invoked")
            #prop = self.nodeEditOptions.GetProperties()
            #labelEditOption = prop.GetEnum("Value")
            #prop.Dispose()
            nodeEditOption = self.nodeEditOptions.ValueAsString

            if nodeEditOption == "Label Edit":
                return NXOpen.BlockStyler.Tree.BeginLabelEditState.Allow
            else:
                return NXOpen.BlockStyler.Tree.BeginLabelEditState.Disallow

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def OnEndLabelEdit(self, tree, node, columnId, editedText):  
        try:
            self.WriteCallbackToListingWindow("OnEndLabelEditCallback Invoked")

            if editedText == "Reject":
                return NXOpen.BlockStyler.Tree.EndLabelEditState.RejectText
            else:
                return NXOpen.BlockStyler.Tree.EndLabelEditState.AcceptText

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def OnEditOptionSelected(self, tree, node, columnID, selectedOptionID, selectedOptionText, type):  
        try:
            if type == NXOpen.BlockStyler.Tree.ControlType.ComboBox:
                if selectedOptionText == "ComboBox-RejectText":
                    return NXOpen.BlockStyler.Tree.EditControlOption.Reject
                else:
                    return NXOpen.BlockStyler.Tree.EditControlOption.Accept
                
            elif type == NXOpen.BlockStyler.Tree.ControlType.ListBox:
                if selectedOptionText == "ListBox-RejectText":
                    return NXOpen.BlockStyler.Tree.EditControlOption.Reject
                else:
                    return NXOpen.BlockStyler.Tree.EditControlOption.Accept

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def AskEditControl(self, tree, node, columnID):
        try:
            nodeEditOption = self.nodeEditOptions.ValueAsString

            if nodeEditOption == "Combo Box Edit":
                options = ["ComboBox-AcceptText", "ComboBox-DefaultText", "ComboBox-RejectText"]
                # The option must be set here else there would be no options available to edit
                tree.SetEditOptions(options, 1)
                return NXOpen.BlockStyler.Tree.ControlType.ComboBox
            elif nodeEditOption == "Listbox Edit":
                options = ["ListBox-AcceptText", "ListBox-DefaultText", "ListBox-RejectText"]
                # The option must be set here else there would be no options available to edit
                tree.SetEditOptions(options, 1)
                return NXOpen.BlockStyler.Tree.ControlType.ListBox
            else:
                return NXOpen.BlockStyler.Tree.ControlType.NotSet

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
    def OnMenuCallback(self, tree, node, columnID):
        try:
            self.WriteCallbackToListingWindow("OnMenuCallback Invoked")
            if self.showMenuToggle.Value == False:
                return
            
            if self.redrawToggle.Value == True:

                # Create Menu
                menu = tree.CreateMenu()
                subMenu1 = tree.CreateMenu()
                subMenu2 = tree.CreateMenu()

                if node == None: # Menu request attempted on some part of the tree and not on node

                    menu.AddMenuItem(MenuID.AddNode, "Add Node")
                    menu.AddSeparator()
                    menu.AddMenuItem(MenuID.TreeMenuItem, "Tree menu item")

                else: # Menu request for Node

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

                    # Sub menu
                    subMenu1.AddMenuItem(MenuID.SubMenuItem1, "Sub Menu Item 1")
                    subMenu1.AddMenuItem(MenuID.SubMenuItem2, "Sub Menu Item 2")

                    subMenu2.AddMenuItem(MenuID.SubMenuItem3, "Sub Menu Item 3")
                    subMenu2.AddMenuItem(MenuID.SubMenuItem4, "Sub Menu Item 4")

                    # Set submenu
                    menu.SetSubMenu(MenuID.SubMenu1, subMenu1)
                    menu.SetSubMenu(MenuID.SubMenu2, subMenu2)

                    # Edit Menu Items
                    menu.SetItemChecked(MenuID.CheckedMenuItem, True)
                    menu.SetItemDefault(MenuID.DefaultMenuItem, True)
                    menu.SetItemDialogLaunching(MenuID.DialogLaunchMenuItem, True)
                    menu.SetItemDisable(MenuID.DisableMenuItem, True)
                    menu.SetItemHidden(MenuID.HiddenMenuItem, True)
                    menu.SetItemIcon(MenuID.IconMenuItem, "sketch")

                # Set menu on tree
                tree.SetMenu(menu)

                # Dispose the menu only after setting the menu on tree
                menu.Dispose()
                subMenu1.Dispose()
                subMenu2.Dispose()

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def OnMenuCommandCallback(self, tree, node, menu_item_id):
        try:
            self.WriteCallbackToListingWindow("OnMenuSelectionCallback Invoked")
            if node == NXOpen.BlockStyler.Node.Null: # Menu request was attempted on some part of the tree and not on node followed by menu selection
                if menu_item_id == MenuID.AddNode:
                    self.CreateAndAddNode(NXOpen.BlockStyler.Node.Null)
                
            else: # Menu request for Node was attempted followed by menu selection
                if menu_item_id == MenuID.AddNode:
                    self.CreateAndAddNode(NXOpen.BlockStyler.Node.Null)
                elif menu_item_id == MenuID.DeleteNode:
                    selectedNodes = self.tree_control0.GetSelectedNodes()
                    if len(selectedNodes) > 0:
                        self.DeleteSelectedNodes()
                    else:
                        tree.DeleteNode(node)

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    def IsDropAllowedCallback(self, tree, node, columnID, targetNode, targetColumnID):  
        isDropAllowed = NXOpen.BlockStyler.Node.DropType.NotSet
        try:
            # The following commented out section shows how to access the 
            # numerical value of an enumeration block and switch on its
            # integer value. There is no static API property on the enumeration 
            # block that returns its numerical value so you need to use the
            # property list API if you want to work with the numerical value

            #prop = self.dropOptions.GetProperties()
            #dropOption = prop.GetEnum("Value")
            #prop.Dispose()

            ## This will just show iconic representation that drop is allowed. No default action is performed after drop.
            ## OnDropCallback should be implemented for specific drop behaviour

            #if dropOption == 0:
            #    isDropAllowed = NXOpen.BlockStyler.Node.DropType.NotSet
            #elif dropOption == 1:
            #    isDropAllowed = NXOpen.BlockStyler.Node.DropType.Before
            #elif dropOption == 2:
            #    isDropAllowed = NXOpen.BlockStyler.Node.DropType.After
            #elif dropOption == 3:
            #    isDropAllowed = NXOpen.BlockStyler.Node.DropType.BeforeAndAfter
            #elif dropOption == 4:
            #    isDropAllowed = NXOpen.BlockStyler.Node.DropType.On

            dropOption = self.dropOptions.ValueAsString

            # This will just show iconic representation that drop is allowed. No default action is performed after drop.
            # OnDropCallback should be implemented for specific drop behaviour

            if dropOption == "Drop not allowed":
                isDropAllowed = NXOpen.BlockStyler.Node.DropType.NotSet
            elif dropOption == "Drop before node":
                isDropAllowed = NXOpen.BlockStyler.Node.DropType.Before
            elif dropOption == "Drop after node":
                isDropAllowed = NXOpen.BlockStyler.Node.DropType.After
            elif dropOption == "Drop before and after node":
                isDropAllowed = NXOpen.BlockStyler.Node.DropType.BeforeAndAfter
            elif dropOption == "Drop on node":
                isDropAllowed = NXOpen.BlockStyler.Node.DropType.On

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return isDropAllowed

    def IsDragAllowedCallback(self, tree, node, columnID):  
        result = NXOpen.BlockStyler.Node.DragType.NotSet
        try:
            isDragDisallowed = self.disallowDragToggle.Value

            if isDragDisallowed == True:
                result = NXOpen.BlockStyler.Node.DragType.NotSet
            else:
                result = NXOpen.BlockStyler.Node.DragType.All

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return result

    def OnDropCallback(self, tree, node, columnID, targetNode, targetColumnID, dropType, dropMenuItemId):
        try:
            self.WriteCallbackToListingWindow("OnDropCallback Invoked")
            return True
        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return False

    #def OnDropMenuCallback(self, tree, node, columnID, targetNode, targetColumnID):
    #

    def OnDefaultActionCallback(self, tree, node, columnID):

        try:
            self.WriteCallbackToListingWindow("OnDefaultAction Invoked")
            if self.defaultActionToggle != None:

                defaultActionToggle1 = self.defaultActionToggle.Value

                if defaultActionToggle1 == True:
                    selectedNode = self.tree_control0.GetSelectedNodes()
                    selectedNode[0].SetColumnDisplayText(2, "Default Action")
                    self.theUI.NXMessageBox.Show(
                        "Block Styler", NXOpen.NXMessageBox.DialogType.Information, 
                        "Default Action: Third column text is changed")
                    selectedNode = None

        except Exception as ex:
            #---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))


#------------------------------- DIALOG LAUNCHING ---------------------------------
#
#    Before invoking this application one needs to open any part/empty part in NX
#    because of the behavior of the blocks.
#
#    Make sure the dlx file is in one of the following locations:
#        1.) From where NX session is launched
#        2.) $UGII_USER_DIR/application
#        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
#            recommended. This variable is set to a full directory path to a file 
#            containing a list of root directories for all custom applications.
#            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
#
#    You can create the dialog using one of the following way:
#
#    1. Journal Replay
#
#        1) Replay this file through Tool->Journal->Play Menu.
#
#    2. USER EXIT
#
#        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
#        2) Invoke the Shared Library through File->Execute->NX Open menu.
#
#------------------------------------------------------------------------------
def main():
    theTreeListDemo = None
    try:
        theTreeListDemo = TreeListDemo()
        # The following method shows the dialog immediately
        theTreeListDemo.Show()
    
    except Exception as ex:
        #---- Enter your exception handling code here -----
        traceback.print_exc()
    finally:
        if theTreeListDemo != None:
            theTreeListDemo.Dispose()
        
if __name__ == '__main__':
    main()


