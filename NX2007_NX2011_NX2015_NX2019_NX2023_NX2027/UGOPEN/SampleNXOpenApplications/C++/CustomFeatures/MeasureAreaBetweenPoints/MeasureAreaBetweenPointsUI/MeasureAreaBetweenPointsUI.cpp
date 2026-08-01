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
#include "MeasureAreaBetweenPointsUI.hpp"
#include <NXOpen/Features_CustomFeatureBuilder.hxx>
#include <NXOpen/Features_CustomAttribute.hxx>
#include <NXOpen/Features_CustomFeatureClass.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/Session.hxx>
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
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Features_CustomExpressionAttribute.hxx>
#include <NXOpen/BlockStyler_ExpressionBlock.hxx>
#include <NXOpen/UnitCollection.hxx>
#include <NXOpen/ExpressionCollection.hxx>
#include <NXOpen/Unit.hxx>
#include <NXOpen/Point.hxx>
#include <NXOpen/BlockStyler_SpecifyPoint.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/BlockStyler_CompositeBlock.hxx>



using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(MeasureAreaBetweenPointsUI::theSession) = NULL;
UI *(MeasureAreaBetweenPointsUI::theUI) = NULL;

// Utility functions

NXOpen::Vector3d  VectorBetwenPoints(NXOpen::Point3d &startPoint, NXOpen::Point3d &endPoint)
{
    NXOpen::Vector3d vector;

    vector.X = endPoint.X - startPoint.X;
    vector.Y = endPoint.Y - startPoint.Y;
    vector.Z = endPoint.Z - startPoint.Z;

    return vector;
}

NXOpen::Vector3d VectorCrossProduct(NXOpen::Vector3d &vector1, NXOpen::Vector3d &vector2)
{
    NXOpen::Vector3d NormalVector;

    NormalVector.X = vector1.Y*vector2.Z - vector1.Z*vector2.Y;
    NormalVector.Y = -vector1.X*vector2.Z + vector1.Z*vector2.X;
    NormalVector.Z = vector1.X*vector2.Y - vector1.Y*vector2.X;

    return NormalVector;
}

bool ArePointsCoplaner(std::vector<NXOpen::TaggedObject*> pointsVec)
{
    std::vector<NXOpen::Point3d>point3dVec;

    if (pointsVec.size() < 4)
    {
        return true;
    }

    for (int i = 0; i < pointsVec.size(); ++i)
    {
        NXOpen::Point* point = dynamic_cast<NXOpen::Point*>(pointsVec[i]);

        point3dVec.push_back(point->Coordinates());
    }

    NXOpen::Vector3d v1 = VectorBetwenPoints(point3dVec[0], point3dVec[1]);
    NXOpen::Vector3d v2 = VectorBetwenPoints(point3dVec[0], point3dVec[2]);

    NXOpen::Vector3d vCross = VectorCrossProduct(v1, v2);

    for (int i = 3; i < point3dVec.size(); ++i)
    {
        NXOpen::Vector3d vi0 = VectorBetwenPoints(point3dVec[0], point3dVec[i]);

        double det = vi0.X* vCross.X - vi0.Y* (-vCross.Y) + vi0.Z* vCross.Z;

        det = det < 0.0 ? -det : det;

        if (det > 0.01)
        {
            return false;
        }
    }
    return true;
}

