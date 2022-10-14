-------------------------------------------------------------------------------

              Copyright (c) 2010  Siemens PLM Software
                Unpublished - All rights reserved

'  
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
               Block Styler Extrude with preview Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This Block Styler example is to demonstrate the use of block styler application. 
The example demonstrates the creation of an extrude feature and has a preview 
facility available. 

--------------
Files required
--------------

     1. ExtrudewithPreview.vb
     2. ExtrudewithPreview.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/ExtrudewithPreview) 
     3. ExtrudewithPreview.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/ExtrudewithPreview) 
    
-----------
Build Steps
-----------

Windows
-------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as ExtrudewithPreview. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the ExtrudewithPreview.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.

5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called ExtrudewithPreview.dll in the Debug directory.

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
   
-----------------------
Example execution steps
-----------------------
1. Using Tools->Journal->Play 

	1.1 Start NX.
	
	1.2 Open 'ExtrudewithPreview.prt' part.
		   
	1.3 Invoke ExtrudewithPreview.vb file using Tools->Journal->Play (Alt+F8).
	    It will launch the Extrude with Preview Dialog Box.Select Curve,Specify Vector,enter the parameters in Limits and preview as per the user's interest.
	    This will create the extrude with preview for the selected curve.
	    	
2. By creating Shared Library and invoke it through File->Execute->NX Open Menu. 

        2.1 Start NX.
	
	2.2 Open 'ExtrudewithPreview.prt' part.
	
	2.3 Invoke Shared Library ExtrudewithPreview.dll through File->Execute->NX Open Menu (Ctrl+U). 
	    It will launch the Extrude with Preview Dialog Box.Select Curve,Specify Vector,enter the parameters in Limits and preview as per the user's interest.
	    This will create the extrude with preview for the selected curve.
      
-----
Note:
-----

"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
