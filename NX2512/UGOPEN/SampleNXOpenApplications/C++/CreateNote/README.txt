'===============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=================================================================================

----------------------------------------------------------------------------------
        		                  Create Note
----------------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates the placement of the drawing notes or symbol on user picked locations in drawing sheet.
The drawing notes or symbols are placed either by copying an existing note or by creating a note from a user defined
symbol. The required inputs to collect the information on the drawing note and its placement is aided by the 
block styler dialog. Then the placement of these notes is done using NXOpen C++ API.

--------------
Files required
--------------

    1. CreateNote.cpp
    2. CreateNote.hpp
    3. CreateNote.dlx    
	
The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CreateNote.


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
   
   3. Add the CreateNote.cpp, CreateNote.hpp to Source Files and Header Files respectively 
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called CreateNote.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp CreateNote.cpp
      uflink UFDLL=CreateNote.dll

   This will create CreateNote.dll in the current directory.

   Linux
   -----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select "y" for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => CreateNote
   7. Do not add any subroutines or libraries.
       
   This will create CreateNote.so in the current directory.

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
   1. Create a part with a drawing sheet in it. If you have a note in it, that would be helpful.
   2. Invoke CreateNote.dll (CreateNote.so on Linux) file using File->Execute->NX Open... menu command.
   3. In the dialog, if the note type option selection is "Create from user defined symbol" below are the steps:
		3.1 Select the name of the user defined symbol from the drop down list.
		Note: The above symbol list is populated using the NX default .sbf file. (To specify other .sbf file, click on browse file).
		3.2 Key in the scale and the aspect ratio values.
		3.3 Pick the location in the drawing sheet for the note placement.
		3.4 Verify that the selected symbol is placed in those positions.
		3.5 Now click Apply the dialog will be reset.
   4. In the dialog, if the note type option selection is "Copy existing symbol" below are the steps:
		4.1 Select a note or symbol in the drawing sheet using select note to clone block.
		4.2 Pick the location in the drawing sheet for the cloned note or symbol placement.
		4.3 Verify that the selected symbol is placed in those positions with the properties being cloned.
		4.4 Now click Apply the dialog will be reset.
   
   
-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
