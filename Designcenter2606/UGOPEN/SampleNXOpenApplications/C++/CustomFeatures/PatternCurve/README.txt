-------------------------------------------------------------------------------


          Copyright 2026 Siemens Industry Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Demonstration example for custom feature Pattern Curve.
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates how a Custom feature "Pattern Curve" can be implemented.

------------
Build Steps
------------
The custom feature consists of two parts: Core and UI. Both parts must be built separately.

Build instructions for each part are provided in the following locations:
    $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CustomFeatures/PatternCurve/PatternCurveCore/README.txt
    $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CustomFeatures/PatternCurve/PatternCurveUI/README.txt

After completing these steps, you should have the following libraries ready to be executed in NX:
    - PatternCurveCore.dll and PatternCurveUI.dll

----------------------------
Settings before Launching NX
---------------------------- 
The executables PatternCurveCore.dll and PatternCurveUI.dll along with files CustomFeatureConfiguration.xml and PatternCurveUI.dlx, must be placed in one of the following locations:

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

    3. Launch the dialog by invoking PatternCurveUI.dll library through File->Execute->NX Open or Ctrl+U.
    
    4. This will launch the "Pattern Curve" dialog.

    5. Provide inputs as indicated in dialog.
        - Select a curve to pattern.
        - Provide valid number of count (minimum 2) and pitch distance for the pattern.

    6. Dialog OK/Apply creates the Pattern Curve.
	
	7. Newly created Pattern Curve feature can be edited by RMB on Part Navigator feature node and choosing Edit with Rollback.
	
	8. Editing feature will launch the same dialog populated using edited feature parameters.
            
-----
Note:
-----
 "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
