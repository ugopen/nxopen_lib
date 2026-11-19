//=============================================================================
//
//                   Copyright (c) 2012 Siemens PLM Solutions
//                    Unpublished - All rights reserved
//===============================================================================
// This program creates a very simple UDO example.
// 
// It demonstrates each of the following callbacks: 
//     * Display 
//     * Selection 
//     * Attention Point 
//     * Fit 
//     * Edit 
//     * Information 
// 
// In NX execute this program via: File -> Execute -> NX Open... 
// This program begins by opening a new part (if there were no open parts). 
// Next it will prompt you to select a position on the screen. 
// The screen position will be used as a reference point for the UDO. 
// The UDO will display as a triangle on that point with a name 
// "C# UDO" next to the triangle. 
// 
// This UDO is selectable. If you go to Information->Object and select
// the UDO you will see custom information output to the listing window from 
// the function myInfoCB defined in this program. 
// 
// You can also edit the location of the UDO. Start by right-clicking 
// on the UDO and selecting "Edit User Defined Object" from the MB3 popup menu. 
// Editing the UDO will invoke the myEditCB function defined in this program. 
// You will be prompted to select a new screen position, and after you make 
// the selection the UDO will move to the new location. 
//=============================================================================
//
//=============================================================================
using System; 
using NXOpen; 
using NXOpen.UF; 
using NXOpen.UserDefinedObjects; 

public class Program 
{ 
    // class members 
    static Session theSession = null; 
    static UI theUI = null; 
    static UFSession theUFSession = null; 
    static UserDefinedClass myUDOclass = null; 

    //------------------------------------------------------------------------------ 

    // Callback Name: myDisplayCB 
    // This is a callback method associated with displaying a UDO. 
    // This same callback is registered for display, select, fit, and attention point 
    //------------------------------------------------------------------------------ 

    public static int myDisplayCB(UserDefinedDisplayEvent displayEvent)
    { 
        try 
        { 
            // Get the doubles used to define the selected screen position for this UDO. 
            double[] myUDOdoubles = displayEvent.UserDefinedObject.GetDoubles(); 

            // Use the doubles to define points of a triangle 
            Point3d[] myPoints = new Point3d[4]; 
            myPoints[0].X = myUDOdoubles[0] + 0; 
            myPoints[0].Y = myUDOdoubles[1] + 0; 
            myPoints[0].Z = myUDOdoubles[2] + 0; 

            myPoints[1].X = myUDOdoubles[0] + 100; 
            myPoints[1].Y = myUDOdoubles[1] + 0; 
            myPoints[1].Z = myUDOdoubles[2] + 0; 

            myPoints[2].X = myUDOdoubles[0] + 0; 
            myPoints[2].Y = myUDOdoubles[1] + 100; 
            myPoints[2].Z = myUDOdoubles[2] + 0; 

            myPoints[3].X = myUDOdoubles[0] + 0; 
            myPoints[3].Y = myUDOdoubles[1] + 0; 
            myPoints[3].Z = myUDOdoubles[2] + 0; 

            // Display the triangle 
            displayEvent.DisplayContext.DisplayPolyline(myPoints); 

            // Display the text next to the triangle 
            Point3d myPt = new Point3d(); 
            myPt.X = myUDOdoubles[0] + 100; 
            myPt.Y = myUDOdoubles[1] + 0; 
            myPt.Z = myUDOdoubles[2] + 0; 
            displayEvent.DisplayContext.DisplayText("C# UDO", myPt, 0); 
        } 
        catch (NXOpen.NXException ex) 
        { 
            // ---- Enter your exception handling code here ----- 
            UI.GetUI().NXMessageBox.Show("Caught exception", 
                     NXMessageBox.DialogType.Error, ex.Message); 
        } 
        return 0; 
    } 
    //------------------------------------------------------------------------------ 

    // Callback Name: myEditCB 
    // This is a callback method associated with editing a UDO. 
    //------------------------------------------------------------------------------ 

