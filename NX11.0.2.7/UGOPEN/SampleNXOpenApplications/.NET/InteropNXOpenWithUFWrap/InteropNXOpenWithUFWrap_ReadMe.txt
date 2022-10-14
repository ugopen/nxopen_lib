'=============================================================================
'
'                   Copyright (c) 2013 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
' 
'  
'=============================================================================

------------------------------------------------------------------------------
        		InteropNXOpenWithUFWrap Example
------------------------------------------------------------------------------

-----------
Description
-----------

This Sample program demonstrates the interoperability of NXOpen and NXOpen.UF

--------------
Files required
--------------

   1. InteropNXOpenWithUFWrap.cs

------------
Build steps
------------
   Windows
  ---------
   1. In a working directory, copy the files for the InteropNXOpenWithUFWrap example.

   2. Open up the CS project file InteropNXOpenWithUFWrap.csproj in Visual Studio .Net .

   3. Add references to NXOpen.dll, NXOpen.UF.dll, NXOpen.Utilities.dll.
  
      - To do this, click MB3 on "References" under the InteropNXOpenWithUFWrap project in Solution
  Explorer.  
      - Pick "Add Reference..." and then navigate to the location of the dlls.
  
      - These NX dlls can be found in the managed subdirectory under %UGII_BASE_DIR%\nxbin.  
  
      - Find and highlight the library, click Select and then OK on the Add Reference form.

   4. Select the Build->Build Solution menu command.

   5. The executable will be placed in a subdirectory named "bin\Debug" under the working 
  
      directory after the build completes.

   Once you have successfully finished with "How to build" steps, it will create executable called
InteropNXOpenWithUFWrap.exe in bin\debug folder.
  
   Linux
   -------
     -NA-

----------------------------
Settings before Launching NX
----------------------------
Make sure that C++ dll (i.e. UFLegacyApp.dll) is available in your PATH

----------------------------
Settings after Launching NX
----------------------------
1. Change the Role to Advanced.

-----------------------
Example execution steps
-----------------------
   1. Executing this project through Visual Studio :
	
      1. Click on Debug->Start or Start icon.

   
2. Executing this project using executable :
	
      1. Execute exe file on command prompt.
	

      The part file InteropNXOpenWithUFWrap.prt is created under bin\Debug folder in project directory.
Use any one of the above methods to execute this project and can be opened for viewing in NX.
------
Notes
------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

'=================================End=========================================
