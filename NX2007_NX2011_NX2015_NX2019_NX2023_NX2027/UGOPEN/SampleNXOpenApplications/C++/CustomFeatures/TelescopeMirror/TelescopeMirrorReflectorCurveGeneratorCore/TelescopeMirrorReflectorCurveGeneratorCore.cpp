//=============================================================================
//
//                   Copyright (c) 2015 Siemens Industry Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Custom feature 
//=============================================================================
//

//==============================================================================
//  Purpose:  This TEMPLATE file contains C++ source to guide you in the
//  construction of core library for custom feature.
//
//  1.  Help on how to write Core library for custom feature
//      using APIs provided in NXOpen namespace
//  2.  The empty callback methods (stubs) associated with custom feature
//      have also been placed in this file. These empty methods have been
//      created simply to start you along with your coding requirements.
//      The method name, argument list and possible return values have already
//      been provided for you.
//==============================================================================

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
#include <NXOpen/Point.hxx>
#include <NXOpen/Direction.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>

#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/Xform.hxx>
#include <NXOpen/XformCollection.hxx>
#include <NXOpen/CartesianCoordinateSystem.hxx>
#include <NXOpen/NXMatrixCollection.hxx>
#include <NXOpen/CoordinateSystemCollection.hxx>
#include <NXOpen/Ellipse.hxx>
#include <NXOpen/CurveCollection.hxx>
#include <NXOpen/Features_RevolveBuilder.hxx>
#include <NXOpen/GeometricUtilities_Limits.hxx>
#include <NXOpen/GeometricUtilities_Extend.hxx>
#include <NXOpen/SectionCollection.hxx>
#include <NXOpen/ScRuleFactory.hxx>
#include <NXOpen/DirectionCollection.hxx>
#include <NXOpen/AxisCollection.hxx>
#include <NXOpen/CurveDumbRule.hxx>
#include <NXOpen/BodyDumbRule.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/SelectBodyList.hxx>

#include <NXOpen/Features_CylinderBuilder.hxx>
#include <NXOpen/GeometricUtilities_BooleanOperation.hxx>
#include <NXOpen/Axis.hxx>
#include <NXOpen/PointCollection.hxx>
#include <NXOpen/Features_BooleanBuilder.hxx>
#include <NXOpen/ScCollectorCollection.hxx>

#include <NXOpen/Features_ExtrudeBuilder.hxx>
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/Features_OutputFeatureData.hxx>

// Custom Feature specific Includes
#include <NXOpen/Features_CustomFeaturePreUpdateEvent.hxx>
#include <NXOpen/Features_CustomFeatureCreateFeatureGeometryEvent.hxx>
#include <NXOpen/Features_CustomFeatureModifyFeatureGeometryEvent.hxx>
#include <NXOpen/Features_CustomFeaturePostUpdateEvent.hxx>
#include <NXOpen/Features_CustomFeatureInformationEvent.hxx>
#include <NXOpen/Features_CustomFeature.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>

// Std C++ Includes
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace NXOpen;
using std::string;
using std::exception;
using std::stringstream;
using std::endl;
using std::cout;
using std::cerr;

//------------------------------------------------------------------------------
// NXOpen c++ test class 
//------------------------------------------------------------------------------
class TelescopeMirrorReflectorCurveGeneratorCore
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;

    TelescopeMirrorReflectorCurveGeneratorCore();
    ~TelescopeMirrorReflectorCurveGeneratorCore();

    static int preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event);
    static int createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event);
    static int modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event);

    static int postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event);
    static int informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event);

    static int GenerateCurveToRevolve(NXOpen::Features::CustomFeatureData* cfData, NXOpen::Curve** pedastal);
    static int GenereateCircelPedastal(double radiusOfCurvature, Point3d basePoint, Vector3d upDirection, NXOpen::Curve **circularArc);
    static int GenereateHyperBolaPedastal(double radiusOfCurvature, double conicConstant, double baseDia, Point3d basePoint, Vector3d upDirection, NXOpen::Curve **heperBola);
    static int GenereateParaBolaPedastal(double radiusOfCurvature, double conicConstant, double baseDia, Point3d basePoint, Vector3d upDirection);
    static int GenereateEllipsePedastal(double radiusOfCurvature, double conicConstant, Point3d basePoint, Vector3d upDirection, NXOpen::Curve **ellipse1);
   