    public static int myEditCB(UserDefinedEvent editEvent) 
    { 
        try 
        { 
            View myView = null; 
            Point3d myCursor; 
            myCursor.X = 0; 
            myCursor.Y = 0; 
            myCursor.Z = 0; 

            // highlight the current udo we are about to edit 
            // this is helpful if multiple udo's were on the selection 
            // list when the user decided to edit them 
            editEvent.UserDefinedObject.Highlight(); 

            // ask the user to select a new origin for this UDO 
            Selection.DialogResponse myResponse = 
theUI.SelectionManager.SelectScreenPosition("Select New Origin for C# UDO", out myView, out myCursor); 
            // we are done asking the user for input... unhighlight the udo 
            editEvent.UserDefinedObject.Unhighlight(); 

            // use the new screen position (if the user picked one) 
            if( myResponse == Selection.DialogResponse.Pick ) 
            { 
                double[] myUDOdoubles = new double[3]; 
                myUDOdoubles[0] = myCursor.X; 
                myUDOdoubles[1] = myCursor.Y; 
                myUDOdoubles[2] = myCursor.Z; 
                // store the newly selected origin with the udo 
                editEvent.UserDefinedObject.SetDoubles(myUDOdoubles); 

                // add the udo to the display list manually 
                // this will force the udo display to regenerate 
                // immediately and show the changes we just made 
                theUFSession.Disp.AddItemToDisplay
(editEvent.UserDefinedObject.Tag); 
            } 
        } 
        catch (NXOpen.NXException ex) 
        { 
            // ---- Enter your exception handling code here ----- 
            UI.GetUI().NXMessageBox.Show("Caught exception", 
                   NXMessageBox.DialogType.Error, ex.Message); 
        } 
        return 0; 
    } //------------------------------------------------------------------------------ /

    // Callback Name: myInfoCB 
    // This is a callback method associated with querying information for a UDO. 
    // The information is printed in the listing window. 
    //------------------------------------------------------------------------------ 

