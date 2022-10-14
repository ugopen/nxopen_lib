===============================================================================
'
'       Copyright 2012 Siemens Product Lifecycle Management Software Inc.
'                           All Rights Reserved.
'
'
'=================================================================================

----------------------------------------------------------------------------------
                        ConfigureContextMenu Example
----------------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates how to customize context menus in NX. It defines basic 
functionality for making changes to context menu options for the C++ language.  

--------------
Files required
--------------

    1. ConfigureContextMenu.cpp
    2. ConfigureContextMenu.h

The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/ConfigureContextMenu.


-----------
Build Steps
-----------

   Windows
   -------
   1. Using Visual studio - create a new project using the NXOpen AppWizard.
      This is described in the Automation -> NXOpen -> Open for C/C++ -> 
      Open C Reference Guide -> Overview -> Setting up your system -> Windows operating system setup. 
      When setting the Application Settings, select "Create an Internal application" 
      and select C++ as the language. 
   2. Remove all the existing files from project.
   3. Add the ConfigureContextMenu.cpp, ConfigureContextMenu.h to Source Files and Header files respectively 
      by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.
   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
   This will create an executable called ConfigureContextMenu.dll and ConfigureContextMenu.lib  in the 'Debug' directory.

 The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:

      ufcomp ConfigureContextMenu.cpp
      uflink UFDLL=ConfigureContextMenu.dll

   This will create ConfigureContextMenu.dll and ConfigureContextMenu.lib in the current directory.

   Linux
   -----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select "y" for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => ConfigureContextMenu
   7. Do not add any subroutines or libraries.

   This will create ConfigureContextMenu.so and ConfigureContextMenu.o in the current directory.

   Exit out of ufmenu.


----------------------------
Settings before Launching NX
----------------------------
   1. Create the below folder structure in any of the system drives and place the following files:
        + ConfigureContextMenu
            + startup
                a. ConfigureContextMenu.dll on Windows or ConfigureContextMenu.so on Linux (This file is obtained from the build steps) 

   2.   Set the variable UGII_USER_DIR pointing to the directory ConfigureContextMenu location in NX command prompt.
        For ex: if ConfigureContextMenu is created in the location D:\ConfigureContextMenu then the setting should be "set UGII_USER_DIR=D:\ConfigureContextMenu" on Windows.
        On Linux, the variable  should be "export UGII_USER_DIR=/D/ConfigureContextMenu"

----------------------------
Settings after Launching NX
----------------------------
    None

-----------------------
Example execution steps
-----------------------

        1. Start NX.

        2. Create a new part

        3. Change the Role to Advanced if not set.

        4. Insert a Block, go to Insert->Design Feature->Block. 

        5. Right-click on the Block in the Part Navigator.  Notice that Properties has moved to the top of the context menu and is the default option.

        6. Right-click on the Block in the Graphics Window.  Notice that here the Delete option has been removed.

        7. Insert a Cylinder, go to Insert->Design Feature->Cylinder.

        8. Right-click on the Cylinder in the Graphics Window.  Notice that the submenu "Custom" has been added that includes a Visualization Preferences entry.

-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

