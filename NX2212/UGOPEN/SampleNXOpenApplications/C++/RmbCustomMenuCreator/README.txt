'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
                  RMB Custom Menu Creator Example
------------------------------------------------------------------------------

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
   2. CustomMenuCreator.h

  The above listed files are located at
  $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/RmbCustomMenuCreator.

------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio .Net.

   2. Create new project as:
        2.1. File->New->Project.
 	2.2. Using Visual C++ Projects select the NX Open AppWizard, Class Library Application, Enter
             name as 'CustomMenuCreator'. Click Next
        2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
             and select 'C++'. 
        2.4. Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

   3. Remove the CustomMenuCreator.cpp file from the source folder in the project. Highlight it in the Solution Explorer and use 
      the 3rd mouse button and pull to remove it. You will receive a pop-up that says it will be deleted permanently. Hit OK.

   4. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'. Navigate to and add the CustomMenuCreator.cpp & CustomMenuCreator.h file.

   5. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.
   		
   6. This will create an executable called CustomMenuCreator.dll in the \Debug directory.


   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp CustomMenuCreator.cpp
      uflink UFDLL=CustomMenuCreator.dll

   This will create CustomMenuCreator.dll in the current directory.


   Linux
   -------
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => CustomMenuCreator
   7. Do not add any subroutines or libraries.
       
   This will create CustomMenuCreator.so in the current directory.

   Exit out of ufmenu.

----------------------------
Settings before Launching NX
----------------------------
-NA-

----------------------------
Settings after Launching NX
----------------------------
1. Change the Role to Advanced.

-----------------------
Example execution steps
-----------------------
     Journal execution
     ------------------
     -NA-

     Shared Library execution
     ------------------------
      1. File -> Execute -> NX Open through Menu or type Ctrl+U to open the
         "Execute User Function" dialog.
      2. Browse and select the CustomMenuCreator.dll/.so and execute.
      3. Pick a item/itemrev/dataset/folder in the Teamcenter Navigator and hit RMB
      4. Popup menu will show custom popup menu entries.
      5. You should be able to see the following options. 
         #Main Menu 1
         #Main Menu 2 > #Sub Menu 2-1
                        #Sub Menu 2-1 > #Sub Menu 2-2-1 
      6. Select a custom menu entry and corresponding registered menu entry will be 
         displayed in the information window
    
-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

'=================================End=========================================
