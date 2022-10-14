-------------------------------------------------------------------------------


          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
		        Block Styler Tree list demonstration example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates some of the functionalities offered by Tree List as mentioned below: 

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

    1. TreeListDemo.vb
    2. TreeListDemo.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/TreeListDemo)
    3. Any Part file.
    
-----------
Build Steps
-----------   
    
 Windows
 -------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as TreeListDemo. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on popup menu.You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the TreeListDemo.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.
        
5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an shared library TreeListDemo.dll in the Debug directory.
    
Linux
-----
Not applicable

----------------------------
Settings before Launching NX
----------------------------

The dlx file must be placed in one of the following locations:
    1. From where NX session is launched
    2. $UGII_USER_DIR/application
    3. For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat


----------------------------
Settings after Launching NX
----------------------------

    1. Change the Role to Advanced with full menus.
                        
-----------------------
Example execution steps
-----------------------

    1. Start NX.

    2. Open any part file. There should be atleast one feature available in that part.

    3. Launch the dialog by using any one of the methods mentioned below:

        a. Using the menu, Tools->Journal->Play... 
               - Invoke TreeListDemo.vb file using Tools->Journal->Play.
        b. By creating a shared Library and invoking it through File->Execute->NX Open Menu.
		  (Refer Build steps to create a shared library that is TreeListDemo.dll)
    
    4.	This will launch the �Tree List Demonstration� dialog.  The functionality offered by "Tree List" and 
        "Node" are grouped together under the different groups on the dialog. The group-label provides the 
        hint on the functionality offered by tree and node.

    5.	Add/Delete Nodes, Icons and Column Text: 

        a.	Clicking "Add Node� button creates a node. The first column displays the title picked from Node 
            Title field. The second and third column displays the icon and text respectively.
            
        b.	To add a sub node, select a node in the Tree List and then click �Add Node� button.
            A sub node can be added at any level in the tree.
				
        c.	To delete a node/nodes, select the required node/nodes in the Tree List and click 
            �Delete Selected Node/s� button. Deleting a parent node will delete all of its associated child 
            nodes.
				
    6.	State Icon and ToolTip: 

        a.	Adding a node by clicking on the �Add Node� button by setting "Don't show state icons" adds a 
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
              allowed. In order for drop to work, users need to implement OnDropCallback in the automation code. 

        a.	Toggle on "Disallow drag" to disable dragging the node by left mouse click. While switching 
            off the toggle allows the node dragging.

        b.	The drop options will work only when the toggle "Disallow drag" is off.

        c.	Tree List provides various drop option as listed in the Drag and Drop group.

        d.	Setting the required drop option will show the corresponding visual effect on dragging and 
            dropping a selected node.
			
    10. Default Action
    
        Note: Default Action toggle is disabled when Node edit Options is set to "Combo Box Edit" or to "Listbox Edit".
		This is because double click on the tree list node is not allowed when Node edit Options is set to "Combo Box Edit" or to "Listbox Edit".
        
        a. Toggle on "Default Action" and double click on the node in the tree list. This will invoke OnDefaultAction callback.
        
        b. Observe that the column text is changed to "Default Action" in the third column of the selected node in the treelist.
           A message box is shown which indicates the change in the column text. Ok the dialog.
		   
    11.	Node Data and Cross Selection:

        a.	This capability of Tree List allows the user to create a node that is associated with the NXObject, 
            such as feature, curve etc. Selecting the node highlights the associatted object in the graphics
            window.

        b.	For creating such nodes, follow the instructions provided under the Instruction text box in the 
            "Node Data and Cross Selection" group.
		   
    12.	Redraw tree: 

        a.	Toggling off the Redraw option freezes the tree. When toggled on, the tree is updated with 
            all the actions that are performed after the tree was frozen 

        b.	To see this behavior, follow the instructions mentioned in the text box in the �Redraw Tree� 
            group.

    13. Tree List Callback Information
    
        a. Toggling on the "Listing Window" will allow printing of invoked tree list's callback on the listing window. 

        b. Toggling off the "Listing Window" will not print the callback name on the listing window.
    
-----
Note:
-----
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
    

