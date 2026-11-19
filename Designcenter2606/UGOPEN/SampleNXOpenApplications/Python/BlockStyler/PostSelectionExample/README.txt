------------------------------------------------------------------------------

    Copyright 2014 Siemens Product Lifecycle Management Software Inc. 
                           All Rights Reserved.


------------------------------------------------------------------------------



------------------------------------------------------------------------------
                   Block Styler Post Selection Example
------------------------------------------------------------------------------

-----------
Description
-----------
The example shows two selection blocks used to select post nodes and post elements.
It also includes post group creation code for both of blocks.

--------------
Files required
--------------
1.  PostSelectionExample.py 
2.  PostSelectionExample.dlx (This file is located at 
    $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/Python/BlockStyler/PostSelectionExample)

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
	
    2.  Open a solved simulation file, load the result, and plot a contour result in the post view.
	
    3.  Execute the Python journal using the command Tools->Journal->Play  

        - Invoke PostSelectionExample.py file using Tools->Journal->Play (Alt+F8).

    4.  It will launch the "Post selection example" dialog. 

    5.  Select one or more Post Nodes or enter the desired post node labels.

    6.  Select one or more Post Elements or enter the desired post element labels.

    7.  Click on OK or Apply for your selected nodes/elements to new post group, if the group name or label is duplicate, an error will occur.
        In that case, either change the group name and label or delete the existing group.

