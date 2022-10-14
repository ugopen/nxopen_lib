//===============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for Block Styler Tree List.
//===============================================================================
//

//==============================================================================
//  WARNING!!  This file is overwritten by the Block UI Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
//==============================================================================

//==============================================================================
//  Purpose:  This TEMPLATE file contains JAVA source to guide you in the
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
//These imports are needed for the following template code
//------------------------------------------------------------------------------
import java.rmi.RemoteException;

import nxopen.BaseSession;
import nxopen.NXException;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.TaggedObject;
import nxopen.UI;
import nxopen.blockstyler.BlockDialog;
import nxopen.blockstyler.Node;
import nxopen.blockstyler.Tree;
import nxopen.blockstyler.TreeListMenu;
import nxopen.blockstyler.Node.Scroll;
import nxopen.blockstyler.Tree.ColumnDisplay;
import nxopen.blockstyler.Tree.ColumnResizePolicy;
import nxopen.blockstyler.Tree.NodeInsertOption;
import nxopen.blockstyler.Tree.OnSelectCallback;
import nxopen.blockstyler.Tree.OnDefaultActionCallback;

//------------------------------------------------------------------------------
//Represents Block Styler application class
//------------------------------------------------------------------------------
public class TreeListDemo implements BlockDialog.Initialize, BlockDialog.DialogShown, BlockDialog.Apply, BlockDialog.Ok, BlockDialog.Update
,Tree.OnInsertNodeCallback
,Tree.OnDeleteNodeCallback
,Tree.OnSelectCallback
,Tree.OnStateChangeCallback
,Tree.ToolTipTextCallback
,Tree.StateIconNameCallback
,Tree.OnBeginLabelEditCallback
,Tree.OnEndLabelEditCallback
,Tree.OnEditOptionSelectedCallback
,Tree.AskEditControlCallback
,Tree.OnMenuCallback
,Tree.OnMenuSelectionCallback
,Tree.IsDropAllowedCallback
,Tree.IsDragAllowedCallback
,Tree.OnDropCallback
,Tree.OnDefaultActionCallback



