//----------------------------------------------------------------------------
//   Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
//                         All rights reserved
//----------------------------------------------------------------------------
// 
//File description: NX/Open example of a dialog to edit dimension prefix
//===============================================================================
//

//==============================================================================
//  WARNING!!  This file is overwritten by the Block UI Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
//
//==============================================================================

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
#include "dimpref.hpp"
#include <NXOpen/Annotations_Dimension.hxx>
#include <NXOpen/PropertyContainer.hxx>
#include <string.h>

using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(dimpref::theSession) = NULL;
UI *(dimpref::theUI) = NULL;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
dimpref::dimpref()
{
    try
    {
        // Initialize the NX Open C++ API environment
        dimpref::theSession = NXOpen::Session::GetSession();
        dimpref::theUI = UI::GetUI();
        theDlxFileName = "dimpref.dlx";
        theDialog = dimpref::theUI->CreateDialog(theDlxFileName);
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &dimpref::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &dimpref::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &dimpref::update_cb));
        theDialog->AddFilterHandler(make_callback(this, &dimpref::filter_cb));
        theDialog->AddInitializeHandler(make_callback(this, &dimpref::initialize_cb));
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
dimpref::~dimpref()
{
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
    dimpref *thedimpref = NULL;
    try
    {
        thedimpref = new dimpref();
        // The following method shows the dialog immediately
        thedimpref->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        dimpref::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if(thedimpref != NULL)
    {
        delete thedimpref;
        thedimpref = NULL;
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
        dimpref::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int dimpref::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        dimpref::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void dimpref::initialize_cb()
{
    try
    {
        group0 = theDialog->TopBlock()->FindBlock("group0");
        SelectDims = theDialog->TopBlock()->FindBlock("SelectDims");
        group = theDialog->TopBlock()->FindBlock("group");
        PrefixOptions = theDialog->TopBlock()->FindBlock("PrefixOptions");
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        dimpref::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int dimpref::apply_cb()
{
    int errorCode = 0;
    try
    {


        //---- Enter your callback code here -----
        NXOpen::BlockStyler::PropertyList* props = PrefixOptions->GetProperties();
        NXString option = props->GetEnumAsString("Value");
        delete props;
        props = NULL;

        props = SelectDims->GetProperties();
        std::vector<NXOpen::TaggedObject *> dimensions = props->GetTaggedObjectVector("SelectedObjects");
        delete props;
        props = NULL;

        EditPrefix(dimensions, option.GetText());
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        dimpref::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int dimpref::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == SelectDims)
        {
        //---------Enter your code here-----------
        }
        else if(block == PrefixOptions)
        {
        //---------Enter your code here-----------
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        dimpref::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int dimpref::ok_cb()
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
        dimpref::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: filter_cb
//------------------------------------------------------------------------------
int dimpref::filter_cb(NXOpen::BlockStyler::UIBlock* block, NXOpen::TaggedObject* selectedObject)
{
    if (dynamic_cast<Annotations::Dimension*>(selectedObject) != NULL)
    {
        return UF_UI_SEL_ACCEPT;
    }
    
    return UF_UI_SEL_REJECT;
}

void dimpref::EditPrefix(std::vector<NXOpen::TaggedObject*>dimensions, NXString option)
{   
    Session* session = Session::GetSession();
    Session::UndoMarkId mark = session->SetUndoMark(Session::MarkVisibilityInvisible, "Edit Appended Text");

    for (int loop = 0; loop < (int)dimensions.size(); ++loop) 
    {
        NXOpen::Annotations::Dimension* dimensionPt =
            dynamic_cast<NXOpen::Annotations::Dimension*>(dimensions[loop]);

        if (dimensionPt != NULL)
        {
            Annotations::AppendedText* appendedText = dimensionPt->GetAppendedText();
            
            if(strcmp(option.GetText(), "Diameter Symbol") == 0)
            {
                std::vector<NXString> lines(1);
                lines[0] = "<O>";
                appendedText->SetBeforeText(lines);
            }
            else if (strcmp(option.GetText(), "None") == 0)
            {
                std::vector<NXString> lines(0);
                appendedText->SetBeforeText(lines);
            }

            dimensionPt->SetAppendedText(appendedText);

            delete appendedText;
        }
    }

    session->UpdateManager()->DoUpdate(mark);
}
