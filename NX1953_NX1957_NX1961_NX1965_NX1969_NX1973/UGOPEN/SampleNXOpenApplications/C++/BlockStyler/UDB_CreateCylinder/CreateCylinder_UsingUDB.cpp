//=============================================================================
//
//                   Copyright (c) 2011 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for Block Styler
//===============================================================================
//

//==============================================================================
//  Purpose:  This TEMPLATE file contains C++ source to guide you in the
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
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include "CreateCylinder_UsingUDB.hpp"
#include <NXOpen/Axis.hxx>
#include <NXOpen/Direction.hxx>
#include <NXOpen/DirectionCollection.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_CylinderBuilder.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Point.hxx>

#include <sstream>

using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(CreateCylinder_UsingUDB::theSession) = NULL;
UI *(CreateCylinder_UsingUDB::theUI) = NULL;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
CreateCylinder_UsingUDB::CreateCylinder_UsingUDB()
{
    try
    {
        // Initialize the NX Open C++ API environment
        CreateCylinder_UsingUDB::theSession = NXOpen::Session::GetSession();
        CreateCylinder_UsingUDB::theUI = UI::GetUI();
        theDlxFileName = "CreateCylinder_UsingUDB.dlx";
        theDialog = CreateCylinder_UsingUDB::theUI->CreateDialog(theDlxFileName);
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &CreateCylinder_UsingUDB::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &CreateCylinder_UsingUDB::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &CreateCylinder_UsingUDB::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &CreateCylinder_UsingUDB::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &CreateCylinder_UsingUDB::dialogShown_cb));
        diameter = DimensionUDB::RegisterUserDefinedUIBlock(theDialog, "diameter");
        height = DimensionUDB::RegisterUserDefinedUIBlock(theDialog, "height");
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
CreateCylinder_UsingUDB::~CreateCylinder_UsingUDB()
{
    if (diameter != NULL)
    {
        delete diameter;
        diameter = NULL;
    }
    if (height != NULL)
    {
        delete height;
        height = NULL;
    }
    if (theDialog != NULL)
    {
        delete theDialog;
        theDialog = NULL;
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
//    1. USER EXIT
//
//        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
//        2) Invoke the Shared Library through File->Execute->NX Open menu.
//
//------------------------------------------------------------------------------
extern "C" DllExport void  ufusr(char *param, int *retcod, int param_len)
{
    CreateCylinder_UsingUDB *theCreateCylinder_UsingUDB = NULL;
    try
    {
        theCreateCylinder_UsingUDB = new CreateCylinder_UsingUDB();
        // The following method shows the dialog immediately
        theCreateCylinder_UsingUDB->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateCylinder_UsingUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if(theCreateCylinder_UsingUDB != NULL)
    {
        delete theCreateCylinder_UsingUDB;
        theCreateCylinder_UsingUDB = NULL;
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
extern "C" DllExport int ufusr_ask_unload()
{
    //return (int)Session::LibraryUnloadOptionExplicitly;
    return (int)Session::LibraryUnloadOptionImmediately;
    //return (int)Session::LibraryUnloadOptionAtTermination;
}

//------------------------------------------------------------------------------
// Following method cleanup any housekeeping chores that may be needed.
// This method is automatically called by NX.
//------------------------------------------------------------------------------
extern "C" DllExport void ufusr_cleanup(void)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateCylinder_UsingUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int CreateCylinder_UsingUDB::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateCylinder_UsingUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void CreateCylinder_UsingUDB::initialize_cb()
{
    try
    {
        group0 = theDialog->TopBlock()->FindBlock("group0");
        point0 = theDialog->TopBlock()->FindBlock("point0");
        vector0 = theDialog->TopBlock()->FindBlock("vector0");
        group = theDialog->TopBlock()->FindBlock("group");

        //Set diameter and height
        diameter->SetLabel("Diameter");
        diameter->SetValue(200);

        height->SetLabel("Height");
        height->SetValue( 500);
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateCylinder_UsingUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void CreateCylinder_UsingUDB::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateCylinder_UsingUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int CreateCylinder_UsingUDB::apply_cb()
{
    int errorCode = 0;
    try
    {
        //---- Enter your callback code here -----
        CreateCylinder();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        CreateCylinder_UsingUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int CreateCylinder_UsingUDB::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == point0)
        {
        //---------Enter your code here-----------
        }
        else if(block == vector0)
        {
        //---------Enter your code here-----------
        }
        else if(block == diameter->GetTopBlock())
        {
        //---------Enter your code here-----------
        }
        else if(block == height->GetTopBlock())
        {
        //---------Enter your code here-----------
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateCylinder_UsingUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int CreateCylinder_UsingUDB::ok_cb()
{
    int errorCode = 0;
    try
    {
        errorCode = apply_cb();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        CreateCylinder_UsingUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//Creates cylinder based on the value available on User Defined UI Block (UDB), Point and Vector
 
void CreateCylinder_UsingUDB::CreateCylinder()
{
        Part* workPart(theSession->Parts()->Work());

        Features::CylinderBuilder* cylinderBuilder1 = NULL;
        cylinderBuilder1 = workPart->Features()->CreateCylinderBuilder(NULL);

        //Get the point
        PropertyList* pointPropertyList = point0->GetProperties();
        Point3d originPoint = pointPropertyList->GetPoint("Point");
        delete pointPropertyList;
        pointPropertyList = NULL;

        //Get the direction
        PropertyList* vectorPropertyList = vector0->GetProperties();
        Vector3d direction = vectorPropertyList->GetVector("Vector");
        delete vectorPropertyList;
        vectorPropertyList = NULL;

        Direction* direction1  = NULL;
        direction1 = workPart->Directions()->CreateDirection(originPoint, direction, SmartObject::UpdateOptionWithinModeling);

        //Set diameter and height
        std::stringstream diameterValue;
        diameterValue << diameter->GetValue();
        std::stringstream heightValue;
        heightValue << height->GetValue();

        cylinderBuilder1->Diameter()->SetRightHandSide(diameterValue.str());
        cylinderBuilder1->Height()->SetRightHandSide(heightValue.str());

        //Set the axis
        Axis* axis1 = NULL;
        axis1 = cylinderBuilder1->Axis();
        axis1->Point()->SetCoordinates(originPoint);
        axis1->SetDirection(direction1);

        //Commit
        cylinderBuilder1->Commit();
        cylinderBuilder1->Destroy();
        cylinderBuilder1 = NULL;
}
