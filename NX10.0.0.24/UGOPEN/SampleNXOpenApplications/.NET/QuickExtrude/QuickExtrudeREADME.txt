---------------------------------------------------------------------

                    Copyright (c) 2004 UGS
                Unpublished - All rights reserved
 
'  
---------------------------------------------------------------------

---------------------------------------------------------------------
                         QuickExtrude Example
---------------------------------------------------------------------

-----------
Description
-----------
 
        This example demonstrates the creation of Extrude feature for the selected sketch. 

--------------
Files required
--------------

        1. QuickExtrude.vb
        2. block_with_sketch.prt(This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/QuickExtrude)
        
-----------
Build Steps
-----------

Windows
-------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as QuickExtrude. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the QuickExtrude.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.

5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called QuickExtrude.dll in the Debug directory.
                   
Linux
-------
   -NA-             
    
----------------------------
Settings before Launching NX
----------------------------
        N/A

----------------------------
Settings after Launching NX
----------------------------

        1. Change the Role to Advanced.
  
  
-----------------------
Example execution steps
-----------------------
        1. Start NX.
        
        2. Open block_with_sketch.prt or any other part with a sketch.
        
        3. Follow any one of the methods mentioned below:

            3.1 Using Tools->Journal->Play  
            
               - Invoke QuickExtrude.vb file using Tools->Journal->Play (Alt+F8).
               
            3.2 By creating Shared Library and invoke QuickExtrude.dll through File->Execute->NX Open Menu (Ctrl+U).
            
        4. It will prompt for a sketch to be selected - Select a sketch and hit OK. 
        
        5. It will prompt for a start limit - Enter a value if desired and hit OK.
        
        6. It will prompt for an end limit - Enter a value if desired and hit OK.
        
        7. Extrude feature will be created for the selected sketch with an two sided Offset value of 0.25 inch.
        
-----
Note:
-----

"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."      
        
        
            


