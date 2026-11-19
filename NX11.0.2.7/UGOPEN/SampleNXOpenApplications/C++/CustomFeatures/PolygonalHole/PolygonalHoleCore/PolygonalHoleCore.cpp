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
#include <NXOpen/Point.hxx>
#include <NXOpen/Direction.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>


#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/UnitCollection.hxx>
#include <NXOpen/Unit.hxx>
#include <NXOpen/ExpressionCollection.hxx>
#include <NXOpen/Expression.hxx>

// Custom Feature specific Includes
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomAttributeCollection.hxx>
#include <NXOpen/Features_CustomTagArrayAttribute.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>
#include <NXOpen/Features_CustomIntegerAttribute.hxx>
#include <NXOpen/Features_CustomLogicalAttribute.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/Features_CustomFeature.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeaturePreUpdateEvent.hxx>
#include <NXOpen/Features_CustomFeatureCreateFeatureGeometryEvent.hxx>
#include <NXOpen/Features_CustomFeatureModifyFeatureGeometryEvent.hxx>
#include <NXOpen/Features_CustomFeaturePostUpdateEvent.hxx>
#include <NXOpen/Features_CustomFeatureInformationEvent.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>

// These are parasolid headers and not available with OOTB NX kits
#include <parasolid_kernel.h>
#include <parasolid_ifails.h>
#include <parasolid_tokens.h>


// Std C++ Includes
#include <set>
#include <iostream>
#include <sstream>

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
class PolygonalHoleCore
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;

    PolygonalHoleCore();
    ~PolygonalHoleCore();
    
    static int preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event);
    static int createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event);
    static int modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event);
    static int postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event);
    static int informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event);
    
    void print(const NXString &);
    void print(const string &);
    void print(const char*);

private:
    Part *workPart, *displayPart;
    NXMessageBox *mb;
    ListingWindow *lw;
};

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(PolygonalHoleCore::theSession) = NULL;
UI *(PolygonalHoleCore::theUI) = NULL;

//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
PolygonalHoleCore::PolygonalHoleCore()
{

    // Initialize the NX Open C++ API environment
    PolygonalHoleCore::theSession = NXOpen::Session::GetSession();
    PolygonalHoleCore::theUI = UI::GetUI();
    mb = theUI->NXMessageBox();
    lw = theSession->ListingWindow();

    workPart = theSession->Parts()->Work();
    displayPart = theSession->Parts()->Display();

    NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();
    
    NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::SamplePolygonalHole");

    // Registration of callback functions
    cfClass->AddPreUpdateHandler(make_callback(&PolygonalHoleCore::preUpdateCallBack));
    cfClass->AddCreateFeatureGeometryHandler(make_callback(&PolygonalHoleCore::createGeometryCallBack));
    cfClass->AddModifyFeatureGeometryHandler(make_callback(&PolygonalHoleCore::modifyGeometryCallBack));
    cfClass->AddPostUpdateHandler(make_callback(&PolygonalHoleCore::postUpdateCallBack));

    cfClass->AddInformationHandler(make_callback(&PolygonalHoleCore::informationCallBack));
    
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
PolygonalHoleCore::~PolygonalHoleCore()
{
}

static NXOpen::Vector3d  GetPerpandicularVector(NXOpen::Vector3d u)
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

    return outVec;
}

//------------------------------------------------------------------------------
// Print string to listing window or stdout
//------------------------------------------------------------------------------
void PolygonalHoleCore::print(const NXString &msg)
{
    if(! lw->IsOpen() ) lw->Open();
    lw->WriteLine(msg);
}
void PolygonalHoleCore::print(const string &msg)
{
    if(! lw->IsOpen() ) lw->Open();
    lw->WriteLine(msg);
}
void PolygonalHoleCore::print(const char * msg)
{
    if(! lw->IsOpen() ) lw->Open();
    lw->WriteLine(msg);
}

// Optional callback registered as sample code, not utilized in current example.
int PolygonalHoleCore::preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event)
{
    return 0;
}

