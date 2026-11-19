-------------------------------------------------------------------------------


          Copyright 2013 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.


-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                            MachineControlPanelCS Example
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
 1.MachineControlPanel.csproj
 2.MCP.cs
 3.Program.cs
 4.MCP.Designer.cs
 5.MCP.resx

 All the above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/MachineControlPanelCS
 
-----------
Build Steps
----------- 

 Windows
 ---------
   1. Open Microsoft Visual Studio .Net.
   2. Open up the C# project MachineControlPanel.csproj
   3. Add the following references,
   3.1. NXOpen.dll 
   3.2. NXOpen.Utilities.dll
        To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
        Go to %UGII_BASE_DIR%\nxbin\managed.  Select and add the DLL's one after the other.
	  Set the copy local attribute for these DLLs to be false so you always use the versions from the NX install.  		
   4. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
      right click on project name and select Build.
   5. This will create an executable called mcp.dll in the \obj\Release directory.
   
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
  2. copy the mcp.dll to the path that is defined by MCP_FILE keyword in the machine dat file
  3. Start NX.
  4. Open a vnck part file, go to Start -> Manufacturing
  5. Select any operation in ONT and RMB->Tool Path->Simulate and switch to the Visualization: Machine Code Simulation
     or Select Tools->Simulate VNCK Internal Program
  
-----
Note:
-----
  "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
  
 	 
	
	
       



