'=============================================================================
'
'                   Copyright (c) 2016 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

-----------------------------------------------------------------------------
                               CreatePreview
-----------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates the creation of fitted model view previews for disclosed modeling views.

--------------
Files required
--------------

    1. CreatePreview.cpp
	The above file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CreatePreview
	
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
   
   3. Add the CreatePreview.cpp to Source Files
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called CreatePreview.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp CreatePreview.cpp
      uflink UFDLL=CreatePreview.dll

   This will create CreatePreview.dll in the current directory.
   
   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select "y" for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => CreatePreview
   7. Do not add any subroutines or libraries.
       
   This will create CreatePreview.so in the current directory.

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

    2. Open a part or assembly.

    3. Invoke CreatePreview.dll (CreatePreview.so on Linux) file using  File->Execute->NX Open... menu command.
    
    4. Invoke PMIExample.dll (PMIExample.so on Linux) file using  File->Execute->NX Open... menu command.

    5. For each part, the following will be performed:
	
		4.1 Looks through all views and gathers the modeling views that are disclosed.
		4.2 Checks each disclosed modeling view to see if it has a preview.
		4.3 If the disclosed modeling view does not have a preview, a fitted preview will be created for that view.
		4.4 The syslog will have a list of all disclosed modeling views that had previews created. 
		4.5 Checks again to see if any disclosed modeling view still does not have a preview.
		4.6 If any exists, the syslog will have a list of all disclosed modeling views that failed to have previews created.
		
-----
Note:
-----
	"NXOpen application must be signed before its release. If not signed the application may not get executed.
	For more details on signing the application refer to NXOpen Programmer's Guide."	  
