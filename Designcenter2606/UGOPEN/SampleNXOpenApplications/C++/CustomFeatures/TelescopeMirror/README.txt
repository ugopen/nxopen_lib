-------------------------------------------------------------------------------


          Copyright 2026 Siemens Industry Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Demonstration example for custom feature Telescope Mirror.
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates how a Custom feature "Telescope Mirror" can be implemented.

------------
Build Steps
------------
This custom feature example consists of four parts: three Core libraries and one UI library. All parts must be built separately.

Build instructions for each part are provided in the following locations:
    $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CustomFeatures/TelescopeMirror/TelescopeMirrorCore/README.txt
    $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CustomFeatures/TelescopeMirror/TelescopeMirrorShapeGeneratorCore/README.txt
    $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CustomFeatures/TelescopeMirror/TelescopeMirrorReflectorCurveGeneratorCore/README.txt
    $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CustomFeatures/TelescopeMirror/TelescopeMirrorUI/README.txt

After completing these steps, you should have the following libraries ready to be executed in NX:
    - TelescopeMirrorCore.dll, TelescopeMirrorUI.dll, TelescopeMirrorShapeGeneratorCore.dll and TelescopeMirrorReflectorCurveGeneratorCore.dll

----------------------------
Settings before Launching NX
---------------------------- 
The executables TelescopeMirrorCore.dll, TelescopeMirrorUI.dll, TelescopeMirrorShapeGeneratorCore.dll and TelescopeMirrorReflectorCurveGeneratorCore.dll  along with files TelescopeMirror/CustomFeatureConfiguration.xml, TelescopeMirrorShapeGeneratorCore/CustomFeatureConfiguration.xml, TelescopeMirrorReflectorCurveGeneratorCore/CustomFeatureConfiguration.xml and TelescopeMirrorUI/TelescopeMirrorUI.dlx, must be placed in one of the following locations:

For this example, where multiple CustomFeatureConfiguration.xml files are used, each configuration XML file should be placed in its respective subfolder under the application folder. These subfolders should be specified as an entry in UGII_CUSTOM_DIRECTORY_FILE.

    1.    $UGII_USER_DIR/application
    2.    For released applications, using the environment variable UGII_CUSTOM_DIRECTORY_FILE is highly recommended. 
        This variable is set to a full directory path to a file containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

Note: The entry in UGII_CUSTOM_DIRECTORY_FILE should specify the parent directory of the application folder where the executables and other files are placed. For example, if the executables and files are located in <user_custom_dir>\application, then the entry in UGII_CUSTOM_DIRECTORY_FILE should be <user_custom_dir>.
    
----------------------------
Settings after Launching NX
----------------------------

    None.    
  
-----------------------
Example execution steps
-----------------------
    1. Start NX.

    2. Open any part file.

    3. Launch the dialog by invoking TelescopeMirrorUI.dll library through File->Execute->NX Open or Ctrl+U.
    
    4. This will launch the "Telescope Mirror" dialog.

    5. Provide inputs as indicated in dialog.
       - For Base Reflector:
        - Select a point at origin (0.0, 0.0, 0.0) for the reflector.
        - Provide valid diameter (3000 mm), radius of curvature (2000 mmm) and conic constant (0) and thickness at centre (100 mm).

       - For Aperature:
        - Select a apprpriate shape for the aperature.
        - Insert valid primary length (200 mm) and secondary length (200 mm) for the aperature.
        - Insert valid offset values for the aperature (primary offset: 100 mm, secondary offset: 100 mm).

    6. Dialog OK/Apply creates the Telescope Mirror.
	
	7. Newly created Telescope Mirror feature can be edited by RMB on Part Navigator feature node and choosing Edit with Rollback.
	
	8. Editing feature will launch the same dialog populated using edited feature parameters.
            
-----
Note:
-----
 "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
