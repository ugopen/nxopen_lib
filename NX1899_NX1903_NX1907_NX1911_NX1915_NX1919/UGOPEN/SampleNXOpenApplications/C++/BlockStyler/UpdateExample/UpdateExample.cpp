//===============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for Block Styler
//===============================================================================
//
//==============================================================================
//  WARNING!!  This file is overwritten by the Block UI Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
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
#include "UpdateExample.hpp"
#include <sstream>
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(UpdateExample::theSession) = NULL;
UI *(UpdateExample::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
UpdateExample *theUpdateExample;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
UpdateExample::UpdateExample()
{
    try
    {
        // Initialize the NX Open C++ API environment
        UpdateExample::theSession = NXOpen::Session::GetSession();
        UpdateExample::theUI = UI::GetUI();
        theDialogName = "UpdateExample.dlx";
        theDialog = UpdateExample::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &UpdateExample::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &UpdateExample::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &UpdateExample::update_cb));
        theDialog->AddCancelHandler(make_callback(this, &UpdateExample::cancel_cb));
        theDialog->AddFilterHandler(make_callback(this, &UpdateExample::filter_cb));
        theDialog->AddInitializeHandler(make_callback(this, &UpdateExample::initialize_cb));
        theDialog->AddFocusNotifyHandler(make_callback(this, &UpdateExample::focusNotify_cb));
        theDialog->AddKeyboardFocusNotifyHandler(make_callback(this, &UpdateExample::keyboardFocusNotify_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &UpdateExample::dialogShown_cb));
        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        throw;
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
UpdateExample::~UpdateExample()
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
    try
    {
        theUpdateExample = new UpdateExample();
        // The following method shows the dialog immediately
        theUpdateExample->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if(theUpdateExample != NULL)
    {
        delete theUpdateExample;
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
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int UpdateExample::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void UpdateExample::initialize_cb()
{
    try
    {
        group0 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("group0"));
        string0 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("string0"));
        toggle0 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("toggle0"));
        integer0 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("integer0"));
        string01 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("string01"));
        group01 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("group01"));
        toggle01 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("toggle01"));
        toggle02 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("toggle02"));

        //In the initialize call back Labels are set for string0,outputString and toggle01
        BlockStyler::PropertyList *string0Props = string0->GetProperties();
        string0Props->SetString("Label","Input String");
        delete string0Props;

        
        BlockStyler::PropertyList *string01Props = string01->GetProperties();
        string01Props->SetString("Label","Output String");
        delete string01Props;


        BlockStyler::PropertyList *toggle01Props = toggle01->GetProperties();
        toggle01Props->SetString("Label","Lock Input String");
        delete toggle01Props;

    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void UpdateExample::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
            
        //Creating Property lists for integer0,toggle02 and toggle0           
         BlockStyler::PropertyList *integer0Props = integer0->GetProperties();
         BlockStyler::PropertyList *toggle02Props = toggle02->GetProperties();
         BlockStyler::PropertyList *toggle0Props = toggle0->GetProperties();

        //Setting the Visibility status for integer0 and toggle0
         integer0Props->SetLogical("Enable",!(toggle02Props->GetLogical("Value")));
         toggle0Props->SetLogical("Enable",!(toggle02Props->GetLogical("Value")));

         //Deleting Property lists after their use             
         delete integer0Props;
         delete toggle02Props;
         delete toggle0Props;

         //Getting String Values from the fields string0 and toggle01
         BlockStyler::PropertyList *string0Props1 = string0->GetProperties();
         BlockStyler::PropertyList *toggle01Props1 = toggle01->GetProperties();

         //Setting the visibility status for toggle01
         string0Props1->SetLogical("Enable",!(toggle01Props1->GetLogical("Value")));


        //Deleting Property lists after their use
         delete string0Props1;
         delete toggle01Props1;



    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int UpdateExample::apply_cb()
{
    int errorCode = 0;
    try
    {
        //---- Enter your callback code here -----
        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}



//  --------------------------------------------------------------------------------
//  updateOutputString() - copies the input string to the output string and
//                         optionally concatenates the number to the output string
//  --------------------------------------------------------------------------------
int UpdateExample::updateOutputString()
{
    int errorCode = 0;
    try
    {
        //---- Enter your callback code here -----

        // Get the input string and establish an empty number string
        BlockStyler::PropertyList *string0Props = string0->GetProperties();
        NXOpen::NXString inputText = string0Props->GetString("Value");
        delete string0Props;
        NXString numberText = "";

        // If the include number toggle is ON (true)
        // then get the number and create a string for it
        PropertyList *toggle0Props = toggle0->GetProperties();
        if(toggle0Props->GetLogical("Value"))
        {
            BlockStyler::PropertyList *integer0Props = integer0->GetProperties();
            int numberValue = integer0Props->GetInteger("Value");

            std::stringstream stringBuffer;
            stringBuffer << numberValue;
            numberText = " - ";
            numberText += stringBuffer.str();
            delete integer0Props;
        }
        delete toggle0Props;

        // Set the output string to the concatenated input string and optional number string
        BlockStyler::PropertyList *string01Props = string01->GetProperties();
        string01Props->SetString("Value", (inputText+=numberText));
        delete string01Props;    
        
        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int UpdateExample::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == string0)
        {
        //---------Enter your code here-----------
            updateOutputString();
        }
        else if(block == toggle0)
        {
        //---------Enter your code here-----------
            updateOutputString();
        }
        else if(block == integer0)
        {
        //---------Enter your code here-----------
            updateOutputString();
        }
        else if(block == string01)
        {
        //---------Enter your code here-----------
             //The output string block is disabled and only used for display
        }
        else if(block == toggle01)
        {
        //---------Enter your code here-----------

        //Enable or disable the input string block based on the state
        //of the string lock toggle block

        BlockStyler::PropertyList *string0Props = string0->GetProperties();
        BlockStyler::PropertyList *toggle01Props =  toggle01->GetProperties();


        string0Props->SetLogical("Enable", !(toggle01Props->GetLogical("Value")));
        delete string0Props;
        delete toggle01Props;


        }
        else if(block == toggle02)
        {
        //---------Enter your code here-----------

        //Enable or disable the integer0 block based on the state
        //of the integer0 lock toggle block
        BlockStyler::PropertyList *integer0Props = integer0->GetProperties();
        BlockStyler::PropertyList *toggle02Props = toggle02->GetProperties();
        BlockStyler::PropertyList *toggle0Props = toggle0->GetProperties();

        integer0Props->SetLogical("Enable", !(toggle02Props->GetLogical("Value")));
        toggle0Props->SetLogical("Enable", !(toggle02Props->GetLogical("Value")));

        delete integer0Props;
        delete toggle02Props;
        delete toggle0Props;


        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int UpdateExample::ok_cb()
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
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: cancel_Cb
//------------------------------------------------------------------------------
int UpdateExample::cancel_cb()
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: filter_cb
//------------------------------------------------------------------------------
int UpdateExample::filter_cb(NXOpen::BlockStyler::UIBlock*  block, NXOpen::TaggedObject* selectObject)
{
    return(UF_UI_SEL_ACCEPT);
}

//------------------------------------------------------------------------------
//Callback Name: focusNotify_cb
//This callback is executed when any block (except the ones which receive keyboard entry such as Integer block) receives focus.
//------------------------------------------------------------------------------
void UpdateExample::focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: keyboardFocusNotify_cb
//This callback is executed when block which can receive keyboard entry, receives the focus.
//------------------------------------------------------------------------------
void UpdateExample::keyboardFocusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        UpdateExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
