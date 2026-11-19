'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		Block Styler Update Example
------------------------------------------------------------------------------

-----------
Description
-----------
This Block Styler example is the one given in the Block Styler Update section
of the Block Styler chapters in the NX Open Programmer’s Guide. The example shows 
a minimum number of template source files edits to demonstrate how to handle 
events from various blocks in the given dialog.

--------------
Files required
--------------
   1. UpdateExample.vb
   2. UpdateExample.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/UpdateExample)

------------
Build steps
------------
      Windows
     ---------
   1. Open Microsoft Visual Studio .Net.

   2. Create new project as:
      2.1. File->New->Project.
      2.2. Select Visual Basic Projects using the NX Open AppWizard, Class Library Application, Enter
           name as 'UpdateExample'. Click Next
      2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'
           and select 'NXOpen.UI API'. 
      2.4. Select to activate the application explicitly and to unload the application when NX session terminates. Click Finish.

   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
   4. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add-> Existing Item'. Navigate to and add the UpdateExample.vb file.
   		
   5. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   6. This will create an executable called UpdateExample.dll in the \bin\Release directory.

      Linux
     ---------
      -NA-

----------------------------
Settings before Launching NX
----------------------------
The UpdateExample.dlx file must be placed in one of the following locations:
	
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

-----------------------
Example execution steps
-----------------------
     Journal execution
     ------------------
      1. Open new part.
      2. Using Tools->Journal->Play or (ALT+F8)
      3. Select UpdateExample.vb and Run
      4. This will pop-up Update Example dialog box.
      5. Input String Block - the user may enter a string which will be copied to the Output 
         String Block.
      6. Include Number Toggle Block - when this toggle in ON the following number will be
         appended to the Output String Block.
      7. Number Integer Block - a slider that the user can use to set a number that is 
         optionally appended to the Output String Block.
      8. Output String Block - a String Block that is only used to display the input string 
         and the optional number. This block is always disabled.
      9. Lock Input String Toggle - when this toggle is ON the input string is disabled.
      10. Lock Number Toggle - when this toggle is ON the number slider is disable.
        
     Shared Library execution
     ------------------------
      1. Open new part.
      2. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      3. Browse and select the UpdateExample.dll and execute.
      4. This will pop-up Update Example dialog box.
      5. Follow instruction No.5 from Journal execution mentioned above.
    
-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."


'=================================End=========================================
