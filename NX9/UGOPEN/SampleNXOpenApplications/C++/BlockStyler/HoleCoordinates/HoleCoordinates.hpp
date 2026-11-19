//=============================================================================
//
//                   Copyright (c) 2008 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//

#ifndef HOLECOORDINATES_H_INCLUDED
#define HOLECOORDINATES_H_INCLUDED

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
#include <NXOpen/BlockStyler_ListBox.hxx>
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
#define                          EntityType_AllowFaces (1 << 4);
#define                         EntityType_AllowDatums (1 << 5);
#define                         EntityType_AllowBodies (1 << 6);
//------------------------------------------------------------------------------
//Bit Option for Property: FaceRules
//------------------------------------------------------------------------------
#define                           FaceRules_SingleFace (1 << 0);
#define                          FaceRules_RegionFaces (1 << 1);
#define                         FaceRules_TangentFaces (1 << 2);
#define                   FaceRules_TangentRegionFaces (1 << 3);
#define                            FaceRules_BodyFaces (1 << 4);
#define                         FaceRules_FeatureFaces (1 << 5);
#define                        FaceRules_AdjacentFaces (1 << 6);
#define                  FaceRules_ConnectedBlendFaces (1 << 7);
#define                        FaceRules_AllBlendFaces (1 << 8);
#define                             FaceRules_RibFaces (1 << 9);
#define                            FaceRules_SlotFaces (1 <<10);
#define                   FaceRules_BossandPocketFaces (1 <<11);
#define                       FaceRules_MergedRibFaces (1 <<12);
#define                  FaceRules_RegionBoundaryFaces (1 <<13);
#define                 FaceRules_FaceandAdjacentFaces (1 <<14);
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Forward declaration for Class
//------------------------------------------------------------------------------
class HoleCoordinates;

namespace NXOpen 
{
    class DatumAxis;
    class Direction;
    class Face;
    class Part;
    class Point;
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
extern HoleCoordinates *theHoleCoordinates;

class HoleCoordinates
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    HoleCoordinates();
    ~HoleCoordinates();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the HoleCoordinates.cpp file. 
    // You are REQUIRED to write the implementation for these funtions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    
private:
    std::string theDialogName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::UIBlock* groupPoint;// Block type: Group
    NXOpen::BlockStyler::UIBlock* origin;// Block type: Specify Point
    NXOpen::BlockStyler::UIBlock* groupXdir;// Block type: Group
    NXOpen::BlockStyler::UIBlock* xDir;// Block type: Specify Vector
    NXOpen::BlockStyler::UIBlock* groupYdir;// Block type: Group
    NXOpen::BlockStyler::UIBlock* yDir;// Block type: Specify Vector
    NXOpen::BlockStyler::UIBlock* groupFace;// Block type: Group
    NXOpen::BlockStyler::UIBlock* face;// Block type: Face Collector
    NXOpen::BlockStyler::UIBlock* groupInfo;// Block type: Group
    NXOpen::BlockStyler::UIBlock* buttonInfo;// Block type: Button
    NXOpen::BlockStyler::ListBox* listBoxInfo;// Block type: List Box
    
    NXOpen::DatumAxis* datumaxiscreater(NXOpen::Point* point1, NXOpen::Direction* direction1);
    double holedimension(NXOpen::DatumAxis* refaxis1, NXOpen::DatumAxis* refaxis2, NXOpen::Point* refpoint1);
    void deletedatumaxis(std::vector<NXObject *> objects1);
    NXOpen::DatumAxis* editdatumaxis(NXOpen::DatumAxis* datumaxis1, NXOpen::Direction* vect1, NXOpen::Point* origpoint);
    void setEnablePropForBlock(NXOpen::BlockStyler::UIBlock* blk, bool value);
    std::vector<std::string> splitStrings(const std::string& stringToSplit);

    // user defined variables
    NXOpen::DatumAxis* refaxis1;
    NXOpen::DatumAxis* refaxis2;
    NXOpen::Point* axispoint;
    NXOpen::Face* holeface;
    NXOpen::Features::Feature* highlightedFeature;
    NXOpen::Part* workPart;
    NXOpen::Part* displayPart;
    NXOpen::Point* point1;
    std::vector<NXOpen::TaggedObject* > vectCol;
    std::vector<NXOpen::TaggedObject* > vectCol1;
    std::vector<NXOpen::TaggedObject* > pointCol;
    std::vector<NXOpen::TaggedObject* > faceCol;
    std::vector<NXOpen::NXObject* > objects1;
    std::vector<NXOpen::NXString> allholesNX5;
    std::vector<NXOpen::NXString> allholesNX6;
    NXOpen::Point3d holelocation;
    double holeCoordinates;
};
#endif //HOLECOORDINATES_H_INCLUDED
