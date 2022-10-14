//=============================================================================
//
//                   Copyright (c) 2015 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//

#ifndef MISSINGWELDS_H_INCLUDED
#define MISSINGWELDS_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <map>
#include <utility>
#include <vector>
#include <NXOpen/BlockStyler_Wizard.hxx>
#include <uf_defs.h>

//------------------------------------------------------------------------------
// Forward declaration for Class
//------------------------------------------------------------------------------
class MissingWelds;
namespace NXOpen
{
    class DisplayableObject;
    class Session;
    class UI;

    namespace Assemblies
    {
        class ClearanceSet;
        class Component;
    }

    namespace BlockStyler
    {
        class BlockDialog;
        class Group;
        class Enumeration;
        class ListBox;
        class SelectObject;
        class UIBlock;
    }
}

class DllExport MissingWelds
{
    // class members
public:
    static NXOpen::Session *theSession;
    static NXOpen::UI *theUI;
    MissingWelds();
    ~MissingWelds();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementation
    // of these prototypes is provided in the MissingWelds.cpp file. 
    // You are REQUIRED to write the implementation for these functions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int ok_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    
    //int AddCallback (NXOpen::BlockStyler::ListBox* list_box);
    //int DeleteCallback(NXOpen::BlockStyler::ListBox* list_box);
    //------------------------------------------------------------------------------
    //Wizard specific callbacks
    //------------------------------------------------------------------------------
    int StepNotifyPreCallback(NXOpen::BlockStyler::Wizard* wizard, int nextStep);
    
    //void StepNotifyPostCallback(Wizard* wizard, int previousStep);
    
    bool IsStepOkayCallback(NXOpen::BlockStyler::Wizard* wizard, int step);
    
    void OnSubNodeCallback(NXOpen::BlockStyler::Wizard* wizard, int step, int subNodeId, NXOpen::BlockStyler::Wizard::SubNodeAction action);
    
    void OnMenuCallback(NXOpen::BlockStyler::Wizard* wizard, NXOpen::BlockStyler::Wizard::TaskNavigatorItem item, int step, int subNodeId);
    
    void OnMenuSelectionCallback(NXOpen::BlockStyler::Wizard* wizard, NXOpen::BlockStyler::Wizard::TaskNavigatorItem item, int step, int subNodeId, int commandIndex);
    
private:
    const char* theDlxFileName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::Wizard* missingWeldWizard;// Block type: Wizard
    NXOpen::BlockStyler::Group* clearanceSetStep;// Block type: Group
    NXOpen::BlockStyler::SelectObject* compSelection;// Block type: Selection
    NXOpen::BlockStyler::Group* resultsStep;// Block type: Group
    NXOpen::BlockStyler::Enumeration* compDisplay;// Block type: Enumeration
    NXOpen::BlockStyler::ListBox* missingWeldObjectsListBox;// Block type: List Box

    //------------------------------------------------------------------------------
    //User defined members
    //------------------------------------------------------------------------------
    NXOpen::Assemblies::ClearanceSet* theClearanceSet;
    bool wasSubNodeCreated;

    // contains all the components in the assembly, except root component
    std::vector<NXOpen::DisplayableObject*> allObjects;
    // contains a pair of objects for each checked sub node
    std::vector< std::pair<NXOpen::DisplayableObject*, NXOpen::DisplayableObject*> > checkedSubNodeObjects;
    // contains a pair of objects for each missing weld, indexed by subNodeId
    std::map<int, std::pair<NXOpen::DisplayableObject*, NXOpen::DisplayableObject*> > missingWelds;
    // temporarily hold the two displayable objects for the selected missing weld
    // for access by update_cb, apply_cb, and StepNotifyPreCallback methods
    NXOpen::DisplayableObject* selectedMissingWeldObjects[2];

    void AddChildren(NXOpen::Assemblies::Component* component);
};
#endif //MISSINGWELDS_H_INCLUDED
