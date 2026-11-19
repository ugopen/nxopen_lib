' ==================================================================================
'
'             Copyright (c) 2008  Siemens PLM Software
'               Unpublished - All rights reserved
'
'  
' ==================================================================================
-------------------------------------------------------------------------------
		Block Styler Hole-Coordinates Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates measurement of holes coordinates from user defined origin
using the Block Styler C++ APIs. 

--------------
Files required
--------------

    1. HoleCoordinates.cpp
    2. HoleCoordinates.hpp
    3. HoleCoordinates.dlx
    4. HoleCoordinates.prt
        
      The dlx file must be placed in one of the following locations:
      1.) From where NX session is launched
      2.) $UGII_USER_DIR/application
      3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
          recommended. This variable is set to a full directory path to a file 
          containing a list of root directories for all custom applications.
          e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

-------------------------
How to Build C++ examples
-------------------------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the Automation -> NXOpen -> Open for C/C++ -> 
	  Open C Reference Guide -> Overview -> Setting up your system. 
	  When setting the Application Settings,
      select "Create an Internal application" and select C++ as the language. 

   2. Remove all the existing files from project.
   
   3. Add the HoleCoordinates.cpp, HoleCoordinates.hpp to Source Files and Header Files respectively 
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called HoleCoordinates.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:

      uflink UFDLL=HoleCoordinates.dll

   This will create HoleCoordinates.dll in the current directory.

   Unix
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => HoleCoordinates
   7. Do not add any subroutines or libraries.
       
   This will create HoleCoordinates.so in the current directory.

   Exit out of ufmenu.

----------------------
How to run the example
----------------------

    1. Start NX.

    2. Open HoleCoordinates.prt file

    3. Launch the dialog by invoking the HoleCoordinates shared library through the
        File->Execute->NX Open... menu command. 

     4. Specify a point and two vectors along with a face which contains ‘hole features’.

     5. Click on button “Get coordinates information of holes”

     6. All the hole features on the selected face with the respective coordinate will be 
        listed in the List-Block.

     7. Selecting the item in the list (which indicates the feature name) will highlight 
        the respective hole feature

