//=============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
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
//  1.  Help on how to load and display your Block Styler dialog in NX
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
#include "EditExpression.hpp"
#include "NXOpen/BlockStyler_UIBlock.hxx"
#include "NXOpen/Expression.hxx"
#include "NXOpen/ExpressionCollection.hxx"
#include "NXOpen/Features_Feature.hxx"
#include "NXOpen/Features_FeatureCollection.hxx"
#include "NXOpen/Part.hxx"
#include "NXOpen/PartCollection.hxx"
#include "NXOpen/Unit.hxx"
#include "NXOpen/UnitCollection.hxx"
#include "NXOpen/Update.hxx"
#include <sstream>
#include <iomanip>
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(EditExpression::theSession) = NULL;
UI *(EditExpression::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
EditExpression *theEditExpression;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
EditExpression::EditExpression()
{
    try
    {
        // Initialize the NX Open C++ API environment
        EditExpression::theSession = NXOpen::Session::GetSession();
        EditExpression::theUI = UI::GetUI();
        theDialogName = "EditExpression.dlx";
        theDialog = EditExpression::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &EditExpression::apply_cb));
        theDialog->AddUpdateHandler(make_callback(this, &EditExpression::update_cb));
        theDialog->AddFilterHandler(make_callback(this, &EditExpression::filter_cb));
        theDialog->AddInitializeHandler(make_callback(this, &EditExpression::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &EditExpression::dialogShown_cb));
    }
    catch(exception& ex)
    {
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
EditExpression::~EditExpression()
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
//    You can create the dialog using one of the following ways:
//
//    1. USER EXIT
//
//        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
//        2) Invoke the Shared Library through File->Execute->NX Open menu.
//
//------------------------------------------------------------------------------
extern "C" DllExport void  ufusr(char *param, int *retcod, int param_len)
{
    try
    {
        theEditExpression = new EditExpression();
        // The following method shows the dialog immediately
        theEditExpression->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        EditExpression::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    delete theEditExpression;
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
        EditExpression::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int EditExpression::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        EditExpression::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void EditExpression::initialize_cb()
{
    try
    {
        GroupFeatureSelection = theDialog->TopBlock()->FindBlock("GroupFeatureSelection");
        FeatureList = dynamic_cast<NXOpen::BlockStyler::SetList* >(theDialog->TopBlock()->FindBlock("FeatureList"));
        GroupExpressionList = theDialog->TopBlock()->FindBlock("GroupExpressionList");
        ButtonGetExpressions = theDialog->TopBlock()->FindBlock("ButtonGetExpressions");
        ExpressionList = dynamic_cast<NXOpen::BlockStyler::ListBox* >(theDialog->TopBlock()->FindBlock("ExpressionList"));
        GroupExpression = theDialog->TopBlock()->FindBlock("GroupExpression");
        ExpressionName = theDialog->TopBlock()->FindBlock("ExpressionName");
        ExpressionValue = theDialog->TopBlock()->FindBlock("ExpressionValue");
        // User defined code
        newFeatCol.clear();
        newBlock = FeatureList->AddNewSet(true);
        FeatureList->SetAddHandler(make_callback(this, &EditExpression::add_handler));
        FeatureList->SetDeleteHandler(make_callback(this, &EditExpression::delete_handler));
        FeatureList->SetReorderObserver(make_callback(this, &EditExpression::reorder_handler));
        expToEdit = NULL;
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        EditExpression::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb()
//------------------------------------------------------------------------------
void EditExpression::dialogShown_cb()
{
    try
    {
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        EditExpression::theUI->NXMessageBox()->Show("dialogShown_cb", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int EditExpression::apply_cb()
{
    int errorCode = 0;
    try
    {
        if (expToEdit != NULL)
        {
            NXOpen::Part* workPart = EditExpression::theSession->Parts()->Work();
            PropertyList* ExpressionValueProperties = ExpressionValue->GetProperties();
            double editedvalue = ExpressionValueProperties->GetDouble("Value");
            delete ExpressionValueProperties;
            ExpressionValueProperties = NULL;

            Unit* unit1 = dynamic_cast<NXOpen::Unit*>(workPart->UnitCollection()->FindObject("MilliMeter"));

            NXOpen::Session::UndoMarkId markId2 = EditExpression::theSession->SetUndoMark(NXOpen::Session::MarkVisibilityInvisible, "Update Expression Data");


            // Convert angle in double to std::string
            std::stringstream expValue;
            expValue << setprecision(16) << editedvalue;
            workPart->Expressions()->EditWithUnits(expToEdit, unit1, expValue.str());

            int nErrs1 = EditExpression::theSession->UpdateManager()->DoUpdate(markId2);

            if (nErrs1 > 0)
            {
                errorCode = 1;
                EditExpression::theUI->NXMessageBox()->Show("Update Errors", NXOpen::NXMessageBox::DialogTypeError, "Update Failed with errors");
            }

            EditExpression::theSession->DeleteUndoMark(markId2, "Update Expression Data");
        }
    }
    catch(exception& ex)
    {
        errorCode = 1;
        //---- Enter your exception handling code here -----
        EditExpression::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int EditExpression::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        NXOpen::Part* workPart = EditExpression::theSession->Parts()->Work();
        if(block == FeatureList)
        {
            NXOpen::BlockStyler::CompositeBlock* updatedBlock = 
                dynamic_cast<NXOpen::BlockStyler::CompositeBlock* >(FeatureList->FindUpdated());
            if (updatedBlock != NULL) 
            {
                NXOpen::BlockStyler::UIBlock* subBlock = updatedBlock->FindBlock("select_feature0");
                if( subBlock != NULL) 
                {
                    PropertyList* subBlockProperties = subBlock->GetProperties();
                    std::vector<NXOpen::TaggedObject* > featCol = subBlockProperties->GetTaggedObjectVector("SelectedObjects");
                    if (featCol.size() > 1)
                    {
                        newFeatCol.clear();
                        newFeatCol.push_back(featCol[featCol.size() - 1]);
                        subBlockProperties->SetTaggedObjectVector("SelectedObjects", newFeatCol);
                    }
                    else if (featCol.size() == 1) 
                    {
                        newFeatCol.clear();
                        newFeatCol.push_back(featCol[0]);
                    }
                    NXOpen::Features::Feature* feature1 = dynamic_cast<NXOpen::Features::Feature*>(newFeatCol[0]);
                    std::vector<NXOpen::NXString> str;
                    str.push_back(feature1->JournalIdentifier());
                    FeatureList->SetItemText(updatedBlock, str);
                    delete subBlockProperties;
                }
            }
        }
        else if(block == ButtonGetExpressions)
        {
            std::vector<NXOpen::BlockStyler::UIBlock* > selectedBlocks = FeatureList->GetSelected();
            UIBlock* updatedBlock = NULL;

            if (selectedBlocks.size() > 0)
            {
                updatedBlock = selectedBlocks[0];
            }

            if (updatedBlock != NULL)
            {
                
                FeatureList->GetItemText(updatedBlock);
                std::vector<NXOpen::NXString> strings = FeatureList->GetItemText(updatedBlock);
                if ( strings[0].GetText() != "" )
                {
                    NXOpen::Features::Feature* feat = workPart->Features()->FindObject(strings[0]);
                    std::vector<NXOpen::Expression* > allExp = feat->GetExpressions();
                    std::vector<NXOpen::NXString> allExpStr;
                    for (unsigned int ii = 0; ii < allExp.size(); ++ii)
                    {
                        Expression* exp = allExp[ii];
                        stringstream tmpStream;
                        tmpStream << exp->Name().GetUTF8Text() << " = " << exp->Value() << " - " << exp->GetDescriptor().GetUTF8Text();
                        allExpStr.push_back(tmpStream.str());
                    }

                    PropertyList* ExpressionListProperties = ExpressionList->GetProperties();
                    ExpressionListProperties->SetStrings("ListItems", allExpStr);
                    delete ExpressionListProperties;

                    FeatureList->SetItemText(updatedBlock, strings);
                }
            }

        }
        else if(block == ExpressionList)
        {
            PropertyList* ExpressionListProperties = ExpressionList->GetProperties();
            std::vector<NXOpen::NXString> listStrings = ExpressionListProperties->GetStrings("ListItems");
            std::vector<int> index = ExpressionListProperties->GetIntegerVector("SelectedItems");
            delete ExpressionListProperties;

            std::string splitStr (listStrings[index[0]].GetUTF8Text());
            size_t ind = splitStr.find(" ");
            if (ind != splitStr.npos)
            {
                splitStr = splitStr.substr(0, ind);
            }

            PropertyList* ExpressionNameProperties = ExpressionName->GetProperties();
            ExpressionNameProperties->SetString("Value", splitStr);
            delete ExpressionNameProperties;

            expToEdit = workPart->Expressions()->FindObject(splitStr);

            PropertyList* ExpressionValueProperties = ExpressionValue->GetProperties();
            ExpressionValueProperties->SetDouble("Value", expToEdit->Value());
            delete ExpressionValueProperties;
        }
        else if(block == ExpressionName)
        {
        //---------Enter your code here-----------
        }
        else if(block == ExpressionValue)
        {
        //---------Enter your code here-----------
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        EditExpression::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: filter_cb
//------------------------------------------------------------------------------
int EditExpression::filter_cb(NXOpen::BlockStyler::UIBlock*  block, NXOpen::TaggedObject* selectObject)
{
    return(UF_UI_SEL_ACCEPT);
}
//------------------------------------------------------------------------------
//----------------------------User defined Functions----------------------------
//------------------------------------------------------------------------------
int EditExpression::add_handler(SetList* list)
{
    UIBlock* newItem = list->AddNewSet(true);
    return 0;
}

int EditExpression::delete_handler(SetList* list, UIBlock* doomed)
{
    EditExpression::theUI->NXMessageBox()->Show("Edit Expression", NXOpen::NXMessageBox::DialogTypeInformation, "Control is in delete_handler function");
    return 0;

}

int EditExpression::reorder_handler(SetList* list, UIBlock* moved, int oldPos, int newPos)
{
    EditExpression::theUI->NXMessageBox()->Show("Edit Expression", NXOpen::NXMessageBox::DialogTypeInformation, "Moved list item");
    return 0;

}
 
