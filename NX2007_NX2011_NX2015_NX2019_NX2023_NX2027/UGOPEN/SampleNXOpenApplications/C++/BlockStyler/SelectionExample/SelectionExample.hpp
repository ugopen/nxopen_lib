//=============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//

#ifndef SELECTIONEXAMPLE_H_INCLUDED
#define SELECTIONEXAMPLE_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <uf_ui_types.h>
#include <iostream>
#include <string.h>
#include <NXOpen/Edge.hxx>
#include <NXOpen/Features_Chamfer.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/BlockStyler_PropertyList.hxx>
//------------------------------------------------------------------------------
//Bit Option for Property: EntityType
//------------------------------------------------------------------------------
#define                          EntityType_AllowEdges (1 << 0);
#define                         EntityType_AllowCurves (1 << 2);
#define                          EntityType_AllowPoint (1 << 3);
#define                         EntityType_AllowBodies (1 << 6);
//------------------------------------------------------------------------------
//Bit Option for Property: CurveRules
//------------------------------------------------------------------------------
#define                         CurveRules_SingleCurve (1 << 0);
#define                     CurveRules_ConnectedCurves (1 << 1);
#define                       CurveRules_TangentCurves (1 << 2);
#define                           CurveRules_FaceEdges (1 << 3);
#define                           CurveRules_BodyEdges (1 << 4);
#define                          CurveRules_SheetEdges (1 << 5);
#define                       CurveRules_FeatureCurves (1 << 6);
#define                         CurveRules_VertexEdges (1 << 8);
#define                  CurveRules_VertexTangentEdges (1 << 9);
#define                CurveRules_RegionBoundaryCurves (1 <<11);
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Forward declaration for Class
//------------------------------------------------------------------------------
class SelectionExample;
//
//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
extern SelectionExample *theSelectionExample;

class SelectionExample
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    SelectionExample();
    ~SelectionExample();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the SelectionExample.cpp file. 
    // You are REQUIRED to write the implementation for these funtions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int ok_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    int filter_cb(NXOpen::BlockStyler::UIBlock*  block, NXOpen::TaggedObject* selectObject);
    
private:
    std::string theDialogName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::UIBlock* group0;// Block type: Group
    NXOpen::BlockStyler::UIBlock* edgeSelect;// Block type: Curve Collector
    NXOpen::BlockStyler::UIBlock* faceToggle;// Block type: Toggle
    NXOpen::BlockStyler::UIBlock* angleDouble;// Block type: Double
    NXOpen::BlockStyler::UIBlock* group01;// Block type: Group
    NXOpen::BlockStyler::UIBlock* chamferSelect;// Block type: Select Feature
    NXOpen::BlockStyler::UIBlock* angleToggle;// Block type: Toggle
    NXOpen::BlockStyler::UIBlock* angleLimitDouble;// Block type: Double

    //NEW CODE
    NXOpen::Face* limitingFace; //face to limit edge selection

    NXOpen::Face* sharedFace(NXOpen::Edge* edge1, NXOpen::Edge* edge2);
    void addChamfer(NXOpen::Edge* selectedEdge, double angle);
    int deleteObject(NXOpen::NXObject* selectedObject);

    int faceFilter(NXOpen::Edge* selectedEdge);
    int angleFilter(NXOpen::Features::Chamfer* chamferFeature);
};
#endif //SELECTIONEXAMPLE_H_INCLUDED
