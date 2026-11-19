//===============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for Block Styler
//===============================================================================
//

//  WARNING!!  This file is overwritten by the Block UI Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.

//================================================================================

//================================================================================
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
//================================================================================

//--------------------------------------------------------------------------------
//These includes are needed for the following template code
//--------------------------------------------------------------------------------
#include "TreeListDemo.hpp"
#include <sstream>
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(TreeListDemo::theSession) = NULL;
UI *(TreeListDemo::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
TreeListDemo *theTreeListDemo;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
TreeListDemo::TreeListDemo()
{
    try
    {
        // Initialize the NX Open C++ API environment
        TreeListDemo::theSession = NXOpen::Session::GetSession();
        TreeListDemo::theUI = UI::GetUI();
        theDialogName = "TreeListDemo.dlx";
        theDialog = TreeListDemo::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &TreeListDemo::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &TreeListDemo::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &TreeListDemo::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &TreeListDemo::initialize_cb));
        theDialog->AddFocusNotifyHandler(make_callback(this, &TreeListDemo::focusNotify_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &TreeListDemo::dialogShown_cb));
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
TreeListDemo::~TreeListDemo()
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
    try
    {
        theTreeListDemo = new TreeListDemo();
        // The following method shows the dialog immediately
        theTreeListDemo->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    delete theTreeListDemo;
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
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int TreeListDemo::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb

NXOpen::NXString nodeBaseString;
int nodeSuffixNumber = 0;
//------------------------------------------------------------------------------
void TreeListDemo::initialize_cb()
{
    try
    {
        group0 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("group0"));
        tree_control0 = dynamic_cast<NXOpen::BlockStyler::Tree* >(theDialog->TopBlock()->FindBlock("tree_control0"));
        addDeleteNodeGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("addDeleteNodeGroup"));
        nodeString = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("nodeString"));
        addNodeButton = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("addNodeButton"));
        deleteNodeButton = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("deleteNodeButton"));
        stateIconGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("stateIconGroup"));
        stateIconOptions = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("stateIconOptions"));
        nodeToolTip = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("nodeToolTip"));
        NodeEditGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("NodeEditGroup"));
        nodeEditOptions = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("nodeEditOptions"));
        menuGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("menuGroup"));
        showMenuToggle = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("showMenuToggle"));
        dragDropGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("dragDropGroup"));
        disallowDragToggle = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("disallowDragToggle"));
        dropOptions = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("dropOptions"));
        defaultActionGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("defaultActionGroup"));
        defaultActionToggle = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("defaultActionToggle"));
        nodeDataGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("nodeDataGroup"));
        instructions = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("instructions"));
        selection0 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("selection0"));
        addCrossSelectionNodeButton = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("addCrossSelectionNodeButton"));
        redrawGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("redrawGroup"));
        redrawInstruction = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("redrawInstruction"));
        redrawToggle = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("redrawToggle"));
        listingWindowGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("listingWindowGroup"));
        listingWindowToggle = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("listingWindowToggle"));
        //------------------------------------------------------------------------------
        //Registration of Treelist specific callbacks
        //------------------------------------------------------------------------------
        //tree_control0->SetOnExpandHandler(make_callback(this, &TreeListDemo::OnExpandCallback));

        //tree_control0->SetOnInsertColumnHandler(make_callback(this, &TreeListDemo::OnInsertColumnCallback));

        tree_control0->SetOnInsertNodeHandler(make_callback(this, &TreeListDemo::OnInsertNodeCallback));

        tree_control0->SetOnDeleteNodeHandler(make_callback(this, &TreeListDemo::OnDeleteNodeCallback));

        //tree_control0->SetOnPreSelectHandler(make_callback(this, &TreeListDemo::OnPreSelectCallback));

        tree_control0->SetOnSelectHandler(make_callback(this, &TreeListDemo::OnSelectCallback));

        tree_control0->SetOnStateChangeHandler(make_callback(this, &TreeListDemo::OnStateChangeCallback));

        tree_control0->SetToolTipTextHandler(make_callback(this, &TreeListDemo::ToolTipTextCallback));

        //tree_control0->SetColumnSortHandler(make_callback(this, &TreeListDemo::ColumnSortCallback));

        tree_control0->SetStateIconNameHandler(make_callback(this, &TreeListDemo::StateIconNameCallback));

        tree_control0->SetOnBeginLabelEditHandler(make_callback(this, &TreeListDemo::OnBeginLabelEditCallback));

        tree_control0->SetOnEndLabelEditHandler(make_callback(this, &TreeListDemo::OnEndLabelEditCallback));        

        tree_control0->SetOnEditOptionSelectedHandler(make_callback(this, &TreeListDemo::OnEditOptionSelectedCallback));

        tree_control0->SetAskEditControlHandler(make_callback(this, &TreeListDemo::AskEditControlCallback));

        tree_control0->SetOnMenuHandler(make_callback(this, &TreeListDemo::OnMenuCallback));

        tree_control0->SetOnMenuSelectionHandler(make_callback(this, &TreeListDemo::OnMenuSelectionCallback));

        tree_control0->SetIsDropAllowedHandler(make_callback(this, &TreeListDemo::IsDropAllowedCallback));

        tree_control0->SetIsDragAllowedHandler(make_callback(this, &TreeListDemo::IsDragAllowedCallback));

        tree_control0->SetOnDropHandler(make_callback(this, &TreeListDemo::OnDropCallback));

        //tree_control0->SetOnDropMenuHandler(make_callback(this, &TreeListDemo::OnDropMenuCallback));

        tree_control0->SetOnDefaultActionHandler(make_callback(this, &TreeListDemo::OnDefaultAction));

        //------------------------------------------------------------------------------

        BlockStyler::PropertyList *stringPropList = nodeString->GetProperties() ;
        nodeBaseString = stringPropList->GetString("Value");    
        NXOpen::NXString nodeDisplayString = nodeBaseString;
        std::stringstream stringBuffer;
        stringBuffer << nodeSuffixNumber;            
        nodeDisplayString += stringBuffer.str();                
        stringPropList->SetString("Value",nodeDisplayString);            
        delete stringPropList;
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

