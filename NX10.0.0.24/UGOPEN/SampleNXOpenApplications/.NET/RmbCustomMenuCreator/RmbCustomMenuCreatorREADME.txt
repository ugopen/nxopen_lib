' =============================================================================
'
'             Copyright (c) 2009  Siemens PLM Software
'               Unpublished - All rights reserved
'
'  
' =============================================================================
-------------------------------------------------------------------------------
        RMB Custom Menu Creator Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example demostrates adding custom popup menus/submenus for node(s) selected
in a Tc Navigator tree.

Customer implementation will use CustomPopupMenuHandler object to register two callback methods. 
NX Teamcenter Navigator will invoke the first callback to allow the customer to add custom RMB menus/submenus.
In order for the NX Teamcenter Navigator to invoke the callback to append custom RMB menus, all nodes 
selected must be any combination of Item, Item Revision, Dataset and Folder.
Methods like AddMenu, AddMenuItem and AddMenuSeparator can be used to add top-level menus and submenus.  
The second callback method will be invoked when the user actually selects a custom  menu command. 
Client can implement this callback to perform customer specific tasks. Method GetInvokedCommand can be 
used to get the selected menu item object of type CustomPopupuMenuItem. There should be only one instance 
of CustomPopupMenuHandler object per customer library. 


--------------
Files required
--------------
1. CustomMenuCreator.cs 


----------------------
How to execute the example
----------------------

Once you have successfully finished with "How to Build C# example" steps, 
follow the steps below:
   
    1. Start NX. 
    3. Go to File -> Execute ->NX Open.
    4. You will lead to window called "Execute User Function". 
    5. Navigate to the location of the .dll/.so file. Hit ok.
    6. Pick a item/itemrev/dataset/folder in the Teamcenter Navigator and hit RMB
    7. Popup menu will show custom popup menu entries.
    8  Select a custom menu entry and corresponding registered menu entry method will be invoked.
	
	
--------------------------
How to Build C# example
--------------------------
1. Open Microsoft Visual Studio .Net.

2. Create a new C# project using the NX Open AppWizard. This is described in the 
   NX Open Programmers Guide -> Wizard Setup.
   Also information under Creating NX Open Automation -> Applications will be helpful.
   When setting the Application Settings, select "Create an Internal application"
   and select NXOpen.UI API. 
   Select to activate the application Explicitly and to unload when NX terminates.
   Then pick Finish.

3.  Add the CustomMenuCreator.cs to the project by selecting the Project pulldown and select 
    "Add Existing Item...". Select the file using the popup window.

4. Build the internal image by going to the Build menu and selecting either "Build" or "Rebuild".

This will create an executable called CustomMenuCreator.dll in the Release directory.

