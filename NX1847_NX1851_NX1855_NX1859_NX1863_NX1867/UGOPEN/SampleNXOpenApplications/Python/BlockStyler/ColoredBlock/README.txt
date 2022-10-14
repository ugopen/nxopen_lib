-------------------------------------------------------------------------------

       Copyright 2014 Siemens Product Lifecycle Management Software Inc. 
                           All Rights Reserved.

   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Block Styler Colored Block NX Open Python Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates creation of a colored block using the Block Styler Python APIs. 
The set of APIs designed for Block Styler application are property based. While using 
these APIs one must be aware about the Block, its associated properties and their data type.
Executing this example will launch a dialog which allows you to pick the point and 
color to create a block.

--------------
Files required
--------------

    1.  ColoredBlock.py 
    2.  ColoredBlock.dlx (This file is located at 
        $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/ColoredBlock) 
	
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

    1. Change the Role to Advanced.

--------------------------
Example execution steps
--------------------------

    1. Using Tools->Journal->Play
   
        1.1 Start NX.
  
        1.2 Create new part.
        
        1.3 Invoke ColoredBlock.py file using Tools->Journal->Play (Alt+F8).
        
        1.4 It will launch the New ColoredBlock dialog; 
            Enter the values for the height, width, length of the block. 
            Specify the block origin and color of the block.
	        It will create the new ColoredBlock at the specified location.
	
