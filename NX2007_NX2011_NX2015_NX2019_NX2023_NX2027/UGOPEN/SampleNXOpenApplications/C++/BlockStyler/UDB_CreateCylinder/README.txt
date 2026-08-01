-------------------------------------------------------------------------------


          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
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
 DimensionUDB.hpp, DimensionUDB.cpp and DimensionUDB.udx. Dlx file defines the UDB, hpp/cpp file defines 
 the behavior/implementation details of UDB, and udx file defines the catalog entry of UDB on block palette. 

UDB Usage in dialog:
 In order to put UDB in dialog, the udx and dlx file should be available in user directory. Udx file is responsible for
 putting the UDB on block palette under the category as defined by udx file itself. For this example the udx defines the 
 category as "Dimension" and block name as "DimensionUDB". Like other standard block, UDB can be put on dialog by clicking 
 its entry on block palette.

UDB Implementation:
 DimensionUDB.cpp file defines the behavior of the UDB. It has following elements:
 - Two blocks are defined - Toggle and Double block
 - If Toggle is set to true then Double block is disabled. Refer to dialogShown_cb and update_cb.
 - Double block defines default values using combo selection
 - If Double block has value set to zero then OK/Apply of parent dialog is disabled. Refer to enableOKButton_cb.
 - Has property defined to set and get the value of Double block
 - Has function to set the label of the Double block

Dialog:
 Dialog CreateCylinder_UsingUDB contains two instances of DimensionUDB to accept the height and diameter value respectively. The other blocks 
 dialog contains are Point and Vector block. The dialog file CreateCylinder_UsingUDB.dlx has implementation defined in CreateCylinder_UsingUDB.cpp.
 This dialog simply uses the vector, origin point, height (UDB) and diameter (UDB) to create the cylinder on dialog OK/Apply.

--------------
Files required
--------------
    1. CreateCylinder_UsingUDB.hpp
    2. CreateCylinder_UsingUDB.cpp
    3. CreateCylinder_UsingUDB.dlx 
    4. DimensionUDB.hpp
    5. DimensionUDB.cpp
    6. DimensionUDB.dlx 
    7. DimensionUDB.udx (Required only in the case of new dialog creation when UDB available on palette is selected to put the UDB in dialog)                       
    
 The above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/UDB_CreateCylinder.
 
------------
Build Steps
------------

  Windows
  -------
   1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the Automation -> NX Open -> Open for C/C++ -> 
      Open C Reference Guide -> Overview -> Setting up your system. 
      When setting the Application Settings,
      select "Create an Internal application" and select C++ as the language. 

   2. Remove all the existing files from project.
   
   3. Add the CreateCylinder_UsingUDB.cpp, DimensionUDB.cpp to Source Files and CreateCylinder_UsingUDB.hpp, DimensionUDB.hpp Header Files respectively 
      by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called CreateCylinder_UsingUDB.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
     1. Open an NX command prompt window.
     2. Change directories to the directory containing the source code.
     3. Compile and link using uflink:

    ufcomp CreateCylinder_UsingUDB.cpp DimensionUDB.cpp
      uflink UFDLL=CreateCylinder_UsingUDB.dll DimensionUDB.obj

   This will create CreateCylinder_UsingUDB.dll in the current directory.
   
  Linux
  -----
   Start up an NX command prompt window then start up "ufmenu" ($UGII_BASE_DIR/ugopen/ufmenu)
   Compile and link an internal user function program.  Select "i" when prompted for the 
   type of application to link - internal/external.  Select "y" for linking with user
   interface code.  Also select "n" for Linking a UG/Open++ image.  Select "y" for Link
   a C++ image.

   This will create CreateCylinder_UsingUDB.so.   
   
----------------------------
Settings before Launching NX
---------------------------- 
The dlx file must be placed in any one of the following locations mentioned below:

    1.    The directory from which NX was launched.
    2.    $UGII_USER_DIR/application
    3.    For released applications, using the environment variable UGII_CUSTOM_DIRECTORY_FILE is highly recommended. 
        This variable is set to a full directory path to a file containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
    
----------------------------
Settings after Launching NX
----------------------------

    1.    Change the Role to “Advanced”.        
  
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
