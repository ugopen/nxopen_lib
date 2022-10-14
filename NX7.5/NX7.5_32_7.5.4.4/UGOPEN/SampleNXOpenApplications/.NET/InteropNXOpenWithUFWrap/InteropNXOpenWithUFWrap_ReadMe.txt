-------------------------------------------------------------------------------


          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        CONSOLE APPLICATION : InteropNXOpenWithUFWrap Project Overview
-------------------------------------------------------------------------------

Purpose of this Example : 
-------------------------

This Sample program demonstrates the interoprability of NXOpen and NXOpen.UF 

Steps followed in this Example
------------------------------
1. Create a new part file	using	NXOpen
2. Query the part name		using	NXOpen.UF
3. Create Line			using	NXOpen
4. Query line data		using	NXOpen.UF
5. Create Arc			using	NXOpen.UF
6. Query  Arc parameters	using	NXOpen
7. Save the Part		using	NXOpen.UF

How to Build
------------
- In a working directory, copy the files for the InteropNXOpenWithUFWrap example.
- Open up the CS project file InteropNXOpenWithUFWrap.csproj in Visual Studio .Net 2003.
- Add references to NXOpen.dll, NXOpen.UF.dll, NXOpen.Utilities.dll.
  To do this, click MB3 on "References" under the InteropNXOpenWithUFWrap project in Solution
  Explorer.  Pick "Add Reference..." and then navigate to the location of the dlls.
  These NX dlls can be found in the managed subdirectory under %UGII_ROOT_DIR%.  
  Find and highlight the library, click Select and then OK on the Add Reference form.
- Select the Build->Build Solution menu command.
- The executable will be placed in a subdirectory named "bin\Debug" under the working 
  directory after the build completes.

How to Run
----------

Once you have successfully finished with "How to build" steps, it will create executable called
InteropNXOpenWithUFWrap.exe in bin\debug folder.

1. Executing this project thru Visual Studio :
	1. Click on Debug->Start or Start icon.

2. Executing this project using executable :
	1. Execute exe file on command prompt.
	
The part file InteropNXOpenWithUFWrap.prt is created under bin\Debug folder in project directory
even if you use any one of the above method to execute this project and can be opened for viewing in NX.
