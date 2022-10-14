//=============================================================================
//
//            Copyright 2010 Siemens Product Lifecycle Management Software Inc.
//                              All Rights Reserved.
//==============================================================================
//File description: Sample NXOpen Application for displaying a tree structure 
//of an assembly in the tree list of a Block Styler UI dialog.
//===============================================================================
//
//==============================================================================
//  WARNING!!  This file is overwritten by the Block UI Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
//==============================================================================

#ifndef ASSEMBLYVIEWER_H_INCLUDED
#define ASSEMBLYVIEWER_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <uf_ui_types.h>
#include <iostream>
#include <uf.h>
#include <uf_ui.h>
#include <string.h>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/BlockStyler_PropertyList.hxx>
#include <NXOpen/BlockStyler_Tree.hxx>
#include <NXOpen/BlockStyler_Node.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/BasePart.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Assemblies_ComponentAssembly.hxx>
#include <NXOpen/DisplayManager.hxx>
#include <NXOpen/DisplayModification.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/PartCleanup.hxx>

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
class AssemblyViewer;
//
//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
BlockStyler::Node *parentNode=NULL;
extern AssemblyViewer *theAssemblyViewer;

class DllExport AssemblyViewer
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    AssemblyViewer();
    ~AssemblyViewer();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the AssemblyViewer.cpp file. 
    // You are REQUIRED to write the implementation for these funtions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int ok_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    int filter_cb(NXOpen::BlockStyler::UIBlock*  block, NXOpen::TaggedObject* selectObject);
    void focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus);
    void keyboardFocusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus);    
    void OnSelectCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *, int columnID, bool selected);    
private:
    const char* theDlxFileName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::UIBlock* group0;// Block type: Group
    NXOpen::BlockStyler::Tree* treeList;// Block type: Tree Control
    NXOpen::BlockStyler::UIBlock* group;// Block type: Group
    NXOpen::BlockStyler::UIBlock* compDisplay;// Block type: Enumeration
    NXOpen::BlockStyler::UIBlock* group1;// Block type: Group
    NXOpen::BlockStyler::UIBlock* selComponent;// Block type: Selection
    NXOpen::BlockStyler::UIBlock* selColor;// Block type: Color Picker
    NXOpen::BlockStyler::UIBlock* setColor;// Block type: Button
    void PopulateTree(NXOpen::Assemblies::Component *);// Cycles through assembly components and populates the tree list    
    void ApplyColor(std::vector<NXOpen::TaggedObject *>&selObjectData);// Sets the selected color to the components
    void HighlightComponent(std::vector<NXOpen::TaggedObject *>&selObjectData, bool highlight);// Highlights the selected components
    void ComponentSelection();// Based on the IsSingleComponentSelection, selection is done for either single component or for all components
    std::vector<NXOpen::TaggedObject *> GetComponentOccurences(std::vector<NXOpen::Assemblies::Component *>&assemblyComponent);// Gets the component occurrences
    std::vector<NXOpen::TaggedObject *> GetSelectedNodes();// Gets the tags of the selected nodes from the tree list
    std::vector<NXOpen::TaggedObject *> GetSelectedObjects();// Gets the tags of the selected objects from the select object block
    bool IsSingleComponentSelection();// Specifies whether the component selection option is "Single component" or "All Components"
    void PartCleanup();// Performs part clean up and turns off the highlighting
    bool drawAll;// This variable decides either to select a single component or all component occurrences based on the component selection option 
    std::vector<NXOpen::BlockStyler::Node *> treeNodes;
};
#endif //ASSEMBLYVIEWER_H_INCLUDED
