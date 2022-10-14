------------------------------------------------------------------------------------

       Copyright 2014 Siemens Product Lifecycle Management Software Inc. 
                           All Rights Reserved.

------------------------------------------------------------------------------------



------------------------------------------------------------------------------------
                        Selection.py Example
------------------------------------------------------------------------------------

DESCRIPTION
This example demonstrates alternatives to the code recorded while performing a
'Select All' using various filtering methods before an operation.  The example
shows how filtering by type, detailed type, layers, display attributes and color
can be accomplished via automation. The example gets the datums on the work part
that satisfy the filtering criteria and blanks the datums.

HOW TO RUN THE EXAMPLE
- Open the sample part, Selection_datums.prt from the directory
   $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/Selection
   or any other part with datums.
- Run Selection.py from the Journal Manager (ALT-F8).
- After each blanking opertion, a message box will display indicating
  how many datums were blanked and then the blanking is undone.
