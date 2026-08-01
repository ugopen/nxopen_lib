
//=============================================================================
//
//                    Copyright (c) 2017 Siemens PLM Solutions
//                    Unpublished - All rights reserved
//
//===============================================================================
//
// NX Open .NET example to demonstrate using SelectionSubscriber
//
// This example instantiates a SelectionSubscriber that is left loaded until the
// session terminates. 
//
// Any time the set of selected objects changes due to any user interaction, the
// callback registered with the SelectionSubscriber will print the tags of the
// current set of selected objects out to the Listing Window.
//
// The callback code may be executed while in Global Selection, or while in a command. 
// It may be executed with or without objects already selected.
//
// No additional files are required to build or execute the C# code.
// There are no OS specific instructions.
//
//===============================================================================
//

using System;
using NXOpen;

//------------------------------------------------------------------------------
//NXOpen SelectionSubscriber C# test class 
//------------------------------------------------------------------------------
public class SelectionSubscriberExample 
{
    public static SelectionSubscriberExample theSelectionSubscriber = null;
    public static Session theSession = null;
    public static ListingWindow lw = null;
    public static UI theUI = null;

    private static SelectionSubscriber selSub = null;
    private static Selection selMgr = null;
    private static System.Collections.Generic.Dictionary<Tag, TaggedObject> mySet = new System.Collections.Generic.Dictionary<Tag, TaggedObject>();

    private static LogFile lf = null;

    // constructor
    public SelectionSubscriberExample()
    {
        try 
        {
            // Initialize the NX Open .Net API environment
            theSession = Session.GetSession();
            theUI = UI.GetUI();
            lw = theSession.ListingWindow;
            lf = theSession.LogFile;

            // Get the Selection Manager pointer, and use it to create a
            // SelectionSubscriber.
            selMgr = theUI.SelectionManager;
            selSub = selMgr.CreateSelectionSubscriber();

            // Register this class as implementing the 
            // onSelectionChangeCallback for the subscriber object.
            selSub.RegisterOnSelectionChangeCallback(new SelectionSubscriber.OnSelectionChangeCallback(selection_cb));

            // Deactivate the SelectionSubscriber until activated by DoIt().
            selSub.Deactivate();
            if (!selSub.IsActive())
            {
                Print("SelectionSubscriber is Deactivated. onSelectionChangeCallback will NOT be called.");
            }
        } 
        catch (Exception ex) 
        {
            throw ex;
        }
    }

    public void DoIt()
    {
        try 
        {
            selSub.Activate();
            if (selSub.IsActive())
            {
                Print("SelectionSubscriber is Active again!");
            }

            // Load myList with all currently selected objects in the active
            // command, or if no active command then in Global Selection.
            int selCount = selMgr.GetNumSelectedObjects();
            for (int ii = 0; ii < selCount; ++ii) 
            {
                TaggedObject obj = selMgr.GetSelectedTaggedObject(ii);
                mySet.Add(obj.Tag, obj);
            }

            // Copy the set into a local vector, just to illustrate usage of
            // the Request* methods below.
            TaggedObject[] objArray = new TaggedObject[mySet.Count];
            mySet.Values.CopyTo(objArray, 0);

            // No net change to the selected set here; just demonstrating APIs.
            selMgr.RequestDeselections(objArray);
            Print(String.Format("After selMgr.RequestDeselections(objArray): selected count = {0:d}", selMgr.GetNumSelectedObjects()));

            selMgr.RequestSelections(objArray);
            Print(String.Format("After selMgr.RequestSelections(objArray): selected count = {0:d}", selMgr.GetNumSelectedObjects()));

            // If Global Selection is active, clear and repopulate the Global
            // Selection select set.
            if (selMgr.IsGlobalSelectionActive())
            {
                Print("Global Selection IS Active.");

                selMgr.ClearGlobalSelectionList();
                Print(String.Format("After selMgr.ClearGlobalSelectionList(): selected count = {0:d}", selMgr.GetNumSelectedObjects()));

                selMgr.RequestSelections(objArray);
                Print(String.Format("After selMgr.RequestSelections(objArray): selected count = {0:d}", selMgr.GetNumSelectedObjects()));
            } 
            else 
            {
                Print("Global Selection is NOT Active.");
            }
        } 
        catch (Exception ex) 
        {
            lf.WriteLine(String.Format("Exception in DoIt method: {0}", ex.Message));
            lf.WriteLine(ex.StackTrace);
        }
    }

    public void Print(String nxString)
    {
        if (!lw.IsOpen)
            lw.Open();
        lw.WriteLine(nxString);
        // Write string to log file for debugging purposes. Comment out
        // the following line if desired.
        lf.WriteLine(nxString);
    }

    public void selection_cb(bool clearAll, TaggedObject[] deselectedObjects, TaggedObject[] selectedObjects)
    {
        try 
        {
            // Query whether or not Global Selection (the state of NOT being in
            // a command) is active.
            bool globalSelectionActive = selMgr.IsGlobalSelectionActive();
            int numDeselectedObjects = deselectedObjects == null ? 0 : deselectedObjects.Length;
            int numSelectedObjects = selectedObjects == null ? 0 : selectedObjects.Length;

            Print(String.Format("onSelectionChangeCallback: ({0} Global Selection)", globalSelectionActive ? "IN" : "NOT IN"));
            Print(String.Format("clearAll = {0}; number of deselectedObjects is {1:d}; number of selectedObjects is {2:d}", 
                clearAll ? "true" : "false", numDeselectedObjects, numSelectedObjects));

            if (clearAll)
            {
                mySet.Clear();
            }
            else
            {
                Print(String.Format("Deselected count = {0:d}", numDeselectedObjects));
                if (deselectedObjects.Length <= 20)
                {
                    foreach (TaggedObject deselObj in deselectedObjects)
                    {
                        Print(String.Format("{0:d}", deselObj.Tag));
                    }
                }
                foreach (TaggedObject deselObj in deselectedObjects)
                {
                    mySet.Remove(deselObj.Tag);
                }
            }

            // Always check selectedObjects, even if clearAll was true.

            foreach (TaggedObject selObj in selectedObjects)
            {
                mySet.Add(selObj.Tag, selObj);
            }

            Print(String.Format("Selected count = {0:d}", mySet.Count));
            if (mySet.Count <= 20)
            {
                foreach (TaggedObject obj in mySet.Values)
                {
                    Print(String.Format("{0:d}", obj.Tag));
                }
            }
        }
        catch (Exception ex)
        {
            lf.WriteLine(String.Format("Exception in DoIt method: {0}", ex.Message));
            lf.WriteLine(ex.StackTrace);
        }
    }

    // Called manually from File->Execute->NX Open
    public static void Main(String[] args)
    {
        try
        {
            if (theSelectionSubscriber == null)
            {
                theSelectionSubscriber = new SelectionSubscriberExample();
                theSelectionSubscriber.DoIt();
            }
        }
        catch (Exception ex)
        {
            UI.GetUI().NXMessageBox.Show("Exception", NXMessageBox.DialogType.Error, ex.Message);
        }
    }

    public void Dispose()
    {
        Print("SelectionSubscriber.Dispose() called");
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
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);
        return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
    }
}

