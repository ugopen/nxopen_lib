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
#include "PolygonalHoleUI.hpp"
#include <NXOpen/Features_CustomFeatureBuilder.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/UnitCollection.hxx>
#include <NXOpen/Unit.hxx>
#include <NXOpen/ExpressionCollection.hxx>
#include <NXOpen/Expression.hxx>

#include <NXOpen/Features_CustomAttributeCollection.hxx>
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeature.hxx>
#include <NXOpen/Direction.hxx>
#include <NXOpen/Point.hxx>
#include <NXOpen/Body.hxx>

#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/Features_CustomFeature.hxx>

#include <NXOpen/Features_CustomFeatureDataCollection.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>

#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>

using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(PolygonalHoleUI::theSession) = NULL;
UI *(PolygonalHoleUI::theUI) = NULL;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
PolygonalHoleUI::PolygonalHoleUI()
{
    try
    {
        // Initialize the NX Open C++ API environment
        PolygonalHoleUI::theSession = NXOpen::Session::GetSession();
        PolygonalHoleUI::theUI = UI::GetUI();
        theDlxFileName = "PolygonalHoleUI.dlx";
        theDialog = PolygonalHoleUI::theUI->CreateDialog(theDlxFileName);

        // Get custom feature manager from session.
        NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();
        
        cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::SamplePolygonalHole");

        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &PolygonalHoleUI::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &PolygonalHoleUI::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &PolygonalHoleUI::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &PolygonalHoleUI::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &PolygonalHoleUI::dialogShown_cb));
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
PolygonalHoleUI::~PolygonalHoleUI()
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
//        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
//        2) Invoke the Shared Library through File->Execute->NX Open menu.
//
//------------------------------------------------------------------------------
extern "C" DllExport void  ufusr(char *param, int *retcod, int param_len)
{
    PolygonalHoleUI *thePolygonalHoleUI = NULL;
    try
    {
        thePolygonalHoleUI = new PolygonalHoleUI();
        // The following method shows the dialog immediately
        thePolygonalHoleUI->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        PolygonalHoleUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if(thePolygonalHoleUI != NULL)
    {
        delete thePolygonalHoleUI;
        thePolygonalHoleUI = NULL;
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
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        PolygonalHoleUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int PolygonalHoleUI::Show()
{
    try
    {
        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();
        BlockDialog::DialogMode mode = editedFeature != NULL ? BlockDialog::DialogModeEdit : BlockDialog::DialogModeCreate;
        theDialog->Show(mode);
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        PolygonalHoleUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void PolygonalHoleUI::initialize_cb()
{
    try
    {
        NXOpen::Part *workPart(theSession->Parts()->Work());

        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();

        PolygonDefinition = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("PolygonDefinition"));
        polygonPoint = dynamic_cast<NXOpen::BlockStyler::SpecifyPoint*>(theDialog->TopBlock()->FindBlock("polygonPoint"));
        polygonDiameter = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("polygonDiameter"));
        numSides = dynamic_cast<NXOpen::BlockStyler::IntegerBlock*>(theDialog->TopBlock()->FindBlock("numSides"));
        holeDefinitio = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("holeDefinitio"));
        holeDepth = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("holeDepth"));
        holeDirection = dynamic_cast<NXOpen::BlockStyler::SpecifyVector*>(theDialog->TopBlock()->FindBlock("holeDirection"));
        targetBody = dynamic_cast<NXOpen::BlockStyler::BodyCollector*>(theDialog->TopBlock()->FindBlock("targetBody"));

        if (editedFeature == NULL)
        {
            NXOpen::Unit *unit0(dynamic_cast<NXOpen::Unit *>(workPart->UnitCollection()->FindObject("MilliMeter")));
            NXOpen::Expression *polygonDiameterexp = workPart->Expressions()->CreateSystemExpressionWithUnits("5", unit0);
            polygonDiameter->SetExpressionObject(polygonDiameterexp);

            NXOpen::Expression *holeDepthExp = workPart->Expressions()->CreateSystemExpressionWithUnits("5", unit0);
            holeDepth->SetExpressionObject(holeDepthExp);

            numSides->SetValue(3);
        }
        else
        {
            NXOpen::Features::CustomFeature *cfFeature = (NXOpen::Features::CustomFeature *)editedFeature;

            NXOpen::Features::CustomFeatureData* cfData = cfFeature->FeatureData();

            PopulateUIFromCustomFeatureData(cfData);
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        PolygonalHoleUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void PolygonalHoleUI::dialogShown_cb()
{
    try
    {
        if (polygonDepthCached)
        {
            holeDepth->SetValue(polygonDepthCache);
            polygonDepthCached = false;
        }
        if (polygonSidesCached)
        {
            numSides->SetValue(polygonSidesCache);
            polygonSidesCached = false;
        }
        if (polygonDiameterCached)
        {
            polygonDiameter->SetValue(polygonDiameterCache);
            polygonDiameterCached = false;
        }
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        PolygonalHoleUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

void PolygonalHoleUI::CreateFeatureAttributes(std::vector<NXOpen::Features::CustomAttribute*> &attrs)
{
    NXOpen::Part *workPart(theSession->Parts()->Work());

    NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
    NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

    std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;

    // Number of side for polygon attribute
    NXOpen::Features::CustomExpressionAttribute* m_polygonSidesAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_polygonSides", attributeProperties));
    attrs.push_back(m_polygonSidesAttrib);
    
    // Diameter attribute            
    NXOpen::Features::CustomExpressionAttribute* polygonDiameterAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_polygonDiameter", attributeProperties));
    attrs.push_back(polygonDiameterAttrib);
   
    // Depth attribute
    NXOpen::Features::CustomExpressionAttribute* holeDepthAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("m_holeDepth", attributeProperties));
    attrs.push_back(holeDepthAttrib);
    
    // Hole attribute
    attributeProperties.push_back(NXOpen::Features::CustomAttribute::Property::PropertyMandatoryInput);
    NXOpen::Features::CustomTagAttribute* holeDirectionAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_holeDirection", attributeProperties));
    attrs.push_back(holeDirectionAttrib);

    // polygonPoint attribute
    NXOpen::Features::CustomTagAttribute* polygonPointAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_polygonPoint", attributeProperties));
    attrs.push_back(polygonPointAttrib);

    // TargetBody attribute
    attributeProperties.push_back(NXOpen::Features::CustomAttribute::PropertyIsReferencingTargetBody);
    NXOpen::Features::CustomTagAttribute* targetBodyAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("m_targetBody", attributeProperties));
    attrs.push_back(targetBodyAttrib);
}

void PolygonalHoleUI::PopulateAttributeValues(NXOpen::Features::CustomFeatureData * cfData)
{
    NXOpen::Part *workPart(theSession->Parts()->Work());

    Features::CustomExpressionAttribute *m_polygonSidesAttrib = cfData->CustomExpressionAttributeByName("m_polygonSides");
    NXOpen::Expression* polygoneSidesExp = m_polygonSidesAttrib->Value();
    if (polygoneSidesExp == NULL)
    {
        polygoneSidesExp = workPart->Expressions()->CreateSystemExpression("3");
    }
    polygoneSidesExp->SetValue(this->numSides->Value());
    m_polygonSidesAttrib->SetValue(polygoneSidesExp);
     
    NXOpen::Features::CustomExpressionAttribute* polygonDiameterAttrib = cfData->CustomExpressionAttributeByName("m_polygonDiameter");
    polygonDiameterAttrib->SetValue(dynamic_cast<NXOpen::Expression*>(this->polygonDiameter->ExpressionObject()));

    // Depth Expression     
    NXOpen::Features::CustomExpressionAttribute* holeDepthAttrib = cfData->CustomExpressionAttributeByName("m_holeDepth");
    holeDepthAttrib->SetValue(dynamic_cast<NXOpen::Expression*>(this->holeDepth->ExpressionObject()));
  
    std::vector<NXOpen::TaggedObject *> SelectedObjVec;

    // Hole Direction
    NXOpen::Features::CustomTagAttribute* holeDirectionAttrib = cfData->CustomTagAttributeByName("m_holeDirection");
    SelectedObjVec = this->holeDirection->GetSelectedObjects();
    if (SelectedObjVec.size() == 1)
    {
        holeDirectionAttrib->SetValue(SelectedObjVec[0]);
    }
    SelectedObjVec.clear();

    // polygonPoint 
    NXOpen::Features::CustomTagAttribute* polygonPointAttrib = cfData->CustomTagAttributeByName("m_polygonPoint");
    SelectedObjVec = this->polygonPoint->GetSelectedObjects();
    if (SelectedObjVec.size() == 1)
    {
        polygonPointAttrib->SetValue(SelectedObjVec[0]);
    }
    SelectedObjVec.clear();

    // TargetBody 
    NXOpen::Features::CustomTagAttribute* targetBodyAttrib = cfData->CustomTagAttributeByName("m_targetBody");
    SelectedObjVec = this->targetBody->GetSelectedObjects();
    if (SelectedObjVec.size() == 1)
    {
        targetBodyAttrib->SetValue(SelectedObjVec[0]);
    }
    SelectedObjVec.clear();
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int PolygonalHoleUI::apply_cb()
{
    int errorCode = 0;
    Features::CustomFeatureBuilder *customFeatureBuilder = NULL;
    try
    {
        NXOpen::Part *workPart(theSession->Parts()->Work());        

        NXOpen::Features::CustomFeatureData *cfData = NULL;
        
        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();

        customFeatureBuilder = workPart->Features()->CreateCustomFeatureBuilder(editedFeature);
                
        if (editedFeature == NULL)
        {
            std::vector<NXOpen::Features::CustomAttribute*> attrs(0);
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

        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        if (customFeatureBuilder != NULL)
        {
            customFeatureBuilder->Destroy();
            customFeatureBuilder = NULL;
        }
        PolygonalHoleUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int PolygonalHoleUI::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == polygonPoint)
        {
        //---------Enter your code here-----------
        }
        else if(block == polygonDiameter)
        {
        //---------Enter your code here-----------
        }
        else if(block == numSides)
        {
        //---------Enter your code here-----------
        }
        else if(block == holeDepth)
        {
        //---------Enter your code here-----------
        }
        else if(block == holeDirection)
        {
        //---------Enter your code here-----------
        }
        else if(block == targetBody)
        {
        //---------Enter your code here-----------
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        PolygonalHoleUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int PolygonalHoleUI::ok_cb()
{
    int errorCode = 0;
    try
    {
        errorCode = apply_cb();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        PolygonalHoleUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Function Name: GetBlockProperties
//Description: Returns the propertylist of the specified BlockID
//------------------------------------------------------------------------------
PropertyList* PolygonalHoleUI::GetBlockProperties(const char *blockID)
{
    return theDialog->GetBlockProperties(blockID);
}

void PolygonalHoleUI::PopulateUIFromCustomFeatureData(NXOpen::Features::CustomFeatureData* cfData)
{
    Features::CustomExpressionAttribute *m_polygonSidesAttrib = cfData->CustomExpressionAttributeByName("m_polygonSides");
    NXOpen::Expression* polygoneSidesExp = m_polygonSidesAttrib->Value();
    numSides->SetValue((int)polygoneSidesExp->Value());
    polygonSidesCache = (int)polygoneSidesExp->Value();
    polygonSidesCached = true;

    NXOpen::Features::CustomExpressionAttribute* polygonDiameterAttrib = cfData->CustomExpressionAttributeByName("m_polygonDiameter");
    NXOpen::Expression* polygoneDiaExp = polygonDiameterAttrib->Value();
    polygonDiameter->SetExpressionObject(polygoneDiaExp);
    polygonDiameterCache = polygoneDiaExp->Value();
    polygonDiameterCached = true;
     
    NXOpen::Features::CustomExpressionAttribute* holeDepthAttrib = cfData->CustomExpressionAttributeByName("m_holeDepth");
    NXOpen::Expression* holeDepthExp = holeDepthAttrib->Value();
    holeDepth->SetExpressionObject(holeDepthExp);
    polygonDepthCache = holeDepthExp->Value();
    polygonDepthCached = true;

    std::vector<NXOpen::TaggedObject *> SelectedObjVec;

    // Hole Direction
    NXOpen::Features::CustomTagAttribute* holeDirectionAttrib = cfData->CustomTagAttributeByName("m_holeDirection");
    NXOpen::Direction* holeDirection1 = dynamic_cast<NXOpen::Direction*>(holeDirectionAttrib->Value());
    if (holeDirection1 != NULL)
    {
        SelectedObjVec.push_back(holeDirection1);
        holeDirection->SetSelectedObjects(SelectedObjVec);
    }
    SelectedObjVec.clear();

    // polygonPoint 
    NXOpen::Features::CustomTagAttribute* polygonPointAttrib = cfData->CustomTagAttributeByName("m_polygonPoint");
    NXOpen::Point* polygonPoint1 = dynamic_cast<NXOpen::Point*>(polygonPointAttrib->Value());
    if (polygonPoint1 != NULL)
    {
        SelectedObjVec.push_back(polygonPoint1);
        polygonPoint->SetSelectedObjects(SelectedObjVec);
    }
    SelectedObjVec.clear();

    // TargetBody 
    NXOpen::Features::CustomTagAttribute* targetBodyAttrib = cfData->CustomTagAttributeByName("m_targetBody");
    NXOpen::Body* body = dynamic_cast<NXOpen::Body*>(targetBodyAttrib->Value());
    
    if (body != NULL)
    {
        SelectedObjVec.push_back(body);
        targetBody->SetSelectedObjects(SelectedObjVec);
    }

    SelectedObjVec.clear();
}
