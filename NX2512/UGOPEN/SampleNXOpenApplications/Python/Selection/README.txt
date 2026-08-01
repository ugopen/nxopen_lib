------------------------------------------------------------------------------------

       Copyright 2018 Siemens Product Lifecycle Management Software Inc. 
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
    2. Selection_datums.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/Selection)

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
  
        1.2 Open the part Selection_datums.prt or any other part with datums.
        
        1.3 Invoke Selection.py file using Tools->Journal->Play (Alt+F8).
        
        1.4 This will start blanking datum's and a message will be popped to the user after every blank operation and then the blanking is undone.
-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

