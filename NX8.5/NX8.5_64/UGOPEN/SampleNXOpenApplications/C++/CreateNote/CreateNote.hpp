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

#ifndef CREATENOTE_H_INCLUDED
#define CREATENOTE_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <uf_ui_types.h>
#include <uf.h>
#include <uf_ui.h>
#include <iostream>
#include <string.h>
#include <algorithm>
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
#include <NXOpen/SymbolFont.hxx>
#include <NXOpen/Annotations_CustomSymbol.hxx>



//------------------------------------------------------------------------------
//Bit Option for Property: SnapPointTypesEnabled
//------------------------------------------------------------------------------
#define              SnapPointTypesEnabled_UserDefined (1 << 0);
#define                 SnapPointTypesEnabled_Inferred (1 << 1);
#define           SnapPointTypesEnabled_ScreenPosition (1 << 2);
#define                 SnapPointTypesEnabled_EndPoint (1 << 3);
#define                 SnapPointTypesEnabled_MidPoint (1 << 4);
#define             SnapPointTypesEnabled_ControlPoint (1 << 5);
#define             SnapPointTypesEnabled_Intersection (1 << 6);
#define                SnapPointTypesEnabled_ArcCenter (1 << 7);
#define            SnapPointTypesEnabled_QuadrantPoint (1 << 8);
#define            SnapPointTypesEnabled_ExistingPoint (1 << 9);
#define             SnapPointTypesEnabled_PointonCurve (1 <<10);
#define           SnapPointTypesEnabled_PointonSurface (1 <<11);
#define         SnapPointTypesEnabled_PointConstructor (1 <<12);
#define     SnapPointTypesEnabled_TwocurveIntersection (1 <<13);
#define             SnapPointTypesEnabled_TangentPoint (1 <<14);
#define                    SnapPointTypesEnabled_Poles (1 <<15);
#define         SnapPointTypesEnabled_BoundedGridPoint (1 <<16);
//------------------------------------------------------------------------------
//Bit Option for Property: SnapPointTypesOnByDefault
//------------------------------------------------------------------------------
#define             SnapPointTypesOnByDefault_EndPoint (1 << 3);
#define             SnapPointTypesOnByDefault_MidPoint (1 << 4);
#define         SnapPointTypesOnByDefault_ControlPoint (1 << 5);
#define         SnapPointTypesOnByDefault_Intersection (1 << 6);
#define            SnapPointTypesOnByDefault_ArcCenter (1 << 7);
#define        SnapPointTypesOnByDefault_QuadrantPoint (1 << 8);
#define        SnapPointTypesOnByDefault_ExistingPoint (1 << 9);
#define         SnapPointTypesOnByDefault_PointonCurve (1 <<10);
#define       SnapPointTypesOnByDefault_PointonSurface (1 <<11);
#define     SnapPointTypesOnByDefault_PointConstructor (1 <<12);
#define     SnapPointTypesOnByDefault_BoundedGridPoint (1 <<16);
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;
using namespace Annotations;

//------------------------------------------------------------------------------
// Forward declaration for Class
//------------------------------------------------------------------------------
class CreateNote;
//
//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
extern CreateNote *theCreateNote;

class CreateNote
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    CreateNote();
    ~CreateNote();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the CreateNote.cpp file. 
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
    NXOpen::BlockStyler::UIBlock* noteType;// Block type: Enumeration
    NXOpen::BlockStyler::UIBlock* sbfFileBrowse;// Block type: NativeFileBrowser
    NXOpen::BlockStyler::UIBlock* symList;// Block type: Enumeration
    NXOpen::BlockStyler::UIBlock* scale;// Block type: Double
    NXOpen::BlockStyler::UIBlock* aspectRatio;// Block type: Double
    NXOpen::BlockStyler::UIBlock* selectNote;// Block type: Selection
    NXOpen::BlockStyler::UIBlock* selLocation;// Block type: Specify Cursor Location
	void ShowAndHideBlocks();
	void LoadSbfFile();
	void PlaceNote(Annotations::LetteringPreferences *,Annotations::UserSymbolPreferences *,std::vector<NXString>);
    
};
#endif //CREATENOTE_H_INCLUDED
