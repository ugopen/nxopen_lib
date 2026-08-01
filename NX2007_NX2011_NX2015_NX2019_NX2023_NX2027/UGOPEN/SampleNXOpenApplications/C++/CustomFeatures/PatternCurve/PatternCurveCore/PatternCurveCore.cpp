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
#include <NXOpen/CurveCollection.hxx>
#include <NXOpen/Direction.hxx>
#include <NXOpen/ExpressionCollection.hxx>
#include <NXOpen/Face.hxx>

// Custom Feature specific Includes
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>
#include <NXOpen/Features_CustomFeature.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeatureCreateFeatureGeometryEvent.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>
#include <NXOpen/Features_CustomFeatureInformationEvent.hxx>
#include <NXOpen/Features_CustomIntegerAttribute.hxx>
#include <NXOpen/Features_CustomLogicalAttribute.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/Line.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/Xform.hxx>
#include <NXOpen/XformCollection.hxx>


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
class PatternCurveCore
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;

    PatternCurveCore();
    ~PatternCurveCore();
    
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

    static NXOpen::Curve* PatternCurveCore::ExtractCurve(NXOpen::Curve* curve, NXOpen::Direction* d1, NXOpen::Expression* d1Pitch);
};

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(PatternCurveCore::theSession) = NULL;
UI *(PatternCurveCore::theUI) = NULL;

//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
PatternCurveCore::PatternCurveCore()
{
    // Initialize the NX Open C++ API environment
    PatternCurveCore::theSession = NXOpen::Session::GetSession();
    PatternCurveCore::theUI = UI::GetUI();
    mb = theUI->NXMessageBox();
    lw = theSession->ListingWindow();

    workPart = theSession->Parts()->Work();
    displayPart = theSession->Parts()->Display();

    NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

    NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::SamplePatternCurve");

    // Registration of callback functions
    cfClass->AddPreUpdateHandler(make_callback(&PatternCurveCore::preUpdateCallBack));
    cfClass->AddCreateFeatureGeometryHandler(make_callback(&PatternCurveCore::createGeometryCallBack));
    cfClass->AddModifyFeatureGeometryHandler(make_callback(&PatternCurveCore::modifyGeometryCallBack));
    cfClass->AddPostUpdateHandler(make_callback(&PatternCurveCore::postUpdateCallBack));

    cfClass->AddInformationHandler(make_callback(&PatternCurveCore::informationCallBack));
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
PatternCurveCore::~PatternCurveCore()
{
}

//------------------------------------------------------------------------------
// Print string to listing window or stdout
//------------------------------------------------------------------------------
void PatternCurveCore::print(const NXString &msg)
{
    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);
}
void PatternCurveCore::print(const string &msg)
{
    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);
}
void PatternCurveCore::print(const char * msg)
{
    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);
}

NXOpen::Curve* PatternCurveCore::ExtractCurve(NXOpen::Curve* curve, NXOpen::Direction* direction, NXOpen::Expression* dPitch)
{
    Part* workPart = theSession->Parts()->Work();
    NXOpen::XformCollection *xfmCollection = workPart->Xforms();
    NXOpen::CurveCollection *crvCollection = workPart->Curves();

    NXOpen::SmartObject::VisibilityOption restoreVisibility = curve->Visibility();

    curve->SetVisibility(NXOpen::SmartObject::VisibilityOption::VisibilityOptionVisible);

    NXOpen::Xform* xform = xfmCollection->CreateXformDistanceDirection(direction, dPitch, SmartObject::UpdateOptionWithinModeling);
    xform->RemoveParameters();

    NXOpen::ICurve* extractCurve = crvCollection->CreateExtractedCurve(curve, 0, 0, xform, 0.01, SmartObject::UpdateOptionWithinModeling);

    NXOpen::Curve* extractedCrv = dynamic_cast<NXOpen::Curve*>(extractCurve);

    extractedCrv->SetVisibility(NXOpen::SmartObject::VisibilityOption::VisibilityOptionVisible);

    extractedCrv->RedisplayObject();

    extractedCrv->RemoveParameters();    

    curve->SetVisibility(restoreVisibility);
    
    return extractedCrv;
}

