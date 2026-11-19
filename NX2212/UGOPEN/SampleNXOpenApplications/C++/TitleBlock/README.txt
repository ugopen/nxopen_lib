'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		Title Block Example
------------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates the placement of symbol(.sbf file) in the drafting application through NXOpen C++ API
and also placing drawing notes in the desired location with all the Annotation preferences are being set during program
execution.

--------------
Files required
--------------

    1. TitleBlock.cpp
    2. TitleBlock.hpp
    3. TitleBlock.dlx 
    4. TitleBlock_DrawingSheet.prt
    5. special.sbf

The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/TitleBlock.


------------
Build Steps
------------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NXOpen AppWizard.
      This is described in the Automation -> NXOpen -> Open for C/C++ -> 
	  Open C Reference Guide -> Overview -> Setting up your system -> Windows Operating System Setup. 
      When setting the Application Settings, select "Create an Internal application" 
      and select C++ as the language. 

   2. Remove all the existing files from project.
   
   3. Add the  TitleBlock.cpp, TitleBlock.hpp to Source Files and Header Files respectively 
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called  TitleBlock.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp  TitleBlock.cpp
      uflink UFDLL= TitleBlock.dll

   This will create  TitleBlock.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link =>  TitleBlock
   7. Do not add any subroutines or libraries.
       
   This will create TitleBlock.so in the current directory.

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

    2. Open the part  TitleBlock_DrawingSheet.prt that contains a drawing sheet. 

    3. Invoke  TitleBlock.dll ( TitleBlock.so on Linux) file using  File->Execute->NX Open... menu command.

    4. The above step will launch TitleBlock dialog.

    5. Fill in Part Name and Author Name fields, and hit OK on the dialog.

    6. And then the program will insert a custom symbol for the title block from special.bf file 

    7. Then it inserts the labels in the title block and the user entered data.

    8. The date field is determined by the System's date

    9. Verify that entered information is correct in the title block as per the given input in the dialog.
    
   10. The title block can then be moved to another location on the sheet.Notice that all the text is 
       associative to the framing title block.
	   
-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	
