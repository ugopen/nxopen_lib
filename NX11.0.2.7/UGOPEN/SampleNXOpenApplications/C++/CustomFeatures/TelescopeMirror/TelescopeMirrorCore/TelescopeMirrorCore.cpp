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
#include <NXOpen/DirectionCollection.hxx>
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

// Custom Feature specific Includes
#include <NXOpen/Features_CustomFeature.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>
#include <NXOpen/Features_CustomFeatureBuilder.hxx>
#include <NXOpen/Features_CustomFeatureDataCollection.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomAttributeCollection.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/Features_CustomFeatureInternalFeaturePreUpdateEvent.hxx>
#include <NXOpen/Features_CustomFeaturePreUpdateEvent.hxx>
#include <NXOpen/Features_CustomFeatureCreateFeatureGeometryEvent.hxx>
#include <NXOpen/Features_CustomFeatureModifyFeatureGeometryEvent.hxx>
#include <NXOpen/Features_CustomFeaturePostUpdateEvent.hxx>
#include <NXOpen/Features_CustomFeatureInformationEvent.hxx>
#include <NXOpen/Features_ConstructionFeatureData.hxx>

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
class TelescopeMirrorCore
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;

    TelescopeMirrorCore();
    ~TelescopeMirrorCore();
    
    static int InternalFeaturePreUpdateCallBack(NXOpen::Features::CustomFeatureInternalFeaturePreUpdateEvent* event);

    static void GetConstructionFeatures(NXOpen::Features::CustomFeatureEvent* event, NXOpen::Features::CustomFeature* &mirrorReflectorCurveGenerator, NXOpen::Features::CustomFeature* &mirrorShapeGenerator, NXOpen::Features::Feature* &revolve, NXOpen::Features::Feature* &cylinder, NXOpen::Features::Feature* &subtract, NXOpen::Features::Feature* &extrude, NXOpen::Features::Feature* &intersect);

    static int PreUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event);

    static void CreateConstructionFeaturesIfRequired(NXOpen::Features::CustomFeaturePreUpdateEvent* event);

    static int createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event);
    static int modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event);
    
    static int postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event);
    static int informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event);

    static int CreateUpdateSubstract(NXOpen::Features::Feature* revolve, NXOpen::Features::Feature* cylinder, NXOpen::Features::Feature** subtract);
    static int CreateUpdateExtrude(NXOpen::Features::CustomFeature* customFeature, NXOpen::Features::CustomFeature* mirrorShapeGenerator, NXOpen::Features::Feature ** extrudeFeature);

    static void AddCurvesToSection(std::vector<NXOpen::Curve *> &aperCurve, NXOpen::Part * workPart, NXOpen::Section * section2);

    static int CreateUpdateIntersect(NXOpen::Features::Feature* pedastalObject, NXOpen::Features::Feature* extrudeFeature, NXOpen::Features::Feature** intersectFeature);
    static int CreateUpdateCylinder(NXOpen::Features::CustomFeature* customFeature, NXOpen::Features::Feature** cylinderFeature);
    static int CreateUpdateRevolve(NXOpen::Features::CustomFeature* customFeature, NXOpen::Features::CustomFeature* mirrorReflectorCurveGenerator , NXOpen::Features::Feature** revolveFeature);
    static int CreateMirrorReflectorCurveFeature(NXOpen::Features::CustomFeature* customFeature, NXOpen::Features::CustomFeature** mirrorReflectorCurveGenerator);
    static int CreateMirrorShapeFeature(NXOpen::Features::CustomFeature* customFeature, NXOpen::Features::CustomFeature** mirrorShapeGenerator);

    static void EditSection(NXOpen::Section * section, std::vector<NXOpen::Curve*> inputCurves, NXOpen::Part * workPart);

    void do_it();
    void print(const NXString &);
    void print(const string &);
    void print(const char*);

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

int TelescopeMirrorCore::CreateUpdateSubstract(NXOpen::Features::Feature* revolve, NXOpen::Features::Feature* cylinder, NXOpen::Features::Feature** subtract)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        NXOpen::Part *workPart(theSession->Parts()->Work());
        
        std::vector<NXOpen::Body *> revolveBodies = ((NXOpen::Features::BodyFeature*) revolve)->GetBodies();

        std::vector<NXOpen::Body *> cylinderBodies = ((NXOpen::Features::BodyFeature*) cylinder)->GetBodies();

        if (revolveBodies.size() > 0 && cylinderBodies.size() > 0)
        {
            NXOpen::Features::BooleanBuilder *booleanBuilder1;
            booleanBuilder1 = workPart->Features()->CreateBooleanBuilderUsingCollector((NXOpen::Features::BooleanFeature *)(*subtract));

            if (*subtract == NULL)
            {
                booleanBuilder1->SetTolerance(0.01);

                booleanBuilder1->SetOperation(NXOpen::Features::Feature::BooleanTypeSubtract);

                bool added1 = booleanBuilder1->Targets()->Add(cylinderBodies[0]);

                NXOpen::ScCollector *scCollector2;
                scCollector2 = workPart->ScCollectors()->CreateCollector();

                NXOpen::BodyDumbRule *bodyDumbRule1;
                bodyDumbRule1 = workPart->ScRuleFactory()->CreateRuleBodyDumb(revolveBodies, true);

                std::vector<NXOpen::SelectionIntentRule *> rules1(1);
                rules1[0] = bodyDumbRule1;
                scCollector2->ReplaceRules(rules1, false);

                booleanBuilder1->SetToolBodyCollector(scCollector2);
            }
            if (*subtract == NULL)
            {
                *subtract = (NXOpen::Features::Feature *)booleanBuilder1->Commit();

                (*subtract)->SetName("CustSubtract");
            }
            booleanBuilder1->Destroy();
        }
    }
    catch (NXException& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}

