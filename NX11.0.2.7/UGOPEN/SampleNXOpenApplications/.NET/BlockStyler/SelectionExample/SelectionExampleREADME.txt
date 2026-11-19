-------------------------------------------------------------------------------

              Copyright (c) 2010  Siemens PLM Software
              Unpublished - All rights reserved
'
'  
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                   Block Styler Selection Example
-------------------------------------------------------------------------------

-----------
Description
-----------
The example shows two selection blocks used to select edges and features. 
It also includes filter callback code for each block.
 

--------------
Files required
--------------
1. SelectionExample.vb 
2. SelectionExample.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/SelectionExample)

-----------
Build Steps
-----------

Windows
-------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as SelectionExample. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on popped menu.You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the SelectionExample.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.
        
5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an shared library SelectionExample.dll in the Debug directory.


Linux
-----
  N/A

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
Example Execution Steps
-----------------------
1. Using Tools->Journal->Play (Alt+F8)

	1. Start NX.
	
	2. Create a new part with atleast one feature(Eg:Block). 
	
	3. Follow any one of the methods mentioned below:

           3.1 Using Tools->Journal->Play  
            
                  - Invoke SelectionExample.vb file using Tools->Journal->Play (Alt+F8).
               
           3.2 By creating Shared Library and invoke SelectionExample.dll through File->Execute->NX Open Menu (Ctrl+U).
         
	4. It will launch the New "Selection Example" dialog, Select the edges to chamfer and Enter the chamfer angle as per the user's Interest, then click on "Apply".
	   It will create the chamfer on the selected edge with the specified chamfer angle.
	   
	5. Then click on "select chamfer" button and select the chamfer on the feature which you want to remove.Hit "OK". Now the selected chamfers will be removed.   
	   
	6. The following describes the behaviour of the dialog.
	  
	   6.1 Edge Select Block – this selection block will select edges that Chamfer features
               will be applied to.
         6.2 Face Limit Toggle Block – when this toggle in ON the edges that are selected
               will be limited to just the edges on a single face. Also, when this toggle is
               first turned ON, the edge selection list is cleared.
         6.3 Angle Double Block – this value is used to define the angle of the Chamfer features.
         6.4 Feature Select Block – this selection block will select Chamfer features that are removed.
         6.5 Angle Limit Toggle – when this toggle is ON the Chamfer features are limited to those 
               that have the angle in the next block. Also, when this toggle is first turned on the 
               selected Chamfer features are cleared.
         6.6 Angle Limit Double – when this toggle is ON the value is this block is used to limit
               Chamfer selection to only those of the given angle.
	                  
-----
Note
-----
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."          