// Optional callback registered as sample code, not utilized in current example.
int PatternCurveCore::preUpdateCallBack(NXOpen::Features::CustomFeaturePreUpdateEvent* event)
{
    return 0;
}

int PatternCurveCore::createGeometryCallBack(NXOpen::Features::CustomFeatureCreateFeatureGeometryEvent* event)
{
    NXOpen::Features::CustomFeature *cfFeature = event->GetCustomFeature();

    NXOpen::Features::CustomFeatureData* cfData = cfFeature->FeatureData();

    Features::CustomTagAttribute *sectionAttrib = cfData->HasCustomAttribute("section", NXOpen::Features::CustomAttribute::TypeTag) ? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("section")) : NULL;

    Features::CustomTagAttribute *d1Attrib = cfData->HasCustomAttribute("d1", NXOpen::Features::CustomAttribute::TypeTag) ? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("d1")) : NULL;

    Features::CustomExpressionAttribute* d1CountAttrib = cfData->HasCustomAttribute("d1Count", NXOpen::Features::CustomAttribute::TypeExpression) ? dynamic_cast<Features::CustomExpressionAttribute*> (cfData->CustomExpressionAttributeByName("d1Count")) : NULL;

    Features::CustomExpressionAttribute *d1PtichAttrib = cfData->HasCustomAttribute("d1Pitch", NXOpen::Features::CustomAttribute::TypeExpression) ? dynamic_cast<Features::CustomExpressionAttribute*> (cfData->CustomExpressionAttributeByName("d1Pitch")) : NULL;

    Features::CustomLogicalAttribute *useD2Attrib = cfData->HasCustomAttribute("useD2", NXOpen::Features::CustomAttribute::TypeBool) ? dynamic_cast<Features::CustomLogicalAttribute*> (cfData->CustomLogicalAttributeByName("useD2")) : NULL;

    Features::CustomTagAttribute *d2Attrib = cfData->HasCustomAttribute("d2", NXOpen::Features::CustomAttribute::TypeTag) ? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("d2")) : NULL;

    Features::CustomExpressionAttribute* d2CountAttrib = cfData->HasCustomAttribute("d2Count", NXOpen::Features::CustomAttribute::TypeExpression) ? dynamic_cast<Features::CustomExpressionAttribute*> (cfData->CustomExpressionAttributeByName("d2Count")) : NULL;

    Features::CustomExpressionAttribute *d2PtichAttrib = cfData->HasCustomAttribute("d2Pitch", NXOpen::Features::CustomAttribute::TypeExpression) ? dynamic_cast<Features::CustomExpressionAttribute*> (cfData->CustomExpressionAttributeByName("d2Pitch")) : NULL;
        
    NXOpen::Section* section = dynamic_cast<NXOpen::Section*>(sectionAttrib->Value());
    NXOpen::Direction* d1 = dynamic_cast<NXOpen::Direction*>(d1Attrib->Value());
    NXOpen::Expression* d1Count = d1CountAttrib->Value();
    NXOpen::Expression* d1Pitch = d1PtichAttrib->Value();

    bool useD2Value = useD2Attrib->Value();

    std::vector<NXOpen::NXObject *> objects;

    try
    {
        section->EvaluateAndAskOutputEntities(objects);
    }
    catch (NXOpen::NXException error)
    {
        event->SetErrorCode(error.ErrorCode());
    }
    
    std::vector<NXOpen::Curve*> curves;
    std::vector<NXOpen::Point*> points;
    for (int i = 0; i < objects.size(); ++i)
    {
        NXOpen::Curve* crv = dynamic_cast<NXOpen::Curve*>(objects[i]);
        if (crv != NULL)
        {
            curves.push_back(crv);
        }
    }
    Part* workPart = theSession->Parts()->Work();

    std::vector<Features::TrackingData *> trackingObjectVector; 

    NXOpen::ExpressionCollection *expCollection = workPart->Expressions();  
    NXOpen::CurveCollection *crvCollection = workPart->Curves();    

    double d1PitchValue = d1Pitch->Value();
    double d1countValue = d1Count->Value();

    std::vector<NXOpen::Curve *> d1InstanceCurves;

    for (int i = 0; i < curves.size(); ++i)
    {
        NXOpen::Curve* curve = curves[i];

        d1InstanceCurves.push_back(curve);

        std::vector<NXOpen::NXObject *> sourceVec;
        sourceVec.push_back(dynamic_cast<NXOpen::NXObject*>(curve));
        int d2Index = 1;
        for (int d1Index = 1; d1Index < d1countValue; ++d1Index)
        {
            d1Pitch->SetValue(d1Index*d1PitchValue);
            
            NXOpen::Curve* extractedCrv = PatternCurveCore::ExtractCurve(curve, d1, d1Pitch);

            d1InstanceCurves.push_back(extractedCrv);

            Features::TrackingData *trackObject1 = event->CreateTrackingDataForNXObject(extractedCrv);
            
            trackObject1->AddTagSourceEntities(sourceVec);
            trackObject1->SetIntApplicationKey(d1Index+1);
            trackObject1->AddIntSourceEntity(d2Index);           

            trackingObjectVector.push_back(trackObject1);
        }
    }

    if (useD2Value && d2CountAttrib && d2PtichAttrib && d2Attrib)
    {
        NXOpen::Direction* d2 = dynamic_cast<NXOpen::Direction*>(d2Attrib->Value());
        
        if (d2->Update() == SmartObject::UpdateOption::UpdateOptionDontUpdate)
        {
            cfFeature->LogDiagnostic(1, "Direction 2 to pattern is not associative", NXOpen::Features::Feature::DiagnosticType::DiagnosticTypeWarning);
        }
        NXOpen::Expression* d2Count = d2CountAttrib->Value();
        NXOpen::Expression* d2Pitch = d2PtichAttrib->Value();
        
        double d2PitchValue = d2Pitch->Value();
        double d2countValue = d2Count->Value();

        for (int d2Index = 1; d2Index < d2countValue; ++d2Index)
        {
            // increase pitch to value in multiple of index of pattern
            d2Pitch->SetValue(d2Index*d2PitchValue);

            NXOpen::Curve* sourceCurve = NULL;

            int d1Index = 0; 
            for (int ithD1Instance = 0; ithD1Instance < d1InstanceCurves.size(); ++ithD1Instance)
            {
                NXOpen::Curve* curve = d1InstanceCurves[ithD1Instance];
                d1Index++;
                if (d1Index > d1countValue)
                {
                    d1Index = 1;
                }

                if ((ithD1Instance % (int)d1countValue) == 0)
                {
                    sourceCurve = curve;
                }

                NXOpen::Curve* extractedCrv = PatternCurveCore::ExtractCurve(curve, d2, d2Pitch);

                Features::TrackingData *trackObject1 = event->CreateTrackingDataForNXObject(extractedCrv);
                
                std::vector<NXOpen::NXObject *> sourceVec;
                sourceVec.push_back(dynamic_cast<NXOpen::NXObject*>(sourceCurve));
                trackObject1->AddTagSourceEntities(sourceVec);
                trackObject1->SetIntApplicationKey(d1Index);
                trackObject1->AddIntSourceEntity(d2Index + 1);

                trackingObjectVector.push_back(trackObject1);
            }
        }
        d2Pitch->SetValue(d2PitchValue); // Set value to original input
    }
    d1Pitch->SetValue(d1PitchValue); // Set value to original input

    event->AppendOutputTrackingData(trackingObjectVector);

    return 0;
}

// Optional callback registered as sample code, not utilized in current example.
int PatternCurveCore::modifyGeometryCallBack(NXOpen::Features::CustomFeatureModifyFeatureGeometryEvent* event)
{
    return 0;
}

// Optional callback registered as sample code, not utilized in current example.
int PatternCurveCore::postUpdateCallBack(NXOpen::Features::CustomFeaturePostUpdateEvent* event)
{
    return 0;
}

// Optional callback registered as sample code, not utilized in current example.
int PatternCurveCore::informationCallBack(NXOpen::Features::CustomFeatureInformationEvent* event)
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
        PatternCurveCore *thePatternCurveCore;
        thePatternCurveCore = new PatternCurveCore();
        delete thePatternCurveCore;
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
