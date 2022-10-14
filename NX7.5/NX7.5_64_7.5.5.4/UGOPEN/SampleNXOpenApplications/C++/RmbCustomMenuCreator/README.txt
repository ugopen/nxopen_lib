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

This example demonstrates adding custom popup menus/submenus for node(s) selected
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
1. CustomMenuCreator.cpp
2. CustomMenuCreator.hpp
   
        
-------------------------
How to Build C++ examples
-------------------------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the NX Open for C/C++ -> Open C Reference Guide -> 
      Overview -> setting up your system. When setting the Application Settings,
      select "Create an Internal application" and select C++ as the language. 

   2. Add the CustomMenuCreator.cpp, CustomMenuCreator.hpp to Source Files and Header Files respectively 
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   3. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called CustomMenuCreator.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:

      uflink UFDLL=CustomMenuCreator.dll

   This will create CustomMenuCreator.dll in the current directory.

   Unix
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => CustomMenuCreator
   7. Do not add any subroutines or libraries.
       
   This will create ColoredBlock.so in the current directory.

   Exit out of ufmenu.

----------------------
How to Run C++ Example
----------------------

Once you have successfully finished with "How to Build C++ example" steps, follow the steps below:

    1. Start NX. On Unix, this must be done using ugmenu or $UGII_ROOT_DIR/ugii.
    3. Go to File -> Execute ->NX Open.
    4. You will lead to window called "Execute User Function". 
    5. Navigate to the location of the .dll/.so file. Hit ok.
    6. Pick a item/itemrev/dataset/folder in the Teamcenter Navigator and hit RMB
    7. Popup menu will show custom popup menu entries.
    8  Select a custom menu entry and corresponding registered menu entry method will be invoked.
