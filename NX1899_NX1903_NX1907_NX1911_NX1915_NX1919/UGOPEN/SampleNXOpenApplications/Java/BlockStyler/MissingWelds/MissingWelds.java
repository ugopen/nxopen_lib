//=============================================================================
//
//                   Copyright (c) 2015 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//

//==============================================================================
//  Purpose:  This TEMPLATE file contains JAVA source to guide you in the
//  construction of your Block application dialog. The generation of your
//  dialog file (.dlx extension) is the first step towards dialog construction
//  within NX.  You must now create a NX Open application that
//  utilizes this file (.dlx).
//
//  The information in this file provides you with the following:
//
//  1.  Help on how to load and display your Block UI Styler dialog in NX
//      using APIs provided in NXOpen.BlockStyler namespace
//  2.  The empty callback methods (stubs) associated with your dialog items
//      have also been placed in this file. These empty methods have been
//      created simply to start you along with your coding requirements.
//      The method name, argument list and possible return values have already
//      been provided for you.
//==============================================================================

//------------------------------------------------------------------------------
//These imports are needed for the following template code
//------------------------------------------------------------------------------
import java.rmi.RemoteException;
import java.util.*;
import nxopen.*;
import nxopen.assemblies.*;
import nxopen.blockstyler.*;
import nxopen.features.*;

