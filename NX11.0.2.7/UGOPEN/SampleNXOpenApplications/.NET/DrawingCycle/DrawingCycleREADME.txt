'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		Drawing Cycle Example
------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates on how to cycle through multiple drawing sheets 
acquiring and printing sheet data. 

--------------
Files required
--------------
   1. Drawing_part.prt 
   2. drawing_cycle.vb
  
    The above listed files are located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\DrawingCycle
    Note: the UGII_BASE_DIR is expanded in the SYSLOG if the system does not recognize the environment variable.

------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio.

   2. Create new project as:
		2.1. File->New->Project.
		2.2. Select Visual Basic Projects using the NX Open AppWizard, Class Library Application, Enter
			 name as DrawingCycle. Click Next
		2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
			 and select 'NXOpen.UI API'. 
		2.4. Select to activate the application explicitly(Main) and to unload the application when NX session terminates. Click Finish.

   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.

   4. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'. Select the file drawing_cycle.vb ($UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\DrawingCycle)
      and add it. 
	  
   5. Add the following reference,
		5.1. System.Windows.Forms
        To do this Go to Project->Add Reference-> .NET Tab->Under the Component Name; Select 'System.Windows.Forms' and hit Ok.
   		5.2. NX Open References
        Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
        To do this, right click on "References" under the DrawingCycle project in Solution Explorer. 
        Pick "Add Reference..." and then navigate to the location of the dlls. 
        These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.

   6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   7. This will create an executable called DrawingCycle.dll in the \bin\Release directory.

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
    1. Change the Role to Advanced.

-----------------------
Example execution steps
-----------------------
     Journal execution
     ------------------
      1. Open Drawing_part.prt 
      2. Using Tools->Journal->Play or (Alt+F8)
      3. Select drawing_cycle.vb and Run
      4. Window printing sheet:SH1 will pop-up showing names of all views on the sheet. Check for current Date 
         on the right hand top corner of the sheet. Click OK.
      5. Window printing sheet:SH2 will pop-up showing names of all views on the sheet. Check for current Date 
         on the right hand top corner of the sheet. Click OK and the print date should disappear

     Shared Library execution
     ------------------------
      1. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      2. Browse and select the DrawingCycle.dll and execute.
      3. Window printing sheet:SH1 will pop-up showing names of all views on the sheet. Check for current Date 
         on the right hand top corner of the sheet. Click OK.
      4. Window printing sheet:SH2 will pop-up showing names of all views on the sheet. Check for current Date 
         on the right hand top corner of the sheet. Click OK and the print date should disappear

-----------------------
Notes
-----------------------
	1.  "NXOpen application must be signed before its release. If not signed the application may not get executed.
		For more details on signing the application refer to NXOpen Programmer's Guide."

	2. Design NOTE: 
		2.1 This example is setup to place a note correctly for an E size drawing.  
			If you do not want to delete the note that is created, change the constant value of DO_NOT_DELETE_NOTE to be 1. 
		2.2 This example could be easily modified to cycle through multiple parts.
  

'=================================End=====================================
