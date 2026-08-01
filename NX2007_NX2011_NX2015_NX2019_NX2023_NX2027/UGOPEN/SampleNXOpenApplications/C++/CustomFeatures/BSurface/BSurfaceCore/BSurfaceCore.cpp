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
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>

//Feature specific includes
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>
#include <NXOpen/Features_CustomFeature.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeatureCreateFeatureGeometryEvent.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>
#include <NXOpen/Features_CustomFeatureInformationEvent.hxx>
#include <NXOpen/Features_CustomIntegerAttribute.hxx>
#include <NXOpen/Features_CustomTagArrayAttribute.hxx>
#include <NXOpen/Features_Feature.hxx>
#include <uf_modl_bsurf.h>
#include <NXOpen/Point.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/Update.hxx>
#include <NXOpen/Features_CustomFeaturePreUpdateEvent.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/Features_ConstructionFeatureData.hxx>
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
// Open C error handling
//------------------------------------------------------------------------------
#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))
int report_error( char *file, int line, char *call, int code)
{
    if (code) 
    {

        stringstream errmsg;
        errmsg << "Error " << code << " in " << file << " at line " << line << endl;
        errmsg << call << endl;
        UI::GetUI()->NXMessageBox()->Show("Open C Error", NXOpen::NXMessageBox::DialogTypeError, errmsg.str().c_str());
        throw NXOpen::NXException::Create(code);
    }
    return(code);
}

//------------------------------------------------------------------------------
// NXOpen c++ test class 
//------------------------------------------------------------------------------
class BSurfaceCore
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;

    BSurfaceCore();
    ~BSurfaceCore();

    static int preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event);
    static int createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event);
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
Session *(BSurfaceCore::theSession) = NULL;
UI *(BSurfaceCore::theUI) = NULL;

//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
BSurfaceCore::BSurfaceCore()
{
    // Initialize the Open C API environment */
    UF_CALL( UF_initialize() );

    // Initialize the NX Open C++ API environment
    BSurfaceCore::theSession = NXOpen::Session::GetSession();
    BSurfaceCore::theUI = UI::GetUI();
    mb = theUI->NXMessageBox();
    lw = theSession->ListingWindow();

    workPart = theSession->Parts()->Work();
    displayPart = theSession->Parts()->Display();

    NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

    NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::BSurface");

    // Registration of callback functions
    cfClass->AddPreUpdateHandler(make_callback(&BSurfaceCore::preUpdateCallBack));
    cfClass->AddCreateFeatureGeometryHandler(make_callback(&BSurfaceCore::createGeometryCallBack));
    cfClass->AddInformationHandler(make_callback(&BSurfaceCore::informationCallBack));
}

