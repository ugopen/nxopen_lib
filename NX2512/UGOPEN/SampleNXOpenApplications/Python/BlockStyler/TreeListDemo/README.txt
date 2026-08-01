-------------------------------------------------------------------------------


          Copyright 2014 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.


-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
		        Block Styler Tree list demonstration example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates some of the functionalities offered by the Tree List as mentioned below: 

a.	Adding and deleting nodes
b.	Setting column properties
c.	Setting state icons
d.	Setting tooltip
e.	Editing nodes
f.	Menu creation
g.	Drag and drop nodes
h.	Node data usage
i.	Cross selection (associating an object or a feature to a node in the Tree List)

--------------
Files required
--------------

    1. TreeListDemo.py
    2. TreeListDemo.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/TreeListDemo)
    3. Any Part file.
    

----------------------------
Settings before Launching NX
----------------------------

The dlx file must be placed in one of the following locations:
    1. From where the NX session is launched
    2. $UGII_USER_DIR/application
    3. For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat


----------------------------
Settings after Launching NX
----------------------------

    1. Change the Role to Advanced.
                        
-----------------------
Example execution steps
-----------------------

    1. Start NX.

    2. Open any part file. There should be at least one feature available in that part.

    3. Launch the dialog by using the following command:

        a. Using the menu, Tools->Journal->Play... 
               - Invoke TreeListDemo.py file using Tools->Journal->Play.
    
    4.	This will launch the “Tree List Demonstration” dialog.  The functionality offered by "Tree List" and 
        "Node" are grouped together under the different groups on the dialog. The group-label provides the 
        hint on the functionality offered by tree and node.

    5.	Add/Delete Nodes, Icons and Column Text: 

        a.	Clicking "Add Node” button creates a node. The first column displays the title picked from Node 
            Title field. The second and third column displays the icon and text respectively.
            
        b.	To add a sub node, select a node in the Tree List and then click “Add Node” button.
            A sub node can be added at any level in the tree.
				
        c.	To delete a node/nodes, select the required node/nodes in the Tree List and click 
            “Delete Selected Node/s” button. Deleting a parent node will delete all of its associated child 
            nodes.
				
    6.	State Icon and ToolTip: 

        a.	Adding a node by clicking on the “Add Node” button by setting "Don't show state icons" adds a 
            node to the Tree List without any state icon.

        b.	Adding a node by setting "Show state icons" option adds a node with an unchecked state icon. 
            The unchecked icon can be checked.

        c.	Adding a node by setting "Other than checked/unchecked state icons" option adds  a node with a 
            random icon in place of the checked icon.

        d.	Enter some text in the node Tooltip string block and hit the enter button on the keyboard. 
            Hover the cursor on any of the nodes in the Tree List to see the entered text displayed as a 
            tooltip.
				
    7.	Node Edit:

        a.	Setting the node edit option to "Label Edit", allows editing of the label of the node in Tree 
            List. To change the label, select a node and press F2 button on the Keyboard or select the 
            column text, enter the new text for label and hit enter on the keyboard.

        b.	Setting the node Edit Options to "Combo Box Edit", allows the selection of the label from 
            a predefined Combo box. This edit option allows user-defined text apart from the options 
            available on Combo box

        c.	Setting the node Edit Options to "Listbox Edit", allows the selection of the label from 
            a predefined List box. This edit option does not allow user-defined text.

        d.	Setting the node Edit Options to "Don't allow node edits", doesn't allow any of the above 
            edits on the node.
				
    8.	Menu and Submenu: 

        a.	Toggle on the "Show Menu" option to see the popup menu on the right mouse button (RMB) 
            click on the node and tree.

        b.	RMB click on the tree allows to create nodes while RMB on node allows creation of a sub 
            node or deletion of a node.

        c.	The rest of the submenus and icons displayed in the RMB click popup are for representation 
            only. User can customize their actions on these menu clicks.
		   
    9.	Drag and Drop:
 
        Note: The drag and drop of nodes in this example is just for visual representation that drop is 
              allowed. In order for drop to work, users need to implement OnDropCallback in the automation 
              code. The dropType argument to the OnDropCallback indicates whether the nodes are dropped 
              On target node, Before target node or After target node.

        a.	Toggle on "Disallow drag" to disable dragging the node by left mouse click. While switching 
            off the toggle allows the node dragging.

        b.	The drop options will work only when the toggle "Disallow drag" is off.

        c.	Tree List provides various drop option as listed in the Drag and Drop group.

        d.	Setting the required drop option will show the corresponding visual effect on dragging and 
            dropping a selected node.
			
    10. Default Action
    
        Note: The Default Action toggle is disabled when Node edit Options is set to "Combo Box Edit" or 
              to "Listbox Edit". This is because double clicking on the tree list node is not allowed
              when the Node edit Options is set to "Combo Box Edit" or to "Listbox Edit".
        
        a. Toggle on "Default Action" and double click on the node in the tree list. This will invoke 
           the OnDefaultAction callback.
        
        b. Observe that the column text is changed to "Default Action" in the third column of the selected 
           node in the treelist. A message box is shown which indicates the change in the column text. 
           Click Ok on the dialog.
		   
    11.	Node Data and Cross Selection:

        a.	This capability of Tree List allows the user to create a node that is associated with the NXObject, 
            such as feature, curve etc. Selecting the node highlights the associatted object in the graphics
            window.

        b.	For creating such nodes, follow the instructions provided under the Instruction text box in the 
            "Node Data and Cross Selection" group.
		   
    12.	Redraw tree: 

        a.	Toggling off the Redraw option freezes the tree. When toggled on, the tree is updated with 
            all the actions that are performed after the tree was frozen. Also Show Menu does not work 
			when Redraw option is toggled off.

        b.	To see this behavior, follow the instructions mentioned in the text box in the “Redraw Tree” 
            group.

    13. Tree List Callback Information
    
        a. Toggling on the "Listing Window" will allow printing of invoked tree list's callback on the listing window. 

        b. Toggling off the "Listing Window" will not print the callback name on the listing window.
    


    

