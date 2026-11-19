'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

-------------------------------------------------------------------------------
        		Block Styler Update Example
-------------------------------------------------------------------------------

-------------------
Example Description
-------------------
This Block Styler example is the one given in the Block Styler Update section
of the Block Styler chapters in the NXOpen Programmer’s Guide. The example shows 
a minimum number of template source files edits to demonstrate how to handle 
events from various blocks in the given dialog.

--------------
Files required
--------------

    1. UpdateExample.cpp
    2. UpdateExample.hpp
    3. UpdateExample.dlx 

The above listed files are Located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/UpdateExample.


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
   
   3. Add the UpdateExample.cpp,UpdateExample.hpp to Source Files and Header Files respectively 
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called UpdateExample.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp UpdateExample.cpp
      uflink UFDLL=UpdateExample.dll

   This will create UpdateExample.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => UpdateExample
   7. Do not add any subroutines or libraries.
       
   This will create UpdateExample.so in the current directory.

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

    2. Create new part.

    3. Invoke UpdateExample.dll (UpdateExample.so on linux) file using  File->Execute->NX Open... menu command.

    4. The above step will launch UpdateExample dialog.

    5. Then the Dialog should behave as follows:
	
    	5.1 Input String Block - the user may enter a string which will be copied to the Output 
   	String Block.

    	5.2 Include Number Toggle Block - when this toggle in ON the following number will be
   	appended to the Output String Block.
	
    	5.3 Number Integer Block - a slider that the user can use to set a number that is 
   	optionally appended to the Output String Block.

    	5.4 Output String Block - a String Block that is only used to display the input string 
  	and the optional number. This block is always disabled.

    	5.5 Lock Input String Toggle - when this toggle is ON the input string is disabled.

    	5.6 Lock Number Toggle - when this toggle is ON the number slider is disabled.
		
-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	  