int BSurfaceCore::preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event)
{
    std::vector<NXOpen::Features::ConstructionFeatureData *> constructionnFeatureData = event->GetConstructionFeatures();

    constructionnFeatureData.clear();

    NXOpen::Features::CustomFeature *cfFeature = event->GetCustomFeature();

    NXOpen::Features::CustomFeatureData* cfData = cfFeature->FeatureData();

    Features::CustomTagArrayAttribute *polesAttr = cfData->HasCustomAttribute("m_poles", NXOpen::Features::CustomAttribute::TypeTagVla) ? dynamic_cast<Features::CustomTagArrayAttribute*> (cfData->CustomTagArrayAttributeByName("m_poles")):NULL;

    Features::CustomIntegerAttribute *nuAttr = cfData->HasCustomAttribute("m_nu", NXOpen::Features::CustomAttribute::TypeInteger) ? dynamic_cast<Features::CustomIntegerAttribute*> (cfData->CustomIntegerAttributeByName("m_nu")):NULL;
    Features::CustomIntegerAttribute *nvAttr = cfData->HasCustomAttribute("m_nv", NXOpen::Features::CustomAttribute::TypeInteger) ? dynamic_cast<Features::CustomIntegerAttribute*> (cfData->CustomIntegerAttributeByName("m_nv")) : NULL;
    Features::CustomIntegerAttribute *kuAttr = cfData->HasCustomAttribute("m_ku", NXOpen::Features::CustomAttribute::TypeInteger) ? dynamic_cast<Features::CustomIntegerAttribute*> (cfData->CustomIntegerAttributeByName("m_ku")) : NULL;
    Features::CustomIntegerAttribute *kvAttr = cfData->HasCustomAttribute("m_kv", NXOpen::Features::CustomAttribute::TypeInteger) ? dynamic_cast<Features::CustomIntegerAttribute*> (cfData->CustomIntegerAttributeByName("m_kv")) : NULL;

    // If any of the attribute is NULL we cannot proceed
    if (nuAttr == NULL || nvAttr == NULL || kuAttr == NULL || kvAttr == NULL)
    {
        return 1;
    }

    int nu = nuAttr->Value();
    int nv = nvAttr->Value();
    int ku = kuAttr->Value();
    int kv = kvAttr->Value();

    std::vector<NXOpen::TaggedObject*> poleObjects = polesAttr->GetValues();
    std::vector<double> poles;

    NXOpen::Point* sourcePoint = NULL;

    for (int iPole = 0; iPole < poleObjects.size(); ++iPole)
    {
        NXOpen::Point* ithPoint = dynamic_cast<NXOpen::Point*>(poleObjects[iPole]);

        if (ithPoint != NULL)
        {
            Point3d ithPoint3d = ithPoint->Coordinates();

            poles.push_back(ithPoint3d.X);
            poles.push_back(ithPoint3d.Y);
            poles.push_back(ithPoint3d.Z);
            poles.push_back(1.0);
        }

        if (sourcePoint == NULL)
        {
            sourcePoint = ithPoint;
        }
    }

    std::vector<double> uKnots, vKnots;

    int nuKnots = ku + nu;
    double uKnotDifference = 1 / (nuKnots - 2.0*ku + 1.0);

    for (int i = 0; i < nuKnots; ++i)
    {
        double knot = 0.0;
        if (i < ku)
        {
            knot = 0.0;
        }
        else if (nuKnots - i <= ku)
        {
            knot = 1.0;
        }
        else
        {
            knot = uKnotDifference;
            uKnotDifference += uKnotDifference;
        }
        uKnots.push_back(knot);
    }

    int nvKnots = kv + nv;

    double vKnotDifference = 1 / (nvKnots - 2.0*kv + 1.0);

    for (int i = 0; i < nvKnots; ++i)
    {
        double knot = 0.0;
        if (i < kv)
        {
            knot = 0.0;
        }
        else if (nvKnots - i <= kv)
        {
            knot = 1.0;
        }
        else
        {
            knot = vKnotDifference;
            vKnotDifference += vKnotDifference;
        }
        vKnots.push_back(knot);
    }

    tag_t eid = NULL_TAG;
    int knotFixup = 0;
    int poleFixup = 0;
    int error = UF_MODL_create_bsurf(nu, nv, ku, kv, &uKnots[0], &vKnots[0], &poles[0], &eid, &knotFixup, &poleFixup);
    
    std::vector<NXOpen::Features::ConstructionFeatureData*> connFeatDataVector;

    if (error !=0)
    {
        event->SetConstructionFeatures(connFeatDataVector);
        return 0;
    }

    NXOpen::Body* baseBody = dynamic_cast<NXOpen::Body*>(NXOpen::NXObjectManager::Get(eid));

    NXOpen::Session* theSession = NXOpen::Session::GetSession();
    
    Part* workPart = theSession->Parts()->Work();
    NXOpen::Features::Feature *feature = workPart->Features()->GetParentFeatureOfBody(baseBody);

    std::vector<Features::Feature*> connstructionFeature;
    connstructionFeature.push_back(feature);
    
    NXOpen::Features::ConstructionFeatureData* connFeatData = event->CreateConstructionFeatureData(feature);
    connFeatData->SetShowInGraphicView(false);
    //connFeatData->SetShowInPartNavigator(false);

    connFeatDataVector.push_back(connFeatData);

    event->SetConstructionFeatures(connFeatDataVector);
    return 0;
}