int TelescopeMirrorCore::CreateUpdateExtrude(NXOpen::Features::CustomFeature* customFeature, NXOpen::Features::CustomFeature* mirrorShapeGenerator , NXOpen::Features::Feature ** extrudeFeature)
{
    Session* theSession = Session::GetSession();

    NXOpen::Features::ExtrudeBuilder *extrudeBuilder1 = NULL;

    int error = 0;
    try
    {
        std::vector<NXOpen::Curve *> aperCurve;
        std::vector<NXOpen::NXObject *> entities = mirrorShapeGenerator->GetEntities();

        for (int i = 0; i < entities.size(); ++i)
        {
            aperCurve.push_back(dynamic_cast<NXOpen::Curve *>(entities[i]));
        }

        if (aperCurve.size() < 1)
        {
            return 1;
        }

        NXOpen::Part *workPart(theSession->Parts()->Work());

        extrudeBuilder1 = workPart->Features()->CreateExtrudeBuilder(*extrudeFeature);

        NXOpen::Features::CustomFeatureData* cfData = customFeature->FeatureData();

        NXOpen::Features::CustomTagAttribute* m_locationAttrib = cfData->CustomTagAttributeByName("m_location");
        NXOpen::Point* location = dynamic_cast<NXOpen::Point*>(m_locationAttrib->Value());

        NXOpen::Features::CustomTagAttribute* m_directionAttrib = cfData->CustomTagAttributeByName("m_direction");
        NXOpen::Direction* direction = dynamic_cast<NXOpen::Direction*>(m_directionAttrib->Value());

        NXOpen::Features::CustomExpressionAttribute* m_radiusOfCurvatureAttrib = cfData->CustomExpressionAttributeByName("m_radiusOfCurvature");
        NXOpen::Expression* radiusOfCurvatureExp = dynamic_cast<NXOpen::Expression*>(m_radiusOfCurvatureAttrib->Value());

        NXOpen::Direction* extDirection = extrudeBuilder1->Direction();
        if (extDirection == NULL)
        {
            extrudeBuilder1->SetDirection(direction);
        }
        else if (extDirection != direction)
        {
            NXOpen::Direction* newDirection = workPart->Directions()->CreateDirection(direction->Origin(), direction->Vector(),  NXOpen::SmartObject::UpdateOption::UpdateOptionWithinModeling);
            extDirection->ReplaceParameters(newDirection);
        }
        

        if (*extrudeFeature == NULL)
        {
            extrudeBuilder1->SetDistanceTolerance(0.01);

            extrudeBuilder1->AllowSelfIntersectingSection(true);

            extrudeBuilder1->BooleanOperation()->SetType(NXOpen::GeometricUtilities::BooleanOperation::BooleanTypeCreate);

            char formula1[40];

            strcpy(formula1, radiusOfCurvatureExp->Name().GetText());

            extrudeBuilder1->Limits()->EndExtend()->Value()->SetRightHandSide(formula1);

            strcat(formula1, "* -1");

            extrudeBuilder1->Limits()->StartExtend()->Value()->SetRightHandSide(formula1);

            NXOpen::Section *section2 = extrudeBuilder1->Section();

            section2 = workPart->Sections()->CreateSection(0.0095, 0.01, 0.5);

            extrudeBuilder1->SetSection(section2);

            AddCurvesToSection(aperCurve, workPart, section2);           

            *extrudeFeature = extrudeBuilder1->CommitFeature();
            (*extrudeFeature)->SetName("CustExtrude");
        }
        else
        {

            NXOpen::Section *section2 = extrudeBuilder1->Section();

            EditSection(section2, aperCurve, workPart);
        }
        extrudeBuilder1->Destroy();
    }

    catch (NXException& ex)
    {
        if (extrudeBuilder1 != NULL)
        {
            extrudeBuilder1->Destroy();
        }
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}

int TelescopeMirrorCore::CreateUpdateIntersect(NXOpen::Features::Feature* pedastalObject, NXOpen::Features::Feature* extrudeFeature, NXOpen::Features::Feature** intersectFeature)
{
    Session* theSession = Session::GetSession();

    NXOpen::Features::BooleanBuilder *booleanBuilder1 = NULL;

    int error = 0;
    try
    {
        NXOpen::Part *workPart(theSession->Parts()->Work());

        std::vector<NXOpen::Body *> targetBodies = ((NXOpen::Features::BodyFeature*) extrudeFeature)->GetBodies();

        std::vector<NXOpen::Body *> toolBodies = ((NXOpen::Features::BodyFeature*) pedastalObject)->GetBodies();

        if (targetBodies.size() > 0 && toolBodies.size() > 0)
        {
            

            booleanBuilder1 = workPart->Features()->CreateBooleanBuilderUsingCollector((NXOpen::Features::BooleanFeature *)(*intersectFeature));

            if (*intersectFeature == NULL)
            {
                booleanBuilder1->SetOperation(NXOpen::Features::Feature::BooleanTypeIntersect);

                bool added1 = booleanBuilder1->Targets()->Add(targetBodies);

                NXOpen::ScCollector *scCollector1;
                scCollector1 = booleanBuilder1->ToolBodyCollector();

                NXOpen::BodyDumbRule *bodyDumbRule1;
                bodyDumbRule1 = workPart->ScRuleFactory()->CreateRuleBodyDumb(toolBodies, true);

                NXOpen::ScCollector *scCollector2;
                scCollector2 = workPart->ScCollectors()->CreateCollector();
                std::vector<NXOpen::SelectionIntentRule *> rules2(1);
                rules2[0] = bodyDumbRule1;
                scCollector2->ReplaceRules(rules2, false);

                booleanBuilder1->SetToolBodyCollector(scCollector2);
            }

            if (*intersectFeature == NULL)
            {
                *intersectFeature = (NXOpen::Features::Feature *)booleanBuilder1->Commit();

                (*intersectFeature)->SetName("CustIntersect");
            }
            booleanBuilder1->Destroy();
        }
    }
    catch (NXException& ex)
    {
        if (booleanBuilder1 != NULL)
        {
            booleanBuilder1->Destroy();
        }
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}


int TelescopeMirrorCore::CreateUpdateCylinder(NXOpen::Features::CustomFeature* customFeature, NXOpen::Features::Feature** cylinderFeature)
{
    Session* theSession = Session::GetSession();

    NXOpen::Features::CylinderBuilder *cylinderBuilder1 = NULL;
    int error = 0;
    try
    {
        NXOpen::Features::CustomFeatureData* cfData = customFeature->FeatureData();

        NXOpen::Features::CustomTagAttribute* m_locationAttrib = cfData->CustomTagAttributeByName("m_location");
        NXOpen::Point* location = dynamic_cast<NXOpen::Point*>(m_locationAttrib->Value());

        NXOpen::Features::CustomTagAttribute* m_directionAttrib = cfData->CustomTagAttributeByName("m_direction");
        NXOpen::Direction* direction = dynamic_cast<NXOpen::Direction*>(m_directionAttrib->Value());

        NXOpen::Features::CustomExpressionAttribute* m_thickAtCenterAttrib = cfData->CustomExpressionAttributeByName("m_thickAtCenter");
        NXOpen::Expression* m_thickAtCenterExp = dynamic_cast<NXOpen::Expression*>(m_thickAtCenterAttrib->Value());

        NXOpen::Part *workPart(theSession->Parts()->Work());

        cylinderBuilder1 = workPart->Features()->CreateCylinderBuilder(*cylinderFeature);

        NXOpen::Direction *reversesDir = workPart->Directions()->CreateDirection(direction, SmartObject::UpdateOptionWithinModeling);
        
        NXOpen::Xform* xform = workPart->Xforms()->CreateXformDistanceDirection(reversesDir, m_thickAtCenterExp, SmartObject::UpdateOptionWithinModeling);

        NXOpen::Point *point2;
        point2 = workPart->Points()->CreatePoint(location, xform, SmartObject::UpdateOptionWithinModeling);
        point2->RemoveParameters();
        NXOpen::Axis *axis1 = cylinderBuilder1->Axis();
        axis1->SetDirection(direction);
        axis1->SetPoint(point2);

        if (*cylinderFeature == NULL)
        {
            NXOpen::Features::CustomExpressionAttribute* m_baseDiaAttrib = cfData->CustomExpressionAttributeByName("m_baseDia");
            NXOpen::Expression* cylinderDiaExp = dynamic_cast<NXOpen::Expression*>(m_baseDiaAttrib->Value());

            NXOpen::Features::CustomExpressionAttribute* m_radiusOfCurvatureAttrib = cfData->CustomExpressionAttributeByName("m_radiusOfCurvature");
            NXOpen::Expression* radiusOfCurvatureExp = dynamic_cast<NXOpen::Expression*>(m_radiusOfCurvatureAttrib->Value());

            cylinderBuilder1->BooleanOption()->SetType(NXOpen::GeometricUtilities::BooleanOperation::BooleanTypeCreate);

            cylinderBuilder1->Diameter()->SetRightHandSide(cylinderDiaExp->Name().GetText());

            char formula[40];

            strcpy(formula, radiusOfCurvatureExp->Name().GetText());
            strcat(formula, "*1");

            cylinderBuilder1->Height()->SetRightHandSide(formula);

            *cylinderFeature = (NXOpen::Features::Feature *)cylinderBuilder1->Commit();

            (*cylinderFeature)->SetName("CustCylinder");
        }
        cylinderBuilder1->Destroy();
    }
    catch (NXException& ex)
    {
        if (cylinderBuilder1 != NULL)
        {
            cylinderBuilder1->Destroy(); 
        }

        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }

    return error;
}

static void PopulateMirrorReflectorCurveData(NXOpen::Features::CustomFeatureData* cfData1, NXOpen::Features::CustomFeatureData * cfData2)
{
    NXOpen::Features::CustomTagAttribute* m_locationAttrib1 = cfData1->CustomTagAttributeByName("m_location");
    NXOpen::Features::CustomTagAttribute* m_locationAttrib2 = cfData2->CustomTagAttributeByName("m_location");

    m_locationAttrib2->SetValue(m_locationAttrib1->Value());

    NXOpen::Features::CustomTagAttribute* m_directionAttrib1 = cfData1->CustomTagAttributeByName("m_direction");
    NXOpen::Features::CustomTagAttribute* m_directionAttrib2 = cfData2->CustomTagAttributeByName("m_direction");
    m_directionAttrib2->SetValue(m_directionAttrib1->Value());

    NXOpen::Features::CustomExpressionAttribute* m_radiusOfCurvatureAttrib1 = cfData1->CustomExpressionAttributeByName("m_radiusOfCurvature");
    NXOpen::Features::CustomExpressionAttribute* m_radiusOfCurvatureAttrib2 = cfData2->CustomExpressionAttributeByName("m_radiusOfCurvature");
    m_radiusOfCurvatureAttrib2->SetValue(m_radiusOfCurvatureAttrib1->Value());

    NXOpen::Features::CustomExpressionAttribute* m_conicConstantAttrib1 = cfData1->CustomExpressionAttributeByName("m_conicConstant");
    NXOpen::Features::CustomExpressionAttribute* m_conicConstantAttrib2 = cfData2->CustomExpressionAttributeByName("m_conicConstant");
    m_conicConstantAttrib2->SetValue(m_conicConstantAttrib1->Value());
}

static void CreateMirrorReflectorCurveAattributes(std::vector<NXOpen::Features::CustomAttribute*> &attrs)
{
    Session* theSession = Session::GetSession();
    NXOpen::Part *workPart(theSession->Parts()->Work());

    NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
    NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

    std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
    NXOpen::Features::CustomExpressionAttribute* m_radiusOfCurvatureAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_radiusOfCurvature", attributeProperties));
    attrs.push_back(m_radiusOfCurvatureAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_conicConstantAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_conicConstant", attributeProperties));
    attrs.push_back(m_conicConstantAttrib);

    attributeProperties.push_back(NXOpen::Features::CustomAttribute::Property::PropertyMandatoryInput);
    NXOpen::Features::CustomTagAttribute* m_locationAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_location", attributeProperties));
    attrs.push_back(m_locationAttrib);

    NXOpen::Features::CustomTagAttribute* m_directionAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_direction", attributeProperties));
    attrs.push_back(m_directionAttrib);

    attributeProperties.clear();
}


int TelescopeMirrorCore:: CreateMirrorReflectorCurveFeature(NXOpen::Features::CustomFeature* customFeature, NXOpen::Features::CustomFeature** mirrorReflectorCurveGenerator)
{
    Session* theSession = Session::GetSession();
    NXOpen::Part *workPart(theSession->Parts()->Work());
    NXOpen::Features::CustomFeatureBuilder *mirrorReflectorCurveGeneratorBuilder = NULL;
    int error = 0;
    try
    {
        NXOpen::Features::CustomFeatureData *cfData2 = NULL;

        mirrorReflectorCurveGeneratorBuilder = workPart->Features()->CreateCustomFeatureBuilder(*mirrorReflectorCurveGenerator);

        if (*mirrorReflectorCurveGenerator == NULL)
        { 
            std::vector<NXOpen::Features::CustomAttribute*> attrs(0);

            NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();
            
            NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::TelescopeMirrorReflectorCurveGenerator");

            CreateMirrorReflectorCurveAattributes(attrs);
            // Create custom feature data to store attributes
            cfData2 = workPart->Features()->CustomFeatureDataCollection()->CreateData(cfClass, attrs);
        }
        else
        {
            cfData2 = (*mirrorReflectorCurveGenerator)->FeatureData();
        }
        // populate attributes.

        PopulateMirrorReflectorCurveData(customFeature->FeatureData(), cfData2);

        mirrorReflectorCurveGeneratorBuilder->SetFeatureData(cfData2);

        NXOpen::Features::Feature* frec = mirrorReflectorCurveGeneratorBuilder->CommitFeature();

        *mirrorReflectorCurveGenerator = dynamic_cast<NXOpen::Features::CustomFeature*>(frec);

        (*mirrorReflectorCurveGenerator)->SetName("CustMirrorReflectorCurve");

        mirrorReflectorCurveGeneratorBuilder->Destroy();

        mirrorReflectorCurveGeneratorBuilder = NULL;
    }
    catch (NXException& ex)
    {
        if (mirrorReflectorCurveGeneratorBuilder != NULL)
        {
            mirrorReflectorCurveGeneratorBuilder->Destroy();
        }

        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}

static void CreateMirrorShapeCurveAttributes(std::vector<NXOpen::Features::CustomAttribute*> &attrs)
{
    Session* theSession = Session::GetSession();
    NXOpen::Part *workPart(theSession->Parts()->Work());
    NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
    NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();
    std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
    NXOpen::Features::CustomExpressionAttribute* m_primaryLenAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_primaryLen", attributeProperties));
    attrs.push_back(m_primaryLenAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_secondaryLenAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_secondaryLen", attributeProperties));
    attrs.push_back(m_secondaryLenAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_primaryOffsetAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_primaryOffset", attributeProperties));
    attrs.push_back(m_primaryOffsetAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_secondaryOffsetAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_secondaryOffset", attributeProperties));
    attrs.push_back(m_secondaryOffsetAttrib);

    NXOpen::Features::CustomStringAttribute* m_aperatureShapeAttrib = dynamic_cast<NXOpen::Features::CustomStringAttribute*>(attribCollection->CreateCustomStringAttribute("m_aperatureShape", attributeProperties));
    attrs.push_back(m_aperatureShapeAttrib);

    attributeProperties.push_back(NXOpen::Features::CustomAttribute::Property::PropertyMandatoryInput);
    NXOpen::Features::CustomTagAttribute* m_locationAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_location", attributeProperties));
    attrs.push_back(m_locationAttrib);

    NXOpen::Features::CustomTagAttribute* m_directionAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_direction", attributeProperties));
    attrs.push_back(m_directionAttrib);

    NXOpen::Features::CustomTagAttribute* m_primaryDirAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_primaryDir", attributeProperties));
    attrs.push_back(m_primaryDirAttrib);

    attributeProperties.clear();
}

static void PopulateMirrorShareCurveAttributes(NXOpen::Features::CustomFeatureData* cfData1, NXOpen::Features::CustomFeatureData * cfData2)
{
    NXOpen::Features::CustomExpressionAttribute* m_primaryLenAttrib1 = cfData1->CustomExpressionAttributeByName("m_primaryLen");
    NXOpen::Features::CustomExpressionAttribute* m_primaryLenAttrib2 = cfData2->CustomExpressionAttributeByName("m_primaryLen");
    m_primaryLenAttrib2->SetValue(m_primaryLenAttrib1->Value());

    NXOpen::Features::CustomExpressionAttribute* m_secondaryLenAttrib1 = cfData1->CustomExpressionAttributeByName("m_secondaryLen");
    NXOpen::Features::CustomExpressionAttribute* m_secondaryLenAttrib2 = cfData2->CustomExpressionAttributeByName("m_secondaryLen");
    m_secondaryLenAttrib2->SetValue(m_secondaryLenAttrib1->Value());

    NXOpen::Features::CustomExpressionAttribute* m_primaryOffsetAttrib1 = cfData1->CustomExpressionAttributeByName("m_primaryOffset");
    NXOpen::Features::CustomExpressionAttribute* m_primaryOffsetAttrib2 = cfData2->CustomExpressionAttributeByName("m_primaryOffset");
    m_primaryOffsetAttrib2->SetValue(m_primaryOffsetAttrib1->Value());

    NXOpen::Features::CustomExpressionAttribute* m_secondaryOffsetAttrib1 = cfData1->CustomExpressionAttributeByName("m_secondaryOffset");
    NXOpen::Features::CustomExpressionAttribute* m_secondaryOffsetAttrib2 = cfData2->CustomExpressionAttributeByName("m_secondaryOffset");
    m_secondaryOffsetAttrib2->SetValue(m_secondaryOffsetAttrib1->Value());

    NXOpen::Features::CustomTagAttribute* m_locationAttrib1 = cfData1->CustomTagAttributeByName("m_location");
    NXOpen::Features::CustomTagAttribute* m_locationAttrib2 = cfData2->CustomTagAttributeByName("m_location");
    m_locationAttrib2->SetValue(m_locationAttrib1->Value());

    NXOpen::Features::CustomTagAttribute* m_directionAttrib1 = cfData1->CustomTagAttributeByName("m_direction");
    NXOpen::Features::CustomTagAttribute* m_directionAttrib2 = cfData2->CustomTagAttributeByName("m_direction");
    m_directionAttrib2->SetValue(m_directionAttrib1->Value());

    NXOpen::Features::CustomStringAttribute* m_aperatureShapeAttrib1 = cfData1->CustomStringAttributeByName("m_aperatureShape");
    NXOpen::Features::CustomStringAttribute* m_aperatureShapeAttrib2 = cfData2->CustomStringAttributeByName("m_aperatureShape");
    m_aperatureShapeAttrib2->SetValue(m_aperatureShapeAttrib1->Value());
}


int TelescopeMirrorCore::CreateMirrorShapeFeature(NXOpen::Features::CustomFeature* customFeature, NXOpen::Features::CustomFeature** mirrorShapeGenerator)
{
    Session* theSession = Session::GetSession();
    NXOpen::Part *workPart(theSession->Parts()->Work());
    Features::CustomFeatureBuilder *mirrorShapeCurveGeneratorBuilder = NULL;
    int error = 0;
    try
    {
        NXOpen::Features::CustomFeatureData *cfData2 = NULL;

        mirrorShapeCurveGeneratorBuilder = workPart->Features()->CreateCustomFeatureBuilder(*mirrorShapeGenerator);

        if (*mirrorShapeGenerator == NULL)
        {
            std::vector<NXOpen::Features::CustomAttribute*> attrs(0);

            NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

            NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::TelescopeMirrorShapeGenerator");
            
            CreateMirrorShapeCurveAttributes(attrs);

            // Create custom feature data to store attributes
            cfData2 = workPart->Features()->CustomFeatureDataCollection()->CreateData(cfClass, attrs);
        }
        else
        {
            cfData2 = (*mirrorShapeGenerator)->FeatureData();
        }

        PopulateMirrorShareCurveAttributes(customFeature->FeatureData(), cfData2);

        mirrorShapeCurveGeneratorBuilder->SetFeatureData(cfData2);
        
        NXOpen::Features::Feature* frec = mirrorShapeCurveGeneratorBuilder->CommitFeature();

        *mirrorShapeGenerator = dynamic_cast<NXOpen::Features::CustomFeature*>(frec);

        (*mirrorShapeGenerator)->SetName("CustMirrorShape");

        mirrorShapeCurveGeneratorBuilder->Destroy();

        mirrorShapeCurveGeneratorBuilder = NULL;
    }
    catch (NXException& ex)
    {
        if (mirrorShapeCurveGeneratorBuilder != NULL)
        {
            mirrorShapeCurveGeneratorBuilder->Destroy();
        }
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }

    return error;
}

int TelescopeMirrorCore::CreateUpdateRevolve(NXOpen::Features::CustomFeature* customFeature, NXOpen::Features::CustomFeature* mirrorReflectorCurveGenerator, NXOpen::Features::Feature** revolveFeature)
{
    Session* theSession = Session::GetSession();
    NXOpen::Part *workPart(theSession->Parts()->Work());

    NXOpen::Features::RevolveBuilder *revolveBuilder1 = NULL;

    int error = 0;
    try
    {
        NXOpen::Curve* curveToRevolve;
        std::vector<NXOpen::NXObject*> entities = mirrorReflectorCurveGenerator->GetEntities();
        if (entities.size() == 1)
        {
            curveToRevolve = dynamic_cast<NXOpen::Curve* >(entities[0]);
        }
        else
        {
            return 1;
        }
        NXOpen::Features::CustomFeatureData* cfData = customFeature->FeatureData();

        NXOpen::Features::CustomTagAttribute* m_locationAttrib = cfData->CustomTagAttributeByName("m_location");
        NXOpen::Point* location = dynamic_cast<NXOpen::Point*>(m_locationAttrib->Value());

        NXOpen::Features::CustomTagAttribute* m_directionAttrib = cfData->CustomTagAttributeByName("m_direction");
        NXOpen::Direction* direction = dynamic_cast<NXOpen::Direction*>(m_directionAttrib->Value());

   

        NXOpen::Part *workPart(theSession->Parts()->Work());

        revolveBuilder1 = workPart->Features()->CreateRevolveBuilder(*revolveFeature);  
        
        NXOpen::Axis *axis1 = revolveBuilder1->Axis();

        if(axis1 == NULL)
        {
            axis1 = workPart->Axes()->CreateAxis(location, direction, NXOpen::SmartObject::UpdateOptionWithinModeling);
            revolveBuilder1->SetAxis(axis1);
        }
        else
        {
            axis1->SetPoint(location);
            axis1->SetDirection(direction);
        }

        if (*revolveFeature == NULL)
        {            
            revolveBuilder1->Limits()->StartExtend()->Value()->SetRightHandSide("0");

            revolveBuilder1->Limits()->EndExtend()->Value()->SetRightHandSide("360");

            revolveBuilder1->SetTolerance(0.01);

            NXOpen::Section *sectionToRevolve = revolveBuilder1->Section();

            sectionToRevolve = workPart->Sections()->CreateSection(0.0095, 0.01, 0.5);

            revolveBuilder1->SetSection(sectionToRevolve);

            sectionToRevolve->SetDistanceTolerance(0.01);

            sectionToRevolve->SetChainingTolerance(0.0095);

            sectionToRevolve->SetAllowedEntityTypes(NXOpen::Section::AllowTypesOnlyCurves);

            std::vector<NXOpen::Curve*>curves;
            curves.push_back(curveToRevolve);
            AddCurvesToSection(curves, workPart, sectionToRevolve);

            revolveBuilder1->SetParentFeatureInternal(false);

            *revolveFeature = revolveBuilder1->CommitFeature();

            (*revolveFeature)->SetName("CustRevolve");
        }
        else
        {
            NXOpen::Section *sectionToRevolve = revolveBuilder1->Section();
            std::vector<NXOpen::Curve*>curves;
            curves.push_back(curveToRevolve);
            EditSection(sectionToRevolve, curves, workPart);
        }
        revolveBuilder1->Destroy();
    }
    catch (NXException& ex)
    {
        if (revolveBuilder1 != NULL)
        {
            revolveBuilder1->Destroy();
        }
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}


int TelescopeMirrorCore::InternalFeaturePreUpdateCallBack(NXOpen::Features::CustomFeatureInternalFeaturePreUpdateEvent* event)
{
    Session* theSession = Session::GetSession();
    NXOpen::Part *workPart(theSession->Parts()->Work());

    int error = 0;
    try
    {
        NXOpen::Features::Feature* eventFeature = event->GetFeature();

        NXOpen::Features::CustomFeature* customFeature = event->GetCustomFeature();

        NXOpen::Features::CustomFeature* mirrorReflectorCurveGenerator(NULL);
        NXOpen::Features::CustomFeature* mirrorShapeGenerator(NULL);
        NXOpen::Features::Feature* revolve(NULL);
        NXOpen::Features::Feature* cylinder(NULL);
        NXOpen::Features::Feature* subtract(NULL);
        NXOpen::Features::Feature* extrude(NULL);
        NXOpen::Features::Feature* intersect(NULL);

        GetConstructionFeatures(event, mirrorReflectorCurveGenerator, mirrorShapeGenerator, revolve, cylinder, subtract, extrude, intersect);

        int error = 0;

        if (mirrorReflectorCurveGenerator != NULL && eventFeature == mirrorReflectorCurveGenerator)
        {
            error = CreateMirrorReflectorCurveFeature(customFeature, &mirrorReflectorCurveGenerator);
        }

        if (mirrorShapeGenerator != NULL && eventFeature == mirrorShapeGenerator)
        {
            error = CreateMirrorShapeFeature(customFeature, &mirrorShapeGenerator);
        }

        if (revolve != NULL && mirrorReflectorCurveGenerator != NULL && eventFeature == revolve)
        {
            error = CreateUpdateRevolve(customFeature, mirrorReflectorCurveGenerator, &revolve);
        }

        if (cylinder != NULL && eventFeature == cylinder)
        {
            error = CreateUpdateCylinder(customFeature, &cylinder);
        }

        if (subtract != NULL && eventFeature == subtract && revolve != NULL && cylinder != NULL)
        {
            error = CreateUpdateSubstract(revolve, cylinder, &subtract);
        }

        if (extrude != NULL && eventFeature == extrude && mirrorShapeGenerator != NULL)
        {
            error = CreateUpdateExtrude(customFeature, mirrorShapeGenerator, &extrude);
        }

        if (intersect != NULL && eventFeature == intersect && subtract != NULL && extrude != NULL)
        {
            error = CreateUpdateIntersect(subtract, extrude, &intersect);
        }
    }
    catch (NXException& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}

int TelescopeMirrorCore::PreUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event)
{
    Session* theSession = Session::GetSession();
    NXOpen::Part *workPart(theSession->Parts()->Work());

    int error = 0;
    try
    {
        NXOpen::Features::CustomFeature* customFeature = event->GetCustomFeature();
        
        CreateConstructionFeaturesIfRequired(event);    
    }
    catch (NXException& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}


int TelescopeMirrorCore::createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        NXOpen::Features::CustomFeature* customFeature = event->GetCustomFeature();
        NXOpen::Features::CustomFeature* mirrorReflectorCurveGenerator(NULL);
        NXOpen::Features::CustomFeature* mirrorShapeGenerator(NULL);
        NXOpen::Features::Feature* revolve(NULL);
        NXOpen::Features::Feature* cylinder(NULL);
        NXOpen::Features::Feature* subtract(NULL);
        NXOpen::Features::Feature* extrude(NULL);
        NXOpen::Features::Feature* intersect(NULL);

        GetConstructionFeatures(event, mirrorReflectorCurveGenerator, mirrorShapeGenerator, revolve, cylinder, subtract, extrude, intersect);

        std::vector<NXString> errors;
        if (error == 0)
        {
            if (mirrorReflectorCurveGenerator != NULL)
            {
                errors = mirrorReflectorCurveGenerator->GetFeatureErrorMessages();
            }

            if (errors.size() > 0 || mirrorReflectorCurveGenerator == NULL)
            {
                NXOpen::ListingWindow* lw = theSession->ListingWindow();
                lw->Open();
                lw->WriteLine("Unable to create Telescope Mirror Reflector curve feature");
                error = 1;
                customFeature->LogDiagnostic(1, "Unable to create Telescope Mirror Reflector curve feature", NXOpen::Features::Feature::DiagnosticTypeWarning);
                event->SetErrorCode(error);
            }
        }

        if (error == 0)
        {
            if (mirrorShapeGenerator != NULL)
            {
                errors = mirrorShapeGenerator->GetFeatureErrorMessages();
            }
            if (errors.size() > 0 || mirrorShapeGenerator == NULL)
            {
                NXOpen::ListingWindow* lw = theSession->ListingWindow();
                lw->Open();
                lw->WriteLine("Unable to create Telescope Mirror shape generator feature");
                error = 1;
                customFeature->LogDiagnostic(1, "Unable to create Telescope Mirror shape generator feature", NXOpen::Features::Feature::DiagnosticTypeWarning);
                event->SetErrorCode(error);
            }
        }
        if (error == 0)
        {
            if (revolve != NULL)
            {
                errors = revolve->GetFeatureErrorMessages();
            }
            if (errors.size() > 0 || revolve == NULL)
            {
                NXOpen::ListingWindow* lw = theSession->ListingWindow();
                lw->Open();
                lw->WriteLine("Unable to create revolve");
                error = 1;
                customFeature->LogDiagnostic(1, "Unable to create revolve", NXOpen::Features::Feature::DiagnosticTypeWarning);
                event->SetErrorCode(error);
            }
        }

        if (error == 0)
        {
            if (cylinder != NULL)
            {
                errors = cylinder->GetFeatureErrorMessages();
            }
            if (errors.size() > 0 || cylinder == NULL)
            {
                NXOpen::ListingWindow* lw = theSession->ListingWindow();
                lw->Open();
                lw->WriteLine("Unable to create cylinder");
                error = 1;
                customFeature->LogDiagnostic(1, "Unable to create cylinder", NXOpen::Features::Feature::DiagnosticTypeWarning);
                event->SetErrorCode(error);
            }
        }
        if (error == 0)
        {
            if (subtract != NULL)
            {
                errors = subtract->GetFeatureErrorMessages();
            }
            if (errors.size() > 0 || subtract == NULL)
            {
                NXOpen::ListingWindow* lw = theSession->ListingWindow();
                lw->Open();
                lw->WriteLine("Unable to create subtract feature");
                error = 1;
                customFeature->LogDiagnostic(1, "Unable to create subtract feature", NXOpen::Features::Feature::DiagnosticTypeWarning);
                event->SetErrorCode(error);
            }
        }
        if (error == 0)
        {
            if (extrude != NULL)
            {
                errors = extrude->GetFeatureErrorMessages();
            }
            if (errors.size() > 0 || extrude == NULL)
            {
                NXOpen::ListingWindow* lw = theSession->ListingWindow();
                lw->Open();
                lw->WriteLine("Unable to create extrude");
                error = 1;
                customFeature->LogDiagnostic(1, "Unable to create extrude", NXOpen::Features::Feature::DiagnosticTypeWarning);
                event->SetErrorCode(error);
            }
        }
        if (error == 0)
        {
            if (intersect != NULL)
            {
                errors = intersect->GetFeatureErrorMessages();
            }
            if (errors.size() > 0 || intersect == NULL)
            {
                NXOpen::ListingWindow* lw = theSession->ListingWindow();
                lw->Open();
                lw->WriteLine("Unable to create intersect");
                error = 1;
                customFeature->LogDiagnostic(1, "Unable to create intersect", NXOpen::Features::Feature::DiagnosticTypeWarning);
                event->SetErrorCode(error);
            }
        }
    }
    catch (NXException& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}

int TelescopeMirrorCore::modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        
    }
    catch (NXException& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}

int TelescopeMirrorCore::postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        
    }
    catch (NXException& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}

int TelescopeMirrorCore::informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event)
{
    Session* theSession = Session::GetSession();

    int error = 0;
    try
    {
        NXString string = "This is custom information \n \t\t Custom feature has not yet implemented custom code to show custom information";
        event->SetInformation(string);
    }
    catch (NXException& ex)
    {
        NXOpen::ListingWindow* lw = theSession->ListingWindow();
        lw->Open();
        lw->WriteLine(ex.what());
        lw->Close();
        error = ex.ErrorCode();
    }
    return error;
}
//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(TelescopeMirrorCore::theSession) = NULL;
UI *(TelescopeMirrorCore::theUI) = NULL;

//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
TelescopeMirrorCore::TelescopeMirrorCore()
{

    // Initialize the NX Open C++ API environment
    TelescopeMirrorCore::theSession = NXOpen::Session::GetSession();
    TelescopeMirrorCore::theUI = UI::GetUI();
    mb = theUI->NXMessageBox();
    lw = theSession->ListingWindow();

    workPart = theSession->Parts()->Work();
    displayPart = theSession->Parts()->Display();

    NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

    NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::TelescopeMirror");

    // Registration of callback functions
    cfClass->AddInternalFeaturePreUpdateHandler(make_callback(&TelescopeMirrorCore::InternalFeaturePreUpdateCallBack));
    cfClass->AddPreUpdateHandler(make_callback(&TelescopeMirrorCore::PreUpdateCallBack));
    cfClass->AddCreateFeatureGeometryHandler(make_callback(&TelescopeMirrorCore::createGeometryCallBack));
    cfClass->AddModifyFeatureGeometryHandler(make_callback(&TelescopeMirrorCore::modifyGeometryCallBack));
    cfClass->AddPostUpdateHandler(make_callback(&TelescopeMirrorCore::postUpdateCallBack));

    cfClass->AddInformationHandler(make_callback(&TelescopeMirrorCore::informationCallBack));
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
TelescopeMirrorCore::~TelescopeMirrorCore()
{
}

//------------------------------------------------------------------------------
// Print string to listing window or stdout
//------------------------------------------------------------------------------
void TelescopeMirrorCore::print(const NXString &msg)
{
    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);
}
void TelescopeMirrorCore::print(const string &msg)
{
    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);
}
void TelescopeMirrorCore::print(const char * msg)
{
    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);
}

void TelescopeMirrorCore::AddCurvesToSection(std::vector<NXOpen::Curve *> &inputCurves, NXOpen::Part * workPart, NXOpen::Section * section)
{
    std::vector<NXOpen::IBaseCurve *> curves1;
    for (int i = 0; i < inputCurves.size(); ++i)
    {
        curves1.push_back((NXOpen::IBaseCurve*)inputCurves[i]);
    }
    NXOpen::CurveDumbRule *curveDumbRule1;
    curveDumbRule1 = workPart->ScRuleFactory()->CreateRuleBaseCurveDumb(curves1);

    std::vector<NXOpen::SelectionIntentRule *> rules1(1);
    rules1[0] = curveDumbRule1;
    NXOpen::NXObject *nullNXOpen_NXObject(NULL);
    NXOpen::Point3d helpPoint1(0.0, 0.0, 0.0);
    section->AddToSection(rules1, nullNXOpen_NXObject, nullNXOpen_NXObject, nullNXOpen_NXObject, helpPoint1, NXOpen::Section::ModeCreate, false);
}

void TelescopeMirrorCore::EditSection(NXOpen::Section * section, std::vector<NXOpen::Curve*> inputCurves, NXOpen::Part * workPart)
{
    section->PrepareMappingData();

    section->Clear();

    AddCurvesToSection(inputCurves, workPart, section);

    std::vector<NXOpen::NXObject *> outputs1;
    section->GetOutputCurves(outputs1);

    std::vector<NXOpen::NXObject *> oldoutputs1;
    section->GetOldOutputCurves(oldoutputs1);
    for (int i = 0; i < (int)oldoutputs1.size() && i < (int)outputs1.size(); ++i)
    {
        NXOpen::NXObject* oldOutput = (NXOpen::NXObject*)oldoutputs1[i];
        NXOpen::NXObject* newOutput = (NXOpen::NXObject*)outputs1[i];
        section->MapSectionElements(oldOutput, newOutput);
    }
    section->CleanMappingData();
}

void TelescopeMirrorCore::CreateConstructionFeaturesIfRequired(NXOpen::Features::CustomFeaturePreUpdateEvent* event)
{
    NXOpen::Features::CustomFeature* customFeature = event->GetCustomFeature();

    NXOpen::Features::CustomFeature* mirrorReflectorCurveGenerator(NULL);
    NXOpen::Features::CustomFeature* mirrorShapeGenerator(NULL);
    NXOpen::Features::Feature* revolve(NULL);
    NXOpen::Features::Feature* cylinder(NULL);
    NXOpen::Features::Feature* subtract(NULL);
    NXOpen::Features::Feature* extrude(NULL);
    NXOpen::Features::Feature* intersect(NULL);

    GetConstructionFeatures(event, mirrorReflectorCurveGenerator, mirrorShapeGenerator, revolve, cylinder, subtract, extrude, intersect);


    std::vector<NXOpen::Features::ConstructionFeatureData*>oldConstructionFeatDataVector;
    
    int error = 0;
    if (mirrorReflectorCurveGenerator == NULL)
    {
        error = CreateMirrorReflectorCurveFeature(customFeature, &mirrorReflectorCurveGenerator);
    }
    if (mirrorReflectorCurveGenerator != NULL)
    {
        NXOpen::Features::ConstructionFeatureData* outputFeatData = event->CreateConstructionFeatureData(mirrorReflectorCurveGenerator);
        outputFeatData->SetShowInGraphicView(false);
        oldConstructionFeatDataVector.push_back(outputFeatData);
    }
    else
    {
        customFeature->LogDiagnostic(1, "Unable to create Telescope Mirror Reflector curve feature", NXOpen::Features::Feature::DiagnosticTypeWarning);
        event->SetErrorCode(error);
    }

    if (error == 0 && mirrorShapeGenerator == NULL)
    {
        error = CreateMirrorShapeFeature(customFeature, &mirrorShapeGenerator);
    }
    if (mirrorShapeGenerator != NULL)
    {
        NXOpen::Features::ConstructionFeatureData* outputFeatData = event->CreateConstructionFeatureData(mirrorShapeGenerator);
        outputFeatData->SetShowInGraphicView(false);
        oldConstructionFeatDataVector.push_back(outputFeatData);
    }
    else
    {
        customFeature->LogDiagnostic(1, "Unable to create Telescope Mirror shape generator feature", NXOpen::Features::Feature::DiagnosticTypeWarning);
        event->SetErrorCode(error);
    }

    if (error == 0 && mirrorReflectorCurveGenerator != NULL && revolve == NULL)
    {
        error = CreateUpdateRevolve(customFeature, mirrorReflectorCurveGenerator, &revolve);
    }

    if (revolve != NULL)
    {
        NXOpen::Features::ConstructionFeatureData* outputFeatData = event->CreateConstructionFeatureData(revolve);
        outputFeatData->SetShowInGraphicView(true);
        oldConstructionFeatDataVector.push_back(outputFeatData);
    }
    else
    {
        customFeature->LogDiagnostic(1, "Unable to create revolve", NXOpen::Features::Feature::DiagnosticTypeWarning);
        event->SetErrorCode(error);
    }


    if (error == 0 && cylinder == NULL)
    {
        error = CreateUpdateCylinder(customFeature, &cylinder);
    }
    if (cylinder != NULL)
    {
        NXOpen::Features::ConstructionFeatureData* outputFeatData = event->CreateConstructionFeatureData(cylinder);
        outputFeatData->SetShowInGraphicView(true);
        oldConstructionFeatDataVector.push_back(outputFeatData);
    }
    else
    {
        customFeature->LogDiagnostic(1, "Unable to create cylinder", NXOpen::Features::Feature::DiagnosticTypeWarning);
        event->SetErrorCode(error);
    }

    if (error == 0 && revolve != NULL && cylinder != NULL && subtract == NULL)
    {
        error = CreateUpdateSubstract(revolve, cylinder, &subtract);
    }
    if (subtract != NULL)
    {
        NXOpen::Features::ConstructionFeatureData* outputFeatData = event->CreateConstructionFeatureData(subtract);
        outputFeatData->SetShowInGraphicView(true);
        oldConstructionFeatDataVector.push_back(outputFeatData);
    }
    else
    {
        customFeature->LogDiagnostic(1, "Unable to create subtract feature", NXOpen::Features::Feature::DiagnosticTypeWarning);
        event->SetErrorCode(error);
    }

    if (error == 0 && mirrorShapeGenerator != NULL && extrude == NULL)
    {
        error = CreateUpdateExtrude(customFeature, mirrorShapeGenerator, &extrude);
    }
    if (extrude != NULL)
    {
        NXOpen::Features::ConstructionFeatureData* outputFeatData = event->CreateConstructionFeatureData(extrude);
        outputFeatData->SetShowInGraphicView(true);
        oldConstructionFeatDataVector.push_back(outputFeatData);
    }
    else
    {
        customFeature->LogDiagnostic(1, "Unable to create extrude", NXOpen::Features::Feature::DiagnosticTypeWarning);
        event->SetErrorCode(error);
    }

    if (error == 0 && subtract != NULL && extrude != NULL && intersect == NULL)
    {
        error = CreateUpdateIntersect(subtract, extrude, &intersect);
    }
    if (intersect != NULL)
    {
        NXOpen::Features::ConstructionFeatureData* outputFeatData = event->CreateConstructionFeatureData(intersect);
        outputFeatData->SetShowInGraphicView(true);
        oldConstructionFeatDataVector.push_back(outputFeatData);
    }
    else
    {
        customFeature->LogDiagnostic(1, "Unable to create Intersect feature", NXOpen::Features::Feature::DiagnosticTypeWarning);
        event->SetErrorCode(error);
    }

    event->SetConstructionFeatures(oldConstructionFeatDataVector);
}

void TelescopeMirrorCore::GetConstructionFeatures(NXOpen::Features::CustomFeatureEvent* event, NXOpen::Features::CustomFeature* &mirrorReflectorCurveGenerator, NXOpen::Features::CustomFeature* &mirrorShapeGenerator, NXOpen::Features::Feature* &revolve, NXOpen::Features::Feature* &cylinder, NXOpen::Features::Feature* &subtract, NXOpen::Features::Feature* &extrude, NXOpen::Features::Feature* &intersect)
{
    std::vector<NXOpen::Features::ConstructionFeatureData*>ConstructionFeatDataVector = event->GetConstructionFeatures();

    for (int i = 0; i < (int)ConstructionFeatDataVector.size(); ++i)
    {
        NXOpen::Features::Feature* constructionFeature = ConstructionFeatDataVector[i]->GetFeature();

        const char* featureName = constructionFeature->Name().GetText();

        if (strcmp(featureName, "CustMirrorReflectorCurve") == 0)
        {
            mirrorReflectorCurveGenerator = (NXOpen::Features::CustomFeature*)constructionFeature;
        }
        else if (strcmp(featureName, "CustMirrorShape") == 0)
        {
            mirrorShapeGenerator = (NXOpen::Features::CustomFeature*)constructionFeature;
        }
        else  if (strcmp(featureName, "CustRevolve") == 0)
        {
            revolve = constructionFeature;
        }
        else if (strcmp(featureName, "CustCylinder") == 0)
        {
            cylinder = constructionFeature;
        }
        else if (strcmp(featureName, "CustSubtract") == 0)
        {
            subtract = constructionFeature;
        }
        else if (strcmp(featureName, "CustExtrude") == 0)
        {
            extrude = constructionFeature;
        }
        else if (strcmp(featureName, "CustIntersect") == 0)
        {
            intersect = constructionFeature;
        }
    }
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
        TelescopeMirrorCore *theMirrorGeneratorCore;
        theMirrorGeneratorCore = new TelescopeMirrorCore();
        delete theMirrorGeneratorCore;
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
