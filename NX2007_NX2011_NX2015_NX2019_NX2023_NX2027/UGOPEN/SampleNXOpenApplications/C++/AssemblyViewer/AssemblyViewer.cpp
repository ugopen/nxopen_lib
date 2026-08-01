//=============================================================================
//
//         Copyright 2010 Siemens Product Lifecycle Management Software Inc.
//                           All Rights Reserved.
//===============================================================================
//File description: Sample NXOpen Application for displaying a tree structure 
//of an assembly in the tree list of a Block Styler UI dialog.
//===============================================================================
//
//==============================================================================
//  WARNING!!  This file is overwritten by the Block UI Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
//==============================================================================

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
#include "AssemblyViewer.hpp"

using namespace NXOpen;
using namespace NXOpen::BlockStyler;
using namespace NXOpen::Assemblies;

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(AssemblyViewer::theSession) = NULL;
UI *(AssemblyViewer::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
AssemblyViewer *theAssemblyViewer;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
AssemblyViewer::AssemblyViewer()
{
    try
    {
        // Initialize the NX Open C++ API environment
        AssemblyViewer::theSession = NXOpen::Session::GetSession();
        AssemblyViewer::theUI = UI::GetUI();
        theDlxFileName = "AssemblyViewer.dlx";
        theDialog = AssemblyViewer::theUI->CreateDialog(theDlxFileName);
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &AssemblyViewer::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &AssemblyViewer::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &AssemblyViewer::update_cb));
        theDialog->AddFilterHandler(make_callback(this, &AssemblyViewer::filter_cb));
        theDialog->AddInitializeHandler(make_callback(this, &AssemblyViewer::initialize_cb));
        theDialog->AddFocusNotifyHandler(make_callback(this, &AssemblyViewer::focusNotify_cb));
        theDialog->AddKeyboardFocusNotifyHandler(make_callback(this, &AssemblyViewer::keyboardFocusNotify_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &AssemblyViewer::dialogShown_cb));
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
AssemblyViewer::~AssemblyViewer()
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
        theAssemblyViewer = new AssemblyViewer();
        // The following method shows the dialog immediately
        theAssemblyViewer->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if(theAssemblyViewer != NULL)
    {
        delete theAssemblyViewer;
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
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int AssemblyViewer::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void AssemblyViewer::initialize_cb()
{
    try
    {
        group0 = dynamic_cast<NXOpen::BlockStyler::UIBlock*>(theDialog->TopBlock()->FindBlock("group0"));
        treeList = dynamic_cast<NXOpen::BlockStyler::Tree*>(theDialog->TopBlock()->FindBlock("treeList"));
        group = dynamic_cast<NXOpen::BlockStyler::UIBlock*>(theDialog->TopBlock()->FindBlock("group"));
        compDisplay = dynamic_cast<NXOpen::BlockStyler::UIBlock*>(theDialog->TopBlock()->FindBlock("compDisplay"));
        group1 = dynamic_cast<NXOpen::BlockStyler::UIBlock*>(theDialog->TopBlock()->FindBlock("group1"));
        selComponent = dynamic_cast<NXOpen::BlockStyler::UIBlock*>(theDialog->TopBlock()->FindBlock("selComponent"));
        selColor = dynamic_cast<NXOpen::BlockStyler::UIBlock*>(theDialog->TopBlock()->FindBlock("selColor"));
        setColor = dynamic_cast<NXOpen::BlockStyler::UIBlock*>(theDialog->TopBlock()->FindBlock("setColor"));
        //------------------------------------------------------------------------------
        //Registration of Treelist specific callbacks
        //------------------------------------------------------------------------------                
        treeList->SetOnSelectHandler(make_callback(this, &AssemblyViewer::OnSelectCallback));         
        //------------------------------------------------------------------------------

        drawAll = false;
        NXOpen::BlockStyler::PropertyList *setColorProps = setColor->GetProperties();
        setColorProps->SetLogical("Enable",true);
        delete setColorProps;
        setColorProps = NULL;
        
        //Setting selection mask to select only components
        NXOpen::Selection::SelectionAction action = Selection::SelectionActionClearAndEnableSpecific;
        std::vector<NXOpen::Selection::MaskTriple>selectionMask_array(2);
        selectionMask_array[0].Type = UF_component_type ;
        selectionMask_array[0].Subtype = UF_component_subtype  ;
        selectionMask_array[1].Type = UF_component_type;
        selectionMask_array[1].Subtype = UF_part_occurrence_subtype;
        
        NXOpen::BlockStyler::PropertyList *selComponentProps = selComponent->GetProperties();
        selComponentProps->SetSelectionFilter("SelectionFilter",action,selectionMask_array);
        delete selComponentProps;
        selComponentProps = NULL;
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//Cycles through assembly components and populates the tree list
void AssemblyViewer::PopulateTree(NXOpen::Assemblies::Component *component)
{
    std::vector<Component *> childComponent = component->GetChildren();    
    int childComponentCount = childComponent.size();
    for(int i=0; i<childComponentCount; ++i)
    {
        BlockStyler::Node *node = treeList->CreateNode(childComponent[i]->Name());
        NXOpen::DataContainer *nodeData = node->GetNodeData();
        nodeData->AddTaggedObject("Data",childComponent[i]);
        treeNodes.push_back(node);
        delete nodeData;
        nodeData = NULL;

        node->SetForegroundColor(198);
        treeList->InsertNode(node,parentNode,NULL,treeList->NodeInsertOptionLast);
        parentNode = node;
        PopulateTree(childComponent[i]);
        parentNode = node->ParentNode();    
    }
}

//Performs part clean up and turns off the highlighting
void AssemblyViewer::PartCleanup()
{
    try
    {
        NXOpen::PartCleanup *partCleanup1;        
        partCleanup1 = theSession->NewPartCleanup();
        partCleanup1->SetTurnOffHighlighting(true);
        partCleanup1->DoCleanup();
        delete partCleanup1;
        partCleanup1 = NULL;
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//Highlights the selected components
void AssemblyViewer::HighlightComponent(std::vector<NXOpen::TaggedObject *>&selObjectData, bool highlight)
{
    try
    {
        //---- Enter your callback code here ----- 
        int selObjectCount = selObjectData.size();

        for(int i=0; i<selObjectCount; ++i)
        {
            NXOpen::Assemblies::Component *component = dynamic_cast<NXOpen::Assemblies::Component *> (selObjectData[i]);

            if(!component)
                continue;

            highlight?component->Highlight():component->Unhighlight();
            
            if(drawAll)
            {
                ComponentAssembly *owner =component->DirectOwner();//Gets the parent assembly of the component
                Component *mapped = owner->MapComponentFromParent(component);//Gets other occurence of this component
                ComponentAssembly *topOwner = theSession->Parts()->Display()->ComponentAssembly();//Gets the root part of the component

                std::vector<Component *>mappedBack = topOwner->MapComponentsFromSubassembly(mapped);//Returns the component occurences

                int mappedBackCount = mappedBack.size();
                for(int i=0; i<mappedBackCount; ++i)
                {
                    highlight?mappedBack[i]->Highlight():mappedBack[i]->Unhighlight();
                }
            }
        }                
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }    
}

//Sets the selected color to the components
void AssemblyViewer::ApplyColor(std::vector<NXOpen::TaggedObject *>&selObjectData)
{
    try
    {
        //---- Enter your callback code here -----
        NXOpen::BlockStyler::PropertyList *selColorProps =selColor->GetProperties();
        std::vector<int > colorValue = selColorProps->GetIntegerVector("Value");            
        delete selColorProps;
        selColorProps = NULL;      

        DisplayModification *displayModification1 = theSession->DisplayManager()->NewDisplayModification();       
        displayModification1->SetApplyToAllFaces(false);
        displayModification1->SetApplyToOwningParts(false);
        displayModification1->SetNewColor(colorValue[0]);
        
        std::vector<DisplayableObject *> objects1;
        int selObjectCount = selObjectData.size();
        for(int i=0; i<selObjectCount; ++i)
        {
            objects1.push_back(dynamic_cast<NXOpen::DisplayableObject *>(selObjectData[i]));
        }
        displayModification1->Apply(objects1);
        objects1.clear();
        delete displayModification1;
        displayModification1 = NULL;

        PartCleanup();        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//Gets the component occurrences
std::vector<NXOpen::TaggedObject *>AssemblyViewer::GetComponentOccurences(std::vector<NXOpen::Assemblies::Component *>&assemblyComponent)
{
    std::vector<NXOpen::TaggedObject *>componentOccurences ;
    try
    {
        int assemblyComponentCount = assemblyComponent.size();

        for(int i=0; i<assemblyComponentCount; ++i)
        {
            ComponentAssembly *owner = assemblyComponent[i]->DirectOwner(); //Gets the parent assembly of the component
            Component *mapped = owner->MapComponentFromParent(assemblyComponent[i]); //Gets other occurence of this component
            ComponentAssembly *topOwner = theSession->Parts()->Display()->ComponentAssembly();//Gets the root part of the component

            std::vector<Component *>mappedBack = topOwner->MapComponentsFromSubassembly(mapped);
            for (std::vector<Component *>::iterator it = mappedBack.begin(); it != mappedBack.end(); ++it)                        
            {
                componentOccurences.push_back(*it);
            }
        }
    }
    catch(exception& ex)
    {
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return componentOccurences;
}

//Gets the tags of the selected objects from the select object block
std::vector<NXOpen::TaggedObject *>AssemblyViewer::GetSelectedObjects()
{
    std::vector<NXOpen::TaggedObject *>selCompTags ;
    try
    {
        NXOpen::BlockStyler::PropertyList *selCompProps =selComponent->GetProperties();
        selCompTags = selCompProps->GetTaggedObjectVector("SelectedObjects");
        delete selCompProps;
        selCompProps = NULL;      
    }
    catch(exception& ex)
    {
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return selCompTags;
}

//Gets the tags of the selected nodes from the tree list
std::vector<NXOpen::TaggedObject *>AssemblyViewer::GetSelectedNodes()
{
    std::vector<NXOpen::TaggedObject *>selNodeTags ;
    try
    {
        std::vector<NXOpen::BlockStyler::Node *>selectedNodes =  treeList->GetSelectedNodes();
        int selectedNodesCount = selectedNodes.size();
        for(int i=0; i<selectedNodesCount; ++i)
        {
            NXOpen::DataContainer *nodeData = selectedNodes[i]->GetNodeData();
            selNodeTags.push_back(nodeData->GetTaggedObject("Data"));
        }
    }
    catch(exception& ex)
    {
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return selNodeTags;
}

//Specifies whether the component selection option is "Single component" or "All Components"
bool AssemblyViewer::IsSingleComponentSelection()
{
    bool singleComponent = false;
    try
    {
        NXOpen::BlockStyler::PropertyList *compDisplayProps = compDisplay->GetProperties();
        NXString componentDisplayType = compDisplayProps->GetEnumAsString("Value");
        delete compDisplayProps;
        compDisplayProps = NULL;

        if(!strcmp(componentDisplayType.GetText(),"Single Component"))        
            singleComponent = true;               
    }
    catch(exception& ex)
    {
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return singleComponent;
}

//Based on the IsSingleComponentSelection, selection is done for either single component or for all components
void AssemblyViewer::ComponentSelection()
{
    try
    {
        bool singleComponent = IsSingleComponentSelection();       
        std::vector<NXOpen::TaggedObject *>selObjectData = GetSelectedObjects();
        std::vector<NXOpen::TaggedObject *>selNodeComps = GetSelectedNodes();    

        // Create a DisplayModification object to set the color
        if (selObjectData.size()>0)
        {
            HighlightComponent(selObjectData,false);
            drawAll = singleComponent?false:true;
            HighlightComponent(selObjectData, true);
        }
        if (selNodeComps.size()>0)
        {                
            HighlightComponent(selNodeComps,false);
            drawAll = singleComponent?false:true;
            HighlightComponent(selNodeComps, true);
        }        
    }
    catch(exception& ex)
    {
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}



//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void AssemblyViewer::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
        treeList->InsertColumn(0, "Component Names", 240);
        treeList->SetColumnResizePolicy(0, Tree::ColumnResizePolicyConstantWidth);

        BasePart *basePart(theSession->Parts()->BaseWork());

        //Creating nodes in the treelist and associating the components with the node data.
        if(basePart!=NULL)
        {
            NXOpen::Assemblies::Component *rootComponent = basePart->ComponentAssembly()->RootComponent();

            if(rootComponent != NULL)
            {    
                parentNode = treeList->CreateNode("ROOT");
                NXOpen::DataContainer *nodeData = parentNode->GetNodeData();
                nodeData->AddTaggedObject("Data",rootComponent);        

                delete nodeData;
                nodeData = NULL;

                parentNode->SetForegroundColor(198);
                treeList->InsertNode(parentNode,NULL,NULL,treeList->NodeInsertOptionAlwaysFirst);            
                parentNode->Expand(Node::ExpandOptionExpand);
                PopulateTree(rootComponent);
            }
            else
            {
                AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeInformation, "Opened part is not an assembly. Tree-list will be empty");
                return;
            }
        }        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int AssemblyViewer::apply_cb()
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
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int AssemblyViewer::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {
        if(block == compDisplay)
        {
            //---------Enter your code here-----------
            ComponentSelection();            
        }
        else if(block == selComponent)
        {
            //---------Enter your code here-----------
            PartCleanup();
            ComponentSelection();            
        }
        else if(block == selColor)
        {
            //---------Enter your code here-----------
        }
        else if(block == setColor)
        {
            //---------Enter your code here-----------
            bool singleComponent = IsSingleComponentSelection();

            NXOpen::BlockStyler::PropertyList *selCompProps = selComponent->GetProperties();          
            std::vector<NXOpen::TaggedObject*>emptyArray ;

            std::vector<NXOpen::TaggedObject *>selObjectData = GetSelectedObjects();
            std::vector<NXOpen::TaggedObject *>selNodeComps = GetSelectedNodes();


            if( (!selNodeComps.size()) && (!selObjectData.size()) )
            {
                AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeInformation, "No Components Selected");
            }
            else
            {
                // Create a DisplayModification object to set the color
                std::vector<NXOpen::Assemblies::Component *>selectedComps;
                std::vector<NXOpen::Assemblies::Component *>selectedNodeComps;                
                std::vector<NXOpen::TaggedObject *>selectedNodeCompsTags;

                int selObjectCount = selObjectData.size();
                int selNodeCompsCount = selNodeComps.size();

                for(int i=0; i<selObjectCount; ++i)
                {
                    selectedComps.push_back(dynamic_cast<Component *>(selObjectData[i]));
                }
                if(singleComponent)
                {
                    if (selObjectCount)
                    {
                        ApplyColor(selObjectData);
                        selCompProps->SetTaggedObjectVector("SelectedObjects",emptyArray);
                    }
                    if(selNodeCompsCount)
                    {
                        ApplyColor(selNodeComps);
                        selNodeComps.clear();
                    }
                }
                else //if All Components
                { 
                    selObjectData = GetComponentOccurences(selectedComps);

                    if(selObjectCount)
                    {
                        ApplyColor(selObjectData);                    
                        selCompProps->SetTaggedObjectVector("SelectedObjects",emptyArray);  
                    }
                    for(int i=0; i<selNodeCompsCount; ++i)
                    {                    
                        selectedNodeComps.push_back(dynamic_cast<Component *>(selNodeComps[i]));                                        
                    }

                    selectedNodeCompsTags = GetComponentOccurences(selectedNodeComps);

                    if(selectedNodeCompsTags.size()>0)
                    {
                        ApplyColor(selectedNodeCompsTags);                    
                        selectedNodeCompsTags.clear();
                    }
                }
            }
            delete selCompProps;
            selCompProps = NULL;            
        }        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int AssemblyViewer::ok_cb()
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
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: filter_cb
//------------------------------------------------------------------------------
int AssemblyViewer::filter_cb(NXOpen::BlockStyler::UIBlock* block, NXOpen::TaggedObject* selectObject)
{
    return(UF_UI_SEL_ACCEPT);
}

//------------------------------------------------------------------------------
//Callback Name: focusNotify_cb
//This callback is executed when any block (except the ones which receive keyboard entry such as Integer block) receives focus.
//------------------------------------------------------------------------------
void AssemblyViewer::focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: keyboardFocusNotify_cb
//This callback is executed when block which can receive keyboard entry, receives the focus.
//------------------------------------------------------------------------------
void AssemblyViewer::keyboardFocusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
//------------------------------------------------------------------------------
//Treelist specific callbacks
//------------------------------------------------------------------------------
void AssemblyViewer::OnSelectCallback(NXOpen::BlockStyler::Tree *tree, NXOpen::BlockStyler::Node *, int columnID, bool selected)
{
    try
    {
        //---- Enter your callback code here -----
        if(selected == true)
        {
            PartCleanup();
            ComponentSelection();
        }        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        AssemblyViewer::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
