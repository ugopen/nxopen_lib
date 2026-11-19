//=============================================================================
//
//                   Copyright (c) 2015 Siemens Industry Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Custom feature 
//=============================================================================
//

#ifndef PatternCurveUI_H_INCLUDED
#define PatternCurveUI_H_INCLUDED

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
#include <NXOpen/BlockStyler_SectionBuilder.hxx>
#include <NXOpen/BlockStyler_SpecifyVector.hxx>
#include <NXOpen/BlockStyler_ExpressionBlock.hxx>
#include <NXOpen/BlockStyler_LinearDimension.hxx>
#include <NXOpen/BlockStyler_Toggle.hxx>

#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>

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
#define         SnapPointTypesEnabled_FacetVertexPoint (1 <<17);
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
//Bit Option for Property: EntityType
//------------------------------------------------------------------------------
#define                 EntityType_AllowEdgesandCurves (1 << 2);
#define                         EntityType_AllowPoints (1 << 3);
//------------------------------------------------------------------------------
//Bit Option for Property: CurveRules
//------------------------------------------------------------------------------
#define                         CurveRules_SingleCurve (1 << 0);
#define                     CurveRules_ConnectedCurves (1 << 1);
#define                       CurveRules_TangentCurves (1 << 2);
#define                           CurveRules_FaceEdges (1 << 3);
#define                          CurveRules_SheetEdges (1 << 5);
#define                       CurveRules_FeatureCurves (1 << 6);
#define                         CurveRules_InferCurves (1 << 7);
#define                CurveRules_RegionBoundaryCurves (1 <<11);
#define                       CurveRules_CurvesinGroup (1 <<12);
#define                   CurveRules_OuterEdgesofFaces (1 <<13);
#define                     CurveRules_RibTopFaceEdges (1 <<14);
#define            CurveRules_FeatureIntersectionEdges (1 <<15);
//------------------------------------------------------------------------------
//Bit Option for Property: SnapPointTypesOnByDefault
//------------------------------------------------------------------------------
#define          SnapPointTypesOnByDefault_UserDefined (1 << 0);
#define             SnapPointTypesOnByDefault_Inferred (1 << 1);
#define       SnapPointTypesOnByDefault_ScreenPosition (1 << 2);
#define SnapPointTypesOnByDefault_TwocurveIntersection (1 <<13);
#define         SnapPointTypesOnByDefault_TangentPoint (1 <<14);
#define                SnapPointTypesOnByDefault_Poles (1 <<15);
#define     SnapPointTypesOnByDefault_FacetVertexPoint (1 <<17);
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

class DllExport PatternCurveUI
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    PatternCurveUI();
    ~PatternCurveUI();
    int Show();
    void RegisterWithMenu();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementation
    // of these prototypes is provided in the PatternCurveUI.cpp file. 
    // You are REQUIRED to write the implementation for these functions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int ok_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    PropertyList* GetBlockProperties(const char *blockID);
    
private:
    const char* theDlxFileName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::Group* group0;// Block type: Group
    NXOpen::BlockStyler::SectionBuilder* section;// Block type: Section Builder
    NXOpen::BlockStyler::Group* group;// Block type: Group
    NXOpen::BlockStyler::Group* group1;// Block type: Group
    NXOpen::BlockStyler::SpecifyVector* d1;// Block type: Specify Vector
    NXOpen::BlockStyler::ExpressionBlock* d1Count;// Block type: Expression
    NXOpen::BlockStyler::LinearDimension* d1Pitch;// Block type: Linear Dim
    NXOpen::BlockStyler::Toggle* UseD2;// Block type: Toggle
    NXOpen::BlockStyler::Group* group11;// Block type: Group
    NXOpen::BlockStyler::SpecifyVector* d2;// Block type: Specify Vector
    NXOpen::BlockStyler::ExpressionBlock* d2Count;// Block type: Expression
    NXOpen::BlockStyler::LinearDimension* d2Pitch;// Block type: Linear Dim

	NXOpen::Features::CustomFeatureClassManager * mgr; // Custom feature class manager 
	NXOpen::Features::CustomFeatureClass* cfClass;  //Custom feature class

    bool   useD2Cached = false;
    bool   useD2Cache = false;
    bool   d1CountCached     = false;
    double d1CountCache = 0.0;
    bool   d1pitchCached      = false;
    double d1PitchCache = 0.1;
    bool   d2CountCached = false;
    double d2CountCache = 0.0;
    bool   d2pitchCached = false;
    double d2PitchCache = 0.1;
};
#endif //PatternCurveUI_H_INCLUDED
