-------------------------------------------------------------------------------
		Block Styler Edit-Expression Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates editing an expression of a feature.

--------------
Files required
--------------

    1. EditExpression.vb
    2. EditExpression.dlx 
    3. FeatureSeed.dlx

        Above dlx(s) file must be placed in one of the following locations:
	1.) From where NX session is launched
	2.) $UGII_USER_DIR/application
	3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
	    recommended. This variable is set to a full directory path to a file 
	    containing a list of root directories for all custom applications.
	    e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

----------------------
How to run the example
----------------------

    1. Start NX.

    2. Open HoleCoordinates.prt file

    3. Launch the dialog by using any one of the methods mentioned below:

        a. - Using Tools->Journal->Play 
	   - Read the instruction under DIALOG LAUNCHING section of HoleCoordinates.vb
             file in order to understand where to keep the HoleCoordinates.dlx file.
	   - Invoke HoleCoordinates.vb file using Tools->Journal->Play.
        b. By creating Shared Library and invoke it through File->Execute->NX Open Menu.

    4. Select a feature. The selected feature will be listed in list below. (You can add more 
       than one features in the list by clicking “Add New Set” button and then moving the focus 
       to the selection block and selecting the new feature. The list-items can be manipulated 
       using the 3 buttons provided on the right side of the list-block)

    5. Select the feature for which you want to edit an expression and click on button “Get Expressions”

    6. Select an expression which you want to edit in the list box. The expression name and 
       its value will get reflected in fields at the bottom of dialog. Enter a new value in the 
       ‘Value’ field and hit “Apply”/“OK”.

--------------------------
How to Build VB example
--------------------------

    1. Open Microsoft Visual Studio .Net.

    2. Create a new VB project using the NX Open AppWizard. This is described in the 
       NX Open Programmers Guide -> Wizard Setup.
       Also information under Creating NX Open Automation -> Applications will be helpful.
       When setting the Application Settings, select "Create an Internal application"
       and select NXOpen.UI API. 
       Select to activate the application Explicitly and to unload when NX terminates.
       Then pick Finish.

    3. Add the EditExpression.vb to the project by selecting the Project pulldown and select 
       "Add Existing Item...". Select the file using the popup window.

    4. Build the internal image by going to the Build menu and selecting either "Build" or "Rebuild".
       This will create an executable called EditExpression.dll in the Release directory.
-------------------------------------------------------------------------------
