-------------------------------------------------------------------------------


          Copyright 2018 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.


-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                            CreateSimulationIni Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates the use of the NX Automation API in conjunction with
creating a to_ini.ini for the machine code simulation. The example uses tool and MCS functionality to create 
a file which contains the tooldata and zero offsets.


--------------
Files required
--------------
 1.CreateSimulationIniFile.csproj
 2.IniProgram.cs
 3.Program.cs
 4.ToolObject.cs
 5.GeometryObject.cs


 All the above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/CreateSimulationIniFileCS
 
-----------
Build Steps
----------- 

 Windows
 ---------
   1. Open Microsoft Visual Studio .Net.
   2. Open up the C# project CreateSimulationIniFile.csproj
   3. Add the following references,
   3.1. NXOpen.dll 
   3.2. NXOpen.Utilities.dll
      To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
      Go to %UGII_BASE_DIR%\nxbin\managed.  Select and add the DLL's one after the other.
	  Set the copy local attribute for these DLLs to be false so you always use the versions from the NX install.
   4. Add the signing process in the Build Events:
   4.1. Right Mouse Button -> MachineControlPanel -> Properties, Build Events
   4.2. Add following command in the Post-build event command line:
        "<NX install dir>\NXBIN\SignDotNet" $(TargetPath)
   4.3. Update in the file MachineControlPanelAssemblyInfo.cs the entry AssemblyVersion and AssemblyFileVersion
        to reflect the proper version.
   5. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
      right click on project name and select Build.
   6. This will create an executable called CreateIniFile.dll in the Release or Debug directory as per selected configuration.
   
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
     Journal execution
     ------------------
     -NA-
        
     Shared Library execution
     ------------------------  
  1. Start NX.
  2. Open a part file, go to Start -> Manufacturing
  3. Start the CreateIniFile.dll with Ctrl+U or from the menu
  
-----
Note:
-----
  "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
  
 	 
	
	
       



