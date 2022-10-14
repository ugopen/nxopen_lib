' =============================================================================
'
'             Copyright (c) 2008  Siemens PLM Software
'               Unpublished - All rights reserved
'
'  
' =============================================================================
-------------------------------------------------------------------------------
		Block Styler ColoredBlock Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates creation of colored block using the Block Styler .Net APIs. 
The set of APIs designed for Block Styler application are property based. While using 
these APIs one must be aware about the Block, its associated properties and their datatype.
Executing this example will launch a dialog which allows you to pick the point and 
color to create a block.

--------------
Files required
--------------
1. ColoredBlock.vb Or ColoredBlock.cs 
2. ColoredBlock.dlx :This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/ColoredBlock. 
	
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
	2. Create new part.
	3. Read the instruction under DIALOG LAUNCHING section of ColoredBlock.vb
	   in order to understand where to keep the ColoredBlock.dlx file.
	4. Invoke ColoredBlock.vb file using Tools->Journal->Play.
	
2. By creating Shared Library and invoke it through File->Execute->NX Open Menu. 
   
   Once you have successfully finished with "How to Build VB/C# example" steps, 
   follow the steps below:

	1. Start NX.
	2. Create new part.
	3. Read the instruction under DIALOG LAUNCHING section of ColoredBlock.vb
	   in order to understand where to keep the ColoredBlock.dlx file.
	4. Invoke Shared Library through  File->Execute->NX Open  Menu.
	
--------------------------
How to Build VB/C# example
--------------------------
1. Open Microsoft Visual Studio .Net.

2. Create a new VB/C# project using the NX Open AppWizard. This is described in the 
   NX Open Programmers Guide -> Wizard Setup.
   Also information under Creating NX Open Automation -> Applications will be helpful.
   When setting the Application Settings, select "Create an Internal application"
   and select NXOpen.UI API. 
   Select to activate the application Explicitly and to unload when NX terminates.
   Then pick Finish.

3.  Add the ColoredBlock.vb to the project by selecting the Project pulldown and select 
    "Add Existing Item...". Select the file using the popup window.

4. Build the internal image by going to the Build menu and selecting either "Build" or "Rebuild".

This will create an executable called ColoredBlock.dll in the Release directory.

