-------------------------------------------------------------------------------
 
        Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc.
                         All rights reserved



-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                            CAMSetupImport Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates the use of the NX Automation API to create and initialize a CAM Setup.
This dll creates a CAM Setup as it is defined in a xml with
    - Machine from the library
    - Part, Blank, Fixtures
    - Tools from the library
    - Main Programs, Subprograms

--------------
Files required
--------------
 1.CAMSetupImport.csproj
 2.Controller.cs
 3.GeometryImporter.cs
 4.Importer.cs
 5.MatrixHelper.cs
 6.MessageUtils.cs
 7.ResourcesExtensions.cs
 8.SetupPartExtensions.cs
 9.SimulationApi.xsd
 10.SimulationApi.cs
 11.Utils.cs

 All the above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/CAMSetupImport
 
-----------
Build Steps
----------- 

 Windows
 ---------
   1. Open Microsoft Visual Studio .Net.
   2. Open up the C# project CAMSetupImport.csproj
   3. Add the following references,
   3.1. NXOpen.dll 
   3.2. NXOpen.Utilities.dll
   3.3. NXOpenUI.dll
        To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
        Go to %UGII_BASE_DIR%\nxbin\managed.  Select and add the DLL's one after the other.
      Set the copy local attribute for these DLLs to be false so you always use the versions from the NX install.  		
   4. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
      right click on project name and select Build.
   5. This will create an executable called CAMSetupImport.dll in the Release or Debug  directory as per selected configuration.
   
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
 
--------------------------
Example execution steps
--------------------------
  
  1. Start NX.
    
  2. Go to Task -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog. Navigate to CAMSetupImport.dll file.

  3. Open File Dialog appears. Navigate to the xml file containing the cam setup import information.
    3.1. An example xml file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/CAMSetupImport/sample/sim01.XML


  4. When the Work in Progress dialog disappears the execution is complete and the created cam setup can be saved.

  5. The cam setup can be executed immediately:
        Menu -> Tools -> Simulate Machine Code File...
  
  
-----
Note:
-----
  "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
  
     
    
    
       



