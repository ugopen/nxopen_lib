//=============================================================================
//
//                   Copyright (c) 2012 Siemens PLM Solutions
//                    Unpublished - All rights reserved
//===============================================================================
// This program creates a very simple UDO example. 
// 
// It demonstrates each of the following callbacks: 
// * Display 
// * Selection 
// * Attention Point 
// * Fit 
// * Edit 
// * Information 
// 
// In NX execute this program via: File -> Execute -> NX Open... 
// This program begins by opening a new part (if there were no open parts). 
// Next it will prompt you to select a position on the screen. 
// The screen position will be used as a reference point for the UDO. 
// The UDO will display as a triangle on that point with a name 
// "C++ UDO" next to the triangle. 
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
/* Include files */ 
#include <sstream>
#include <iostream>
using std::ostringstream;
using std::endl;    
using std::ends;
using std::cerr;

#include <uf.h>
#include <uf_ui.h>
#include <uf_exit.h> 
#include <uf_disp.h>  
#include <vector>
#include <iostream>
#include <sstream>

#include <NXOpen/Session.hxx>  
#include <NXOpen/Part.hxx> 
#include <NXOpen/PartCollection.hxx>  
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx> 
#include <NXOpen/UI.hxx> 
#include <NXOpen/Selection.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/View.hxx>

#include <NXOpen/UserDefinedObjects_UserDefinedClass.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedClassManager.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedObject.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedObjectManager.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedEvent.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedDisplayEvent.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedLinkEvent.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedObjectDisplayContext.hxx> 

using namespace NXOpen; 
using namespace NXOpen::UserDefinedObjects; 
//static variables 
static NXOpen::Session* theSession = NULL; 
static UI* theUI = NULL; 
static UserDefinedClass* myUDOclass = NULL; 