//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
MeasureAreaBetweenPointsUI::MeasureAreaBetweenPointsUI()
{
    try
    {
        // Initialize the NX Open C++ API environment
        MeasureAreaBetweenPointsUI::theSession = NXOpen::Session::GetSession();
        MeasureAreaBetweenPointsUI::theUI = UI::GetUI();

        customFeatureManager = theSession->CustomFeatureClassManager();
        editedFeature = customFeatureManager->GetEditedCustomFeature();
        cfClass = customFeatureManager->GetClassFromName("NXOpen::CustomFeature::MeasureAreaBetweenPoints");


        theDlxFileName = "MeasureAreaBetweenPointsUI.dlx";
        theDialog = MeasureAreaBetweenPointsUI::theUI->CreateDialog(theDlxFileName);
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &MeasureAreaBetweenPointsUI::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &MeasureAreaBetweenPointsUI::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &MeasureAreaBetweenPointsUI::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &MeasureAreaBetweenPointsUI::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &MeasureAreaBetweenPointsUI::dialogShown_cb));
        this->theDialog->AddEnableOKButtonHandler(make_callback(this, &MeasureAreaBetweenPointsUI::CanOkay));
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
MeasureAreaBetweenPointsUI::~MeasureAreaBetweenPointsUI()
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
    MeasureAreaBetweenPointsUI *theMeasureAreaBetweenPointsUI = NULL;
    try
    {
        theMeasureAreaBetweenPointsUI = new MeasureAreaBetweenPointsUI();
        // The following method shows the dialog immediately
        theMeasureAreaBetweenPointsUI->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MeasureAreaBetweenPointsUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if(theMeasureAreaBetweenPointsUI != NULL)
    {
        delete theMeasureAreaBetweenPointsUI;
        theMeasureAreaBetweenPointsUI = NULL;
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
        MeasureAreaBetweenPointsUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int MeasureAreaBetweenPointsUI::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MeasureAreaBetweenPointsUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

std::vector<NXOpen::TaggedObject*> GetSelectedPoints(std::vector< NXOpen::BlockStyler::UIBlock*> &itemList)
{
    std::vector<NXOpen::TaggedObject*> pointTagArray;
    for (int count = 0; count < itemList.size(); ++count)
    {
        NXOpen::BlockStyler::CompositeBlock* block = dynamic_cast<NXOpen::BlockStyler::CompositeBlock*>(itemList[count]);

        std::vector< NXOpen::BlockStyler::UIBlock*> blocks = block->GetBlocks();

        NXOpen::BlockStyler::SpecifyPoint* blockpointBlock = dynamic_cast<NXOpen::BlockStyler::SpecifyPoint*>(blocks[1]);

        std::vector< NXOpen::TaggedObject*> selectedObject = blockpointBlock->GetSelectedObjects();
        
        if (selectedObject.size() > 0 && selectedObject[0] != NULL_TAG)
        {
            pointTagArray.push_back(selectedObject[0]);
        }
    }
    return pointTagArray;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void MeasureAreaBetweenPointsUI::initialize_cb()
{
    try
    {
        Session *theSession = Session::GetSession();

        NXOpen::Part *workPart(theSession->Parts()->Work());

        group0 = dynamic_cast<NXOpen::BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("group0"));
        list0 = dynamic_cast<NXOpen::BlockStyler::SetList*>(theDialog->TopBlock()->FindBlock("list0"));

        if (editedFeature != NULL)
        {
            NXOpen::Features::CustomFeatureData* cfData = editedFeature->FeatureData();

            if (cfData->HasCustomAttribute("Points", NXOpen::Features::CustomAttribute::TypeTagVla))
            {
                Features::CustomTagArrayAttribute *points = cfData->HasCustomAttribute("Points", NXOpen::Features::CustomAttribute::TypeTagVla) ? cfData->CustomTagArrayAttributeByName("Points"):NULL;

                std::vector<NXOpen::TaggedObject*> pointsVec;

                if (points)
                {
                    pointsVec = points->GetValues();
                }

                std::vector< NXOpen::BlockStyler::UIBlock*> itemList = this->list0->GetItems();

                for (int i = 0; i < pointsVec.size(); ++i)
                {
                    NXOpen::BlockStyler::UIBlock* block = list0->AddNewSet(false);

                    NXOpen::BlockStyler::CompositeBlock* compositeBlock = dynamic_cast<NXOpen::BlockStyler::CompositeBlock*>(block);

                    std::vector< NXOpen::BlockStyler::UIBlock*> blocks = compositeBlock->GetBlocks();

                    NXOpen::BlockStyler::SpecifyPoint* blockpointBlock = dynamic_cast<NXOpen::BlockStyler::SpecifyPoint*>(blocks[1]);

                    std::vector<NXOpen::TaggedObject*> pointTagArray;

                    pointTagArray.push_back(pointsVec[i]);

                    blockpointBlock->SetSelectedObjects(pointTagArray);

                    NXOpen::NXString name = "Point";
                    std::vector<NXOpen::NXString> text;
                    text.push_back(name);
                    list0->SetItemText(block, text);                   
                }
            }
        }
        else
        {
            NXOpen::BlockStyler::UIBlock* block = list0->AddNewSet(false);
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MeasureAreaBetweenPointsUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void MeasureAreaBetweenPointsUI::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MeasureAreaBetweenPointsUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int MeasureAreaBetweenPointsUI::apply_cb()
{
    int errorCode = 0;
    
    Features::CustomFeatureBuilder *MeasureAreaBetweenPointsBuilder = NULL;

    try
    {
        Session *theSession = Session::GetSession();

        NXOpen::Part *workPart( theSession->Parts()->Work());
        NXOpen::Features::Feature *nullFeatures_Feature(NULL);

        std::vector<NXOpen::Features::CustomAttribute*> attrs(0);

        NXOpen::Features::CustomFeatureData *MeasureAreaBetweenPointsData = editedFeature != NULL ? editedFeature->FeatureData(): NULL;

        MeasureAreaBetweenPointsBuilder = workPart->Features()->CreateCustomFeatureBuilder(editedFeature);
               
        // Create attributes
        NXOpen::Features::FeatureCollection *featureCollection = workPart->Features();
        NXOpen::Features::CustomAttributeCollection *attribCollection = featureCollection->CustomAttributeCollection();

        std::vector< NXOpen::BlockStyler::UIBlock*> itemList = this->list0->GetItems();

        std::vector<NXOpen::TaggedObject*> pointTagArray = GetSelectedPoints(itemList);

        std::vector<NXOpen::Features::CustomAttribute::Property> attrProp;
                
        NXOpen::Features::CustomTagArrayAttribute* pointsAttrib;
        if (editedFeature == NULL)
        {
            pointsAttrib = attribCollection->CreateCustomTagArrayAttribute("Points", attrProp); 
            attrProp.clear();
            
            attrs.push_back(pointsAttrib);

            MeasureAreaBetweenPointsData = workPart->Features()->CustomFeatureDataCollection()->CreateData(cfClass, attrs);

            MeasureAreaBetweenPointsBuilder->SetFeatureData(MeasureAreaBetweenPointsData);
        }
        else
        {
            pointsAttrib = MeasureAreaBetweenPointsData->HasCustomAttribute("Points", NXOpen::Features::CustomAttribute::TypeTagVla) ? MeasureAreaBetweenPointsData->CustomTagArrayAttributeByName("Points") : NULL;
        }
        
        std::vector<NXOpen::TaggedObject*> oldPointTagArray = pointsAttrib->SetValues(pointTagArray);
        
        NXOpen::Features::Feature *MeasureAreaBetweenPointsFeature = MeasureAreaBetweenPointsBuilder->CommitFeature();

        MeasureAreaBetweenPointsBuilder->Destroy();

        MeasureAreaBetweenPointsBuilder = NULL;
    }
    catch(exception& ex)
    {
        if (MeasureAreaBetweenPointsBuilder != NULL)
        {
            MeasureAreaBetweenPointsBuilder->Destroy();
        }
        //---- Enter your exception handling code here -----
        errorCode = 1;
        MeasureAreaBetweenPointsUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int MeasureAreaBetweenPointsUI::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == list0)
        {          
            NXOpen::BlockStyler::UIBlock* block = list0->FindUpdated();

            std::vector< NXOpen::BlockStyler::UIBlock*> itemList = list0->GetItems(); 

            std::vector<NXOpen::TaggedObject*> pointTagArray = GetSelectedPoints(itemList);

            if (block != NULL)
            {
                if (pointTagArray.size() > 3 && !ArePointsCoplaner(pointTagArray))
                {
                    NXOpen::BlockStyler::CompositeBlock* compositeBlock = dynamic_cast<NXOpen::BlockStyler::CompositeBlock*>(block);

                    std::vector< NXOpen::BlockStyler::UIBlock*> blocks = compositeBlock->GetBlocks();

                    NXOpen::BlockStyler::SpecifyPoint* blockpointBlock = dynamic_cast<NXOpen::BlockStyler::SpecifyPoint*>(blocks[1]);

                    std::vector< NXOpen::TaggedObject*> selectedObject = blockpointBlock->GetSelectedObjects();

                    if (selectedObject.size() > 0 && selectedObject[0] != NULL_TAG)
                    {
                        std::vector<NXOpen::TaggedObject*> pointTagArray;
                        blockpointBlock->SetSelectedObjects(pointTagArray);
                        MeasureAreaBetweenPointsUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeWarning, "Selected point is not planner with first three");
                    }
                }

                NXOpen::NXString name = " Point";
                std::vector<NXOpen::NXString> text;
                text.push_back(name);
                list0->SetItemText(block, text);
            }

        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MeasureAreaBetweenPointsUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

bool MeasureAreaBetweenPointsUI::CanOkay()
{
    std::vector< NXOpen::BlockStyler::UIBlock*> itemList = list0->GetItems();
    std::vector<NXOpen::TaggedObject*> pointTagArray = GetSelectedPoints(itemList);

    return pointTagArray.size() > 2;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int MeasureAreaBetweenPointsUI::ok_cb()
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
        MeasureAreaBetweenPointsUI::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}
//------------------------------------------------------------------------------
//SetList specific callbacks
//------------------------------------------------------------------------------
//int MeasureAreaBetweenPointsUI::AddCallback (NXOpen::BlockStyler::SetList* set_list)
//{
//}

//int MeasureAreaBetweenPointsUI::DeleteCallback(NXOpen::BlockStyler::SetList* set_list, NXOpen::BlockStyler::SetList::UIBlock* blockToDelete)
//{
//}

//int MeasureAreaBetweenPointsUI::ReorderCallback(NXOpen::BlockStyler::SetList* set_list, NXOpen::BlockStyler::UIBlock* reorderedBlock, int oldPosition, int newPosition)
//{
//}

//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Function Name: GetBlockProperties
//Description: Returns the propertylist of the specified BlockID
//------------------------------------------------------------------------------
PropertyList* MeasureAreaBetweenPointsUI::GetBlockProperties(const char *blockID)
{
    return theDialog->GetBlockProperties(blockID);
}
