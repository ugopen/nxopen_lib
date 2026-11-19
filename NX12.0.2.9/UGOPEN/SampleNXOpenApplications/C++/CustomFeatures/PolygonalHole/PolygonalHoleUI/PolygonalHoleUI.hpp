//=============================================================================
//
//                   Copyright (c) 2015 Siemens Industry Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Custom feature 
//=============================================================================
//

#ifndef POLYGONALHOLEUI_H_INCLUDED
#define POLYGONALHOLEUI_H_INCLUDED

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
#include <NXOpen/BlockStyler_SpecifyPoint.hxx>
#include <NXOpen/BlockStyler_ExpressionBlock.hxx>
#include <NXOpen/BlockStyler_IntegerBlock.hxx>
#include <NXOpen/BlockStyler_SpecifyVector.hxx>
#include <NXOpen/BlockStyler_BodyCollector.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>
#include <NXOpen/Part.hxx>


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
#define     SnapPointTypesOnByDefault_FacetVertexPoint (1 <<17);
//------------------------------------------------------------------------------
//Bit Option for Property: EntityType
//------------------------------------------------------------------------------
#define                         EntityType_AllowBodies (1 << 6);
//------------------------------------------------------------------------------
//Bit Option for Property: BodyRules
//------------------------------------------------------------------------------
#define                           BodyRules_SingleBody (1 << 0);
#define                        BodyRules_FeatureBodies (1 << 1);
#define                        BodyRules_BodiesinGroup (1 << 2);
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

class DllExport PolygonalHoleUI
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    PolygonalHoleUI();
    ~PolygonalHoleUI();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementation
    // of these prototypes is provided in the PolygonalHoleUI.cpp file. 
    // You are REQUIRED to write the implementation for these functions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int ok_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    PropertyList* GetBlockProperties(const char *blockID);

    void PopulateUIFromCustomFeatureData(NXOpen::Features::CustomFeatureData * cfData);
    void CreateAndSetExpressionsObjects(NXOpen::Part * workPart);
    void PopulateAttributeValues(NXOpen::Features::CustomFeatureData * cfData);
    void CreateFeatureAttributes(std::vector<NXOpen::Features::CustomAttribute*> &attrs);
    
private:
    const char* theDlxFileName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::Group* PolygonDefinition;// Block type: Group
    NXOpen::BlockStyler::SpecifyPoint* polygonPoint;// Block type: Specify Point
    NXOpen::BlockStyler::ExpressionBlock* polygonDiameter;// Block type: Expression
    NXOpen::BlockStyler::IntegerBlock* numSides;// Block type: Integer
    NXOpen::BlockStyler::Group* holeDefinitio;// Block type: Group
    NXOpen::BlockStyler::ExpressionBlock* holeDepth;// Block type: Expression
    NXOpen::BlockStyler::SpecifyVector* holeDirection;// Block type: Specify Vector
    NXOpen::BlockStyler::BodyCollector* targetBody;// Block type: Body Collector
	
	NXOpen::Features::CustomFeatureClassManager * mgr; // Custom feature class manager 
	NXOpen::Features::CustomFeatureClass* cfClass;  //Custom feature class

    int polygonSidesCache;
    bool polygonSidesCached = false;

    double polygonDiameterCache;
    bool polygonDiameterCached = false;

    double polygonDepthCache;
    bool polygonDepthCached = false;
    
};
#endif //POLYGONALHOLEUI_H_INCLUDED
