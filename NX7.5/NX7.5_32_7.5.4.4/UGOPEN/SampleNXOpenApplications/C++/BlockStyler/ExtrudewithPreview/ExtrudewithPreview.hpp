//=============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//
#ifndef EXTRUDEWITHPREVIEW_H_INCLUDED
#define EXTRUDEWITHPREVIEW_H_INCLUDED

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
#define          SnapPointTypesOnByDefault_UserDefined (1 << 0);
#define             SnapPointTypesOnByDefault_Inferred (1 << 1);
#define       SnapPointTypesOnByDefault_ScreenPosition (1 << 2);
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
#define SnapPointTypesOnByDefault_TwocurveIntersection (1 <<13);
#define         SnapPointTypesOnByDefault_TangentPoint (1 <<14);
#define                SnapPointTypesOnByDefault_Poles (1 <<15);
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
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Forward declaration for Class
//------------------------------------------------------------------------------
class ExtrudewithPreview;

namespace NXOpen
{
    class Direction;
    class Part;
    class TaggedObject;
    namespace Features
    {
        class Feature;
    }
}
//
//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
extern ExtrudewithPreview *theExtrudewithPreview;

class ExtrudewithPreview
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    ExtrudewithPreview();
    ~ExtrudewithPreview();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the ExtrudewithPreview.cpp file. 
    // You are REQUIRED to write the implementation for these funtions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    void focusNotify_cb(NXOpen::BlockStyler::UIBlock*, bool );
    
private:
    std::string theDialogName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::UIBlock* SectionGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* SectionToExtrude;// Block type: Section Builder
    NXOpen::BlockStyler::UIBlock* DirectionGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* DirectionToExtrude;// Block type: Specify Vector
    NXOpen::BlockStyler::UIBlock* LimitsGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* StartLimit;// Block type: Linear Dim
    NXOpen::BlockStyler::UIBlock* EndLimit;// Block type: Linear Dim
    NXOpen::BlockStyler::UIBlock* PreviewGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* PreviewToggle;// Block type: Toggle
    NXOpen::BlockStyler::UIBlock* ResultButton;// Block type: Button

    Part* workPart;
    Part* displayPart;
    std::vector<NXOpen::TaggedObject *> vectCol;
    NXOpen::Direction* extrudeDirection;
    std::vector<NXOpen::TaggedObject *> tagObjArray;
    NXOpen::Features::Feature* feature1;
    bool isFeatureCreated;
    bool preview;
    NXOpen::Session::UndoMarkId markId1;
    double startValueOfExt;
    double endValueOfExt;
    NXOpen::Direction* directionToSet;
    bool value;
	bool Translucency1;

    void createExtrude();
    void redefineFeature();
    void visibility();
    void showOrCreate(int transparencyValue);
    void setBoolean(bool value);
    NXString doubleToNXString(double value);
    NXString intToNXString(int value);
    
};
#endif //EXTRUDEWITHPREVIEW_H_INCLUDED