//------------------------------------------------------------------------------ 
// Callback Name: myDisplayCB 
// This is a callback method associated with displaying a UDO. 
// This same callback is registered for display, select, fit, and attention point 
//------------------------------------------------------------------------------ 
extern int myDisplayCB(UserDefinedDisplayEvent*  displayEvent) 
{ 
    try 
    { 
        // Get the doubles used to define the selected screen position for this UDO. 
        std::vector<double> myUDOdoubles = displayEvent->UserDefinedObject()->GetDoubles(); 
        
        // Use the doubles to define points of a triangle 
        std::vector<Point3d> myPoints(4); 
        
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

        UserDefinedObjectDisplayContext* dispContext = displayEvent->DisplayContext();
        
        // Display the triangle 
        dispContext->DisplayPolyline(myPoints); 
        
        // Display the text next to the triangle 
        Point3d myPt = Point3d(myUDOdoubles[0] + 100, myUDOdoubles[1], myUDOdoubles[2]); 
        dispContext->DisplayText("C++ UDO", myPt, UserDefinedObjectDisplayContext::TextRefBottomLeft); 
        delete dispContext;
        delete displayEvent;
    } 
    catch (NXException ex) 
    { 
        // ---- Enter your exception handling code here ----- 
        cerr << "Caught exception: " << ex.Message() << endl; 
    } 
    return 0; 
} 
//------------------------------------------------------------------------------ 
// Callback Name: myEditCB 
// This is a callback method associated with editing a UDO. 
//------------------------------------------------------------------------------ 
extern int myEditCB(UserDefinedEvent* editEvent) 
{ 
    try 
    { 
        // required for calls to legacy UF routines 
        // such as UF_DISP_add_item_to_display 
        UF_initialize(); 
        
        View* myView = NULL; 
        Point3d myCursor(0,0,0); 
        
        // highlight the current udo we are about to edit 
        // this is helpful if multiple udo's were on the selection 
        // list when the user decided to edit them 
        editEvent->UserDefinedObject()->Highlight(); 
        
        // ask the user to select a new origin for this UDO 
        Selection::DialogResponse myResponse = theUI->SelectionManager()->SelectScreenPosition("Select New Origin for C++ UDO", &myView, &myCursor); 
        // we are done asking the user for input... unhighlight the udo 
        editEvent->UserDefinedObject()->Unhighlight(); 
        
        // use the new screen position (if the user picked one) 
        if( myResponse == Selection::DialogResponsePick ) 
        { 
            std::vector<double> myUDOdoubles(3); 
            myUDOdoubles[0] = myCursor.X; 
            myUDOdoubles[1] = myCursor.Y; 
            myUDOdoubles[2] = myCursor.Z; 
            // store the newly selected origin with the udo 
            editEvent->UserDefinedObject()->SetDoubles(myUDOdoubles); 
            // add the udo to the display list manually 
            // this will force the udo display to regenerate 
            // immediately and show the changes we just made 
            UF_DISP_add_item_to_display(editEvent->UserDefinedObject()->Tag()); 
        } 
        UF_terminate(); 
        delete editEvent;
    } catch (NXException ex) 
    { 
        // ---- Enter your exception handling code here ----- 
        cerr << "Caught exception: " << ex.Message() << endl; 
    } return 0; 
} 
//------------------------------------------------------------------------------ 
// Callback Name: myInfoCB 
// This is a callback method associated with querying information for a UDO. 
// The information is printed in the listing window. 
//------------------------------------------------------------------------------ 
extern int myInfoCB(UserDefinedEvent* infoEvent) 
{ 
    try 
    { 
        ListingWindow* theLW = theSession->ListingWindow(); 
        char msg[256]; 
        theLW->Open(); 
        theLW->WriteLine(" "); 
        theLW->WriteLine("------------------------------------------------------------"); 
        theLW->WriteLine("Begin Custom Information"); 
        theLW->WriteLine(" "); 
        NXOpen::NXString formattedMessage;
        formattedMessage = "UDO Class Name: " + (infoEvent->UserDefinedObject()->UserDefinedClass()->ClassName()); 
        theLW->WriteLine(formattedMessage); 
        formattedMessage = "UDO Friendly Name: " + infoEvent->UserDefinedObject()->UserDefinedClass()->FriendlyName();
        theLW->WriteLine(formattedMessage); 
        std::vector<double> myUDOdoubles = infoEvent->UserDefinedObject()->GetDoubles(); 
        std::ostringstream DoubleBuffer; 
        DoubleBuffer << myUDOdoubles[0]; 
        formattedMessage = DoubleBuffer.str(); 
        theLW->WriteLine(formattedMessage); 
        DoubleBuffer.str("");
        DoubleBuffer.clear();
        DoubleBuffer << myUDOdoubles[1]; 
        formattedMessage = DoubleBuffer.str();  
        theLW->WriteLine(formattedMessage); 
        DoubleBuffer.str("");
        DoubleBuffer.clear();
        DoubleBuffer << myUDOdoubles[2]; 
        formattedMessage = DoubleBuffer.str();  
        theLW->WriteLine(formattedMessage); 
        theLW->WriteLine(" "); 
        theLW->WriteLine("End Custom Information"); 
        delete infoEvent;
    } 
    catch (NXException ex) 
    { 
        // ---- Enter your exception handling code here ----- 
        cerr << "Caught exception: " << ex.Message() << endl; 
    } 
    return 0; 
} 

//------------------------------------------------------------------------------ 
// initUDO 
// Checks to see which (if any) of the application's static variables are 
// uninitialized, and sets them accordingly. 
// Initializes the UDO class and registers all of its callback methods. 
//------------------------------------------------------------------------------ 
static int initUDO( bool alertUser) 
{ 
    try 
    { 
        if (theSession == NULL) 
        { 
            theSession = Session::GetSession(); 
        } 
        if( theUI == NULL ) 
        { 
            theUI = UI::GetUI(); 
        } 
        if (myUDOclass == NULL) 
        { 
            if (alertUser) 
            { 
                ListingWindow* 
                theLW = theSession->ListingWindow(); 
                theLW->Open(); 
                theLW->WriteLine("Registering C++ UDO Class"); 
            } 
            // Define your custom UDO class 
            myUDOclass = theSession->UserDefinedClassManager()->CreateUserDefinedObjectClass("Sample_Cpp_UDO", "Sample C++ UDO"); 
            // Setup properties on the custom UDO class 
            myUDOclass->SetAllowQueryClassFromName(UserDefinedClass::AllowQueryClassOn); 
            // Register callbacks for the UDO class 
            myUDOclass->AddDisplayHandler(make_callback(&myDisplayCB)); 
            myUDOclass->AddAttentionPointHandler(make_callback(&myDisplayCB)); 
            myUDOclass->AddFitHandler(make_callback(&myDisplayCB)); 
            myUDOclass->AddSelectionHandler(make_callback(&myDisplayCB)); 
            myUDOclass->AddEditHandler(make_callback(&myEditCB)); 
            myUDOclass->AddInformationHandler(make_callback(&myInfoCB)); 
            // Add this class to the list of object types available for selection in NX. 
            // If you skip this step you won't be able to select UDO's of this class, 
            // even though you registered a selection callback. 
            theUI->SelectionManager()->SetSelectionStatusOfUserDefinedClass(myUDOclass, true); 
        } 
    } 
    catch (NXException ex) 
    { 
        // ---- Enter your exception handling code here ----- 
        cerr << "Caught exception: " << ex.Message() << endl; 
    } 
    return 0; 
} 

