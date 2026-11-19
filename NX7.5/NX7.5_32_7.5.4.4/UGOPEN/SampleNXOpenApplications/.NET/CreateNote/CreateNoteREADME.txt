-------------------------------------------------------------------------------


          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.
                           
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                            Create Note Example
-------------------------------------------------------------------------------

This example creates notes by either copying an existing note or creating a note from a user defined symbol.

HOW TO RUN THE EXAMPLE

- Open a part.  If you have one that has a note in it, that would be helpful.  If not, open any part or an new/empty part.
- Run create_note.vb.
- On the dialog, select either the "create from user defined symbol" or "copy existing note" option.
	For create from user defined symbol:
		- Select the name of the user defined symbol and the symbol's size and aspect ratio.
		- Click the "Create" button.
		- Pick the location for the new note.  The note will be created in the XY plane of the WCS.  
		  You can create as many copies as you want.  
		- When you are finished, cancel when prompted for the location.

	For copy existing note:
		- Click the "Create" button.
		- Select a note to copy.  You can select one that existed previously in the part or select
		  one that was just created.
		- Pick the location for the new note.  The note will be created in the XY plane of the WCS.  
		  You can create as many copies as you want.  
		- When you are finished, cancel when prompted for the location.


DESIGN NOTES

The key portions of code are UserSymbolForm.GetNoteCreationData, UserSymbolForm.LoadSymbolNames, and the call to Annotations.CreateNote in the Main subroutine.  Most of the rest of the code is just for the GUI for the example.  LoadSymbolNames reads the names of the available user defined symbols from the selected Symbol Font Definition file (sbf file).  GetNoteCreationData gets the text and preferences for the new note.  If "copy existing note" was selected, GetNoteCreationData prompts the user to pick a note and gets the text and preferences for the new note from the selected note.  If "create from user defined symbol" is selected, the user symbol that was selected is loaded into the part and the user symbol preferences for the new note are constructed based on what the user specified on the form.  Then, the main subroutine prompts the user for the location for the new note and creates the note.
