-------------------------------------------------------------------------------


          Copyright 2016 Siemens Industry Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Demonstration example for custom feature Composite Curve.
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates how a Custom feature UI for "Composite Curve" can be implemented.

--------------
Files required
--------------    
	1. CompositeCurveUI.py
	2. CompositeCurveUI.dlx	
    3. README.txt
	
 The above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/Python/CustomFeatures/CompositeCurve/CompositeCurveUI.

----------------------------
Settings before Launching NX
---------------------------- 
The CompositeCurveUI.py and CompositeCurveUI.dlx must be placed in any one of the following locations mentioned below:

    1.    $UGII_USER_DIR/application
    2.    For released applications, using the environment variable UGII_CUSTOM_DIRECTORY_FILE is highly recommended. 
        This variable is set to a full directory path to a file containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

----------------------------
Settings after Launching NX
----------------------------

    None.    
  
-----------------------
Example execution steps
-----------------------

    1. Start NX.

    2. Open any part file. 

    3. Launch the dialog by creating a shared Library and invoking it through File->Execute->NX Open Menu.
    
    4. This will launch the "Composite Curve" dialog.

    5. Provide inputs as indicated in dialog.

    6. Dialog OK/Apply creates the Composite Curve feature.
	
	7. Newly created Composite Curve feature can be edited by RMB on Part Navigator feature node and choosing Edit with Rollback
	
	8. Editing feature will launch the same dialog populated with using edited feature.
