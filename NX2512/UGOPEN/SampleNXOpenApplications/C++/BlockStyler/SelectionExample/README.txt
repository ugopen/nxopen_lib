-------------------------------------------------------------------------------
'
'             Copyright (c) 2008  Siemens PLM Software
'               Unpublished - All rights reserved
'
'  
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                       Block Styler Selection Example
-------------------------------------------------------------------------------

-----------
Description
-----------
The example shows two selection blocks used to select edges and features. 
It also includes filter callback code for each block.

--------------
Files required
--------------

   1. SelectionExample.cpp 
   2. SelectionExample.hpp
   3. SelectionExample.dlx 

The above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/SelectionExample.

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
   
   3. Add the SelectionExample.cpp, SelectionExample.hpp to Source Files and Header Files respectively 
      by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called SelectionExample.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
      1. Open an NX command prompt window.
      2. Change directories to the directory containing the source code.
      3. Compile and link using uflink:

      uflink UFDLL=SelectionExample.dll

   This will create SelectionExample.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => SelectionExample
   7. Do not add any subroutines or libraries.
       
   This will create SelectionExample.so in the current directory.

   Exit out of ufmenu.
   
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
    1. Change the Role to Advanced if not set.
          
-----------------------
Example execution steps
-----------------------

    1. Start NX.
	
    2. Create a new part with at least one feature(Eg:Block).
    
    3. Go to File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog. 
       Navigate to SelectionExample.dll (SelectionExample.so under Linux)file. 
        
    4. It will launch the New "Selection Example" dialog, Select the edges to chamfer and Enter the chamfer angle as per the user's Interest, then click on "Apply".
	   It will create the chamfer on the selected edge with the specified chamfer angle.
	   
	5. Then click on "select chamfer" button and select the chamfer on the feature which you want to remove.Hit "OK". Now the selected chamfers will be removed.   
	   
	6. The following describes the behaviour of the dialog.
	  
	   6.1 Edge Select Block – this selection block will select edges that Chamfer features
           will be applied to.
       6.2 Face Limit Toggle Block – when this toggle in ON the edges that are selected
           will be limited to just the edges on a single face. Also, when this toggle is
           first turned ON, the edge selection list is cleared.
       6.3 Angle Double Block – this value is used to define the angle of the Chamfer features.
       6.4 Feature Select Block – this selection block will select Chamfer features that are removed.
       6.5 Angle Limit Toggle – when this toggle is ON the Chamfer features are limited to those 
           that have the angle in the next block. Also, when this toggle is first turned on the 
           selected Chamfer features are cleared.
       6.6 Angle Limit Double – when this toggle is ON the value in this block is used to limit
           Chamfer selection to only those of the given angle.
           
-----
Note:
-----
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	 
                  
