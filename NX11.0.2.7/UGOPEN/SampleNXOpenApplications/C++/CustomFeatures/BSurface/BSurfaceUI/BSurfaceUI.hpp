//=============================================================================
//
//                   Copyright (c) 2015 Siemens Industry Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Custom feature 
//=============================================================================
//

#ifndef BSURFACEUI_H_INCLUDED
#define BSURFACEUI_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <uf_ui_types.h>
#include <iostream>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/BlockStyler_PropertyList.hxx>
#include <NXOpen/BlockStyler_Group.hxx>
#include <NXOpen/BlockStyler_IntegerBlock.hxx>
#include <NXOpen/BlockStyler_SetList.hxx>

#include <NXOpen/Features_CustomFeature.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

class DllExport BSurfaceUI
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;

    NXOpen::Features::CustomFeatureClassManager * customFeatureManager;
    NXOpen::Features::CustomFeature* editedFeature;
    NXOpen::Features::CustomFeatureClass* cfClass;

    BSurfaceUI();
    ~BSurfaceUI();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementation
    // of these prototypes is provided in the BSurfaceUI.cpp file. 
    // You are REQUIRED to write the implementation for these functions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int ok_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    int filter_cb(NXOpen::BlockStyler::UIBlock*  block, NXOpen::TaggedObject* selectObject);
    PropertyList* GetBlockProperties(const char *blockID);
    
    //int AddCallback (NXOpen::BlockStyler::SetList* set_list);
    //int DeleteCallback(NXOpen::BlockStyler::SetList* set_list, NXOpen::BlockStyler::SetList::UIBlock* blockToDelete);
    //int ReorderCallback(NXOpen::BlockStyler::SetList* set_list, NXOpen::BlockStyler::UIBlock* reorderedBlock, int oldPosition, int newPosition);
private:
    const char* theDlxFileName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::Group* group0;// Block type: Group
    NXOpen::BlockStyler::IntegerBlock* nu;// Block type: Integer
    NXOpen::BlockStyler::IntegerBlock* ku;// Block type: Integer
    NXOpen::BlockStyler::Group* group;// Block type: Group
    NXOpen::BlockStyler::IntegerBlock* nv;// Block type: Integer
    NXOpen::BlockStyler::IntegerBlock* kv;// Block type: Integer
    NXOpen::BlockStyler::Group* Poles;// Block type: Group
    NXOpen::BlockStyler::SetList* list0;// Block type: Set List
    
};
#endif //BSURFACEUI_H_INCLUDED
