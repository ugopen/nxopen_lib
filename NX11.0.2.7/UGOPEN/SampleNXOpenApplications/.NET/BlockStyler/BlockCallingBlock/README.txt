-------------------------------------------------------------------------------

              Copyright (c) 2015  Siemens PLM Software
                Unpublished - All rights reserved

   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
		         Block Styler Block Calling Block Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates two concepts: 
    * A BlockStyler Dialog calling another BlockStyler dialog
    * Usage of the PerformOK functionality

    This example does a trivial workflow of the main dialog Keeping a list of the Faces selected, a
    button to select the faces, and way to indicate what color to change the selected faces.  The Apply\OK
    will change the selected faces color.

    This example has two ways of running: normal and test mode.  In Normal mode the dialog
    will let the user pick which faces to change the colors.  While TestMode will pass in
    hardcoded journal identifiers to the SubDialog to select and the do the PerformOK when the "Select Faces"
    button is pressed.

--------------
Files required
--------------

 1. BlockCallingBlock.csproj
 2. SubDialog.cs
 3. SubDialog.dlx
 4. TopLevelDialog.cs
 5. TopLevelDialog.dlx
 6. SampleBlock.prt
	
-----------
Build Steps
-----------

Windows
-------
1. Open project file BlockCallingBlock.csproj

2. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called BlockCallingBlock.dll in the Debug directory.

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
  
    Once you have successfully finished with "Build Steps", 
    follow the steps below:

        2.1 Start NX.
  
        2.2 Open the supplied part - SampleBlock.prt
          	  
        2.3 Invoke Shared Library BlockCallingBlock.dll through  File->Execute->NX Open Menu (Ctrl+U).
        
        2.4 This will launch the TopDialog dialog.  Select "Select Face" button. Which will bring up a dialog to select a Face.  
        Select a single Face, and then wait and the dialog will perform a "PerformOK".  
        
        2.5 Repeat Step 2.4 and select a different face.

        2.6 Wait and see that PerformOK is done on the TopDialog and the faces will be changed to the color on the TopDialog.

    To Run this in "TestMode"

        2.1 Start NX.
  
        2.2 Open the supplied part - SampleBlock.prt
          	  
        2.3 Invoke Shared Library BlockCallingBlock.dll through  File->Execute->NX Open Menu (Ctrl+U).
        
        2.4 This will launch the TopDialog dialog.  Select "Select Face" button. This will return quickly with the faced selected.
         
        
        2.5 Repeat Step 2.4 and a different face will be selected.

        2.6 Wait and see that PerformOK is done on the TopDialog and the faces will be changed to the color on the TopDialog.
        
-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