int PolygonalHoleCore::createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event)
{
    // Create attributes
    NXOpen::Part *workPart(theSession->Parts()->Work());

    NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
    NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

    NXOpen::Features::CustomFeature *cfFeature = event->GetCustomFeature();

    NXOpen::Features::CustomFeatureData* cfData = cfFeature->FeatureData();

    Features::CustomExpressionAttribute *polygonDiameterAttrib = cfData->CustomExpressionAttributeByName("m_polygonDiameter");
    NXOpen::Expression* polygoneDiaExp = polygonDiameterAttrib->Value();

    Features::CustomExpressionAttribute *m_polygonSidesAttrib = cfData->CustomExpressionAttributeByName("m_polygonSides");
    NXOpen::Expression* polygoneSides = m_polygonSidesAttrib->Value();
    
    Features::CustomExpressionAttribute *holeDepthAttrib = cfData->CustomExpressionAttributeByName("m_holeDepth");
    NXOpen::Expression* holeDepthExp = holeDepthAttrib->Value();

    Features::CustomTagAttribute *polygonPointAttrib = cfData->CustomTagAttributeByName("m_polygonPoint");
    NXOpen::Point* polygonPoint = dynamic_cast<NXOpen::Point*>(polygonPointAttrib->Value());

    Features::CustomTagAttribute *holeDirectionAttrib = cfData->CustomTagAttributeByName("m_holeDirection");
    NXOpen::Direction* holeDirection = dynamic_cast<NXOpen::Direction*>(holeDirectionAttrib->Value());

    Features::CustomTagAttribute *targetBodyAttrib = cfData->CustomTagAttributeByName("m_targetBody");
    NXOpen::Body* body = dynamic_cast<NXOpen::Body*>(targetBodyAttrib->Value());

    NXOpen::Features::CustomFeatureEvent::ParasolidId bodyId = event->GetParasolidId(body);

    PK_PARTITION_t partition;

    PK_ENTITY_ask_partition(bodyId, &partition);

    PK_AXIS2_sf_s basis_set;

    NXOpen::Point3d origin = polygonPoint->Coordinates();

    PK_VECTOR_t  origPoint = { origin.X * 0.001, origin.Y * 0.001, origin.Z * 0.001 };

    NXOpen::Vector3d direction = holeDirection->Vector();

    PK_VECTOR_t  holeDir = { direction.X, direction.Y, direction.Z };

    NXOpen::Vector3d refVector = GetPerpandicularVector(direction);

    PK_VECTOR_t  holeRefDir = { refVector.X, refVector.Y, refVector.Z };

    basis_set.location = origPoint;
    basis_set.axis = holeDir;
    basis_set.ref_direction = holeRefDir;
    
    PK_BODY_t output1 = 0;

    double radius = polygoneDiaExp->Value()*0.5*0.001;
    double height = holeDepthExp->Value()*0.001;
    int numSides = (int)polygoneSides->Value();

    PK_BODY_create_solid_prism(radius, height, numSides, &basis_set, &output1);

    PK_BODY_change_partition(output1, partition);

    std::vector<NXOpen::Features::CustomFeatureEvent::ParasolidId> bodiesVector;

    bodiesVector.push_back((NXOpen::Features::CustomFeatureEvent::ParasolidId)output1);

    event->SetBodies(bodiesVector);
    
    std::vector<Features::TrackingData*> trackingObjectVector;

    int numFaces = 0;
    PK_FACE_t *faces = NULL;
    PK_BODY_ask_faces(output1, &numFaces, &faces);
    
    int j = 1;
    for (int i = (numFaces - 1); i > -1; i--)
    {
        Features::TrackingData *trackObject = event->CreateTrackingDataForParasolidEntity((NXOpen::Features::CustomFeatureEvent::ParasolidId)faces[i]);
        trackObject->AddIntSourceEntity(j++);
        trackingObjectVector.push_back(trackObject);
    }

    event->AppendOutputTrackingData(trackingObjectVector);
    
    return 0;
}

int PolygonalHoleCore::modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event)
{
    // Create attributes
    NXOpen::Part *workPart(theSession->Parts()->Work());

    NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
    NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

    NXOpen::Features::CustomFeature *cfFeature = event->GetCustomFeature();

    NXOpen::Features::CustomFeatureData* cfData = cfFeature->FeatureData();

    Features::CustomTagAttribute *targetBodyAttrib = cfData->CustomTagAttributeByName("m_targetBody");
    NXOpen::Body* body = dynamic_cast<NXOpen::Body*>(targetBodyAttrib->Value());
    if (body == NULL)
    {
        event->SetErrorCode(690025);
        return 0;
    }
    NXOpen::Features::CustomFeatureEvent::ParasolidId bodyId = event->GetParasolidId(body);
    if (bodyId == PK_ENTITY_null)
    {
        event->SetErrorCode(690025);
        return 0;
    }
    std::vector<NXOpen::Features::CustomFeatureEvent::ParasolidId> bodiesVector = event->GetCreatedBodies();

    int numFaces = 0;
    PK_FACE_t *faces = NULL;
    PK_BODY_ask_faces(bodyId, &numFaces, &faces);

    std::set<PK_FACE_t> oldFaces (faces, faces+numFaces);

    int numResultBodies = 0;
    PK_BODY_t *resultBodies = NULL;

    PK_ERROR_code_t   error = PK_BODY_subtract_bodies(bodyId, (int)bodiesVector.size(), (const PK_BODY_t*)&bodiesVector[0], &numResultBodies, &resultBodies);

    bodiesVector.clear();

    if (numResultBodies == 0)
    {
        event->SetErrorCode(670029);
        return 0;
    }

    if (numResultBodies == 1)
    {
        int numNewFaces = 0;
        PK_FACE_t *newFaces = NULL;
        PK_BODY_ask_faces(bodyId, &numNewFaces, &newFaces);

        std::set<PK_FACE_t> newFacesVec(newFaces, newFaces + numNewFaces);
       
        for (int i = 0; i < numFaces; ++i)
        {
            if (newFacesVec.find(faces[i]) != newFacesVec.end())
            {
                newFacesVec.erase(faces[i]);
            }
        }
        if (error != 0 || newFacesVec.size() == 0)
        {
            event->SetErrorCode(670030);
            return 0;
        }
    }
    if (numResultBodies > 1)
    {
        event->SetErrorCode(670032);
        return 0;
    }

    return 0;
}

// Optional callback registered as sample code, not utilized in current example.
int PolygonalHoleCore::postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event)
{
    return 0;
}

// Optional callback registered as sample code, not utilized in current example.
int PolygonalHoleCore::informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event)
{
    NXString string = "This is custom information \n \t\t Custom feature has not yet implemented custom code to show custom information";
    event->SetInformation(string);
    return 0;
}

//------------------------------------------------------------------------------
// Entry point(s) for unmanaged internal NXOpen C/C++ programs
//------------------------------------------------------------------------------
//  Explicit Execution
extern "C" DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
    try
    {
        // Create NXOpen C++ class instance
        PolygonalHoleCore *thePolygonalHoleCore;
        thePolygonalHoleCore = new PolygonalHoleCore();
        delete thePolygonalHoleCore;
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


