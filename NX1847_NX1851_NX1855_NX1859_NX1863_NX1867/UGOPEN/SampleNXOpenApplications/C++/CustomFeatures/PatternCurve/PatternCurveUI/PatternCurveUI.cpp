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
//  construction of your Block application dialog. The generation of your
//  dialog file (.dlx extension) is the first step towards dialog construction
//  within NX.  You must now create a NX Open application that
//  utilizes this file (.dlx).
//
//  The information in this file provides you with the following:
//
//  1.  Help on how to load and display your Block UI Styler dialog in NX
//      using APIs provided in NXOpen.BlockStyler namespace
//  2.  The empty callback methods (stubs) associated with your dialog items
//      have also been placed in this file. These empty methods have been
//      created simply to start you along with your coding requirements.
//      The method name, argument list and possible return values have already
//      been provided for you.
//==============================================================================

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include "PatternCurveUI.hpp"
#include <NXOpen/Features_CustomFeatureBuilder.hxx>

#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/Features_Feature.hxx>

#include <NXOpen/Features_CustomFeatureDataCollection.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>

#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>

#include <NXOpen/Features_CustomAttributeCollection.hxx>
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/Features_CustomLogicalAttribute.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>
#include <NXOpen/Features_CustomFeature.hxx>
#include <NXOpen/Direction.hxx>

#include <NXOpen/UnitCollection.hxx>
#include <NXOpen/Unit.hxx>
#include <NXOpen/ExpressionCollection.hxx>
#include <NXOpen/Expression.hxx>

#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/SectionCollection.hxx>


using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(PatternCurveUI::theSession) = NULL;
UI *(PatternCurveUI::theUI) = NULL;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
PatternCurveUI::PatternCurveUI()
{
    try
    {
        // Initialize the NX Open C++ API environment
        PatternCurveUI::theSession = NXOpen::Session::GetSession();
        PatternCurveUI::theUI = UI::GetUI();
        theDlxFileName = "PatternCurveUI.dlx";
        theDialog = PatternCurveUI::theUI->CreateDialog(theDlxFileName);
        
        // Get custom feature manager from session.
        mgr = theSession->CustomFeatureClassManager();
        cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::SamplePatternCurve");

        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &PatternCurveUI::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &PatternCurveUI::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &PatternCurveUI::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &PatternCurveUI::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &PatternCurveUI::dialogShown_cb));
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
PatternCurveUI::~PatternCurveUI()
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
//            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_ROOT_DIR\menus\custom_dirs.dat
//
//    You can create the dialog using one of the following way:
//
//    1. USER EXIT
//
//        1) Remove the following conditional definitions:
//                a) #if USER_EXIT_OR_MENU
//                    #endif//USER_EXIT_OR_MENU
//
//                b) #if USER_EXIT
//                    #endif//USER_EXIT
//        2) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
//        3) Invoke the Shared Library through File->Execute->NX Open menu.
//
//    2. MENU BAR
//    
//        1) Remove the following conditional definition:
//                a) #if USER_EXIT_OR_MENU
//                   #endif//USER_EXIT_OR_MENU
//        2) Add the following lines to your MenuScript file in order to
//           associate a menu bar button with your dialog.  In this
//           example, a cascade menu will be created and will be
//           located just before the Help button on the main menubar.
//           The button, SAMPLEVB_BTN is set up to launch your dialog and
//           will be positioned as the first button on your pulldown menu.
//           If you wish to add the button to an existing cascade, simply
//           add the 3 lines between MENU LAUNCH_CASCADE and END_OF_MENU
//           to your menuscript file.
//           The MenuScript file requires an extension of ".men".
//           Move the contents between the dashed lines to your Menuscript file.
//        
//           !-----------------------------------------------------------------------------
//           VERSION 120
//        
//           EDIT UG_GATEWAY_MAIN_MENUBAR
//        
//           BEFORE UG_HELP
//           CASCADE_BUTTON BLOCKSTYLER_DLX_CASCADE_BTN
//           LABEL Dialog Launcher
//           END_OF_BEFORE
//        
//           MENU BLOCKSTYLER_DLX_CASCADE_BTN
//           BUTTON SAMPLEVB_BTN
//           LABEL Display SampleVB dialog
//           ACTIONS <path of Shared library> !For example: D:\temp\SampleVB.dll
//           END_OF_MENU
//           !-----------------------------------------------------------------------------
//        
//        3) Make sure the .men file is in one of the following locations:
//        
//           - $UGII_USER_DIR/startup   
//           - For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
//             recommended. This variable is set to a full directory path to a file 
//             containing a list of root directories for all custom applications.
//             e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_ROOT_DIR\menus\custom_dirs.dat
//    
//------------------------------------------------------------------------------

