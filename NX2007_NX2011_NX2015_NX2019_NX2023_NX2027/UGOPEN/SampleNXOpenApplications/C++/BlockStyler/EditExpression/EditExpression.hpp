//=============================================================================
//
//                   Copyright (c) 2008 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//

#ifndef EDITEXPRESSION_H_INCLUDED
#define EDITEXPRESSION_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <uf_ui_types.h>
#include <iostream>
#include <NXOpen/Session.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/BlockStyler_PropertyList.hxx>
#include <NXOpen/BlockStyler_SetList.hxx>
#include <NXOpen/BlockStyler_ListBox.hxx>
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Forward declaration for Class
//------------------------------------------------------------------------------
class EditExpression;
namespace NXOpen 
{
    class Expression;
}
//
//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
extern EditExpression *theEditExpression;

class EditExpression
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    EditExpression();
    ~EditExpression();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the EditExpression.cpp file. 
    // You are REQUIRED to write the implementation for these funtions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    int filter_cb(NXOpen::BlockStyler::UIBlock*  block, NXOpen::TaggedObject* selectObject);
    
private:
    std::string theDialogName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::UIBlock* GroupFeatureSelection;// Block type: Group
    NXOpen::BlockStyler::SetList* FeatureList;// Block type: Set List
    NXOpen::BlockStyler::UIBlock* GroupExpressionList;// Block type: Group
    NXOpen::BlockStyler::UIBlock* ButtonGetExpressions;// Block type: Button
    NXOpen::BlockStyler::ListBox* ExpressionList;// Block type: List Box
    NXOpen::BlockStyler::UIBlock* GroupExpression;// Block type: Group
    NXOpen::BlockStyler::UIBlock* ExpressionName;// Block type: String
    NXOpen::BlockStyler::UIBlock* ExpressionValue;// Block type: Double
    
    NXOpen::BlockStyler::UIBlock* newBlock;// Block type: CompositeBlock
    std::vector<NXOpen::TaggedObject*> newFeatCol;
    NXOpen::Expression* expToEdit;
    int add_handler(SetList* list);
    int delete_handler(SetList* list, UIBlock* doomed);
    int reorder_handler(SetList* list, UIBlock* moved, int oldPos, int newPos);
};
#endif //EDITEXPRESSION_H_INCLUDED