{
    //class members
    public static Session theSession = null;
    public static UI theUI = null;
    static TreeListDemo theTreeListDemo;
    private String theDialogName;
    private nxopen.blockstyler.BlockDialog theDialog;
    private nxopen.blockstyler.UIBlock group0;// Block type: Group
    private nxopen.blockstyler.Tree tree_control0;// Block type: Tree Control
    private nxopen.blockstyler.UIBlock addDeleteNodeGroup;// Block type: Group
    private nxopen.blockstyler.UIBlock nodeString;// Block type: String
    private nxopen.blockstyler.UIBlock addNodeButton;// Block type: Button
    private nxopen.blockstyler.UIBlock deleteNodeButton;// Block type: Button
    private nxopen.blockstyler.UIBlock stateIconGroup;// Block type: Group
    private nxopen.blockstyler.UIBlock stateIconOptions;// Block type: Enumeration
    private nxopen.blockstyler.UIBlock nodeToolTip;// Block type: String
    private nxopen.blockstyler.UIBlock NodeEditGroup;// Block type: Group
    private nxopen.blockstyler.UIBlock nodeEditOptions;// Block type: Enumeration
    private nxopen.blockstyler.UIBlock menuGroup;// Block type: Group
    private nxopen.blockstyler.UIBlock showMenuToggle;// Block type: Toggle
    private nxopen.blockstyler.UIBlock dragDropGroup;// Block type: Group
    private nxopen.blockstyler.UIBlock disallowDragToggle;// Block type: Toggle
    private nxopen.blockstyler.UIBlock dropOptions;// Block type: Enumeration
    private nxopen.blockstyler.UIBlock defaultActionGroup;// Block type: Group
    private nxopen.blockstyler.UIBlock defaultActionToggle;// Block type: Toggle
    private nxopen.blockstyler.UIBlock nodeDataGroup;// Block type: Group
    private nxopen.blockstyler.UIBlock instructions;// Block type: Multiline String
    private nxopen.blockstyler.UIBlock selection0;// Block type: Selection
    private nxopen.blockstyler.UIBlock addCrossSelectionNodeButton;// Block type: Button
    private nxopen.blockstyler.UIBlock redrawGroup;// Block type: Group
    private nxopen.blockstyler.UIBlock redrawInstruction;// Block type: Multiline String
    private nxopen.blockstyler.UIBlock redrawToggle;// Block type: Toggle
    private nxopen.blockstyler.UIBlock listingWindowGroup;// Block type: Group
    private nxopen.blockstyler.UIBlock listingWindowToggle;// Block type: Toggle


    //Integers used for columns
    private final int              ColumnFirst=0;
    private final int              ColumnSecond=1;
    private final int              ColumnThird=2;

    //Integers used for menu
    private final int              AddNode =0;
    private final int              DeleteNode=1;
    private final int              CheckedMenuItem=2;
    private final int              DefaultMenuItem=3;
    private final int              DialogLaunchMenuItem=4;    
    private final int              DisableMenuItem=5;
    private final int              HiddenMenuItem=6;
    private final int              IconMenuItem=7;
    private final int              SubMenu1=8;
    private final int              SubMenu2=9;
    private final int              SubMenuItem1=10;
    private final int              SubMenuItem2=11;
    private final int              SubMenuItem3=12;
    private final int              SubMenuItem4=13;
    private final int              TreeMenuItem=14;    


    //------------------------------------------------------------------------------
    //Constructor for NX Styler class
    //------------------------------------------------------------------------------
    public TreeListDemo() throws Exception, RemoteException
    {
        try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUI = (UI)SessionFactory.get("UI");
            theDialogName = "TreeListDemo.dlx";
            theDialog = theUI.createDialog(theDialogName);
            theDialog.addApplyHandler(this);
            theDialog.addOkHandler(this);
            theDialog.addUpdateHandler(this);
            theDialog.addInitializeHandler(this);            
            theDialog.addDialogShownHandler(this);
        }
        catch(Exception ex)
        {

            throw new Exception(ex);
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
    //            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\\ugii\menus\custom_dirs.dat
    //
    //    You can create the dialog using one of the following way:
    //
    //    1. USER EXIT
    //
    //        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
    //        2) Invoke the Shared Library through File->Execute->NX Open menu.
    //
    //------------------------------------------------------------------------------
    public static void main(String [] argv) throws Exception
    {
        try
        {
            theTreeListDemo = new TreeListDemo();
            // The following method shows the dialog immediately
            theTreeListDemo.show();
        }
        catch(Exception ex)
        {

            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        finally
        {
            theTreeListDemo.dispose();
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
    public static final int getUnloadOption()
    {

        return BaseSession.LibraryUnloadOption.EXPLICITLY;

    }

    //------------------------------------------------------------------------------
    // Following method cleanup any housekeeping chores that may be needed.
    // This method is automatically called by NX.
    //------------------------------------------------------------------------------
    public static void unloadLibrary() throws NXException, RemoteException
    {
        try
        {
        }
        catch(Exception ex)
        {

            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }

    //------------------------------------------------------------------------------
    //This method shows the dialog on the screen
    //------------------------------------------------------------------------------
    public int show() throws NXException, RemoteException
    {
        try
        {
            theDialog.show();
        }
        catch(Exception ex)
        {

            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return 0;
    }

    //------------------------------------------------------------------------------
    //Method Name: dispose
    //------------------------------------------------------------------------------
    public void dispose() throws NXException, RemoteException
    {
        if(theDialog != null)
        {
            theDialog.dispose();
            theDialog = null;
        }
    }

    //------------------------------------------------------------------------------
    //---------------------Block UI Styler Callback Functions--------------------------
    //------------------------------------------------------------------------------

    String nodeBaseString ;   
    int nodeSuffixNumber = 0;


    //------------------------------------------------------------------------------
    //Callback Name: initialize
    //------------------------------------------------------------------------------
    public void initialize() throws NXException, RemoteException
    {
        try
        {
            group0 = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("group0");
            tree_control0 = (nxopen.blockstyler.Tree)theDialog.topBlock().findBlock("tree_control0");
            addDeleteNodeGroup = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("addDeleteNodeGroup");
            nodeString = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("nodeString");
            addNodeButton = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("addNodeButton");
            deleteNodeButton = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("deleteNodeButton");
            stateIconGroup = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("stateIconGroup");
            stateIconOptions = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("stateIconOptions");
            nodeToolTip = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("nodeToolTip");
            NodeEditGroup = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("NodeEditGroup");
            nodeEditOptions = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("nodeEditOptions");
            menuGroup = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("menuGroup");
            showMenuToggle = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("showMenuToggle");
            dragDropGroup = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("dragDropGroup");
            disallowDragToggle = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("disallowDragToggle");
            dropOptions = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("dropOptions");
            defaultActionGroup = theDialog.topBlock().findBlock("defaultActionGroup");
            defaultActionToggle = theDialog.topBlock().findBlock("defaultActionToggle");
            nodeDataGroup = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("nodeDataGroup");
            instructions = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("instructions");
            selection0 = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("selection0");
            addCrossSelectionNodeButton = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("addCrossSelectionNodeButton");
            redrawGroup = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("redrawGroup");
            redrawInstruction = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("redrawInstruction");
            redrawToggle = (nxopen.blockstyler.UIBlock)theDialog.topBlock().findBlock("redrawToggle");
            listingWindowGroup = theDialog.topBlock().findBlock("listingWindowGroup");
            listingWindowToggle = theDialog.topBlock().findBlock("listingWindowToggle");

            //------------------------------------------------------------------------------
            //Registration of Treelist specific callbacks
            //------------------------------------------------------------------------------

            tree_control0.setOnInsertNodeHandler(this);

            tree_control0.setOnDeleteNodeHandler(this);   
            
            tree_control0.setOnSelectHandler(this);

            tree_control0.setOnStateChangeHandler(this);

            tree_control0.setToolTipTextHandler(this);   

            tree_control0.setStateIconNameHandler(this);

            tree_control0.setOnBeginLabelEditHandler(this);

            tree_control0.setOnEndLabelEditHandler(this);

            tree_control0.setOnEditOptionSelectedHandler(this);

            tree_control0.setAskEditControlHandler(this);

            tree_control0.setOnMenuHandler(this);

            tree_control0.setOnMenuSelectionHandler(this);

            tree_control0.setIsDropAllowedHandler(this);

            tree_control0.setIsDragAllowedHandler(this);

            tree_control0.setOnDropHandler(this);
            
            tree_control0.setOnDefaultActionHandler(this);



            //------------------------------------------------------------------------------           

            nxopen.blockstyler.PropertyList stringPropList = nodeString.getProperties();
            nodeBaseString = stringPropList.getString("Value");
            stringPropList.setString("Value",nodeBaseString + nodeSuffixNumber);
            stringPropList.dispose(); 


        }
        catch(Exception ex)
        {

            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }



    nxopen.blockstyler.Node previousAddedNode ;
    int randomIcon = 0;
    String randomIconString[] = {"extrude", "cone", "block", "blend"};
    private TaggedObject[] blank;




    //------------------------------------------------------------------------------
    //Callback Name: dialogShown
    //This callback is executed just before the dialog launch. Thus any value set 
    //here will take precedence and dialog will be launched showing that value. 
    //------------------------------------------------------------------------------
    public void dialogShown() throws NXException, RemoteException
    {
        try
        {

            //Insert Columns        
            tree_control0.insertColumn(ColumnFirst,"First Column", 80);    
            tree_control0.insertColumn(ColumnSecond,"Second Column", 80);
            tree_control0.insertColumn(ColumnThird,"Third Column", 80);


            //Set resize policy for columns
            tree_control0.setColumnResizePolicy(ColumnFirst,ColumnResizePolicy.CONSTANT_WIDTH);
            tree_control0.setColumnResizePolicy(ColumnSecond,ColumnResizePolicy.CONSTANT_WIDTH);
            tree_control0.setColumnResizePolicy(ColumnThird,ColumnResizePolicy.CONSTANT_WIDTH);

            //Let the second column interpret the text as icon
            tree_control0.setColumnDisplayType(ColumnSecond,ColumnDisplay.ICON);



        }
        catch(Exception ex)
        {

            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }

    //------------------------------------------------------------------------------
    //Callback Name: apply
    //Following callback is associated with the "theDialog" Block.
    //------------------------------------------------------------------------------
    public int apply() throws NXException, RemoteException
    {
        int errorCode = 0;
        try
        {


        }
        catch(Exception ex)
        {

            errorCode = 1;
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return errorCode;
    }



    private nxopen.blockstyler.Node CreateAndAddNode(nxopen.blockstyler.Node afterNode)throws NXException, RemoteException
    {


        nxopen.blockstyler.Node node = null;

        try
        {

            nxopen.blockstyler.Node parentNode = null;    

            //Get node display string from the block
            nxopen.blockstyler.PropertyList stringPropList = nodeString.getProperties();
            String nodeDisplayString  = stringPropList.getString("Value");
            stringPropList.dispose();            
            node = tree_control0.createNode(nodeDisplayString); 

            //Set few properties of node
            node.setForegroundColor(198);
            node.setDisplayIcon(randomIconString[randomIcon]);
            node.setSelectedIcon("draft");

            //Take first selected node as parent node
            nxopen.blockstyler.Node selectedNodes[] = tree_control0.getSelectedNodes();

            if(selectedNodes.length>0)
            {
                parentNode = selectedNodes[0];
            }    

            //Insert Node
            tree_control0.insertNode(node, parentNode, afterNode, NodeInsertOption.SORT);
            node.scrollTo(ColumnFirst, Scroll.CENTER);

            //Change the last node color. Making sure that new node color is distinct
            if (previousAddedNode != null)
            {
                previousAddedNode.setForegroundColor(211);        

            }
            previousAddedNode = node;        

        }              
        catch(Exception ex)
        {


            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }

        return node;               

    }

    private void DeleteSelectedNodes()throws NXException, RemoteException
    {    

        try
        {

            nxopen.blockstyler.Node selectedNodes[] = tree_control0.getSelectedNodes();
            if(selectedNodes.length>0)
            {
                while(selectedNodes.length>0)
                {
                    tree_control0.deleteNode(selectedNodes[0]);
                    selectedNodes = tree_control0.getSelectedNodes();                      
                }
            }
            else
            {
                theUI.nxmessageBox().show("Delete Node", nxopen.NXMessageBox.DialogType.INFORMATION, "No Nodes are selected");
            }
        }
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }
    
    //Writes callback name to ListingWindow
    private void WriteCallbackToListingWindow(String callbackName )throws NXException, RemoteException
    {    
        if(listingWindowToggle == null )
            return ;
        try
        {
            nxopen.blockstyler.PropertyList listingWindowToggleProps = listingWindowToggle.getProperties();
            boolean listingWindow = listingWindowToggleProps.getLogical("Value");
            listingWindowToggleProps.dispose();
            
            if(listingWindow)
            {
                theSession.listingWindow().open();
                String nullString = null;
                theSession.listingWindow().writeLine(callbackName);                
            }
        }
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }


    //------------------------------------------------------------------------------
    //Callback Name: update
    //Following callback is associated with the "theDialog" Block.
    //------------------------------------------------------------------------------
    public int update( nxopen.blockstyler.UIBlock block) throws NXException, RemoteException
    {
        try
        {
            if(block == nodeString)
            {

            }
            else if(block == addNodeButton)
            {

                nxopen.blockstyler.Node afterNode = null;
                nxopen.blockstyler.Node node = CreateAndAddNode(afterNode); 

                //State Icon
                nxopen.blockstyler.PropertyList prop = stateIconOptions.getProperties();
                int enumValue = prop.getEnum("Value");
                prop.dispose();
                if(enumValue==0)
                {
                    //Ignore

                }
                else if(enumValue==1)
                {
                    node.setState(1);

                }
                else if(enumValue==2)
                {
                    node.setState(3);  //Set value other than 1 or 2                  
                }                

            }
            else if(block == deleteNodeButton)
            {

                DeleteSelectedNodes();
            }
            else if(block == stateIconOptions)
            {

            }
            else if(block == nodeToolTip)
            {

            }
            else if(block == nodeEditOptions)
            {
                if (defaultActionToggle == null)
                {
                    return 0 ;
                }
                nxopen.blockstyler.PropertyList nodeEditOptionsProps = nodeEditOptions.getProperties();
                String nodeEditOption = nodeEditOptionsProps.getEnumAsString("Value");
                nodeEditOptionsProps.dispose();
                
                
                
                nxopen.blockstyler.PropertyList defaultActionToggleProps = defaultActionToggle.getProperties();
                if((nodeEditOption.equals("Combo Box Edit")) || (nodeEditOption.equals("Listbox Edit")))
                {                    
                    defaultActionToggleProps.setLogical("Enable",false);
                    defaultActionToggleProps.setLogical("Value",false);                    
                }
                else
                {
                    defaultActionToggleProps.setLogical("Enable",true);
                }            
                
                defaultActionToggleProps.dispose();
            }
            else if(block == showMenuToggle)
            {

            }
            else if(block == disallowDragToggle)
            {

            }
            else if(block == dropOptions)
            {

            }
            else if(block == instructions)
            {

            }
            else if(block == selection0)
            {

            }
            else if(block == addCrossSelectionNodeButton)
            {

                nxopen.blockstyler.PropertyList prop = selection0.getProperties();
                nxopen.TaggedObject[] objects =prop.getTaggedObjectVector("SelectedObjects");
                if(objects.length>0)
                {
                    //Create node and node data 
                    nxopen.blockstyler.Node node=tree_control0.createNode("CrossSelection-NodeData");
                    nxopen.DataContainer nodeData = node.getNodeData();
                    nodeData.addTaggedObject("Data", objects[0]);

                    nodeData.dispose();
                    tree_control0.insertNode(node,null, null, NodeInsertOption.ALWAYS_LAST);

                    //Reset Selection block                       
                    nxopen.TaggedObject blank[] = {};
                    prop.setTaggedObjectVector("SelectedObjects",blank);

                }              
                prop.dispose();                

            }
            else if(block == redrawInstruction)
            {

            }
            else if(block == redrawToggle)
            {

                nxopen.blockstyler.PropertyList prop = redrawToggle.getProperties();
                boolean isRedraw = prop.getLogical("Value");
                prop.dispose();
                tree_control0.redraw(isRedraw);                  

            }
        }
        catch(Exception ex)
        {

            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return 0;
    }

    //------------------------------------------------------------------------------
    //Callback Name: ok
    //------------------------------------------------------------------------------
    public int ok() throws NXException, RemoteException
    {
        int errorCode = 0;
        try
        {

            errorCode = apply();
        }
        catch(Exception ex)
        {

            errorCode = 1;
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return errorCode;
    }    

    //------------------------------------------------------------------------------
    //Treelist specific callbacks
    //------------------------------------------------------------------------------

    public void onInsertNodeCallback(Tree tree, Node node) throws NXException,RemoteException
    {
        try
        {
            WriteCallbackToListingWindow("OnInsertNodeCallback Invoked");


            //Setting random icon
            if (randomIcon==0)
            {
                node.setColumnDisplayText(ColumnSecond, randomIconString[randomIcon]);
            }
            else if(randomIcon==1)
            {
                node.setColumnDisplayText(ColumnSecond, randomIconString[randomIcon]);
            }
            else if(randomIcon==2)
            {
                node.setColumnDisplayText(ColumnSecond, randomIconString[randomIcon]);
            }
            else if(randomIcon==3)
            {
                node.setColumnDisplayText(ColumnSecond, randomIconString[randomIcon]);
            }
            randomIcon = randomIcon + 1;
            if (randomIcon > 3)
            {
                randomIcon = 0;
            }

            String columnText = "Column Text - " + randomIcon;
            node.setColumnDisplayText(ColumnThird, columnText);
            if (nodeSuffixNumber == 15000)
            {
                nodeSuffixNumber = 0;
            }
            else
            {
                nodeSuffixNumber = nodeSuffixNumber + 1;
            }

            //New Node text for the next node               
            nxopen.blockstyler.PropertyList prop = nodeString.getProperties();
            String nodeDisplayString = nodeBaseString;
            nodeDisplayString = nodeBaseString + nodeSuffixNumber;
            prop.setString("Value", nodeDisplayString);
            prop.dispose();            
        }
        catch(Exception ex)
        {

            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }

    public void onDeleteNodeCallback(Tree tree, Node node) throws NXException,RemoteException
    {
        try
        {
            WriteCallbackToListingWindow("OnDeleteNodeCallback Invoked");

            if(node==previousAddedNode)
            {
                //Set the previous node to Nothing. Done for safe execution.
                previousAddedNode = null;
            }
        }
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }

    public void onSelectCallback(Tree tree, Node node, int columnID, boolean selected)throws NXException, RemoteException
    {
        try
        {
            String text = null;
            if(selected)
            {
                text = "OnSelectCallback Invoked: Node \"" + node.displayText().toString() + "\" " + "Selected at column " + columnID ;                
            }
            else
            {
                text = "OnSelectCallback Invoked: Node \"" + node.displayText().toString() + "\"Deselected" ;                
            }
            WriteCallbackToListingWindow(text);
        }
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }    


    public void onStateChangeCallback(Tree tree, Node node, int state)throws NXException, RemoteException
    {
        try
        {
            WriteCallbackToListingWindow("OnStateChangeCallback Invoked");

            if (state == 1)
            {
                node.setState(2);
            }
            else if (state == 2)
            {
                node.setState(1);
            }
            else if (state == 3)
            {
                node.setState(4);
            }
            else if (state == 4)
            {
                node.setState(3);
            }    
        }
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }

    public String toolTipTextCallback(Tree tree, Node node, int columnID)throws NXException, RemoteException
    {
        String ToolTipText=null;
        try
        {
            nxopen.blockstyler.PropertyList prop = nodeToolTip.getProperties();
            ToolTipText = prop.getString("Value");
        }
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return ToolTipText;  
    }



    public String stateIconNameCallback(Tree tree, Node node, int state)throws NXException, RemoteException
    {
        String stateIcon=null;

        try
        {
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

        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return stateIcon; 
    }

    public nxopen.blockstyler.Tree.BeginLabelEditState onBeginLabelEditCallback(Tree tree, Node node,int columnID) throws NXException, RemoteException
    {
        nxopen.blockstyler.Tree.BeginLabelEditState OnBeginLabelEdit = Tree.BeginLabelEditState.DISALLOW;

        try
        {
            WriteCallbackToListingWindow("OnBeginLabelEditCallback Invoked");
            nxopen.blockstyler.PropertyList prop = nodeEditOptions.getProperties();
            int labelEditOption = prop.getEnum("Value");
            prop.dispose();

            if (labelEditOption==1)
            {
                OnBeginLabelEdit = Tree.BeginLabelEditState.ALLOW;
            }
            else
            {
                OnBeginLabelEdit = Tree.BeginLabelEditState.DISALLOW;
            }  
        }

        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return OnBeginLabelEdit; 
    }

    public nxopen.blockstyler.Tree.EndLabelEditState onEndLabelEditCallback(Tree tree, Node node,int columnID, String editedText) throws NXException, RemoteException
    {
        nxopen.blockstyler.Tree.EndLabelEditState OnEndLabelEdit = Tree.EndLabelEditState.REJECT_TEXT;
        try
        {
            WriteCallbackToListingWindow("OnEndLabelEditCallback Invoked");
            if (editedText == "Reject")
            {
                OnEndLabelEdit = Tree.EndLabelEditState.REJECT_TEXT;                   

            }
            else
            {
                OnEndLabelEdit = Tree.EndLabelEditState.ACCEPT_TEXT;                   
            } 
        }

        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return OnEndLabelEdit;
    }

    public nxopen.blockstyler.Tree.EditControlOption onEditOptionSelectedCallback(Tree tree, Node node,int columnID, int selectedOptionID, String selectedOptionText, nxopen.blockstyler.Tree.ControlType type)throws NXException, RemoteException
    {
        nxopen.blockstyler.Tree.EditControlOption OnEditOptionSelected = Tree.EditControlOption.REJECT;
        try
        {
            if(type == Tree.ControlType.COMBO_BOX)
            {
                if(selectedOptionText == "ComboBox-RejectText" )
                {
                    OnEditOptionSelected = Tree.EditControlOption.REJECT;                       
                }
                else
                {
                    OnEditOptionSelected = Tree.EditControlOption.ACCEPT;
                }
            }
            else if(type == Tree.ControlType.LIST_BOX)
            {
                if(selectedOptionText == "ListBox-RejectText" )
                {
                    OnEditOptionSelected = Tree.EditControlOption.REJECT;                       
                }
                else
                {
                    OnEditOptionSelected = Tree.EditControlOption.ACCEPT;
                }
            }
        }
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return OnEditOptionSelected;
    }

    public nxopen.blockstyler.Tree.ControlType askEditControlCallback(Tree tree, Node node, int columnID)throws NXException, RemoteException
    {
        nxopen.blockstyler.Tree.ControlType AskEditControl = Tree.ControlType.NONE;

        try
        {
            nxopen.blockstyler.PropertyList prop = nodeEditOptions.getProperties();
            int labelEditOption = prop.getEnum("Value");
            prop.dispose();

            if (labelEditOption==2)
            {
                AskEditControl =Tree.ControlType.COMBO_BOX;
                String options[] = {"ComboBox-AcceptText", "ComboBox-DefaultText", "ComboBox-RejectText"};
                tree.setEditOptions(options, 1);
            }
            else if (labelEditOption==3)
            {
                AskEditControl =Tree.ControlType.LIST_BOX;
                String options[] = {"ListBox-AcceptText", "ListBox-DefaultText", "ListBox-RejectText"};
                tree.setEditOptions(options, 1);
            }  
            else
            {
                AskEditControl = Tree.ControlType.NONE;
            }
        }        
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return AskEditControl; 
    }


    public void onMenuCallback(Tree tree, Node node, int columnID)throws NXException, RemoteException
    {
        try
        {
            WriteCallbackToListingWindow("OnMenuCallback Invoked");
            nxopen.blockstyler.PropertyList prop = showMenuToggle.getProperties();
            boolean  value = prop.getLogical("Value");
            prop.dispose();

            if(value == false )
            {
                return;
            }

            //Create Menu
            TreeListMenu menu = tree.createMenu();
            TreeListMenu SubMenu1Main = tree.createMenu();
            TreeListMenu SubMenu2Main = tree.createMenu();

            if(node == null )
            {
                menu.addMenuItem(AddNode, "Add Node");
                menu.addSeparator();
                menu.addMenuItem(TreeMenuItem,"Tree Menu Item");                
            }
            else //Menu request for node
            {
                menu.addMenuItem(AddNode,"Add Node");
                menu.addMenuItem(DeleteNode,"Delete Node");

                menu.addSeparator();
                menu.addMenuItem(CheckedMenuItem,"Checked Menu Item");
                menu.addMenuItem(DefaultMenuItem,"Default Menu Item");
                menu.addMenuItem(DialogLaunchMenuItem,"Dialog Launch Menu Item");
                menu.addMenuItem(DisableMenuItem,"Disable Menu Item");
                menu.addMenuItem(HiddenMenuItem,"Hidden Menu Item");
                menu.addMenuItem(IconMenuItem,"Icon Menu Item");     

                menu.addSeparator();
                menu.addMenuItem(SubMenu1,"Sub Menu 1");
                menu.addMenuItem(SubMenu2,"Sub Menu 2");

                //Sub Menu
                SubMenu1Main.addMenuItem(SubMenuItem1,"Sub Menu Item 1");
                SubMenu1Main.addMenuItem(SubMenuItem2, "Sub Menu Item 2");

                SubMenu1Main.addMenuItem(SubMenuItem3,"Sub Menu Item 3");
                SubMenu1Main.addMenuItem(SubMenuItem4, "Sub Menu Item 4");

                //Set Sub Menu
                menu.setSubMenu(SubMenu1,SubMenu1Main);
                menu.setSubMenu(SubMenu2,SubMenu2Main);

                //Edit Menu Items
                menu.setItemChecked(CheckedMenuItem,true);
                menu.setItemDefault(DefaultMenuItem,true);
                menu.setItemDialogLaunching(DialogLaunchMenuItem,true);
                menu.setItemDisable(DisableMenuItem,true);
                menu.setItemHidden(HiddenMenuItem,true);
                menu.setItemIcon(IconMenuItem,"sketch");    

            }

            //Set menu on tree
            tree.setMenu(menu);

            //Dispose the menu only after setting the menu on tree
            menu.dispose();
            SubMenu1Main.dispose();
            SubMenu2Main.dispose();   
        }        
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }

    public void onMenuSelectionCallback(Tree tree, Node node, int menuItemID)throws NXException, RemoteException
    {
        try
        {
            WriteCallbackToListingWindow("OnMenuSelectionCallback Invoked");
            if(node == null)
            {
                if(menuItemID == AddNode)
                {
                    CreateAndAddNode(null);
                }

            }
            else
            {
                if(menuItemID == AddNode)
                {
                    CreateAndAddNode(null);
                }
                else if(menuItemID == DeleteNode)
                {
                    nxopen.blockstyler.Node selectedNodes[] = tree_control0.getSelectedNodes();
                    if(selectedNodes.length>0)
                    {
                        DeleteSelectedNodes();
                    }
                    else
                    {
                        if(node != null)
                        {
                            tree.deleteNode(node);
                        }
                    }
                }
            }
        }        
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }

    public nxopen.blockstyler.Node.DropType isDropAllowedCallback(Tree tree, Node node, int columnID,Node targetNode, int targetColumnID) throws NXException, RemoteException
    {
        nxopen.blockstyler.Node.DropType IsDropAllowed = Node.DropType.NONE;
        try
        {
            nxopen.blockstyler.PropertyList prop = dropOptions.getProperties();
            int dropOption = prop.getEnum("Value");
            prop.dispose();

            // This will just show iconic representation that drop is allowed. No default action is performed after drop.
            // OnDropCallback should be implemented for specific drop behaviour

            if (dropOption == 0)
            {
                IsDropAllowed = Node.DropType.NONE;
            }
            else if (dropOption == 1)
            {
                IsDropAllowed = Node.DropType.AFTER;
            }
            else if (dropOption == 2)
            {
                IsDropAllowed = Node.DropType.BEFORE;
            }
            else if (dropOption == 3)
            {
                IsDropAllowed = Node.DropType.BEFORE_AND_AFTER;
            }
            else if (dropOption == 4)
            {
                IsDropAllowed = Node.DropType.ON;
            }
        }        
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return IsDropAllowed;
    }

    public nxopen.blockstyler.Node.DragType isDragAllowedCallback(Tree tree, Node node, int columnID)throws NXException, RemoteException
    {
        nxopen.blockstyler.Node.DragType IsDragAllowed = Node.DragType.NONE;
        try
        {

            nxopen.blockstyler.PropertyList prop = disallowDragToggle.getProperties();
            boolean isDragDisallowed = prop.getLogical("Value");
            prop.dispose();

            // This will just show iconic representation that drop is allowed. No default action is performed after drop.
            // OnDropCallback should be implemented for specific drop behaviour

            if (isDragDisallowed == true)
            {
                IsDragAllowed = Node.DragType.NONE;
            }
            else
            {
                IsDragAllowed = Node.DragType.ALL;
            }                       
        }        
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return IsDragAllowed;
    }

    public boolean onDropCallback(Tree tree, Node[] node, int columnID, Node targetNode,int targetColumnID, nxopen.blockstyler.Node.DropType dropType, int dropMenuItemId) throws NXException,RemoteException
    {
        try
        {
            WriteCallbackToListingWindow("OnDropCallback Invoked");
        }        
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return true;
    }

    public void onDefaultActionCallback(Tree tree, Node node, int columnID) throws NXException,RemoteException
    {
        try
        {
            WriteCallbackToListingWindow("OnDefaultAction Invoked");
            
            if (defaultActionToggle == null)
                return;
            
            nxopen.blockstyler.PropertyList defaultActionToggleProps = defaultActionToggle.getProperties();
            boolean defaultActionToggle = defaultActionToggleProps.getLogical("Value");
            defaultActionToggleProps.dispose();
            
            if(defaultActionToggle)
            {
                nxopen.blockstyler.Node selectedNode[] = tree_control0.getSelectedNodes();
                selectedNode[0].setColumnDisplayText(2, "Default Action");
                theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, "Default Action: Third column text is changed");
                selectedNode = null;
            }            
        }        
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }    
}


