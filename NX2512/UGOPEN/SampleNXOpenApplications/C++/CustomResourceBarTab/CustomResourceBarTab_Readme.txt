===============================================================================
'
'       Copyright 2014 Siemens Product Lifecycle Management Software Inc.
'                           All Rights Reserved.
'
'
'=================================================================================

----------------------------------------------------------------------------------
                        CustomResourceBarTab Example
----------------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates how to embed the third party window into a tab within NX resource bar.
This exmaple can only be built on Windows.


--------------
Files required
--------------

    1. CustomResourceBarTab.cpp
    2. CustomResourceBarTab.h

The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CustomResourceBarTab.


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
   3. Add the CustomResourceBarTab.cpp, CustomResourceBarTab.h to Source Files and Header files respectively 
      by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.
   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
   This will create an executable called CustomResourceBarTab.dll and CustomResourceBarTab.lib  in the 'Debug' directory.

 The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:

      ufcomp CustomResourceBarTab.cpp
      uflink UFDLL=CustomResourceBarTab.dll

   This will create CustomResourceBarTab.dll and CustomResourceBarTab.lib in the current directory.

   
----------------------------
Settings before Launching NX
----------------------------
   1. Create the below folder structure in any of the system drives and place the following files:
        + CustomResourceBarTab
            + startup
                a. CustomResourceBarTab.dll on Windows (This file is obtained from the build steps) 

   2.   Set the variable UGII_USER_DIR pointing to the directory CustomResourceBarTab location in NX command prompt.
        For example: 
		if CustomResourceBarTab is created in the location D:\CustomResourceBarTab then the setting should be "set UGII_USER_DIR=D:\CustomResourceBarTab" on Windows.

----------------------------
Settings after Launching NX
----------------------------
    None

-----------------------
Example execution steps
-----------------------

        1. Start NX.

        2. A "Main" window with five push buttons is created and displayed.

        3. Click on the "Add New Tab" button to add a new tab to the NX resource bar area.

        4. Click on the "Activate New Tab" button to activate the newly created tab. The resource bar docking window will display with controls.

        5. Click on the "Hide New Tab" button to hide the newly created tab. The resource bar docking window will display another tab's content.

        6. Click on the "Show New Tab" button to show the hidden tab. The resource bar docking window won't display unless it is undocked before the tab being hidden.

        7. Click on the "Remove New Tab" button to remove the newly created tab. The resource bar docking window will display another tab's content.

-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

