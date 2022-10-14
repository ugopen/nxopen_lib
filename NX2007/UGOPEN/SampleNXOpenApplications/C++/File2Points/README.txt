'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		File2Points C++ Project Overview
------------------------------------------------------------------------------

-----------
Description
-----------
This example shows how a user can select a text file and create a set of points 
in the work part from the data in the text file. It is a reimplementation of the 
file2points grip program in C++. 

Design Notes
------------
On Windows, the example illustrates how to use Microsoft Foundation Classes to 
create an open file dialog, but we could have used UF_UI_create_filebox instead.  
The ONLY reason that we use MFC instead of UF_UI_create_filebox is for the 
purpose of demonstrating how MFC can be used inside an NX Open application.

INPUT file Format
-----------------
The text file read should have one point per line. Each point is a comma separated 
list of three numbers. An example to create points at the corners of a square is:

--- start of file ---
0,0,0
1,0,0
1,1,0
0,1,0
--- end of file ---


--------------
Files required
--------------
   1. File2Points.cpp
   2. File2PointsCPP_Input.txt  

  The above listed files are located at
  $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/File2Points.

------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio.

   2. Create new project as:
        2.1. File->New->Project.
 	2.2. Using Visual C++ Projects select the NX Open AppWizard, Class Library Application, Enter
             name as 'File2Points'. Click Next
        2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
             and select 'C++'. 
        2.4. Select to activate the application explicitly and to unload the application when NX session terminates. Click Finish.

   3. Remove the File2Points.cpp file from the source folder in the project. Highlight it in the Solution Explorer and use 
      the 3rd mouse button and pull to remove it. You will receive a pop-up that says it will be deleted permanently. Hit OK.

   4. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'. Navigate to and add the File2Points.cpp file provide with the example.

   5. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.
   		
   6. This will create an executable called File2Points.dll in the \Debug directory.


   The uflink tool can also be used to create the executable by following these steps:
   ------------------------------------------------------------------------------------
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink. Type the following commands:
	
      ufcomp File2Points.cpp
      uflink UFDLL=File2Points.dll

   This will create File2Points.dll in the current directory.


   Linux
   -------
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => File2Points
   7. Do not add any subroutines or libraries.
       
   This will create File2Points.so in the current directory.

   Exit out of ufmenu.

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
     -NA-

     Shared Library execution
     ------------------------
      1. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      2. Browse and select the File2Points.dll/.so and execute.
      3. This will lead to Windows Open File Dialog.
      4. Navigate to the location of the provided File2PointsCPP_Input.txt file.
      5. Hit Ok. You will see four points on the screen.
    
-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

'=================================End=========================================
