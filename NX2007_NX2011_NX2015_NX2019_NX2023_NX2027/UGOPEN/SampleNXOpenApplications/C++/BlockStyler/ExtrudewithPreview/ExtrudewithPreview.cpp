//=============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//
#include "ExtrudewithPreview.hpp"
#include "NXOpen/Body.hxx"
#include "NXOpen/Direction.hxx"
#include "NXOpen/DisplayableObject.hxx"
#include "NXOpen/DisplayModification.hxx"
#include "NXOpen/DisplayManager.hxx"
#include "NXOpen/Expression.hxx"
#include "NXOpen/Facet_FacetedBodyCollection.hxx"
#include "NXOpen/Features_BodyFeature.hxx"
#include "NXOpen/Features_Extrude.hxx"
#include "NXOpen/Features_ExtrudeBuilder.hxx"
#include "NXOpen/Features_Feature.hxx"
#include "NXOpen/Features_FeatureCollection.hxx"
#include "NXOpen/GeometricUtilities_Extend.hxx"
#include "NXOpen/GeometricUtilities_Limits.hxx"
#include "NXOpen/ModelingView.hxx"
#include "NXOpen/ModelingViewCollection.hxx"
#include "NXOpen/Part.hxx"
#include "NXOpen/PartCollection.hxx"
#include "NXOpen/Update.hxx"
#include "NXOpen/View.hxx"
#include "NXOpen/ViewCollection.hxx"
#include "NXOpen/Preferences_SessionVisualizationVisual.hxx"
#include <sstream>
#include <iomanip>
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(ExtrudewithPreview::theSession) = NULL;
UI *(ExtrudewithPreview::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
ExtrudewithPreview *theExtrudewithPreview;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
ExtrudewithPreview::ExtrudewithPreview()
{
    try
    {
        // Initialize the NX Open C++ API environment
        ExtrudewithPreview::theSession = NXOpen::Session::GetSession();
        ExtrudewithPreview::theUI = UI::GetUI();
        theDialogName = "ExtrudewithPreview.dlx";
        theDialog = ExtrudewithPreview::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &ExtrudewithPreview::apply_cb));
        theDialog->AddUpdateHandler(make_callback(this, &ExtrudewithPreview::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &ExtrudewithPreview::initialize_cb));
        theDialog->AddFocusNotifyHandler(make_callback(this, &ExtrudewithPreview::focusNotify_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &ExtrudewithPreview::dialogShown_cb));
    }
    catch(exception& ex)
    {
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
ExtrudewithPreview::~ExtrudewithPreview()
{
    if (theDialog != NULL)
    {
        delete theDialog;
        theDialog = NULL;
    }
}
//------------------------------- DIALOG LAUNCHING ---------------------------------
//
//    Before invoking this application one needs to open any part/empty part in NX
//    because of the behavior of the blocks.
//
//    Make sure the dlx file is in one of the following locations:
//        1.) From where NX session is launched
//        2.) $UGII_USER_DIR/application
//        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
//            recommended. This variable is set to a full directory path to a file 
//            containing a list of root directories for all custom applications.
//            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
//
//    You can create the dialog using one of the following way:
//
//    1. USER EXIT
//
//        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
//        2) Invoke the Shared Library through File->Execute->NX Open menu.
//
//------------------------------------------------------------------------------
extern "C" DllExport void  ufusr(char *param, int *retcod, int param_len)
{
    try
    {
        theExtrudewithPreview = new ExtrudewithPreview();
        // The following method shows the dialog immediately
        theExtrudewithPreview->Show();
    }
    catch(exception& ex)
    {
        ExtrudewithPreview::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    delete theExtrudewithPreview;
}

//------------------------------------------------------------------------------
// This method specifies how a shared image is unloaded from memory
// within NX. This method gives you the capability to unload an
// internal NX Open application or user  exit from NX. Specify any
// one of the three constants as a return value to determine the type
// of unload to perform:
//
//
//    Immediately : unload the library as soon as the automation program has completed
//    Explicitly  : unload the library from the "Unload Shared Image" dialog
//    AtTermination : unload the library when the NX session terminates
//
//
// NOTE:  A program which associates NX Open applications with the menubar
// MUST NOT use this option since it will UNLOAD your NX Open application image
// from the menubar.
//------------------------------------------------------------------------------
extern "C" DllExport int ufusr_ask_unload()
{
    return (int)Session::LibraryUnloadOptionImmediately;
}

//------------------------------------------------------------------------------
// Following method cleanup any housekeeping chores that may be needed.
// This method is automatically called by NX.
//------------------------------------------------------------------------------
extern "C" DllExport void ufusr_cleanup(void)
{
    try
    {
        //Release the memory
    }
    catch(exception& ex)
    {
        ExtrudewithPreview::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int ExtrudewithPreview::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        ExtrudewithPreview::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void ExtrudewithPreview::initialize_cb()
{
    try
    {
        SectionGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("SectionGroup"));
        SectionToExtrude = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("SectionToExtrude"));
        DirectionGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("DirectionGroup"));
        DirectionToExtrude = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("DirectionToExtrude"));
        LimitsGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("LimitsGroup"));
        StartLimit = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("StartLimit"));
        EndLimit = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("EndLimit"));
        PreviewGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("PreviewGroup"));
        PreviewToggle = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("PreviewToggle"));
        ResultButton = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("ResultButton"));

        NXOpen::BlockStyler::PropertyList* Endlimitproplist = EndLimit->GetProperties();
        Endlimitproplist->SetDouble("Value", 36.0);
        delete Endlimitproplist;
        Endlimitproplist = NULL;

        workPart = ExtrudewithPreview::theSession->Parts()->Work();
        displayPart = ExtrudewithPreview::theSession->Parts()->Display();

        feature1 = NULL;
        isFeatureCreated = false;
        preview = true;
        value = true;

        tagObjArray.clear();
        vectCol.clear();

        Translucency1 = ExtrudewithPreview::theUI->VisualizationVisualPreferences()->Translucency();
        ExtrudewithPreview::theUI->VisualizationVisualPreferences()->SetTranslucency(true);

    }
    catch(exception& ex)
    {
        ExtrudewithPreview::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
    
//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void ExtrudewithPreview::dialogShown_cb()
{
    try
    {
        //Do nothing
    }
    catch(exception& ex)
    {
        ExtrudewithPreview::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int ExtrudewithPreview::apply_cb()
{
    int errorCode = 0;
    try
    {
        showOrCreate(0);
    }
    catch(exception& ex)
    {
        errorCode = 1;
        ExtrudewithPreview::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int ExtrudewithPreview::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == SectionToExtrude)
        {
            NXOpen::BlockStyler::PropertyList* SectionToExtrudeproplist = SectionToExtrude->GetProperties();
            tagObjArray = SectionToExtrudeproplist->GetTaggedObjectVector("SelectedObjects");
            delete SectionToExtrudeproplist;
            NXOpen::BlockStyler::PropertyList* PreviewToggleproplist = PreviewToggle->GetProperties();
            preview = PreviewToggleproplist->GetLogical("Value");
            delete PreviewToggleproplist;
            createExtrude();
        }
        else if(block == DirectionToExtrude)
        {
            NXOpen::BlockStyler::PropertyList* DirectionToExtrudeproplist = DirectionToExtrude->GetProperties();
            vectCol = DirectionToExtrudeproplist->GetTaggedObjectVector("SelectedObjects");
            delete DirectionToExtrudeproplist;
            if (vectCol.size() > 0)
            {
                extrudeDirection = dynamic_cast<NXOpen::Direction* >(vectCol[0]);
                directionToSet = extrudeDirection;
            }

            NXOpen::BlockStyler::PropertyList* PreviewToggleproplist = PreviewToggle->GetProperties();
            preview = PreviewToggleproplist->GetLogical("Value");
            delete PreviewToggleproplist;

            createExtrude();
        }
        else if(block == StartLimit)
        {
            NXOpen::BlockStyler::PropertyList* PreviewToggleproplist = PreviewToggle->GetProperties();
            preview = PreviewToggleproplist->GetLogical("Value");
            delete PreviewToggleproplist;

            NXOpen::BlockStyler::PropertyList* StartLimitproplist = StartLimit->GetProperties();
            startValueOfExt = StartLimitproplist->GetDouble("Value");
            delete StartLimitproplist;

            createExtrude();
        }
        else if(block == EndLimit)
        {
            NXOpen::BlockStyler::PropertyList* PreviewToggleproplist = PreviewToggle->GetProperties();
            preview = PreviewToggleproplist->GetLogical("Value");
            delete PreviewToggleproplist;

            NXOpen::BlockStyler::PropertyList* EndLimitproplist = EndLimit->GetProperties();
            endValueOfExt = EndLimitproplist->GetDouble("Value");
            delete EndLimitproplist;

            createExtrude();
        }
        else if(block == PreviewToggle)
        {
            NXOpen::BlockStyler::PropertyList* PreviewToggleproplist = PreviewToggle->GetProperties();
            preview = PreviewToggleproplist->GetLogical("Value");
            delete PreviewToggleproplist;

            createExtrude();
        }
        else if(block == ResultButton)
        {
            createExtrude();

            if (value)
            {
                setBoolean(false);
                NXOpen::BlockStyler::PropertyList* ResultButtonproplist = ResultButton->GetProperties();
                ResultButtonproplist->SetString("Bitmap", "undo");
                ResultButtonproplist->SetString("Label", "Undo result");
                delete ResultButtonproplist;

                showOrCreate(0);
            }
            else 
            {
                setBoolean(true);
                NXOpen::BlockStyler::PropertyList* ResultButtonproplist = ResultButton->GetProperties();
                ResultButtonproplist->SetString("Bitmap", "general_preview");
                ResultButtonproplist->SetString("Label", "Show Result");
                delete ResultButtonproplist;

                if (feature1 != NULL)
                {
                    visibility();
                }
            }
            value = !value;
        }
    }
    catch(exception& ex)
    {
        ExtrudewithPreview::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}
//------------------------------------------------------------------------------
//Callback Name: focusNotify_cb
//This callback is executed when any block (except the ones which receive keyboard entry such as Integer block) receives focus.
//------------------------------------------------------------------------------
void ExtrudewithPreview::focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //do nothing
    }
    catch(exception& ex)
    {
        ExtrudewithPreview::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
void ExtrudewithPreview::createExtrude()
{
    if (tagObjArray.size() > 0 && vectCol.size() > 0) 
    {
        if (isFeatureCreated)
        {
            redefineFeature();
            return;
        }

        NXOpen::Features::Feature* nullFeatures_Feature = NULL;
        NXOpen::Features::ExtrudeBuilder* extrudeBuilder1 = workPart->Features()->CreateExtrudeBuilder(nullFeatures_Feature);
        extrudeBuilder1->SetDistanceTolerance(0.0254);
        extrudeBuilder1->SetDirection(extrudeDirection);

        NXOpen::BlockStyler::PropertyList* StartLimitproplist = StartLimit->GetProperties();
        int starvalueofext = (int)StartLimitproplist->GetDouble("Value");
        delete StartLimitproplist;
        extrudeBuilder1->Limits()->StartExtend()->Value()->SetRightHandSide (intToNXString(starvalueofext));

        NXOpen::BlockStyler::PropertyList* EndLimitproplist = EndLimit->GetProperties();
        int endValueOfExt = (int)EndLimitproplist->GetDouble("Value");
        delete EndLimitproplist;
        extrudeBuilder1->Limits()->EndExtend()->Value()->SetRightHandSide (intToNXString(endValueOfExt));

        extrudeBuilder1->SetSection (dynamic_cast<NXOpen::Section* >(tagObjArray[0]));
        feature1 = extrudeBuilder1->CommitFeature();
        extrudeBuilder1->Destroy();
        workPart->FacetedBodies()->DeleteTemporaryFacesAndEdges();
        isFeatureCreated = true;
        visibility();
    }
}

void ExtrudewithPreview::redefineFeature()
{
    NXOpen::Features::Extrude* extrude1 = dynamic_cast<NXOpen::Features::Extrude* >(feature1);

    NXOpen::Features::ExtrudeBuilder* extrudeBuilder2 = 
        workPart->Features()->CreateExtrudeBuilder(extrude1);

    extrudeBuilder2->SetDistanceTolerance(0.0254);

    extrudeBuilder2->SetDirection(extrudeDirection);

    NXOpen::BlockStyler::PropertyList* StartLimitproplist = StartLimit->GetProperties();
    double starvalueofext = StartLimitproplist->GetDouble("Value");
    delete StartLimitproplist;

    extrudeBuilder2->Limits()->StartExtend()->Value()->SetRightHandSide(doubleToNXString(starvalueofext));

    NXOpen::BlockStyler::PropertyList* EndLimitproplist = EndLimit->GetProperties();
    double endValueOfExt = EndLimitproplist->GetDouble("Value");
    delete EndLimitproplist;

    extrudeBuilder2->Limits()->EndExtend()->Value()->SetRightHandSide(doubleToNXString(endValueOfExt));

    extrudeBuilder2->SetSection(dynamic_cast<NXOpen::Section* >(tagObjArray[0]));

    markId1 = ExtrudewithPreview::theSession->SetUndoMark(NXOpen::Session::MarkVisibilityVisible, "Start Extrude");
    feature1 = extrudeBuilder2->CommitFeature();
    extrudeBuilder2->Destroy();
    workPart->FacetedBodies()->DeleteTemporaryFacesAndEdges();
    ExtrudewithPreview::theSession->UpdateManager()->DoUpdate(markId1);
    ExtrudewithPreview::theSession->DeleteUndoMark(markId1, NULL);
    visibility();
}

void ExtrudewithPreview::visibility()
{
    if (preview)
    {
        NXOpen::Features::BodyFeature* bodyfeat = 
            dynamic_cast<NXOpen::Features::BodyFeature* >(feature1);
        std::vector<NXOpen::Body* > featureBodies = bodyfeat->GetBodies();

        NXOpen::DisplayModification* displayModification1 = 
            ExtrudewithPreview::theSession->DisplayManager()->NewDisplayModification();
        displayModification1->SetApplyToAllFaces(true);
        displayModification1->SetNewTranslucency(80);

        std::vector<NXOpen::DisplayableObject* > objects1(featureBodies.size());
        for (unsigned int ii = 0; ii < featureBodies.size(); ++ii) 
        {
            NXOpen::Body* body = featureBodies[ii];
            objects1[ii] = dynamic_cast<NXOpen::DisplayableObject* > (body);
        }

        displayModification1->Apply(objects1);
        workPart->ModelingViews()->WorkView()->SetRenderingStyle(NXOpen::View::RenderingStyleTypeShadedWithEdges);
    }
    else
    {
        NXOpen::Features::BodyFeature* bodyfeat = 
            dynamic_cast<NXOpen::Features::BodyFeature* >(feature1);
        std::vector<NXOpen::Body* > featureBodies = bodyfeat->GetBodies();

        NXOpen::DisplayModification* displayModification1 = 
            ExtrudewithPreview::theSession->DisplayManager()->NewDisplayModification();
        displayModification1->SetApplyToAllFaces(true);
        displayModification1->SetNewTranslucency(100);

        std::vector<NXOpen::DisplayableObject* > objects1(featureBodies.size());
        for (unsigned int ii = 0; ii < featureBodies.size(); ++ii) 
        {
            objects1[ii] = featureBodies[ii];
        }

        displayModification1->Apply(objects1);
        workPart->ModelingViews()->WorkView()->SetRenderingStyle(NXOpen::View::RenderingStyleTypeShaded);
    }
}

void ExtrudewithPreview::showOrCreate(int transparencyValue)
{
    if (feature1 != NULL)
    {
        NXOpen::Features::BodyFeature* bodyfeat = dynamic_cast<NXOpen::Features::BodyFeature* >(feature1);
        std::vector<NXOpen::Body *> featureBodies = bodyfeat->GetBodies();
        NXOpen::DisplayModification* displayModification1 
            = ExtrudewithPreview::theSession->DisplayManager()->NewDisplayModification();
        displayModification1->SetApplyToAllFaces(true);
        displayModification1->SetNewTranslucency(transparencyValue);
        std::vector<NXOpen::DisplayableObject* > objects1(featureBodies.size());
        for (unsigned int ii = 0; ii < featureBodies.size(); ++ii)
        {
            objects1[ii] = featureBodies[ii];
        }
        displayModification1->Apply(objects1);
        delete displayModification1;
    }
}

void ExtrudewithPreview::setBoolean(bool value)
{
    NXOpen::BlockStyler::PropertyList* SectionToExtrudeproplist = SectionToExtrude->GetProperties();
    SectionToExtrudeproplist->SetLogical("Enable", value);
    delete SectionToExtrudeproplist;
    SectionToExtrudeproplist = NULL;

    NXOpen::BlockStyler::PropertyList* DirectionToExtrudeproplist = DirectionToExtrude->GetProperties();
    DirectionToExtrudeproplist->SetLogical("Enable", value);
    delete DirectionToExtrudeproplist;
    DirectionToExtrudeproplist = NULL;

    NXOpen::BlockStyler::PropertyList* StartLimitproplist = StartLimit->GetProperties();
    StartLimitproplist->SetLogical("Enable", value);
    delete StartLimitproplist;
    StartLimitproplist = NULL;

    NXOpen::BlockStyler::PropertyList* EndLimitproplist = EndLimit->GetProperties();
    EndLimitproplist->SetLogical("Enable", value);
    delete EndLimitproplist;
    EndLimitproplist = NULL;

    NXOpen::BlockStyler::PropertyList* PreviewToggleproplist = PreviewToggle->GetProperties();
    PreviewToggleproplist->SetLogical("Enable", value);
    delete PreviewToggleproplist;
    PreviewToggleproplist = NULL;
}    

NXString ExtrudewithPreview::doubleToNXString(double value)
{
    stringstream tmpValue;
    tmpValue << setprecision(16) << value;
    return NXString(tmpValue.str());
}
NXString ExtrudewithPreview::intToNXString(int value)
{
    stringstream tmpValue;
    tmpValue << setprecision(16) << value;
    return NXString(tmpValue.str());
}
