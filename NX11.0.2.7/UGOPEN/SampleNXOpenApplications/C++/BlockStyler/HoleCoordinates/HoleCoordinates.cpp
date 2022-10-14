//=============================================================================
//
//                   Copyright (c) 2008 Siemens PLM Software
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
#include "HoleCoordinates.hpp"
#include "NXOpen/DatumAxis.hxx"
#include "NXOpen/Direction.hxx"
#include "NXOpen/DirectionCollection.hxx"
#include "NXOpen/Edge.hxx"
#include "NXOpen/Face.hxx"
#include "NXOpen/Facet_FacetedBodyCollection.hxx"
#include "NXOpen/Features_DatumAxisBuilder.hxx"
#include "NXOpen/Features_DatumAxisFeature.hxx"
#include "NXOpen/Features_Feature.hxx"
#include "NXOpen/Features_FeatureCollection.hxx"
#include "NXOpen/Features_Hole.hxx"
#include "NXOpen/Features_HolePackage.hxx"
#include "NXOpen/MeasureManager.hxx"
#include "NXOpen/MeasureDistance.hxx"
#include "NXOpen/MeasureDistanceBuilder.hxx"
#include "NXOpen/ModelingView.hxx"
#include "NXOpen/ModelingViewCollection.hxx"
#include "NXOpen/NXString.hxx"
#include "NXOpen/Part.hxx"
#include "NXOpen/PartCollection.hxx"
#include "NXOpen/Preferences_SessionModeling.hxx"
#include "NXOpen/Preferences_SessionPreferences.hxx"
#include "NXOpen/Point.hxx"
#include "NXOpen/PointCollection.hxx"
#include "NXOpen/Part.hxx"
#include "NXOpen/SmartObject.hxx"
#include "NXOpen/SelectDisplayableObject.hxx"
#include "NXOpen/Update.hxx"
#include "NXOpen/View.hxx"
#include "NXOpen/ViewCollection.hxx"
#include "NXOpen/Xform.hxx"
#include "NXOpen/XformCollection.hxx"

