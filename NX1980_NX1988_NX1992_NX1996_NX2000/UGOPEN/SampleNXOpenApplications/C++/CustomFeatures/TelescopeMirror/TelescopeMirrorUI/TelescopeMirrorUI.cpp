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

//Added for functionality
#include <NXOpen/Ellipse.hxx>
#include <NXOpen/NXMatrix.hxx>
#include <NXOpen/NXMatrixCollection.hxx>
#include <NXOpen/CurveCollection.hxx>
#include <NXOpen/Xform.hxx>
#include <NXOpen/XformCollection.hxx>
#include <NXOpen/CartesianCoordinateSystem.hxx>
#include <NXOpen/CoordinateSystemCollection.hxx>
#include <NXOpen/Features_RevolveBuilder.hxx>
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/GeometricUtilities_Limits.hxx>
#include <NXOpen/GeometricUtilities_Extend.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SectionCollection.hxx>
#include <NXOpen/CurveDumbRule.hxx>
#include <NXOpen/ScRuleFactory.hxx>
#include <NXOpen/DirectionCollection.hxx>
#include <NXOpen/AxisCollection.hxx>
#include <NXOpen/Features_CylinderBuilder.hxx>
#include <NXOpen/Axis.hxx>
#include <NXOpen/Point.hxx>
#include <NXOpen/PointCollection.hxx>
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/Features_BooleanBuilder.hxx>
#include <NXOpen/SelectBodyList.hxx>
#include <NXOpen/ScCollectorCollection.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/BodyDumbRule.hxx>
#include <NXOpen/Features_ExtrudeBuilder.hxx>
#include <NXOpen/GeometricUtilities_FeatureOffset.hxx>
#include <NXOpen/ExpressionCollection.hxx>
#include <NXOpen/Unit.hxx>

// Custom Feature specific Includes
#include <NXOpen/Features_CustomFeatureBuilder.hxx>
#include <NXOpen/Features_CustomFeatureDataCollection.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>
#include <NXOpen/Features_CustomAttributeCollection.hxx>
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/Features_CustomLogicalAttribute.hxx>
#include <NXOpen/Features_CustomLogicalAttribute.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeature.hxx>


using std::string;
using std::exception;
using std::stringstream;
using std::endl;
using std::cout;
using std::cerr;

typedef std::vector<NXOpen::IBaseCurve *> baseVector_t;

#include "TelescopeMirrorUI.hpp"

using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(TelescopeMirrorUI::theSession) = NULL;
UI *(TelescopeMirrorUI::theUI) = NULL;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
TelescopeMirrorUI::TelescopeMirrorUI()
{
    try
    {
        // Initialize the NX Open C++ API environment
        TelescopeMirrorUI::theSession = NXOpen::Session::GetSession();
        TelescopeMirrorUI::theUI = UI::GetUI();
        theDlxFileName = "TelescopeMirrorUI.dlx";
        theDialog = TelescopeMirrorUI::theUI->CreateDialog(theDlxFileName);
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &TelescopeMirrorUI::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &TelescopeMirrorUI::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &TelescopeMirrorUI::update_cb));
        theDialog->AddFilterHandler(make_callback(this, &TelescopeMirrorUI::filter_cb));
        theDialog->AddInitializeHandler(make_callback(this, &TelescopeMirrorUI::initialize_cb));
        theDialog->AddFocusNotifyHandler(make_callback(this, &TelescopeMirrorUI::focusNotify_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &TelescopeMirrorUI::dialogShown_cb));
        theDialog->AddEnableOKButtonHandler(make_callback(this, &TelescopeMirrorUI::enableOKButton_cb));
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
TelescopeMirrorUI::~TelescopeMirrorUI()
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
//    2. THROUGH CALLBACK OF ANOTHER DIALOG
//
//        1) Remove the following conditional definition:
//             #if CALLBACK
//             #endif//CALLBACK
//        2) Call the following line of code from where ever you want to lauch this dialog.
//             MirrorGeneratorUI->Show_MirrorGeneratorUI();
//        3) Integrate this file with your main application file.
//
//    3. MENU BAR
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
//#if USER_EXIT_OR_MENU ::: Want to lauch from menu 

