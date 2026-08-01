'==================================================================================
'
'       Copyright (c) 2018 Siemens Product Lifecycle Management Software Inc.
'                            All Rights Reserved.
'
'===================================================================================
'    

------------------------------------------------------------------------------------
                        ValidateNXOpenSetup.cpp Example
------------------------------------------------------------------------------------

-----------
Description
-----------

    This example first obtains a Session object and with the help of Session object, 
    it creates a system log file and reads the environment variable to get the full 
    version number of the installed Siemens NX software. If the Siemens NX software 
    is successfully installed then the application receives the version number and 
    it displays the version number on the listing window as well in the system log 
    file. This is a simple NX Open batch application program and the fact that it 
    runs validates the NX Open software automation setup.

--------------
Files required
--------------

    1. ValidateNXOpenSetup.cpp

------------
Build steps
------------

   Windows
  ---------
   1. Open Microsoft Visual Studio.
   2. Create a new Visual C++ project using the NXOpen C++ Wizard.
   3. Under Application Settings, select 'An external application 
      that runs independent of NX (EXE)'. 
   4. Click on Finish.
   5. Remove the existing C++ file from project.
   6. Add the ValidateNXOpenSetup.cpp to Source Files
      by selecting the Project pulldown and select "Add Existing Item...". 
	  Select the file using the popup window.
   7. Build the external exe by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable exe in the Debug directory.
  
   Linux
   -------
   1. Start up a NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "e" (Link internal/external user function (i/e):)  
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => ValidateNXOpenSetup.
   7. Do not add any subroutines or libraries.
       
   This will create ValidateNXOpenSetup.so in the current directory.

   Exit out of ufmenu.
   
----------------------------
Settings before Launching NX
----------------------------
    -NA-

----------------------------
Settings after Launching NX
----------------------------
    -NA-

-----------------------
Example execution steps
-----------------------
    
   Windows
  ---------
    1. Start up a NX command prompt window.
    
    2. Run the executable exe created from above Build steps.
    
	
   Linux
   -------	
    1. Start up a NX command prompt window.
    
    2. Type command ./ValidateNXOpenSetup
	
------
Notes
------
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

