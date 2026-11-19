'=============================================================================
'
'                   Copyright (c) 2012 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================
-------------------------------------------------------------------------------
                      File to Points Example
-------------------------------------------------------------------------------


-------------------
Description
-------------------
This example shows a journal which allows the user to select a text file and create a set of points in the work part
from the data in the file. It is a reimplementation of the file2points grip program in Visual Basic .Net and 
show using the .Net open file dialog together with .Net IO to read a text file. 
The grip program is provided for comparison.


--------------
Files required
--------------

	1. file2points.grs
	2. file2points.vb
	3. points.txt
	
    The above listed files are located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\File2Points
    Note: the UGII_BASE_DIR is expanded in the SYSLOG if the system does not recognize the environment variable.

------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio

   2. Create new project as:
		2.1. File->New->Project.
		2.2. Select Visual Basic Projects using the NX Open AppWizard, Class Library Application, Enter
		   name as 'FileToPoint'. Click Next
		2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
		   and select 'NXOpen.UI API'. 
		2.4. Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.
 
   4. Add the following reference,
		4.1. System.Windows.Forms
		4.2. System.Drawing
			 To do this, right click on "References" under the project in Solution
			 Explorer. Pick Add Reference->.NET Tab->under component name,
			 select System.Windows.Forms. Repeat the process and select System.Drawing
        4.3. NX Open References
             Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
             To do this, right click on  "References" under the FileToPoint project in Solution Explorer. 
             Pick "Add Reference..." and then navigate to the location of the dlls. 
             These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.

   5. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'. Navigate to and add the File2Points.vb file.
   		
   6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   7. This will create an executable called FileToPoint.dll in the \bin\Release directory.

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
    1. Change the Role to Advanced.

-----------------------
Example execution steps
-----------------------
    Journal execution
     ------------------
      1. Open an existing part or create a new part.

      2. Using Tools->Journal->Play or (Alt+F8)

      3. Select file2points.vb and Run

      4. You will be prompted for an input file.  This file should contain the points that you want to create.  
	     An example has been provided (points.txt).  Its contents are described below in the Notes section.

      5. Select the input file and hit OK.

      6. The points from the file will be created in the part.
  
     Shared Library execution
     ------------------------
      1. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.

      2. Browse and select the FileToPoint.dll and execute.
      
      3. Follow point no.4 and onwards, mentioned above in 'Journal execution'.
	
 
-----------------------
Notes
-----------------------
	1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
	    For more details on signing the application refer to NXOpen Programmer's Guide."
	
	2. User will require a .NET authoring license to run the example. See the online documentation for details of licensing.

	3. This uses the .Net Windows Forms open file dialog to select a .txt file. The file is read a line at a time and the
	   line is parsed into 3 doubles. Points are created using this data.
	   The points are created invisible and must be made visible explicitly.

	4. FILE FORMAT:
	   The text file read should have one point per line. Each point is a comma separated list of three numbers. 
	   An Example to create points at the corners of a square is:

	   --- start of file ---
	   0,0,0
	   1,0,0
	   1,1,0
	   0,1,0
	   --- end of file ---
	   
'=================================End=========================================