private:
    Part *workPart, *displayPart;
    NXMessageBox *mb;
    ListingWindow *lw;
};

NXOpen::Vector3d  GetPerpandicularVector(NXOpen::Vector3d u)
{
    NXOpen::Vector3d outVec;
    NXOpen::Vector3d unitVec1;

    double vecMagnitude = sqrt((u.X*u.X) + (u.Y*u.Y) + (u.Z*u.Z));

    unitVec1.X = 1.0 / vecMagnitude *u.X;
    unitVec1.Y = 1.0 / vecMagnitude *u.Y;
    unitVec1.Z = 1.0 / vecMagnitude *u.Z;

    NXOpen::Vector3d unitVec2;
    if (abs(unitVec1.X) != 1.0)
    {
        unitVec2.X = 1.0;
        unitVec2.Y = 0.0;
        unitVec2.Z = 0.0;
    }
    else
    {
        unitVec2.X = 0.0;
        unitVec2.Y = 1.0;
        unitVec2.Z = 0.0;
    }

    outVec.X = unitVec1.Y*unitVec2.Z - unitVec1.Z* unitVec2.Y;
    outVec.Y = unitVec1.Z*unitVec2.X - unitVec1.X* unitVec2.Z;
    outVec.Z = unitVec1.X*unitVec2.Y - unitVec1.Y* unitVec2.X;

    double outVecMagnitude = sqrt((outVec.X*outVec.X) + (outVec.Y*outVec.Y) + (outVec.Z*outVec.Z));

    outVec.X = 1.0 / outVecMagnitude *outVec.X;
    outVec.Y = 1.0 / outVecMagnitude *outVec.Y;
    outVec.Z = 1.0 / outVecMagnitude *outVec.Z;

    return outVec;
}

int TelescopeMirrorReflectorCurveGeneratorCore::GenereateCircelPedastal(double radiusOfCurvature, Point3d basePoint, Vector3d upDirection, NXOpen::Curve **circularArc)
{
    Session* theSession = Session::GetSession();
    int error = 0;
    try
    {
        Point3d center(0.0, 0.0, 0.0);

        {
            center.X = basePoint.X + (upDirection.X * radiusOfCurvature);
            center.Y = basePoint.Y + (upDirection.Y * radiusOfCurvature);
            center.Z = basePoint.Z + (upDirection.Z * radiusOfCurvature);
        }

        double startAng = 0;
        double endAngle = 90;

        Vector3d xDir(-upDirection.X, -upDirection.Y, -upDirection.Z);
        Vector3d yDir = GetPerpandicularVector(xDir);

        NXOpen::Part *workPart(theSession->Parts()->Work());

        *circularArc = (NXOpen::Curve*)(workPart->Curves()->CreateArc(center, xDir, yDir, radiusOfCurvature, (startAng* DEGRA), (endAngle* DEGRA)));
    }
    catch (exception& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = 1;
    }
    return error;
}

int TelescopeMirrorReflectorCurveGeneratorCore::GenereateHyperBolaPedastal(double radiusOfCurvature, double conicConstant, double baseDia, Point3d basePoint, Vector3d upDirection, NXOpen::Curve **heperBola)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        double d6, d7, hy_a, hy_b, hy_c, hy_diam;

        d6 = -1 * (radiusOfCurvature / (conicConstant + 1) * sqrt(-1 * conicConstant) + 1);
        d7 = -1 * (radiusOfCurvature / (conicConstant + 1) * sqrt(-1 * conicConstant) - 1);

        hy_a = (d6 - d7) / 2;
        hy_c = (d6 + d7) / 2;
        hy_b = sqrt((hy_c * hy_c) - (hy_a*hy_a));
        hy_diam = ((2 * hy_b * hy_b) / hy_a);

        Vector3d xDirection(0.0, 0.0, 0.0), yDirection(0.0, 0.0, 0.0);
        Point3d centerP(0, 0, 0);

        centerP.X = upDirection.X *(-hy_a);
        centerP.Y = upDirection.Y *(-hy_a);
        centerP.Z = upDirection.Z *(-hy_a);

        if (upDirection.X)
        {
            xDirection.Y = 1.0;
            yDirection.Z = 1.0;
        }
        else if (upDirection.Z)
        {
            xDirection.X = 1.0;
            yDirection.Y = 1.0;
        }
        else
        {
            xDirection.X = 1.0;
            yDirection.Z = 1.0;
        }

        NXOpen::Part *workPart(theSession->Parts()->Work());
        NXOpen::Xform *xform10;
        xform10 = workPart->Xforms()->CreateXform(centerP, xDirection, yDirection, NXOpen::SmartObject::UpdateOptionWithinModeling, 1.0);

        NXOpen::NXMatrixCollection* matrixCollection = workPart->NXMatrices();
        NXOpen::NXMatrix *nXMatrix1 = matrixCollection->Create(xform10->Orientation());

        *heperBola = (NXOpen::Curve*)workPart->Curves()->CreateHyperbola(centerP, hy_a / 2, hy_b / 2, -1.0, baseDia*0.51, 0.0, nXMatrix1);

    }
    catch (exception& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = 1;
    }
    return error;
}

