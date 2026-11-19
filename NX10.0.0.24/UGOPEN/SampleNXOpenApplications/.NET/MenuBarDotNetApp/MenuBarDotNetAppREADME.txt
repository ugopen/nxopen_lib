'=============================================================================
'
'                   Copyright (c) 2013 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'   
'
' =============================================================================

------------------------------------------------------------------------------------
						  MenuBarDotNetApp  Example
------------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates how a custom application is added to NX. It defines menubar applications with callbacks
for both the C Sharp and VB.Net languages and adds the applications to the start menu.  

--------------
Files required
--------------

    1. MenuBarCSharpApp.cs
    2. MenuBarCSharpApp.men
    3. MenuBarDotNetAppButton.men
    4. MenuBarVbApp.men
    5. MenuBarVbApp.vb

The above listed files are located at
$UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\MenuBarDotNetApp
    
-----------
Build Steps
-----------

    Windows
    -------
    For VB.Net:

    1. Open Microsoft Visual Studio .Net.

    2. Create a new Vb project using the NX Open AppWizard. 
       Create new project as:
            2.1 File->New->Project.
 	        2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as MenuBarVbApp. Click Next.
            2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
            2.4 Select to activate the application explicitly and to unload the application when NX session terminates. Click Finish.

    3. Remove all *.vb files from created project by clicking MB3 on respective file and 
       clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
    4. Add the MenuBarVbApp.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
       the popup window.

    5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

    This will create an executable called MenuBarVbApp.dll in the Debug directory.


    For C Sharp:-

    1. Open Microsoft Visual Studio .Net.

    2. Create a new VC# project using the NX Open AppWizard. 
       Create new project as:
            2.1 File->New->Project.
 	         2.2 Select VC# Project using the NX Open AppWizard, Class Library Application, Enter name as MenuBarCSharpApp. Click Next.
            2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
            2.4 Select to activate the application explicitly and to unload the application when NX session terminates. Click Finish.

    3. Be sure to include a reference to Microsoft.VisualBasic before building the solution
   
    4. Remove all *.cs files from created project by clicking MB3 on respective file and 
       clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
    5. Add the MenuBarCSharpApp.cs to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
       the popup window.

    6. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

    This will create an executable called MenuBarCSharpApp.dll in the Debug directory.

    Linux
    -------
    -N/A-

----------------------------
Settings before Launching NX
----------------------------
    1. Create the below folder Structure in any of the sytem drives and place the following files:
		+ MenuBarDotNetApp
			+ application
				a. MenuBarVbApp.men
				b. MenuBarCSharpApp.men
				c. MenuBarVbApp.dll (This file is obtained from the build steps For VB.Net)
				d. MenuBarCSharpApp.dll (This file is obtained from the build steps For C Sharp)
			+ startup
				a. MenuBarDotNetAppButton.men
	
   2. Set the varaible UGII_USER_DIR pointing to the directory MenuBarDotNetApp location in NX command prompt.
      For ex: if MenuBarDotNetApp is created in the location D:\MenuBarDotNetApp then the setting should be "set UGII_USER_DIR = D:\MenuBarDotNetApp"
     

----------------------------
Settings after Launching NX
----------------------------

    1. Change the Role to Advanced.
    
    
--------------------------
Example execution steps
--------------------------
    
    1. Start NX.
        
    2. Create a new part or open any part file
                
    3. To launch VB application, go to Start->All Applications-> Sample VB Application. This will create "Sample VB" menu next to Help.
        
    4. Click on the different buttons under the menu "Sample VB" to verify the callbacks associated with the button names.
		
    5. To launch C Sharp application, go to Start->All Applications-> Sample C Sharp Application. This will create "Sample C Sharp" menu next to Help.
        
    6. Click on the different buttons under the menu "Sample C Sharp" to verify the callbacks associated with the button names.
	       
-----
Note:
-----
    1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
       For more details on signing the application refer to NXOpen Programmer's Guide."
    
    2. User will require a .NET authoring license to run the example. See the online documentation for details of licensing.
  
  '=================================End=========================================
