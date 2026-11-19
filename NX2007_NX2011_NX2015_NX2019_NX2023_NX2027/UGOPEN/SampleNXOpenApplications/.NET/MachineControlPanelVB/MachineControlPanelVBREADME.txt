-------------------------------------------------------------------------------


          Copyright 2013 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.


-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                            MachineControlPanelVB Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates the use of the NX Automation API in conjunction with
Winforms. The example uses simulation functionality to create machine control panel 
by the user via a Winform.

--------------
Files required
--------------
 1.MachineControlPanel.vbproj
 2.MCP.vb
 3.Module1.vb
 4.MCP.Designer.vb
 5.MCP.resx
 6.MachineControlPanelAssemblyInfo.vb
 7.NXSigningResource.res
 
 All the above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/MachineControlPanelVB
 
-----------
Build Steps
----------- 

 Windows
 ---------
   1. Open Microsoft Visual Studio .Net.
   2. Open up the VB project MachineControlPanel.vbproj
   3. Add the following references,
   3.1. NXOpen.dll 
   3.2. NXOpen.Utilities.dll
      To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
      Go to %UGII_BASE_DIR%\nxbin\managed.  Select and add the DLL's one after the other.
     Set the copy local attribute for these DLLs to be false so you always use the versions from the NX install.	
   4. Add the signing process in the Build Events:
   4.1. Right Mouse Button -> MachineControlPanel -> Properties, Compile, Select Build Events... button
   4.2. Add following command in the Post-build event command line:
        "<NX install dir>\NXBIN\SignDotNet" $(TargetPath)
   4.3. Update in the file MachineControlPanelAssemblyInfo.vb the entry AssemblyVersion and AssemblyFileVersion
        to reflect the proper version.
   5. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
      right click on project name and select Build.
   6. This will create an executable called mcp.dll in the Release or Debug directory as per selected configuration.
   
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
  1. Add the MCP_FILE keyword in the machine dat file in the ${UGII_CAM_LIBRARY_INSTALLED_MACHINES_DIR}MyMachine
     for example: MCP_FILE, ${UGII_CAM_LIBRARY_INSTALLED_MACHINES_DIR}MyMachine\cse_driver\mcp.dll
  2. Copy the mcp.dll to the path that is defined by MCP_FILE keyword in the machine dat file
  3. Start NX.
  4. Open a vnck part file, go to Start -> Manufacturing
  5. Click on Simulate Machine and switch to: "Virtual Controller Program Simulation" or
     "External Program Simulation".
     or
     Select any operation in ONT and select "Machine Code Based Simulation"
  
-----
Note:
-----
 "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
  
 	 
	
	
       



