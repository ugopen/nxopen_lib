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
class ListBodyProperties:
    # static class members
    theSession = None
    theUI = None
    
    #------------------------------------------------------------------------------
    # Constructor for NX Styler class
    #------------------------------------------------------------------------------
    def __init__(self):
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.ufs = NXOpen.UF.UFSession.GetUFSession()
            self.theDlxFileName = "ListBodyProperties.dlx"
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
            self.bodySelect0 = self.theDialog.TopBlock.FindBlock("bodySelect0")
            self.button0 = self.theDialog.TopBlock.FindBlock("button0")
            self.list_box0 = self.theDialog.TopBlock.FindBlock("list_box0")
            #------------------------------------------------------------------------------
            # Registration of ListBox specific callbacks
            #------------------------------------------------------------------------------
            # self.list_box0.SetAddHandler(self.AddCallback)
            # self.list_box0.SetDeleteHandler(self.DeleteCallback)
            #------------------------------------------------------------------------------
            self.theDialog.TopBlock.Label = "List Body Properties"
            self.group0.Label = "Body Properties"
            self.button0.Label = "Clear Selection"

            # Set Body Collector (bodySelect0) Properties

            # Block Specific Properties
            self.bodySelect0.AllowConvergentObject = True
            self.bodySelect0.AutomaticProgression = False
            self.bodySelect0.BalloonTooltipText = \
                "Select a body to list out its properties."
            self.bodySelect0.BlendVirtualCurveOverlay = False
            self.bodySelect0.CreateInterpartLink = False
            self.bodySelect0.InterpartSelectionAsString = "Simple"
            #self.bodySelect0.InterpartSelectionAsString = "Non-associative Interpart Copy Only"
            #self.bodySelect0.InterpartSelectionAsString = "Associative and Non-associative Interpart Copy"
            #self.bodySelect0.InterpartSelectionAsString = "Associative Interpart Copy"
            self.bodySelect0.LabelString = "Select Body"
            # Setting the Maximum Scope defines the maximum scope that is available for
            # selection. It determines the options to be populated in the Selection Scope 
            # list in the Top Border Bar in NX. The user may select one of the options in
            # this list to further restrict the Selection Scope.
            self.bodySelect0.MaximumScopeAsString = "Entire Assembly"
            #self.bodySelect0.MaximumScopeAsString = "Within Work Part and Components"
            #self.bodySelect0.MaximumScopeAsString = "Within Work Part Only"
            #self.bodySelect0.SelectModeAsString = "Single"
            self.bodySelect0.SelectModeAsString = "Multiple"
            self.bodySelect0.ToolTip = "Body"

            # Selection Intent Properties
            self.bodySelect0.BodyRules = self.SpecifyBodyRules()
            self.bodySelect0.DefaultBodyRulesAsString = self.SpecifyDefaultBodyRules()
            self.bodySelect0.EntityType = self.SpecifyEntityType()
            self.bodySelect0.IncludeSheetBodies = True
            self.bodySelect0.PopupMenuEnabled = True
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
            if block == self.bodySelect0:
                list_info = []
                bodies = self.GetSelectedBodies()
                for body in bodies:
                    list_info.extend(self.GetBodyInfo(body))
                self.list_box0.SetListItems(list_info)
            elif block == self.button0:
                self.ClearDialog()
            elif block == self.list_box0:
                # ---- Enter your code here -----
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

    def SpecifyBodyRules(self):
        """
        Define the allowed body rules for BodyRules in the Body Collector control.
        Use the Python bitwise operator to combine the desired body rule values,
        then set the BodyRules property of the Body Collector to the result.
        Documentation explaining the different rules is in the Selecting objects 
        section of the Fundamentals chapter of the NX Help Documentation.
        """
        body_rules  = 0x1     # Single Body - Required
        body_rules |= 0x2     # Feature Bodies
        body_rules |= 0x4     # Bodies in Group
        return body_rules

    def SpecifyDefaultBodyRules(self):
        body_rules = "Single Body"
        #body_rules = "Feature Bodies"
        #body_rules = "Bodies in Group"
        return body_rules

    def SpecifyEntityType(self):
        """
        Define the allowed entity types for the Body Collector. The only
        allowed entity type for the Body Collector is Allow Bodies.
        """
        entity_type = 0x40  # Allow Bodies
        return entity_type
        
    def ClearDialog(self):
        """
        Clears the collector and the list box by calling the set methods with empty lists. 
        """
        selObjs = []
        self.bodySelect0.SetSelectedObjects(selObjs)
        info = []
        self.list_box0.SetListItems(info)
        
    def GetSelectedBodies(self):
        """
        Returns a list of the bodies selected using the Body Collector dialog element.
        """
        try:
            return self.bodySelect0.GetSelectedObjects()
        except Exception as ex:
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return []
            
    def GetBodyInfo(self, body):
        """
        Returns a multiple line string containing information about the given body.
        """
        info = []
        bodyType = self.ufs.Modeling.AskBodyType(body.Tag)
        info.append("Body tag is {}".format(body.Tag))
        info.append("Body type is {}".format(self.GetBodyTypeString(bodyType)))
        info.append("Body has {} faces".format(len(self.ufs.Modeling.AskBodyFaces(body.Tag))))
        info.append("Body has {} edges".format(len(self.ufs.Modeling.AskBodyEdges(body.Tag))))
        info.append("Is body convergent: {}".format(str(body.IsConvergentBody)))
        bodyPrototype = self.GetPrototypeOfOccurrence(body)
        bodyFeatures = bodyPrototype.GetFeatures()
        info.append("Browseable feature list (False, False)")
        numBrowseableFeatures = 0
        for feature in bodyFeatures:
            if self.ufs.Modeling.IsBrowseableFeature(feature.Tag, False, False):
                numBrowseableFeatures += 1
                info.append("    Feature: {}".format(feature.GetFeatureName()))
        info.append("Body created by {} features".format(numBrowseableFeatures))
        info.append("Browseable feature list (True, False) (Inactive features included)")
        numBrowseableFeatures = 0
        for feature in bodyFeatures:
            if self.ufs.Modeling.IsBrowseableFeature(feature.Tag, True, False):
                numBrowseableFeatures += 1
                info.append("    Feature: {}".format(feature.GetFeatureName()))
        info.append("Body created by {} features".format(numBrowseableFeatures))
        info.append("Browseable feature list (True, True)")
        numBrowseableFeatures = 0
        for feature in bodyFeatures:
            if self.ufs.Modeling.IsBrowseableFeature(feature.Tag, True, True):
                numBrowseableFeatures += 1
                info.append("    Feature: {}".format(feature.GetFeatureName()))
        info.append("Body created by {} features".format(numBrowseableFeatures))
        info.append("")
        return info
        
    def GetPrototypeOfOccurrence(self, occurrence):
        """
        If the input object is an occurrence, this method gets 
        the prototype of the occurrence. If the input object is
        not an occurrence, this method simply returns the input
        object, since it is assumed to be the prototype of the 
        input object.
        """
        if not occurrence.IsOccurrence:
            return occurrence
        return occurrence.Prototype
        
    def GetBodyTypeString(self, bodyType):
        """
        Returns a string representation of the body type given 
        an integer value.
        Mapping:
            "solid body" : NXOpen.UF.UFConstants.UF_MODL_SOLID_BODY
            "sheet body" : NXOpen.UF.UFConstants.UF_MODL_SHEET_BODY
        """
        if bodyType == NXOpen.UF.UFConstants.UF_MODL_SOLID_BODY:
            return "solid body"
        if bodyType == NXOpen.UF.UFConstants.UF_MODL_SHEET_BODY:
            return "sheet body"
        return "unknown body type"

    
def main():
    theListBodyProperties = None
    try:
        theListBodyProperties =  ListBodyProperties()
        #  The following method shows the dialog immediately
        theListBodyProperties.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if theListBodyProperties != None:
            theListBodyProperties.Dispose()
            theListBodyProperties = None
    
if __name__ == '__main__':
    main()
