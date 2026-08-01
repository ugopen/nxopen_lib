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
#include "BlockAndCylinderUI.hpp"
#include <NXOpen/NXException.hxx>
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/Features_CustomFeatureBuilder.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/Features_CustomFeatureDataCollection.hxx>
#include <NXOpen/Features_CustomAttributeCollection.hxx>
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Features_CustomFeatureClassManager.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>
#include <NXOpen/BlockStyler_ExpressionBlock.hxx>
#include <NXOpen/UnitCollection.hxx>
#include <NXOpen/ExpressionCollection.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Unit.hxx>

#include <NXOpen/Features_CustomFeature.hxx>
#include <NXOpen/Direction.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/SmartObject.hxx>

using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(BlockAndCylinderUI::theSession) = NULL;
UI *(BlockAndCylinderUI::theUI) = NULL;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
BlockAndCylinderUI::BlockAndCylinderUI()
{
    try
    {
        // Initialize the NX Open C++ API environment
        BlockAndCylinderUI::theSession = NXOpen::Session::GetSession();
        BlockAndCylinderUI::theUI = UI::GetUI();
        theDlxFileName = "BlockAndCylinderUI.dlx";
        theDialog = BlockAndCylinderUI::theUI->CreateDialog(theDlxFileName);

        BlockAndCylinderUI::customFeatureManager = theSession->CustomFeatureClassManager();
        BlockAndCylinderUI::editedFeature = customFeatureManager->GetEditedCustomFeature();

        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &BlockAndCylinderUI::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &BlockAndCylinderUI::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &BlockAndCylinderUI::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &BlockAndCylinderUI::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &BlockAndCylinderUI::dialogShown_cb));
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
BlockAndCylinderUI::~BlockAndCylinderUI()
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
//
//                a) #if USER_EXIT
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
//             BlockAndCylinderUI->Show_BlockAndCylinderUI();
//        3) Integrate this file with your main application file.
//
//------------------------------------------------------------------------------