int TelescopeMirrorReflectorCurveGeneratorCore::GenereateParaBolaPedastal(double radiusOfCurvature, double conicConstant, double baseDia, Point3d basePoint, Vector3d upDirection)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        Session* theSession = Session::GetSession();
        double d5, d6, d7, hy_a, hy_b, hy_c, hy_diam;

        d5 = radiusOfCurvature / 2;

        d7 = -1 * (radiusOfCurvature / (conicConstant + 1) * sqrt(-1 * conicConstant) - 1);

        hy_a = (d6 - d7) / 2;
        hy_c = (d6 + d7) / 2;
        hy_b = sqrt((hy_c * hy_c) - (hy_a*hy_a));
        hy_diam = ((2 * hy_b * hy_b) / hy_a);

        Vector3d xDirection(0.0, 0.0, 0.0), yDirection(0.0, 0.0, 0.0);
        Point3d centerP(0, 0, 0);

        centerP.X = upDirection.X *(-hy_a);
        centerP.Y = upDirection.Y *(-hy_a);
        centerP.Z = upDirection.Z *(-hy_a);

        if (upDirection.X)
        {
            xDirection.Y = 1.0;
            yDirection.Z = 1.0;
        }
        else if (upDirection.Z)
        {
            xDirection.X = 1.0;
            yDirection.Y = 1.0;
        }
        else
        {
            xDirection.X = 1.0;
            yDirection.Z = 1.0;
        }

        NXOpen::Part *workPart(theSession->Parts()->Work());
        NXOpen::Xform *xform10;
        xform10 = workPart->Xforms()->CreateXform(centerP, xDirection, yDirection, NXOpen::SmartObject::UpdateOptionWithinModeling, 1.0);

        NXOpen::NXMatrixCollection* matrixCollection = workPart->NXMatrices();
        NXOpen::NXMatrix *nXMatrix1 = matrixCollection->Create(xform10->Orientation());
    }
    catch (exception& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = 1;
    }
    return error;
}

