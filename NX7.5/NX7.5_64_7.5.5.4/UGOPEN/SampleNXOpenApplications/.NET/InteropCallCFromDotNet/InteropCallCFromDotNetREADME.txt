' ===================================================================
'
'             Copyright (c) 2009  Siemens PLM
'
'  
' ===================================================================


How to build the example:

You need to build both the C++ and .Net portions.

C++ 
- Use ufcomp and uflink to build the UFLegacyApp.cpp into UFLegacyApp.dll.

.Net
- In a working directory, copy the files for the InteropCallCFromDotNet example.
- Open up the VB .NET project (InteropCallCFromDotNet.vbproj) in Visual Studio.
- Add references to NXOpen.dll, NXOpen.UF.dll, NXOpenUI.dll, NXOpen.Utilities.dll.
  To do this, click MB3 on InteropCallCFromDotNet project in Solution
  Explorer.  Pick "Add Reference..." and then navigate to the location of the dlls.
  These NX dlls can be found in the managed subdirectory under %UGII_ROOT_DIR%.  
  Find and highlight the library, click Select and then OK on the Add Reference form.
- Select the Build->Build Solution menu command.
- The executable will be placed in a subdirectory named "bin" under the working 
  directory after the build completes.

How to run the example

- Make sure that C++ dll (i.e. UFLegacyApp.dll) is available in your PATH.
- Start up an NX session.
- Go to File -> Execute -> NX Open.  This will bring up the Execute User Function 
  dialog. Browse to the InteropCallCFromDotNet.exe location in the "bin" directory.  
- Select the InteropCallCFromDotNet.exe executable and click OK.  NOTE: you may have to 
  change the file type filter to *.exe to allow you to select the .exe file.