#include "uf_vec.h"
#include <sstream>
#include <iomanip>
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(HoleCoordinates::theSession) = NULL;
UI *(HoleCoordinates::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
HoleCoordinates *theHoleCoordinates;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
HoleCoordinates::HoleCoordinates()
{
    try
    {
        // Initialize the NX Open C++ API environment
        HoleCoordinates::theSession = NXOpen::Session::GetSession();
        HoleCoordinates::theUI = UI::GetUI();
        theDialogName = "HoleCoordinates.dlx";
        theDialog = HoleCoordinates::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &HoleCoordinates::apply_cb));
        theDialog->AddUpdateHandler(make_callback(this, &HoleCoordinates::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &HoleCoordinates::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &HoleCoordinates::dialogShown_cb));
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
HoleCoordinates::~HoleCoordinates()
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
        theHoleCoordinates = new HoleCoordinates();
        // The following method shows the dialog immediately
        theHoleCoordinates->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    delete theHoleCoordinates;
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
        HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int HoleCoordinates::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void HoleCoordinates::initialize_cb()
{
    try
    {
        workPart = HoleCoordinates::theSession->Parts()->Work();
        displayPart = HoleCoordinates::theSession->Parts()->Display();
        //ufsess = NXOpen::UF::UFSession->GetUFSession();
        groupPoint = theDialog->TopBlock()->FindBlock("groupPoint");
        origin = theDialog->TopBlock()->FindBlock("origin");
        groupXdir = theDialog->TopBlock()->FindBlock("groupXdir");
        xDir = theDialog->TopBlock()->FindBlock("xDir");
        groupYdir = theDialog->TopBlock()->FindBlock("groupYdir");
        yDir = theDialog->TopBlock()->FindBlock("yDir");
        groupFace = theDialog->TopBlock()->FindBlock("groupFace");
        face = theDialog->TopBlock()->FindBlock("face");
        groupInfo = theDialog->TopBlock()->FindBlock("groupInfo");
        buttonInfo = theDialog->TopBlock()->FindBlock("buttonInfo");
        listBoxInfo = dynamic_cast<NXOpen::BlockStyler::ListBox* >(theDialog->TopBlock()->FindBlock("listBoxInfo"));

        // User defined code
        setEnablePropForBlock(buttonInfo, false);
        setEnablePropForBlock(xDir, false);
        setEnablePropForBlock(yDir, false);
        setEnablePropForBlock(face, false);

        refaxis1 = NULL;
        refaxis2 = NULL;
        highlightedFeature = NULL;

    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void HoleCoordinates::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int HoleCoordinates::apply_cb()
{
    int errorCode = 0;
    try
    {
        if ( refaxis1 != NULL && refaxis2 != NULL) 
        {
            NXOpen::Features::Feature* delaxis1 = dynamic_cast<NXOpen::Features::Feature* >(workPart->Features()->FindObject(refaxis1->JournalIdentifier()));
            NXOpen::Features::Feature* delaxis2 = dynamic_cast<NXOpen::Features::Feature* >(workPart->Features()->FindObject(refaxis2->JournalIdentifier()));
            objects1.resize(2);
            objects1[0] = delaxis1;
            objects1[1] = delaxis2;
            deletedatumaxis(objects1);
            refaxis1 = NULL;
            refaxis2 = NULL;
        }
        else
        {
            HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, "Please define all the inputs.");
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int HoleCoordinates::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == origin)
        {
            NXOpen::BlockStyler::PropertyList* originProperties = origin->GetProperties();
            pointCol = originProperties->GetTaggedObjectVector("SelectedObjects");
            delete originProperties;

            axispoint = dynamic_cast<NXOpen::Point* >(pointCol[0]);
            setEnablePropForBlock(xDir, true);
            if (refaxis1 != NULL) 
            {
                refaxis1 = editdatumaxis(refaxis1, dynamic_cast<NXOpen::Direction* >(vectCol[0]), axispoint);
            }
            if (refaxis2 != NULL)
            {
                refaxis2 = editdatumaxis(refaxis2, dynamic_cast<NXOpen::Direction* >(vectCol1[0]), axispoint);
            }
        }
        else if(block == xDir)
        {
            NXOpen::BlockStyler::PropertyList* xDirProperties = xDir->GetProperties();
            vectCol = xDirProperties->GetTaggedObjectVector("SelectedObjects");
            delete xDirProperties;

            if (refaxis1 == NULL)
            {
                refaxis1 = datumaxiscreater(axispoint, dynamic_cast<NXOpen::Direction* >(vectCol[0]));
            }
            else
            {
                refaxis1 = editdatumaxis(refaxis1, dynamic_cast<NXOpen::Direction* >(vectCol[0]), axispoint);
            }
            setEnablePropForBlock(yDir, true);
        }
        else if(block == yDir)
        {
            NXOpen::BlockStyler::PropertyList* yDirProperties = yDir->GetProperties();
            vectCol1 = yDirProperties->GetTaggedObjectVector("SelectedObjects");
            delete yDirProperties;

            if (refaxis2 == NULL)
            {
                refaxis2 = datumaxiscreater(axispoint, dynamic_cast<NXOpen::Direction* >(vectCol1[0]));
            }
            else
            {
                refaxis2 = editdatumaxis(refaxis2, dynamic_cast<NXOpen::Direction* >(vectCol1[0]), axispoint);
            }
            setEnablePropForBlock(face, true);
        }
        else if(block == face)
        {
            NXOpen::BlockStyler::PropertyList* faceProperties = face->GetProperties();
            faceCol = faceProperties->GetTaggedObjectVector("SelectedObjects");
            delete faceProperties;

            if (faceCol.size() > 0)
            {
                holeface = dynamic_cast<NXOpen::Face* >(faceCol[0]);

                setEnablePropForBlock(buttonInfo, true);
            }
            else if (faceCol.size() == 0) 
            {
                holeface = NULL;
                setEnablePropForBlock(buttonInfo, false);
            }
        }
        else if(block == listBoxInfo)
        {
            NXOpen::BlockStyler::PropertyList* listBoxInfoProperties = listBoxInfo->GetProperties();
            std::vector<NXOpen::NXString> str = listBoxInfoProperties->GetStrings("ListItems");
            std::vector<int> index = listBoxInfoProperties->GetIntegerVector("SelectedItems");
            delete listBoxInfoProperties;

            if (index.size() > 0)
            {
                std::string selectedText(str[index[0]].GetUTF8Text());
                if (selectedText.find("HOLE") != string::npos)
                {
                    NXOpen::Features::Feature* selectedFeature = dynamic_cast<NXOpen::Features::Feature* >(workPart->Features()->FindObject(str[index[0]]));
                    if (selectedFeature != NULL)
                    {
                        if (index.size() > 0)
                        {
                            holeface->Unhighlight();
                            // Comment out the following command because it is causing 
                            // excessive flickering
                            // workPart->ModelingViews()->WorkView()->Regenerate();
                        }
                        if (highlightedFeature != NULL) 
                        {
                            highlightedFeature->Unhighlight();
                        }
                        selectedFeature->Highlight();
                        highlightedFeature = selectedFeature;
                    }
                }
                else
                {
                    if (highlightedFeature != NULL) 
                    {
                        highlightedFeature->Unhighlight();
                    }
                    // Comment out the following command because it is causing 
                    // excessive flickering
                    // workPart->ModelingViews()->WorkView()->Regenerate();
                }
            }
        }
        else if(block == buttonInfo)
        {
            NXOpen::BlockStyler::PropertyList* listBoxInfoProperties = listBoxInfo->GetProperties();
            std::vector<NXOpen::NXString> liststrings1 = listBoxInfoProperties->GetStrings("ListItems");
            if (liststrings1.size() > 0) 
            {
                liststrings1.clear();
                //ReDim liststrings1(-1)
                listBoxInfoProperties->SetStrings("ListItems", liststrings1);
            }

            bool foundholes = true;
            NXOpen::Direction* dir1 = NULL;
            NXOpen::Direction* dir2 = NULL;
            try
            {
                if (vectCol.size() > 0 && vectCol1.size() > 0) 
                {
                    dir1 = dynamic_cast<NXOpen::Direction* >(vectCol[0]);
                    dir2 = dynamic_cast<NXOpen::Direction* >(vectCol1[0]);

                    // Checking for perpendicularity between vectors
                    double doublearray1[3] = {dir1->Vector().X, dir1->Vector().Y, dir1->Vector().Z};
                    double doublearray2[3] = {dir2->Vector().X, dir2->Vector().Y, dir2->Vector().Z};
                    int result1;
                    //ufsess.Vec3.IsPerpendicular(doublearray1, doublearray2, 0.000001, result1)
                    UF_VEC3_is_perpendicular(doublearray1, doublearray2, 0.000001, &result1);
                    if (result1 == 0)
                    {
                        HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, "Selected Vectors should be perpendicular");
                        return 0;
                    }

                    UF_VEC3_is_parallel(doublearray1, doublearray2, 0.000001, &result1);
                    if (result1 == 1) 
                    {
                        HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, "Selected Vectors are parallel");
                    }
                    else
                    {
                        std::vector<NXOpen::Edge* > selectedFaceEdges = holeface->GetEdges();

                        if (allholesNX5.size() > 0)
                        {
                            allholesNX5.clear();
                            //ReDim allholesNX5(-1)
                        }
                        if (allholesNX6.size() > 0)
                        {
                            allholesNX6.clear();
                            //ReDim allholesNX6(-1)
                        }

                        for (unsigned int ii = 0; ii < selectedFaceEdges.size(); ++ii) 
                        {
                            NXOpen::Edge* seledge = selectedFaceEdges[ii];
                            NXOpen::Features::Feature* assocFeature = workPart->Features()->GetAssociatedFeature(seledge);
                            std::string featureString = std::string(assocFeature->FeatureType().GetUTF8Text());
                            if (featureString.find("HOLE") != std::string::npos)
                            {
                                if (featureString.find("SIMPLE") != std::string::npos)
                                {
                                    // Found NX5 type hole feature, add to NX 5 list
                                    allholesNX5.push_back(assocFeature->JournalIdentifier());
                                    //allholesNX5.push_back(featureString);
                                }
                                else
                                {
                                    // Found NX6 type hole feature, add to NX 6 list
                                    allholesNX6.push_back(assocFeature->JournalIdentifier());
                                    //allholesNX6.push_back(featureString);
                                }
                            }
#if 0
                            NXString journalstring = seledge->JournalIdentifier();
                            std::vector<std::string> individualstring = splitStrings(std::string(journalstring.GetUTF8Text()));
                            for (unsigned int jj = 0; jj < individualstring.size(); ++jj)
                            {
                                std::string featurestring = individualstring[jj];
                                if (featurestring.find("HOLE") != std::string::npos)
                                {
                                    if (featurestring.find("SIMPLE") != std::string::npos)
                                    {
                                        allholesNX5.push_back(featurestring);
                                        //Array.Resize(allholesNX5, allholesNX5.Length + 1)
                                        //allholesNX5.SetValue(featurestring, allholesNX5.Length - 1)
                                    }
                                    else
                                    {
                                        std::string tempString("SIMPLE ");
                                        tempString.append(featurestring);
                                        featurestring.clear();
                                        featurestring.append(tempString);
                                        allholesNX6.push_back(featurestring);
                                        //Array.Resize(allholesNX6, allholesNX6.Length + 1)
                                        //allholesNX6.SetValue(featurestring, allholesNX6.Length - 1)
                                    }
                                }
                            }
#endif
                        }
                        if (allholesNX5.size() == 0 && allholesNX6.size() == 0)
                        {
                            foundholes = false;
                            HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, "No hole features found on this face");
                            std::vector<NXOpen::TaggedObject* > tags1;
                            NXOpen::BlockStyler::PropertyList* faceProperties = face->GetProperties();
                            faceProperties->SetTaggedObjectVector("SelectedObjects", tags1);
                            delete faceProperties;
                            std::vector<NXOpen::NXString> liststrings = listBoxInfoProperties->GetStrings("ListItems");
                            liststrings.clear();
                            //ReDim liststrings(-1)
                            listBoxInfoProperties->SetStrings("ListItems", liststrings);

                            setEnablePropForBlock(buttonInfo, false);
                        }
                        else
                        {
                            if (allholesNX5.size() > 0)
                            {
                                for (unsigned int ii = 0; ii < allholesNX5.size(); ++ii)
                                {
                                    NXOpen::NXString nx5holes = allholesNX5[ii];
                                    NXOpen::Features::Feature* myFeature = workPart->Features()->FindObject(nx5holes);
                                    NXOpen::Features::Hole* myHoleFeature = dynamic_cast<NXOpen::Features::Hole* >(workPart->Features()->FindObject(nx5holes));
                                    holelocation = myFeature->Location();
                                    NXOpen::Point* point1 = workPart->Points()->CreatePoint(holelocation);
                                    double xcoord = holedimension(refaxis1, refaxis2, point1);
                                    double ycoord = holedimension(refaxis2, refaxis1, point1);
                                    std::vector<NXOpen::NXString> holedata;
                                    holedata.push_back(myFeature->JournalIdentifier());
                                    std::stringstream xCoordStream;
                                    xCoordStream << "X Coordinate = " << setprecision(16) << xcoord;
                                    holedata.push_back(NXString(xCoordStream.str().c_str()));
                                    std::stringstream yCoordStream;
                                    yCoordStream << "Y Coordinate = " << setprecision(16) << ycoord;
                                    holedata.push_back(NXString(yCoordStream.str().c_str()));
                                    std::vector<NXOpen::NXString> liststrings = listBoxInfoProperties->GetStrings("ListItems");
                                    liststrings.push_back(holedata[0]);
                                    liststrings.push_back(holedata[1]);
                                    liststrings.push_back(holedata[2]);
                                    listBoxInfoProperties->SetStrings("ListItems", liststrings);
                                }
                            }
                            if (allholesNX6.size() > 0)
                            {
                                for (unsigned int ii = 0; ii < allholesNX6.size(); ++ii)
                                {
                                    NXOpen::Features::BodyFeature* myFeature = dynamic_cast<NXOpen::Features::BodyFeature* >(workPart->Features()->FindObject(allholesNX6[ii]));
                                    NXOpen::Features::HolePackage* myHolePackage = dynamic_cast<NXOpen::Features::HolePackage* >(myFeature);
                                    //Point3d holeorigins() As  = Nothing
                                    NXOpen::Point* point1 = workPart->Points()->CreatePoint(myFeature->Location());
                                    double xcoord = holedimension(refaxis1, refaxis2, point1);
                                    double ycoord = holedimension(refaxis2, refaxis1, point1);
                                    std::vector<NXOpen::NXString> holedata1;
                                    holedata1.push_back(myFeature->JournalIdentifier());
                                    std::stringstream xCoordStream;
                                    xCoordStream << setprecision(16) << "X Coordinate = " << xcoord;
                                    holedata1.push_back(NXString(xCoordStream.str().c_str()));
                                    std::stringstream yCoordStream;
                                    yCoordStream << setprecision(16) << "Y Coordinate = " << ycoord;
                                    holedata1.push_back(NXString(yCoordStream.str().c_str()));
                                    std::vector<NXOpen::NXString> liststrings = listBoxInfoProperties->GetStrings("ListItems");
                                    liststrings.push_back(holedata1[0]);
                                    liststrings.push_back(holedata1[1]);
                                    liststrings.push_back(holedata1[2]);
                                    listBoxInfoProperties->SetStrings("ListItems", liststrings);
                                }
                            }
                        }
                    }
                }
                else
                {
                    HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, 
                        "Vectors not defined, please define the vectors for X and Y direction");
                }
                delete listBoxInfoProperties;
            }
            catch(exception& ex)
            {
                //---- Enter your exception handling code here -----
                HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());

            }
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        HoleCoordinates::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

