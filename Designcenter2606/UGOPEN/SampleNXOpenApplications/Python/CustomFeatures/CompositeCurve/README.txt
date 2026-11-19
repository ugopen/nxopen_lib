-------------------------------------------------------------------------------


          Copyright 2026 Siemens Industry Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Demonstration example for custom feature Composite Curve.
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates how a Custom feature for "Composite Curve" can be implemented.

--------------
Files required
--------------    
	1. CompositeCurveUI.py
	2. CompositeCurveUI.dlx
    3. CompositeCurveCore.py
	4. CustomFeatureConfiguration.xml
	
 The above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/Python/CustomFeatures/CompositeCurve/CompositeCurveUI and
 $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/Python/CustomFeatures/CompositeCurve/CompositeCurveCore.

----------------------------
Settings before Launching NX
---------------------------- 
The files must be placed in one of the following locations mentioned below:

    1.    $UGII_USER_DIR/application
    2.    The environment variable UGII_CUSTOM_DIRECTORY_FILE must be set to a full directory path to a file containing a list of root directories 
          for all custom applications. e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

Note: The entry in UGII_CUSTOM_DIRECTORY_FILE should specify the parent directory of the application folder where the files are placed. For example, if the files are located in <user_custom_dir>\application, then the entry in UGII_CUSTOM_DIRECTORY_FILE should be <user_custom_dir>.
 
----------------------------
Settings after Launching NX
----------------------------

    None.    
  
-----------------------
Example execution steps
-----------------------

    1. Start NX.

    2. Open any part file. 

    3. Launch the dialog by executing CompositeCurveUI.py through Tools->Journal->Play Menu.
    
    4. This will launch the "Composite Curve" dialog.

    5. Provide inputs as indicated in dialog.

    6. Dialog OK/Apply creates the Composite Curve feature.
	
	7. Newly created Composite Curve feature can be edited by RMB on Part Navigator feature node and choosing Edit with Rollback
	
	8. Editing feature will launch the same dialog populated using edited feature parameters.
