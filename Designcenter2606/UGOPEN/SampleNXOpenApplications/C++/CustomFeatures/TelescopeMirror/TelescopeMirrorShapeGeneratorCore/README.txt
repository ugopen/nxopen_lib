-------------------------------------------------------------------------------


          Copyright 2015 Siemens Industry Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Demonstration example for custom feature Telescope Mirror Shape Generator Core code.
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates the core logic for the "Telescope Mirror Shape Generator" custom feature.

--------------
Files required
--------------
    1. TelescopeMirrorShapeGeneratorCore.cpp
	2. CustomFeatureConfiguration.xml
	
 The above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CustomFeatures/TelescopeMirror/TelescopeMirrorShapeGeneratorCore
 
------------
Build Steps
------------

  Windows
  -------
   1. Using Visual Studio - create a new project with name "TelescopeMirrorShapeGeneratorCore" using the NX Open C++ Wizard.
      This is described in the Automation -> NX Open -> Open for C/C++ -> 
      Open C Reference Guide -> Overview -> Setting up your system. 
      When setting the Application Settings,
      select "An internal application that can be activated from an NX session (DLL)".	  

   2. Remove all the existing files from project.
   
   3. Add the TelescopeMirrorShapeGeneratorCore.cpp to Source Files by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called TelescopeMirrorShapeGeneratorCore.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
     1. Open an NX command prompt window.
     2. Change directories to the directory containing the source code.
     3. Compile and link using uflink:

    ufcomp TelescopeMirrorShapeGeneratorCore.cpp
      uflink UFDLL=TelescopeMirrorShapeGeneratorCore.dll TelescopeMirrorShapeGeneratorCore.obj

   This will create TelescopeMirrorShapeGeneratorCore.dll in the current directory.
  
----------------------------
Example execution steps
----------------------------
To execute the created executable, please follow the steps provided in the README.txt located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CustomFeatures/TelescopeMirror

-----
Note:
-----              
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