double HoleCoordinates::holedimension(NXOpen::DatumAxis* refaxis1, NXOpen::DatumAxis* refaxis2, NXOpen::Point* refpoint1)
{
    NXOpen::NXObject* nullNXObject = NULL;

    NXOpen::MeasureDistanceBuilder* measureDistanceBuilder1 = 
        workPart->MeasureManager()->CreateMeasureDistanceBuilder(nullNXObject);

    measureDistanceBuilder1->SetInfoWindow(false);

    measureDistanceBuilder1->SetAnnotationMode(NXOpen::MeasureBuilder::AnnotationTypeShowDimension);

    measureDistanceBuilder1->SetMtype(NXOpen::MeasureDistanceBuilder::MeasureTypeMinimum);

    measureDistanceBuilder1->SetAnnotationMode(NXOpen::MeasureBuilder::AnnotationTypeNone);

    measureDistanceBuilder1->SetInfoWindow(false);

    NXOpen::DatumAxis* datumAxis1 = refaxis1;

    NXOpen::Direction* direction1 = workPart->Directions()->CreateDirection(refaxis1, NXOpen::SenseForward, NXOpen::SmartObject::UpdateOptionWithinModeling);

    measureDistanceBuilder1->SetProjectionVector(direction1);

    NXOpen::Point* point1 = refpoint1;

    NXOpen::Xform* nullXform = NULL;

    NXOpen::Point* point2 =
        workPart->Points()->CreatePoint(point1, nullXform, NXOpen::SmartObject::UpdateOptionAfterModeling);

    NXOpen::NXObject* nXObject1 = NULL; 
    NXOpen::Xform* xform1 = 
        workPart->Xforms()->CreateExtractXform(point1, NXOpen::SmartObject::UpdateOptionAfterModeling, false, &nXObject1);

    measureDistanceBuilder1->Object1()->SetValue(point2);

    measureDistanceBuilder1->Object2()->SetValue(refaxis2);

    NXOpen::Unit* nullUnit = NULL;

    NXOpen::MeasureDistance* measureDistance1 = 
        workPart->MeasureManager()->NewDistance(nullUnit, point2, refaxis2, direction1, NXOpen::MeasureManager::ProjectionTypeMinimum);

    holeCoordinates = measureDistance1->Value();

    measureDistanceBuilder1->Object2()->SetValue(NULL);

    measureDistanceBuilder1->Destroy();

    workPart->FacetedBodies()->DeleteTemporaryFacesAndEdges();

    return holeCoordinates;
}

