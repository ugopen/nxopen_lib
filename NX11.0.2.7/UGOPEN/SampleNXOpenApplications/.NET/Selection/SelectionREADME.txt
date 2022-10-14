' ===================================================================
'
'                   Copyright (c) 2004 UGS
'               Unpublished - All rights reserved
'
'  
' ===================================================================

-------------------------------------------------------------------------------
        		Selection.vb example
-------------------------------------------------------------------------------

DESCRIPTION
This example demonstrates alternatives to the code recorded while performing a
'Select All' using various filtering methods before an operation.  The example
shows how filtering by type, detailed type, layers, display attributes and color
can be accomplished via automation. The example gets the datums on the work part
that satisfy the filtering criteria and blanks the datums.

--------------
Files required
--------------

    1. Selection.vb
    2. datums.prt


-----------
Build Steps
-----------

Windows
-------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as Selection. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the Selection.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.

5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called Selection.dll in the Debug directory.

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

1. Using Tools->Journal->Play
   
        1.1 Start NX.
  
        1.2 Open the sample part, datums.prt or any other part with datums.
        
        1.3 Invoke Selection.vb file using Tools->Journal->Play (Alt+F8).
        
        1.4 After each blanking opertion, a message box will display indicating
       how many datums were blanked and then the blanking is undone.


2. By creating Shared Library and invoke it through File->Execute->NX Open Menu. 

    1. Start NX.

    2. Open the sample part, datums.prt or any other part with datums.
       
    3. Invoke Selection.dll through File->Execute->NX Open Menu (Ctrl+U).

    4. After each blanking opertion, a message box will display indicating
       how many datums were blanked and then the blanking is undone.

-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	   
