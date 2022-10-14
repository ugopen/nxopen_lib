===============================================================================
'
'       Copyright 2010 Siemens Product Lifecycle Management Software Inc.
'                           All Rights Reserved.
'
'  
'=================================================================================

----------------------------------------------------------------------------------
        		            MenuBarCppApp Example
----------------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates how a custom application is added to NX. It defines menubar applications with callbacks for C++ and adds the applications to the start menu.  

--------------
Files required
--------------

    1. MenuBarCppApp.cpp
    2. MenuBarCppApp.h
    3. MenuBarCppApp.men
	4. MenuBarCppAppButton.men
	
The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/MenuBarCppApp.


-----------
Build Steps
-----------

   Windows
   -------
   1. Using Visual studio - create a new project using the NXOpen AppWizard.
      This is described in the Automation -> NXOpen -> Open for C/C++ -> 
	  Open C Reference Guide -> Overview -> Setting up your system -> Windows operating system setup. 
      When setting the Application Settings, select "Create an Internal application" 
      and select C++ as the language. 
   2. Remove all the existing files from project.
   3. Add the MenuBarCppApp.cpp, MenuBarCppApp.h to Source Files and Header files respectively 
      by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.
   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
   This will create an executable called MenuBarCppApp.dll and MenuBarCppApp.lib  in the 'Debug' directory.
 
 The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp MenuBarCppApp.cpp
      uflink UFDLL=MenuBarCppApp.dll

   This will create MenuBarCppApp.dll and MenuBarCppApp.lib in the current directory.

   Linux
   -----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select "y" for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => MenuBarCppApp
   7. Do not add any subroutines or libraries.
       
   This will create MenuBarCppApp.so and MenuBarCppApp.o in the current directory.

   Exit out of ufmenu.


----------------------------
Settings before Launching NX
----------------------------
   1. Create the below folder structure in any of the system drives and place the following files:
		+ MenuBarCppApp
			+ application
				a. MenuBarCppApp.men
				b. MenuBarCppApp.dll on Windows or MenuBarCppApp.so on Linux (This file is obtained from the build steps) 
				c. MenuBarCppApp.lib on windows or MenuBarCppApp.o on Linux (This file is obtained from the build steps)
			+ startup
				a. MenuBarCppAppButton.men
	
   2.	Set the varaible UGII_USER_DIR pointing to the directory MenuBarCppApp location in NX command prompt.
        For ex: if MenuBarCppApp is created in the location D:\MenuBarCppApp then the setting should be "set UGII_USER_DIR = D:\MenuBarCppApp" on Windows.
		On Linux, the variable  should be "export UGII_USER_DIR = /D/MenuBarCppApp"

----------------------------
Settings after Launching NX
----------------------------
   1. Change the Role to Advanced if not set.
	
-----------------------
Example execution steps
-----------------------
    
        1. Start NX.
        
        2. Create a new part or open any part file
                
        3. To launch Sample CPP application, go to Start->All Applications-> Sample CPP Application. This will create "Sample CPP" menu next to Help.
        
        4. Click on the different buttons under the menu "Sample CPP" to verify the callbacks associated with the button names.
				 
-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
	
