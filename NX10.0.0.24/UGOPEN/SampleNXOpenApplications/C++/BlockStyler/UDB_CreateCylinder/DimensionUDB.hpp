//=============================================================================
//
//                   Copyright (c) 2011 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for Block Styler
//===============================================================================
//

//------------------------------------------------------------------------------
//Description:
//------------------------------------------------------------------------------
//This is the implementation for the User Defined UI Block (UDB) CreateCylinder_UsingUDB.dlx
//-Provides default value through Combo options
//-Enables/Disables the double-field based on toggle state. If toggle-field is set to true then 
// double-field is disable. Refer to dialogShown_cb and update_cb
//-If double-field value is zero then OK/Apply of parent dialog is disabled. Refer to enableOKButton_cb


#ifndef DIMENSIONUDB_H_INCLUDED
#define DIMENSIONUDB_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <uf_ui_types.h>
#include <iostream>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/BlockStyler_PropertyList.hxx>
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

class DllExport DimensionUDB
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    DimensionUDB();
    ~DimensionUDB();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the DimensionUDB.cpp file. 
    // You are REQUIRED to write the implementation for these funtions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    bool enableOKButton_cb();
    
    static DimensionUDB* RegisterUserDefinedUIBlock(NXOpen::BlockStyler::BlockDialog* parentDialog, const char* blockID);
    NXOpen::BlockStyler::CompositeBlock* GetTopBlock();

    //-------------------Added Function--------------------

    //Sets the label on the double block
    void SetLabel(const char* label);

    //Gets/Sets the value of the double block
    void SetValue(const double value);
    double GetValue() const;

private:
    const char* theDlxFileName;
    NXOpen::BlockStyler::BlockDialog* theUserDefinedUIBlock;
    NXOpen::BlockStyler::UIBlock* sensitiveFlag;// Block type: Toggle
    NXOpen::BlockStyler::UIBlock* Dimension;// Block type: Double

    //Enables/Disables the double block based on toggle. If toggled on, the double-field is disabled
    void EnableDimensionField();    
};
#endif //DIMENSIONUDB_H_INCLUDED
