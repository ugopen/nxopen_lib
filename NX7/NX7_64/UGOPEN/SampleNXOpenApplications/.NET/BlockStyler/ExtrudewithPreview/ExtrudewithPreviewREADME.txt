' ==================================================================================
'
'             Copyright (c) 2008  Siemens PLM Software
'               Unpublished - All rights reserved
'
'  
' ==================================================================================

-------------------------------------------------------------------------------
        Block Styler Extrude with preview Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This Block Styler example is to demonstrate the use of block styler appication. 
The example demonstrates the creation of an extrude feature and has a preview 
facility available. 

--------------
Files required
--------------
1. ExtrudewithPreview.vb
3. ExtrudewithPreview.prt
2. ExtrudewithPreview.dlx

   The dlx file must be placed in one of the following locations:
    1.) From where NX session is launched
    2.) $UGII_USER_DIR/application
    3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

----------------------
How to execute the example
----------------------
1. Using Tools->Journal->Play 

	1. Start NX.
	2. Open 'ExtrudewithPreview.prt' part.
	3. Read the instruction under DIALOG LAUNCHING section of ExtrudewithPreview.vb
	   in order to understand where to keep the ExtrudewithPreview.dlx file.
	4. Invoke ExtrudewithPreview.vb file using Tools->Journal->Play.
	
2. By creating Shared Library and invoke it through File->Execute->NX Open Menu. 
   
-----------------------
How to Build VB example
-----------------------
1. Open Microsoft Visual Studio .Net.

2. Create a new VB project using the NX Open AppWizard. This is described in the 
   NX Open Programmers Guide -> Wizard Setup.
   Also information under Creating NX Open Automation -> Applications will be helpful.
   When setting the Application Settings, select "Create an Internal application"
   and select NXOpen.UI API. 
   Select to activate the application Explicitly and to unload when NX terminates.
   Then pick Finish.

3.  Add the ExtrudewithPreview.vb to the project by selecting the Project pulldown and select 
    "Add Existing Item...". Select the file using the popup window.

4. Build the internal image by going to the Build menu and selecting either "Build" or "Rebuild".

This will create an executable called ExtrudewithPreview.dll in the Release directory.
           
