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
#include "ColoredBlock.hpp"
#include <iostream>
#include <sstream>
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(ColoredBlock::theSession) = NULL;
UI *(ColoredBlock::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
ColoredBlock *theColoredBlock;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
ColoredBlock::ColoredBlock()
{
    try
    {
        // Initialize the NX Open C++ API environment
        theSession = NXOpen::Session::GetSession();
        ColoredBlock::theUI = UI::GetUI();
        theDialogName = "ColoredBlock.dlx";
        theDialog = ColoredBlock::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &ColoredBlock::apply_cb));
        theDialog->AddInitializeHandler(make_callback(this, &ColoredBlock::initialize_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &ColoredBlock::dialogShown_cb));
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
ColoredBlock::~ColoredBlock()
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
//            e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
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
        theColoredBlock = new ColoredBlock();
        // The following method shows the dialog immediately
        theColoredBlock->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        ColoredBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    delete theColoredBlock;
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
        ColoredBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int ColoredBlock::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        ColoredBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void ColoredBlock::initialize_cb()
{
    try
    {
        group0 = theDialog->TopBlock()->FindBlock("group0");
        blockHeight = theDialog->TopBlock()->FindBlock("blockHeight");
        blockWidth = theDialog->TopBlock()->FindBlock("blockWidth");
        blockLength = theDialog->TopBlock()->FindBlock("blockLength");
        blockOrigin = theDialog->TopBlock()->FindBlock("blockOrigin");
        blockColor = theDialog->TopBlock()->FindBlock("blockColor");

        // Set the upper-limits and lower-limits
        PropertyList *blockHeightProps = blockHeight->GetProperties();
        blockHeightProps->SetDouble("MaximumValue", 100.0);
        blockHeightProps->SetDouble("MinimumValue", 0.001);
        delete blockHeightProps;
        blockHeightProps = NULL;

        PropertyList *blockWidthProps = blockWidth->GetProperties();
        blockWidthProps->SetDouble("MaximumValue", 100.0);
        blockWidthProps->SetDouble("MinimumValue", 0.001);
        delete blockWidthProps;
        blockWidthProps = NULL;

        PropertyList *blockLengthProps = blockLength->GetProperties();
        blockLengthProps->SetDouble("MaximumValue", 100.0);
        blockLengthProps->SetDouble("MinimumValue", 0.001);
        delete blockLengthProps;
        blockLengthProps = NULL;
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        ColoredBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void ColoredBlock::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        ColoredBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int ColoredBlock::apply_cb()
{
    int errorCode = 0;
    Features::BlockFeatureBuilder *blockFeatureBuilder1 = NULL;
    try
    {
        Part *workPart(theSession->Parts()->Work());

        //Get the values from UI Blocks
        PropertyList *blockHeightProps = blockHeight->GetProperties();
        double theHeight = blockHeightProps->GetDouble("Value");
        delete blockHeightProps;
        blockHeightProps = NULL;

        // Convert Height in double to std::string
		std::ostringstream HeightBuffer; 
        HeightBuffer << theHeight; 
        std::string convertedHeight = HeightBuffer.str(); 

        PropertyList *blockWidthProps = blockWidth->GetProperties();
        double theWidth = blockWidthProps->GetDouble("Value");
        delete blockWidthProps;
        blockWidthProps = NULL;

        // Convert Width in double to std::string
        std::ostringstream WidthBuffer; 
        WidthBuffer << theWidth; 
        std::string convertedWidth = WidthBuffer.str(); 

        PropertyList *blockLengthProps = blockLength->GetProperties();
        double theLength = blockLengthProps->GetDouble("Value");
        delete blockLengthProps;
        blockLengthProps = NULL;

        // Convert Length in double to std::string
		std::ostringstream LengthBuffer;  
        LengthBuffer << theLength; 
        std::string convertedLength = LengthBuffer.str(); 

        PropertyList *blockOriginProps = blockOrigin->GetProperties();
        Point3d originPoint = blockOriginProps->GetPoint("Point");
        delete blockOriginProps;
        blockOriginProps = NULL;

        PropertyList *blockColorProps = blockColor->GetProperties();
        std::vector<int> color = blockColorProps->GetIntegerVector("Value");
        delete blockColorProps;
        blockColorProps = NULL;

        //Create the NX block
        Features::Feature *nullFeatures_Feature(NULL);
        blockFeatureBuilder1 = workPart->Features()->CreateBlockFeatureBuilder(nullFeatures_Feature);
        Body *nullBody(NULL);
        blockFeatureBuilder1->SetOriginAndLengths(originPoint, convertedHeight, convertedWidth, convertedLength);

        blockFeatureBuilder1->SetBooleanOperationAndTarget(Features::Feature::BooleanTypeCreate, nullBody);

        Features::Feature *feature1;
        feature1 = blockFeatureBuilder1->CommitFeature();
        blockFeatureBuilder1->Destroy();
        blockFeatureBuilder1 = NULL;

        // Get the body from Feature
        Features::BodyFeature* bodyFeat = dynamic_cast<Features::BodyFeature *>(feature1);
        std::vector<NXOpen::Body *> bodies = bodyFeat->GetBodies();

        // Apply the color to feature body
        DisplayModification *displayModification1;
        displayModification1 = theSession->DisplayManager()->NewDisplayModification();
        displayModification1->SetApplyToAllFaces(true);
        displayModification1->SetNewColor(color[0]);

        std::vector<DisplayableObject *> objects1(1);
        objects1[0] = bodies[0];
        displayModification1->Apply(objects1);
        delete displayModification1;
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        if (blockFeatureBuilder1)
        {
            blockFeatureBuilder1->Destroy();
            blockFeatureBuilder1 = NULL;
        }

        ColoredBlock::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}