extern "C" DllExport void  ufusr(char *param, int *retcod, int param_len)
{
    BlockAndCylinderUI *theBlockAndCylinderUI = NULL;
    try
    {
        theBlockAndCylinderUI = new BlockAndCylinderUI();
        // The following method shows the dialog immediately
        theBlockAndCylinderUI->Show();
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        BlockAndCylinderUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if (theBlockAndCylinderUI != NULL)
    {
        delete theBlockAndCylinderUI;
        theBlockAndCylinderUI = NULL;
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
        BlockAndCylinderUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}


int BlockAndCylinderUI::Show()
{
    try
    {
        editedFeature = customFeatureManager->GetEditedCustomFeature();
        BlockDialog::DialogMode mode = editedFeature != NULL ? BlockDialog::DialogModeEdit : BlockDialog::DialogModeCreate;
        theDialog->Show(mode);
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        BlockAndCylinderUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void BlockAndCylinderUI::initialize_cb()
{
    try
    {
        NXOpen::Part *workPart(theSession->Parts()->Work());

        group = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group"));
        point0 = dynamic_cast<NXOpen::BlockStyler::SpecifyPoint*>(theDialog->TopBlock()->FindBlock("point0"));
        expression0 = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("expression0"));
        expression01 = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("expression01"));
        expression02 = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("expression02"));
        group1 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group1"));
        point01 = dynamic_cast<NXOpen::BlockStyler::SpecifyPoint*>(theDialog->TopBlock()->FindBlock("point01"));
        expression03 = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("expression03"));
        expression04 = dynamic_cast<NXOpen::BlockStyler::ExpressionBlock*>(theDialog->TopBlock()->FindBlock("expression04"));
        vector0 = dynamic_cast<NXOpen::BlockStyler::SpecifyVector*>(theDialog->TopBlock()->FindBlock("vector0"));


        if (editedFeature == NULL)
        {
            NXOpen::Unit *unit0(dynamic_cast<NXOpen::Unit *>(workPart->UnitCollection()->FindObject("MilliMeter")));
            NXOpen::Expression *exp0;
            exp0 = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit0);
            expression0->SetExpressionObject(exp0);

            NXOpen::Expression *exp1;
            exp1 = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit0);
            expression01->SetExpressionObject(exp1);

            NXOpen::Expression *exp2;
            exp2 = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit0);
            expression02->SetExpressionObject(exp2);

            NXOpen::Expression *exp3;
            exp3 = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit0);
            expression03->SetExpressionObject(exp3);

            NXOpen::Expression *exp4;
            exp4 = workPart->Expressions()->CreateSystemExpressionWithUnits("0", unit0);
            expression04->SetExpressionObject(exp4);
        }
        else
        {
            NXOpen::Features::CustomFeatureData* cfData = editedFeature->FeatureData();

            Features::CustomTagAttribute *blockOriginAttrib = cfData->HasCustomAttribute("blockOriginPoint", NXOpen::Features::CustomAttribute::TypeTag) ? cfData->CustomTagAttributeByName("blockOriginPoint"):NULL;


            Features::CustomExpressionAttribute *blockXCAttrib = cfData->HasCustomAttribute("blockXC", NXOpen::Features::CustomAttribute::TypeExpression) ? cfData->CustomExpressionAttributeByName("blockXC") : NULL;
            Features::CustomExpressionAttribute *blockYCAttrib = cfData->HasCustomAttribute("blockYC", NXOpen::Features::CustomAttribute::TypeExpression) ? cfData->CustomExpressionAttributeByName("blockYC") : NULL;
            Features::CustomExpressionAttribute *blockZCAttrib = cfData->HasCustomAttribute("blockZC", NXOpen::Features::CustomAttribute::TypeExpression) ? cfData->CustomExpressionAttributeByName("blockZC") : NULL;

            Features::CustomTagAttribute *cylOriginAttrib = cfData->HasCustomAttribute("cylOriginPoint", NXOpen::Features::CustomAttribute::TypeTag) ? cfData->CustomTagAttributeByName("cylOriginPoint") : NULL;

            Features::CustomExpressionAttribute *cylRadiusAttrib = cfData->HasCustomAttribute("cylRadius", NXOpen::Features::CustomAttribute::TypeExpression) ? cfData->CustomExpressionAttributeByName("cylRadius") : NULL;
            Features::CustomExpressionAttribute *cylHeightAttrib = cfData->HasCustomAttribute("cylHeight", NXOpen::Features::CustomAttribute::TypeExpression) ? cfData->CustomExpressionAttributeByName("cylHeight") : NULL;

            Features::CustomTagAttribute *cylDirVectorAttrib = cfData->HasCustomAttribute("cylDirVector", NXOpen::Features::CustomAttribute::TypeTag) ? cfData->CustomTagAttributeByName("cylDirVector") : NULL;

            std::vector<NXOpen::TaggedObject *> inputVec;

            if (blockOriginAttrib != NULL)
            {
                NXOpen::Point* blockOrigin = dynamic_cast<NXOpen::Point*>(blockOriginAttrib->Value());
                inputVec.push_back(blockOrigin);
                point0->SetSelectedObjects(inputVec);
                inputVec.clear();
            }
            if (blockXCAttrib != NULL)
            {
                NXOpen::Expression* exp = blockXCAttrib->Value();
                this->blockXCCache = exp->Value();
                this->blockXCCached = true;
                expression0->SetExpressionObject(exp);
            }
            if (blockYCAttrib != NULL)
            {
                NXOpen::Expression* exp = blockYCAttrib->Value();
                this->blockYCCache = exp->Value();
                this->blockYCCached = true;
                expression01->SetExpressionObject(exp);
            }
            if (blockZCAttrib != NULL)
            {
                NXOpen::Expression* exp = blockZCAttrib->Value();
                this->blockZCCache = exp->Value();
                this->blockZCCached = true;
                expression02->SetExpressionObject(exp);
            }
            if (cylOriginAttrib != NULL)
            {
                NXOpen::Point* blockOrigin = dynamic_cast<NXOpen::Point*>(cylOriginAttrib->Value());
                inputVec.push_back(blockOrigin);
                point01->SetSelectedObjects(inputVec);
                inputVec.clear();
            }
            if (cylRadiusAttrib != NULL)
            {
                NXOpen::Expression* exp = cylRadiusAttrib->Value();
                this->cylRadiusCache = exp->Value();
                this->cylRadiusCached = true;
                expression03->SetExpressionObject(exp);
            }
            if (cylHeightAttrib != NULL)
            {
                NXOpen::Expression* exp = cylHeightAttrib->Value();
                this->cylHeightCache = exp->Value();
                this->cylHeightCached = true;
                expression04->SetExpressionObject(exp);
            }

            if (cylDirVectorAttrib != NULL)
            {
                NXOpen::Direction* direction = dynamic_cast<NXOpen::Direction*>(cylDirVectorAttrib->Value());
                inputVec.push_back(direction);
                vector0->SetSelectedObjects(inputVec);
                inputVec.clear();
            }

        }
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        BlockAndCylinderUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void BlockAndCylinderUI::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
        if (this->blockXCCached)
        {
            this->expression0->SetValue(this->blockXCCache);
            this->blockXCCached = false;
        }
        if (this->blockYCCached)
        {
            this->expression01->SetValue(this->blockYCCache);
            this->blockYCCached = false;
        }
        if (this->blockZCCached)
        {
            this->expression02->SetValue(this->blockZCCache);
            this->blockZCCached = false;
        }
        if (this->cylRadiusCached)
        {
            this->expression03->SetValue(this->cylRadiusCache);
            this->cylRadiusCached = false;
        }
        if (this->cylHeightCached)
        {
            this->expression04->SetValue(this->cylHeightCache);
            this->cylHeightCached = false;
        }
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        BlockAndCylinderUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int BlockAndCylinderUI::apply_cb()
{
    int errorCode = 0;
    try
    {
        Session *theSession = Session::GetSession();

        NXOpen::Part *workPart(theSession->Parts()->Work()); 
        
        NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

        NXOpen::Features::CustomFeatureClass* cfClass = mgr->GetClassFromName("NXOpen::CustomFeature::BlockAndCylinder");

        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();

        Features::CustomFeatureBuilder *cfbuilder = workPart->Features()->CreateCustomFeatureBuilder(editedFeature);

        NXOpen::Features::CustomFeatureData *cfData = NULL;
        
        if (editedFeature == NULL)
        {
            NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
            NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

            std::vector<NXOpen::Features::CustomAttribute*> attrs(0);
            std::vector<NXOpen::Features::CustomAttribute::Property> properyVector;
            // Create attributes

            // Block Point
            std::vector<NXOpen::TaggedObject *> SelectedObjCollectorVec = this->point0->GetSelectedObjects();

            if (SelectedObjCollectorVec.size() == 1)
            {
                properyVector.push_back(NXOpen::Features::CustomAttribute::Property::PropertyMandatoryInput);
                NXOpen::Features::CustomTagAttribute* blockoriginPointAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("blockOriginPoint", properyVector));
                
                properyVector.clear();
                blockoriginPointAttrib->SetValue(SelectedObjCollectorVec[0]);
                attrs.push_back(blockoriginPointAttrib);
            }
            else
            {
                throw NXOpen::NXException::Create("Please select origin point for block.");
            }
            SelectedObjCollectorVec.clear();
            
            //Block Length
            SelectedObjCollectorVec.push_back(this->expression0->ExpressionObject());
            NXOpen::Expression* expression_1 = dynamic_cast<NXOpen::Expression*>(SelectedObjCollectorVec[0]);
            
            if (expression_1->Value() <= 0.0)
            {
                throw NXOpen::NXException::Create("Block XC must be greater than 0.");
            }

            if (!SelectedObjCollectorVec.empty())
            {
                NXOpen::Features::CustomExpressionAttribute* blockXCAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("blockXC", properyVector));
                blockXCAttrib->SetValue(expression_1);
                attrs.push_back(blockXCAttrib);
            }
            SelectedObjCollectorVec.clear();


            //Block Width
            SelectedObjCollectorVec.push_back(this->expression01->ExpressionObject());
            expression_1 = dynamic_cast<NXOpen::Expression*>(SelectedObjCollectorVec[0]);

            if (expression_1->Value() <= 0.0)
            {
                throw NXOpen::NXException::Create("Block YC must be greater than 0.");
            }

            if (!SelectedObjCollectorVec.empty())
            {
                NXOpen::Features::CustomExpressionAttribute* blockYCAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("blockYC", properyVector));
                blockYCAttrib->SetValue(expression_1);
                attrs.push_back(blockYCAttrib);
            }
            SelectedObjCollectorVec.clear();


            //Block Hieght
            SelectedObjCollectorVec.push_back(this->expression02->ExpressionObject());
            expression_1 = dynamic_cast<NXOpen::Expression*>(SelectedObjCollectorVec[0]);

            if (expression_1->Value() <= 0.0)
            {
                throw NXOpen::NXException::Create("Block ZC must be greater than 0.");
            }
            if (!SelectedObjCollectorVec.empty())
            {
                NXOpen::Features::CustomExpressionAttribute* blockZCAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("blockZC", properyVector));
                blockZCAttrib->SetValue(expression_1);
                attrs.push_back(blockZCAttrib);
            }
            SelectedObjCollectorVec.clear();


            //Cylinder Point
            SelectedObjCollectorVec = this->point01->GetSelectedObjects();
            if (SelectedObjCollectorVec.size() == 1)
            {
                properyVector.push_back(NXOpen::Features::CustomAttribute::Property::PropertyMandatoryInput);
                NXOpen::Features::CustomTagAttribute* cylOriginPointAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("cylOriginPoint", properyVector));
                properyVector.clear();
                cylOriginPointAttrib->SetValue(SelectedObjCollectorVec[0]);
                attrs.push_back(cylOriginPointAttrib);
            }
            else
            {
                throw NXOpen::NXException::Create("Please select origin point for cylinder.");
            }
            SelectedObjCollectorVec.clear();


            //Cylinder Radius
            SelectedObjCollectorVec.push_back(this->expression03->ExpressionObject());
            expression_1 = dynamic_cast<NXOpen::Expression*>(SelectedObjCollectorVec[0]);

            if (expression_1->Value() <= 0.0)
            {
                throw NXOpen::NXException::Create("Cylinder radius must be greater than 0.");
            }

            if (!SelectedObjCollectorVec.empty())
            {
                NXOpen::Features::CustomExpressionAttribute* cylRadiusAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("cylRadius", properyVector));
                cylRadiusAttrib->SetValue(expression_1);
                attrs.push_back(cylRadiusAttrib);
            }
            SelectedObjCollectorVec.clear();

            //Cylinder Height
            SelectedObjCollectorVec.push_back(this->expression04->ExpressionObject());
            expression_1 = dynamic_cast<NXOpen::Expression*>(SelectedObjCollectorVec[0]);

            if (expression_1->Value() <= 0.0)
            {
                throw NXOpen::NXException::Create("Cylinder height must be greater than 0.");
            }

            if (!SelectedObjCollectorVec.empty())
            {
                NXOpen::Features::CustomExpressionAttribute* cylHeightAttrib = dynamic_cast<NXOpen::Features::CustomExpressionAttribute*>(attribCollection->CreateCustomExpressionAttribute("cylHeight", properyVector));
                cylHeightAttrib->SetValue(expression_1);
                attrs.push_back(cylHeightAttrib);
            }
            SelectedObjCollectorVec.clear();


            //Cylinder Direction Cosine
            SelectedObjCollectorVec = this->vector0->GetSelectedObjects();
                        
            if (SelectedObjCollectorVec.size() == 1)
            {
                properyVector.push_back(NXOpen::Features::CustomAttribute::Property::PropertyMandatoryInput);
                NXOpen::Features::CustomTagAttribute* cylDirVectorAttrib = dynamic_cast<NXOpen::Features::CustomTagAttribute*>(attribCollection->CreateCustomTagAttribute("cylDirVector", properyVector));
                properyVector.clear();
                cylDirVectorAttrib->SetValue(SelectedObjCollectorVec[0]);
                attrs.push_back(cylDirVectorAttrib);
            }
            else
            {
                throw NXOpen::NXException::Create("Please select direction for cylinder.");
            }
            SelectedObjCollectorVec.clear();

            cfData = workPart->Features()->CustomFeatureDataCollection()->CreateData(cfClass, attrs);

            // If we create CustomFeatureData in this program, we need to set it back to the builder
            cfbuilder->SetFeatureData(cfData);
        }
        
        NXOpen::Features::Feature *cfFeature = cfbuilder->CommitFeature();

        cfbuilder->Destroy();

    }
    catch (NXOpen::NXException& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        BlockAndCylinderUI::theUI->NXMessageBox()->Show("Block and Cylinder", NXOpen::NXMessageBox::DialogTypeError, ex.Message());
    }
    return errorCode;
}


