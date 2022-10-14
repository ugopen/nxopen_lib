-------------------------------------------------------------------------------


          Copyright 2011 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
	Block Styler demonstration example for User Defined UI Block (UDB)
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates how a UDB is created and used in the dialog. UDB, which itself is a set of blocks, can be thought 
as a block with behavior defined in automation code.

UDB Creation:
 DimensionUDB UDB is created in Block Styler Application. The generated files are DimensionUDB.dlx,
 DimensionUDB.vb and DimensionUDB.udx. Dlx file defines the UDB, vb file defines the behavior/implementation
 details of UDB, and udx file defines the catalog entry of UDB on block palette. 

UDB Usage in dialog:
 In order to put UDB in dialog, the udx and dlx file should be available in user directory. Udx file is responsible for
 putting the UDB on block palette under the category as defined by udx file itself. For this example the udx defines the 
 category as "Dimension" and block name as "DimensionUDB". Like other standard block, UDB can be put on dialog by clicking 
 its entry on block palette.

UDB Implementation:
 DimensionUDB.vb file defines the behavior of the UDB. It has following elements:
 - Two blocks are defined - Toggle and Double block
 - If Toggle is set to true then Double block is disabled. Refer to dialogShown_cb and update_cb.
 - Double block defines default values using combo selection
 - If Double block has value set to zero then OK/Apply of parent dialog is disabled. Refer to enableOKButton_cb.
 - Has property defined to set and get the value of Double block
 - Has function to set the label of the Double block

Dialog:
 Dialog CreateCylinder_UsingUDB contains two instances of DimensionUDB to accept the height and diameter value respectively. The other blocks 
 dialog contains are Point and Vector block. The dialog file CreateCylinder_UsingUDB.dlx has implementation defined in CreateCylinder_UsingUDB.vb.
 This dialog simply uses the vector, origin point, height (UDB) and diameter (UDB) to create the cylinder on dialog OK/Apply.

--------------
Files required
--------------

    1. CreateCylinder_UsingUDB.vb
    2. CreateCylinder_UsingUDB.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/UDB_CreateCylinder)
    3. DimensionUDB.vb
    4. DimensionUDB.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/UDB_CreateCylinder)
    5. DimensionUDB.udx (Required only in the case of new dialog creation when UDB available on palette is selected to put the UDB in dialog)
                        (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/UDB_CreateCylinder)

-----------
Build Steps
-----------   
    
 Windows
 -------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as CreateCylinder_UsingUDB. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on popup menu.You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the CreateCylinder_UsingUDB.vb and DimensionUDB.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.
        
5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an shared library CreateCylinder_UsingUDB.dll in the Debug directory.
    
Linux
-----
Not applicable

----------------------------
Settings before Launching NX
----------------------------

The dlx files must be placed in one of the following locations:
    1. From where NX session is launched
    2. $UGII_USER_DIR/application
    3. For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat


----------------------------
Settings after Launching NX
----------------------------

    1. Change the Role to Advanced.
                        
-----------------------
Example execution steps
-----------------------

    1. Start NX.

    2. Open any part file. 

    3. Launch the dialog by creating a shared Library and invoking it through File->Execute->NX Open Menu.
    
    4. This will launch the “Create Cylinder Using UDB” dialog. The blocks with label "Diameter" and "Height" are instances of UDB.

    5. Provide Point and Vector. The Diameter and Height will have default value. The value may be set using the combo options.

    6. Notice that entering zero disables the OK/Apply button of dialog, and toggling on disables the double-field. This 
       behavior is as per the implementation in DimensionUDB.cpp.

    7. Dialog OK/Apply creates the cylinder. Next dialog launch shows the diameter and height value from dialog memory.
    
    
-----
Note:
-----
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
    

