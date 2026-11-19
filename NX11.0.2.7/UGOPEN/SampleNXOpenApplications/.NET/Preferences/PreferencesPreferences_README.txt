-----------------------------------------------------------------------------------

          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.
'   
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
						  Preferences Example
------------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates to set the Preferences of Sketch and Work Plane for NX session as per the requirement.
Executing this example will create prefs.prt with the specified preferences.   

--------------
Files required
--------------

    1. preferences.vb
    
-----------
Build Steps
-----------

Windows
-------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as preferences. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the preferences.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.

5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called preferences.dll in the Debug directory.

Linux
-------
   -N/A-

----------------------------
Settings before Launching NX
----------------------------
   -N/A-

----------------------------
Settings after Launching NX
----------------------------

1. Change the Role to Advanced.
    
    
--------------------------
Example execution steps
--------------------------
    
        1. Start NX.
        
        2. Follow any one of the methods mentioned below:

            2.1 Using Tools->Journal->Play 
            
               - Invoke preferences.vb file using Tools->Journal->Play or (Alt+F8).
               
            2.2 Go to File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog. Navigate to preferences.dll file.
                
        3.  It will open the new "prefs.prt" file with the specified Sketch, Grid and Workplane Preferences as mentioned in the "preferences.vb" file.
        
        4.  For cross verifying the set preferences,
                       
            Go to Preferences->Sketch->Session Settings tab, you can observe the Name Prefixes as follows
        
            Sketch Preferences:

            Default Name Prefixes
            Sketch:  SKT_
            Vertex:  VRT_
            Line:    LIN_
            Arc:     ARC_
            Conic:   CON_
            Spline:  SPL_
        
            Go to Preferences->Grid and Work plane, you can observe the work plane grid type is changed from rectangular to polar.
            Also, the following spacing preferences for grid lines are set: 
            
            Grid and Work Plane Preferences:
           
            Radial Spacing
            Major Grid Spacing:     75.0
            Minor Lines per Major:	3
            Snap Points per Minor:	5

            Angular Spacing
            Major Grid Spacing:     45.0
            Minor Lines per Major:	4		
            Snap Points per Minor:	2
            
	   
	       
-----
Note:
-----
  1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

 2. If the user want to change the Default "Sketch" and "Grid and Work plane" preferences, just update the preferences.vb file with the required parameters.     
    
    
    
    