extern "C" DllExport void  ufusr(char *param, int *retcod, int param_len)
{
    PatternCurveUI *thePatternCurveUI = NULL;
    try
    {
        thePatternCurveUI = new PatternCurveUI();
        // The following method shows the dialog immediately
        thePatternCurveUI->Show();
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        PatternCurveUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if (thePatternCurveUI != NULL)
    {
        delete thePatternCurveUI;
        thePatternCurveUI = NULL;
    }
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
    //return (int)Session::LibraryUnloadOptionExplicitly;
    return (int)Session::LibraryUnloadOptionImmediately;
    //return (int)Session::LibraryUnloadOptionAtTermination;
}

//------------------------------------------------------------------------------
// Following method cleanup any housekeeping chores that may be needed.
// This method is automatically called by NX.
//------------------------------------------------------------------------------
extern "C" DllExport void ufusr_cleanup(void)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        PatternCurveUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int PatternCurveUI::Show()
{
    try
    {
        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();
        BlockDialog::DialogMode mode = editedFeature != NULL ? BlockDialog::DialogModeEdit : BlockDialog::DialogModeCreate;
        theDialog->Show(mode);
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        PatternCurveUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void PatternCurveUI::initialize_cb()
{
    try
    {
        NXOpen::Part *workPart(theSession->Parts()->Work());

        group0 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group0"));
        section = dynamic_cast<NXOpen::BlockStyler::SectionBuilder*>(theDialog->TopBlock()->FindBlock("section"));
        group = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group"));
        group1 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group1"));
        d1 = dynamic_cast<NXOpen::BlockStyler::SpecifyVector*>(theDialog->TopBlock()->FindBlock("d1"));
        d1Count = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("d1Count"));
        d1Pitch = dynamic_cast<NXOpen::BlockStyler::LinearDimension*>(theDialog->TopBlock()->FindBlock("d1Pitch"));
        UseD2 = dynamic_cast<NXOpen::BlockStyler::Toggle*>(theDialog->TopBlock()->FindBlock("UseD2"));
        group11 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group11"));
        d2 = dynamic_cast<NXOpen::BlockStyler::SpecifyVector*>(theDialog->TopBlock()->FindBlock("d2"));
        d2Count = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("d2Count"));
        d2Pitch = dynamic_cast<NXOpen::BlockStyler::LinearDimension*>(theDialog->TopBlock()->FindBlock("d2Pitch"));

        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();

        if (editedFeature == NULL)
        {
            NXOpen::Unit *unit0(dynamic_cast<NXOpen::Unit *>(workPart->UnitCollection()->FindObject("MilliMeter")));
            NXOpen::Expression *d1PitchExp = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit0);
            d1Pitch->SetExpressionObject(d1PitchExp);

            NXOpen::Expression *d1CountExp = workPart->Expressions()->CreateSystemExpression("1");

            tag_t tagexp = d1CountExp->Tag();
            d1Count->SetExpressionObject(d1CountExp);

            NXOpen::Expression *d2PitchExp = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit0);
            d2Pitch->SetExpressionObject(d2PitchExp);

            NXOpen::Expression *d2CountExp = workPart->Expressions()->CreateSystemExpression("1");
            d2Count->SetExpressionObject(d2CountExp);

            group11->SetShow(UseD2->Value());         
            
            NXOpen::Section* sectionObj = workPart->Sections()->CreateSection(0.0095, 0.01, 0.5);
            
            sectionObj->AllowSelfIntersection(true);

            std::vector<NXOpen::TaggedObject *> SelectedObjVec;

            SelectedObjVec.push_back((NXOpen::TaggedObject *)sectionObj);
            
            section->SetSelectedObjects(SelectedObjVec);               
        }
        else
        {
            NXOpen::Features::CustomFeatureData* cfData = editedFeature->FeatureData();

            Features::CustomTagAttribute *sectionAttrib = cfData->HasCustomAttribute("section", NXOpen::Features::CustomAttribute::TypeTag) ? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("section")) : NULL;

            Features::CustomTagAttribute *d1Attrib = cfData->HasCustomAttribute("d1", NXOpen::Features::CustomAttribute::TypeTag) ? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("d1")) : NULL;

            Features::CustomExpressionAttribute* d1CountAttrib = cfData->HasCustomAttribute("d1Count", NXOpen::Features::CustomAttribute::TypeExpression) ? dynamic_cast<Features::CustomExpressionAttribute*> (cfData->CustomExpressionAttributeByName("d1Count")) : NULL;

            Features::CustomExpressionAttribute *d1PtichAttrib = cfData->HasCustomAttribute("d1Pitch", NXOpen::Features::CustomAttribute::TypeExpression) ? dynamic_cast<Features::CustomExpressionAttribute*> (cfData->CustomExpressionAttributeByName("d1Pitch")) : NULL;

            Features::CustomLogicalAttribute *useD2Attrib = cfData->HasCustomAttribute("useD2", NXOpen::Features::CustomAttribute::TypeBool) ? dynamic_cast<Features::CustomLogicalAttribute*> (cfData->CustomLogicalAttributeByName("useD2")) : NULL;

            Features::CustomTagAttribute *d2Attrib = cfData->HasCustomAttribute("d2", NXOpen::Features::CustomAttribute::TypeTag) ? cfData->CustomTagAttributeByName("d2") : NULL;

            Features::CustomExpressionAttribute* d2CountAttrib = cfData->HasCustomAttribute("d2Count", NXOpen::Features::CustomAttribute::TypeExpression) ? dynamic_cast<Features::CustomExpressionAttribute*> (cfData->CustomExpressionAttributeByName("d2Count")) : NULL;

            Features::CustomExpressionAttribute *d2PtichAttrib = cfData->HasCustomAttribute("d2Pitch", NXOpen::Features::CustomAttribute::TypeExpression) ? dynamic_cast<Features::CustomExpressionAttribute*> (cfData->CustomExpressionAttributeByName("d2Pitch")) : NULL;

            std::vector<NXOpen::TaggedObject *> inputVec;

            if (sectionAttrib != NULL)
            {
                NXOpen::Section* sectionValue = dynamic_cast<NXOpen::Section*>(sectionAttrib->Value());
                std::vector<NXOpen::NXObject *> objects;
                try
                {
                    sectionValue->EvaluateAndAskOutputEntities(objects);
                }
                catch (exception& ex)
                {
                    
                }      
                inputVec.push_back(sectionValue);
                section->SetSelectedObjects(inputVec);
                inputVec.clear();
            }

            if (d1Attrib != NULL)
            {
                NXOpen::Direction* d1Value = dynamic_cast<NXOpen::Direction*>(d1Attrib->Value());
                inputVec.push_back(d1Value);
                d1->SetSelectedObjects(inputVec);
                inputVec.clear();
            }

            if (d1CountAttrib != NULL)
            {
                NXOpen::Expression* d1CountValue = d1CountAttrib->Value();
                this->d1CountCache = d1CountValue->Value();
                this->d1CountCached = true;
                d1Count->SetExpressionObject(d1CountValue);
            }
            else
            {
                NXOpen::Expression *d1CountExp = workPart->Expressions()->CreateSystemExpression("1");
                d1Count->SetExpressionObject(d1CountExp);
            }

            if (d1PtichAttrib != NULL)
            {
                NXOpen::Expression* d1PitchValue = d1PtichAttrib->Value();
                this->d1PitchCache = d1PitchValue->Value();
                this->d1pitchCached = true;
                d1Pitch->SetExpressionObject(d1PitchValue);
            }
            else
            {
                NXOpen::Unit *unit0(dynamic_cast<NXOpen::Unit *>(workPart->UnitCollection()->FindObject("MilliMeter")));

                NXOpen::Expression *d1PitchExp = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit0);
                d1Pitch->SetExpressionObject(d1PitchExp);
            }

            if (useD2Attrib != NULL)
            {
                bool useD2Value = useD2Attrib->Value();
                this->useD2Cache = useD2Value;
                this->useD2Cached = true;
                UseD2->SetValue(useD2Attrib->Value());
                group11->SetShow(useD2Value);
            }

            if (d2Attrib != NULL)
            {
                NXOpen::Direction* d2Value = dynamic_cast<NXOpen::Direction*>(d2Attrib->Value());
                inputVec.push_back(d2Value);
                d2->SetSelectedObjects(inputVec);
                inputVec.clear();
            }

            if (d2CountAttrib != NULL)
            {
                NXOpen::Expression* d2CountValue = d2CountAttrib->Value();
                this->d2CountCache = d2CountValue->Value();
                this->d2CountCached = true;
                d2Count->SetExpressionObject(d2CountValue);
            }
            else
            {
                NXOpen::Expression *d2CountExp = workPart->Expressions()->CreateSystemExpression("1");
                d2Count->SetExpressionObject(d2CountExp);
            }

            if (d2PtichAttrib != NULL)
            {
                NXOpen::Expression* d2PitchValue = d2PtichAttrib->Value();
                this->d2PitchCache = d2PitchValue->Value();
                this->d2pitchCached = true;
                d2Pitch->SetExpressionObject(d2PitchValue);
            }
            else
            {
                NXOpen::Unit *unit0(dynamic_cast<NXOpen::Unit *>(workPart->UnitCollection()->FindObject("MilliMeter")));

                NXOpen::Expression *d2PitchExp = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit0);
                d2Pitch->SetExpressionObject(d2PitchExp);
            }
        }

        group11->SetShow(UseD2->Value());

    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        PatternCurveUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void PatternCurveUI::dialogShown_cb()
{
    try
    {    
        // Restore cached values so as to override values set by dialog memory.
        this->UseD2->SetValue(false);
        this->group11->SetShow(false);
        if (this->d1CountCached)
        {
            this->d1Count->SetValue(this->d1CountCache);
            this->d1CountCached = false;
        }
        if (this->d1pitchCached)
        {
            this->d1Pitch->SetValue(this->d1PitchCache);
            this->d1pitchCached = false;
        }
        if (this->useD2Cached)
        {
            this->UseD2->SetValue(this->useD2Cache);
            this->group11->SetShow(this->useD2Cache);
            this->useD2Cached = false;
        }
        if (this->d2CountCached)
        {
            this->d2Count->SetValue(this->d2CountCache);
            this->d2CountCached = false;
        }
        if (this->d2pitchCached)
        {
            this->d2Pitch->SetValue(this->d2PitchCache);
            this->d2pitchCached = false;
        }
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        PatternCurveUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int PatternCurveUI::apply_cb()
{
    int errorCode = 0;
    Features::CustomFeatureBuilder *customFeatureBuilder = NULL;
    try
    {
        NXOpen::Part *workPart(theSession->Parts()->Work());

        std::vector<NXOpen::Features::CustomAttribute*> attrs(0);

        NXOpen::Features::CustomFeatureData *cfData = NULL;

        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();

        customFeatureBuilder = workPart->Features()->CreateCustomFeatureBuilder(editedFeature);

        std::vector<NXOpen::TaggedObject *> SelectedObjVec;

        NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
        NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

        if (editedFeature == NULL)
        {
            // Create attributes

            // Section :: Curve to pattern
            SelectedObjVec = this->section->GetSelectedObjects();

            if (SelectedObjVec.size() == 1)
            {
                std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
                attributeProperties.push_back(NXOpen::Features::CustomAttribute::Property::PropertyMandatoryInput);
                NXOpen::Features::CustomTagAttribute* sectionAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("section", attributeProperties));
                sectionAttrib->SetValue(SelectedObjVec[0]);
                attrs.push_back(sectionAttrib);
            }
            SelectedObjVec.clear();

            // d1 : Direction 1 to pattern

            SelectedObjVec = this->d1->GetSelectedObjects();
            if (SelectedObjVec.size() == 1)
            {
                std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
                attributeProperties.push_back(NXOpen::Features::CustomAttribute::Property::PropertyMandatoryInput);
                NXOpen::Features::CustomTagAttribute* d1Attrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("d1", attributeProperties));
                d1Attrib->SetValue(SelectedObjVec[0]);
                attrs.push_back(d1Attrib);
            }
            SelectedObjVec.clear();

            // d1Count : Number of instances in direction 1 
            SelectedObjVec.push_back(this->d1Count->ExpressionObject());

            if (!SelectedObjVec.empty())
            {
                NXOpen::Expression*  d1CountExp = dynamic_cast<NXOpen::Expression*>(SelectedObjVec[0]);
                std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
                NXOpen::Features::CustomExpressionAttribute* d1CountAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("d1Count", attributeProperties));
                d1CountAttrib->SetValue(d1CountExp);
                attrs.push_back(d1CountAttrib);
            }
            SelectedObjVec.clear();

            // d1Pitch : Pitch distance in direction 1. 
            SelectedObjVec.push_back(this->d1Pitch->ExpressionObject());

            if (!SelectedObjVec.empty())
            {
                NXOpen::Expression*  d1PitchExpression = dynamic_cast<NXOpen::Expression*>(SelectedObjVec[0]);
                std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
                NXOpen::Features::CustomExpressionAttribute* d1PitchAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("d1Pitch", attributeProperties));
                d1PitchAttrib->SetValue(d1PitchExpression);
                attrs.push_back(d1PitchAttrib);
            }
            SelectedObjVec.clear();

            // useD2 :: Use direction 2 to pattern
            std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
            NXOpen::Features::CustomLogicalAttribute* useD2Attrib = dynamic_cast<NXOpen::Features::CustomLogicalAttribute*>(attribCollection->CreateCustomLogicalAttribute("useD2", attributeProperties));
            useD2Attrib->SetValue(this->UseD2->Value());
            attrs.push_back(useD2Attrib);

            // d2 : Direction 2 to pattern

            SelectedObjVec = this->d2->GetSelectedObjects();
            if (SelectedObjVec.size() == 1)
            {
                std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
                NXOpen::Features::CustomTagAttribute* d2Attrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("d2", attributeProperties));
                d2Attrib->SetValue(SelectedObjVec[0]);
                attrs.push_back(d2Attrib);
            }
            SelectedObjVec.clear();


            // d2Count : Number of instances in direction 2
            SelectedObjVec.push_back(this->d2Count->ExpressionObject());

            if (!SelectedObjVec.empty())
            {
                NXOpen::Expression*  d2CountExp = dynamic_cast<NXOpen::Expression*>(SelectedObjVec[0]);
                std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
                NXOpen::Features::CustomExpressionAttribute* d2CountAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("d2Count", attributeProperties));
                d2CountAttrib->SetValue(d2CountExp);
                attrs.push_back(d2CountAttrib);
            }
            SelectedObjVec.clear();


            // d2Pitch : Pitch distance in direction 2. 
            SelectedObjVec.push_back(this->d2Pitch->ExpressionObject());

            if (!SelectedObjVec.empty())
            {
                NXOpen::Expression*  d2PitchExpression = dynamic_cast<NXOpen::Expression*>(SelectedObjVec[0]);
                std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
                NXOpen::Features::CustomExpressionAttribute* d2PitchAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("d2Pitch", attributeProperties));
                d2PitchAttrib->SetValue(d2PitchExpression);
                attrs.push_back(d2PitchAttrib);
            }
            SelectedObjVec.clear();

            // Create custom feature data to store attributes
            cfData = workPart->Features()->CustomFeatureDataCollection()->CreateData(cfClass, attrs);
        }
        else
        {
            cfData = editedFeature->FeatureData();
            
            // Synch up d2 : Direction 2 to pattern
            Features::CustomTagAttribute *d2Attrib = cfData->HasCustomAttribute("d2", NXOpen::Features::CustomAttribute::TypeTag)? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("d2")):NULL;

            if (d2Attrib == NULL)
            {
                SelectedObjVec = this->d2->GetSelectedObjects();
                if (SelectedObjVec.size() == 1)
                {
                    std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
                    d2Attrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("d2", attributeProperties));
                    d2Attrib->SetValue(SelectedObjVec[0]);
                    attrs.push_back(d2Attrib);
                }
                SelectedObjVec.clear();
            }

            // Synch Up useD2 attribute to UI
            Features::CustomLogicalAttribute* useD2Attrib = cfData->HasCustomAttribute("useD2", NXOpen::Features::CustomAttribute::TypeBool) ? dynamic_cast<Features::CustomLogicalAttribute*> (cfData->CustomLogicalAttributeByName("useD2")):NULL;
            useD2Attrib->SetValue(this->UseD2->Value());
            
            cfData->AddCustomAttributes(attrs);
        }
        // Set Custom Feature data in Custom feature builder
        customFeatureBuilder->SetFeatureData(cfData);

        // Commit the builder to create feature
        Features::Feature *feature1;
        feature1 = customFeatureBuilder->CommitFeature();

        // Delete the builder
        customFeatureBuilder->Destroy();
        customFeatureBuilder = NULL;

    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        if (customFeatureBuilder != NULL)
        {
            customFeatureBuilder->Destroy();
            customFeatureBuilder = NULL;
        }

        PatternCurveUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int PatternCurveUI::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        NXOpen::Part *workPart(theSession->Parts()->Work());

        std::vector<NXOpen::Features::CustomAttribute*> attrs(0);

        NXOpen::Features::CustomFeatureData *cfData = NULL;
        
        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();
        
        std::vector<NXOpen::TaggedObject *> SelectedObjVec;

        NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
        NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

        if (editedFeature != NULL)
        {
            cfData = editedFeature->FeatureData();
        }

        if (block == section)
        {
            //---------Enter your code here-----------
        }
        else if (block == d1 && cfData != NULL)
        {
            // Synch up d1 : Direction 1 to pattern
            Features::CustomTagAttribute *d1Attrib = cfData->HasCustomAttribute("d1", NXOpen::Features::CustomAttribute::TypeTag) ? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("d1")):NULL;

            if (d1Attrib == NULL)
            { 
                std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
                d1Attrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("d1", attributeProperties));
                attrs.push_back(d1Attrib); 
                cfData->AddCustomAttributes(attrs);
            }

            SelectedObjVec = this->d1->GetSelectedObjects();
            if (SelectedObjVec.size() == 1)
            {
                d1Attrib->SetValue(SelectedObjVec[0]);
            }
            SelectedObjVec.clear();
        }
        else if (block == d1Count)
        {
            //---------Enter your code here-----------
        }
        else if (block == d1Pitch)
        {
            //---------Enter your code here-----------
        }
        else if (block == UseD2)
        {
            group11->SetShow(UseD2->Value());
        }
        else if (block == d2 && cfData != NULL)
        {
            // Synch up d2 : Direction 2 to pattern
            Features::CustomTagAttribute *d2Attrib = cfData->HasCustomAttribute("d2", NXOpen::Features::CustomAttribute::TypeTag) ? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("d2")):NULL;

            if (d2Attrib == NULL)
            {
                std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
                d2Attrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("d2", attributeProperties));
                attrs.push_back(d2Attrib);
                cfData->AddCustomAttributes(attrs);
            }

            SelectedObjVec = this->d2->GetSelectedObjects();
            if (SelectedObjVec.size() == 1)
            {
                d2Attrib->SetValue(SelectedObjVec[0]);
            }
            SelectedObjVec.clear();
        }
        else if (block == d2Count)
        {
            //---------Enter your code here-----------
        }
        else if (block == d2Pitch)
        {
            //---------Enter your code here-----------
        }
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        PatternCurveUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int PatternCurveUI::ok_cb()
{
    int errorCode = 0;
    try
    {
        errorCode = apply_cb();
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        PatternCurveUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Function Name: GetBlockProperties
//Description: Returns the propertylist of the specified BlockID
//------------------------------------------------------------------------------
PropertyList* PatternCurveUI::GetBlockProperties(const char *blockID)
{
    return theDialog->GetBlockProperties(blockID);
}
