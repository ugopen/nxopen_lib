'=============================================================================
'
'                   Copyright (c) 2017 Siemens PLM Solutions
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

    1. SelectionSubscriberExample.cs

The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/SelectionSubscriberExample.

-----------
Build Steps
-----------

   Windows
   -------
   For C#:
   1. Open Microsoft Visual Studio 

   2. Create a new VC# project using the NX Open AppWizard
      Create new project as:

        2.1 File->New->Project.

        2.2 Select VC# Project using the NX Open AppWizard, Class Library Application,
            Enter name as SelectionSubscriberExample. Click Next.

        2.3 Under Application Settings, select 'An Internal application that can be
            activated from an NX session (DLL)'.

        2.4 Select to activate the application explicitly and to unload the
            application when NX session terminates. Click Finish.

    3. Remove all *.cs files from created project by clicking MB3 on the respective files
       and clicking 'Delete' on the pop-up menu. You will receive a pop-up that says it will be
       deleted permanently. Click OK.

    4. Add the SelectionSubscriberExample.cs to the project by selecting the Project
       pull down and select "Add Existing Item...". Select the file using the popup window.

    5. Confirm following four references are added into this project:

          $UGII_BASE_DIR\nxbin\managed\NXOpen.dll
          $UGII_BASE_DIR\nxbin\managed\NXOpen.UF.dll
          $UGII_BASE_DIR\nxbin\managed\NXOpen.Utilities.dll
          $UGII_BASE_DIR\nxbin\managed\NXOpenUI.dll

       Confirm the version of target framework is .NET Framework 4:

          Right-click this project in the Solution Explorer and select Properties on the popup menu.
          Select .NET Framework 4 for Target framework on the Application tab page.

       Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

    This will create an executable called SelectionSubscriberExample.dll in the Debug directory.

Linux
-------
    -N/A-

----------------------------
Settings before Launching NX
----------------------------
    None

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

    4. Invoke SelectionSubscriberExample.dll file using  File->Execute->NX Open... menu command.

    5. Observe the output to the Listing Window.

    6. Perform any normal NX interaction involving entering and exiting commands, and selecting and deselecting objects.
       Observe that all such activity is reported to the SelectionSubscriber, as indicated by the output to the Listing Window.

-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	   
