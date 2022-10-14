========================================================================
                 File2Points C++ Project Overview
========================================================================

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
   1. Open Microsoft Visual Studio .NET 2003.
   2. Open File2Points.vcproj file thru File Menu->Open->Project.
   3. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Build or Rebuild OR Go to Build Menu -> Build Solution or Ctrl + Shift + B.
   This will create File2Points.dll in the project's Debug folder.
   
   Unix
   ------
   Run make.
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
