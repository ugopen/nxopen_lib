
//=============================================================================
//
//                    Copyright (c) 2017 Siemens PLM Solutions
//                    Unpublished - All rights reserved
//
//===============================================================================
//
// File description: Java version of SelectionSubscriber.cpp
//
// This example instantiates a SelectionSubscriber that is left loaded until the
// session terminates. 
//
// Any time the set of selected objects changes due to any user interaction, the
// SelectionSubscriber will print the current selected set of tags out to the Listing Window.
//
// The callback code may be executed while in Global Selection, or while in a command. It may be
// executed with or without objects already selected.
//
// No additional files are required to build or execute the Java code.
// There are no OS specific instructions.
//
//===============================================================================
//

import java.rmi.RemoteException;
import java.util.HashMap;
import java.util.Map;

import nxopen.BaseSession;
import nxopen.ListingWindow;
import nxopen.LogFile;
import nxopen.NXException;
import nxopen.Selection;
import nxopen.SelectionSubscriber;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.Tag;
import nxopen.UI;
import nxopen.TaggedObject;

//------------------------------------------------------------------------------
//NXOpen SelectionSubscriber java test class 
//------------------------------------------------------------------------------
public class SelectionSubscriberExample implements SelectionSubscriber.OnSelectionChangeCallback {
    public static SelectionSubscriberExample theSelectionSubscriber = null;
    public static Session theSession = null;
    public static ListingWindow lw = null;
    public static UI theUI = null;

    private static SelectionSubscriber selSub = null;
    private static Selection selMgr = null;
    private static Map<Tag, TaggedObject> myMap = new HashMap<Tag, TaggedObject>();

    private static LogFile lf = null;

    // constructor
    public SelectionSubscriberExample() throws NXException, RemoteException {
        try {
            // Initialize the NX Open Java API environment
            theSession = (Session) SessionFactory.get("Session");
            theUI = (UI) SessionFactory.get("UI");
            lw = theSession.listingWindow();
            lf = theSession.logFile();

            // Get the SelectionManager and use it to create a
            // SelectionSubscriber.
            selMgr = theUI.selectionManager();
            selSub = selMgr.createSelectionSubscriber();

            // Register this class as implementing the 
            // onSelectionChangeCallback for the subscriber object.
            selSub.registerOnSelectionChangeCallback(this);

            // Deactivate the SelectionSubscriber until activated by doIt().
            selSub.deactivate();
            if (!selSub.isActive())
                print("SelectionSubscriber is DeActivated. onSelectionChangeCallback will NOT be called.");
        } catch (Exception e) {
            StackTraceElement[] stackTrace = e.getStackTrace();
            if (SelectionSubscriberExample.lf != null) {
                SelectionSubscriberExample.lf.writeLine(e.getMessage());
                for (StackTraceElement elem : stackTrace) {
                    lf.writeLine(elem.toString());
                }
            }
        }
    }

    public void doIt() throws NXException, RemoteException {
        try {
            selSub.activate();
            if (selSub.isActive()) {
                print("SelectionSubscriber is Active again!");
            }

            // Load myList with all currently selected objects in the active
            // command, or if no active command then in Global Selection.
            int selCount = selMgr.getNumSelectedObjects();
            for (int ii = 0; ii < selCount; ++ii) {
                TaggedObject obj = selMgr.getSelectedTaggedObject(ii);
                myMap.put(obj.tag(), obj);
            }

            // Copy the set into a local vector, just to illustrate usage of
            // request* methods below.
            TaggedObject[] objArray = new nxopen.TaggedObject[myMap.size()];
            objArray = myMap.values().toArray(objArray);

            // No net change to the selected set here; just demonstrating APIs.
            selMgr.requestDeselections(objArray);
            print(String.format("After selMgr.requestDeselections(objArray): selected count = %1$d", 
                    selMgr.getNumSelectedObjects()));

            selMgr.requestSelections(objArray);
            print(String.format("After selMgr.requestSelections(objArray): selected count = %1$d",
                    selMgr.getNumSelectedObjects()));

            // If Global Selection is active, clear and repopulate the Global
            // Selection select set.
            if (selMgr.isGlobalSelectionActive()) {
                print("Global Selection IS Active.");

                selMgr.clearGlobalSelectionList();
                print(String.format("After selMgr.clearGlobalSelectionList(): selected count = %1$d",
                        selMgr.getNumSelectedObjects()));

                selMgr.requestSelections(objArray);
                print(String.format("After selMgr.requestSelections(objArray): selected count = %1$d",
                        selMgr.getNumSelectedObjects()));
            } else {
                print("Global Selection is NOT Active.");
            }
        } catch (Exception e) {
            StackTraceElement[] stackTrace = e.getStackTrace();
            if (SelectionSubscriberExample.lf != null) {
                SelectionSubscriberExample.lf.writeLine(e.getMessage());
                for (StackTraceElement elem : stackTrace) {
                    lf.writeLine(elem.toString());
                }
            }
        }
    }

    public void print(String nxString) throws NXException, RemoteException {
        if (!lw.isOpen())
            lw.open();
        lw.writeLine(nxString);
        // Write string to log file for debugging purposes. 
        // Comment out the following line if desired.
        lf.writeLine(nxString);
    }

    public void onSelectionChangeCallback(boolean clearAll, TaggedObject[] deselectedObjects,
            TaggedObject[] selectedObjects) throws NXException, RemoteException {
        try {
            // Query whether or not Global Selection (the state of NOT being in
            // a command) is active.
            boolean globalSelectionActive = selMgr.isGlobalSelectionActive();
            int numDeselectedObjects = deselectedObjects == null ? 0 : deselectedObjects.length;
            int numSelectedObjects = selectedObjects == null ? 0 : selectedObjects.length;

            print(String.format("onSelectionChangeCB: (%s Global Selection)", globalSelectionActive ? "IN" : "NOT IN"));
            print(String.format("clearAll = %s;  deselectedObjects size = %d; selectedObjects size = %d", 
                clearAll ? "true" : "false", numDeselectedObjects, numSelectedObjects));

            if (clearAll) {
                myMap.clear();
            }
            else {
                print(String.format("Deselected count = %d", numDeselectedObjects));
                for (TaggedObject deselObj : deselectedObjects) {
                    print(String.format("%d", deselObj.tag().value));
                    myMap.remove(deselObj.tag());
                }
            }

            // Always check selectedObjects, even if clearAll was true.

            for (TaggedObject selObj : selectedObjects) {
                myMap.put(selObj.tag(), selObj);
            }

            print(String.format("Selected count = %d", myMap.size()));

            for (TaggedObject obj : myMap.values()) {
                print(String.format("%d", obj.tag().value));
            }
        } catch (Exception e) {
            StackTraceElement[] stackTrace = e.getStackTrace();
            if (SelectionSubscriberExample.lf != null) {
                SelectionSubscriberExample.lf.writeLine(e.getMessage());
                for (StackTraceElement elem : stackTrace) {
                    lf.writeLine(elem.toString());
                }
            }
        }
    }

    // Called manually from File->Execute->NX Open
    public static void main(String[] args) {
        try {
            if (theSelectionSubscriber == null) {
                theSelectionSubscriber = new SelectionSubscriberExample();
                theSelectionSubscriber.doIt();
            }
        } catch (Exception e) {
        }
    }

    public void dispose() throws NXException, RemoteException {
        print("SelectionSubscriber.dispose() called");

    }

    public static final int getUnloadOption() {
        return BaseSession.LibraryUnloadOption.AT_TERMINATION;
    }
}
