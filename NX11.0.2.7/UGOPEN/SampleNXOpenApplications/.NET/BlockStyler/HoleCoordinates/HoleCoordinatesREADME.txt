-------------------------------------------------------------------------------
'
'             Copyright (c) 2010  Siemens PLM Software
'               Unpublished - All rights reserved
'
'  
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
		           Block Styler Hole Coordinates Example
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
    2. HoleCoordinates.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/BlockStyler/HoleCoordinates)
    3. HoleCoordinates.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/HoleCoordinates)
    
-----------
Build Steps
-----------

Windows
-------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as HoleCoordinates. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the HoleCoordinates.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.

5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called HoleCoordinates.dll in the Debug directory.

           
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

    1. Start NX.

    2. Open HoleCoordinates.prt file.

    3. Launch the dialog by using any one of the methods mentioned below:

        3.1 Using Tools->Journal->Play 
        
	        - Invoke HoleCoordinates.vb file using Tools->Journal->Play or (Alt+F8).
	       
        3.2 Go to File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog. Navigate to HoleCoordinates.dll file.
        
    4. It will launch the Hole Position information dialog.    

    5. Specify a point and two vectors along with a face which contains ‘hole features’.

    6. Click on button “Get coordinates information of holes”.

    7. All the hole features on the selected face with the respective coordinate will be 
       listed in the List-Block.

    8. Selecting the item in the list (which indicates the feature name) will highlight 
        the respective hole feature.
        
        
-----
Note:
-----

"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."       
	
