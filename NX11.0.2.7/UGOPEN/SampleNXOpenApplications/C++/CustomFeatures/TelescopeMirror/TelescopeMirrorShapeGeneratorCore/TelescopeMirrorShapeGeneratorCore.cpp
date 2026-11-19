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
class TelescopeMirrorShapeGeneratorCore
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;

    TelescopeMirrorShapeGeneratorCore();
    ~TelescopeMirrorShapeGeneratorCore();

    static int preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event);
    static int createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event);
    static int modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event);

    static int postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event);
    static int informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event);

    static int CreateMirrorShapeCurves(NXOpen::Features::CustomFeature* customFeature, std::vector<NXOpen::Curve *>* curveVec);

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

int TelescopeMirrorShapeGeneratorCore::CreateMirrorShapeCurves(NXOpen::Features::CustomFeature* customFeature, std::vector<NXOpen::Curve *>* curveVec)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        NXOpen::Features::Feature *cylinderFeature = NULL;
        NXOpen::Features::CustomFeatureData* cfData = customFeature->FeatureData();

        NXOpen::Features::CustomExpressionAttribute* m_primaryLenAttrib = cfData->CustomExpressionAttributeByName("m_primaryLen");
        NXOpen::Expression* primaryLenExp = dynamic_cast<NXOpen::Expression*>(m_primaryLenAttrib->Value());
        double primaryLen = primaryLenExp->Value();

        NXOpen::Features::CustomExpressionAttribute* m_secondaryLenAttrib = cfData->CustomExpressionAttributeByName("m_secondaryLen");
        NXOpen::Expression* secondaryLenExp = dynamic_cast<NXOpen::Expression*>(m_secondaryLenAttrib->Value());
        double secondaryLen = secondaryLenExp->Value();

        NXOpen::Features::CustomExpressionAttribute* m_primaryOffsetAttrib = cfData->CustomExpressionAttributeByName("m_primaryOffset");
        NXOpen::Expression* primaryOffsetExp = dynamic_cast<NXOpen::Expression*>(m_primaryOffsetAttrib->Value());
        double primaryOff = primaryOffsetExp->Value();

        NXOpen::Features::CustomExpressionAttribute* m_secondaryOffsetAttrib = cfData->CustomExpressionAttributeByName("m_secondaryOffset");
        NXOpen::Expression* secondaryOffsetExp = dynamic_cast<NXOpen::Expression*>(m_secondaryOffsetAttrib->Value());
        double secondaryOff = secondaryOffsetExp->Value();

        NXOpen::Features::CustomTagAttribute* m_locationAttrib = cfData->CustomTagAttributeByName("m_location");
        NXOpen::Point* location = dynamic_cast<NXOpen::Point*>(m_locationAttrib->Value());
        Point3d basePoint = location->Coordinates();

        NXOpen::Features::CustomTagAttribute* m_directionAttrib = cfData->CustomTagAttributeByName("m_direction");
        NXOpen::Direction* direction = dynamic_cast<NXOpen::Direction*>(m_directionAttrib->Value());
        Vector3d upDirection = direction->Vector();

        NXOpen::Features::CustomStringAttribute* m_aperatureShapeAttrib = cfData->CustomStringAttributeByName("m_aperatureShape");
        NXOpen::NXString apershapes = m_aperatureShapeAttrib->Value();

        Vector3d xDirection(0.0, 0.0, 0.0);
        Vector3d yDirection(0.0, 0.0, 0.0);

        NXOpen::Part *workPart(theSession->Parts()->Work());
        std::vector<NXOpen::Curve *> toReturn;

        Point3d centerP;
        centerP.X = basePoint.X + primaryOff;
        centerP.Y = basePoint.Y + secondaryOff;
        centerP.Z = basePoint.Z;

        const char* nType = apershapes.GetText();

        if (!strcmp(nType, "Ellipse"))
        {
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
            NXOpen::Xform *xform10;
            xform10 = workPart->Xforms()->CreateXform(centerP, xDirection, yDirection, NXOpen::SmartObject::UpdateOptionWithinModeling, 1.0);

            NXOpen::NXMatrixCollection* matrixCollection = workPart->NXMatrices();
            NXOpen::NXMatrix *nXMatrix1 = matrixCollection->Create(xform10->Orientation());

            NXOpen::Ellipse *ellipse1;
            ellipse1 = workPart->Curves()->CreateEllipse(centerP, primaryLen / 2, secondaryLen / 2, 0.0, (360.0* DEGRA), 0.0, nXMatrix1);

            curveVec->push_back((NXOpen::Curve*) ellipse1);
        }
        else if (!strcmp(nType, "Rectangle"))
        {
            double eachXSideHalf = primaryLen / 2.0;
            double eachYSideHalf = secondaryLen / 2.0;

            NXOpen::Point3d p1(centerP.X + eachXSideHalf, centerP.Y + eachYSideHalf, 0.0);

            NXOpen::Point3d p2(centerP.X - eachXSideHalf, centerP.Y + eachYSideHalf, 0.0);

            NXOpen::Point3d p3(centerP.X - eachXSideHalf, centerP.Y - eachYSideHalf, 0.0);

            NXOpen::Point3d p4(centerP.X + eachXSideHalf, centerP.Y - eachYSideHalf, 0.0);

            NXOpen::Line *l1;
            l1 = workPart->Curves()->CreateLine(p1, p2);

            NXOpen::Line *l2;
            l2 = workPart->Curves()->CreateLine(p2, p3);

            NXOpen::Line *l3;
            l3 = workPart->Curves()->CreateLine(p3, p4);

            NXOpen::Line *l4;
            l4 = workPart->Curves()->CreateLine(p4, p1);

            curveVec->push_back((NXOpen::Curve*) l1);
            curveVec->push_back((NXOpen::Curve*) l2);
            curveVec->push_back((NXOpen::Curve*) l3);
            curveVec->push_back((NXOpen::Curve*) l4);
        }
        else if (!strcmp(nType, "Hexagon (Flat)"))
        {
            double xHexSide = primaryLen / 2.0;
            double yHexSide = sqrt(3) * primaryLen / 2.0;

            double xHexCorner = primaryLen;
            double yHexCorner = 0;

            NXOpen::Point3d p1(centerP.X + xHexSide, centerP.Y + yHexSide, 0);
            NXOpen::Point3d p2(centerP.X + xHexCorner, centerP.Y, 0);
            NXOpen::Point3d p3(centerP.X + xHexSide, centerP.Y - yHexSide, 0);
            NXOpen::Point3d p4(centerP.X - xHexSide, centerP.Y - yHexSide, 0);
            NXOpen::Point3d p5(centerP.X - xHexCorner, centerP.Y, 0);
            NXOpen::Point3d p6(centerP.X - xHexSide, centerP.Y + yHexSide, 0);

            NXOpen::Line *l1;
            l1 = workPart->Curves()->CreateLine(p1, p2);

            NXOpen::Line *l2;
            l2 = workPart->Curves()->CreateLine(p2, p3);

            NXOpen::Line *l3;
            l3 = workPart->Curves()->CreateLine(p3, p4);

            NXOpen::Line *l4;
            l4 = workPart->Curves()->CreateLine(p4, p5);

            NXOpen::Line *l5;
            l5 = workPart->Curves()->CreateLine(p5, p6);

            NXOpen::Line *l6;
            l6 = workPart->Curves()->CreateLine(p6, p1);

            curveVec->push_back((NXOpen::Curve*) l1);
            curveVec->push_back((NXOpen::Curve*) l2);
            curveVec->push_back((NXOpen::Curve*) l3);
            curveVec->push_back((NXOpen::Curve*) l4);
            curveVec->push_back((NXOpen::Curve*) l5);
            curveVec->push_back((NXOpen::Curve*) l6);
        }
        else if (!strcmp(nType, "Hexagon (Vertex)"))
        {
            double xHexSide = primaryLen / 2.0;
            double yHexSide = sqrt(3) / 2 * primaryLen;

            double xHexCorner = primaryLen;
            double yHexCorner = 0;

            NXOpen::Point3d p1(centerP.X + xHexSide, centerP.Y + yHexSide, 0);
            NXOpen::Point3d p2(centerP.X + xHexCorner, centerP.Y, 0);
            NXOpen::Point3d p3(centerP.X + xHexSide, centerP.Y - yHexSide, 0);
            NXOpen::Point3d p4(centerP.X - xHexSide, centerP.Y - yHexSide, 0);
            NXOpen::Point3d p5(centerP.X - xHexCorner, centerP.Y, 0);
            NXOpen::Point3d p6(centerP.X - xHexSide, centerP.Y + yHexSide, 0);

            NXOpen::Line *l1;
            l1 = workPart->Curves()->CreateLine(p1, p2);

            NXOpen::Line *l2;
            l2 = workPart->Curves()->CreateLine(p2, p3);

            NXOpen::Line *l3;
            l3 = workPart->Curves()->CreateLine(p3, p4);

            NXOpen::Line *l4;
            l4 = workPart->Curves()->CreateLine(p4, p5);

            NXOpen::Line *l5;
            l5 = workPart->Curves()->CreateLine(p5, p6);

            NXOpen::Line *l6;
            l6 = workPart->Curves()->CreateLine(p6, p1);

            curveVec->push_back((NXOpen::Curve*) l1);
            curveVec->push_back((NXOpen::Curve*) l2);
            curveVec->push_back((NXOpen::Curve*) l3);
            curveVec->push_back((NXOpen::Curve*) l4);
            curveVec->push_back((NXOpen::Curve*) l5);
            curveVec->push_back((NXOpen::Curve*) l6);
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



int TelescopeMirrorShapeGeneratorCore::preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event)
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