int TelescopeMirrorReflectorCurveGeneratorCore::GenereateEllipsePedastal(double radiusOfCurvature, double conicConstant, Point3d basePoint, Vector3d upDirection, NXOpen::Curve **ellipse1)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        double d1, d2, d3, d4;

        d1 = radiusOfCurvature / (conicConstant + 1);
        d2 = d1 * (2 * sqrt(-1 * conicConstant));
        d3 = d1 * (1 + sqrt(-1 * conicConstant));
        d4 = d1 * (1 - sqrt(-1 * conicConstant));

        double el_a, el_b, el_c, el_diam;

        el_a = ((d3 + d4) / 2);
        el_c = ((d3 - d4) / 2);
        el_b = (sqrt((el_a * el_a) - (el_c *el_c)));
        el_diam = ((2 * el_b*el_b) / el_a);

        Point3d center(0.0, 0.0, 0.0);
        Vector3d xDir(0.0, 0.0, 0.0), yDir(0.0, 0.0, 0.0);
        double startAng, endAngel;
        if (upDirection.Z)
        {
            xDir.X = 1.0;
            yDir.Z = 1.0;
            center.Z = el_a;
            startAng = -90.0;
            endAngel = 0.0;
        }
        else if (upDirection.X)
        {
            xDir.Y = 1.0;
            yDir.X = 1.0;
            center.X = el_a;
            startAng = -90.0;
            endAngel = 0.0;
        }
        else
        {
            xDir.Y = 1.0;
            yDir.Z = 1.0;
            center.Y = el_a;
            startAng = 90.0;
            endAngel = 180.0;
        }

        double majorRadis = el_a;
        double minorRadius = el_b;
        double focalLength = 2 * radiusOfCurvature;

        Vector3d xDirection(1.0, 0.0, 0.0);
        NXOpen::Part *workPart(theSession->Parts()->Work());

        NXOpen::Xform *xform10;
        xform10 = workPart->Xforms()->CreateXform(basePoint, xDir, yDir, NXOpen::SmartObject::UpdateOptionWithinModeling, 1.0);

        NXOpen::CartesianCoordinateSystem *cartesianCoordinateSystem6;
        cartesianCoordinateSystem6 = workPart->CoordinateSystems()->CreateCoordinateSystem(xform10, NXOpen::SmartObject::UpdateOptionWithinModeling);

        NXOpen::NXMatrixCollection* matrixCollection = workPart->NXMatrices();
        NXOpen::NXMatrix *nXMatrix1 = matrixCollection->Create(xform10->Orientation());

        *ellipse1 = workPart->Curves()->CreateEllipse(center, majorRadis, minorRadius, (startAng * DEGRA), (endAngel * DEGRA), 0.0, nXMatrix1);

    }
    catch (exception& ex)
    {
        error = 0;
        //---- Enter your exception handling code here -----

    }
    return error;
}

int TelescopeMirrorReflectorCurveGeneratorCore::GenerateCurveToRevolve(NXOpen::Features::CustomFeatureData* cfData, NXOpen::Curve** pedastal)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        NXOpen::Features::CustomExpressionAttribute* m_radiusOfCurvatureAttrib = cfData->CustomExpressionAttributeByName("m_radiusOfCurvature");
        NXOpen::Expression* radiusOfCurvatureExp = dynamic_cast<NXOpen::Expression*>(m_radiusOfCurvatureAttrib->Value());
        double radiusOfCurvature = radiusOfCurvatureExp->Value();

        NXOpen::Features::CustomExpressionAttribute* m_conicConstantAttrib = cfData->CustomExpressionAttributeByName("m_conicConstant");
        NXOpen::Expression* conicConstantExp = dynamic_cast<NXOpen::Expression*>(m_conicConstantAttrib->Value());
        double  conicConstant = conicConstantExp->Value();

        NXOpen::Features::CustomTagAttribute* m_locationAttrib = cfData->CustomTagAttributeByName("m_location");
        NXOpen::Point* location = dynamic_cast<NXOpen::Point*>(m_locationAttrib->Value());
        NXOpen::Point3d basePoint = location->Coordinates();

        NXOpen::Features::CustomTagAttribute* m_directionAttrib = cfData->CustomTagAttributeByName("m_direction");
        NXOpen::Direction* direction = dynamic_cast<NXOpen::Direction*>(m_directionAttrib->Value());
        NXOpen::Vector3d upDirection = direction->Vector();

        if (conicConstant == 0)
        {
            GenereateCircelPedastal(radiusOfCurvature, basePoint, upDirection, pedastal);
        }
        else if (0 > conicConstant && conicConstant > -1)
        {
            GenereateEllipsePedastal(radiusOfCurvature, conicConstant, basePoint, upDirection, pedastal);
        }
        else if (conicConstant == -1)
        {

        }
        else if (conicConstant < -1)
        {

        }

        if (*pedastal != NULL)
        {
            (*pedastal)->SetVisibility(NXOpen::SmartObject::VisibilityOption::VisibilityOptionVisible);

            (*pedastal)->RedisplayObject();
        }

    }
    catch (exception& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = 1;
    }
    return error;
}



int TelescopeMirrorReflectorCurveGeneratorCore::preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
    }
    catch (exception& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = 1;
    }
    return error;
}


