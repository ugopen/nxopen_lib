//=============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Software
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
//  1.  Help on how to load and display your Block Styler dialog in NX
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
#include "SelectionExample.hpp"
#include <NXOpen/Edge.hxx>
#include <NXOpen/EdgeTangentRule.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Face.hxx>
#include <NXOpen/Features_Chamfer.hxx>
#include <NXOpen/Features_ChamferBuilder.hxx>
#include <NXOpen/Features_FeatureCollection.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/ScCollectorCollection.hxx>
#include <NXOpen/ScRuleFactory.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <sstream>
#include <iomanip>
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(SelectionExample::theSession) = NULL;
UI *(SelectionExample::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
SelectionExample *theSelectionExample;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
SelectionExample::SelectionExample()
{
    try
    {
        // Initialize the NX Open C++ API environment
        SelectionExample::theSession = NXOpen::Session::GetSession();
        SelectionExample::theUI = UI::GetUI();
        theDialogName = "SelectionExample.dlx";
        theDialog = SelectionExample::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &SelectionExample::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &SelectionExample::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &SelectionExample::update_cb));
        theDialog->AddFilterHandler(make_callback(this, &SelectionExample::filter_cb));
        theDialog->AddInitializeHandler(make_callback(this, &SelectionExample::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &SelectionExample::dialogShown_cb));
    }
    catch(exception& ex)
    {
        std::string exceptionText = ex.what();
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
SelectionExample::~SelectionExample()
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
        theSelectionExample = new SelectionExample();
        // The following method shows the dialog immediately
        theSelectionExample->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        SelectionExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    delete theSelectionExample;
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
        SelectionExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int SelectionExample::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        SelectionExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void SelectionExample::initialize_cb()
{
    try
    {
        group0 = theDialog->TopBlock()->FindBlock("group0");
        edgeSelect = theDialog->TopBlock()->FindBlock("edge_select0");
        faceToggle = theDialog->TopBlock()->FindBlock("toggle0");
        angleDouble = theDialog->TopBlock()->FindBlock("double0");
        group01 = theDialog->TopBlock()->FindBlock("group01");
        chamferSelect = theDialog->TopBlock()->FindBlock("select_feature0");
        angleToggle = theDialog->TopBlock()->FindBlock("toggle01");
        angleLimitDouble = theDialog->TopBlock()->FindBlock("double01");

        //Initialize
        limitingFace = NULL;
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        SelectionExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void SelectionExample::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        SelectionExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int SelectionExample::apply_cb()
{
    int errorCode = 0;
    try
    {

        //*****************************************************************************************
        //Add Chamfers to Selected Edges

        //Get the chamfer angle and edge selection list from the dialog
        PropertyList* angleDoubleProps = angleDouble->GetProperties();
        double creationAngle = angleDoubleProps->GetDouble("Value");
        delete angleDoubleProps;
        angleDoubleProps = NULL;

        PropertyList*  edgeSelectProps = edgeSelect->GetProperties();
        std::vector<NXOpen::TaggedObject *> edges = edgeSelectProps->GetTaggedObjectVector("SelectedObjects");
        delete edgeSelectProps;
        edgeSelectProps = NULL;

        //Add a chamfer to each selected edge
        for (unsigned int ii = 0; ii < edges.size(); ++ii) 
        {
            NXOpen::Edge* selectedEdge = dynamic_cast<NXOpen::Edge*>(edges[ii]);
            addChamfer(selectedEdge, creationAngle);
        }

        //*****************************************************************************************
        //Remove Selected Chamfers

        //Get the selected chamfers from the dialog
        PropertyList*  chamferSelectProps = chamferSelect->GetProperties();
        std::vector<NXOpen::TaggedObject *> chamfers = chamferSelectProps->GetTaggedObjectVector("SelectedObjects");
        delete chamferSelectProps;
        chamferSelectProps = NULL;

        //Set an undo mark for update
        Session::UndoMarkId undoMark = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Remove Chamfers");

        //Add the selected chamfers to the delete list
        for (unsigned int ii = 0; ii < chamfers.size(); ++ii)
        {
            NXOpen::Features::Chamfer* chamferObject = dynamic_cast<NXOpen::Features::Chamfer*>(chamfers[ii]);
            errorCode = deleteObject(chamferObject);
        }

        //Update the model to delete the chamfers
        int nErrs = theSession->UpdateManager()->DoUpdate(undoMark);

        //Report any errors - normally the error list should be scanned and each error processed
        if (nErrs > 0) 
        {
            errorCode = 1;
            std::stringstream tmpString;
            tmpString << "nErrs =" << nErrs;
            SelectionExample::theUI->NXMessageBox()->Show("Update Errors", NXOpen::NXMessageBox::DialogTypeError,tmpString.str());
        }

    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        SelectionExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int SelectionExample::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        PropertyList* faceToggleProps = faceToggle->GetProperties();
        PropertyList* edgeSelectProps = edgeSelect->GetProperties();
        PropertyList* chamferSelectProps = chamferSelect->GetProperties();
        PropertyList* angleLimitDoubleProps = angleLimitDouble->GetProperties();
        PropertyList* angleToggleProps = angleToggle->GetProperties();

        if(block == edgeSelect)
        {
            // When face filtering is on, establish a limiting face after two edges are selected

            if(faceToggleProps->GetLogical("Value")) 
            {
                std::vector<TaggedObject*> edges = edgeSelectProps->GetTaggedObjectVector("SelectedObjects");
                if (edges.size() == 2) 
                {
                    limitingFace = sharedFace(dynamic_cast<NXOpen::Edge*>(edges[0]), dynamic_cast<NXOpen::Edge*>(edges[1]));
                }
            }
        }
        else if(block == faceToggle)
        {
            // When the face filter is turned on...
            // Clear the current edge selection list

            if (faceToggleProps->GetLogical("Value")) 
            {
                std::vector<NXOpen::TaggedObject* > edges(0);
                edgeSelectProps->SetTaggedObjectVector("SelectedObjects", edges);
                limitingFace = NULL;
            }
        }
        else if(block == angleDouble)
        {
        //---------Enter your code here-----------
        }
        else if(block == chamferSelect)
        {
        //---------Enter your code here-----------
        }
        else if(block == angleToggle)
        {
            // When the angle filter is turned on...
            //   1. Clear the current chamfer selection list
            //   2. Also, enable/disable the angle limit entry field

            if (angleToggleProps->GetLogical("Value")) 
            {
                std::vector<NXOpen::TaggedObject* > chamfers(0);
                chamferSelectProps->SetTaggedObjectVector("SelectedObjects", chamfers);
                angleLimitDoubleProps->SetLogical("Enable", true);
            }
            else
            {
                angleLimitDoubleProps->SetLogical("Enable", false);
            }
        }
        else if(block == angleLimitDouble)
        {
            // When the angle limit value changes...
            //    Clear the current chamfer selection list
            std::vector<TaggedObject*> chamfers(0);
            chamferSelectProps->SetTaggedObjectVector("SelectedObjects", chamfers);
        }
        delete faceToggleProps;
        faceToggleProps = NULL;
        delete edgeSelectProps;
        faceToggleProps = NULL;
        delete chamferSelectProps;
        chamferSelectProps = NULL;
        delete angleLimitDoubleProps;
        angleLimitDoubleProps = NULL;
        delete angleToggleProps;
        angleToggleProps = NULL;
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        SelectionExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int SelectionExample::ok_cb()
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
        SelectionExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: filter_cb
//------------------------------------------------------------------------------
int SelectionExample::filter_cb(NXOpen::BlockStyler::UIBlock*  block, NXOpen::TaggedObject* selectedObject)
{
    int accept = UF_UI_SEL_ACCEPT;
    try
    {
        if (block == edgeSelect)
        {
            // Edge Select Filter
            PropertyList* faceToggleProps = faceToggle->GetProperties();
            if (faceToggleProps->GetLogical("Value"))
            {
                accept = faceFilter(dynamic_cast<NXOpen::Edge*>(selectedObject));
            }
            delete faceToggleProps;
            faceToggleProps = NULL;
        }
        else if (block == chamferSelect)
        {
            // Feature Selection Filter - limit selection to chamfer features
            NXOpen::Features::Feature* featureObject = dynamic_cast<NXOpen::Features::Feature*>(selectedObject);

            if (strcmp(featureObject->FeatureType().GetText(),"CHAMFER") == 0) 
            {
                accept = angleFilter(dynamic_cast<NXOpen::Features::Chamfer*>(featureObject));
            }
            else
            {
                accept = UF_UI_SEL_REJECT;
            }
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        accept = UF_UI_SEL_REJECT;
        SelectionExample::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return accept;
}

// **********************************************************************************************************
// FACE FILTER

int SelectionExample::faceFilter(NXOpen::Edge* selectedEdge)
{
    int accept = UF_UI_SEL_REJECT;
    try
    {
        // If a limiting face has not been established...
        //   then use the first two selected edges to establish the limiting face 
        //   otherwise use the limiting face

        if (limitingFace == NULL) 
        {
            PropertyList* edgeSelectProps = edgeSelect->GetProperties();
            // Limit faces to those of the first selected edge
            std::vector<NXOpen::TaggedObject* > edges = edgeSelectProps->GetTaggedObjectVector("SelectedObjects");
            delete edgeSelectProps;
            edgeSelectProps = NULL;

            if (edges.size() < 1) 
            {
                accept = UF_UI_SEL_ACCEPT;
            }
            else if (edges.size() == 1) 
            {
                if (sharedFace(dynamic_cast<NXOpen::Edge* >(edges[0]), selectedEdge) != NULL)
                {
                    accept = UF_UI_SEL_ACCEPT;
                }
            }
        }
        else
        {
            // Limit the edges to just those of the limiting face
            if (selectedEdge)
            {
                std::vector<NXOpen::Face* > edgeFaces = selectedEdge->GetFaces();
                for (unsigned int ii = 0; ii < edgeFaces.size(); ++ii)
                {
                    NXOpen::Face* faceObject = dynamic_cast<NXOpen::Face* >(edgeFaces[ii]);
                    if (faceObject == NULL) 
                        continue;
                    if (faceObject == limitingFace) 
                    {
                        accept = UF_UI_SEL_ACCEPT;
                        break;
                    }
                }
            }
        }
    }
    catch(exception &ex)
    {
        throw;
    }

    return accept;
}

// **********************************************************************************************************
// ANGLE FILTER

int SelectionExample::angleFilter(NXOpen::Features::Chamfer* chamferFeature)
{
    int accept = UF_UI_SEL_ACCEPT;
    NXOpen::Features::ChamferBuilder* chamferBuilder = NULL;
    PropertyList* angleToggleProps = NULL;
    PropertyList* angleLimitDoubleProps = NULL;

    try
    {

        // If the angle filter toggle is ON...
        //   then only accept chamfers of the limiting angle
        angleToggleProps = angleToggle->GetProperties();

        if (angleToggleProps->GetLogical("Value")) 
        {
            NXOpen::Part* workPart  = SelectionExample::theSession->Parts()->Work();
            chamferBuilder = workPart->Features()->CreateChamferBuilder(chamferFeature);
            angleLimitDoubleProps = angleLimitDouble->GetProperties();
            if (chamferBuilder->AngleExp()->Value() != angleLimitDoubleProps->GetDouble("Value")) 
            {
                accept = UF_UI_SEL_REJECT;
            }
            delete angleLimitDoubleProps;
            angleLimitDoubleProps = NULL;

            chamferBuilder->Destroy();
            chamferBuilder = NULL;
        }
        delete angleToggleProps;
        angleToggleProps = NULL;
    }
    catch(exception& ex)
    {
        if (NULL != chamferBuilder)
        {
            chamferBuilder->Destroy();
            chamferBuilder = NULL;
        }
        if (NULL != angleLimitDoubleProps)
        {
            delete angleLimitDoubleProps;
            angleLimitDoubleProps = NULL;
        }
        if (NULL != angleToggleProps)
        {
            delete angleToggleProps;
            angleToggleProps = NULL;
        }

        throw;
    }

    return accept;
}

//**********************************************************************************************************
//SHARED FACE - return face shared between two edges
NXOpen::Face* SelectionExample::sharedFace(NXOpen::Edge* edge1, NXOpen::Edge* edge2)
{
    NXOpen::Face* foundFace = NULL;
    try
    {

        std::vector<NXOpen::Face* > edgeFaces1 = edge1->GetFaces();
        std::vector<NXOpen::Face* > edgeFaces2 = edge2->GetFaces();

        for (unsigned int ii = 0; ii < edgeFaces1.size(); ++ii)
        {
            for (unsigned int jj = 0; jj < edgeFaces2.size(); ++jj) 
            {
                if (edgeFaces1[ii] == edgeFaces2[jj])
                {
                    foundFace = edgeFaces1[ii];
                    break;
                }
            }

            if (foundFace != NULL) 
                break;
        }
    }
    catch(exception &ex)
    {
        throw;
    }

    return foundFace;
}

//**********************************************************************************************************
//ADD CHAMFER FEATURE of given angle to given edge

void SelectionExample::addChamfer(NXOpen::Edge* selectedEdge, double angle)
{
    NXOpen::Features::ChamferBuilder* chamferBuilder1 = NULL;
    try
    {
        NXOpen::Part* workPart = SelectionExample::theSession->Parts()->Work();
        NXOpen::Features::Feature* nullFeatures_Feature = NULL;
        chamferBuilder1 = workPart->Features()->CreateChamferBuilder(nullFeatures_Feature);
        

        chamferBuilder1->SetOption(Features::ChamferBuilder::ChamferOptionOffsetAndAngle);
        chamferBuilder1->SetMethod(Features::ChamferBuilder::OffsetMethodEdgesAlongFaces);

        chamferBuilder1->SetFirstOffset("15");
        chamferBuilder1->SetSecondOffset("15");

        // Convert angle in double to std::string
        std::stringstream tmpAngle;
        tmpAngle << setprecision(16) << angle;
        chamferBuilder1->SetAngle(tmpAngle.str());
        chamferBuilder1->SetTolerance(0.0254);

        NXOpen::Edge*  nullEdge = NULL;
        NXOpen::EdgeTangentRule* edgeTangentRule1 = workPart->ScRuleFactory()->CreateRuleEdgeTangent(selectedEdge, nullEdge, false, 0.5, false);

        std::vector<NXOpen::SelectionIntentRule* > rules1(1);
        rules1[0] = edgeTangentRule1;

        NXOpen::ScCollector* scCollector1 = workPart->ScCollectors()->CreateCollector();

        scCollector1->ReplaceRules(rules1, false);

        chamferBuilder1->SetSmartCollector(scCollector1);

        NXOpen::Features::Feature* feature1 = chamferBuilder1->CommitFeature();

        chamferBuilder1->Destroy();
        chamferBuilder1 = NULL;
    }
    catch(exception& ex)
    {
        if (NULL != chamferBuilder1)
        {
            chamferBuilder1->Destroy();
            chamferBuilder1 = NULL;
        }
        throw;
    }
}

//**********************************************************************************************************
//DELETE OBJECT - add the given object to the delete list

int SelectionExample::deleteObject(NXOpen::NXObject* selectedObject)
{
    int error = 0;
    try
    {
        std::vector<NXObject* >  obj(1);
        obj[0] = selectedObject;
        int nErrs = theSession->UpdateManager()->AddToDeleteList(obj);

        //Report any errors - normally the error list should be scanned and each error processed
        if(nErrs > 0)
        {
            error = 1;
            std::stringstream tmpString;
            tmpString << "nErrs =" << nErrs;
            SelectionExample::theUI->NXMessageBox()->Show("Add To Delete Errors", NXOpen::NXMessageBox::DialogTypeError, tmpString.str() );
        }
    }
    catch(exception& ex)
    {
        throw;
    }

    return error;
}


