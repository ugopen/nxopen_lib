===============================================================================

    Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

  
=================================================================================

----------------------------------------------------------------------------------
        		        Fillout Title Block Example
----------------------------------------------------------------------------------

-------------------
Description
-------------------
This example demonstrates the filling up of drawing notes in the empty title block of a 'C' size drawing sheet only.
The inputs for the fields are queried from user and then the placement of these notes at appropriate locations in the title block is done.

--------------
Files required
--------------

    1. FilloutTitleBlock.vb
    2. FillOutTitleBlock_bonnet_5055.prt (The part file is located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\C++\FilloutTitleBlock.)
	
    The above listed files are located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\FilloutTitleBlock.
    Note: the UGII_BASE_DIR is expanded in the SYSLOG if the system does not recognize the environment variable.

------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio .Net.

   2. Create new project as:
      2.1. File->New->Project.
 	  2.2. Select Visual Basic Projects using the NX Open AppWizard, Class Library Application, Enter
           name as FilloutTitleBlock. Click Next
      2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
           and select 'NXOpen.UI API'. 
      2.4. Select to activate the application explicitly and to unload the application when NX session terminates. Click Finish.

   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.

   4. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'.  Navigate to and add the FilloutTitleBlock.vb file.

   5. Add the following reference,
	  5.1. System.Windows.Forms
      5.2. System.Drawing
		   To do this, right click on "References" under the project in Solution
		   Explorer. Pick Add Reference->.NET Tab->under component name,
		   select System.Windows.Forms. Repeat the process and select System.Drawing
      5.3. NX Open References
           Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
           To do this, right click on "References" under the FilloutTitleBlock project in Solution Explorer. 
           Pick "Add Reference..." and then navigate to the location of the dlls. 
           These dlls can be found in %UGII_ROOT_DIR%\managed.
   		
   6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   7. This will create an executable called FilloutTitleBlock.dll in the \bin\Release directory.

   Linux
   -------
   -NA-

----------------------------
Settings before Launching NX
----------------------------
    -NA-

----------------------------
Settings after Launching NX
----------------------------
    1. Change the Role to Advanced with full menus.
    2. Set the drawing template as per the below instructions:-
		2.1	In NX, go to Preferences-Palettes.
		2.2	On the palette dialog choose "Open Palette File".
		2.3	Browse to your "%UGII_BASE_DIR%\ugii\html_files" folder.
		2.4	Choose the "english_drawing_templates.pax" file.
		2.5	The palette should now be available on your resource bar.

-----------------------
Example execution steps
-----------------------
     Journal execution
     ------------------
      1. Open FilloutTitleBlock_bonnet_5055.prt
	  2. Click on Start, Go to Drafting Application and apply the Template for a C-size drawing from the Drawing Template tab.
	     Note: If drawing template is unavailable then set the template as per the instruction specified in section "Settings after Launching NX".
      3. Once the template is loaded the drafting application will have C-drawing sheet.
	  4. Use Tools->Journal->Play or (Alt+F8) to launch the Journal Manager.
      5. Select FilloutTitleBlock.vb and click Run.
      6. User will be prompted to fill out the data to populate in the title block using a form. Fill the required data and click Ok.
      7. The TitleBlock will be updated with the required data. As a result, sheet:SH1 will pop up showing names, date and updated information on the sheet.

     Library execution
     ------------------------
      1. Perform the steps 1 - 3 as specified above in Journal execution.
	  2. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      3. Browse and select the FilloutTitleBlock.dll and execute.
      4. User will be prompted to fill out the data to populate in the title block using a form. Fill the required data and click Ok.
      5. The TitleBlock will be updated with the required data. As a result, sheet:SH1 will pop up showing names, date and updated information on the sheet. 
  
-----------------------
Notes
-----------------------
	1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
	    For more details on signing the application refer to NXOpen Programmer's Guide."
	
	2. User will require a .NET authoring license to run the example. See the online documentation for details of licensing.
		
 '=================================End=========================================
