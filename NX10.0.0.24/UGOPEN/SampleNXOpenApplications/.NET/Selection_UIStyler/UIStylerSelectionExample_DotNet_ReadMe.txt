-------------------------------------------------------------------------------
		Selection_UIStyler Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates the Selection capability of NXOpen UIStyler.
Running this example will launch a dialog which creates Edge Blend on the selected edges.

--------------
Files required
--------------
1. UistylerselectionExample.cs Or UistylerselectionExample.vb
2. Block.prt
3. UistylerselectionExample.dlg
	
   The UistylerselectionExample.dlg file must be placed in one of the following locations:
    1.) $UGII_USER_DIR/application
    2.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

----------------------
How to execute the example
----------------------

1. Using Tools->Journal->Play 

	1. Start NX.
	2. Open Block.prt file
	3. Uncomment the function calls for LockAccess and UnlockAccess from source file.
	4. Invoke UistylerselectionExample.cs or UistylerselectionExample.vb file using 
       'Tools->Journal->Play'.
	
2. By creating Shared Library and invoking it through File->Execute->NX Open Menu. 
   
   Once you have successfully finished with "How to Build VB/C# example" steps (mentioned below), 
   follow the steps below:

	1. Start NX.
	2. Open Block.prt file
	3. Invoke Shared Library through  File->Execute->NX Open  Menu.
	
--------------------------
How to Build VB/C# example
--------------------------
1. Open Microsoft Visual Studio .Net.

2. Create a new VB/C# project using the NX Open AppWizard. This is described in the 
   Automation -> NXOpen ->NX Open Programmer's Guide-> Wizard Setup.
   Also information under Creating NX Open Automation -> Applications will be helpful.
   When setting the Application Settings, select "Create an Internal application"
   and select NXOpen.UI API. 
   Select to activate the application Explicitly and to unload when NX terminates.
   Then pick Finish.

3. Remove all .vb or .cs files from created project by clicking MB3 on respetive file and 
   clicking 'Delete' on poped menu.
   
4. Add the UistylerselectionExample.vb (or UistylerselectionExample.cs) to the project by 
   selecting the Project pulldown and select "Add Existing Item...". Select the file using 
   the popup window.

5. Build the internal image by going to the Build menu and selecting either "Build" or "Rebuild".

This will create an shared library <PROJECT NAME>.dll in the Release directory.

