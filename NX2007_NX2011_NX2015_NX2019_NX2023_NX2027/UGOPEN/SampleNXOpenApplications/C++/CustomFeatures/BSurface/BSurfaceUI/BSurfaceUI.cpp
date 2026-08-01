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
#include "BSurfaceUI.hpp"

#include <NXOpen/Features_CustomFeatureBuilder.hxx>

#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/Features_Feature.hxx>

#include <NXOpen/Features_CustomFeatureDataCollection.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>

#include <NXOpen/Features_CustomAttributeCollection.hxx>
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomTagAttribute.hxx>
#include <NXOpen/Features_CustomLogicalAttribute.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>

#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/BlockStyler_SpecifyPoint.hxx>

using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(BSurfaceUI::theSession) = NULL;
UI *(BSurfaceUI::theUI) = NULL;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
BSurfaceUI::BSurfaceUI()
{
    try
    {
        // Initialize the NX Open C++ API environment
        BSurfaceUI::theSession = NXOpen::Session::GetSession();
        BSurfaceUI::theUI = UI::GetUI();

        customFeatureManager = theSession->CustomFeatureClassManager();
        editedFeature = customFeatureManager->GetEditedCustomFeature();
        cfClass = customFeatureManager->GetClassFromName("NXOpen::CustomFeature::BSurface");

        theDlxFileName = "BSurfaceUI.dlx";
        theDialog = BSurfaceUI::theUI->CreateDialog(theDlxFileName);
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &BSurfaceUI::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &BSurfaceUI::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &BSurfaceUI::update_cb));
        theDialog->AddFilterHandler(make_callback(this, &BSurfaceUI::filter_cb));
        theDialog->AddInitializeHandler(make_callback(this, &BSurfaceUI::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &BSurfaceUI::dialogShown_cb));
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
BSurfaceUI::~BSurfaceUI()
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
    BSurfaceUI *theBSurfaceUI = NULL;
    try
    {
        theBSurfaceUI = new BSurfaceUI();
        // The following method shows the dialog immediately
        theBSurfaceUI->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        BSurfaceUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if(theBSurfaceUI != NULL)
    {
        delete theBSurfaceUI;
        theBSurfaceUI = NULL;
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
        BSurfaceUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int BSurfaceUI::Show()
{
    try
    {
        Session *theSession = Session::GetSession();
        NXOpen::Features::CustomFeatureClassManager * mgr = theSession->CustomFeatureClassManager();
        NXOpen::Features::CustomFeature* editedFeature = mgr->GetEditedCustomFeature();
        BlockDialog::DialogMode mode = editedFeature != NULL ? BlockDialog::DialogModeEdit : BlockDialog::DialogModeCreate;
        theDialog->Show(mode);
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        BSurfaceUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void BSurfaceUI::initialize_cb()
{
    try
    {
        group0 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group0"));
        nu = dynamic_cast<NXOpen::BlockStyler::IntegerBlock*>(theDialog->TopBlock()->FindBlock("nu"));
        ku = dynamic_cast<NXOpen::BlockStyler::IntegerBlock*>(theDialog->TopBlock()->FindBlock("ku"));
        group = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group"));
        nv = dynamic_cast<NXOpen::BlockStyler::IntegerBlock*>(theDialog->TopBlock()->FindBlock("nv"));
        kv = dynamic_cast<NXOpen::BlockStyler::IntegerBlock*>(theDialog->TopBlock()->FindBlock("kv"));
        Poles = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("Poles"));
        list0 = dynamic_cast<NXOpen::BlockStyler::SetList*>(theDialog->TopBlock()->FindBlock("list0"));
        
        if (editedFeature == NULL)
        {
            list0->AddNewSet(true);
        }
        else
        {
            NXOpen::Features::CustomFeatureData *cfData = editedFeature->FeatureData();
            NXOpen::Features::CustomTagArrayAttribute* pointsAttrib = cfData->CustomTagArrayAttributeByName("m_poles");
            std::vector<NXOpen::TaggedObject*> pointTagArray = pointsAttrib->GetValues();

            //Set Points in the Custom Feature Data
            for (int i = 0; i < pointTagArray.size(); ++i)
            {
                NXOpen::BlockStyler::CompositeBlock* block = dynamic_cast<NXOpen::BlockStyler::CompositeBlock*>(list0->AddNewSet(true));
                std::vector< NXOpen::BlockStyler::UIBlock*> blocks = block->GetBlocks();

                NXOpen::BlockStyler::SpecifyPoint* blockpointBlock = dynamic_cast<NXOpen::BlockStyler::SpecifyPoint*>(blocks[1]);
                std::vector<NXOpen::TaggedObject*> ithPointTagArray;
                ithPointTagArray.push_back(pointTagArray[i]);
                blockpointBlock->SetSelectedObjects(ithPointTagArray);

                NXOpen::NXString name = " Point :- ";
                NXOpen::NXString pointCount = std::to_string(i);
                name += pointCount;
                std::vector<NXOpen::NXString> text;
                text.push_back(name);
                list0->SetItemText(block, text);
            }


        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        BSurfaceUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void BSurfaceUI::dialogShown_cb()
{
    try
    {
        if (editedFeature != NULL)
        {
            NXOpen::Features::CustomFeatureData *cfData = editedFeature->FeatureData();
            NXOpen::Features::CustomIntegerAttribute* nuAttrib = cfData->CustomIntegerAttributeByName("m_nu");
            NXOpen::Features::CustomIntegerAttribute* nvAttrib = cfData->CustomIntegerAttributeByName("m_nv");
            NXOpen::Features::CustomIntegerAttribute* kuAttrib = cfData->CustomIntegerAttributeByName("m_ku");
            NXOpen::Features::CustomIntegerAttribute* kvAttrib = cfData->CustomIntegerAttributeByName("m_kv");

            this->nu->SetValue(nuAttrib->Value());
            this->nv->SetValue(nvAttrib->Value());
            this->ku->SetValue(kuAttrib->Value());
            this->kv->SetValue(kvAttrib->Value());
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        BSurfaceUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int BSurfaceUI::apply_cb()
{
    int errorCode = 0;
    Features::CustomFeatureBuilder *customFeatureBuilder = NULL;
    try
    {
        Session *theSession = Session::GetSession();

        NXOpen::Part *workPart(theSession->Parts()->Work());

        std::vector<NXOpen::Features::CustomAttribute*> attrs(0);

        NXOpen::Features::CustomFeatureData *cfData = NULL;

        customFeatureBuilder = workPart->Features()->CreateCustomFeatureBuilder(editedFeature);

        NXOpen::Features::CustomTagArrayAttribute* pointsAttrib = NULL;
        NXOpen::Features::CustomIntegerAttribute* nuAttrib = NULL;
        NXOpen::Features::CustomIntegerAttribute* nvAttrib = NULL;
        NXOpen::Features::CustomIntegerAttribute* kuAttrib = NULL;
        NXOpen::Features::CustomIntegerAttribute* kvAttrib = NULL;

        if (editedFeature == NULL)
        {
            // Create attributes
            NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
            NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

            std::vector<NXOpen::Features::CustomAttribute::Property> attributeProperties;
            attributeProperties.push_back(NXOpen::Features::CustomAttribute::Property::PropertyMandatoryInput);

            pointsAttrib = attribCollection->CreateCustomTagArrayAttribute("m_poles", attributeProperties);
            attrs.push_back(pointsAttrib);
            
            // nu : number of poles in U direction
            nuAttrib = dynamic_cast<NXOpen::Features::CustomIntegerAttribute*>(attribCollection->CreateCustomIntegerAttribute("m_nu", attributeProperties));
            attrs.push_back(nuAttrib);

            // nv : number of poles in V direction
            nvAttrib = dynamic_cast<NXOpen::Features::CustomIntegerAttribute*>(attribCollection->CreateCustomIntegerAttribute("m_nv", attributeProperties));
            attrs.push_back(nvAttrib);

            // ku : order in U direction
            kuAttrib = dynamic_cast<NXOpen::Features::CustomIntegerAttribute*>(attribCollection->CreateCustomIntegerAttribute("m_ku", attributeProperties));
            attrs.push_back(kuAttrib);


            // ku : order in U direction
            kvAttrib = dynamic_cast<NXOpen::Features::CustomIntegerAttribute*>(attribCollection->CreateCustomIntegerAttribute("m_kv", attributeProperties));
            attrs.push_back(kvAttrib);
            
            // Create custom feature data to store attributes
            cfData = workPart->Features()->CustomFeatureDataCollection()->CreateData(cfClass, attrs);
        }
        else
        {
            cfData = editedFeature->FeatureData();
            
            pointsAttrib = cfData->CustomTagArrayAttributeByName("m_poles");
            nuAttrib = cfData->CustomIntegerAttributeByName("m_nu");
            nvAttrib = cfData->CustomIntegerAttributeByName("m_nv");
            kuAttrib = cfData->CustomIntegerAttributeByName("m_ku");
            kvAttrib = cfData->CustomIntegerAttributeByName("m_kv");

        }

        std::vector< NXOpen::BlockStyler::UIBlock*> itemList = this->list0->GetItems();

        std::vector<NXOpen::TaggedObject*> pointTagArray;
        for (int count = 0; count < itemList.size(); ++count)
        {
            tag_t blockTag = itemList[count]->Tag();

            NXOpen::TaggedObject* obj = NXOpen::NXObjectManager::Get(blockTag);

            NXOpen::BlockStyler::CompositeBlock* block = dynamic_cast<NXOpen::BlockStyler::CompositeBlock*>(obj);

            std::vector< NXOpen::BlockStyler::UIBlock*> blocks = block->GetBlocks();

            NXOpen::BlockStyler::SpecifyPoint* blockpointBlock = dynamic_cast<NXOpen::BlockStyler::SpecifyPoint*>(blocks[1]);

            std::vector< NXOpen::TaggedObject*> selectedObject = blockpointBlock->GetSelectedObjects();

            if (selectedObject.size() != 0)
            {
                pointTagArray.push_back(selectedObject[0]);
            }         
        }

        pointsAttrib->SetValues(pointTagArray);
        nuAttrib->SetValue(this->nu->Value());
        nvAttrib->SetValue(this->nv->Value());
        kuAttrib->SetValue(this->ku->Value());
        kvAttrib->SetValue(this->kv->Value());

        int nuValue = this->nu->Value();
        int nvValue = this->nv->Value();

        if (nuValue < 2 || 
            nvValue < 2 ||
            this->ku->Value() > nuValue||
            this->kv->Value() > nvValue ||
            itemList.size() != nuValue*nvValue)
        {          
            BSurfaceUI::theUI->NXMessageBox()->Show("Bsurf Feature Error", NXOpen::NXMessageBox::DialogTypeError, "Insufficient points are defined, Please provide sufficient number of points");
            return 1;
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
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        BSurfaceUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int BSurfaceUI::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == nu)
        {
        //---------Enter your code here-----------
        }
        else if(block == ku)
        {
        //---------Enter your code here-----------
        }
        else if(block == nv)
        {
        //---------Enter your code here-----------
        }
        else if(block == kv)
        {
        //---------Enter your code here-----------
        }
        else if(block == list0)
        {
            std::vector< NXOpen::BlockStyler::UIBlock*> itemList = list0->GetItems();

            for (int count = 0; count < itemList.size(); ++count)
            {
                NXOpen::NXString name = " Point :- ";
                NXOpen::NXString pointCount = std::to_string(count);
                name += pointCount;
                std::vector<NXOpen::NXString> text;
                text.push_back(name);
                list0->SetItemText(itemList[count], text);
            }
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        BSurfaceUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int BSurfaceUI::ok_cb()
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
        BSurfaceUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: filter_cb
//------------------------------------------------------------------------------
int BSurfaceUI::filter_cb(NXOpen::BlockStyler::UIBlock* block, NXOpen::TaggedObject* selectObject)
{
    return(UF_UI_SEL_ACCEPT);
}
//------------------------------------------------------------------------------
//SetList specific callbacks
//------------------------------------------------------------------------------
//int BSurfaceUI::AddCallback (NXOpen::BlockStyler::SetList* set_list)
//{
//}

//int BSurfaceUI::DeleteCallback(NXOpen::BlockStyler::SetList* set_list, NXOpen::BlockStyler::SetList::UIBlock* blockToDelete)
//{
//}

//int BSurfaceUI::ReorderCallback(NXOpen::BlockStyler::SetList* set_list, NXOpen::BlockStyler::UIBlock* reorderedBlock, int oldPosition, int newPosition)
//{
//}

//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Function Name: GetBlockProperties
//Description: Returns the propertylist of the specified BlockID
//------------------------------------------------------------------------------
PropertyList* BSurfaceUI::GetBlockProperties(const char *blockID)
{
    return theDialog->GetBlockProperties(blockID);
}
