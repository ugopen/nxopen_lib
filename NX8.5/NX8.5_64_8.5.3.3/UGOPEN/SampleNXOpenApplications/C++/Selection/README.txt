'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

-------------------------------------------------------------------------------
        		Selection Example
-------------------------------------------------------------------------------


-------------------
Example Description
-------------------
This example demonstrates alternatives to the code recorded while performing a
'Select All' using various filtering methods before an operation.  The example
shows how filtering by type, detailed type, layers, display attributes and color
can be accomplished via automation. The example gets the datums on the work part
that satisfy the filtering criteria and blanks the datums.


--------------
Files required
--------------

    1. Selection.cpp
    2. Selection_datums.prt

The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/Selection.

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
   
   3. Add the Selection.cpp to Source Files
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called Selection.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp Selection.cpp
      uflink UFDLL=Selection.dll

   This will create Selection.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select �y� for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => Selection.
   7. Do not add any subroutines or libraries.
       
   This will create Selection.so in the current directory.

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

    2. Open the part Selection_datums.prt.
       
    3. Invoke Selection.dll (Selection.so on linux) file using  File->Execute->NX Open... menu command.

    4. This will start blanking datums and a message will be popped to the user after every blank operation.

    5. Finally verify the messages by blanking the datums manually after complete execution of the program.

-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	   
