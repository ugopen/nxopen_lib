'===============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=================================================================================

----------------------------------------------------------------------------------
        		        Fillout Title Block 
----------------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates the filling up of drawing notes in the empty title block of a 'C' size drawing sheet.
The inputs for the fields are queried from user with the help of a Block Styler dialog. Then the placement of these notes at 
appropriate locations in the Title Block is done using NXOpen C++ API. All the required annotation preferences are set 
during program execution.

--------------
Files required
--------------

    1. FillOutTitleBlock.cpp
    2. FillOutTitleBlock.hpp
    3. FillOutTitleBlock.dlx 
    4. FillOutTitleBlock_bonnet_5055.prt
	
The above listed files are Located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/FillOutTitleBlock.


-----------
Build Steps
-----------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NXOpen AppWizard.
      This is described in the Automation -> NXOpen -> Open for C/C++ -> 
	  Open C Reference Guide -> Overview -> Setting up your system -> Windows Operating System Setup. 
      When setting the Application Settings, select "Create an Internal application" 
      and select C++ as the language. 

   2. Remove all the existing files from project.
   
   3. Add the FillOutTitleBlock.cpp, FillOutTitleBlock.hpp to Source Files and Header Files respectively 
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called FillOutTitleBlock.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp FillOutTitleBlock.cpp
      uflink UFDLL=FillOutTitleBlock.dll

   This will create FillOutTitleBlock.dll in the current directory.

   Linux
   -----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select "y" for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => FillOutTitleBlock
   7. Do not add any subroutines or libraries.
       
   This will create FillOutTitleBlock.so in the current directory.

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
   1. Change the Role to Advanced with full menus if not set.
   2. Setup the drawing templates if not set, as per the following steps:
		2.1	In NX, go to Preferences-Palettes.
		2.2	On the palette dialog choose "Open Palette File".
		2.3	Browse to your "%UGII_BASE_DIR%\ugii\html_files" folder. (On Linux go to base dir /ugii/html_files/ folder).
		Note: the UGII_BASE_DIR is expanded in the SYSLOG if the system does not recognize the environment variable.
		2.4	Choose the "english_drawing_templates.pax" file.
		2.5	The palette should now be available on your resource bar.
			

-----------------------
Example execution steps
-----------------------
   1. Open the part FillOutTitleBlock_bonnet_5055.prt that has been provided. But any part will do.
   2. Select the template for a 'C' drawing, from the drawing templates tab.  
      Note: If the drawing templates tab has not already been set up, it needs to be set.
	  See the template setup steps under "Settings after Launching NX" session of this file to setup the drawing templates.
   3. Now you will be viewing a 'C' size drawing sheet with views and empty Title Block.
   4. Now invoke FillOutTitleBlock.dll( FillOutTitleBlock.so on linux) file using File->Execute->NX Open... menu command.
   5. When prompted, fill in the dialog with the information to populate in the Title block. Hit 'OK' when you are satisfied with the information.  
   6. The Title block in the drafting sheet will then be updated with the information that you had entered in the dialog.
   
-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
