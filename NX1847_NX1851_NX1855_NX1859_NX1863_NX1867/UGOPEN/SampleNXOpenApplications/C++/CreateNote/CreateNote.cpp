//=============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NXOpen Application for drawing notes placement
//either by copying an existing note or creating a note from a user defined symbol.
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
#include "CreateNote.hpp"
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(CreateNote::theSession) = NULL;
UI *(CreateNote::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
CreateNote *theCreateNote;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
CreateNote::CreateNote()
{
    try
    {
        // Initialize the NX Open C++ API environment
        CreateNote::theSession = NXOpen::Session::GetSession();
        CreateNote::theUI = UI::GetUI();
        theDialogName = "CreateNote.dlx";
        theDialog = CreateNote::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &CreateNote::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &CreateNote::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &CreateNote::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &CreateNote::initialize_cb));
        theDialog->AddFocusNotifyHandler(make_callback(this, &CreateNote::focusNotify_cb));
        theDialog->AddKeyboardFocusNotifyHandler(make_callback(this, &CreateNote::keyboardFocusNotify_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &CreateNote::dialogShown_cb));
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
CreateNote::~CreateNote()
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
        theCreateNote = new CreateNote();
        // The following method shows the dialog immediately
        theCreateNote->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    delete theCreateNote;
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
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int CreateNote::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//This method will show or hide blocks based on the radio button option selection
void CreateNote::ShowAndHideBlocks()
{
    NXOpen::BlockStyler::PropertyList *noteTypeProps = noteType->GetProperties();
    NXOpen::NXString noteType1 = noteTypeProps->GetEnumAsString("Value");
    delete noteTypeProps;

    if(!strcmp(noteType1.GetText(),"Create from user defined symbol"))
    {
        //If selection is create from user defined symbol,
        //then enabling file browser,symbol list,scale and aspect ratio fields
        sbfFileBrowse->GetProperties()->SetLogical("Show",true);
        symList->GetProperties()->SetLogical("Show",true);
        scale->GetProperties()->SetLogical("Show",true);
        aspectRatio->GetProperties()->SetLogical("Show",true);
        selectNote->GetProperties()->SetLogical("Show",false);    
        
        

    }
    else if(!strcmp(noteType1.GetText(),"Copy existing symbol"))
    {
        //If selection is copy existing symbol,
        //then disabling file browser,symbol list,scale and aspect ratio fields
        sbfFileBrowse->GetProperties()->SetLogical("Show",false);
        symList->GetProperties()->SetLogical("Show",false);
        scale->GetProperties()->SetLogical("Show",false);
        aspectRatio->GetProperties()->SetLogical("Show",false);
        selectNote->GetProperties()->SetLogical("Show",true);
        
        
    }

}

//Load all the symbols from current sbf file to the enum list
void CreateNote::LoadSbfFile()
{
    NXOpen::BlockStyler::PropertyList *sbfFileBrowseProps = sbfFileBrowse->GetProperties();
    NXOpen::NXString sbfFileBrowse1 = sbfFileBrowseProps->GetString("Path");    

    //If browse field is null then ug_default.sbf is shown in the path using root directory path
    if(!strcmp(sbfFileBrowse1.GetText(),""))
    {
        NXString baseDir = theSession->GetEnvironmentVariableValue("UGII_BASE_DIR");
        NXString symbolDir = baseDir;
        sbfFileBrowseProps->SetString("Path", symbolDir + "\\ugii\\ug_default.sbf");
    }

    sbfFileBrowse1 = sbfFileBrowseProps->GetString("Path");    
    delete sbfFileBrowseProps;

    theSession->Parts()->Work()->Annotations()->SetCurrentSbfFile(sbfFileBrowse1.GetText());
    std::vector<NXString> symbolNames= theSession->Parts()->Work()->Annotations()->ReadAllSymbolNamesFromSbfFile();

    NXOpen::BlockStyler::PropertyList *symListProps = symList->GetProperties();    
    symListProps->SetEnumMembers("Value",symbolNames);
    delete symListProps;
    
}

//These are the global variables
Annotations::LetteringPreferences *letteringPreferences1=NULL;
Annotations::UserSymbolPreferences *userSymbolPreferences1=NULL;
std::vector<NXString > stringArray1;

//Place note/symbol in the user picked cursor location
void CreateNote::PlaceNote(Annotations::LetteringPreferences *letteringPreferences1,Annotations::UserSymbolPreferences *userSymbolPreferences1,std::vector<NXString>  stringArray1)
{
    //Getting noteType selection option from radio button
    NXOpen::BlockStyler::PropertyList *noteTypeProps = noteType->GetProperties();
    NXOpen::NXString noteType2 = noteTypeProps->GetEnumAsString("Value");
    delete noteTypeProps;        

    if(!strcmp(noteType2.GetText(),"Create from user defined symbol"))
    {
        NXOpen::BlockStyler::PropertyList *symListProps = symList->GetProperties();
        NXString text = symListProps->GetEnumAsString("Value");
        delete symListProps;

        double scaleVal = scale->GetProperties()->GetDouble("Value");
        double aspectRatioVal = aspectRatio->GetProperties()->GetDouble("Value");
        double symWidth[256],symHeight[256];

        NXOpen::SymbolFont *noteSymbol = theSession->Parts()->Work()->Annotations()->LoadSymbolFontFromSbfFile(text,symWidth,symHeight);
        userSymbolPreferences1 = theSession->Parts()->Work()->Annotations()->NewUserSymbolPreferences(Annotations::UserSymbolPreferences::SizeTypeScaleAspectRatio,scaleVal,aspectRatioVal);

        //Selected text of the symbol is converted to symbol
        text = "<%"  + text + ">";
        string noteText = text.GetText();
        std::remove(noteText.begin(),noteText.end(),' ');

        size_t pos1 = noteText.find_first_of(">");
        noteText = noteText.substr(0,++pos1);
        NXString text1 = noteText;
        stringArray1.push_back(text1.GetText());    

        NXOpen::BlockStyler::PropertyList *selLocationProps = selLocation->GetProperties();
        NXOpen::Point3d cursor = selLocationProps->GetPoint("CursorLocation");
        delete selLocationProps;

        //Creates note in the given location
        theSession->Parts()->Work()->Annotations()->CreateNote(stringArray1,cursor,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);        

    }
    else if(!strcmp(noteType2.GetText(),"Copy existing symbol"))
    {
        std::vector<NXOpen::TaggedObject *>selectedObject;

        NXOpen::BlockStyler::PropertyList *selectNoteProps = selectNote->GetProperties();        
        selectedObject = selectNoteProps->GetTaggedObjectVector("SelectedObjects");
        delete selectNoteProps;

        NXOpen::BlockStyler::PropertyList *selLocationProps = selLocation->GetProperties();
        NXOpen::Point3d cursor = selLocationProps->GetPoint("CursorLocation");
        delete selLocationProps;

        //Here the user selected note/symbol is copied
        if (selectedObject.size()>0)
        {
            Annotations::Note *note1(dynamic_cast<Annotations::Note *>(selectedObject[0]));
            if(note1!=NULL)
            {                
                letteringPreferences1 = note1->GetLetteringPreferences();
                userSymbolPreferences1 = note1->GetUserSymbolPreferences(); 
                stringArray1 = note1->GetText();
                theSession->Parts()->Work()->Annotations()->CreateNote(stringArray1,cursor,AxisOrientationHorizontal,letteringPreferences1,userSymbolPreferences1);
            }
        }
    }
}


//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void CreateNote::initialize_cb()
{
    try
    {
        group0 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("group0"));
        noteType = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("noteType"));
        sbfFileBrowse = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("sbfFileBrowse"));
        symList = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("symList"));
        scale = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("scale"));
        aspectRatio = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("aspectRatio"));
        selectNote = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("selectNote"));
        selLocation = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("selLocation"));

        //Initially setting radio button selection to copy existing symbol
        noteType->GetProperties()->SetEnumAsString("Value","Copy existing symbol");
        ShowAndHideBlocks();

        //Setting selection mask to select only drafting notes or symbols
        NXOpen::Selection::SelectionAction action = Selection::SelectionActionClearAndEnableSpecific;
        std::vector<NXOpen::Selection::MaskTriple>selectionMask_array(2);
        selectionMask_array[0].Type = UF_drafting_entity_type;
        selectionMask_array[0].Subtype = UF_draft_note_subtype;
        selectionMask_array[1].Type = UF_drafting_entity_type;
        selectionMask_array[1].Subtype = UF_draft_label_subtype;
        selLocation->GetProperties()->SetEnumAsString("StepStatus","Required");        
        selectNote->GetProperties()->SetEnumAsString("StepStatus","Required");
        selectNote->GetProperties()->SetSelectionFilter("SelectionFilter",action,selectionMask_array);
        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void CreateNote::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----        
        noteType->GetProperties()->SetEnumAsString("Value","Copy existing symbol");
        ShowAndHideBlocks();
        
        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int CreateNote::apply_cb()
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
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int CreateNote::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == noteType)
        {
        //---------Enter your code here-----------

            ShowAndHideBlocks();

            //Getting noteType selection option from radio button
            NXOpen::BlockStyler::PropertyList *noteTypeProps = noteType->GetProperties();
            NXOpen::NXString noteType1 = noteTypeProps->GetEnumAsString("Value");
            delete noteTypeProps;

            if(!strcmp(noteType1.GetText(),"Create from user defined symbol"))
            {
                LoadSbfFile();
                symList->Focus();
            }

        }
        else if(block == sbfFileBrowse)
        {
        //---------Enter your code here-----------

            //Getting noteType selection option from radio button        
            LoadSbfFile();                
            
        }
        else if(block == symList)
        {
        //---------Enter your code here-----------

        }
        else if(block == scale)
        {
        //---------Enter your code here-----------

        }
        else if(block == aspectRatio)
        {
        //---------Enter your code here-----------

        }
        else if(block == selectNote)
        {
        //---------Enter your code here-----------
            

        }
        else if(block == selLocation)
        {
        //---------Enter your code here-----------
            PlaceNote(letteringPreferences1,userSymbolPreferences1,stringArray1);
            

        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int CreateNote::ok_cb()
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
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: focusNotify_cb
//This callback is executed when any block (except the ones which receive keyboard entry such as Integer block) receives focus.
//------------------------------------------------------------------------------
void CreateNote::focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: keyboardFocusNotify_cb
//This callback is executed when block which can receive keyboard entry, receives the focus.
//------------------------------------------------------------------------------
void CreateNote::keyboardFocusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        CreateNote::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