    public static int myInfoCB(UserDefinedEvent infoEvent) 
    { 
        try 
    { 
        ListingWindow 
        theLW = theSession.ListingWindow; 
        theLW.Open(); theLW.WriteLine(" "); 
        theLW.WriteLine("------------------------------------------------------------"); 
        theLW.WriteLine("Begin Custom Information"); 
        theLW.WriteLine(" "); 
        theLW.WriteLine("UDO Class Name: '" + 
                  infoEvent.UserDefinedObject.UserDefinedClass.ClassName + "'"); 
        theLW.WriteLine("UDO Friendly Name: '" + 
                  infoEvent.UserDefinedObject.UserDefinedClass.FriendlyName + "'"); 
        double[] myUDOdoubles = infoEvent.UserDefinedObject.GetDoubles();
        theLW.WriteLine("myUDOdoubles(0) = " + myUDOdoubles[0]); 
        theLW.WriteLine("myUDOdoubles(1) = " + myUDOdoubles[1]); 
        theLW.WriteLine("myUDOdoubles(2) = " + myUDOdoubles[2]); 
        theLW.WriteLine(" "); theLW.WriteLine("End Custom Information"); 
    } 
    catch (NXOpen.NXException ex) 
    { 
        // ---- Enter your exception handling code here ----- 
        UI.GetUI().NXMessageBox.Show("Caught exception", 
NXMessageBox.DialogType.Error, ex.Message); 
    } 
    return 0; 
} 
//------------------------------------------------------------------------------ 
// initUDO // Checks to see which (if any) of the application's static variables are 
// uninitialized, and sets them accordingly. 
// Initializes the UDO class and registers all of its callback methods. 
//------------------------------------------------------------------------------ 
static int initUDO( bool alertUser) 
{ 
    try 
    { 
        if (theSession == null) 
        { 
            theSession = Session.GetSession(); 
        } 
        if( theUI == null ) 
        { 
            theUI = UI.GetUI(); 
        } 
        if( theUFSession == null ) 
        { 
        theUFSession = UFSession.GetUFSession(); 
        } 
        if (myUDOclass == null) 
        { 
            if (alertUser) 
            { 
                ListingWindow theLW = theSession.ListingWindow; 
                theLW.Open(); 
                theLW.WriteLine("Registering C# UDO Class"); 
            } 
            // Define your custom UDO class 
            myUDOclass = theSession.UserDefinedClassManager.CreateUserDefinedObjectClass
                          ("Sample_CSharp_UDO", "Sample C# UDO"); 
            // Setup properties on the custom UDO class 
            myUDOclass.AllowQueryClassFromName = UserDefinedClass.AllowQueryClass.On; 
            // Register callbacks for the UDO class 
            myUDOclass.AddDisplayHandler(new UserDefinedClass.DisplayCallback(Program.myDisplayCB)); 
            myUDOclass.AddAttentionPointHandler(new UserDefinedClass.DisplayCallback   (Program.myDisplayCB)); 
            myUDOclass.AddFitHandler(new UserDefinedClass.DisplayCallback
(Program.myDisplayCB)); 
            myUDOclass.AddSelectionHandler(new 
UserDefinedClass.DisplayCallback(Program.myDisplayCB)); 
            myUDOclass.AddEditHandler(new UserDefinedClass.GenericCallback(Program.myEditCB)); 
            myUDOclass.AddInformationHandler(new 
UserDefinedClass.GenericCallback(Program.myInfoCB)); 
            // Add this class to the list of object types available for selection in NX. 
            // If you skip this step you won't be able to select UDO's of this class, 
            // even though you registered a selection callback. 
            theUI.SelectionManager.SetSelectionStatusOfUserDefinedClass(myUDOclass, true); 
        } 
    } 
    catch (NXOpen.NXException ex) 
    { 
        // ---- Enter your exception handling code here ----- 
        UI.GetUI().NXMessageBox.Show("Caught exception", NXMessageBox.DialogType.Error, ex.Message); 
    } 
    return 0; 
} 
//------------------------------------------------------------------------------ 

// Main (Explicit Activation) 
// This entry point is used to activate the application explicitly, as in 
// "File->Execute UG/Open->NX Open..." 
//------------------------------------------------------------------------------ 
public static int Main(string[] args) 
{ 
    int retValue = 0; 
    try 
    { 
        // initialize the UDO - if we didn't load this library at 
        // startup, here is our second chance to load it 
        initUDO(true); 

        // if we don't have any parts open create one 
        BasePart myBasePart = theSession.Parts.BaseDisplay; 
        if( myBasePart == null) 
        { myBasePart = theSession.Parts.NewBaseDisplay
("test_csharp_udo.prt", BasePart.Units.Millimeters); 
        } 

        View myView = null; 
        Point3d myCursor; 
        myCursor.X = 0; 
        myCursor.Y = 0; 
        myCursor.Z = 0; 
        // ask the user to select an origin for this UDO 
        Selection.DialogResponse myResponse = 
theUI.SelectionManager.SelectScreenPosition("Select Origin of C# UDO", out myView, out myCursor); 
        if
        ( myResponse == Selection.DialogResponse.Pick ) 
        { 
        // The user selected a point - go ahead and create the udo 
    UserDefinedObjectManager myUDOmanager = myBasePart.UserDefinedObjectManager; 
        UserDefinedObject firstUDO = myUDOmanager.CreateUserDefinedObject(myUDOclass); 
        // set the color property of the udo - just for fun :) 
        firstUDO.Color = 36; 
        // store the origin selected by the user with the udo 
        double[] myUDOdoubles = new double[3]; 
        myUDOdoubles[0] = myCursor.X; 
        myUDOdoubles[1] = myCursor.Y; 
        myUDOdoubles[2] = myCursor.Z; 
        firstUDO.SetDoubles(myUDOdoubles); 
        // add the udo to the display list manually 
        // this will force the udo to display immediately 
        theUFSession.Disp.AddItemToDisplay(firstUDO.Tag); 
    } 
        } 
        catch (NXOpen.NXException ex) 
        {
            // ---- Enter your exception handling code here ----- 
            UI.GetUI().NXMessageBox.Show("Caught exception", 
NXMessageBox.DialogType.Error, ex.Message); 
        } 
        return retValue; 
    } 
    //------------------------------------------------------------------------------ 

    // Startup 
    // Entrypoint used when program is loaded automatically 
    // as NX starts up. Note this application must be placed in a 
    // special folder for NX to find and load it during startup. 
    // Refer to the NX Open documentation for more details on how 
    // NX finds and loads applications during startup. 
    //------------------------------------------------------------------------------ 

    public static int Startup() 
    { 
        int retValue = 0; 
        try 
    { 
        initUDO(false); 
    } 
    catch (NXOpen.NXException ex) 
    { 
        // ---- Enter your exception handling code here ----- 
        UI.GetUI().NXMessageBox.Show("Caught exception", 
NXMessageBox.DialogType.Error, ex.Message); 
    } 
    return retValue; 
    } 

    //------------------------------------------------------------------------------ 

    // GetUnloadOption 
    // Make sure you specify AtTermination for the unload option. 
    // If you unload the library before the NX Session Terminates 
    // bad things could happen when we try to execute a udo 
    // callback that no longer exists in the session. 
    //------------------------------------------------------------------------------ 

    public static int GetUnloadOption(string arg) 
    { 
        //Unloads the image when the NX session terminates 
        return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination); 
    } 
}
