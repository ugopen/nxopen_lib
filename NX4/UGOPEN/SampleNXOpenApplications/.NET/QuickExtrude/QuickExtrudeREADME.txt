' ===================================================================
'
'                   Copyright (c) 2004 UGS
'               Unpublished - All rights reserved
'
'  
' ===================================================================
QuickExtrude.vb example

This example demostrates the process of modifying a journal to work generically on
part files.  The original journal was the result of recording the extrude of the 
circle sketch on the block face and accepting the default extrude options.  Selection
code was added to allow selection of a sketch rather than using the circle sketch.  
Code was also added to allow the input of the start and end limits of the extrude
rather than using the defaults. 

Comments were added to the vb file to indicate where code was added and removed.
Added code is enclosed in the following comment lines:

'**** Added Code *****
'^^^^^^^^^^^^^^^^^^^^^

And removed code is enclosed in the following comment lines:

'**** Removed Code *****
'^^^^^^^^^^^^^^^^^^^^^^^

HOW TO RUN THE EXAMPLE
- Open the sample part, block_with_sketch.prt or any other part with a sketch.
- Run QuickExtrude.vb from the Journal Manager (ALT-F8). 
- It will prompt for a sketch to be selected - Select a sketch and hit OK.
- It will prompt for a start limit - Enter a value if desired and hit OK.
- It will prompt for an end limit - Enter a value if desired and hit OK.
The selected sketch will be a boolean create extrude.
