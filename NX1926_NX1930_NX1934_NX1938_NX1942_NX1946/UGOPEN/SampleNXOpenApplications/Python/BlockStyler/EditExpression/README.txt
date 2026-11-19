-------------------------------------------------------------------------------

          Copyright 2014 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.


-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
		         Block Styler EditExpression Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates editing an expression of a feature.

--------------
Files required
--------------

    1. EditExpression.py
    2. EditExpression.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression) 
    3. FeatureSeed.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression)
    4. EditExpression.prt(This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression)
    
      
----------------------------
Settings before Launching NX
----------------------------
The dlx(s) files must be placed in one of the following locations:
	 1. From where the NX session is launched
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

    2. Open EditExpression.prt file

    3. Launch the dialog by using the following method:

       3.1 Using Tools->Journal->Play 
             - Invoke EditExpression.py file using Tools->Journal->Play (Alt+F8).

    4. Select a feature. The selected feature will be listed in list below. (You can add more 
       than one features in the list by clicking “Add New Set” button and then moving the focus 
       to the selection block and selecting the new feature. The list-items can be manipulated 
       using the 3 buttons provided on the right side of the list-block)

    5. Select the feature for which you want to edit an expression and click on button “Get Expressions”

    6. Select an expression which you want to edit in the list box. The expression name and 
       its value will get reflected in fields at the bottom of dialog. Enter a new value in the 
       ‘Value’ field and hit “Apply”/“OK”.
       
