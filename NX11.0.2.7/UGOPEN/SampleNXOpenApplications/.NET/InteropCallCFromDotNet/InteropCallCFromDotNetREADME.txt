'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		InteropCallCFromDotNet Example
------------------------------------------------------------------------------

-----------
Description
-----------
Sample code showing interactions with a C application. 
Example shows how to call a C++ application from within DotNet.

--------------
Files required
--------------
   1. InteropCallCFromDotNet.vbproj
   2. UFLegacyApp.cpp
   3. VBapp.vb
   4. wrappers.vb

------------
Build steps
------------
   Windows
  ---------
   Build Steps for UFLegacyApp.dll in CPP
  -----------------------------------------
   1. Open Microsoft Visual Studio .Net.
   2. Create new project as:
      2.1. File->New->Project.
      2.2. Select Visual C++ .Using the NX Open AppWizard, Class Library Application, Enter
           name as 'UFLegacyApp'. Click Next
      2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'
           and select 'C++'. 
      2.4. Select to activate the application explicitly and to unload the application when NX session terminates.
            Click Finish.

   3. Remove the 'UFLegacyApp.cpp' file under source from the project. Highlight it in the Solution Explorer and 
      use the 3rd mouse button and pull to Remove it. You will receive a pop-up that says it will be deleted 
      permanently. Hit Remove.
   4. In the Solution Explorer Select the Source folder and use the 3rd mouse button and drag to Add.  
      Choose 'Add-> Existing Item'. Navigate to and add the UFLegacyApp.cpp file provided with the example.   		
   5. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.
   6. This will create an executable called UFLegacyApp.dll in the \debug directory.

   Build Steps for VB project
  ----------------------------
   1. Open Microsoft Visual Studio .Net.
   2. Open up the VB project InteropCallCFromDotNet.vbproj
   3. Add the following references,
        3.1. NXOpen.dll 
        3.2. NXOpenUI.dll 
        3.3. NXOpen.Utilities.dll
        3.4. NXOpen.UF.dll.

      To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
      Go to %UGII_BASE_DIR%\nxbin\managed.  Select and add the DLL's one after the other.
   4. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
      right click on project name and select Build.
   5. This will create an executable called InteropCallCFromDotNet.exe in the \bin\Release directory.

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
     Journal execution
     ------------------
     -NA-
        
     Shared Library execution
     ------------------------
      1. Open new part.
      2. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      3. Select InteropCallCFromDotNet.exe and Run
         NOTE: you may have to change the file type filter to *.exe to allow you to select the .exe file.
      4. See the syslog for success / failure messages . 
      
    
------
Notes
------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

'=================================End=========================================
