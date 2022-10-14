' ===================================================================
'
'             Copyright (c) 2004  UGS PLM Solutions
'               Unpublished - All rights reserved
'
'  
' ===================================================================
This NX Open example demonstrates the use of NXOpen and the Microsoft Word
COM API for enhancing the functionality of NX.  The example demonstrates
programmatic access to the NX user interface and the NX application data.
The example has been tested with Word 9.0 and 11.0.

The flow of the example is as follows:

- Select Notes/Labels within NX.
- Query of the text property for a Note/Label.
- Pass the text to Word for spell checking.
- Modify the text property for a Note/Label.
- Perform an update in NX to reflect the changes to the text.
- Unhighlight the selected Notes/Labels.

To build this example:

- Open up the VB .NET project (SpellChecker.vbproj) in Visual Studio.
  NOTE: For Visual Studio 2005, this will bring up a series of dialogs to migrate
  the project to 2005.  Accept the defaults.
- Set the reference path to the NXOpen* dlls.  To do this, MB3 on the SpellChecker
  project in Solution Explorer and pick Properties.  Under Common Properties, pick
  Reference Path.  Add the directory for the managed dlls to the Reference Path
  (enter the location and click Add Folder).
  NOTE: For Visual Studio 2005, the UI has changed.  To do this, MB3 on the SpellChecker
  project in Solution Explorer and pick Properties.  Select References tab on the left side.  
  Then pick pick Reference Path.  Add the directory for the managed dlls to the Reference Path
  (enter the location and click Add Folder).

  Note: The dlls are located at %UGII_ROOT_DIR%\managed but you will need to
  enter the value of %UGII_ROOT_DIR% instead of the variable directly because
  Visual Studio does not accept environment variables in the Reference Path.
  
- Add a reference to:
	Microsoft Word Object Library
  To do this,
   -click MB3 on "References" under the SpellChecker project in Solution Explorer.  
    NOTE: For Visual Studio 2005, the UI has changed.  To do this, MB3 on the SpellChecker
    project in Solution Explorer and pick Add Reference.  
   -The Microsoft Word Object Library is under the COM tab on the Add Reference form.  
    Find and highlight the library, click Select and then OK on the Add Reference form.
   
   NOTE: For Visual Studio 2005, change the Imports statement for Word in  WordSpellChecker.vb.
   Comment the "Imports Word" and uncomment the lines below it.
   
- Build the project.

To run this example:

- Start NX
- Open the part file, block_with_notes.prt included with the example or another
  part with Notes/Labels via File->Open.
- Enter the Drafting application.
- Load the SpellCheck.dll located in the <working directory>\bin 
  subdirectory via File->Execute->NX Open... or Ctrl+U.
- Select any number of Notes or Labels on the part.
- Each line in a Note or Label will bring up the Word spell checking dialog.
  Make any spelling corrections in the Word spell checking dialog and close
  the dialog each time.
- Once all the selected Notes and Labels have been checked, execution is complete,
  and the SpellCheck.dll is unloaded immediately.
