'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		          Create Note Example
------------------------------------------------------------------------------

-----------
Description
-----------
This example creates notes by either copying an existing note or creating a note from a user defined symbol.

--------------
Files required
--------------
   1. create_note.vb

    The above listed file is located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\CreateNote
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
             name as 'CreateNote'. Click Next
        2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
             and select 'NXOpen.UI API'. 
        2.4. Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.

   4. Add the following reference,
		4.1. System.Windows.Forms
		4.2. System.Drawing
		     To do this, right click on "References" under the project in Solution
             Explorer. Pick Add Reference->.NET Tab->under component name,
             select System.Windows.Forms. Repeat the process and select System.Drawing
        4.3. NX Open References
             Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
             To do this, right click on "References" under the CreateNote project in Solution Explorer. 
             Pick "Add Reference..." and then navigate to the location of the dlls. 
             These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.

   5. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'. Navigate to and add the create_note.vb file.
   		
   6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   7. This will create an executable called CreateNote.dll in the \bin\Release directory.

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
    1. Change the Role to Advanced if not set.

-----------------------
Example execution steps
-----------------------
     Journal execution
     ------------------
    1. Open a part.  If you have one that has a note in it, that would be helpful.  If not, open any part or an new/empty part.
    2. Using Tools->Journal->Play or (ALT+F8).
    3. Select create_note.vb and Run.
    4. Create Note dialog box will pop-up. On the dialog, select either the "Create from user defined symbol" or "Copy existing symbol" option.

        For Create from user defined symbol:
        -------------------------------------
	    4.1. Browse the location of the symbol font file. Select symbol. Enter scale and aspect ratio.
	    4.2. Click the "Create" button. It will prompt you to select screen position for the note.
	    4.3. Pick the location for the new note.  The note will be created in the XY plane of the WCS.You can create as many copies as you want.
	    4.4. When you are finished, hit cancel to escape from the prompt.

        For Copy existing symbol:
	    -------------------------
	    4.1. Click the "Create" button.
	    4.2. Select a note to copy.  You can select one that existed previously in the part or select one that was just created.
	    4.3. Pick the location for the new note.  The note will be created in the XY plane of the WCS. You can create as many copies as you want.  
	    4.4. When you are finished, hit cancel to escape from the prompt.

    Shared Library execution
    ------------------------
    1. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.

    2. Browse and select the CreateNote.dll and execute.

    3. Follow point no.4 mentioned above in 'Journal execution'.
    
-----------------------
Notes
-----------------------
    1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
        For more details on signing the application refer to NXOpen Programmer's Guide."

    2. DESIGN NOTES:
        The key portions of code are UserSymbolForm.GetNoteCreationData, UserSymbolForm.LoadSymbolNames,and the call to Annotations.CreateNote in the Main subroutine.  
        Most of the rest of the code is just for the GUI for the example. 
        LoadSymbolNames reads the names of the available user defined symbols from the selected Symbol Font Definition file (sbf file). 
        GetNoteCreationData gets the text and preferences for the new note.  
        If "copy existing note" was selected, GetNoteCreationData prompts the user to pick a note and gets the text and preferences for the new note from the selected note.  
        If "create from user defined symbol" is selected, the user symbol that was selected is loaded into the part and the user symbol preferences for the new note are 
        constructed based on what the user specified on the form.
        Then, the main subroutine prompts the user for the location for the new note and creates the note.

'=================================End=========================================
