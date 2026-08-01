'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================


-----------------------------------------------------------------------------
                             QuickExtrude Example
-----------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates the process of modifying a journal to work generically on
part files.  The original journal was the result of recording the extrude of the 
circle sketch on the block face and accepting the default extrude options.  Selection
code was added to allow selection of a sketch rather than using the circle sketch.  
Code was also added to allow the input of the start and end limits of the extrude
rather than using the defaults. 

Comments were added in the QuickExtrude.cpp  file to indicate where code was added.
Added code is enclosed in between the following comment lines:

//**** Added Code *****
//^^^^^^^^^^^^^^^^^^^^^

--------------
Files required
--------------

    1. QuickExtrude.cpp
    2. QuickExtrude_block_sketch.prt

The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/QuickExtrude.

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
   
   3. Add the QuickExtrude.cpp to Source Files
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called QuickExtrude.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp QuickExtrude.cpp
      uflink UFDLL=QuickExtrude.dll

   This will create QuickExtrude.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select "y" for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => QuickExtrude
   7. Do not add any subroutines or libraries.
       
   This will create QuickExtrude.so in the current directory.

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

    2. Open the part QuickExtrude_block_sketch.prt

    3. Enter into Modeling application through Start->All Applications->Modeling...
    
    4. Invoke QuickExtrude.dll (QuickExtrude.so on Linux) file using  File->Execute->NX Open... menu command.

    5. It will prompt for a sketch to be selected - Select a sketch and hit OK.

    6. It will prompt for a start limit and an end limit - Enter a value if desired and hit OK.

    7. The selected sketch will be then extruded with the given limits.

    8. The process can be repeated for the remaining other two sketches in the part.
	
-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	  
