//=============================================================================
//
//                   Copyright (c) 2015 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
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
#include "MissingWelds.hpp"
#include <algorithm>
#include <string>
#include <NXOpen/Assemblies_AssemblyManager.hxx>
#include <NXOpen/Assemblies_ClearanceAnalysisBuilder.hxx>
#include <NXOpen/Assemblies_ClearanceSet.hxx>
#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Assemblies_ComponentAssembly.hxx>
#include <NXOpen/BasePart.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/BlockStyler_CompositeBlock.hxx>
#include <NXOpen/BlockStyler_Enumeration.hxx>
#include <NXOpen/BlockStyler_Group.hxx>
#include <NXOpen/BlockStyler_ListBox.hxx>
#include <NXOpen/BlockStyler_PropertyList.hxx>
#include <NXOpen/BlockStyler_SelectObject.hxx>
#include <NXOpen/BlockStyler_TreeListMenu.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/Body.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/DisplayManager.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/PlotManager.hxx>
#include <NXOpen/PlotSourceBuilder.hxx>
#include <NXOpen/PrintPDFBuilder.hxx>
#include <NXOpen/SelectDisplayableObjectList.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/Unit.hxx>
#include <NXOpen/UnitCollection.hxx>
#include <NXOpen/View.hxx>
#include <NXOpen/ViewCollection.hxx>
#include <NXOpen/Weld_ConnectedPart.hxx>
#include <NXOpen/Weld_CustomManager.hxx>
#include <NXOpen/Weld_WeldManager.hxx>

using namespace NXOpen;
using namespace NXOpen::Assemblies;
using namespace NXOpen::BlockStyler;
using namespace NXOpen::Features;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(MissingWelds::theSession) = NULL;
UI *(MissingWelds::theUI) = NULL;

