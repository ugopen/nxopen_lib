-------------------------------------------------------------------------------


          Copyright 2015 Siemens Industry Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Demonstration example for custom feature Pattern Curve Core code.
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates how a Custom feature "Pattern Curve" can be implemented.

--------------
Files required
--------------
    1. PatternCurveUI.hpp
	2. PatternCurveUI.cpp
	3. PatternCurveUI.dlx	
    4. PatternCurveUI_CPP_ReadMe.txt
	
 The above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CustomFeatures/PatternCurve/PatternCurveUI.
 
------------
Build Steps
------------

  Windows
  -------
   1. Using Visual Studio - create a new project with name "PatternCurveUI" using the NX Open C++ Wizard.
      This is described in the Automation -> NX Open -> Open for C/C++ -> 
      Open C Reference Guide -> Overview -> Setting up your system. 
      When setting the Application Settings,
      select "An internal application that can be activated from an NX session (DLL)".	  

   2. Remove all the existing files from project.
   
   3. Add the PatternCurveUI.cpp and PatternCurveUI.hpp to Source Files by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called PatternCurveUI.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
     1. Open an NX command prompt window.
     2. Change directories to the directory containing the source code.
     3. Compile and link using uflink:

    ufcomp PatternCurveUI.cpp
      uflink UFDLL=PatternCurveUI.dll PatternCurveUI.obj

   This will create PatternCurveUI.dll in the current directory.
   
  Linux
  -----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => dimprefix.
   7. Do not add any subroutines or libraries.
     
   This will create PatternCurveUI.so in the current directory.
   
----------------------------
Settings before Launching NX
---------------------------- 
The executable (PatternCurveUI.dll for Windows or PatternCurveUI.so for Linux) and PatternCurveUI.dlx must be placed in any one of the following locations mentioned below:

    1.    $UGII_USER_DIR/application
    2.    For released applications, using the environment variable UGII_CUSTOM_DIRECTORY_FILE is highly recommended. 
        This variable is set to a full directory path to a file containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
    
----------------------------
Settings after Launching NX
----------------------------

    None.    
  
-----------------------
Example execution steps
-----------------------

    1. Start NX.

    2. Open any part file. 

    3. Launch the dialog by creating a shared Library and invoking it through File->Execute->NX Open Menu.
    
    4. This will launch the “Pattern Curve” dialog.

    5. Provide inputs as indicated in dialog.

    6. Dialog OK/Apply creates the Pattern Curve.
	
	7. Newly created pattern curve feature can be edited by RMB on Part Navigator feature node and choosing Edit with Rollback
	
	8. Editing feature will launch the same dialog populated with usign edited feature.
	      
-----
Note:
-----
                
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