NXOpen::DatumAxis* HoleCoordinates::datumaxiscreater(NXOpen::Point* point1, NXOpen::Direction* direction1)
{
    NXOpen::Features::Feature* nullFeatures_Feature = NULL;

    NXOpen::Features::DatumAxisBuilder* datumAxisBuilder1 = 
        workPart->Features()->CreateDatumAxisBuilder(nullFeatures_Feature);

    datumAxisBuilder1->SetType(NXOpen::Features::DatumAxisBuilder::TypesZcAxis);

    datumAxisBuilder1->SetAssociative(true);

    datumAxisBuilder1->SetResizedEndDistance(0.0);

    datumAxisBuilder1->SetType(NXOpen::Features::DatumAxisBuilder::TypesPointAndDir);

    datumAxisBuilder1->SetResizedEndDistance(0.0);

    datumAxisBuilder1->SetPoint(point1);

    datumAxisBuilder1->SetVector(direction1);

    datumAxisBuilder1->SetResizedEndDistance(50);

    NXOpen::NXObject* nXObject1 = datumAxisBuilder1->Commit();

    NXOpen::Features::DatumAxisFeature* datumaxisfeature1 = 
        dynamic_cast<NXOpen::Features::DatumAxisFeature*>(nXObject1);
    NXOpen::DatumAxis* datumaxis1 = datumaxisfeature1->DatumAxis();

    datumAxisBuilder1->Destroy();

    workPart->FacetedBodies()->DeleteTemporaryFacesAndEdges();

    return datumaxis1;
}

