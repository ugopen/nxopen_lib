'=============================================================================
'
'                   Copyright (c) 2016 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

-------------------------------------------------------------------------------
        		Selection Subscriber Example
-------------------------------------------------------------------------------


-------------------
Example Description
-------------------
This example instantiates a SelectionSubscriber that is left loaded until the
session terminates. A subsequent execution of the dll will delete and recreate
the SelectionSubscriber.

Anytime the set of selected objects changes due to any user interaction, the
SelectionSubscriber will print the current set of selected tags out to the Listing Window.

The dll may be executed while in Global Selection, or while in a command. It may be
executed with or without objects already selected.


--------------
Files required
--------------

    1. SelectionSubscriber.cpp

The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/CPP/SelectionSubsriber.

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
   
   3. Add the SelectionSubsriber.cpp to Source Files
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called SelectionSubsriber.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp SelectionSubsriber.cpp
      uflink UFDLL=SelectionSubsriber.dll

   This will create SelectionSubsriber.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select "y" for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => SelectionSubsriber.
   7. Do not add any subroutines or libraries.
       
   This will create SelectionSubscriber.so in the current directory.

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

    2. Open any part.

    3. Select a few objects.

    4. Invoke SelectionSubscriber.dll (SelectionSubscriber.so on linux) file using  File->Execute->NX Open... menu command.

    5. Observe the output to the Listing Window.

    6. Perform any normal NX interaction involving entering and exiting commands, and selecting and deselecting objects.
       Observe that all such activity is reported to the SelectionSubscriber, as indicated by the output to the Listing Window.

-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	   
