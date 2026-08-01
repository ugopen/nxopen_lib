------------------------------------------------------------------------------

       Copyright 2014 Siemens Product Lifecycle Management Software Inc. 
                           All Rights Reserved.


------------------------------------------------------------------------------



------------------------------------------------------------------------------
                   Block Styler Selection Example
------------------------------------------------------------------------------

-----------
Description
-----------
The example shows two selection blocks used to select edges and features. 
It also includes filter callback code for each block.

--------------
Files required
--------------
1.  SelectionExample.py 
2.  SelectionExample.dlx (This file is located at 
    $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/SelectionExample)

----------------------------
Settings before Launching NX
----------------------------

The dlx file must be placed in one of the following locations:
    1.  From where NX session is launched
    2.  $UGII_USER_DIR/application
    3.  For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat


----------------------------
Settings after Launching NX
----------------------------

1.  Change the Role to Advanced.
            
-----------------------
Example Execution Steps
-----------------------
1. Using Tools->Journal->Play (Alt+F8)

    1.  Start NX.
	
    2.  Create a new part with at least one feature (e.g. Block). 
	
    3.  Execute the Python journal using the command Tools->Journal->Play  

        - Invoke SelectionExample.py file using Tools->Journal->Play (Alt+F8).

    4.  It will launch the "Selection Example" dialog. Select the edges to chamfer, 
        enter the desired chamfer angle, then click on "Apply". NX will create the 
        chamfer on the selected edges with the specified chamfer angle.
	   
    5.  Now click on the "Select chamfer" button and select the chamfer on the 
        feature which you want to remove. Click "OK". NX will remove the selected 
        chamfer features.   
	   
	6.  The following describes the blocks used in this dialog:
	  
        6.1 Edge Select Block – use this selection block to select edges to apply 
            chamfer features to.
        6.2 Face Limit Toggle Block – when this toggle is ON the edges that are selected
            will be limited to just the edges on a single face. Also, when this toggle is
            first turned ON, the edge selection list is cleared.
        6.3 Angle Double Block – the value of this block is used to define the 
            angle of the chamfer features.
        6.4 Feature Select Block – this selection block will select chamfer features 
            to be removed.
        6.5 Angle Limit Toggle – when this toggle is ON the Chamfer features are limited 
            to those that have the angle in the next block. Also, when this toggle is 
            first turned on the selected chamfer features are cleared.
        6.6 Angle Limit Double – when this toggle is ON the value of this block is used 
            to limit chamfer selection to only those of the given angle.
	                  