void HoleCoordinates::deletedatumaxis(std::vector<NXObject *> objects1)
{
    NXOpen::Session::UndoMarkId markId3 = 
        HoleCoordinates::theSession->SetUndoMark(NXOpen::Session::MarkVisibilityVisible, "Delete");

    int nErrs1 = HoleCoordinates::theSession->UpdateManager()->AddToDeleteList(objects1);

    bool notifyOnDelete2 = HoleCoordinates::theSession->Preferences()->Modeling()->NotifyOnDelete();
    workPart->ModelingViews()->WorkView()->Regenerate();

    int nErrs2 = HoleCoordinates::theSession->UpdateManager()->DoUpdate(markId3);
    HoleCoordinates::theSession->DeleteUndoMark(markId3, NULL);
}

NXOpen::DatumAxis* HoleCoordinates::editdatumaxis(NXOpen::DatumAxis* datumaxis1, NXOpen::Direction* vect1, NXOpen::Point* origpoint)
{
    NXOpen::Features::FeatureCollection* allfeaturescol = workPart->Features();
    NXOpen::Session::UndoMarkId markId1 =
        HoleCoordinates::theSession->SetUndoMark(NXOpen::Session::MarkVisibilityVisible, "Redefine Feature");
    NXOpen::Features::DatumAxisFeature* datumAxisFeature1 = 
        dynamic_cast<NXOpen::Features::DatumAxisFeature* >(workPart->Features()->FindObject(datumaxis1->JournalIdentifier()));
    datumAxisFeature1->MakeCurrentFeature();

    NXOpen::Features::DatumAxisBuilder* datumAxisBuilder1 =
        workPart->Features()->CreateDatumAxisBuilder(datumAxisFeature1);
    datumAxisBuilder1->SetPoint(origpoint);
    datumAxisBuilder1->SetVector(vect1);
    NXOpen::NXObject* nXObject1 = datumAxisBuilder1->Commit();
    datumAxisBuilder1->Destroy();

    int nErrs1 = HoleCoordinates::theSession->UpdateManager()->DoUpdate(markId1);

    NXOpen::Features::DatumAxisFeature* datumAxisFeature2 = 
        dynamic_cast<NXOpen::Features::DatumAxisFeature* >(nXObject1);
    std::vector<NXOpen::Features::Feature* > allfeatures = allfeaturescol->GetFeatures();
    allfeatures.back()->MakeCurrentFeature();
    HoleCoordinates::theSession->DeleteUndoMark(markId1, NULL);
    workPart->FacetedBodies()->DeleteTemporaryFacesAndEdges();
    return datumAxisFeature2->DatumAxis();
}

void HoleCoordinates::setEnablePropForBlock(NXOpen::BlockStyler::UIBlock* blk, bool value)
{
    NXOpen::BlockStyler::PropertyList* blkProperties = blk->GetProperties();
    blkProperties->SetLogical("Enable", value);
    delete blkProperties;
}

std::vector<std::string> HoleCoordinates::splitStrings(const std::string& stringToSplit)
{
    // Split strings into tokens assuming whitespace is the delimiter
    std::string buf; 
    std::stringstream ss(stringToSplit); 

    vector<std::string> tokens; 

    while (ss >> buf)
        tokens.push_back(buf);
    return tokens;
}