enum Columns
{
    ColumnFirst = 0,
    ColumnSecond = 1,
    ColumnThird = 2
};
BlockStyler::Node *previousAddedNode = NULL;    
int randomIcon = 0;
NXOpen::NXString randomIconString[] = {"extrude", "cone", "block", "blend"};

    


//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void TreeListDemo::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----

        //Insert Columns        
        tree_control0->InsertColumn(ColumnFirst, "First Column", 80);
        tree_control0->InsertColumn(ColumnSecond, "Second Column", 80);
        tree_control0->InsertColumn(ColumnThird, "Third Column", 80);

        //Set resize policy for columns
        tree_control0->SetColumnResizePolicy(ColumnFirst, Tree::ColumnResizePolicyConstantWidth);
        tree_control0->SetColumnResizePolicy(ColumnSecond, Tree::ColumnResizePolicyConstantWidth);
        tree_control0->SetColumnResizePolicy(ColumnThird, Tree::ColumnResizePolicyConstantWidth);

        //Let the second column interpret the text as icon
        tree_control0->SetColumnDisplayType(ColumnSecond, Tree::ColumnDisplayIcon);        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int TreeListDemo::apply_cb()
{
    int errorCode = 0;
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}


BlockStyler::Node* TreeListDemo::CreateAndAddNode(BlockStyler::Node* afterNode)
{
    BlockStyler::Node *parentNode = NULL;

    //Get node display string from the block
    BlockStyler::PropertyList *stringPropList = nodeString->GetProperties() ;
    NXOpen::NXString nodeDisplayString = stringPropList->GetString("Value");
    delete stringPropList;

    BlockStyler::Node *node = tree_control0->CreateNode(nodeDisplayString);

    //Set few properties of node
    node->SetForegroundColor(198);
    node->SetDisplayIcon(randomIconString[randomIcon]);
    node->SetSelectedIcon("draft");

    //Take first selected node as parent node    
    std::vector<BlockStyler::Node *>selectedNodes=tree_control0->GetSelectedNodes();
    if (selectedNodes.size()>0)
    {
        parentNode = selectedNodes[0];    
    }

    //Insert Node
    tree_control0->InsertNode(node,parentNode,afterNode,tree_control0->NodeInsertOptionSort);
    node->ScrollTo(ColumnFirst,BlockStyler::Node::ScrollCenter);

    //Change the last node color. Making sure that new node color is distinct
    if (previousAddedNode != NULL)
    {
        previousAddedNode->SetForegroundColor(211);
    }
    previousAddedNode = node;    
    
    return node;    
}