//------------------------------------------------------------------------------ 
// ufusr (Explicit Activation) 
// This entry point is used to activate the application explicitly, as in 
// "File->Execute UG/Open->NX Open..." 
//------------------------------------------------------------------------------ 
extern void ufusr( char *parm, int *returnCode, int rlen ) 
{ 
    try 
    { 
        // required for calls to legacy UF routines 
        // such as UF_DISP_add_item_to_display 
        UF_initialize(); 
        
        // initialize the UDO - if we didn't load this library at 
        // startup, here is our second chance to load it 
        initUDO(true); 
        
        // if we don't have any parts open create one 
        BasePart* myBasePart = theSession->Parts()->BaseDisplay(); 
        if( myBasePart == NULL) 
        { 
            myBasePart = theSession->Parts()->NewBaseDisplay("test_cpp_udo.prt", BasePart::UnitsMillimeters); 
        } 
        
        View* myView = NULL; 
        Point3d myCursor(0,0,0); 
        
        // ask the user to select an origin for this UDO 
        Selection::DialogResponse myResponse = theUI->SelectionManager()->SelectScreenPosition("Select Origin of C++ UDO", &myView, &myCursor); 
        if( myResponse == Selection::DialogResponsePick ) 
        { 
            // The user selected a point - go ahead and create the udo 
            UserDefinedObjectManager* myUDOmanager = myBasePart->UserDefinedObjectManager(); 
            UserDefinedObject* firstUDO = myUDOmanager->CreateUserDefinedObject(myUDOclass); 
            // set the color property of the udo - just for fun :) 
            firstUDO->SetColor(36); 
            // store the origin selected by the user with the udo 
            std::vector<double> myUDOdoubles(3); 
            myUDOdoubles[0] = myCursor.X; 
            myUDOdoubles[1] = myCursor.Y; 
            myUDOdoubles[2] = myCursor.Z; 
            firstUDO->SetDoubles(myUDOdoubles); 
            // add the udo to the display list manually 
            // this will force the udo to display immediately 
            UF_DISP_add_item_to_display(firstUDO->Tag()); 
        } 
        UF_terminate(); 
    } 
    catch (const NXOpen::NXException& ex) 
    { 
        cerr << "Caught exception: " << ex.Message() << endl; 
    } 
} 

//------------------------------------------------------------------------------ 
// ufsta 
// Entrypoint used when program is loaded automatically 
// as NX starts up. Note this application must be placed in a 
// special folder for NX to find and load it during startup. 
// Refer to the NX Open documentation for more details on how 
// NX finds and loads applications during startup. 
//------------------------------------------------------------------------------ 
extern void ufsta( char *param, int *returnCode, int rlen ) 
{ 
    try 
    { 
        initUDO(false); 
    } 
    catch (const NXOpen::NXException& ex) 
    { 
        cerr << "Caught exception: " << ex.Message() << endl; 
    } 
} //------------------------------------------------------------------------------ 
// ufusr_ask_unload 
// Make sure you specify AtTermination for the unload option. 
// If you unload the library before the NX Session Terminates 
// bad things could happen when we try to execute a udo 
// callback that no longer exists in the session. 
//------------------------------------------------------------------------------ 
extern int ufusr_ask_unload( void ) 
{ 
    //return (int)Session::LibraryUnloadOptionExplicitly; 
    // return (int)Session::LibraryUnloadOptionImmediately; 
    return (int)Session::LibraryUnloadOptionAtTermination; 
}
