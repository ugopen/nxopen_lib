'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
                Spell Checker Example
------------------------------------------------------------------------------

-----------
Description
-----------
This NXOpen example demonstrates the use of NXOpen and the Microsoft Word
COM API for enhancing the functionality of NX.  The example demonstrates
programmatic access to the NX user interface and the NX application data.
The example has been tested with Word 9.0 and 11.0.

--------------
Files required
--------------
   1. NXSpellChecker.vb
   2. SpellChecker.vbproj
   3. SpellCheckerAssemblyInfo.vb
   4. WordSpellChecker.vb
   5. block_with_notes.prt 
   
   The above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.Net/VB/SpellChecker
  
------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio .Net.

   2. Open up the VB project SpellChecker.vbproj

   3. Add the following references,
        3.1. NXOpen.dll 
        3.2. NXOpenUI.dll 
        3.3. NXOpen.Utilities.dll
        3.4. NXOpen.UF.dll.

      To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
      Go to %UGII_BASE_DIR%\nxbin\managed.  Select and add the DLL's one after the other.

   4. Add a reference to Microsoft Word Object Library
    4.1. Microsoft.Office.Interop.Word
         To do this, right click on the project in Solution Explorer. 
         Pick Add Reference->.NET and select Microsoft.Office.Interop.Word from the list.

   5. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
      right click on project name and select Build.

   6. This will create an executable called SpellChecker.dll in the \obj\Release directory.

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
     -NA-
        
     Shared Library execution
     ------------------------
      1. Open block_with_notes.prt part.
      2. Enter Drafting Application.
      3. To add additional note/label, select Insert->Annotation->Note, enter any text in the Formatting window and close.
      3. File -> Execute -> NXOpen through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      4. Browse and select the SpellChecker.dll and execute.
      5. Select any number of Notes or Labels on the part and press OK. Use <ALT><TAB> to bring up the spell checker window.
      6. Each line in a Note or Label will bring up the Word spell checking dialog.
         Make any spelling corrections in the Word spell checking dialog and close
         the dialog each time.
      7. Once all the selected Notes and Labels have been checked, execution is complete,
         and the SpellChecker.dll is unloaded immediately.
------
Notes
------

1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
   For more details on signing the application refer to NXOpen Programmer's Guide."

2. The Spell checker window loads up behind the NX window. To keep the user informed, a hint is shown in the status line to use <ALT><TAB> to 
   bring up the spell checker window. 

'=================================End=========================================
