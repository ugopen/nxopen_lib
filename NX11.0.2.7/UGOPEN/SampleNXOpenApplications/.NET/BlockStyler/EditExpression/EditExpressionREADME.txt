-------------------------------------------------------------------------------

              Copyright (c) 2010  Siemens PLM Software
                Unpublished - All rights reserved

'  
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

    1. EditExpression.vb
    2. EditExpression.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression) 
    3. FeatureSeed.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression)
    4. EditExpression.prt(This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/EditExpression)
    
                
-----------
Build Steps
-----------

Windows
-------
    1. Open Microsoft Visual Studio .Net.

    2. Create a new Vb project using the NX Open AppWizard. 
       Create new project as:
          2.1 File->New->Project.
 	      2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as EditExpression. Click Next
          2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
          2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

    3. Remove all *.vb files from created project by clicking MB3 on respective file and 
       clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
    4. Add the EditExpression.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
       the popup window.

    5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

    This will create an executable called EditExpression.dll in the Debug directory.
       
Linux
-------
   -NA-          
      
----------------------------
Settings before Launching NX
----------------------------
The dlx(s) files must be placed in one of the following locations:
	 1. From where NX session is launched
	 2. $UGII_USER_DIR/application
	 3. For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
	    recommended. This variable is set to a full directory path to a file 
	    containing a list of root directories for all custom applications.
	    e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
	    
	    
----------------------------
Settings after Launching NX
----------------------------

1. Change the Role to Advanced if not set.	    

-----------------------
Example execution steps
-----------------------

    1. Start NX.

    2. Open EditExpression.prt file

    3. Launch the dialog by using any one of the methods mentioned below:

       3.1 Using Tools->Journal->Play 
             - Invoke EditExpression.vb file using Tools->Journal->Play (Alt+F8).
             
       3.2 By creating Shared Library and invoke EditExpression.dll through File->Execute->NX Open Menu (Ctrl+U).

    4. Select a feature. The selected feature will be listed in list below. (You can add more 
       than one features in the list by clicking “Add New Set” button and then moving the focus 
       to the selection block and selecting the new feature. The list-items can be manipulated 
       using the 3 buttons provided on the right side of the list-block)

    5. Select the feature for which you want to edit an expression and click on button “Get Expressions”

    6. Select an expression which you want to edit in the list box. The expression name and 
       its value will get reflected in fields at the bottom of dialog. Enter a new value in the 
       ‘Value’ field and hit “Apply”/“OK”.
       
-----
Note:
-----

"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
