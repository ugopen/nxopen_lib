'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

-----------------------------------------------------------------------------
                               PMI Example
-----------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates the creation of a PMI dimension.

--------------
Files required
--------------

    1. PMIExample.cpp
    2. PMIExample_cylinder.prt

The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/PMIExample.


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
   
   3. Add the PMIExample.cpp to Source Files
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called PMIExample.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp PMIExample.cpp
      uflink UFDLL=PMIExample.dll

   This will create PMIExample.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select "y" for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => PMIExample
   7. Do not add any subroutines or libraries.
       
   This will create PMIExample.so in the current directory.

   Exit out of ufmenu.

----------------------------
Settings before Launching NX
----------------------------
-NA-

----------------------------
Settings after Launching NX
----------------------------
   1. Change the Role to Advanced with full menus if not set.


-----------------------
Example execution steps
-----------------------
    1. Start NX.

    2. Open the part PMIExample_cylinder.prt

    3. Enter into Modeling application through Start->All Applications->Modeling...
    
    4. Invoke PMIExample.dll (PMIExample.so on Linux) file using  File->Execute->NX Open... menu command.

    5. This will create a dimension on the cylinder in the 3D Model.

    6. Now enter into Drafting application through Start->All Applications-Drafting...

    7. Again invoke PMIExample.dll (PMIExample.so on Linux) file using  File->Execute->NX Open... menu command.

    8. Then a dimension will be created in the drafting view.

-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	  