void TreeListDemo::DeleteSelectedNodes()
{
    std::vector<BlockStyler::Node *>selectedNodes=tree_control0->GetSelectedNodes();                
    if(selectedNodes.size()>0)
    {
        while(selectedNodes.size()>0)
        {
            tree_control0->DeleteNode(selectedNodes[0]);
            selectedNodes=tree_control0->GetSelectedNodes();
        }
    }
    else
    {
        theUI->NXMessageBox()->Show("Delete Node", NXOpen::NXMessageBox::DialogTypeInformation, "No Nodes are selected");
    } 
}

//Writes callback name to ListingWindow
void TreeListDemo::WriteCallbackToListingWindow(NXString callbackName)
{
    if (!listingWindowToggle)
        return;
    try
    {
        //---- Enter your callback code here -----

        NXOpen::BlockStyler::PropertyList *listingWindowToggleProps = listingWindowToggle->GetProperties();
        bool listingWindow = listingWindowToggleProps->GetLogical("Value");
        delete listingWindowToggleProps;

        if(listingWindow)
        {
            theSession->ListingWindow()->Open();
            NXString nullString = NULL;
            theSession->ListingWindow()->WriteLine(nullString);
            theSession->ListingWindow()->WriteLine(callbackName);
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}


//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int TreeListDemo::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == nodeString)
        {
            //---------Enter your code here-----------
        }
        else if(block == addNodeButton)
        {
            //---------Enter your code here-----------
            BlockStyler::Node *afterNode = NULL;
            BlockStyler::Node *node = CreateAndAddNode(afterNode);

            //State Icon

            BlockStyler::PropertyList *prop = stateIconOptions->GetProperties();
            int enumValue = prop->GetEnum("Value");
            delete prop;

            if(enumValue==0)
            {
                //Ignore
            }
            else if(enumValue==1)
            {
                node->SetState(1);
            }
            else if(enumValue==2)
            {
                node->SetState(3);//set value other than 1 or 2
            }
        }
        else if(block == deleteNodeButton)
        {
            //---------Enter your code here-----------
            DeleteSelectedNodes();            
        }
        else if(block == stateIconOptions)
        {
            //---------Enter your code here-----------
        }
        else if(block == nodeToolTip)
        {
            //---------Enter your code here-----------
        }
        else if(block == nodeEditOptions)
        {
            //---------Enter your code here-----------
            if (!defaultActionToggle)
            {
                return 0;
            }

            NXOpen::BlockStyler::PropertyList *nodeEditOptionsProps = nodeEditOptions->GetProperties();
            NXString nodeEditOption = nodeEditOptionsProps->GetEnumAsString("Value");
            delete nodeEditOptionsProps;

            NXOpen::BlockStyler::PropertyList *defaultActionToggleProps = defaultActionToggle->GetProperties();

            if(!(strcmp(nodeEditOption.GetText(),"Combo Box Edit"))||!(strcmp(nodeEditOption.GetText(),"Listbox Edit")))
            {
                defaultActionToggleProps->SetLogical("Enable",false);
                defaultActionToggleProps->SetLogical("Value",false);
            }
            else
            {
                defaultActionToggleProps->SetLogical("Enable",true);
            }
            delete defaultActionToggleProps;
        }
        else if(block == showMenuToggle)
        {
            //---------Enter your code here-----------
        }
        else if(block == disallowDragToggle)
        {
            //---------Enter your code here-----------
        }
        else if(block == dropOptions)
        {
            //---------Enter your code here-----------
        }
        else if(block == defaultActionToggle)
        {
            //---------Enter your code here-----------
        }
        else if(block == instructions)
        {
            //---------Enter your code here-----------
        }
        else if(block == selection0)
        {
            //---------Enter your code here-----------
        }
        else if(block == addCrossSelectionNodeButton)
        {
            //---------Enter your code here-----------
            BlockStyler::PropertyList *prop = selection0->GetProperties();
            std::vector<NXOpen::TaggedObject *>objects = prop->GetTaggedObjectVector("SelectedObjects");

            if (objects.size()>0)
            {
                //Create node and node data
                BlockStyler::Node *node = tree_control0->CreateNode("CrossSelection-NodeData");
                NXOpen::DataContainer *nodeData = node->GetNodeData();
                nodeData->AddTaggedObject("Data",objects[0]);
                delete nodeData;
                tree_control0->InsertNode(node,NULL,NULL,tree_control0->NodeInsertOptionAlwaysLast);

                //Reset Selection block
                std::vector<TaggedObject *>blank;            
                prop->SetTaggedObjectVector("SelectedObjects",blank);
            }
            delete prop;                     
        }
        else if(block == redrawInstruction)
        {
            //---------Enter your code here-----------
        }
        else if(block == redrawToggle)
        {
            //---------Enter your code here-----------
            BlockStyler::PropertyList *prop = redrawToggle->GetProperties();
            bool isRedraw = prop->GetLogical("Value");
            delete prop;
            tree_control0->Redraw(isRedraw);            
        }
        else if(block == listingWindowToggle)
        {
            //---------Enter your code here-----------
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int TreeListDemo::ok_cb()
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
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: focusNotify_cb
//This callback is executed when any block (except the ones which receive keyboard entry such as Integer block) receives focus.
//------------------------------------------------------------------------------
void TreeListDemo::focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
//------------------------------------------------------------------------------
//Treelist specific callbacks
//------------------------------------------------------------------------------
//void TreeListDemo::OnExpandCallback (NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node)
//{
//}

//void TreeListDemo::OnInsertColumnCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID)
//{
//}

void TreeListDemo::OnInsertNodeCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node)
{
    try
    {
        //---- Enter your callback code here -----
        WriteCallbackToListingWindow("OnInsertNodeCallback Invoked");

        //Setting random icon
        if (randomIcon==0)
        {
            node->SetColumnDisplayText(ColumnSecond,randomIconString[randomIcon]);
        }
        else if (randomIcon==1)
        {
            node->SetColumnDisplayText(ColumnSecond,randomIconString[randomIcon]);
        }
        else if (randomIcon==2)
        {
            node->SetColumnDisplayText(ColumnSecond,randomIconString[randomIcon]);
        }
        else if (randomIcon==3)
        {
            node->SetColumnDisplayText(ColumnSecond,randomIconString[randomIcon]);
        }
        randomIcon = randomIcon + 1;
        if (randomIcon > 3)
        {
            randomIcon = 0;
        }

        std::stringstream stringBuffer;
        stringBuffer << "Column Text - "<<randomIcon;
        NXOpen::NXString columnText ;
        columnText += stringBuffer.str();
        node->SetColumnDisplayText(ColumnThird,columnText);

        if (nodeSuffixNumber == 15000)
        {
            nodeSuffixNumber = 0;
        }
        else
        {
            nodeSuffixNumber = nodeSuffixNumber + 1;
        }

        //New Node text for the next node
        std::stringstream stringBuffer1;
        BlockStyler::PropertyList *prop = nodeString->GetProperties();        

        NXOpen::NXString nodeDisplayString = nodeBaseString;
        stringBuffer1 << nodeSuffixNumber;
        nodeDisplayString += stringBuffer1.str();
        prop->SetString("Value",nodeDisplayString);
        delete prop;
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

void TreeListDemo::OnDeleteNodeCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node)
{
    try
    {
        //---- Enter your callback code here -----
        WriteCallbackToListingWindow("OnDeleteNodeCallback Invoked");

        if(node==previousAddedNode)
        {
            //Set the previous node to Nothing. Done for safe execution.
            previousAddedNode = NULL;
        }          
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//void TreeListDemo::OnPreSelectCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int ID, bool selected)
//{
//}

void TreeListDemo::OnSelectCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID, bool selected)
{
    std::stringstream column;
    column << columnID;

    std::string text = std::string("OnSelectCallback Invoked: Node \"") + std::string(node->DisplayText().GetText()) + std::string("\" ") +  std::string(selected?"Selected":"Deselected") + std::string(selected?" at column ":"") + std::string(selected?column.str():"");
    WriteCallbackToListingWindow(text);    
}

void TreeListDemo::OnStateChangeCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int state)
{
    try
    {
        //---- Enter your callback code here -----
        WriteCallbackToListingWindow("OnStateChangeCallback Invoked");
        if (state == 1)
        {
            node->SetState(2);
        }
        else if(state == 2)
        {
            node->SetState(1);
        }
        else if(state == 3)
        {
            node->SetState(4);
        }
        else if(state == 4)
        {
            node->SetState(3);
        }          
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

NXString TreeListDemo::ToolTipTextCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID)
{
    NXOpen::NXString ToolTipText;
    try
    {
        //---- Enter your callback code here -----

        BlockStyler::PropertyList *prop = nodeToolTip->GetProperties();
        ToolTipText = prop->GetString("Value");        
        delete prop;
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return ToolTipText;    
}
//The possible return values are 0, positive and negative value, suggesting respectively that both nodes are same, first node greater than second, and first node smaller than second.
//int TreeListDemo::ColumnSortCallback(NXOpen::BlockStyler::Tree *tree, int columnID, NXOpen::BlockStyler::Node *node1, NXOpen::BlockStyler::Node *node2)
//{
//}

NXString TreeListDemo::StateIconNameCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int state)
{
    NXOpen::NXString stateIcon;
    try
    {
        //---- Enter your callback code here -----
        WriteCallbackToListingWindow("StateIconNameCallback Invoked");
        if(state==3)
        {
            stateIcon = "hole";
        }
        else if(state==4)
        {
            stateIcon = "boss";
        }
        else if(state==5)
        {
            stateIcon = "revolve";
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return stateIcon;
}

NXOpen::BlockStyler::Tree::BeginLabelEditState TreeListDemo::OnBeginLabelEditCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID)
{
    NXOpen::BlockStyler::Tree::BeginLabelEditState OnBeginLabelEdit = BlockStyler::Tree::BeginLabelEditStateDisallow;
    try
    {
        //---- Enter your callback code here -----
        WriteCallbackToListingWindow("OnBeginLabelEditCallback Invoked");
        BlockStyler::PropertyList *prop = nodeEditOptions->GetProperties();
        int labelEditOption = prop->GetEnum("Value");
        delete prop;

        if (labelEditOption==1)
        {
            OnBeginLabelEdit = BlockStyler::Tree::BeginLabelEditStateAllow;
        }
        else
        {
            OnBeginLabelEdit = BlockStyler::Tree::BeginLabelEditStateDisallow;
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }

    return OnBeginLabelEdit;

}

NXOpen::BlockStyler::Tree::EndLabelEditState TreeListDemo::OnEndLabelEditCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int, NXString editedText)
{
    NXOpen::BlockStyler::Tree::EndLabelEditState OnEndLabelEdit = BlockStyler::Tree::EndLabelEditStateRejectText;
    try
    {
        //---- Enter your callback code here -----
        WriteCallbackToListingWindow("OnEndLabelEditCallback Invoked");

        if(0 == strcmp(editedText.GetText(),"Reject") )
        {
            OnEndLabelEdit = BlockStyler::Tree::EndLabelEditStateRejectText;
        }
        else
        {
            OnEndLabelEdit = BlockStyler::Tree::EndLabelEditStateAcceptText;
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }

    return OnEndLabelEdit;

}

NXOpen::BlockStyler::Tree::EditControlOption TreeListDemo::OnEditOptionSelectedCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID, int selectedOptionID, NXString selectedOptionText, NXOpen::BlockStyler::Tree::ControlType type)
{
    NXOpen::BlockStyler::Tree::EditControlOption OnEditOptionSelected = BlockStyler::Tree::EditControlOptionReject;    
    try
    {
        //---- Enter your callback code here -----

        if (BlockStyler::Tree::ControlTypeComboBox == type)
        {
            if (0 == strcmp(selectedOptionText.GetText(),"ComboBox-RejectText"))
            {
                OnEditOptionSelected = BlockStyler::Tree::EditControlOptionReject;
            }
            else
            {
                OnEditOptionSelected = BlockStyler::Tree::EditControlOptionAccept;
            }
        }
        else if (BlockStyler::Tree::ControlTypeListBox == type)
        {
            if (0 == strcmp(selectedOptionText.GetText(),"ListBox-RejectText"))
            {
                OnEditOptionSelected = BlockStyler::Tree::EditControlOptionReject;
            }
            else
            {
                OnEditOptionSelected = BlockStyler::Tree::EditControlOptionAccept;
            }
        }                          
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }

    return OnEditOptionSelected;
}

NXOpen::BlockStyler::Tree::ControlType TreeListDemo::AskEditControlCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID)
{
    NXOpen::BlockStyler::Tree::ControlType AskEditControl = BlockStyler::Tree::ControlTypeNone;;

    try
    {
        //---- Enter your callback code here -----
        BlockStyler::PropertyList *prop = nodeEditOptions->GetProperties();
        int labelEditOption = prop->GetEnum("Value");
        delete prop;

        if(labelEditOption==2)
        {
            AskEditControl = BlockStyler::Tree::ControlTypeComboBox;  
            std::vector<NXOpen::NXString> options;
            options.push_back(NXOpen::NXString("ComboBox-AcceptText"));
            options.push_back(NXOpen::NXString("ComboBox-DefaultText"));
            options.push_back(NXOpen::NXString("ComboBox-RejectText"));
            tree->SetEditOptions(options,1);    
        }
        else if(labelEditOption==3)
        {
            AskEditControl = BlockStyler::Tree::ControlTypeListBox;
            
            std::vector<NXOpen::NXString> options;
            options.push_back(NXOpen::NXString("ListBox-AcceptText"));
            options.push_back(NXOpen::NXString("ListBox-DefaultText"));
            options.push_back(NXOpen::NXString("ListBox-RejectText"));

            tree->SetEditOptions(options,1);        
        }                                   
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return AskEditControl;
}

enum MenuID
{
    AddNode = 0,
    DeleteNode,
    CheckedMenuItem,
    DefaultMenuItem,
    DialogLaunchMenuItem,
    DisableMenuItem,
    HiddenMenuItem,
    IconMenuItem,

    SubMenu1,
    SubMenu2,
    SubMenuItem1,
    SubMenuItem2,
    SubMenuItem3,
    SubMenuItem4,

    TreeMenuItem,
};


void TreeListDemo::OnMenuCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID)
{
    try
    {
        //---- Enter your callback code here -----
        WriteCallbackToListingWindow("OnMenuCallback Invoked");
        BlockStyler::PropertyList *prop = showMenuToggle->GetProperties() ;
        bool value = prop->GetLogical("Value");
        delete prop;

        if(value == false)
        {
            return;
        }

        //Create Menu
        BlockStyler::TreeListMenu *menu = tree->CreateMenu();
        BlockStyler::TreeListMenu *SubMenu1 = tree->CreateMenu();
        BlockStyler::TreeListMenu *SubMenu2 = tree->CreateMenu();


        if(node==NULL)
        {
            menu->AddMenuItem(AddNode,"Add Node");
            menu->AddSeparator();
            menu->AddMenuItem(TreeMenuItem,"Tree menu item");            
        }
        else //Menu request for Node
        {
            menu->AddMenuItem(AddNode,"Add Node");
            menu->AddMenuItem(MenuID(DeleteNode),"Delete Node");


            menu->AddSeparator();
            menu->AddMenuItem(CheckedMenuItem,"Checked Menu Item");
            menu->AddMenuItem(DefaultMenuItem,"Default Menu Item");
            menu->AddMenuItem(DialogLaunchMenuItem,"Dialog Launch Menu Item");
            menu->AddMenuItem(DisableMenuItem,"Disable Menu Item");
            menu->AddMenuItem(HiddenMenuItem,"Hidden Menu Item");
            menu->AddMenuItem(IconMenuItem,"Icon Menu Item");

            menu->AddSeparator();
            menu->AddMenuItem(::SubMenu1,"Sub Menu 1");
            menu->AddMenuItem(::SubMenu2,"Sub Menu 2");

            //Sub Menu
            SubMenu1->AddMenuItem(SubMenuItem1,"Sub Menu Item 1");
            SubMenu1->AddMenuItem(SubMenuItem2,"Sub Menu Item 2");

            SubMenu2->AddMenuItem(SubMenuItem3,"Sub Menu Item 3");
            SubMenu2->AddMenuItem(SubMenuItem4,"Sub Menu Item 4");

            //Set Sub Menu
            menu->SetSubMenu(::SubMenu1,SubMenu1);
            menu->SetSubMenu(::SubMenu2,SubMenu2);

            //Edit Menu Items
            menu->SetItemChecked(CheckedMenuItem,true);
            menu->SetItemDefault(DefaultMenuItem,true);
            menu->SetItemDialogLaunching(DialogLaunchMenuItem,true);
            menu->SetItemDisable(DisableMenuItem,true);
            menu->SetItemHidden(HiddenMenuItem,true);
            menu->SetItemIcon(IconMenuItem,"sketch");
        }

        //Set menu on tree
        tree->SetMenu(menu);

        //Dispose the menu only after setting the menu on tree
        delete menu;
        delete SubMenu1;
        delete SubMenu2;            
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

void TreeListDemo::OnMenuSelectionCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int menuItemID)
{
    try
    {
        //---- Enter your callback code here -----
        WriteCallbackToListingWindow("OnMenuSelectionCallback Invoked");
        if(node==NULL)
        {
            if((MenuID)menuItemID == AddNode)
            {
                CreateAndAddNode(NULL);
            }
        }
        else 
        {
            if((MenuID)menuItemID == AddNode)
            {
                CreateAndAddNode(NULL);
            }
            else if((MenuID)menuItemID == DeleteNode)
            {
                std::vector<BlockStyler::Node *>SelectedNodes = tree_control0->GetSelectedNodes();
                if(SelectedNodes.size()>0)
                {
                    DeleteSelectedNodes();
                }
                else 
                {                        
                    if(node!=NULL)
                    {
                        tree->DeleteNode(node);
                    }                        
                }
            }
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

NXOpen::BlockStyler::Node::DropType TreeListDemo::IsDropAllowedCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID, NXOpen::BlockStyler::Node *targetNode, int targetColumnID)
{
    NXOpen::BlockStyler::Node::DropType IsDropAllowed;
    try
    {
        //---- Enter your callback code here -----
        BlockStyler::PropertyList *prop = dropOptions->GetProperties() ;
        int dropOption = prop->GetEnum("Value");
        delete prop;

        // This will just show iconic representation that drop is allowed. No default action is performed after drop.
        // OnDropCallback should be implemented for specific drop behaviour

        if (dropOption == 0)
        {
            IsDropAllowed = BlockStyler::Node::DropTypeNone;
        }
        else if (dropOption == 1)
        {
            IsDropAllowed = BlockStyler::Node::DropTypeAfter;
        }
        else if (dropOption == 2)
        {
            IsDropAllowed = BlockStyler::Node::DropTypeBefore;
        }
        else if (dropOption == 3)
        {
            IsDropAllowed = BlockStyler::Node::DropTypeBeforeAndAfter;
        }
        else if (dropOption == 4)
        {
            IsDropAllowed = BlockStyler::Node::DropTypeOn;
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return IsDropAllowed;
}

NXOpen::BlockStyler::Node::DragType TreeListDemo::IsDragAllowedCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID)
{
    NXOpen::BlockStyler::Node::DragType IsDragAllowedCallback;
    try
    {
        //---- Enter your callback code here -----
        BlockStyler::PropertyList *prop = disallowDragToggle->GetProperties() ;
        bool isDragDisallowed = prop->GetLogical("Value");
        delete prop;

        if(isDragDisallowed == true)
        {
            IsDragAllowedCallback = BlockStyler::Node::DragTypeNone;
        }
        else
        {
            IsDragAllowedCallback = BlockStyler::Node::DragTypeAll;
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }

    return IsDragAllowedCallback;
}

bool TreeListDemo::OnDropCallback(NXOpen::BlockStyler::Tree *tree, std::vector<NXOpen::BlockStyler::Node *> node, int columnID, NXOpen::BlockStyler::Node *targetNode, int targetColumnID, NXOpen::BlockStyler::Node::DropType dropType, int dropMenuItemId)
{
    try
    {
        //---- Enter your callback code here -----
        WriteCallbackToListingWindow("OnDropCallback Invoked");
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return true;
}

//void TreeListDemo::OnDropMenuCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID, NXOpen::BlockStyler::Node *targetNode, int targetColumnID)
//{
//}

void TreeListDemo::OnDefaultAction(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *node, int columnID)
{
     try
    {
        //---- Enter your callback code here -----
        WriteCallbackToListingWindow("OnDefaultAction Invoked");

        if (!defaultActionToggle)
        {
            return;
        }

        NXOpen::BlockStyler::PropertyList *defaultActionToggleProps = defaultActionToggle->GetProperties();
        bool defaultActionToggle = defaultActionToggleProps->GetLogical("Value");
        delete defaultActionToggleProps;

        if(defaultActionToggle)
        {
            std::vector<BlockStyler::Node *> selectedNode = tree_control0->GetSelectedNodes();
            selectedNode[0]->SetColumnDisplayText(2,"Default Action");                
            TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeInformation, "Default Action: Third column text is changed");
            selectedNode.clear();
        }
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        TreeListDemo::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}


