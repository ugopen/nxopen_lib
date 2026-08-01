//=============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for Block Styler
//===============================================================================
//

//  WARNING!!  This file is overwritten by the Block Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.

//==============================================================================

#ifndef TREELISTDEMO_H_INCLUDED
#define TREELISTDEMO_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <string.h>
#include <uf_ui_types.h>
#include <iostream>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/BlockStyler_PropertyList.hxx>
#include <NXOpen/BlockStyler_Tree.hxx>
#include <NXOpen/BlockStyler_Node.hxx>

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

//------------------------------------------------------------------------------
// Forward declaration for Class
//------------------------------------------------------------------------------
class TreeListDemo;
//
//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
extern TreeListDemo *theTreeListDemo;

class TreeListDemo
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    TreeListDemo();
    ~TreeListDemo();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the TreeListDemo.cpp file. 
    // You are REQUIRED to write the implementation for these funtions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int ok_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    void focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus);

    
    //void OnExpandCallback (NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node);
    //void OnInsertColumnCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID);
    void OnInsertNodeCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node);
    void OnDeleteNodeCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node);
    //void OnPreSelectCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int ID, bool selected);
    void OnSelectCallback(NXOpen::BlockStyler::Tree *, NXOpen::BlockStyler::Node *, int columnID, bool selected);
    void OnStateChangeCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int state);
    NXString ToolTipTextCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID);
    //int ColumnSortCallback(NXOpen::BlockStyler::Tree *tree, int columnID, NXOpen::BlockStyler::Node *node1, NXOpen::BlockStyler::Node *node2);
    NXString StateIconNameCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int state);
    NXOpen::BlockStyler::Tree::BeginLabelEditState OnBeginLabelEditCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID);
    NXOpen::BlockStyler::Tree::EndLabelEditState OnEndLabelEditCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int, NXString editedText);
    NXOpen::BlockStyler::Tree::EditControlOption OnEditOptionSelectedCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID, int selectedOptionID, NXString selectedOptionText, NXOpen::BlockStyler::Tree::ControlType type);
    NXOpen::BlockStyler::Tree::ControlType AskEditControlCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID);
    void OnMenuCallback(NXOpen::BlockStyler::Tree *, NXOpen::BlockStyler::Node *node, int columnID);
    void OnMenuSelectionCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int menuItemID);
    NXOpen::BlockStyler::Node::DropType IsDropAllowedCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID, NXOpen::BlockStyler::Node *targetNode, int targetColumnID);
    NXOpen::BlockStyler::Node::DragType IsDragAllowedCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID);
    bool OnDropCallback(NXOpen::BlockStyler::Tree *tree, std::vector<NXOpen::BlockStyler::Node *> node, int columnID, NXOpen::BlockStyler::Node *targetNode, int targetColumnID, NXOpen::BlockStyler::Node::DropType dropType, int dropMenuItemId);
    //void OnDropMenuCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID, NXOpen::BlockStyler::Node *targetNode, int targetColumnID);
    void OnDefaultAction(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID);
private:
    std::string theDialogName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::UIBlock* group0;// Block type: Group
    NXOpen::BlockStyler::Tree* tree_control0;// Block type: Tree Control
    NXOpen::BlockStyler::UIBlock* addDeleteNodeGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* nodeString;// Block type: String
    NXOpen::BlockStyler::UIBlock* addNodeButton;// Block type: Button
    NXOpen::BlockStyler::UIBlock* deleteNodeButton;// Block type: Button
    NXOpen::BlockStyler::UIBlock* stateIconGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* stateIconOptions;// Block type: Enumeration
    NXOpen::BlockStyler::UIBlock* nodeToolTip;// Block type: String
    NXOpen::BlockStyler::UIBlock* NodeEditGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* nodeEditOptions;// Block type: Enumeration
    NXOpen::BlockStyler::UIBlock* menuGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* showMenuToggle;// Block type: Toggle
    NXOpen::BlockStyler::UIBlock* dragDropGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* disallowDragToggle;// Block type: Toggle
    NXOpen::BlockStyler::UIBlock* dropOptions;// Block type: Enumeration
    NXOpen::BlockStyler::UIBlock* defaultActionGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* defaultActionToggle;// Block type: Toggle
    NXOpen::BlockStyler::UIBlock* nodeDataGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* instructions;// Block type: Multiline String
    NXOpen::BlockStyler::UIBlock* selection0;// Block type: Selection
    NXOpen::BlockStyler::UIBlock* addCrossSelectionNodeButton;// Block type: Button
    NXOpen::BlockStyler::UIBlock* redrawGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* redrawInstruction;// Block type: Multiline String
    NXOpen::BlockStyler::UIBlock* redrawToggle;// Block type: Toggle
    NXOpen::BlockStyler::UIBlock* listingWindowGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* listingWindowToggle;// Block type: Toggle
    void DeleteSelectedNodes();
    BlockStyler::Node* CreateAndAddNode(BlockStyler::Node* afterNode);
    void WriteCallbackToListingWindow(NXString);
    
};
#endif //TREELISTDEMO_H_INCLUDED
