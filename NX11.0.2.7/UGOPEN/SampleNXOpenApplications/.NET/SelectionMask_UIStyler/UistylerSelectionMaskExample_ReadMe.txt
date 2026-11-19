-------------------------------------------------------------------------------

        Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                       All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                  		Uistyler Selection Mask Example
-------------------------------------------------------------------------------

------------
Description
------------
This example demonstrates the Selection Masking capability within UIStyler.
Running this example will launch "Move to Layer" dialog which allows the selection of entities and move them from one layer to another layer.
We can check the number of objects in the layers thru the "Layer Setting Information" button.
 
--------------
Files required
--------------
  1.UistylerSelectionMaskExample.vb
  2.UistylerSelectionMaskExample.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/UistylerSelectionMaskExample) 
  3.UistylerSelectionMaskExample.dlg (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/UistylerSelectionMaskExample)
  

-----------
Build Steps
-----------

Windows
-------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as UistylerSelectionMaskExample. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the UistylerSelectionMaskExample.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.
   
5. Add references to NXOpen.dll, NXOpen.UF.dll, NXOpen.Utilities.dll, and NXOpenUI.dll. 
   To do this, right click on
   "Add Reference.." under the UistylerSelectionMaskExample project in Solution Explorer and then navigate to the location of the dlls. These dlls
    can be found in %UGII_BASE_DIR%\nxbin\managed.  Set the copy local attribute
    for these DLLs to be false so you always use the versions from the NX install.
   
6. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called <PROJECTNAME>.dll in the Debug directory.


Linux
-------
   -NA-
   
----------------------------
Settings before Launching NX
----------------------------
  The dlg file must be placed in one of the following locations:
    1. From where NX session is launched
    2. $UGII_USER_DIR/application
    3. For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
        
----------------------------
Settings after Launching NX
----------------------------

 1. Change the Role to Advanced.        
   
         
------------------------
Example execution steps
------------------------

  1. Start NX.
  
  2. Open UistylerSelectionMaskExample.prt file.
  
  3. Go to File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog. 
     Navigate to UistylerSelectionMaskExample.dll file.
  
  4. It will launch "Move to Layer" dialog.
  
  5. Set the Toggle ON for all the entities for which you need to set the Mask and hit the Set Filter button. 
	 Now, you will be able to select only those entities for which the Toggle is ON. Every time you change the
	 filter items you need to hit Set Filter button in order to change the Selection Mask.
	 
  6. If you Hit on the "Layer Setting Information" button, this pops up an information window showing the layer categories, 
	 the layers in each category and the object count in each layer.
	 
  7. After selection, change the layer number in "Move to Layer" field to the layer to which you would like to 
	 move the entities to, and Hit Apply or OK. This will move the selected entities to the desired layer. You can
	 check the number of objects in the layers thru the "Layer Setting Information" button.
  
-----
Note:
-----
   "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