int TelescopeMirrorShapeGeneratorCore::createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        NXOpen::Features::CustomFeature* customFeature = event->GetCustomFeature();

        NXOpen::Features::CustomFeatureData* cfData = customFeature->FeatureData();

        std::vector<NXOpen::Curve *> apperatureCurves;
        CreateMirrorShapeCurves(customFeature, &apperatureCurves);

        std::vector<NXOpen::TaggedObject*> apperCurves(apperatureCurves.begin(), apperatureCurves.end());

        std::vector < NXOpen::Features::TrackingData*> trackVector;

        // Label Curves to extrude
        for (int i = 0; i < apperCurves.size(); ++i)
        {
            NXOpen::Curve* curve = dynamic_cast<NXOpen::Curve*>(apperCurves[i]);
            NXOpen::Features::TrackingData* track = event->CreateTrackingDataForNXObject(apperCurves[i]);
            track->AddIntSourceEntity(i+1);
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

int TelescopeMirrorShapeGeneratorCore::modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event)
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

int TelescopeMirrorShapeGeneratorCore::postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event)
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

int TelescopeMirrorShapeGeneratorCore::informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event)
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
Session *(TelescopeMirrorShapeGeneratorCore::theSession) = NULL;
UI *(TelescopeMirrorShapeGeneratorCore::theUI) = NULL;