int BSurfaceCore::createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event)
{
    NXOpen::Features::CustomFeature *cfFeature = event->GetCustomFeature();

    NXOpen::Features::CustomFeatureData* cfData = cfFeature->FeatureData();

    Features::CustomTagArrayAttribute *polesAttr = cfData->HasCustomAttribute("m_poles", NXOpen::Features::CustomAttribute::TypeTagVla) ? dynamic_cast<Features::CustomTagArrayAttribute*> (cfData->CustomTagArrayAttributeByName("m_poles")):NULL;

    std::vector<NXOpen::TaggedObject*> poleObjects;
    
    if (polesAttr)
    {
        poleObjects = polesAttr->GetValues();
    }

    NXOpen::Point* ithPoint = dynamic_cast<NXOpen::Point*>(poleObjects[0]);

    std::vector<NXOpen::Features::ConstructionFeatureData *> constructionnFeatureData = event->GetConstructionFeatures();

    if (constructionnFeatureData.size() == 0)
    {
        // Write proper error base and return the proper error code. For demostration purpose returning a non zero error.
        event->SetErrorCode(1);
        return 1;
    }

    NXOpen::Features::BodyFeature * bodyFeature = dynamic_cast<NXOpen::Features::BodyFeature*> (constructionnFeatureData[0]->GetFeature());
    std::vector<NXOpen::Body*> outputs = bodyFeature->GetBodies();
    NXOpen::Body* baseBody = outputs[0];
    std::vector<NXOpen::Face*> baseFaces;
    std::vector<NXOpen::Edge*> baseEdges;
    std::vector<NXOpen::Features::CustomFeatureEvent::ParasolidId> copiedFaces, copiedEdges;
    NXOpen::Features::CustomFeatureEvent::ParasolidId copiedBody = (NXOpen::Features::CustomFeatureEvent::ParasolidId)0;
    event->CopyNXBody(baseBody, &copiedBody, baseFaces, copiedFaces, baseEdges, copiedEdges);


    std::vector<NXOpen::Features::TrackingData *> trackingDataVector;

    NXOpen::Features::TrackingData * bodyTrackingObject = event->CreateTrackingDataForParasolidEntity(copiedBody);
    std::vector<NXOpen::NXObject*> sourceVector;
    sourceVector.push_back(ithPoint);
    bodyTrackingObject->AddTagSourceEntities(sourceVector);
    trackingDataVector.push_back(bodyTrackingObject);

    std::vector<NXOpen::Features::CustomFeatureEvent::ParasolidId> copiedBodyVector;
    copiedBodyVector.push_back(copiedBody);
    event->SetBodies(copiedBodyVector);

    for (int iFace = 0; iFace < copiedFaces.size();++iFace)
    {
        NXOpen::Features::TrackingData * trackingObject = event->CreateTrackingDataForParasolidEntity(copiedFaces[iFace]);
        trackingObject->AddIntSourceEntity(iFace);
        trackingDataVector.push_back(trackingObject);
    }

    for (int iEdge = 0; iEdge < copiedEdges.size();++iEdge)
    {
        NXOpen::Features::TrackingData * trackingObject = event->CreateTrackingDataForParasolidEntity(copiedEdges[iEdge]);
        trackingObject->AddIntSourceEntity(iEdge);
        trackingDataVector.push_back(trackingObject);
    }

    event->AppendOutputTrackingData(trackingDataVector);

    return 0;
}

int BSurfaceCore::informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event)
{
    NXString string = "This is custom information \n \t\t Custom feature has not yet implemented custom code to show custom information";
    event->SetInformation(string);
    return 0;
}
//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
BSurfaceCore::~BSurfaceCore()
{
    UF_CALL( UF_terminate() );
}

//------------------------------------------------------------------------------
// Print string to listing window or stdout
//------------------------------------------------------------------------------
void BSurfaceCore::print(const NXString &msg)
{
    if(! lw->IsOpen() ) lw->Open();
    lw->WriteLine(msg);
}
void BSurfaceCore::print(const string &msg)
{
    if(! lw->IsOpen() ) lw->Open();
    lw->WriteLine(msg);
}
void BSurfaceCore::print(const char * msg)
{
    if(! lw->IsOpen() ) lw->Open();
    lw->WriteLine(msg);
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
        BSurfaceCore *theBSurfaceCore;
        theBSurfaceCore = new BSurfaceCore();
        delete theBSurfaceCore;
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