extern "C" DllExport void  ufusr(char *param, int *retcod, int param_len)
{
    TelescopeMirrorUI *theMirrorGeneratorUI = NULL;
    try
    {
        theMirrorGeneratorUI = new TelescopeMirrorUI();
        // The following method shows the dialog immediately
        theMirrorGeneratorUI->Show();
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if (theMirrorGeneratorUI != NULL)
    {
        delete theMirrorGeneratorUI;
        theMirrorGeneratorUI = NULL;
    }
}
//#endif//USER_EXIT_OR_MENU
//#if USER_EXIT

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
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
//#endif//USER_EXIT

int TelescopeMirrorUI::Show()
{
    try
    {
        Session *theSession = Session::GetSession();
        NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();
        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();
        BlockDialog::DialogMode mode = editedFeature != NULL ? BlockDialog::DialogModeEdit : BlockDialog::DialogModeCreate;
        theDialog->Show(mode);
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

#if CALLBACK
//------------------------------------------------------------------------------
//Method name: Show_MirrorGeneratorUI
//------------------------------------------------------------------------------
void TelescopeMirrorUI::Show_MirrorGeneratorUI()
{
    TelescopeMirrorUI *theMirrorGeneratorUI = NULL;
    try
    {
        theMirrorGeneratorUI = new TelescopeMirrorUI();
        // The following method shows the dialog immediately
        theMirrorGeneratorUI->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if(theMirrorGeneratorUI != NULL)
    {
        delete theMirrorGeneratorUI;
        theMirrorGeneratorUI = NULL;
    }
}
#endif//CALLBACK

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void TelescopeMirrorUI::initialize_cb()
{
    try
    {
        Session *theSession = Session::GetSession();
        NXOpen::Part *workPart(theSession->Parts()->Work());
        NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();
        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();

        tabControl = dynamic_cast<NXOpen::BlockStyler::TabControl*>(theDialog->TopBlock()->FindBlock("tabControl"));
        tabPage = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("tabPage"));
        group0 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group0"));
        m_location = dynamic_cast<NXOpen::BlockStyler::SpecifyPoint*>(theDialog->TopBlock()->FindBlock("m_location"));
        m_direction = dynamic_cast<NXOpen::BlockStyler::SpecifyVector*>(theDialog->TopBlock()->FindBlock("m_direction"));
        group = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group"));

        m_baseDia = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("m_baseDia"));

        m_conicConstant = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("m_conicConstant"));
        m_radiusOfCurvature = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("m_radiusOfCurvature"));
        m_typeOfCurve = dynamic_cast<NXOpen::BlockStyler::Label*>(theDialog->TopBlock()->FindBlock("m_typeOfCurve"));
        group1 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group1"));
        m_thickAtCenter = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("m_thickAtCenter"));
        group2 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group2"));
        m_SuppressTrim = dynamic_cast<NXOpen::BlockStyler::Toggle*>(theDialog->TopBlock()->FindBlock("m_SuppressTrim"));
        tabPage1 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("tabPage1"));
        group3 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group3"));
        m_primaryDir = dynamic_cast<NXOpen::BlockStyler::SpecifyVector*>(theDialog->TopBlock()->FindBlock("m_primaryDir"));
        group4 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group4"));
        m_aperatureShape = dynamic_cast<NXOpen::BlockStyler::Enumeration*>(theDialog->TopBlock()->FindBlock("m_aperatureShape"));
        m_trimDir = dynamic_cast<NXOpen::BlockStyler::Enumeration*>(theDialog->TopBlock()->FindBlock("m_trimDir"));
        m_primaryLen = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("m_primaryLen"));
        m_secondaryLen = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("m_secondaryLen"));
        group5 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group5"));
        m_primaryOffset = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("m_primaryOffset"));
        m_secondaryOffset = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("m_secondaryOffset"));
        group6 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group6"));
        m_SuppressAper = dynamic_cast<NXOpen::BlockStyler::Toggle*>(theDialog->TopBlock()->FindBlock("m_SuppressAper"));

        if (editedFeature == NULL)
        {
            CreateAndSetExpressionsObjects(workPart);  
        }
        else
        {
            NXOpen::Features::CustomFeatureData *cfData = editedFeature->FeatureData();

            PopulateUIFromCustomFeatureData(cfData);
        }
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void TelescopeMirrorUI::dialogShown_cb()
{
    try
    {
        Session *theSession = Session::GetSession();
        NXOpen::Part *workPart(theSession->Parts()->Work());
        NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();
        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();
        if (editedFeature != NULL)
        {
            NXOpen::Features::CustomFeatureData *cfData = editedFeature->FeatureData();
            //---- Enter your callback code here -----
            if (m_baseDiaCached)
            {
                m_baseDia->SetValue(m_baseDiacache);
                m_baseDiaCached = false;
            }
            if (m_conicConstantCached)
            {
                m_conicConstant->SetValue(m_conicConstantcache);
                m_conicConstantCached = false;
            }
            if (m_radiusOfCurvatureCached)
            {
                m_radiusOfCurvature->SetValue(m_radiusOfCurvaturecache);
                m_radiusOfCurvatureCached = false;
            }
            if (m_thickAtCenterCached)
            {
                m_thickAtCenter->SetValue(m_thickAtCentercache);
                m_thickAtCenterCached = false;
            }
            if (m_primaryLenCached)
            {
                m_primaryLen->SetValue(m_primaryLencache);
                m_primaryLenCached = false;
            }
            if (m_secondaryLenCached)
            {
                m_secondaryLen->SetValue(m_secondaryLencache);
                m_secondaryLenCached = false;
            }
            if (m_primaryOffsetCached)
            {
                m_primaryOffset->SetValue(m_primaryOffsetcache);
                m_primaryOffsetCached = false;
            }
            if (m_secondaryOffsetCached)
            {
                m_secondaryOffset->SetValue(m_secondaryOffsetcache);
                m_secondaryOffsetCached = false;
            }
            if (m_aperatureShapeCached)
            {
                m_aperatureShape->SetValueAsString(m_aperatureShapecache);
                m_aperatureShapeCached = false;
            }

            NXOpen::Features::CustomLogicalAttribute* m_SuppressTrimAttrib = cfData->CustomLogicalAttributeByName("m_SuppressTrim");
            m_SuppressTrim->SetValue(m_SuppressTrimAttrib->Value());

            NXOpen::Features::CustomLogicalAttribute* m_SuppressAperAttrib = cfData->CustomLogicalAttributeByName("m_SuppressAper");
            m_SuppressAper->SetValue(m_SuppressAperAttrib->Value());
        }
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int TelescopeMirrorUI::apply_cb()
{
    int errorCode = 0;
    Features::CustomFeatureBuilder *customFeatureBuilder = NULL;
    try
    {
        Session *theSession = Session::GetSession();

        NXOpen::Part *workPart(theSession->Parts()->Work());

        std::vector<NXOpen::Features::CustomAttribute*> attrs(0);

        NXOpen::Features::CustomFeatureData *cfData = NULL;

        NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

        NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::TelescopeMirror");

        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();

        customFeatureBuilder = workPart->Features()->CreateCustomFeatureBuilder(editedFeature);

        if (editedFeature == NULL)
        {
            CreateFeatureAttributes(attrs);

            // Create custom feature data to store attributes
            cfData = workPart->Features()->CustomFeatureDataCollection()->CreateData(cfClass, attrs);

        }
        else
        {
            cfData = editedFeature->FeatureData();
        }

        PopulateAttributeValues(cfData);

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
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int TelescopeMirrorUI::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if (block == m_conicConstant)
        {
            // here K = m_conicConstant
            // If K > 0,  conicGeom is Oblate Elliptical and not valid, Reject it.
            // If K = 0,  conicGeom is spherical
            // If 0>K>-1, conicGeom is prolateEllipse
            // If K==-1,  conicGeom is parabolic,
            // If k < -1, conicGeom is hyperbolic
            this->SetCurrentGeomInUI(m_conicConstant->Value());

        }
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int TelescopeMirrorUI::ok_cb()
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
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: filter_cb
//------------------------------------------------------------------------------
int TelescopeMirrorUI::filter_cb(NXOpen::BlockStyler::UIBlock* block, NXOpen::TaggedObject* selectObject)
{
    return(UF_UI_SEL_ACCEPT);
}

//------------------------------------------------------------------------------
//Callback Name: focusNotify_cb
//This callback is executed when any block (except the ones which receive keyboard entry such as Integer block) receives focus.
//------------------------------------------------------------------------------
void TelescopeMirrorUI::focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: enableOKButton_cb
//This callback allows the dialog to enable/disable the OK and Apply button.
//------------------------------------------------------------------------------
bool TelescopeMirrorUI::enableOKButton_cb()
{
    try
    {
        return true;    //Add code above
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        TelescopeMirrorUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return true;
}

//------------------------------------------------------------------------------
//Function Name: GetBlockProperties
//Description: Returns the propertylist of the specified BlockID
//------------------------------------------------------------------------------
PropertyList* TelescopeMirrorUI::GetBlockProperties(const char *blockID)
{
    return theDialog->GetBlockProperties(blockID);
}


//--------Added Code from Template-----------
void TelescopeMirrorUI::print(const NXString &msg)
{
    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);
}
void TelescopeMirrorUI::print(const string &msg)
{
    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);
}
void TelescopeMirrorUI::print(const char * msg)
{
    if (!lw->IsOpen()) lw->Open();
    lw->WriteLine(msg);
}
//-------------------------------------------

void TelescopeMirrorUI::SetCurrentGeomInUI(double K)
{

    if (K == 0)
    {
        m_typeOfCurve->SetLabel("Spherical");
    }
    else if (0 > K && K > -1)
    {
        m_typeOfCurve->SetLabel("Prolate Elliptical");
    }
    else if (K == -1)
    {
        m_typeOfCurve->SetLabel("Parabola");
    }
    else if (K < -1)
    {
        m_typeOfCurve->SetLabel("Hyperbola");
    }

}

void TelescopeMirrorUI::CreateFeatureAttributes(std::vector<NXOpen::Features::CustomAttribute*> &attrs)
{
    Session *theSession = Session::GetSession();

    NXOpen::Part *workPart(theSession->Parts()->Work());

    NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
    NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

    std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
    NXOpen::Features::CustomExpressionAttribute* m_radiusOfCurvatureAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_radiusOfCurvature", attributeProperties));
    attrs.push_back(m_radiusOfCurvatureAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_conicConstantAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_conicConstant", attributeProperties));
    attrs.push_back(m_conicConstantAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_baseDiaAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_baseDia", attributeProperties));
    attrs.push_back(m_baseDiaAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_thickAtCenterAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_thickAtCenter", attributeProperties));
    attrs.push_back(m_thickAtCenterAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_primaryLenAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_primaryLen", attributeProperties));
    attrs.push_back(m_primaryLenAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_secondaryLenAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_secondaryLen", attributeProperties));
    attrs.push_back(m_secondaryLenAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_primaryOffsetAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_primaryOffset", attributeProperties));
    attrs.push_back(m_primaryOffsetAttrib);

    NXOpen::Features::CustomExpressionAttribute* m_secondaryOffsetAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_secondaryOffset", attributeProperties));
    attrs.push_back(m_secondaryOffsetAttrib);

    NXOpen::Features::CustomLogicalAttribute* m_SuppressTrimAttrib = dynamic_cast<NXOpen::Features::CustomLogicalAttribute*>(attribCollection->CreateCustomLogicalAttribute("m_SuppressTrim", attributeProperties));
    attrs.push_back(m_SuppressTrimAttrib);

    NXOpen::Features::CustomLogicalAttribute* m_SuppressAperAttrib = dynamic_cast<NXOpen::Features::CustomLogicalAttribute*>(attribCollection->CreateCustomLogicalAttribute("m_SuppressAper", attributeProperties));
    attrs.push_back(m_SuppressAperAttrib);

    NXOpen::Features::CustomStringAttribute* m_aperatureShapeAttrib = dynamic_cast<NXOpen::Features::CustomStringAttribute*>(attribCollection->CreateCustomStringAttribute("m_aperatureShape", attributeProperties));
    attrs.push_back(m_aperatureShapeAttrib);

    NXOpen::Features::CustomTagAttribute* m_revolveCurvesAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_revolveCurve", attributeProperties));
    attrs.push_back(m_revolveCurvesAttrib);

    NXOpen::Features::CustomTagArrayAttribute* m_apperCurvesAttrib = dynamic_cast<NXOpen::Features::CustomTagArrayAttribute*>(attribCollection->CreateCustomTagArrayAttribute("m_apperCurves", attributeProperties));
    attrs.push_back(m_apperCurvesAttrib);

    attributeProperties.push_back(NXOpen::Features::CustomAttribute::Property::PropertyMandatoryInput);
    NXOpen::Features::CustomTagAttribute* m_locationAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_location", attributeProperties));
    attrs.push_back(m_locationAttrib);

    NXOpen::Features::CustomTagAttribute* m_directionAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_direction", attributeProperties));
    attrs.push_back(m_directionAttrib);

    NXOpen::Features::CustomTagAttribute* m_primaryDirAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_primaryDir", attributeProperties));
    attrs.push_back(m_primaryDirAttrib);

    attributeProperties.clear();
}

void TelescopeMirrorUI::PopulateAttributeValues(NXOpen::Features::CustomFeatureData * cfData)
{
    {
        NXOpen::Features::CustomExpressionAttribute* m_radiusOfCurvatureAttrib = cfData->CustomExpressionAttributeByName("m_radiusOfCurvature");
        m_radiusOfCurvatureAttrib->SetValue(dynamic_cast<NXOpen::Expression*>(m_radiusOfCurvature->ExpressionObject()));

        NXOpen::Features::CustomExpressionAttribute* m_conicConstantAttrib = cfData->CustomExpressionAttributeByName("m_conicConstant");
        m_conicConstantAttrib->SetValue(dynamic_cast<NXOpen::Expression*>(m_conicConstant->ExpressionObject()));

        NXOpen::Features::CustomExpressionAttribute* m_baseDiaAttrib = cfData->CustomExpressionAttributeByName("m_baseDia");
        m_baseDiaAttrib->SetValue(dynamic_cast<NXOpen::Expression*>(m_baseDia->ExpressionObject()));
        
        NXOpen::Features::CustomExpressionAttribute* m_thickAtCenterAttrib = cfData->CustomExpressionAttributeByName("m_thickAtCenter");
        m_thickAtCenterAttrib->SetValue(dynamic_cast<NXOpen::Expression*>(m_thickAtCenter->ExpressionObject()));

        NXOpen::Features::CustomExpressionAttribute* m_primaryLenAttrib = cfData->CustomExpressionAttributeByName("m_primaryLen");
        m_primaryLenAttrib->SetValue(dynamic_cast<NXOpen::Expression*>(m_primaryLen->ExpressionObject()));

        NXOpen::Features::CustomExpressionAttribute* m_secondaryLenAttrib = cfData->CustomExpressionAttributeByName("m_secondaryLen");
        m_secondaryLenAttrib->SetValue(dynamic_cast<NXOpen::Expression*>(m_secondaryLen->ExpressionObject()));

        NXOpen::Features::CustomExpressionAttribute* m_primaryOffsetAttrib = cfData->CustomExpressionAttributeByName("m_primaryOffset");
        m_primaryOffsetAttrib->SetValue(dynamic_cast<NXOpen::Expression*>(m_primaryOffset->ExpressionObject()));

        NXOpen::Features::CustomExpressionAttribute* m_secondaryOffsetAttrib = cfData->CustomExpressionAttributeByName("m_secondaryOffset");
        m_secondaryOffsetAttrib->SetValue(dynamic_cast<NXOpen::Expression*>(m_secondaryOffset->ExpressionObject()));

        std::vector<NXOpen::TaggedObject *> SelectedObjVec;
        NXOpen::Features::CustomTagAttribute* m_locationAttrib = cfData->CustomTagAttributeByName("m_location");
        SelectedObjVec = m_location->GetSelectedObjects();
        m_locationAttrib->SetValue(SelectedObjVec[0]);
        SelectedObjVec.clear();

        NXOpen::Features::CustomTagAttribute* m_directionAttrib = cfData->CustomTagAttributeByName("m_direction");
        SelectedObjVec = m_direction->GetSelectedObjects();
        m_directionAttrib->SetValue(SelectedObjVec[0]);
        SelectedObjVec.clear();

        NXOpen::Features::CustomTagAttribute* m_primaryDirAttrib = cfData->CustomTagAttributeByName("m_primaryDir");
        SelectedObjVec = m_primaryDir->GetSelectedObjects();
        m_primaryDirAttrib->SetValue(SelectedObjVec[0]);
        SelectedObjVec.clear();

        NXOpen::Features::CustomLogicalAttribute* m_SuppressTrimAttrib = cfData->CustomLogicalAttributeByName("m_SuppressTrim");
        m_SuppressTrimAttrib->SetValue(m_SuppressTrim->Value());

        NXOpen::Features::CustomLogicalAttribute* m_SuppressAperAttrib = cfData->CustomLogicalAttributeByName("m_SuppressAper");
        m_SuppressAperAttrib->SetValue(m_SuppressAper->Value());

        NXOpen::Features::CustomStringAttribute* m_aperatureShapeAttrib = cfData->CustomStringAttributeByName("m_aperatureShape");
        m_aperatureShapeAttrib->SetValue(m_aperatureShape->ValueAsString());
    }
}

void TelescopeMirrorUI::CreateAndSetExpressionsObjects(NXOpen::Part * workPart)
{
    NXOpen::Expression *m_baseDiaExp = workPart->Expressions()->CreateSystemExpressionWithUnits("1000", dynamic_cast<NXOpen::Unit *>(m_baseDia->Units()));
    m_baseDia->SetExpressionObject(m_baseDiaExp);

    NXOpen::Expression *m_radiusOfCurvatureExp = workPart->Expressions()->CreateSystemExpressionWithUnits("1000", dynamic_cast<NXOpen::Unit *>(m_radiusOfCurvature->Units()));
    m_radiusOfCurvature->SetExpressionObject(m_radiusOfCurvatureExp);

    NXOpen::Expression *m_thickAtCenterExp = workPart->Expressions()->CreateSystemExpressionWithUnits("100", dynamic_cast<NXOpen::Unit *>(m_thickAtCenter->Units()));
    m_thickAtCenter->SetExpressionObject(m_thickAtCenterExp);

    NXOpen::Expression *m_primaryLenExp = workPart->Expressions()->CreateSystemExpressionWithUnits("300", dynamic_cast<NXOpen::Unit *>(m_primaryLen->Units()));
    m_primaryLen->SetExpressionObject(m_primaryLenExp);

    NXOpen::Expression *m_secondaryLenExp = workPart->Expressions()->CreateSystemExpressionWithUnits("500", dynamic_cast<NXOpen::Unit *>(m_secondaryLen->Units()));
    m_secondaryLen->SetExpressionObject(m_secondaryLenExp);

    NXOpen::Expression *m_primaryOffsetExp = workPart->Expressions()->CreateSystemExpressionWithUnits("200", dynamic_cast<NXOpen::Unit *>(m_primaryOffset->Units()));
    m_primaryOffset->SetExpressionObject(m_primaryOffsetExp);

    NXOpen::Expression *m_secondaryOffsetExp = workPart->Expressions()->CreateSystemExpressionWithUnits("0", dynamic_cast<NXOpen::Unit *>(m_secondaryOffset->Units()));
    m_secondaryOffset->SetExpressionObject(m_secondaryOffsetExp);

    NXOpen::Expression *m_conicConstantExp = workPart->Expressions()->CreateSystemExpression("-0.5");
    m_conicConstant->SetExpressionObject(m_conicConstantExp);
}

void TelescopeMirrorUI::PopulateUIFromCustomFeatureData(NXOpen::Features::CustomFeatureData * cfData)
{
    NXOpen::Expression* exp;
    NXOpen::Features::CustomExpressionAttribute* m_radiusOfCurvatureAttrib = cfData->CustomExpressionAttributeByName("m_radiusOfCurvature");
    exp = dynamic_cast<NXOpen::Expression*>(m_radiusOfCurvatureAttrib->Value());
    m_radiusOfCurvature->SetExpressionObject(exp);
    m_radiusOfCurvaturecache = exp->Value();
    m_radiusOfCurvatureCached = true;

    NXOpen::Features::CustomExpressionAttribute* m_conicConstantAttrib = cfData->CustomExpressionAttributeByName("m_conicConstant");
    exp = dynamic_cast<NXOpen::Expression*>(m_conicConstantAttrib->Value());
    m_conicConstant->SetExpressionObject(exp);
    m_conicConstantcache = exp->Value();
    m_conicConstantCached = true;

    NXOpen::Features::CustomExpressionAttribute* m_baseDiaAttrib = cfData->CustomExpressionAttributeByName("m_baseDia");
    exp = dynamic_cast<NXOpen::Expression*>(m_baseDiaAttrib->Value());
    m_baseDia->SetExpressionObject(exp);
    m_baseDiacache = exp->Value();
    m_baseDiaCached = true;

    NXOpen::Features::CustomExpressionAttribute* m_thickAtCenterAttrib = cfData->CustomExpressionAttributeByName("m_thickAtCenter");
    exp = dynamic_cast<NXOpen::Expression*>(m_thickAtCenterAttrib->Value());
    m_thickAtCenter->SetExpressionObject(exp);
    m_thickAtCentercache = exp->Value();
    m_thickAtCenterCached = true;

    NXOpen::Features::CustomExpressionAttribute* m_primaryLenAttrib = cfData->CustomExpressionAttributeByName("m_primaryLen");
    exp = dynamic_cast<NXOpen::Expression*>(m_primaryLenAttrib->Value());
    m_primaryLen->SetExpressionObject(exp);
    m_primaryLencache = exp->Value();
    m_primaryLenCached = true;

    NXOpen::Features::CustomExpressionAttribute* m_secondaryLenAttrib = cfData->CustomExpressionAttributeByName("m_secondaryLen");
    exp = dynamic_cast<NXOpen::Expression*>(m_secondaryLenAttrib->Value());
    m_secondaryLen->SetExpressionObject(exp);
    m_secondaryLencache = exp->Value();
    m_secondaryLenCached = true;

    NXOpen::Features::CustomExpressionAttribute* m_primaryOffsetAttrib = cfData->CustomExpressionAttributeByName("m_primaryOffset");
    exp = dynamic_cast<NXOpen::Expression*>(m_primaryOffsetAttrib->Value());
    m_primaryOffset->SetExpressionObject(exp);
    m_primaryOffsetcache = exp->Value();
    m_primaryOffsetCached = true;

    NXOpen::Features::CustomExpressionAttribute* m_secondaryOffsetAttrib = cfData->CustomExpressionAttributeByName("m_secondaryOffset");
    exp = dynamic_cast<NXOpen::Expression*>(m_secondaryOffsetAttrib->Value());
    m_secondaryOffset->SetExpressionObject(exp);
    m_secondaryOffsetcache = exp->Value();
    m_secondaryOffsetCached = true;

    std::vector<NXOpen::TaggedObject *> SelectedObjVec;
    NXOpen::Features::CustomTagAttribute* m_locationAttrib = cfData->CustomTagAttributeByName("m_location");
    SelectedObjVec.push_back(m_locationAttrib->Value());
    m_location->SetSelectedObjects(SelectedObjVec);
    SelectedObjVec.clear();

    NXOpen::Features::CustomTagAttribute* m_directionAttrib = cfData->CustomTagAttributeByName("m_direction");
    SelectedObjVec.push_back(m_directionAttrib->Value());
    m_direction->SetSelectedObjects(SelectedObjVec);
    SelectedObjVec.clear();

    NXOpen::Features::CustomTagAttribute* m_primaryDirAttrib = cfData->CustomTagAttributeByName("m_primaryDir");
    SelectedObjVec.push_back(m_primaryDirAttrib->Value());
    m_primaryDir->SetSelectedObjects(SelectedObjVec);
    SelectedObjVec.clear();

    NXOpen::Features::CustomLogicalAttribute* m_SuppressTrimAttrib = cfData->CustomLogicalAttributeByName("m_SuppressTrim");
    m_SuppressTrim->SetValue(m_SuppressTrimAttrib->Value());

    NXOpen::Features::CustomLogicalAttribute* m_SuppressAperAttrib = cfData->CustomLogicalAttributeByName("m_SuppressAper");
    m_SuppressAper->SetValue(m_SuppressAperAttrib->Value());
    
    NXOpen::Features::CustomStringAttribute* m_aperatureShapeAttrib = cfData->CustomStringAttributeByName("m_aperatureShape");
    m_aperatureShapecache = m_aperatureShapeAttrib->Value();
    m_aperatureShapeCached = true;
    m_aperatureShape->SetValueAsString(m_aperatureShapeAttrib->Value());
}
