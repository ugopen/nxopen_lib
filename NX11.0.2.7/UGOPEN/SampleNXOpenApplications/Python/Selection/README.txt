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

--------------
Files required
--------------

    1. Selection.py
    2. datums.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/Selection)

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

1. Using Tools->Journal->Play
   
        1.1 Start NX.
  
        1.2 Open the sample part, datums.prt or any other part with datums.
        
        1.3 Invoke Selection.py file using Tools->Journal->Play (Alt+F8).
        
        1.4 After each blanking opertion, a message box will display indicating
       how many datums were blanked and then the blanking is undone.

