'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================
------------------------------------------------------------------------------
			Preferences User Example
------------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates changing Sketch and work plane Preferences through NXOpen.


--------------
Files required
--------------

    1. Preferences.cpp


The above listed file is located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/Preferences.

-----------
Build Steps
-----------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NXOpen AppWizard.
      This is described in the Automation -> NXOpen -> Open for C/C++ -> 
	  Open C Reference Guide -> Overview -> Setting up your system -> Windows Operating System Setup. 
      When setting the Application Settings, select "Create an Internal application" 
      and select C++ as the language. 

   2. Remove all the existing files from project.
   
   3. Add the Preferences.cpp to Source Files
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called Preferences.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp Preferences.cpp
      uflink UFDLL=Preferences.dll

   This will create Preferences.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => Selection
   7. Do not add any subroutines or libraries.
       
   This will create Preferences.so in the current directory.

   Exit out of ufmenu.

----------------------------
Settings before Launching NX
----------------------------
-NA-

----------------------------
Settings after Launching NX
----------------------------
   1. Change the Role to Advanced if not set.

-----------------------
Example execution steps
-----------------------
    1. Start NX.
       
    2. Invoke Preferences.dll (Preferences.so on Linux) file using  File->Execute->NX Open... menu command.

    3. This will create a Prefernces.prt and displays it and then default preferences of sketch,Work plane 
       and grid properties will be changed

    4. To verify the same follow these below steps
	
	4.1 First enter into Modeling application through Start->All Applications->Modeling...
	
	4.2 Go to Preferences-> Sketch
	   
	    In the Name Prefixes group following values should be set
	   
	    Sketch:  SKT_	   
	    Vertex:  VRT_
	    Line:    LIN_
	    Arc:     ARC_
	    Conic:   CON_
	    Spline:  SPL_
	  
	    Then close the dialog.
	
	4.3 Now go to Preferences-> Grid and Work Plane...
	
	    The work plane grid type is changed from rectangular to polar.
		
	    Also, the following spacing preferences for grid lines are set:

	    Radial Spacing
	    Major Grid Spacing:		75.0
	    Minor Lines per Major:	3
	    Snap Points per Minor:	5

	    Angular Spacing
	    Major Grid Spacing:		45.0
	    Minor Lines per Major:	4		
	    Snap Points per Minor:	2

-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	  
