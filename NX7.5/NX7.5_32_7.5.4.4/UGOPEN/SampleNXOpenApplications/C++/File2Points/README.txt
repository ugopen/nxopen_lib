-------------------------------------------------------------------------------


          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                     File2Points C++ Project Overview
-------------------------------------------------------------------------------

Purpose of this Example
-----------------------

This example shows how a user can select a text file and create a set 
of points in the work part from the data in the text file. It is a reimplementation 
of the file2points grip program in C++. 

Design Notes
------------
On Windows, the example illustrates how to use Microsoft Foundation Classes to create
an open file dialog, but we could have used UF_UI_create_filebox instead.  The ONLY reason that
we use MFC instead of UF_UI_create_filebox is for the purpose of demonstrating how MFC
can be used inside an NX Open application.


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


How to Build
------------
   Windows
   -------
   1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the NX Open for C/C++ -> Open C Reference Guide -> 
      Overview -> setting up your system.  The image being created is an
      Internal User Function program using C++ and Open C++ calls.
   2. Add the File2Points.cpp file by selecting the Project pulldown and select 
      "Add Existing Item...".  Select the file using the popup window.
   3. Build the external image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
   This will create a library called File2Points.dll in the Debug folder.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
      uflink ufdll=File2Points.dll
   This will create File2Points.dll in the current directory.
   
   Unix
   ------
   Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu)
   Compile and link an internal user function program.  Select "i" when prompted for the 
     type of application to link - internal/external.  Select "y" for linking with user
     interface code.  Also select "n" for Linking a UG/Open++ image.  Select "y" for Link
     a C++ image.

   This will create File2Points.so.

How to Run
----------

1. Start NX.
2. Go to File -> New (Open new file) (You can open any part file for this).
3. Go to File Menu -> Execute ->NX Open.
3. You will lead to window called "Execute User Function". 
4. Navigate to the location of the shared object file.  On Windows, it will be in the Debug directory under 
   the directory named for the C++ project.
5. Select File2Points.dll or .so and click ok.
6. This will lead to Windows Open File Dialog.
7. Navigate to the location of the provided File2PointsCPP_Input.txt file.
8. Hit Ok. You will see four points on the screen.
