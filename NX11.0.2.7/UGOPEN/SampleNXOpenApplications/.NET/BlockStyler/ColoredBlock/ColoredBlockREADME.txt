-------------------------------------------------------------------------------

              Copyright (c) 2008  Siemens PLM Software
                Unpublished - All rights reserved

   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
		         Block Styler Colored Block Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates creation of colored block using the Block Styler .Net APIs. 
The set of APIs designed for Block Styler application are property based. While using 
these APIs one must be aware about the Block, its associated properties and their data type.
Executing this example will launch a dialog which allows you to pick the point and 
color to create a block.

--------------
Files required
--------------

 1. ColoredBlock.vb 
 2. ColoredBlock.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/ColoredBlock) 
	
-----------
Build Steps
-----------

Windows
-------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as ColoredBlock. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the ColoredBlock.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.

5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called ColoredBlock.dll in the Debug directory.

Linux
-------
   -NA-

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

 1. Change the Role to Advanced.

--------------------------
Example execution steps
--------------------------

 1. Using Tools->Journal->Play
   
        1.1 Start NX.
  
        1.2 Create new part.
        
        1.3 Invoke ColoredBlock.vb file using Tools->Journal->Play (Alt+F8).
        
        1.4 It will launch the New ColoredBlock dialog; Enter the Block parameter for the Height, Width, Length of the Block, Specify block origin & color of the Block as per the user's Interest.
	        It will create the new ColoredBlock at the specified Location.
	
 2. By creating Shared Library and invoke it through File->Execute->NX Open Menu. 
   
    Once you have successfully finished with "Build Steps", 
    follow the steps below:

        2.1 Start NX.
  
        2.2 Create new part.
          	  
        2.3 Invoke Shared Library ColoredBlock.dll through  File->Execute->NX Open Menu (Ctrl+U).
        
        2.4 It will launch the New ColoredBlock dialog, Enter the Block parameter for the Height, Width, Length of the Block, Specify block origin & color of the Block as per the user's Interest.
	        It will create the new ColoredBlock at the specified Location.
        
-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