//------------------------------------------------------------------------------
//Represents Block Styler application class
//------------------------------------------------------------------------------
public class MissingWelds implements BlockDialog.Initialize, BlockDialog.DialogShown, BlockDialog.Apply, BlockDialog.Ok, BlockDialog.Update
,Wizard.StepNotifyPreCallback
//,Wizard.StepNotifyPostCallback
,Wizard.IsStepOkayCallback
,Wizard.OnSubNodeCallback
,Wizard.OnMenuCallback
,Wizard.OnMenuSelectionCallback
//,ListBox.AddCallback
//,ListBox.DeleteCallback
{
    //class members
    public static Session theSession = null;
    public static UI theUI = null;
    private String theDlxFileName;
    private nxopen.blockstyler.BlockDialog theDialog;
    private nxopen.blockstyler.Wizard missingWeldWizard;// Block type: Wizard
    private nxopen.blockstyler.Group clearanceSetStep;// Block type: Group
    private nxopen.blockstyler.SelectObject compSelection;// Block type: Selection
    private nxopen.blockstyler.Group resultsStep;// Block type: Group
    private nxopen.blockstyler.Enumeration compDisplay;// Block type: Enumeration
    private nxopen.blockstyler.ListBox missingWeldObjectsListBox;// Block type: List Box
    
    //------------------------------------------------------------------------------
    //User defined members
    //------------------------------------------------------------------------------
    private ClearanceSet theClearanceSet;
    private boolean wasSubNodeCreated;
    
    // contains all the components in the assembly, except root component
    private List<DisplayableObject> allObjects;
    // contains a pair of objects for each checked sub node
    private List<DisplayableObject[]> checkedSubNodeObjects;
    // contains a pair of objects for each missing weld, indexed by subNodeId
    private Map<Integer, DisplayableObject[]> missingWelds;
    // temporarily hold the two displayable objects for the selected missing weld
    // for access by update_cb, apply_cb, and StepNotifyPreCallback methods
    private DisplayableObject[] selectedMissingWeldObjects;
    
    //------------------------------------------------------------------------------
    //Constructor for NX Styler class
    //------------------------------------------------------------------------------
    public MissingWelds() throws Exception, RemoteException
    {
        try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUI = (UI)SessionFactory.get("UI");
            theDlxFileName = "MissingWelds.dlx";
            theDialog = theUI.createDialog(theDlxFileName);
            theDialog.addApplyHandler(this);
            theDialog.addOkHandler(this);
            theDialog.addUpdateHandler(this);
            theDialog.addInitializeHandler(this);
            theDialog.addDialogShownHandler(this);
            
            theClearanceSet = null;
            wasSubNodeCreated = false;
            
            allObjects = new ArrayList<DisplayableObject>();
            checkedSubNodeObjects = new ArrayList<DisplayableObject[]>();
            missingWelds = new HashMap<Integer, DisplayableObject[]>();
            selectedMissingWeldObjects = new DisplayableObject[] {null, null};
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            throw new Exception(ex);
        }
    }
    //------------------------------- DIALOG LAUNCHING ---------------------------------
    //
    //    Before invoking this application one needs to open any part/empty part in NX
    //    because of the behavior of the blocks.
    //
    //    Make sure the dlx file is in one of the following locations:
    //        1.) From where NX session is launched
    //        2.) $UGII_USER_DIR/application
    //        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    //            recommended. This variable is set to a full directory path to a file 
    //            containing a list of root directories for all custom applications.
    //            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\\ugii\\menus\\custom_dirs.dat
    //
    //    You can create the dialog using one of the following way:
    //
    //    1. USER EXIT
    //
    //        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
    //        2) Invoke the Shared Library through File->Execute->NX Open menu.
    //
    //------------------------------------------------------------------------------
    public static void main(String [] argv) throws Exception
    {
        MissingWelds theMissingWelds = null;
        try
        {
            theMissingWelds = new MissingWelds();
            // The following method shows the dialog immediately
            theMissingWelds.show();
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        finally
        {
            if(theMissingWelds != null)
            {
                theMissingWelds.dispose();
                theMissingWelds = null;
            }
        }
    }
    
    //------------------------------------------------------------------------------
    // This method specifies how a shared image is unloaded from memory
    // within NX. This method gives you the capability to unload an
    // internal NX Open application or user  exit from NX. Specify any
    // one of the three constants as a return value to determine the type
    // of unload to perform:
    //
    //
    //    Immediately : unload the library as soon as the automation program has completed
    //    Explicitly  : unload the library from the "Unload Shared Image" dialog
    //    AtTermination : unload the library when the NX session terminates
    //
    //
    // NOTE:  A program which associates NX Open applications with the menubar
    // MUST NOT use this option since it will UNLOAD your NX Open application image
    // from the menubar.
    //------------------------------------------------------------------------------
     public static final int getUnloadOption()
    {
        //return BaseSession.LibraryUnloadOption.EXPLICITLY;
         return BaseSession.LibraryUnloadOption.IMMEDIATELY;
        // return BaseSession.LibraryUnloadOption.ATTERMINATION;
    }
    
    //------------------------------------------------------------------------------
    // Following method cleanup any housekeeping chores that may be needed.
    // This method is automatically called by NX.
    //------------------------------------------------------------------------------
    public static void unloadLibrary() throws NXException, RemoteException
    {
        try
        {
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }
    
    //------------------------------------------------------------------------------
    //This method shows the dialog on the screen
    //------------------------------------------------------------------------------
    public int show() throws NXException, RemoteException
    {
        try
        {
            theDialog.show();
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return 0;
    }
    
    //------------------------------------------------------------------------------
    //Method Name: dispose
    //------------------------------------------------------------------------------
    public void dispose() throws NXException, RemoteException
    {
        if(theDialog != null)
        {
            theDialog.dispose();
            theDialog = null;
        }
    }
    
    //------------------------------------------------------------------------------
    //---------------------Block UI Styler Callback Functions--------------------------
    //------------------------------------------------------------------------------
    
    //------------------------------------------------------------------------------
    //Callback Name: initialize
    //------------------------------------------------------------------------------
    public void initialize() throws NXException, RemoteException
    {
        try
        {
            missingWeldWizard = (nxopen.blockstyler.Wizard)theDialog.topBlock().findBlock("missingWeldWizard");
            clearanceSetStep = (nxopen.blockstyler.Group)theDialog.topBlock().findBlock("clearanceSetStep");
            compSelection = (nxopen.blockstyler.SelectObject)theDialog.topBlock().findBlock("compSelection");
            resultsStep = (nxopen.blockstyler.Group)theDialog.topBlock().findBlock("resultsStep");
            compDisplay = (nxopen.blockstyler.Enumeration)theDialog.topBlock().findBlock("compDisplay");
            missingWeldObjectsListBox = (nxopen.blockstyler.ListBox)theDialog.topBlock().findBlock("missingWeldObjectsListBox");
            //------------------------------------------------------------------------------
            //Registration of ListBox specific callbacks
            //------------------------------------------------------------------------------
            //missingWeldObjectsListBox.setAddHandler(this);
            
            //missingWeldObjectsListBox.setDeleteHandler(this);
            
            //------------------------------------------------------------------------------
            //------------------------------------------------------------------------------
            //Registration of Wizard, missingWeldWizard specific callbacks
            //------------------------------------------------------------------------------
            missingWeldWizard.setStepNotifyPreHandler(this);
            
            //missingWeldWizard.setStepNotifyPostHandler(this);
            
            missingWeldWizard.setIsStepOkayHandler(this);
            
            missingWeldWizard.setOnSubNodeHandler(this);
            
            missingWeldWizard.setOnMenuHandler(this);
            
            missingWeldWizard.setOnMenuSelectionHandler(this);
            
            
            compSelection.addFilter(nxopen.blockstyler.SelectObject.FilterType._COMPONENTS);
            
            // Load all the components included in the assembly except the root component
            if (theSession.parts().display() != null)
            {
                Component rootComponent = theSession.parts().display().componentAssembly().rootComponent();
                AddChildren(rootComponent);
            }
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: dialogShown
    //This callback is executed just before the dialog launch. Thus any value set 
    //here will take precedence and dialog will be launched showing that value. 
    //------------------------------------------------------------------------------
    public void dialogShown() throws NXException, RemoteException
    {
        try
        {
            //---- Enter your callback code here -----
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: apply
    //Following callback is associated with the "theDialog" Block.
    //------------------------------------------------------------------------------
    public int apply() throws NXException, RemoteException
    {
        int errorCode = 0;
        try
        {
            
            // Show all bodies and unhighlight all objects
            theSession.displayManager().showByType("SHOW_HIDE_TYPE_SOLID_BODIES", DisplayManager.ShowHideScope.ANY_IN_ASSEMBLY);
            
            if (selectedMissingWeldObjects[0] != null)
            {
                selectedMissingWeldObjects[0].unhighlight();
            }
            if (selectedMissingWeldObjects[1] != null)
            {
                selectedMissingWeldObjects[1].unhighlight();
            }
            
            theSession.parts().work().views().workView().fit();
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            errorCode = 1;
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return errorCode;
    }
    //------------------------------------------------------------------------------
    //Callback Name: update
    //Following callback is associated with the "theDialog" Block.
    //------------------------------------------------------------------------------
    public int update( nxopen.blockstyler.UIBlock block) throws NXException, RemoteException
    {
        try
        {
            if(block == compSelection)
            {
            //---------Enter your code here-----------
            }
            else if(block == compDisplay)
            {
                Part theWorkPart = theSession.parts().work();
                View theWorkView = theWorkPart.views().workView();
                
                // Get value of compDisplay enum
                PropertyList compDisplayProps = compDisplay.getProperties();
                int compDisplayValue = compDisplayProps.getEnum("Value");
                compDisplayProps.dispose();
                compDisplayProps = null;
                
                // "Blank" has the enum value of 0
                if (compDisplayValue == 0)
                {
                    if(selectedMissingWeldObjects[0] != null && selectedMissingWeldObjects[1] != null)
                    {
                        
                        // Unhighlight the objects and show only those two objects
                        selectedMissingWeldObjects[0].unhighlight();
                        selectedMissingWeldObjects[1].unhighlight();
                        
                        theSession.displayManager().hideByType("SHOW_HIDE_TYPE_SHEET_BODIES", DisplayManager.ShowHideScope.ANY_IN_ASSEMBLY);
                        
                        TaggedObjectCollection.Iterator weldManagerIterator = theWorkPart.features().weldManager().iterator();
                        while (weldManagerIterator.hasNext())
                        {
                            Feature weldFeature = (Feature)weldManagerIterator.next();
                            weldFeature.hideBody();
                        }
                        
                        for (DisplayableObject d: allObjects)
                        {
                            if (d != selectedMissingWeldObjects[0] && d != selectedMissingWeldObjects[1])
                            {
                                d.blank();
                            }
                        }
                        
                        theWorkView.fit();
                    }
                }

                // "Highlight" has the enum value of 1
                if (compDisplayValue == 1)
                {
                    if (selectedMissingWeldObjects[0] != null && selectedMissingWeldObjects[1] != null)
                    {
                        
                        // Unblank all bodies and highlight the two objects
                        TaggedObjectCollection.Iterator weldManagerIterator = theWorkPart.features().weldManager().iterator();
                        while (weldManagerIterator.hasNext())
                        {
                            Feature weldFeature = (Feature)weldManagerIterator.next();
                            weldFeature.showBody(true);
                        }
                        
                        for (DisplayableObject d: allObjects)
                        {
                            if (d != selectedMissingWeldObjects[0] && d != selectedMissingWeldObjects[1])
                            {
                                d.unblank();
                            }
                        }
                        
                        theWorkView.fit();
                        
                        selectedMissingWeldObjects[0].highlight();
                        selectedMissingWeldObjects[1].highlight();
                    }
                }
            }
            else if(block == missingWeldObjectsListBox)
            {
            //---------Enter your code here-----------
            }
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return 0;
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: ok
    //------------------------------------------------------------------------------
    public int ok() throws NXException, RemoteException
    {
        int errorCode = 0;
        try
        {
            //---- Enter your callback code here -----
            errorCode = apply();
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            errorCode = 1;
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return errorCode;
    }
    //------------------------------------------------------------------------------
    //ListBox specific callbacks
    //------------------------------------------------------------------------------
    //public int  addCallback (nxopen.blockstyler.ListBox list_box) throws NXException,RemoteException
    //{
    //}
    
    //public int  deleteCallback(nxopen.blockstyler.ListBox list_box) throws NXException,RemoteException
    //{
    //}
    
    //------------------------------------------------------------------------------
    //------------------------------------------------------------------------------
    //Wizard specific callbacks
    //------------------------------------------------------------------------------
    public int stepNotifyPreCallback(Wizard wizard, int nextStep) throws NXException,RemoteException
    {
        try
        {
            Part theWorkPart = theSession.parts().work();
            View theWorkView = theWorkPart.views().workView();
            
            if (nextStep == 0)
            {
                
                // Clear list box
                String[] listBoxMessage = new String[1];
                listBoxMessage[0] = "";
                missingWeldObjectsListBox.setListItems(listBoxMessage);
                
                // Show all bodies and unhighlight all objects
                theSession.displayManager().showByType("SHOW_HIDE_TYPE_SOLID_BODIES", DisplayManager.ShowHideScope.ANY_IN_ASSEMBLY);
                
                if (selectedMissingWeldObjects[0] != null)
                {
                    selectedMissingWeldObjects[0].unhighlight();
                    selectedMissingWeldObjects[0] = null;
                }
                if (selectedMissingWeldObjects[1] != null)
                {
                    selectedMissingWeldObjects[1].unhighlight();
                    selectedMissingWeldObjects[1] = null;
                }
                
                // Remove all sub nodes
                for (int key: missingWelds.keySet())
                {
                    wizard.removeStepSubNode(key);
                }
                
                if (theClearanceSet != null)
                {
                    theClearanceSet.delete();
                    theClearanceSet = null;
                }
                
                wasSubNodeCreated = false;
                missingWelds.clear();
                checkedSubNodeObjects.clear();
                
                theWorkView.fit();
            }
            else if (nextStep == 1)
            {
                ClearanceAnalysisBuilder clearanceAnalysisBuilder1 = theWorkPart.assemblyManager().createClearanceAnalysisBuilder(null);
                
                // Set parameters
                clearanceAnalysisBuilder1.setClearanceSetName("Missing Weld Clearance Set");
                clearanceAnalysisBuilder1.setCollectionOneRange(ClearanceAnalysisBuilder.CollectionRange.SELECTED_OBJECTS);
                
                // Add selected components to CollectionOneObjects
                for (TaggedObject tagObj: compSelection.getSelectedObjects())
                {
                    clearanceAnalysisBuilder1.collectionOneObjects().add((Component)tagObj);
                }
                
                NXObject nXObject1 = clearanceAnalysisBuilder1.commit();
                clearanceAnalysisBuilder1.destroy();
                theClearanceSet = (ClearanceSet)nXObject1; // holds the clearance set created by the wizard
                theClearanceSet.performAnalysis(ClearanceSet.ReanalyzeOutOfDateExcludedPairs.FALSE);
                
                // Store the list of welds
                List<TaggedObject[]> weldObjects = new ArrayList<TaggedObject[]>(); // holds the pair of tagged objects involved in each weld feature
                TaggedObjectCollection.Iterator weldManagerIterator = theWorkPart.features().weldManager().iterator();
                while (weldManagerIterator.hasNext())
                {
                    Feature weldFeature = (Feature)weldManagerIterator.next();
                    nxopen.weld.ConnectedPart connectPartsInfo = theSession.weldCustomManager().askConnectedParts(weldFeature);
                    // We assume that there are exactly two sets for the weld, with one object in each set
                    NXObject[] id1;
                    id1 = connectPartsInfo.getSetInformation(0);
                    NXObject[] id2;
                    id2 = connectPartsInfo.getSetInformation(1);
                    weldObjects.add(new NXObject[] {id1[0], id2[0]});
                }
                
                // Create a subNode for each missing weld and store the pair of objects involved in the weld.
                // NOTE: The interfering objects in the clearance set, and the objects involved in the weld feature
                // must be components when compared with each other.
                DisplayableObject interferenceComponent1 = null;
                DisplayableObject interferenceComponent2 = null;
                ClearanceSet.NextInterferenceData nextInterference;
                
                nextInterference = theClearanceSet.getNextInterference(interferenceComponent1, interferenceComponent2);
                interferenceComponent1 = nextInterference.nextobject1;
                interferenceComponent2 = nextInterference.nextobject2;
                
                int i = 1;
                int subNodeID;
                String missingWeldName;
                
                while (interferenceComponent1 != null)
                {
                    boolean isMissingWeld = true;
                    for (TaggedObject[] weldPair: weldObjects)
                    {
                        Body weldBody1 = (Body)weldPair[0];
                        Body weldBody2 = (Body)weldPair[1];
                        Component weldComponent1 = weldBody1.owningComponent();
                        Component weldComponent2 = weldBody2.owningComponent();
                        if ((weldComponent1 == interferenceComponent1 && weldComponent2 == interferenceComponent2)
                                || (weldComponent2 == interferenceComponent1 && weldComponent1 == interferenceComponent2))
                        {
                            isMissingWeld = false;
                            break;
                        }
                    }
                    
                    if (isMissingWeld)
                    {
                        missingWeldName = "Missing weld " + i;
                        i++;
                        subNodeID = wizard.createStepSubNode(1, missingWeldName, "", true, true);
                        missingWelds.put(subNodeID, new DisplayableObject[] {interferenceComponent1, interferenceComponent2});
                        checkedSubNodeObjects.add(new DisplayableObject[] {interferenceComponent1, interferenceComponent2});
                        wasSubNodeCreated = true;
                    }
                    
                    nextInterference = theClearanceSet.getNextInterference(interferenceComponent1, interferenceComponent2);
                    interferenceComponent1 = nextInterference.nextobject1;
                    interferenceComponent2 = nextInterference.nextobject2;
                }
                
                // If no sub nodes were created, display message
                if (!wasSubNodeCreated)
                {
                    String listBoxMessage[] = new String[1];
                    listBoxMessage[0] = "There are no missing welds.";
                    missingWeldObjectsListBox.setListItems(listBoxMessage);
                }
                
                theWorkView.fit();
            }
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        
        return 0;
    }
    
    //public void stepNotifyPostCallback(Wizard wizard, int previousStep) throws NXException,RemoteException
    //{
    //}
    
    public boolean isStepOkayCallback(Wizard wizard, int step) throws NXException,RemoteException
    {
        try
        {
            if (wizard.currentStep() == 0)
            {
                if (compSelection.getSelectedObjects().length > 0)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            else if (wizard.currentStep() == 1)
            {
                return true;
            }
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        
        return false;
    }
    
    public void onSubNodeCallback(Wizard wizard, int step, int subNodeId, Wizard.SubNodeAction action) throws NXException,RemoteException
    {
        try
        {
            Part theWorkPart = theSession.parts().work();
            View theWorkView = theWorkPart.views().workView();
            
            // Store the pair of objects from the missing weld associated with this sub node
            // for access by update_cb, apply_cb, and StepNotifyPreCallback methods
            selectedMissingWeldObjects = missingWelds.get(subNodeId).clone();
            
            if (action == Wizard.SubNodeAction.SELECT)
            {
                
                // Add the missing weld's objects to list box
                String[] listBoxMessage = new String[2];
                listBoxMessage[0] = selectedMissingWeldObjects[0].name();
                listBoxMessage[1] = selectedMissingWeldObjects[1].name();
                missingWeldObjectsListBox.setListItems(listBoxMessage);
                
                // Get value of compDisplay enum
                PropertyList compDisplayProps = compDisplay.getProperties();
                int compDisplayValue = compDisplayProps.getEnum("Value");
                compDisplayProps.dispose();
                compDisplayProps = null;               
                
                // "Blank" has the enum value of 0
                if (compDisplayValue == 0)
                {
                    
                    // Show only the two objects
                    theSession.displayManager().hideByType("SHOW_HIDE_TYPE_SHEET_BODIES", DisplayManager.ShowHideScope.ANY_IN_ASSEMBLY);
                    
                    TaggedObjectCollection.Iterator weldManagerIterator = theWorkPart.features().weldManager().iterator();
                    while (weldManagerIterator.hasNext())
                    {
                        Feature weldFeature = (Feature)weldManagerIterator.next();
                        weldFeature.hideBody();
                    }
                    
                    for (DisplayableObject d: allObjects)
                    {
                        if (d != selectedMissingWeldObjects[0] && d != selectedMissingWeldObjects[1])
                        {
                            d.blank();
                        }
                    }
                    
                    theWorkView.fit();
                }

                // "Highlight" has the enum value of 1
                if (compDisplayValue == 1)    
                {
                    theWorkView.fit();
                    
                    selectedMissingWeldObjects[0].highlight();
                    selectedMissingWeldObjects[1].highlight();
                }
            }
            
            else if (action == Wizard.SubNodeAction.DESELECT)
            {
                
                // Clear list box
                String[] listBoxMessage = new String[1];
                listBoxMessage[0] = "";
                missingWeldObjectsListBox.setListItems(listBoxMessage);
                
                // Unhighlight and unblank all bodies
                selectedMissingWeldObjects[0].unhighlight();
                selectedMissingWeldObjects[1].unhighlight();
                
                TaggedObjectCollection.Iterator weldManagerIterator = theWorkPart.features().weldManager().iterator();
                while (weldManagerIterator.hasNext())
                {
                    Feature weldFeature = (Feature)weldManagerIterator.next();
                    weldFeature.showBody(true);
                }
                
                for (DisplayableObject d: allObjects)
                {
                    if (d != selectedMissingWeldObjects[0] && d != selectedMissingWeldObjects[1])
                    {
                        d.unblank();
                    }
                }
                
                // Release this pair of objects when the sub node is deselected
                selectedMissingWeldObjects[0] = null;
                selectedMissingWeldObjects[1] = null;
            }
            
            else if (action == Wizard.SubNodeAction.CHECK)
            {
                checkedSubNodeObjects.add(selectedMissingWeldObjects);
            }
            
            else if (action == Wizard.SubNodeAction.UNCHECK)
            {
                
                // If the sub node is unchecked, and the pair of objects associated
                // with the sub node is found in checkedSubNodeObjects, then remove
                // the pair
                boolean found = false;
                int i;
                for (i = 0; i < checkedSubNodeObjects.size(); ++i)
                {
                    DisplayableObject[] tempArray = checkedSubNodeObjects.get(i);
                    if ((tempArray[0] == selectedMissingWeldObjects[0] && tempArray[1] == selectedMissingWeldObjects[1])
                            || (tempArray[0] == selectedMissingWeldObjects[1] && tempArray[1] == selectedMissingWeldObjects[0]))
                    {
                        found = true;
                        break;
                    }
                }
                
                if (found)
                {
                    checkedSubNodeObjects.remove(i);
                }
            }
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }
    
    public void onMenuCallback(Wizard wizard, Wizard.TaskNavigatorItem item, int step, int subNodeId) throws NXException,RemoteException
    {
        try
        {
            TreeListMenu subNodeMenu = missingWeldWizard.createMenu();
            if (item == Wizard.TaskNavigatorItem.STEP)
            {
                if (wasSubNodeCreated)
                {
                    subNodeMenu.addMenuItem(0, "Generate Report for Selected Missing Welds");
                    missingWeldWizard.setMenu(subNodeMenu);
                }
            }
            else if (item == Wizard.TaskNavigatorItem.SUB_NODE)
            {
                subNodeMenu.addMenuItem(1, "Export Image to PDF");
                missingWeldWizard.setMenu(subNodeMenu);
            }
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }
    
    public void onMenuSelectionCallback(Wizard wizard, Wizard.TaskNavigatorItem item, int step, int subNodeId, int commandIndex) throws NXException,RemoteException
    {
        try
        {
            Part theWorkPart = theSession.parts().work();
            
            if (commandIndex == 0)
            {
                ListingWindow reportWindow = theSession.listingWindow();
                reportWindow.open();
                reportWindow.writeLine("Missing Welds for " + theSession.parts().display().componentAssembly().rootComponent().displayName() + "\n\n");
                reportWindow.writeLine(checkedSubNodeObjects.size() + " of " + missingWelds.size() + " missing welds selected\n\n");
                reportWindow.writeLine("     Part 1\t\tPart 2\n\n");
                
                // Format spacing in report
                // Assumes no more than 999 missing weld pairs
                int i = 1;
                for (DisplayableObject[] weldPair: checkedSubNodeObjects)
                {
                    if (i <= 9)
                    {
                        reportWindow.writeLine(i + ")   " + weldPair[0].name() + "\t" + weldPair[1].name());
                        i++;
                    }
                    else if (i <= 99)
                    {
                        reportWindow.writeLine(i + ")  " + weldPair[0].name() + "\t" + weldPair[1].name());
                        i++;
                    }
                    else
                    {
                        reportWindow.writeLine(i + ") " + weldPair[0].name() + "\t" + weldPair[1].name());
                        i++;
                    }
                }
            }
            else if (commandIndex == 1)
            {
                
                // Get value of compDisplay enum
                PropertyList compDisplayProps = compDisplay.getProperties();
                int compDisplayValue = compDisplayProps.getEnum("Value");    
                
                // If Highlight is selected, automatically select Blank before creating image
                // "Highlight" has the enum value of 1
                if (compDisplayValue == 1)
                {

                    // "Blank" has the enum value of 0
                    compDisplayProps.setEnum("Value", 0);
                    
                    // Unhighlight the objects and show only those two objects
                    selectedMissingWeldObjects[0].unhighlight();
                    selectedMissingWeldObjects[1].unhighlight();
                    
                    theSession.displayManager().hideByType("SHOW_HIDE_TYPE_SHEET_BODIES", DisplayManager.ShowHideScope.ANY_IN_ASSEMBLY);
                    
                    TaggedObjectCollection.Iterator weldManagerIterator = theWorkPart.features().weldManager().iterator();
                    while (weldManagerIterator.hasNext())
                    {
                        Feature weldFeature = (Feature)weldManagerIterator.next();
                        weldFeature.hideBody();
                    }
                    
                    for (DisplayableObject d: allObjects)
                    {
                        if (d != selectedMissingWeldObjects[0] && d != selectedMissingWeldObjects[1])
                        {
                            d.blank();
                        }
                    }
                    
                    theWorkPart.views().workView().fit();
                }
                
                compDisplayProps.dispose();
                compDisplayProps = null; 
                

                PrintPDFBuilder printPDFBuilder1 = theWorkPart.plotManager().createPrintPdfbuilder();
                
                NXObject sheets1[] = new nxopen.NXObject[1];
                NXObject nullNXOpen_NXObject = null;
                sheets1[0] = nullNXOpen_NXObject;
                printPDFBuilder1.sourceBuilder().setSheets(sheets1);
                
                // Set pdf path to same directory as work part
                String fullPath = theWorkPart.fullPath();
                int index = fullPath.lastIndexOf('\\');
                String workPartDir = fullPath.substring(0, index);
                String fileName = "MissingWeld_" + selectedMissingWeldObjects[0].name() + "_" + selectedMissingWeldObjects[1].name() + ".pdf";
                printPDFBuilder1.setFilename(workPartDir + "\\" + fileName);
                

                NXObject nXObject1 = printPDFBuilder1.commit();
                printPDFBuilder1.destroy();
            }
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }
    
    
    //------------------------------------------------------------------------------
    //Function Name: AddChildren
    //Recursive function used to add the children of the current component tree
    //node to allObjects
    //------------------------------------------------------------------------------
    public void AddChildren(Component component) throws NXException, RemoteException
    {
        try
        {
            Component[] childComponents = component.getChildren();
            for (int i = 0; i < childComponents.length; ++i)
            {
                allObjects.add(childComponents[i]);
                AddChildren(childComponents[i]);
            }
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }
    
}
