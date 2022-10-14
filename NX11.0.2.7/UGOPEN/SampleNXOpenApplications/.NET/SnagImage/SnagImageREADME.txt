'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		Snag Image Example
------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates the use of NXOpen.UF (.NET Wrapper of UF) API's in
conjunction with Winforms.

The example uses .NET Wrapped UG/Open (NXOpen.UF) API 'Disp.CreateImage' to 
capture the NX Graphics Window in different image formats with different 
background color.

--------------
Files required
--------------
   1. SnagImageVB.vb
   2. SnagImageVB.vbproj
   3. SnagImageVB.resx
  
------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio .Net.
   2. Open up the VB project SnagImage.vbroj
   3. Add the following references,
        3.1. NXOpen.dll 
        3.2. NXOpenUI.dll 
        3.3. NXOpen.Utilities.dll
        3.4. NXOpen.UF.dll.

      To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
      Go to %UGII_BASE_DIR\nxbin%\managed.  Select and add the DLL's one after the other.
   		
   4. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
      right click on project name and select Build.
   5. This will create an executable called SnagImage.dll in the \obj\Release directory.

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
     -NA-
        
     Shared Library execution
     ------------------------
      1. Open new or any part.
      2. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      3. Browse and select the SnagImage.dll and execute.
      4. 'SnagImage: Grab a NX Graphics Windows Region' Dialog box wil pop-up
      5. Select the file format, background color, name and location of the image file.
      6. Click SnagIt button to capture and write the file to the desired location.
      7. When the image is generated, you will receive a pop-up telling you so.
      8. Check the file name, format and location of the file.

-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

The default path for the image file will be in the directory from where NX was started.

'=================================End=========================================
