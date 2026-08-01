//=============================================================================
//
//                   Copyright (c) 2011 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for Block Styler
//===============================================================================
//

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include "DimensionUDB.hpp"
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(DimensionUDB::theSession) = NULL;
UI *(DimensionUDB::theUI) = NULL;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
DimensionUDB::DimensionUDB()
{
    try
    {
        // Initialize the NX Open C++ API environment
        DimensionUDB::theSession = NXOpen::Session::GetSession();
        DimensionUDB::theUI = UI::GetUI();
        theDlxFileName = "DimensionUDB.dlx";
        theUserDefinedUIBlock = DimensionUDB::theUI->CreateDialog(theDlxFileName);
        // Registration of callback functions
        theUserDefinedUIBlock->AddUpdateHandler(make_callback(this, &DimensionUDB::update_cb));
        theUserDefinedUIBlock->AddInitializeHandler(make_callback(this, &DimensionUDB::initialize_cb));
        theUserDefinedUIBlock->AddDialogShownHandler(make_callback(this, &DimensionUDB::dialogShown_cb));
        theUserDefinedUIBlock->AddEnableOKButtonHandler(make_callback(this, &DimensionUDB::enableOKButton_cb));
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
DimensionUDB::~DimensionUDB()
{
    if (theUserDefinedUIBlock != NULL)
    {
        delete theUserDefinedUIBlock;
        theUserDefinedUIBlock = NULL;
    }
}
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void DimensionUDB::initialize_cb()
{
    try
    {
        sensitiveFlag = theUserDefinedUIBlock->TopBlock()->FindBlock("sensitiveFlag");
        Dimension = theUserDefinedUIBlock->TopBlock()->FindBlock("Dimension");
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        DimensionUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void DimensionUDB::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
        EnableDimensionField();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        DimensionUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int DimensionUDB::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == sensitiveFlag)
        {
        //---------Enter your code here-----------
            EnableDimensionField();
        }
        else if(block == Dimension)
        {
        //---------Enter your code here-----------
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        DimensionUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: enableOKButton_cb
//This callback allows the dialog to enable/disable the OK and Apply button.
//------------------------------------------------------------------------------
bool DimensionUDB::enableOKButton_cb()
{
    bool isEnableOKButton = true;
    try
    {
        //If the dimension value is zero then do not enable the OK/Apply button
        PropertyList* prop = Dimension->GetProperties();
        double value = prop->GetDouble("Value");
        delete prop;
        prop = NULL;

        if (0 == value)
        {
            isEnableOKButton = false;
        }            
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        DimensionUDB::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return isEnableOKButton;
}

//------------------------------------------------------------------------------
//Function Name: RegisterUserDefinedUIBlock
//Description: Registers itself to the dialog which contains this block
//------------------------------------------------------------------------------
DimensionUDB* DimensionUDB::RegisterUserDefinedUIBlock(NXOpen::BlockStyler::BlockDialog* parentDialog, const char* blockID)
{
    DimensionUDB* theDimensionUDB = new DimensionUDB();
    parentDialog->RegisterUserDefinedUIBlock(theDimensionUDB->theUserDefinedUIBlock, blockID);
    return theDimensionUDB;
}

//------------------------------------------------------------------------------
//Function Name: GetTopBlock
//Function returning TopBlock
//------------------------------------------------------------------------------
NXOpen::BlockStyler::CompositeBlock* DimensionUDB::GetTopBlock()
{
    if(theUserDefinedUIBlock != NULL)
    {
        return theUserDefinedUIBlock->TopBlock();
    }
    else
    {
        return NULL;
    }
}

//Sets the label on the double block
void DimensionUDB::SetLabel(const char* label)
{
    PropertyList* prop = Dimension->GetProperties();
    prop->SetString("Label", label);
    delete prop;
    prop = NULL;
}

//Sets the value of the double block
void DimensionUDB::SetValue(const double value)
{
    PropertyList* prop = Dimension->GetProperties();
    prop->SetDouble("Value", value);
    delete prop;
    prop = NULL;
}

//Sets the value of the double block
double DimensionUDB::GetValue() const
{
    PropertyList* prop = Dimension->GetProperties();
    double value = prop->GetDouble("Value");
    delete prop;
    prop = NULL;

    return value;
}

//Enables/Disables the double block based on toggle. If toggled on, the double-field is disabled
void DimensionUDB::EnableDimensionField()
{
    PropertyList* prop = sensitiveFlag->GetProperties();
    bool flag = prop->GetLogical("Value");
    delete prop;
    prop = NULL;

    //Disable double block if toggle field is on
    PropertyList* dimensionPropertyList = Dimension->GetProperties();
    dimensionPropertyList->SetLogical("Enable", !flag);
    delete dimensionPropertyList;
    dimensionPropertyList = NULL;
}

