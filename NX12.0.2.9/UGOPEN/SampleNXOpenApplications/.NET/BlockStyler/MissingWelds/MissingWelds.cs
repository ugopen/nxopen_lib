//=============================================================================
//
//                   Copyright (c) 2015 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//

//==============================================================================
//  Purpose:  This TEMPLATE file contains C# source to guide you in the
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
using System;
using System.Collections.Generic;
using NXOpen;
using NXOpen.Assemblies;
using NXOpen.BlockStyler;
using NXOpen.Features;

//------------------------------------------------------------------------------
//Represents Block Styler application class
//------------------------------------------------------------------------------
public class MissingWelds
{
    //class members
    private static Session theSession = null;
    private static UI theUI = null;
    private string theDlxFileName;
    private NXOpen.BlockStyler.BlockDialog theDialog;
    private NXOpen.BlockStyler.Wizard missingWeldWizard;// Block type: Wizard
    private NXOpen.BlockStyler.Group clearanceSetStep;// Block type: Group
    private NXOpen.BlockStyler.SelectObject compSelection;// Block type: Selection
    private NXOpen.BlockStyler.Group resultsStep;// Block type: Group
    private NXOpen.BlockStyler.Enumeration compDisplay;// Block type: Enumeration
    private NXOpen.BlockStyler.ListBox missingWeldObjectsListBox;// Block type: List Box

    //------------------------------------------------------------------------------
    //User defined members
    //------------------------------------------------------------------------------
    private ClearanceSet theClearanceSet;
    private bool wasSubNodeCreated;

    // contains all the components in the assembly, except root component
    private List<DisplayableObject> allObjects = null;
    // contains a pair of objects for each checked sub node
    private List<Tuple<DisplayableObject, DisplayableObject>> checkedSubNodeObjects = null;
    // contains a pair of objects for each missing weld, indexed by subNodeId
    private Dictionary<int, Tuple<DisplayableObject, DisplayableObject>> missingWelds = null;
    // temporarily hold the two displayable objects for the selected missing weld
    // for access by update_cb, apply_cb, and StepNotifyPreCallback methods
    private DisplayableObject[] selectedMissingWeldObjects = null;
    