//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
TelescopeMirrorShapeGeneratorCore::TelescopeMirrorShapeGeneratorCore()
{

    // Initialize the NX Open C++ API environment
    TelescopeMirrorShapeGeneratorCore::theSession = NXOpen::Session::GetSession();
    TelescopeMirrorShapeGeneratorCore::theUI = UI::GetUI();
    mb = theUI->NXMessageBox();
    lw = theSession->ListingWindow();

    workPart = theSession->Parts()->Work();
    displayPart = theSession->Parts()->Display();

    NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

    NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::TelescopeMirrorShapeGenerator");

    // Registration of callback functions
    cfClass->AddPreUpdateHandler(make_callback(&TelescopeMirrorShapeGeneratorCore::preUpdateCallBack));
    cfClass->AddCreateFeatureGeometryHandler(make_callback(&TelescopeMirrorShapeGeneratorCore::createGeometryCallBack));
    cfClass->AddModifyFeatureGeometryHandler(make_callback(&TelescopeMirrorShapeGeneratorCore::modifyGeometryCallBack));
    cfClass->AddPostUpdateHandler(make_callback(&TelescopeMirrorShapeGeneratorCore::postUpdateCallBack));

    cfClass->AddInformationHandler(make_callback(&TelescopeMirrorShapeGeneratorCore::informationCallBack));
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
TelescopeMirrorShapeGeneratorCore::~TelescopeMirrorShapeGeneratorCore()
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
        TelescopeMirrorShapeGeneratorCore *theMirrorShapeGeneratorCore;
        theMirrorShapeGeneratorCore = new TelescopeMirrorShapeGeneratorCore();
        delete theMirrorShapeGeneratorCore;
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