int TelescopeMirrorReflectorCurveGeneratorCore::createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        NXOpen::Features::CustomFeature* customFeature = event->GetCustomFeature();

        NXOpen::Features::CustomFeatureData* cfData = customFeature->FeatureData();

        NXOpen::Curve* curveToRevolve = NULL;

        GenerateCurveToRevolve(cfData, &curveToRevolve);

        // Label Curve to revolve
        std::vector < NXOpen::Features::TrackingData*> trackVector;
        if (curveToRevolve)
        {
            NXOpen::Features::TrackingData* track = event->CreateTrackingDataForNXObject(curveToRevolve);
            track->AddIntSourceEntity(1);
            trackVector.push_back(track);
        }

        event->AppendOutputTrackingData(trackVector);

    }
    catch (exception& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = 1;
    }
    return error;
}

int TelescopeMirrorReflectorCurveGeneratorCore::modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {

    }
    catch (exception& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = 1;
    }
    return error;
}

int TelescopeMirrorReflectorCurveGeneratorCore::postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {

    }
    catch (exception& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = 1;
    }
    return error;
}

int TelescopeMirrorReflectorCurveGeneratorCore::informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        NXString string = "This is custom information \n \t\t Custom feature has not yet implemented custom code to show custom information";
        event->SetInformation(string);
    }
    catch (exception& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = 1;
    }
    return error;
}
//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(TelescopeMirrorReflectorCurveGeneratorCore::theSession) = NULL;
UI *(TelescopeMirrorReflectorCurveGeneratorCore::theUI) = NULL;

//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
TelescopeMirrorReflectorCurveGeneratorCore::TelescopeMirrorReflectorCurveGeneratorCore()
{

    // Initialize the NX Open C++ API environment
    TelescopeMirrorReflectorCurveGeneratorCore::theSession = NXOpen::Session::GetSession();
    TelescopeMirrorReflectorCurveGeneratorCore::theUI = UI::GetUI();
    mb = theUI->NXMessageBox();
    lw = theSession->ListingWindow();

    workPart = theSession->Parts()->Work();
    displayPart = theSession->Parts()->Display();

    NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

    NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::TelescopeMirrorReflectorCurveGenerator");

    // Registration of callback functions
    cfClass->AddPreUpdateHandler(make_callback(&TelescopeMirrorReflectorCurveGeneratorCore::preUpdateCallBack));
    cfClass->AddCreateFeatureGeometryHandler(make_callback(&TelescopeMirrorReflectorCurveGeneratorCore::createGeometryCallBack));
    cfClass->AddModifyFeatureGeometryHandler(make_callback(&TelescopeMirrorReflectorCurveGeneratorCore::modifyGeometryCallBack));
    cfClass->AddPostUpdateHandler(make_callback(&TelescopeMirrorReflectorCurveGeneratorCore::postUpdateCallBack));

    cfClass->AddInformationHandler(make_callback(&TelescopeMirrorReflectorCurveGeneratorCore::informationCallBack));
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
TelescopeMirrorReflectorCurveGeneratorCore::~TelescopeMirrorReflectorCurveGeneratorCore()
{
}

//------------------------------------------------------------------------------
// Entry point(s) for unmanaged internal NXOpen C/C++ programs
//------------------------------------------------------------------------------
//  Explicit Execution
extern "C" DllExport void ufusr(char *parm, int *returnCode, int rlen)
{
    try
    {
        // Create NXOpen C++ class instance
        TelescopeMirrorReflectorCurveGeneratorCore *theMirrorReflectorCurveGeneratorCore;
        theMirrorReflectorCurveGeneratorCore = new TelescopeMirrorReflectorCurveGeneratorCore();
        delete theMirrorReflectorCurveGeneratorCore;
    }
    catch (const NXException& e1)
    {
        UI::GetUI()->NXMessageBox()->Show("NXException", NXOpen::NXMessageBox::DialogTypeError, e1.Message());
    }
    catch (const exception& e2)
    {
        UI::GetUI()->NXMessageBox()->Show("Exception", NXOpen::NXMessageBox::DialogTypeError, e2.what());
    }
    catch (...)
    {
        UI::GetUI()->NXMessageBox()->Show("Exception", NXOpen::NXMessageBox::DialogTypeError, "Unknown Exception.");
    }
}


//------------------------------------------------------------------------------
// Unload Handler
//------------------------------------------------------------------------------
extern "C" DllExport int ufusr_ask_unload()
{
    return (int)NXOpen::Session::LibraryUnloadOptionAtTermination;
}


