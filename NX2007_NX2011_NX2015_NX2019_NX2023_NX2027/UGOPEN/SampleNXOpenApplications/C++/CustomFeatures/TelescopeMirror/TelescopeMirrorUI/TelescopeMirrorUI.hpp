//=============================================================================
//
//                   Copyright (c) 2015 Siemens Industry Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Custom feature 
//=============================================================================
//

#ifndef TELESCOPEMIRRORUI_H_INCLUDED
#define TELESCOPEMIRRORUI_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------

//--------Added Code from Template-----------
// Mandatory UF Includes
#include <uf.h>
#include <uf_object_types.h>

// Internal Includes
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/UI.hxx>

// Internal+External Includes
#include <NXOpen/Annotations.hxx>
#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Assemblies_ComponentAssembly.hxx>
#include <NXOpen/Body.hxx>
#include <NXOpen/BodyCollection.hxx>
#include <NXOpen/Face.hxx>
#include <NXOpen/Line.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>

// Std C++ Includes
#include <iostream>
#include <sstream>

using std::string;
using std::exception;
using std::stringstream;
using std::endl;
using std::cout;
using std::cerr;
//-------------------------------------------

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
#include <NXOpen/BlockStyler_TabControl.hxx>
#include <NXOpen/BlockStyler_Group.hxx>
#include <NXOpen/BlockStyler_SpecifyPoint.hxx>
#include <NXOpen/BlockStyler_SpecifyVector.hxx>
#include <NXOpen/BlockStyler_ExpressionBlock.hxx>
#include <NXOpen/BlockStyler_Label.hxx>
#include <NXOpen/BlockStyler_Toggle.hxx>
#include <NXOpen/BlockStyler_Enumeration.hxx>

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
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

class DllExport TelescopeMirrorUI
{
    // class members
public:
    enum geomOptrics
    {
        spherical,
        prolateEllipse,
        parabola,
        hyperbola
    };

    enum aperShapes
    {
        ellipse,
        rectangle,
        hexagonV,
        hexagonF
    };

    static Session *theSession;
    static UI *theUI;
    TelescopeMirrorUI();
    static void Show_MirrorGeneratorUI();
    ~TelescopeMirrorUI();
    int Show();
    void RegisterWithMenu();
    
    //--------Added Code from Template-----------
    void print(const NXString &);
    void print(const string &);
    void print(const char*);
    //-------------------------------------------


    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementation
    // of these prototypes is provided in the MirrorGeneratorUI.cpp file. 
    // You are REQUIRED to write the implementation for these functions.
    //------------------------------------------------------------------------------
    void initialize_cb();

    void PopulateUIFromCustomFeatureData(NXOpen::Features::CustomFeatureData * cfData);

    void CreateAndSetExpressionsObjects(NXOpen::Part * workPart);

    void dialogShown_cb();
    int apply_cb();

    void PopulateAttributeValues(NXOpen::Features::CustomFeatureData * cfData);

    void CreateFeatureAttributes(std::vector<NXOpen::Features::CustomAttribute*> &attrs);

    int ok_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    int filter_cb(NXOpen::BlockStyler::UIBlock*  block, NXOpen::TaggedObject* selectObject);
    void focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus);
    bool enableOKButton_cb();
    PropertyList* GetBlockProperties(const char *blockID);
    
    void SetCurrentGeomInUI(double);


private:
    const char* theDlxFileName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::TabControl* tabControl;// Block type: Tabs Page
    NXOpen::BlockStyler::Group* tabPage;// Block type: Group
    NXOpen::BlockStyler::Group* group0;// Block type: Group
    NXOpen::BlockStyler::SpecifyPoint* m_location;// Block type: Specify Point
    NXOpen::BlockStyler::SpecifyVector* m_direction;// Block type: Specify Vector
    NXOpen::BlockStyler::Group* group;// Block type: Group
    NXOpen::BlockStyler::ExpressionBlock* m_baseDia;// Block type: Expression
    NXOpen::BlockStyler::ExpressionBlock* m_conicConstant;// Block type: Expression
    NXOpen::BlockStyler::ExpressionBlock* m_radiusOfCurvature;// Block type: Expression
    NXOpen::BlockStyler::Label* m_typeOfCurve;// Block type: Label
    NXOpen::BlockStyler::Group* group1;// Block type: Group
    NXOpen::BlockStyler::ExpressionBlock* m_thickAtCenter;// Block type: Expression
    NXOpen::BlockStyler::Group* group2;// Block type: Group
    NXOpen::BlockStyler::Toggle* m_SuppressTrim;// Block type: Toggle
    NXOpen::BlockStyler::Group* tabPage1;// Block type: Group
    NXOpen::BlockStyler::Group* group3;// Block type: Group
    NXOpen::BlockStyler::SpecifyVector* m_primaryDir;// Block type: Specify Vector
    NXOpen::BlockStyler::Group* group4;// Block type: Group
    NXOpen::BlockStyler::Enumeration* m_aperatureShape;// Block type: Enumeration
    NXOpen::BlockStyler::Enumeration* m_trimDir;// Block type: Enumeration
    NXOpen::BlockStyler::ExpressionBlock* m_primaryLen;// Block type: Expression
    NXOpen::BlockStyler::ExpressionBlock* m_secondaryLen;// Block type: Expression
    NXOpen::BlockStyler::Group* group5;// Block type: Group
    NXOpen::BlockStyler::ExpressionBlock* m_primaryOffset;// Block type: Expression
    NXOpen::BlockStyler::ExpressionBlock* m_secondaryOffset;// Block type: Expression
    NXOpen::BlockStyler::Group* group6;// Block type: Group
    NXOpen::BlockStyler::Toggle* m_SuppressAper;// Block type: Toggle
    
    Part *workPart, *displayPart;
    NXMessageBox *mb;
    ListingWindow *lw;

    double m_baseDiacache;
    bool m_baseDiaCached = false;

    double m_conicConstantcache;
    bool m_conicConstantCached = false;

    double m_radiusOfCurvaturecache;
    bool m_radiusOfCurvatureCached = false;

    double m_thickAtCentercache;
    bool m_thickAtCenterCached = false;

    double m_primaryLencache;
    bool m_primaryLenCached = false;

    double m_secondaryLencache;
    bool m_secondaryLenCached = false;

    double m_primaryOffsetcache;
    bool m_primaryOffsetCached = false;

    double m_secondaryOffsetcache;
    bool m_secondaryOffsetCached = false;


    NXOpen::NXString m_aperatureShapecache;
    bool m_aperatureShapeCached = false;

};
#endif //TELESCOPEMIRRORUI_H_INCLUDED
