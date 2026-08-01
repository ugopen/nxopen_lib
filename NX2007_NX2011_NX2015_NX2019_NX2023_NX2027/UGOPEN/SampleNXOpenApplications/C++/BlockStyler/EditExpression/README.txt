-------------------------------------------------------------------------------
'
'             Copyright (c) 2008  Siemens PLM Software
'               Unpublished - All rights reserved
'
'  
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
		          Block Styler Edit-Expression Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates editing an expression of a feature.

--------------
Files required
--------------

    1. EditExpression.cpp (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression)
    2. EditExpression.hpp (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression)
    3. EditExpression.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression)
    4. FeatureSeed.dlx    (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression)
    5. EditExpression.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression)
    
------------
Build Steps
------------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the Automation -> NX Open -> Open for C/C++ -> 
	  Open C Reference Guide -> Overview -> Setting up your system. 
      When setting the Application Settings, select "Create an Internal application" 
      and select C++ as the language. 

   2. Remove all the existing files from project.
   
   3. Add the EditExpression.cpp, EditExpression.hpp to Source Files and Header Files respectively 
      by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called EditExpression.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
     1. Open an NX command prompt window.
     2. Change directories to the directory containing the source code.
     3. Compile and link using uflink:
	
      ufcomp EditExpression.cpp
      uflink UFDLL=EditExpression.dll

   This will create EditExpression.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => EditExpression
   7. Do not add any subroutines or libraries.
       
   This will create EditExpression.so in the current directory.

   Exit out of ufmenu.
        
----------------------------
Settings before Launching NX
----------------------------
    The dlx file(s) must be placed in one of the following locations:
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

    2. Open EditExpression.prt file

    3. Go to File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog. Navigate to EditExpression.dll(EditExpression.so under Linux)file.

    4. Select a feature. The selected feature will be listed in list below. (You can add more 
       than one features in the list by clicking “Add New Set” button and then moving the focus 
       to the selection block and selecting the new feature. The list-items can be manipulated 
       using the 3 buttons provided on the right side of the list-block)

    5. Select the feature for which you want to edit an expression and click on button “Get Expressions”

    6. Select an expression which you want to edit in the list box. The expression name and 
       its value will get reflected in fields at the bottom of dialog. Enter a new value in the 
       ‘Value’ field and hit “Apply”/“OK”.
-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	 
   
        
