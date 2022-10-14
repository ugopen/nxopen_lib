------------------------------------------------------------------------------------

       Copyright (c) 2016 Siemens Product Lifecycle Management Software Inc. 
                           All Rights Reserved.

------------------------------------------------------------------------------------



------------------------------------------------------------------------------------
                        ListMaterialNames.py Example
------------------------------------------------------------------------------------

DESCRIPTION
This example demonstrates using the XML Element Tree Python module to access the 
materials stored in a library material XML database file. It uses the example material 
database file provided with NX, but it can be modified to look in a different file.
The library material databases used by NX store the materials data in the MatML XML 
schema. This journal uses XPath to look for a specific element in the file that 
represents the name for each material stored in the file. It uses some other Python 
modules to sort the strings using a locale specific sorting algorithm that performs 
a case-insensitive sort. 

--------------
Files required
--------------

    1.  ListMaterialNames.py

----------------------------
Settings before Launching NX
----------------------------
    -NA-

----------------------------
Settings after Launching NX
----------------------------
    1.  Change the Role to Advanced if not set.

-----------------------
Example execution steps
-----------------------

Use Tools->Journal->Play
   
    1.  Start NX.
  
    2.  Invoke ListMaterialNames.py file using Tools->Journal->Play (Alt+F8).
        
    3.  The names of the materials stored in the database are output to the 
        ListingWindow.
