'=============================================================================
'
'         Copyright 2012 Siemens Product Lifecycle Management Software Inc.
'                           All Rights Reserved.
'
'  
'===================================================================================

------------------------------------------------------------------------------------
                        ConfigureContextMenu  Example
------------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates how to customize context menus in NX. It defines basic 
functionality for making changes to context menu options for both the C Sharp and 
VB.Net languages.

--------------
Files required
--------------

    1. ConfigureContextMenu.cs
    2. ConfigureContextMenu.vb

The above listed files are located at
$UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\ConfigureContextMenu
    
-----------
Build Steps
-----------

Windows
-------
For VB.Net:-

1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
        2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as ConfigureContextMenu. Click Next.
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.

4. Add the ConfigureContextMenu.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.

5. Add the following references,
     5.1. NXOpen.dll 
     5.2. NXOpenUI.dll 
     5.3. NXOpen.Utilities.dll
     5.4. NXOpen.UF.dll.

   To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
   Go to %UGII_BASE_DIR%\nxbin\managed.  Select and add the DLL's one after the other.

6. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called ConfigureContextMenu.dll in the Debug directory.

For C Sharp:-

1. Open Microsoft Visual Studio .Net.

2. Create a new VC# project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
        2.2 Select VC# Project using the NX Open AppWizard, Class Library Application, Enter name as ConfigureContextMenu. Click Next.
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.cs files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.

4. Add the ConfigureContextMenu.cs to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.

5. Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
   To do this, right click on "References" under the Assembly Viewer project in Solution Explorer. 
   Pick "Add Reference..." and then navigate to the location of the dlls. 
   These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.

6. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called ConfigureContextMenu.dll in the Debug directory.

Linux
-------
   -N/A-

----------------------------
Settings before Launching NX
----------------------------
   1. Create the below folder Structure in any of the system drives and place the following files:
        + ConfigureContextMenu
            + startup
                a. ConfigureContextMenu.dll (This file is obtained from the build steps For VB.Net or C Sharp)

   2.   Set the variable UGII_USER_DIR pointing to the directory ConfigureContextMenu location in NX command prompt.
        For ex: if ConfigureContextMenu is created in the location D:\ConfigureContextMenu then the setting should be "set UGII_USER_DIR=D:\ConfigureContextMenu"


----------------------------
Settings after Launching NX
----------------------------

None


--------------------------
Example execution steps
--------------------------

        1. Start NX.

        2. Create a new part

        3. Change the Role to Advanced if not set.

        4. Insert a Block, go to Insert->Design Feature->Block. 

        5. Right-click on the Block in the Part Navigator.  Notice that Properties has moved to the top of the context menu and is the default option.

        6. Right-click on the Block in the Graphics Window.  Notice that here the Delete option has been removed.

        7. Insert a Cylinder, go to Insert->Design Feature->Cylinder.

        8. Right-click on the Cylinder in the Graphics Window.  Notice that the submenu "Custom" has been added that includes a Visualization Preferences entry.

-----
Note:
-----
  1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
  2. A .NET authoring license is required to run the example. See the online documentation for details of licensing.