//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int BlockAndCylinderUI::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        Session *theSession = Session::GetSession();

        NXOpen::Part *workPart(theSession->Parts()->Work());

        std::vector<NXOpen::Features::CustomAttribute*> attrs(0);

        NXOpen::Features::CustomFeatureData *cfData = NULL;

        NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();

        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();

        if (editedFeature != NULL)
        {
            cfData = editedFeature->FeatureData();
        }

        std::vector<NXOpen::TaggedObject *> SelectedObjVec;
        
        if (block == point0&& cfData != NULL)
        {
            Features::CustomTagAttribute *blockOriginAttrib = cfData->HasCustomAttribute("blockOriginPoint", NXOpen::Features::CustomAttribute::TypeTag) ? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("blockOriginPoint")):NULL;
            
            SelectedObjVec = this->point0->GetSelectedObjects();
            if (SelectedObjVec.size() == 1)
            {
                NXOpen::Point* oldPoint = dynamic_cast<NXOpen::Point*>(blockOriginAttrib->Value());
                if (oldPoint != NULL)
                {
                    NXOpen::Point* newPoint = dynamic_cast<NXOpen::Point*>(SelectedObjVec[0]);
                    if (newPoint->Update() == NXOpen::SmartObject::UpdateOptionDontUpdate)
                    {
                        oldPoint->RemoveParameters();
                    }
                    else
                    {
                        oldPoint->ReplaceParameters(newPoint);
                    }
                }
            }
            SelectedObjVec.clear();
        }
        else if (block == point01 && cfData != NULL)
        {
            Features::CustomTagAttribute *cylOriginAttrib = cfData->HasCustomAttribute("cylOriginPoint", NXOpen::Features::CustomAttribute::TypeTag) ? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("cylOriginPoint")):NULL;

            SelectedObjVec = this->point01->GetSelectedObjects();
            if (SelectedObjVec.size() == 1)
            {
                NXOpen::Point* oldPoint = dynamic_cast<NXOpen::Point*>(cylOriginAttrib->Value());
                if (oldPoint != NULL)
                {
                    NXOpen::Point* newPoint = dynamic_cast<NXOpen::Point*>(SelectedObjVec[0]);
                    if (newPoint->Update() == NXOpen::SmartObject::UpdateOptionDontUpdate)
                    {
                        oldPoint->RemoveParameters();
                    }
                    else
                    {
                        oldPoint->ReplaceParameters(newPoint);
                    }
                }
            }
            SelectedObjVec.clear();
        }
        else if (block == expression03)
        {
        //---------Enter your code here-----------
        }
        else if(block == expression04)
        {
        //---------Enter your code here-----------
        }
        else if (block == vector0 && cfData != NULL)
        {
            Features::CustomTagAttribute *cylDirectionAttrib = cfData->HasCustomAttribute("cylDirVector", NXOpen::Features::CustomAttribute::TypeTag) ? dynamic_cast<Features::CustomTagAttribute*> (cfData->CustomTagAttributeByName("cylDirVector")):NULL;

            SelectedObjVec = this->vector0->GetSelectedObjects();
            if (SelectedObjVec.size() == 1)
            {
                cylDirectionAttrib->SetValue(SelectedObjVec[0]);
            }
            SelectedObjVec.clear();
        }
    }
    catch (exception& ex)
    {
        //---- Enter your exception handling code here -----
        BlockAndCylinderUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int BlockAndCylinderUI::ok_cb()
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
        BlockAndCylinderUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Function Name: GetBlockProperties
//Description: Returns the propertylist of the specified BlockID
//------------------------------------------------------------------------------
PropertyList* BlockAndCylinderUI::GetBlockProperties(const char *blockID)
{
    return theDialog->GetBlockProperties(blockID);
}
