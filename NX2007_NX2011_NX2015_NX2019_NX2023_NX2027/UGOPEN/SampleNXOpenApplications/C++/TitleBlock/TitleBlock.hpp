//=============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for Title Block generation through 
//Symbol file
//===============================================================================
//
//==============================================================================
//  WARNING!!  This file is overwritten by the Block Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
//==============================================================================

#ifndef GENERATETITLE_H_INCLUDED
#define GENERATETITLE_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <uf_ui_types.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_defs.h>
#include <iostream>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/BlockStyler_PropertyList.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Annotations_LetteringPreferences.hxx>
#include <NXOpen/Annotations_AnnotationManager.hxx>
#include <NXOpen/Annotations_Note.hxx>
#include <NXOpen/Annotations_Annotation.hxx>
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
class GenerateTitle;
//
//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
extern GenerateTitle *theGenerateTitle;

class GenerateTitle
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    GenerateTitle();
    ~GenerateTitle();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the GenerateTitle.cpp file. 
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
    NXOpen::BlockStyler::UIBlock* partName;// Block type: String
    NXOpen::BlockStyler::UIBlock* authorName;// Block type: String

	
    
};
#endif //GENERATETITLE_H_INCLUDED
