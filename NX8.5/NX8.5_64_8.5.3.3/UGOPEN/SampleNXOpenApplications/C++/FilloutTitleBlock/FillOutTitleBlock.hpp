//=============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for filling Title Block of a 
//Drawing Sheet
//===============================================================================
//
//==============================================================================
//  WARNING!!  This file is overwritten by the Block Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
//==============================================================================

#ifndef FILLOUTTITLEBLOCK_H_INCLUDED
#define FILLOUTTITLEBLOCK_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <uf_ui_types.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/BlockStyler_PropertyList.hxx>
#include <NXOpen/Annotations_AnnotationManager.hxx>
#include <NXOpen/Annotations_Note.hxx>
#include <NXOpen/Annotations_NoteCollection.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Preferences_AnnotationPreferences.hxx>
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Forward declaration for Class
//------------------------------------------------------------------------------
class FillOutTitleBlock;
//
//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
extern FillOutTitleBlock *theFillOutTitleBlock;

class FillOutTitleBlock
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    FillOutTitleBlock();
    ~FillOutTitleBlock();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the FillOutTitleBlock.cpp file. 
    // You are REQUIRED to write the implementation for these funtions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int ok_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    void focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus);
    void keyboardFocusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus);
    
private:
    std::string theDialogName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::UIBlock* group0;// Block type: Group
    NXOpen::BlockStyler::UIBlock* compName;// Block type: String
    NXOpen::BlockStyler::UIBlock* dwgName;// Block type: String
    NXOpen::BlockStyler::UIBlock* dwgNo;// Block type: String
	NXOpen::BlockStyler::UIBlock* cageCode;// Block type: String
    NXOpen::BlockStyler::UIBlock* revision;// Block type: String
    NXOpen::BlockStyler::UIBlock* dwgScale;// Block type: String
    NXOpen::BlockStyler::UIBlock* sheetNo;// Block type: Label
    NXOpen::BlockStyler::UIBlock* sheetNo1;// Block type: Integer
    NXOpen::BlockStyler::UIBlock* sheetNoOf;// Block type: Label
    NXOpen::BlockStyler::UIBlock* sheetNo2;// Block type: Integer
    NXOpen::BlockStyler::UIBlock* separator0;// Block type: Separator
    NXOpen::BlockStyler::UIBlock* contractNo;// Block type: String
    NXOpen::BlockStyler::UIBlock* separator02;// Block type: Separator
    NXOpen::BlockStyler::UIBlock* design;// Block type: String
    NXOpen::BlockStyler::UIBlock* desSign;// Block type: String
    NXOpen::BlockStyler::UIBlock* separator01;// Block type: Separator
    NXOpen::BlockStyler::UIBlock* lead;// Block type: String
    NXOpen::BlockStyler::UIBlock* leadSign;// Block type: String
    NXOpen::BlockStyler::UIBlock* separator03;// Block type: Separator
    NXOpen::BlockStyler::UIBlock* str;// Block type: String
    NXOpen::BlockStyler::UIBlock* strSign;// Block type: String
    NXOpen::BlockStyler::UIBlock* separator04;// Block type: Separator
    NXOpen::BlockStyler::UIBlock* me;// Block type: String
    NXOpen::BlockStyler::UIBlock* meSign;// Block type: String
    
};
#endif //FILLOUTTITLEBLOCK_H_INCLUDED
