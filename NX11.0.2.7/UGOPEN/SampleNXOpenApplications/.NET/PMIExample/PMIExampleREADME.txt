'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		PMI Example
------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates the creation of a PMI dimension in 3D model space.

--------------
Files required
--------------
   1. PMIExample.vb
   2. PMI.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/Dotnet/VB/PMIExample)
 
------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio .Net.

   2. Create new project as:
      2.1. File->New->Project.
      2.2. Select Visual Basic Projects using the NX Open AppWizard, Class Library Application, Enter
           name as 'PMIExample'. Click Next
      2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
           and select 'NXOpen.UI API'. 
      2.4. Select to activate the application explicitly and to unload the application when NX session terminates. Click Finish.


   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.

   
   4. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'. Navigate to and add the PMIExample.vb file.
   		
   5. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   6. This will create an executable called PMIExample.dll in the \bin\Release directory.

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
      1. Open part PMI.prt.
      2. Using Tools->Journal->Play or (Alt+F8)
      3. Select PMIExample.vb and Run
      4. This will create a diameter dimension on the cylinder in the 3D Model.
        
     Shared Library execution
     ------------------------
      1. Open part PMI.prt.
      2. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      3. Browse and select the PMIExample.dll and execute.
      4. This will create a diameter dimension on the cylinder in the 3D Model.
    
-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

If you are in Drafting application and you run the Journal the dimension will be created in
the drafting view.

'=================================End=========================================
