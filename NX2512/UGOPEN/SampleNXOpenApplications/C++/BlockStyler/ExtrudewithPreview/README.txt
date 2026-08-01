-------------------------------------------------------------------------------
'
'             Copyright (c) 2008  Siemens PLM Software
'               Unpublished - All rights reserved
'
'  
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                 Block Styler Extrude with preview Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example is to demonstrate the use of selection intent block styler UI elements in
an NX Open Block Styler application. The application creates an extrude feature from 
a section defined by the user. A preview facility for the feature is also provided 
in the example. 

--------------
Files required
--------------
1. ExtrudewithPreview.cpp 
2. ExtrudewithPreview.hpp
3. ExtrudewithPreview.prt
4. ExtrudewithPreview.dlx

The above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/ExtrudewithPreview.

------------
Build Steps
------------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the Automation -> NX Open -> Open for C/C++ -> 
	  Open C Reference Guide -> Overview -> Setting up your system. 
	  When setting the Application Settings,
      select "Create an Internal application" and select C++ as the language. 

   2. Remove all the existing files from project.
   
   3. Add the ExtrudewithPreview.cpp, ExtrudewithPreview.hpp to Source Files and Header Files respectively 
      by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called ExtrudewithPreview.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
       1. Open an NX command prompt window.
       2. Change directories to the directory containing the source code.
       3. Compile and link using uflink:

      uflink UFDLL=ExtrudewithPreview.dll

   This will create ExtrudewithPreview.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => ExtrudewithPreview
   7. Do not add any subroutines or libraries.
       
   This will create ExtrudewithPreview.so in the current directory.

   Exit out of ufmenu.
   
----------------------------
Settings before Launching NX
----------------------------
 The dlx file must be placed in one of the following locations:
    1. From where NX session is launched
    2. $UGII_USER_DIR/application
    3. For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set using a full directory path to a file 
        containing a list of root directories for all custom applications.
        For example, UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
        
----------------------------
Settings after Launching NX
----------------------------
   1. Change the Role to Advanced if not set.
   	  
-----------------------
Example execution steps
-----------------------

    1. Start NX.

    2. Open "ExtrudewithPreview.prt" part file.

    3. Go to File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog. 
       Navigate to ExtrudewithPreview.dll (ExtrudewithPreview.so under Linux)file.
       
    4. It will launch the Extrude with Preview Dialog Box.   
    
    5. Select curves or edges from the part to extrude.
    
    6. Specify the extrude direction.
    
    7. Specify the start and end Distance for the extrude feature.
    
    8. If the "Preview" toggle is ON, the preview of the extrude is visible on the screen.
    
    9. Click OK or Apply to create the feature.
    
-----
Note:
-----
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	 
       
    
    
   
  
    

        
