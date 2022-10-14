'=============================================================================
'
'                   Copyright (c) 2012 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================
-------------------------------------------------------------------------------
                      Title Block Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example performs the following steps:

    1) Queries the user for Part Name and Author Name.
    2) Inserts a custom symbol for the title block.
    3) Inserts the labels in the title block, and the user entered data.
       The date field is determined by the system's date.

--------------
Files required
--------------
    1. Generate_title_block.vb
    2. DrawingSheet.prt
    3. special.sbf

    The above listed files are Located at
    $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\TitleBlock.

------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio

   2. Create new project as:
		2.1. File->New->Project.
		2.2. Select Visual Basic Projects using the NX Open AppWizard, Class Library Application, Enter
             name as 'TitleBlock'. Click Next
        2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
             and select 'NXOpen.UI API'. 
        2.4. Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.

   4. Add the following reference,
		4.1. System.Windows.Forms
		4.2. System.Drawing
		     To do this, right click on "References" under the TitleBlock project in Solution
             Explorer. Pick Add Reference->.NET Tab->under component name,
             select System.Windows.Forms. Repeat the process and select System.Drawing
        4.3. NX Open References
             Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
             To do this, right click on "References" under the TitleBlock project in Solution Explorer. 
             Pick "Add Reference..." and then navigate to the location of the dlls. 
             These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.

   5. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'. Navigate to and add the Generate_title_block.vb file.
   		
   6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   7. This will create an executable called TitleBlock.dll in the \bin\Release directory.

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
    1. Open the example part that contains a drawing sheet(DrawingSheet.prt)

    2. Using Tools->Journal->Play or (ALT+F8).

    3. Select Generate_title_block.vb and Run.

    4. Fill in Part Name and Author Name fields, and hit OK on form.

    5. The title block will be generated.  The title block can then be moved to another location on the sheet.
       Notice that all the text is associative to the framing title block.

    Shared Library execution
    ------------------------
    1. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.

    2. Browse and select the TitleBlock.dll and execute.

    3. Follow point no.4 onwards mentioned above in 'Journal execution'.
    
	USING OTHER PARTS
    -------------------
	A part other than the example part can be used. However, there are two issues 
	that we need to take care of.
		
		1) The file special.sbf, must be at the same file location as the 
		part you want to use.

		2) The preferences related to lettering size may be set in the part
		may cause the title block text to not show optimally. 

------
Notes
------
    1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
       For more details on signing the application refer to NXOpen Programmer's Guide."

    2. You will need a .NET authoring license to run the example. See the online documentation for details of licensing.

'=================================End=========================================