    //------------------------------------------------------------------------------
    //Constructor for NX Styler class
    //------------------------------------------------------------------------------
    public MissingWelds()
    {
        try
        {
            theSession = Session.GetSession();
            theUI = UI.GetUI();
            theDlxFileName = "MissingWelds.dlx";
            theDialog = theUI.CreateDialog(theDlxFileName);
            theDialog.AddApplyHandler(new NXOpen.BlockStyler.BlockDialog.Apply(apply_cb));
            theDialog.AddOkHandler(new NXOpen.BlockStyler.BlockDialog.Ok(ok_cb));
            theDialog.AddUpdateHandler(new NXOpen.BlockStyler.BlockDialog.Update(update_cb));
            theDialog.AddInitializeHandler(new NXOpen.BlockStyler.BlockDialog.Initialize(initialize_cb));
            theDialog.AddDialogShownHandler(new NXOpen.BlockStyler.BlockDialog.DialogShown(dialogShown_cb));

            theClearanceSet = null;
            wasSubNodeCreated = false;

            allObjects = new List<DisplayableObject>();
            checkedSubNodeObjects = new List<Tuple<DisplayableObject, DisplayableObject>>();
            missingWelds = new Dictionary<int, Tuple<DisplayableObject, DisplayableObject>>();
            selectedMissingWeldObjects = new DisplayableObject[2] { null, null };
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            throw ex;
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
    //            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
    //
    //    You can create the dialog using one of the following way:
    //
    //    1. Journal Replay
    //
    //        1) Replay this file through Tool->Journal->Play Menu.
    //
    //    2. USER EXIT
    //
    //        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
    //        2) Invoke the Shared Library through File->Execute->NX Open menu.
    //
    //------------------------------------------------------------------------------
    public static void Main()
    {
        MissingWelds theMissingWelds = null;
        try
        {
            theMissingWelds = new MissingWelds();
            // The following method shows the dialog immediately
            theMissingWelds.Show();
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
        finally
        {
            if(theMissingWelds != null)
                theMissingWelds.Dispose();
                theMissingWelds = null;
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
     public static int GetUnloadOption(string arg)
    {
        //return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);
         return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
    }
    
    //------------------------------------------------------------------------------
    // Following method cleanup any housekeeping chores that may be needed.
    // This method is automatically called by NX.
    //------------------------------------------------------------------------------
    public static void UnloadLibrary(string arg)
    {
        try
        {
            //---- Enter your code here -----
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
    }
    
    //------------------------------------------------------------------------------
    //This method shows the dialog on the screen
    //------------------------------------------------------------------------------
    public NXOpen.UIStyler.DialogResponse Show()
    {
        try
        {
            theDialog.Show();
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
        return 0;
    }
    
    //------------------------------------------------------------------------------
    //Method Name: Dispose
    //------------------------------------------------------------------------------
    public void Dispose()
    {
        if(theDialog != null)
        {
            theDialog.Dispose();
            theDialog = null;
        }
    }
    
    //------------------------------------------------------------------------------
    //---------------------Block UI Styler Callback Functions--------------------------
    //------------------------------------------------------------------------------
    
    //------------------------------------------------------------------------------
    //Callback Name: initialize_cb
    //------------------------------------------------------------------------------
    public void initialize_cb()
    {
        try
        {
            missingWeldWizard = (NXOpen.BlockStyler.Wizard)theDialog.TopBlock.FindBlock("missingWeldWizard");
            clearanceSetStep = (NXOpen.BlockStyler.Group)theDialog.TopBlock.FindBlock("clearanceSetStep");
            compSelection = (NXOpen.BlockStyler.SelectObject)theDialog.TopBlock.FindBlock("compSelection");
            resultsStep = (NXOpen.BlockStyler.Group)theDialog.TopBlock.FindBlock("resultsStep");
            compDisplay = (NXOpen.BlockStyler.Enumeration)theDialog.TopBlock.FindBlock("compDisplay");
            missingWeldObjectsListBox = (NXOpen.BlockStyler.ListBox)theDialog.TopBlock.FindBlock("missingWeldObjectsListBox");
            //------------------------------------------------------------------------------
            //Registration of ListBox specific callbacks
            //------------------------------------------------------------------------------
            //missingWeldObjectsListBox.SetAddHandler(new NXOpen.BlockStyler.ListBox.AddCallback(AddCallback));
            
            //missingWeldObjectsListBox.SetDeleteHandler(new NXOpen.BlockStyler.ListBox.DeleteCallback(DeleteCallback));
            
            //------------------------------------------------------------------------------
            //------------------------------------------------------------------------------
            //Registration of Wizard, missingWeldWizard specific callbacks
            //------------------------------------------------------------------------------
            missingWeldWizard.SetStepNotifyPreHandler(new Wizard.StepNotifyPreCallback(stepNotifyPreCallback));
            
            //missingWeldWizard.SetStepNotifyPostHandler(new Wizard.StepNotifyPostCallback(stepNotifyPostCallback));
            
            missingWeldWizard.SetIsStepOkayHandler(new Wizard.IsStepOkayCallback(isStepOkayCallback));
            
            missingWeldWizard.SetOnSubNodeHandler(new Wizard.OnSubNodeCallback(onSubNodeCallback));
            
            missingWeldWizard.SetOnMenuHandler(new Wizard.OnMenuCallback(onMenuCallback));
            
            missingWeldWizard.SetOnMenuSelectionHandler(new Wizard.OnMenuSelectionCallback(onMenuSelectionCallback));


            compSelection.AddFilter((int)NXOpen.BlockStyler.SelectObject.FilterType.Components);

            // Load all the components included in the assembly except the root component
            if (theSession.Parts.Display != null)
            {
                Component rootComponent = theSession.Parts.Display.ComponentAssembly.RootComponent;
                AddChildren(rootComponent);
            }
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: dialogShown_cb
    //This callback is executed just before the dialog launch. Thus any value set 
    //here will take precedence and dialog will be launched showing that value. 
    //------------------------------------------------------------------------------
    public void dialogShown_cb()
    {
        try
        {
            //---- Enter your callback code here -----
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: apply_cb
    //------------------------------------------------------------------------------
    public int apply_cb()
    {
        int errorCode = 0;
        try
        {
            
            // Show all bodies and unhighlight all objects
            theSession.DisplayManager.ShowByType("SHOW_HIDE_TYPE_SOLID_BODIES", DisplayManager.ShowHideScope.AnyInAssembly);

            if (selectedMissingWeldObjects[0] != null)
            {
                selectedMissingWeldObjects[0].Unhighlight();
            }
            if (selectedMissingWeldObjects[1] != null)
            {
                selectedMissingWeldObjects[1].Unhighlight();
            }

            theSession.Parts.Work.Views.WorkView.Fit();
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            errorCode = 1;
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
        return errorCode;
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: update_cb
    //------------------------------------------------------------------------------
    public int update_cb( NXOpen.BlockStyler.UIBlock block)
    {
        try
        {
            if (block == compSelection)
            {
            //---------Enter your code here-----------
            }
            else if (block == compDisplay)
            {
                Part theWorkPart = theSession.Parts.Work;
                View theWorkView = theWorkPart.Views.WorkView;

                // Get value of compDisplay enum
                PropertyList compDisplayProps = compDisplay.GetProperties();
                int compDisplayValue = compDisplayProps.GetEnum("Value");
                compDisplayProps.Dispose();
                compDisplayProps = null;

                // "Blank" has the enum value of 0
                if (compDisplayValue == 0)
                {
                    if (selectedMissingWeldObjects[0] != null && selectedMissingWeldObjects[1] != null)
                    {

                        // Unhighlight the objects and show only those two objects
                        selectedMissingWeldObjects[0].Unhighlight();
                        selectedMissingWeldObjects[1].Unhighlight();

                        theSession.DisplayManager.HideByType("SHOW_HIDE_TYPE_SHEET_BODIES", DisplayManager.ShowHideScope.AnyInAssembly);

                        foreach (Feature weldFeature in theWorkPart.Features.WeldManager)
                        {
                            weldFeature.HideBody();
                        }

                        foreach (DisplayableObject d in allObjects)
                        {
                            if (d != selectedMissingWeldObjects[0] && d != selectedMissingWeldObjects[1])
                            {
                                d.Blank();
                            }
                        }

                        theWorkView.Fit();
                    }
                }

                // "Highlight" has the enum value of 1
                if (compDisplayValue == 1)
                {
                    if (selectedMissingWeldObjects[0] != null && selectedMissingWeldObjects[1] != null)
                    {

                        // Unblank all bodies and highlight the two objects
                        foreach (Feature weldFeature in theWorkPart.Features.WeldManager)
                        {
                            weldFeature.ShowBody(true);
                        }

                        foreach (DisplayableObject d in allObjects)
                        {
                            if (d != selectedMissingWeldObjects[0] && d != selectedMissingWeldObjects[1])
                            {
                                d.Unblank();
                            }
                        }

                        theWorkView.Fit();

                        selectedMissingWeldObjects[0].Highlight();
                        selectedMissingWeldObjects[1].Highlight();
                    }
                }
            }
            else if (block == missingWeldObjectsListBox)
            {
            //---------Enter your code here-----------
            }
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
        return 0;
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: ok_cb
    //------------------------------------------------------------------------------
    public int ok_cb()
    {
        int errorCode = 0;
        try
        {
            errorCode = apply_cb();
            //---- Enter your callback code here -----
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            errorCode = 1;
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
        return errorCode;
    }
    //------------------------------------------------------------------------------
    //ListBox specific callbacks
    //------------------------------------------------------------------------------
    //public int  AddCallback (NXOpen.BlockStyler.ListBox list_box)
    //{
    //}
    
    //public int  DeleteCallback(NXOpen.BlockStyler.ListBox list_box)
    //{
    //}
    
    //------------------------------------------------------------------------------
    //------------------------------------------------------------------------------
    //Wizard specific callbacks
    //------------------------------------------------------------------------------
    public int stepNotifyPreCallback(Wizard wizard, int nextStep)
    {
        try
        {
            Part theWorkPart = theSession.Parts.Work;
            View theWorkView = theWorkPart.Views.WorkView;

            if (nextStep == 0)
            {

                // Clear list box
                string[] listBoxMessage = new string[1];
                listBoxMessage[0] = "";
                missingWeldObjectsListBox.SetListItems(listBoxMessage);

                // Show all bodies and unhighlight all objects
                theSession.DisplayManager.ShowByType("SHOW_HIDE_TYPE_SOLID_BODIES", DisplayManager.ShowHideScope.AnyInAssembly);

                if (selectedMissingWeldObjects[0] != null)
                {
                    selectedMissingWeldObjects[0].Unhighlight();
                    selectedMissingWeldObjects[0] = null;
                }
                if (selectedMissingWeldObjects[1] != null)
                {
                    selectedMissingWeldObjects[1].Unhighlight();
                    selectedMissingWeldObjects[1] = null;
                }
                

                foreach (int key in missingWelds.Keys)
                {
                    wizard.RemoveStepSubNode(key);
                }


                if (theClearanceSet != null)
                {
                    theClearanceSet.Delete();
                    theClearanceSet = null;
                }

                wasSubNodeCreated = false;
                missingWelds.Clear();
                checkedSubNodeObjects.Clear();

                theWorkView.Fit();
            }
            else if (nextStep == 1)
            {
                ClearanceAnalysisBuilder clearanceAnalysisBuilder1 = theWorkPart.AssemblyManager.CreateClearanceAnalysisBuilder(null);
                
                // Set parameters
                clearanceAnalysisBuilder1.ClearanceSetName = "Missing Weld Clearance Set";
                clearanceAnalysisBuilder1.CollectionOneRange = ClearanceAnalysisBuilder.CollectionRange.SelectedObjects;

                // Add selected components to CollectionOneObjects
                foreach (TaggedObject tagObj in compSelection.GetSelectedObjects())
                {
                    clearanceAnalysisBuilder1.CollectionOneObjects.Add((Component)tagObj);
                }

                NXObject nXObject1 = clearanceAnalysisBuilder1.Commit();
                clearanceAnalysisBuilder1.Destroy();
                theClearanceSet = (ClearanceSet)nXObject1; // holds the clearance set created by the wizard
                theClearanceSet.PerformAnalysis(ClearanceSet.ReanalyzeOutOfDateExcludedPairs.False);


                // Store the list of welds
                var weldObjects = new List<Tuple<TaggedObject, TaggedObject>>(); // holds the pair of tagged objects involved in each weld feature
                foreach (Feature weldFeature in theWorkPart.Features.WeldManager)
                {
                    NXOpen.Weld.ConnectedPart connectPartsInfo = theSession.WeldCustomManager.AskConnectedParts(weldFeature);
                    // We assume that there are exactly two sets for the weld, with one object in each set
                    NXObject[] id1;
                    connectPartsInfo.GetSetInformation(0, out id1);
                    NXObject[] id2;
                    connectPartsInfo.GetSetInformation(1, out id2);
                    weldObjects.Add(new Tuple<TaggedObject, TaggedObject>(
                        NXOpen.Utilities.NXObjectManager.Get(id1[0].Tag),
                        NXOpen.Utilities.NXObjectManager.Get(id2[0].Tag)));
                }

                // Create a subNode for each missing weld and store the pair of objects involved in the weld.
                // NOTE: The interfering objects in the clearance set, and the objects involved in the weld feature
                // must be components when compared with each other.
                DisplayableObject interferenceComponent1 = null;
                DisplayableObject interferenceComponent2 = null;
                theClearanceSet.GetNextInterference(null, null, out interferenceComponent1, out interferenceComponent2);

                int i = 1;
                int subNodeID;
                string missingWeldName;

                while (interferenceComponent1 != null)
                {
                    bool isMissingWeld = true;
                    foreach (Tuple<TaggedObject, TaggedObject> weldPair in weldObjects)
                    {
                        Body weldBody1 = (Body)weldPair.Item1;
                        Body weldBody2 = (Body)weldPair.Item2;
                        Component weldComponent1 = weldBody1.OwningComponent;
                        Component weldComponent2 = weldBody2.OwningComponent;
                        if ((weldComponent1 == interferenceComponent1 && weldComponent2 == interferenceComponent2)
                            || (weldComponent2 == interferenceComponent1 && weldComponent1 == interferenceComponent2))
                        {
                            isMissingWeld = false;
                            break;
                        }
                    }

                    if (isMissingWeld)
                    {
                        missingWeldName = "Missing weld " + i.ToString();
                        i++;
                        subNodeID = wizard.CreateStepSubNode(1, missingWeldName, "", true, true);
                        missingWelds.Add(subNodeID, new Tuple<DisplayableObject, DisplayableObject>(interferenceComponent1, interferenceComponent2));
                        checkedSubNodeObjects.Add(new Tuple<DisplayableObject, DisplayableObject>(interferenceComponent1, interferenceComponent2));
                        wasSubNodeCreated = true;
                    }

                    theClearanceSet.GetNextInterference(interferenceComponent1, interferenceComponent2, out interferenceComponent1, out interferenceComponent2);
                }

                // If no sub nodes were created, display message
                if (!wasSubNodeCreated)
                {
                    string[] listBoxMessage = new string[1];
                    listBoxMessage[0] = "There are no missing welds.";
                    missingWeldObjectsListBox.SetListItems(listBoxMessage);
                }

                theWorkView.Fit();
            }
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
        
        return 0;
    }

    //public void stepNotifyPostCallback(Wizard wizard, int previousStep)
    //{
    //}

    public bool isStepOkayCallback(Wizard wizard, int step)
    {
        try
        {
            if (wizard.CurrentStep == 0)
            {
                if (compSelection.GetSelectedObjects().Length > 0)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            else if (wizard.CurrentStep == 1)
            {
                return true;
            }
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }

        return false;
    }

    public void onSubNodeCallback(Wizard wizard, int step, int subNodeId, Wizard.SubNodeAction action)
    {
        try
        {
            Part theWorkPart = theSession.Parts.Work;
            View theWorkView = theWorkPart.Views.WorkView;

            // Store the pair of objects from the missing weld associated with this sub node
            // for access by update_cb, apply_cb, and StepNotifyPreCallback methods
            selectedMissingWeldObjects[0] = missingWelds[subNodeId].Item1;
            selectedMissingWeldObjects[1] = missingWelds[subNodeId].Item2;
            var subNodeTuple = new Tuple<DisplayableObject, DisplayableObject>(selectedMissingWeldObjects[0], selectedMissingWeldObjects[1]);

            if (action == Wizard.SubNodeAction.Select)
            {

                // Add the missing weld's objects to list box
                string[] listBoxMessage = new string[2];
                listBoxMessage[0] = selectedMissingWeldObjects[0].Name;
                listBoxMessage[1] = selectedMissingWeldObjects[1].Name;
                missingWeldObjectsListBox.SetListItems(listBoxMessage);
                
                // Get value of compDisplay enum
                PropertyList compDisplayProps = compDisplay.GetProperties();
                int compDisplayValue = compDisplayProps.GetEnum("Value");
                compDisplayProps.Dispose();
                compDisplayProps = null;

                // "Blank" has the enum value of 0
                if (compDisplayValue == 0)
                {

                    // Show only the two objects
                    theSession.DisplayManager.HideByType("SHOW_HIDE_TYPE_SHEET_BODIES", DisplayManager.ShowHideScope.AnyInAssembly);

                    foreach (Feature weldFeature in theWorkPart.Features.WeldManager)
                    {
                        weldFeature.HideBody();
                    }

                    foreach (DisplayableObject d in allObjects)
                    {
                        if (d != selectedMissingWeldObjects[0] && d != selectedMissingWeldObjects[1])
                        {
                            d.Blank();
                        }
                    }

                    theWorkView.Fit();
                }

                // "Highlight" has the enum value of 1
                if (compDisplayValue == 1)
                {
                    theWorkView.Fit();

                    selectedMissingWeldObjects[0].Highlight();
                    selectedMissingWeldObjects[1].Highlight();
                }

            }
            else if (action == Wizard.SubNodeAction.Deselect)
            {

                // Clear list box
                string[] listBoxMessage = new string[1];
                listBoxMessage[0] = "";
                missingWeldObjectsListBox.SetListItems(listBoxMessage);

                // Unhighlight and unblank all bodies
                selectedMissingWeldObjects[0].Unhighlight();
                selectedMissingWeldObjects[1].Unhighlight();

                foreach (Feature weldFeature in theWorkPart.Features.WeldManager)
                {
                    weldFeature.ShowBody(true);
                }

                foreach (DisplayableObject d in allObjects)
                {
                    if (d != selectedMissingWeldObjects[0] && d != selectedMissingWeldObjects[1])
                    {
                        d.Unblank();
                    }
                }

                // Release this pair of objects when the sub node is deselected
                selectedMissingWeldObjects[0] = null;
                selectedMissingWeldObjects[1] = null;
            }
            else if (action == Wizard.SubNodeAction.Check)
            {
                checkedSubNodeObjects.Add(subNodeTuple);
            }
            else if (action == Wizard.SubNodeAction.Uncheck)
            {
                checkedSubNodeObjects.Remove(subNodeTuple);
            }
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
    }
    
    public void onMenuCallback(Wizard wizard, Wizard.TaskNavigatorItem item, int step, int subNodeId)
    {
        try
        {
            TreeListMenu subNodeMenu = missingWeldWizard.CreateMenu();
            if (item == Wizard.TaskNavigatorItem.Step)
            {
                if (wasSubNodeCreated)
                {
                    subNodeMenu.AddMenuItem(0, "Generate Report for Selected Missing Welds");
                    missingWeldWizard.SetMenu(subNodeMenu);
                }
            }
            else if (item == Wizard.TaskNavigatorItem.SubNode)
            {
                subNodeMenu.AddMenuItem(1, "Export Image to PDF");
                missingWeldWizard.SetMenu(subNodeMenu);
            }
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
    }
    
    public void onMenuSelectionCallback(Wizard wizard, Wizard.TaskNavigatorItem item, int step, int subNodeId, int commandIndex)
    {
        try
        {
            Part theWorkPart = theSession.Parts.Work;

            if (commandIndex == 0)
            {
                ListingWindow reportWindow = theSession.ListingWindow;
                reportWindow.Open();
                reportWindow.WriteLine("Missing Welds for " + theSession.Parts.Display.ComponentAssembly.RootComponent.DisplayName + "\n\n");
                reportWindow.WriteLine(checkedSubNodeObjects.Count + " of " + missingWelds.Count + " missing welds selected\n\n");
                reportWindow.WriteLine("     Part 1\t\tPart 2\n\n");

                // Format spacing in report
                // Assumes no more than 999 missing weld pairs
                int i = 1;
                foreach (Tuple<DisplayableObject, DisplayableObject> weldPair in checkedSubNodeObjects)
                {
                    if (i <= 9)
                    {
                        reportWindow.WriteLine(i + ")   " + weldPair.Item1.Name + "\t" + weldPair.Item2.Name);
                        i++;
                    }
                    else if (i <= 99)
                    {
                        reportWindow.WriteLine(i + ")  " + weldPair.Item1.Name + "\t" + weldPair.Item2.Name);
                        i++;
                    }
                    else
                    {
                        reportWindow.WriteLine(i + ") " + weldPair.Item1.Name + "\t" + weldPair.Item2.Name);
                        i++;
                    }
                }
            }
            else if (commandIndex == 1)
            {

                // Get value of compDisplay enum
                PropertyList compDisplayProps = compDisplay.GetProperties();
                int compDisplayValue = compDisplayProps.GetEnum("Value");
                
                // If Highlight is selected, automatically select Blank before creating image
                // "Highlight" has the enum value of 1
                if (compDisplayValue == 1)
                {
                    
                    // "Blank" has the enum value of 0
                    compDisplayProps.SetEnum("Value", 0);

                    // Unhighlight the objects and show only those two objects
                    selectedMissingWeldObjects[0].Unhighlight();
                    selectedMissingWeldObjects[1].Unhighlight();

                    theSession.DisplayManager.HideByType("SHOW_HIDE_TYPE_SHEET_BODIES", DisplayManager.ShowHideScope.AnyInAssembly);

                    foreach (Feature weldFeature in theWorkPart.Features.WeldManager)
                    {
                        weldFeature.HideBody();
                    }

                    foreach (DisplayableObject d in allObjects)
                    {
                        if (d != selectedMissingWeldObjects[0] && d != selectedMissingWeldObjects[1])
                        {
                            d.Blank();
                        }
                    }

                    theWorkPart.Views.WorkView.Fit();
                }

                compDisplayProps.Dispose();
                compDisplayProps = null;


                PrintPDFBuilder printPDFBuilder1 = theWorkPart.PlotManager.CreatePrintPdfbuilder();

                NXObject[] sheets1 = new NXObject[1];
                NXObject nullNXOpen_NXObject = null;
                sheets1[0] = nullNXOpen_NXObject;
                printPDFBuilder1.SourceBuilder.SetSheets(sheets1);

                // Set pdf path to same directory as work part
                string path = System.IO.Path.GetDirectoryName(theWorkPart.FullPath);
                string filename = "MissingWeld_" + selectedMissingWeldObjects[0].Name + "_" + selectedMissingWeldObjects[1].Name + ".pdf";
                printPDFBuilder1.Filename = System.IO.Path.Combine(path, filename);


                NXObject nXObject1 = printPDFBuilder1.Commit();
                printPDFBuilder1.Destroy();
            }
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
    }
    
    
    //------------------------------------------------------------------------------
    //Function Name: AddChildren
    //Recursive function used to add the children of the current component tree
    //node to allObjects
    //------------------------------------------------------------------------------
    public void AddChildren(Component component)
    {
        try
        {
            Component[] childComponents = component.GetChildren();
            for (int i = 0; i < childComponents.Length; ++i)
            {
                allObjects.Add(childComponents[i]);
                AddChildren(childComponents[i]);
            }
        }
        catch (Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
        }
    }
}
