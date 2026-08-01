-------------------------------------------------------------------------------

       Copyright 2015 Siemens Product Lifecycle Management Software Inc. 
                           All Rights Reserved.

   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                 Block Styler Missing Welds Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates the block styler wizard. It is used to create a clearance set
on an assembly and determine where the assembly is missing welds. The example also 
demonstrates the task navigator context menu, used to create a report of the missing
welds, or export an image of a missing weld to a pdf.

NOTE: The example is not a comprehensive tool for finding the missing welds and is
solely used for demonstrating the block styler wizard block.

--------------
Files required
--------------

    1. MissingWelds.cs
    2. MissingWelds.dlx
    3. MissingWelds.prt
    4. Plate_2.prt
    5. Plate_3.prt
    6. Plate_7.prt
    7. Plate_8.prt

-----------
Build Steps
-----------

Windows
-------
    1. Open Microsoft Visual Studio .Net.

    2. Create a new C# project using the NX Open AppWizard. 
       Create new project as:
          2.1 File->New->Project.
          2.2 Select C# Project using the NX Open AppWizard, Class Library Application, Enter name as MissingWelds. Click OK
          2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
          2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

    3. Remove all existing files from the created project by clicking MB3 on respective file and 
       clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.

    4. Add the MissingWelds.cs to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
       the popup window.

    5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

    This will create an executable called MissingWelds.dll in the Debug directory.

Linux
-------
   -NA-

----------------------------
Settings before Launching NX
----------------------------
The dlx(s) files must be placed in one of the following locations:
     1. From where NX session is launched

     2. $UGII_USER_DIR/application

     3. For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat


----------------------------
Settings after Launching NX
----------------------------

1. Change a Customer Default by going to:
    
    1.1 File->Utilities->Customer Defaults.

    1.2 Choose Weld Assistant->Continuous Welds from the list on the left of the dialog.

    1.3 Select the 'Groove' tab and choose 'Wave Link Solid Bodies' as the option in 'Assembly Data Linking Method'.

    1.4 Click OK. You must now close NX and reopen it for the change to take place.

2. Change the Role to Advanced if not set.

-----------------------
Example execution steps
-----------------------

    1. Start NX.

    2. Open MissingWelds.prt file

    3. Launch the dialog by using any one of the methods mentioned below:

       3.1 Using Tools->Journal->Play 
             - Invoke MissingWelds.cs file using Tools->Journal->Play (Alt+F8).

       3.2 By creating Shared Library and invoke MissingWelds.dll through File->Execute->NX Open Menu (Ctrl+U).

    4. You will start on the 'Clearance Set' step. Select a set of components to perform a clearance analysis on. The
       selected components will be highlighted. Click 'Next'.

    5. You will now be on the 'Results' step.

        5.1 To return to the 'Clearance Set' step, click 'Back'.

        5.2 A sub node will be created for each missing weld. You can select the sub node by clicking on its name
            'Missing Weld X' where X is the number of the missing weld.

            5.1.1 When you select a sub node, the display will change to show the missing weld. If 'Blank' is selected in
                  the 'Component' enumeration, only the two objects involved in the missing weld will be displayed. If
                  'Highlight' is selected, the entire assembly will be displayed, and the two objects involved in the missing
                  weld will be highlighted. You can switch between 'Blank' and 'Highlight' while a sub node is selected.

            5.1.2 The objects involved in the missing weld will be listed in the list box.

            5.1.3 If you check the check box corresponding to the sub node, the missing weld for the sub node will be
                  included in the report generated by the wizard (see step 5.3). If you uncheck the check box, the
                  missing weld will not be included in the report.

            5.1.4 To export an image of the missing weld to a pdf file, right click on the corresponding sub node to open the
                  sub node context menu, and select 'Export Image to PDF'. If 'Blank' is not selected in the 'Component'
                  enumeration, it will automatically be selected before exporting the image. The pdf file is stored in
                  the same directory as the assembly prt file.

        5.3 To generate a report for the selected missing welds, right click on 'Results' to open the step context menu, and
            select 'Generate Report for Selected Missing Welds'.

        5.4 To close the wizard and keep the clearance set that was created, click 'Finish'. To close without keeping the
            clearance set, click 'Cancel'.

-----
Note:
-----

"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