//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
MissingWelds::MissingWelds()
{
    try
    {
        // Initialize the NX Open C++ API environment
        MissingWelds::theSession = Session::GetSession();
        MissingWelds::theUI = UI::GetUI();
        theDlxFileName = "MissingWelds.dlx";
        theDialog = MissingWelds::theUI->CreateDialog(theDlxFileName);
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &MissingWelds::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &MissingWelds::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &MissingWelds::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &MissingWelds::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &MissingWelds::dialogShown_cb));

        theClearanceSet = NULL;
        wasSubNodeCreated = false;

        selectedMissingWeldObjects[0] = NULL;
        selectedMissingWeldObjects[1] = NULL;
    }
    catch(std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
MissingWelds::~MissingWelds()
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
//        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
//        2) Invoke the Shared Library through File->Execute->NX Open menu.
//
//------------------------------------------------------------------------------
extern "C" DllExport void  ufusr(char *param, int *retcod, int param_len)
{
    MissingWelds *theMissingWelds = NULL;
    try
    {
        theMissingWelds = new MissingWelds();
        // The following method shows the dialog immediately
        theMissingWelds->Show();
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
    if(theMissingWelds != NULL)
    {
        delete theMissingWelds;
        theMissingWelds = NULL;
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
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
}

int MissingWelds::Show()
{
    try
    {
        theDialog->Show();
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void MissingWelds::initialize_cb()
{
    try
    {
        missingWeldWizard = dynamic_cast<BlockStyler::Wizard*>(theDialog->TopBlock()->FindBlock("missingWeldWizard"));
        clearanceSetStep = dynamic_cast<BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("clearanceSetStep"));
        compSelection = dynamic_cast<BlockStyler::SelectObject*>(theDialog->TopBlock()->FindBlock("compSelection"));
        resultsStep = dynamic_cast<BlockStyler::Group*>(theDialog->TopBlock()->FindBlock("resultsStep"));
        compDisplay = dynamic_cast<BlockStyler::Enumeration*>(theDialog->TopBlock()->FindBlock("compDisplay"));
        missingWeldObjectsListBox = dynamic_cast<BlockStyler::ListBox*>(theDialog->TopBlock()->FindBlock("missingWeldObjectsListBox"));
        //------------------------------------------------------------------------------
        //Registration of ListBox specific callbacks
        //------------------------------------------------------------------------------
        //missingWeldObjectsListBox->SetAddHandler(make_callback(this, &MissingWelds::AddCallback));
        
        //missingWeldObjectsListBox->SetDeleteHandler(make_callback(this, &MissingWelds::DeleteCallback));
        
        //------------------------------------------------------------------------------
        //------------------------------------------------------------------------------
        //Registration of Wizard, missingWeldWizard specific callbacks
        //------------------------------------------------------------------------------
        missingWeldWizard->SetStepNotifyPreHandler(make_callback(this, &MissingWelds::StepNotifyPreCallback));;
        
        //missingWeldWizard->SetStepNotifyPostHandler(make_callback(this, &MissingWelds::StepNotifyPostCallback));;
        
        missingWeldWizard->SetIsStepOkayHandler(make_callback(this, &MissingWelds::IsStepOkayCallback));;
        
        missingWeldWizard->SetOnSubNodeHandler(make_callback(this, &MissingWelds::OnSubNodeCallback));;
        
        missingWeldWizard->SetOnMenuHandler(make_callback(this, &MissingWelds::OnMenuCallback));;
        
        missingWeldWizard->SetOnMenuSelectionHandler(make_callback(this, &MissingWelds::OnMenuSelectionCallback));;

        
        compSelection->AddFilter(BlockStyler::SelectObject::FilterTypeComponents);

        // Load all the components included in the assembly except the root component
        if (theSession->Parts()->Display() != NULL)
        {
            Component* rootComponent = theSession->Parts()->Display()->ComponentAssembly()->RootComponent();
            AddChildren(rootComponent);
        }
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void MissingWelds::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int MissingWelds::apply_cb()
{
    int errorCode = 0;
    try
    {

        // Show all bodies and unhighlight all objects
        theSession->DisplayManager()->ShowByType("SHOW_HIDE_TYPE_SOLID_BODIES", DisplayManager::ShowHideScopeAnyInAssembly);

        if (selectedMissingWeldObjects[0] != NULL)
        {
            selectedMissingWeldObjects[0]->Unhighlight();
        }
        if (selectedMissingWeldObjects[1] != NULL)
        {
            selectedMissingWeldObjects[1]->Unhighlight();
        }

        theSession->Parts()->Work()->Views()->WorkView()->Fit();
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int MissingWelds::update_cb(BlockStyler::UIBlock* block)
{
    try
    {
        if (block == compSelection)
        {
        //---------Enter your code here-----------
        }
        else if (block == compDisplay)
        {
            View* theWorkView = theSession->Parts()->Work()->Views()->WorkView();
            Weld::WeldManager* theWeldManager = theSession->Parts()->Work()->Features()->WeldManager();

            // Get value of compDisplay enum
            PropertyList* compDisplayProps = compDisplay->GetProperties();
            int compDisplayValue = compDisplayProps->GetEnum("Value");
            delete compDisplayProps;
            compDisplayProps = NULL;

            // "Blank" has the enum value of 0
            if (compDisplayValue == 0)
            {
                if (selectedMissingWeldObjects[0] != NULL && selectedMissingWeldObjects[1] != NULL)
                {

                    // Unhighlight the objects and show only those two objects
                    selectedMissingWeldObjects[0]->Unhighlight();
                    selectedMissingWeldObjects[1]->Unhighlight();

                    theSession->DisplayManager()->HideByType("SHOW_HIDE_TYPE_SHEET_BODIES", DisplayManager::ShowHideScopeAnyInAssembly);

                    for (Weld::WeldManager::iterator weldManagerIterator = theWeldManager->begin(); weldManagerIterator != theWeldManager->end(); weldManagerIterator++)
                    {
                        (*weldManagerIterator)->HideBody();
                    }
                    
                    for (std::vector<DisplayableObject*>::iterator displayableObjectIterator = allObjects.begin(); displayableObjectIterator != allObjects.end(); displayableObjectIterator++)
                    {
                        if ((*displayableObjectIterator) != selectedMissingWeldObjects[0] && (*displayableObjectIterator) != selectedMissingWeldObjects[1])
                        {
                            (*displayableObjectIterator)->Blank();
                        }
                    }

                    theWorkView->Fit();
                }
            }

            // "Highlight" has the enum value of 1
            if (compDisplayValue == 1)
            {
                if (selectedMissingWeldObjects[0] != NULL && selectedMissingWeldObjects[1] != NULL)
                {

                    // Unblank all bodies and highlight the two objects
                    for (Weld::WeldManager::iterator weldManagerIterator = theWeldManager->begin(); weldManagerIterator != theWeldManager->end(); weldManagerIterator++)
                    {
                        (*weldManagerIterator)->ShowBody(true);
                    }

                    for (std::vector<DisplayableObject*>::iterator displayableObjectIterator = allObjects.begin(); displayableObjectIterator != allObjects.end(); displayableObjectIterator++)
                    {
                        if ((*displayableObjectIterator) != selectedMissingWeldObjects[0] && (*displayableObjectIterator) != selectedMissingWeldObjects[1])
                        {
                            (*displayableObjectIterator)->Unblank();
                        }
                    }

                    theWorkView->Fit();

                    selectedMissingWeldObjects[0]->Highlight();
                    selectedMissingWeldObjects[1]->Highlight();
                }
            }
        }
        else if (block == missingWeldObjectsListBox)
        {
        //---------Enter your code here-----------
        }
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int MissingWelds::ok_cb()
{
    int errorCode = 0;
    try
    {
        errorCode = apply_cb();
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}
//------------------------------------------------------------------------------
//ListBox specific callbacks
//------------------------------------------------------------------------------
//int MissingWelds::AddCallback (BlockStyler::ListBox* list_box)
//{
//}

//int MissingWelds::DeleteCallback(BlockStyler::ListBox* list_box)
//{
//}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
//Wizard specific callbacks
//------------------------------------------------------------------------------
int MissingWelds::StepNotifyPreCallback(Wizard* wizard, int nextStep)
{
    try
    {
        Part* theWorkPart = theSession->Parts()->Work();
        View* theWorkView = theWorkPart->Views()->WorkView();

        if (nextStep == 0)
        {
            
            // Clear list box
            std::vector<NXString> listBoxMessage;
            listBoxMessage.push_back("");
            missingWeldObjectsListBox->SetListItems(listBoxMessage);
            listBoxMessage.clear();

            // Show all bodies and unhighlight all objects
            theSession->DisplayManager()->ShowByType("SHOW_HIDE_TYPE_SOLID_BODIES", DisplayManager::ShowHideScopeAnyInAssembly);

            if (selectedMissingWeldObjects[0] != NULL)
            {
                selectedMissingWeldObjects[0]->Unhighlight();
                selectedMissingWeldObjects[0] = NULL;
            }
            if (selectedMissingWeldObjects[1] != NULL)
            {
                selectedMissingWeldObjects[1]->Unhighlight();
                selectedMissingWeldObjects[1] = NULL;
            }

            for (std::map<int, std::pair<DisplayableObject*, DisplayableObject*> >::iterator mapIterator = missingWelds.begin(); mapIterator != missingWelds.end(); mapIterator++)
            {
                wizard->RemoveStepSubNode(mapIterator->first);
            }

            if (theClearanceSet != NULL)
            {
                theClearanceSet->Delete();
                theClearanceSet = NULL;
            }

            wasSubNodeCreated = false;
            missingWelds.clear();
            checkedSubNodeObjects.clear();

            theWorkView->Fit();
        }
        else if (nextStep == 1)
        {
            ClearanceAnalysisBuilder* clearanceAnalysisBuilder1 = theWorkPart->AssemblyManager()->CreateClearanceAnalysisBuilder(NULL);

            // Set parameters
            clearanceAnalysisBuilder1->SetClearanceSetName("Missing Weld Clearance Set");
            clearanceAnalysisBuilder1->SetCollectionOneRange(ClearanceAnalysisBuilder::CollectionRangeSelectedObjects);

            // Add selected components to CollectionOneObjects
            std::vector<TaggedObject*> selectedObjects = compSelection->GetSelectedObjects();
            for (std::vector<TaggedObject*>::iterator taggedObjectIterator = selectedObjects.begin();
                taggedObjectIterator != selectedObjects.end(); taggedObjectIterator++)
            {
                clearanceAnalysisBuilder1->CollectionOneObjects()->Add(dynamic_cast<DisplayableObject*>(*taggedObjectIterator));
            }

            NXObject* nXObject1 = clearanceAnalysisBuilder1->Commit();
            clearanceAnalysisBuilder1->Destroy();
            theClearanceSet = dynamic_cast<ClearanceSet*>(nXObject1); // holds the clearance set created by the wizard
            theClearanceSet->PerformAnalysis(ClearanceSet::ReanalyzeOutOfDateExcludedPairsFalse);


            // Store the list of welds
            std::vector< std::pair<TaggedObject*, TaggedObject*> > weldObjects; // holds the pair of tagged objects involved in each weld feature
            for (Weld::WeldManager::iterator weldManagerIterator = theWorkPart->Features()->WeldManager()->begin();
                weldManagerIterator != theWorkPart->Features()->WeldManager()->end(); weldManagerIterator++)
            {
                Weld::ConnectedPart* connectPartsInfo = theSession->WeldCustomManager()->AskConnectedParts((*weldManagerIterator));
                // We assume that there are exactly two sets for the weld, with one object in each set
                std::vector<NXObject*> id1;
                connectPartsInfo->GetSetInformation(0, id1);
                std::vector<NXObject*> id2;
                connectPartsInfo->GetSetInformation(1, id2);
                NXObjectManager objectManager1;
                weldObjects.push_back(std::make_pair(objectManager1.Get(id1[0]->Tag()), objectManager1.Get(id2[0]->Tag())));
            }

            // Create a subNode for each missing weld and store the pair of objects involved in the weld.
            // NOTE: The interfering objects in the clearance set, and the objects involved in the weld feature
            // must be components when compared with each other.
            DisplayableObject* interferenceComponent1 = NULL;
            DisplayableObject* interferenceComponent2 = NULL;
            theClearanceSet->GetNextInterference(NULL, NULL, &interferenceComponent1, &interferenceComponent2);

            int i = 1;
            int subNodeID;
            NXString missingweldname;

            while (interferenceComponent1 != NULL)
            {
                bool isMissingWeld = true;
                for (std::vector< std::pair<TaggedObject*, TaggedObject*> >::iterator taggedObjectIterator2 = weldObjects.begin();
                    taggedObjectIterator2 != weldObjects.end(); taggedObjectIterator2++)
                {
                    Body* weldBody1 = dynamic_cast<Body*>((*taggedObjectIterator2).first);
                    Body* weldBody2 = dynamic_cast<Body*>((*taggedObjectIterator2).second);
                    Component* weldComponent1 = weldBody1->OwningComponent();
                    Component* weldComponent2 = weldBody2->OwningComponent();
                    if ((weldComponent1 == interferenceComponent1 && weldComponent2 == interferenceComponent2)
                        || (weldComponent2 == interferenceComponent1 && weldComponent1 == interferenceComponent2))
                    {
                        isMissingWeld = false;
                        break;
                    }
                }

                if (isMissingWeld)
                {
                    missingweldname = "Missing weld " + std::to_string(i);
                    i++;
                    subNodeID = wizard->CreateStepSubNode(1, missingweldname, "", true, true);
                    missingWelds[subNodeID] = std::make_pair(interferenceComponent1, interferenceComponent2);
                    checkedSubNodeObjects.push_back(std::make_pair(interferenceComponent1, interferenceComponent2));
                    wasSubNodeCreated = true;
                }

                theClearanceSet->GetNextInterference(interferenceComponent1, interferenceComponent2, &interferenceComponent1, &interferenceComponent2);
            }

            // If no sub nodes were created, display message
            if (!wasSubNodeCreated)
            {
                std::vector<NXString> listBoxMessage;
                listBoxMessage.push_back("There are no missing welds.");
                missingWeldObjectsListBox->SetListItems(listBoxMessage);
            }

            theWorkView->Fit();
        }
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }

    return 0;
}

//void MissingWelds::StepNotifyPostCallback(Wizard* wizard, int previousStep)
//{
//}

bool MissingWelds::IsStepOkayCallback(Wizard* wizard, int step)
{
    try
    {
        if (wizard->CurrentStep() == 0)
        {
            if (compSelection->GetSelectedObjects().size() > 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else if (wizard->CurrentStep() == 1)
        {
            return true;
        }
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }

    return false;
}

void MissingWelds::OnSubNodeCallback(Wizard* wizard, int step, int subNodeId, Wizard::SubNodeAction action)
{
    try
    {
        View* theWorkView = theSession->Parts()->Work()->Views()->WorkView();
        Weld::WeldManager* theWeldManager = theSession->Parts()->Work()->Features()->WeldManager();

        // Store the pair of objects from the missing weld associated with this sub node
        // for access by update_cb, apply_cb, and StepNotifyPreCallback methods
        selectedMissingWeldObjects[0] = missingWelds[subNodeId].first;
        selectedMissingWeldObjects[1] = missingWelds[subNodeId].second;
        std::pair<DisplayableObject*, DisplayableObject*> subNodePair(selectedMissingWeldObjects[0], selectedMissingWeldObjects[1]); 

        if (action == Wizard::SubNodeActionSelect)
        {
            
            // Add the missing weld's objects to list box
            std::vector<NXString> listBoxMessage;
            listBoxMessage.push_back(selectedMissingWeldObjects[0]->Name());
            listBoxMessage.push_back(selectedMissingWeldObjects[1]->Name());
            missingWeldObjectsListBox->SetListItems(listBoxMessage);
            listBoxMessage.clear();

            // Get value of compDisplay enum
            PropertyList* compDisplayProps = compDisplay->GetProperties();
            int compDisplayValue = compDisplayProps->GetEnum("Value");
            delete compDisplayProps;
            compDisplayProps = NULL;

            // "Blank" has the enum value of 0
            if (compDisplayValue == 0)
            {

                // Show only the two objects
                theSession->DisplayManager()->HideByType("SHOW_HIDE_TYPE_SHEET_BODIES", DisplayManager::ShowHideScopeAnyInAssembly);

                for (Weld::WeldManager::iterator weldManagerIterator = theWeldManager->begin(); weldManagerIterator != theWeldManager->end(); weldManagerIterator++)
                {
                    (*weldManagerIterator)->HideBody();
                }
                for (std::vector<DisplayableObject*>::iterator displayableObjectIterator = allObjects.begin(); displayableObjectIterator != allObjects.end(); displayableObjectIterator++)
                {
                    if ((*displayableObjectIterator) != selectedMissingWeldObjects[0] && (*displayableObjectIterator) != selectedMissingWeldObjects[1])
                    {
                        (*displayableObjectIterator)->Blank();
                    }
                }
                theWorkView->Fit();
            }

            // "Highlight" has the enum value of 1
            if (compDisplayValue == 1)
            {
                theWorkView->Fit();

                selectedMissingWeldObjects[0]->Highlight();
                selectedMissingWeldObjects[1]->Highlight();
            }

        }
        else if (action == Wizard::SubNodeActionDeselect)
        {

            // Clear list box
            std::vector<NXString> listBoxMessage;
            listBoxMessage.push_back("");
            missingWeldObjectsListBox->SetListItems(listBoxMessage);
            listBoxMessage.clear();

            // Unhighlight and unblank all bodies
            selectedMissingWeldObjects[0]->Unhighlight();
            selectedMissingWeldObjects[1]->Unhighlight();

            for (Weld::WeldManager::iterator weldManagerIterator = theWeldManager->begin(); weldManagerIterator != theWeldManager->end(); weldManagerIterator++)
            {
                (*weldManagerIterator)->ShowBody(true);
            }

            for (std::vector<DisplayableObject*>::iterator displayableObjectIterator = allObjects.begin(); displayableObjectIterator != allObjects.end(); displayableObjectIterator++)
            {
                if ((*displayableObjectIterator) != selectedMissingWeldObjects[0] && (*displayableObjectIterator) != selectedMissingWeldObjects[1])
                {
                    (*displayableObjectIterator)->Unblank();
                }
            }

            // Release this pair of objects when the sub node is deselected
            selectedMissingWeldObjects[0] = NULL;
            selectedMissingWeldObjects[1] = NULL;
        }
        else if (action == Wizard::SubNodeActionCheck)
        {
            checkedSubNodeObjects.push_back(subNodePair);
        }
        else if (action == Wizard::SubNodeActionUncheck)
        {
            checkedSubNodeObjects.erase(std::remove(checkedSubNodeObjects.begin(), checkedSubNodeObjects.end(), subNodePair), checkedSubNodeObjects.end());
        }
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
}

void MissingWelds::OnMenuCallback(Wizard* wizard, Wizard::TaskNavigatorItem item, int step, int subNodeId)
{
    try
    {
        TreeListMenu* subNodeMenu = missingWeldWizard->CreateMenu();
        if (item == Wizard::TaskNavigatorItemStep)
        {
            if (wasSubNodeCreated)
            {
                subNodeMenu->AddMenuItem(0, "Generate Report for Selected Missing Welds");
                missingWeldWizard->SetMenu(subNodeMenu);
            }
        }
        else if (item == Wizard::TaskNavigatorItemSubNode)
        {
            subNodeMenu->AddMenuItem(1, "Export Image to PDF");
            missingWeldWizard->SetMenu(subNodeMenu);
        }
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
}

void MissingWelds::OnMenuSelectionCallback(Wizard* wizard, Wizard::TaskNavigatorItem item, int step, int subNodeId, int commandIndex)
{
    try
    {
        Part* theWorkPart = theSession->Parts()->Work();

        if (commandIndex == 0)
        {
            ListingWindow* reportWindow = theSession->ListingWindow();
            reportWindow->Open();
            reportWindow->WriteLine("Missing Welds for " + theSession->Parts()->Display()->ComponentAssembly()->RootComponent()->DisplayName() + "\n\n");
            reportWindow->WriteLine(std::to_string(checkedSubNodeObjects.size()) + " of " + std::to_string(missingWelds.size()) + " missing welds selected\n\n");
            reportWindow->WriteLine("     Part 1\t\tPart 2\n\n");

            // Format spacing in report
            // Assumes no more than 999 missing weld pairs
            int i = 1;
            for (std::vector< std::pair<DisplayableObject*, DisplayableObject*> >::iterator displayableObjectIterator2 = checkedSubNodeObjects.begin();
                displayableObjectIterator2 != checkedSubNodeObjects.end(); displayableObjectIterator2++)
            {
                if (i <= 9)
                {
                    reportWindow->WriteLine(std::to_string(i) + ")   " + (*displayableObjectIterator2).first->Name() + "\t" + (*displayableObjectIterator2).second->Name());
                    i++;
                }
                else if (i <= 99)
                {
                    reportWindow->WriteLine(std::to_string(i) + ")  " + (*displayableObjectIterator2).first->Name() + "\t" + (*displayableObjectIterator2).second->Name());
                    i++;
                }
                else
                {
                    reportWindow->WriteLine(std::to_string(i) + ") " + (*displayableObjectIterator2).first->Name() + "\t" + (*displayableObjectIterator2).second->Name());
                    i++;
                }
            }
        }
        else if (commandIndex == 1)
        {
            
            // Get value of compDisplay enum
            PropertyList* compDisplayProps = compDisplay->GetProperties();
            int compDisplayValue = compDisplayProps->GetEnum("Value");

            // If Highlight is selected, automatically select Blank before creating image
            // "Highlight" has the enum value of 1
            if (compDisplayValue == 1)
            {

                // "Blank" has the enum value of 0
                compDisplayProps->SetEnum("Value", 0);

                // Unhighlight the objects and show only those two objects
                selectedMissingWeldObjects[0]->Unhighlight();
                selectedMissingWeldObjects[1]->Unhighlight();

                theSession->DisplayManager()->HideByType("SHOW_HIDE_TYPE_SHEET_BODIES", DisplayManager::ShowHideScopeAnyInAssembly);

                Weld::WeldManager* theWeldManager = theWorkPart->Features()->WeldManager();
                for (Weld::WeldManager::iterator weldManagerIterator = theWeldManager->begin(); weldManagerIterator != theWeldManager->end(); weldManagerIterator++)
                {
                    (*weldManagerIterator)->HideBody();
                }

                for (std::vector<DisplayableObject*>::iterator displayableObjectIterator = allObjects.begin(); displayableObjectIterator != allObjects.end(); displayableObjectIterator++)
                {
                    if ((*displayableObjectIterator) != selectedMissingWeldObjects[0] && (*displayableObjectIterator) != selectedMissingWeldObjects[1])
                    {
                        (*displayableObjectIterator)->Blank();
                    }
                }

                theWorkPart->Views()->WorkView()->Fit();
            }

            delete compDisplayProps;
            compDisplayProps = NULL;


            PrintPDFBuilder* printPDFBuilder1 = theWorkPart->PlotManager()->CreatePrintPdfbuilder();

            std::vector<NXObject*> sheets1(1);
            NXObject* nullNXOpen_NXObject = NULL;
            sheets1[0] = nullNXOpen_NXObject;
            printPDFBuilder1->SourceBuilder()->SetSheets(sheets1);

            // Set pdf path to same directory as work part
            std::string fullPath = theWorkPart->FullPath().GetText();
            size_t index = fullPath.find_last_of("\\");
            NXString workPartDir = fullPath.substr(0, index);
            NXString fileName = "MissingWeld_" + selectedMissingWeldObjects[0]->Name() + "_" + selectedMissingWeldObjects[1]->Name() + ".pdf";
            printPDFBuilder1->SetFilename(workPartDir + "\\" + fileName);


            NXObject* nXObject1 = printPDFBuilder1->Commit();
            printPDFBuilder1->Destroy();
        }
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    } 
}


//------------------------------------------------------------------------------
//Function Name: AddChildren
//Recursive function used to add the children of the current component tree
//node to allObjects
//------------------------------------------------------------------------------
void MissingWelds::AddChildren(Component* component)
{
    try
    {
        std::vector<Component*> childComponent = component->GetChildren();
        for (int i = 0; i < childComponent.size(); ++i)
        {
            allObjects.push_back(childComponent[i]);
            AddChildren(childComponent[i]);
        }
    }
    catch (std::exception& ex)
    {
        //---- Enter your exception handling code here -----
        MissingWelds::theUI->NXMessageBox()->Show("Block Styler", NXMessageBox::DialogTypeError, ex.what());
    }
}
