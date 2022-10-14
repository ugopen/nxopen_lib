' ==================================================================================
'
'             Copyright (c) 2010  Siemens PLM Software
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
 using the Block Styler .Net APIs. 

--------------
Files required
--------------

    1. HoleCoordinates.vb
    2. HoleCoordinates.dlx: This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/HoleCoordinates.
    3. HoleCoordinates.prt: This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/HoleCoordinates.
        
      The dlx file must be placed in one of the following locations:
      1.) From where NX session is launched
      2.) $UGII_USER_DIR/application
      3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
          recommended. This variable is set to a full directory path to a file 
          containing a list of root directories for all custom applications.
          e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

----------------------
How to run the example
----------------------

    1. Start NX.

    2. Open HoleCoordinates.prt file

    3. Launch the dialog by using any one of the methods mentioned below:

        a. - Using Tools->Journal->Play 
	   - Read the instruction under DIALOG LAUNCHING section of HoleCoordinates.vb
             file in order to understand where to keep the HoleCoordinates.dlx file.
	   - Invoke HoleCoordinates.vb file using Tools->Journal->Play.
        b. By creating Shared Library and invoke it through File->Execute->NX Open Menu.

     4. Specify a point and two vectors along with a face which contains ‘hole features’.

     5. Click on button “Get coordinates information of holes”

     6. All the hole features on the selected face with the respective coordinate will be 
        listed in the List-Block.

     7. Selecting the item in the list (which indicates the feature name) will hightlight 
        the respective hole feature
	
--------------------------
How to Build VB example
--------------------------

    1. Open Microsoft Visual Studio .Net.

    2. Create a new VB project using the NX Open AppWizard. This is described in the 
       NX Open Programmers Guide -> Wizard Setup.
       Also information under Creating NX Open Automation -> Applications will be helpful.
       When setting the Application Settings, select "Create an Internal application"
       and select NXOpen.UI API. 
       Select to activate the application Explicitly and to unload when NX terminates.
       Then pick Finish.

    3. Add the HoleCoordinates.vb to the project by selecting the Project pulldown and select 
       "Add Existing Item...". Select the file using the popup window.

    4. Build the internal image by going to the Build menu and selecting either "Build" or "Rebuild".
       This will create an executable called HoleCoordinates.dll in the Release directory.
