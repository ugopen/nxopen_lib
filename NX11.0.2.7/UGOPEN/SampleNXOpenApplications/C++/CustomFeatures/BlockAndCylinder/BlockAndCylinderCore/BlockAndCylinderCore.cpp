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
#include <NXOpen/Features_CustomFeatureData.hxx>
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>
#include <NXOpen/Features_CustomFeatureInformationEvent.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/NXObjectManager.hxx>

#include <NXOpen/Features_CustomFeatureCreateFeatureGeometryEvent.hxx>
#include <NXOpen/Features_CustomFeature.hxx>

// These are parasolid headers and not available with OOTB NX kits
#include <parasolid_kernel.h>
#include <parasolid_ifails.h>
#include <parasolid_tokens.h>

// Std C++ Includes
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
class BlockAndCylinderCore
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;

    BlockAndCylinderCore();
    ~BlockAndCylinderCore();

    static int createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event);
    
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

int BlockAndCylinderCore::createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event)
{
    NXOpen::Features::CustomFeature *cfFeature = event->GetCustomFeature();

    NXOpen::Features::CustomFeatureData* cfData = cfFeature->FeatureData();

    Features::CustomTagAttribute *blockOriginAttrib = cfData->CustomTagAttributeByName("blockOriginPoint");
    Features::CustomExpressionAttribute *blockXCAttrib = cfData->CustomExpressionAttributeByName("blockXC");
    Features::CustomExpressionAttribute *blockYCAttrib = cfData->CustomExpressionAttributeByName("blockYC");
    Features::CustomExpressionAttribute *blockZCAttrib = cfData->CustomExpressionAttributeByName("blockZC");
    Features::CustomTagAttribute *cylOriginAttrib = cfData->CustomTagAttributeByName("cylOriginPoint");
    Features::CustomExpressionAttribute *cylRadiusAttrib = cfData->CustomExpressionAttributeByName("cylRadius");
    Features::CustomExpressionAttribute *cylHeightAttrib = cfData->CustomExpressionAttributeByName("cylHeight");
    Features::CustomTagAttribute *cylDirVectorAttrib = cfData->CustomTagAttributeByName("cylDirVector");

    NXOpen::Point* blockOriginPoint = dynamic_cast<NXOpen::Point*>(blockOriginAttrib->Value());

    NXOpen::Expression* blockXC = blockXCAttrib->Value();
    NXOpen::Expression* blockYC = blockYCAttrib->Value();
    NXOpen::Expression* blockZC = blockZCAttrib->Value();

    NXOpen::Point* cylOriginPoint = dynamic_cast<NXOpen::Point*>(cylOriginAttrib->Value());

    NXOpen::Expression* cylRadius = cylRadiusAttrib->Value();
    NXOpen::Expression* cylHeight = cylHeightAttrib->Value();

    NXOpen::Direction* cylDirVector = dynamic_cast<NXOpen::Direction*>(cylDirVectorAttrib->Value());

    PK_AXIS2_sf_s basis_set;

    NXOpen::Point3d blockOrigin = blockOriginPoint->Coordinates();

    PK_VECTOR_t  origPoint = { blockOrigin.X * 0.001, blockOrigin.Y * 0.001, blockOrigin.Z * 0.001 };

    PK_VECTOR_t  zDir = { 0.0, 0.0, 1.0 };

    PK_VECTOR_t  refDir = { 1.0, 0.0, 0.0 };

    basis_set.location = origPoint;
    basis_set.axis = zDir;
    basis_set.ref_direction = refDir;

    double Xc = blockXC->Value()*0.001;
    double Yc = blockYC->Value()*0.001;
    double Zc = blockZC->Value()*0.001;

    PK_BODY_t output1 = PK_ENTITY_null;
    PK_BODY_t output2 = PK_ENTITY_null;

    std::vector<Features::TrackingData*> trackingObjectVector;
    std::vector<NXOpen::Features::CustomFeatureEvent::ParasolidId> bodiesVector;

    if (Xc <= 0.0 || Yc <= 0.0 || Zc <= 0.0)
    {
        cfFeature->LogDiagnostic(1, "Block construction parameters must be non zero", NXOpen::Features::Feature::DiagnosticTypeWarning);
    }
    else
    {
        PK_BODY_create_solid_block(Xc, Yc, Zc, &basis_set, &output1);

        bodiesVector.push_back((NXOpen::Features::CustomFeatureEvent::ParasolidId)output1);

        Features::TrackingData *trackObject1 = event->CreateTrackingDataForParasolidEntity((NXOpen::Features::CustomFeatureEvent::ParasolidId)output1);

        std::vector<NXOpen::NXObject *> objVector1;
        objVector1.push_back(dynamic_cast<NXOpen::NXObject *>(blockOriginAttrib->Value()));
        trackObject1->AddTagSourceEntities(objVector1);
        trackingObjectVector.push_back(trackObject1);

        int numFaces = 0;
        PK_FACE_t *faces = NULL;

        PK_BODY_ask_faces(output1, &numFaces, &faces);

        for (int i = 0; i < numFaces; i++)
        {
            Features::TrackingData *trackObject = event->CreateTrackingDataForParasolidEntity((NXOpen::Features::CustomFeatureEvent::ParasolidId)faces[i]);
            trackObject->AddIntSourceEntity(i + 1);
            trackingObjectVector.push_back(trackObject);
        }

    }

    PK_AXIS2_sf_s cyl_basis_set;

    NXOpen::Point3d cylOrigin = cylOriginPoint->Coordinates();

    PK_VECTOR_t  cylOrigPoint = { cylOrigin.X * 0.001, cylOrigin.Y * 0.001, cylOrigin.Z * 0.001 };

    NXOpen::Vector3d direction = cylDirVector->Vector();

    PK_VECTOR_t  cylDir = { direction.X, direction.Y, direction.Z };

    NXOpen::Vector3d refVector = GetPerpandicularVector(direction);

    PK_VECTOR_t  cylRefDir = { refVector.X, refVector.Y, refVector.Z };

    cyl_basis_set.location = cylOrigPoint;
    cyl_basis_set.axis = cylDir;
    cyl_basis_set.ref_direction = cylRefDir;

    double cyl_Rad = cylRadius->Value()*0.001;
    double cyl_Height = cylHeight->Value()*0.001;
    if (cyl_Rad <= 0.0 || cyl_Height <= 0.0 )
    {
        cfFeature->LogDiagnostic(1, "Cylinder construction parameters must be non zero", NXOpen::Features::Feature::DiagnosticTypeWarning);
    }
    else
    {
        PK_BODY_create_solid_cyl(cyl_Rad, cyl_Height, &cyl_basis_set, &output2);

        bodiesVector.push_back((NXOpen::Features::CustomFeatureEvent::ParasolidId)output2);

        Features::TrackingData *trackObject2 = event->CreateTrackingDataForParasolidEntity((NXOpen::Features::CustomFeatureEvent::ParasolidId)output2);

        std::vector<NXOpen::NXObject *> objVector2;
        objVector2.push_back(dynamic_cast<NXOpen::NXObject *>(cylOriginAttrib->Value()));
        trackObject2->AddTagSourceEntities(objVector2);
        trackingObjectVector.push_back(trackObject2);
        
        int numFaces = 0;
        PK_FACE_t *faces = NULL;

        PK_BODY_ask_faces(output2, &numFaces, &faces);

        for (int i = 0; i < numFaces; ++i)
        {
            Features::TrackingData *trackObject = event->CreateTrackingDataForParasolidEntity((NXOpen::Features::CustomFeatureEvent::ParasolidId)faces[i]);
            trackObject->AddIntSourceEntity(i + 7);   // 7 because there will be 6 faces of block.
            trackingObjectVector.push_back(trackObject);
        }
    }
    if (bodiesVector.size() > 0)
    {
        event->SetBodies(bodiesVector);
        event->AppendOutputTrackingData(trackingObjectVector);
    }
    else
    {
        event->SetErrorCode(1);
    }

    return 0;
}


//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(BlockAndCylinderCore::theSession) = NULL;
UI *(BlockAndCylinderCore::theUI) = NULL;

//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
BlockAndCylinderCore::BlockAndCylinderCore()
{

    // Initialize the NX Open C++ API environment
    BlockAndCylinderCore::theSession = NXOpen::Session::GetSession();
    BlockAndCylinderCore::theUI = UI::GetUI();
    mb = theUI->NXMessageBox();
    lw = theSession->ListingWindow();

    workPart = theSession->Parts()->Work();
    displayPart = theSession->Parts()->Display();

    NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

    NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::BlockAndCylinder");

    cfClass->AddCreateFeatureGeometryHandler(make_callback(&BlockAndCylinderCore::createGeometryCallBack));
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
BlockAndCylinderCore::~BlockAndCylinderCore()
{
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
        BlockAndCylinderCore *theBlockAndCylinderCore;
        theBlockAndCylinderCore = new BlockAndCylinderCore();
        delete theBlockAndCylinderCore;
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


