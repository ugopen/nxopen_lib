#==============================================================================
#
#      Copyright (c) 2016 Siemens Product Lifecycle Management Software Inc. 
#                          All Rights Reserved.
#
#==============================================================================
#File description: Sample NX/Open Application for Block Styler
#==============================================================================
#
#==============================================================================
#   WARNING!!  This file is overwritten by the Block UI Styler while generating
#   the automation code. Any modifications to this file will be lost after
#   generating the code again.
# 
#==============================================================================

import NXOpen
import NXOpen.BlockStyler
import NXOpen.UF

#------------------------------------------------------------------------------
# Represents Block Styler application cls
#------------------------------------------------------------------------------
class ListCurveProperties:
    # static class members
    theSession = None
    theUI = None

    EdgeSolidTypeUserNames = {
        2 : 'Circular', 8 : 'Constant Parameter', 10 : 'Convergent', 3 : 'Elliptical', 
        7 : 'Foreign', 4 : 'Intersection', 1 : 'Linear', 0 : 'Rubber', 6 : 'SpCurve',
        5 : 'Spline', 9 : 'Trimmed Curve', 11 : 'Undefined'
        }
    
    #------------------------------------------------------------------------------
    # Constructor for NX Styler class
    #------------------------------------------------------------------------------
    def __init__(self):
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.ufs = NXOpen.UF.UFSession.GetUFSession()
            self.theDlxFileName = "ListCurveProperties.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDlxFileName)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddFilterHandler(self.filter_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            raise ex
        
    
    # ------------------------------- DIALOG LAUNCHING ---------------------------------
    # 
    #     Before invoking this application one needs to open any part/empty part in NX
    #     because of the behavior of the blocks.
    # 
    #     Make sure the dlx file is in one of the following locations:
    #         1.) From where NX session is launched
    #         2.) $UGII_USER_DIR/application
    #         3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    #             recommended. This variable is set to a full directory path to a file 
    #             containing a list of root directories for all custom applications.
    #             e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
    # 
    #     You can create the dialog using one of the following way:
    # 
    #     1. Journal Replay
    # 
    #         1) Replay this file through Tool->Journal->Play Menu.
    # 
    #     2. USER EXIT
    # 
    #         1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
    #         2) Invoke the Shared Library through File->Execute->NX Open menu.
    # 
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # This method shows the dialog on the screen
    #------------------------------------------------------------------------------
    def Show(self):
        try:
            self.theDialog.Show()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
    
    #------------------------------------------------------------------------------
    # Method Name: Dispose
    #------------------------------------------------------------------------------
    def Dispose(self):
        if self.theDialog != None:
            self.theDialog.Dispose()
            self.theDialog = None
    
    #------------------------------------------------------------------------------
    # ---------------------Block UI Styler Callback Functions--------------------------
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Callback Name: initialize_cb
    #------------------------------------------------------------------------------
    def initialize_cb(self):
        try:
            self.group0 = self.theDialog.TopBlock.FindBlock("group0")
            self.edge_select0 = self.theDialog.TopBlock.FindBlock("edge_select0")
            self.button0 = self.theDialog.TopBlock.FindBlock("button0")
            self.list_box0 = self.theDialog.TopBlock.FindBlock("list_box0")
            #------------------------------------------------------------------------------
            # Registration of ListBox specific callbacks
            #------------------------------------------------------------------------------
            # self.list_box0.SetAddHandler(self.AddCallback)
            # self.list_box0.SetDeleteHandler(self.DeleteCallback)
            #------------------------------------------------------------------------------
            self.theDialog.TopBlock.Label = "List Curve Properties"
            self.group0.Label = "Curve Properties"
            self.button0.Label = "Clear Selection"
            
            # Set Curve Collector (edge_select0) Properties
            
            # Block Specific Properties
            self.edge_select0.AllowConvergentObject = False
            self.edge_select0.AutomaticProgression = False
            self.edge_select0.BlendVirtualCurveOverlay = False
            self.edge_select0.CreateInterpartLink = False
            self.edge_select0.InterpartSelectionAsString = "Simple"
            #self.edge_select0.InterpartSelectionAsString = "Non-associative Interpart Copy Only"
            #self.edge_select0.InterpartSelectionAsString = "Associative and Non-associative Interpart Copy"
            #self.edge_select0.InterpartSelectionAsString = "Associative Interpart Copy"
            self.edge_select0.LabelString = "Select Curve"
            # Setting the Maximum Scope defines the maximum scope that is available for
            # selection. It determines the options to be populated in the Selection Scope 
            # list in the Top Border Bar in NX. The user may select one of the options in
            # this list to further restrict the Selection Scope.
            self.edge_select0.MaximumScopeAsString = "Entire Assembly"
            #self.edge_select0.MaximumScopeAsString = "Within Work Part and Components"
            #self.edge_select0.MaximumScopeAsString = "Within Work Part Only"
            #self.edge_select0.SelectModeAsString = "Single"
            self.edge_select0.SelectModeAsString = "Multiple"
            self.edge_select0.ToolTip = "Curve"

            # Selection Intent Properties
            self.edge_select0.AllowInferredCurveSelection = True
            self.edge_select0.CurveRules = self.SpecifyCurveRules()
            self.edge_select0.EntityType = self.SpecifyEntityType()
            self.edge_select0.InferredCurveSelection = False
            self.edge_select0.PopupMenuEnabled = True
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
    
    #------------------------------------------------------------------------------
    # Callback Name: dialogShown_cb
    # This callback is executed just before the dialog launch. Thus any value set 
    # here will take precedence and dialog will be launched showing that value. 
    #------------------------------------------------------------------------------
    def dialogShown_cb(self):
        try:
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
    
    #------------------------------------------------------------------------------
    # Callback Name: update_cb
    #------------------------------------------------------------------------------
    def update_cb(self, block):
        try:
            if block == self.edge_select0:
                list_info = []
                objs = self.GetSelectedObjects()
                for obj in objs:
                    if isinstance(obj, NXOpen.Edge):
                        list_info.extend(self.GetEdgeInfo(obj))
                    elif isinstance(obj, NXOpen.Curve):
                        list_info.extend(self.GetCurveInfo(obj))
                    elif isinstance(obj, NXOpen.Point):
                        list_info.extend(self.GetPointInfo(obj))
                self.list_box0.SetListItems(list_info)
            elif block == self.button0:
                self.ClearDialog()
            elif block == self.list_box0:
                pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return 0
    
    #------------------------------------------------------------------------------
    # Callback Name: filter_cb
    #------------------------------------------------------------------------------
    def filter_cb(self, block, selectedObject):
        return NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
    #------------------------------------------------------------------------------
    # ListBox specific callbacks
    #------------------------------------------------------------------------------
    # def AddCallback (self list_box):
    # 
    # 
    
    # def DeleteCallback(self, list_box):
    # 
    # 
    
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Function Name: GetBlockProperties
    # Returns the propertylist of the specified BlockID
    #------------------------------------------------------------------------------
    def GetBlockProperties(self, blockID):
        try:
            return self.theDialog.GetBlockProperties(blockID)
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return None
        
    def ClearDialog(self):
        selObjs = []
        self.edge_select0.SetSelectedObjects(selObjs)
        info = []
        self.list_box0.SetListItems(info)
        
    def GetSelectedObjects(self):
        try:
            return self.edge_select0.GetSelectedObjects()
        except Exception as ex:
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return []
        
    def GetPointInfo(self, point):
        info = []
        info.append("Point tag is {}".format(point.Tag))
        pt = point.Coordinates
        info.append("Point location is ({0:.6g}, {1:.6g}, {2:.6g})".format(pt.X, pt.Y, pt.Z))
        info.append("")
        return info
        
    def GetCurveInfo(self, curve):
        info = []
        info.append("Curve tag is {}".format(curve.Tag))
        info.append("Curve length is {0:.6g}".format(curve.GetLength()))
        info.append("")
        return info
            
    def GetEdgeInfo(self, edge):
        info = []
        info.append("Edge tag is {}".format(edge.Tag))
        info.append("Edge length is {0:.6g}".format(edge.GetLength()))
        info.append("SolidEdgeType of edge is {}".format(edge.SolidEdgeType))
        edgeType = self.ufs.Modeling.AskEdgeType(edge.Tag)
        info.append("Edge type is {}".format(self.GetEdgeTypeString(edgeType)))
        info.append("Edge tolerance is {}".format(self.ufs.Modeling.AskEdgeTolerance(edge.Tag)))
        pt1, pt2, vertex_count = self.ufs.Modeling.AskEdgeVerts(edge.Tag)
        if vertex_count == 0:
            info.append("Edge is a closed curve with no vertices")
        elif vertex_count == 1:
            info.append("Edge has a single vertex at [{0:.6g}, {1:.6g}, {2:.6g}]".format(pt1[0], pt1[1], pt1[2]))
        elif vertex_count == 2:
            info.append("Edge vertex 1 is at [{0:.6g}, {1:.6g}, {2:.6g}]".format(pt1[0], pt1[1], pt1[2]))
            info.append("Edge vertex 2 is at [{0:.6g}, {1:.6g}, {2:.6g}]".format(pt2[0], pt2[1], pt2[2]))
        isEdgeSmooth = self.ufs.Modeling.AskEdgeSmoothness(edge.Tag, 0.0)
        info.append("Is edge smooth: {}".format(str(isEdgeSmooth)))
        info.append("Is reference edge: {}".format(edge.IsReference))
        info.append("")
        return info

    def GetEdgeSolidTypeUserString(self, edgeSolidType):
        type_string = ListCurveProperties.EdgeSolidTypeUserNames[edgeSolidType]
        if not type_string:
            type_string = "Unknown Edge Type"
        return type_string
        
    def GetEdgeTypeString(self, edgeType):
        if edgeType == NXOpen.UF.UFConstants.UF_MODL_LINEAR_EDGE:
            return "linear edge"
        if edgeType == NXOpen.UF.UFConstants.UF_MODL_CIRCULAR_EDGE:
            return "circular edge"
        if edgeType == NXOpen.UF.UFConstants.UF_MODL_ELLIPTICAL_EDGE:
            return "elliptical edge"
        if edgeType == NXOpen.UF.UFConstants.UF_MODL_INTERSECTION_EDGE:
            return "intersection edge"
        if edgeType == NXOpen.UF.UFConstants.UF_MODL_SPLINE_EDGE:
            return "spline edge"
        if edgeType == NXOpen.UF.UFConstants.UF_MODL_SP_CURVE_EDGE:
            return "sp curve edge"
        if edgeType == NXOpen.UF.UFConstants.UF_MODL_FOREIGN_EDGE:
            return "foreign edge"
        if edgeType == NXOpen.UF.UFConstants.UF_MODL_CONST_PARAMETER_EDGE:
            return "constant parameter edge"
        if edgeType == NXOpen.UF.UFConstants.UF_MODL_TRIMMED_CURVE_EDGE:
            return "trimmed curve edge"
        if edgeType == NXOpen.UF.UFConstants.UF_MODL_CONVERGENT_EDGE: 
            return "convergent edge"
        return "unknown edge type"

    def SpecifyCurveRules(self):
        """
        Define the allowed curve rules for CurveRules in the Curve Collector control.
        Use the Python bitwise operator to combine the desired curve rule values,
        then set the CurveRules property of the Curve Collector to the result.
        Documentation explaining the different rules is in the Selecting objects 
        section of the Fundamentals chapter of the NX Help Documentation.
        """
        curve_rules  = 0x1     # Single Curve - Required
        curve_rules |= 0x10    # Body Edges
        curve_rules |= 0x2     # Connected Curves
        curve_rules |= 0x8     # Face Edges
        #curve_rules |= 0x40    # Feature Curves
        #curve_rules |= 0x8000  # Feature Intersection Edges
        #curve_rules |= 0x2000  # Outer Edges of Faces
        #curve_rules |= 0x800   # Region Boundary Curves
        #curve_rules |= 0x4000  # Rib Top Face Edges
        #curve_rules |= 0x20    # Sheet Edges
        curve_rules |= 0x4     # Tangent Curves
        curve_rules |= 0x100   # Vertex Edges
        curve_rules |= 0x200   # Vertex Tangent Edges
        return curve_rules

    def SpecifyDefaultCurveRules(self):
        """
        Define the Default Curve Rule for selecting curves or edges. The default
        curve rule must be one of the rules set in the bit set specified in the 
        SpecifyCurveRules method. This method returns a string to set the 
        DefaultCurveRules enum property as a string for the Curve Collector.
        Documentation explaining the different rules is in the Selecting objects 
        section of the Fundamentals chapter of the NX Help Documentation.
        """
        #curve_rules  = "Single Curve"
        #curve_rules = "Body Edges"
        #curve_rules = "Connected Curves"
        #curve_rules = "Face Edges"
        #curve_rules = "Feature Curves"
        #curve_rules = "Feature Intersection Edges"
        #curve_rules = "Outer Edges of Faces"
        #curve_rules = "Region Boundary Curves"
        #curve_rules = "Rib Top Face Edges"
        #curve_rules = "Sheet Edges"
        curve_rules = "Tangent Curves"
        #curve_rules = "Vertex Edges"
        #curve_rules = "Vertex Tangent Edges"
        return curve_rules

    def SpecifyEntityType(self):
        """
        Define the allowed entities for EntityType in the Curve Collector control.
        Use the Python bitwise operator to combine the desired Entity Type values,
        then set the EntityType property of the Curve Collector to the result.
        Setting the Entity Type provides some additional control over the entity types
        that the user may select. For example, if Allow Bodies is added for the options
        used for Entity Type, if a body is selected, then all the edges in the body are
        added to the Edge Collector.
        """
        entity_type = 0
        entity_type |= 0x1  # Allow Edges
        entity_type |= 0x4  # Allow Curves
        entity_type |= 0x8  # Allow Point
        entity_type |= 0x40  # Allow Bodies
        return entity_type

def main():
    theListCurveProperties = None
    try:
        theListCurveProperties =  ListCurveProperties()
        #  The following method shows the dialog immediately
        theListCurveProperties.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if theListCurveProperties != None:
            theListCurveProperties.Dispose()
            theListCurveProperties = None
    
if __name__ == '__main__':
    main()


