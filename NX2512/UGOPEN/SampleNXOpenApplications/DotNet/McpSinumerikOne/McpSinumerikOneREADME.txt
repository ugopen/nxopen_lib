-------------------------------------------------------------------------------

            Copyright (c) 2022  Siemens Industry Software
                     All rights reserved


-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                            McpSinumerikOne Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates the use of the NX Open Automation API in conjunction
with Winforms. The example uses simulation functionality to create machine
control panel (MCP) by the user via a Winform. This MCP is tailored for the use
together with Sinumerik One machines only and considers the special
requirements like writing PLC IOs.

--------------
Files required
--------------
 1.McpSinumerikOne.vbproj
 2.McpSinumerikOne.vb
 3.McpSinumerikOneMain.vb
 4.McpSinumerikOne.Designer.vb
 5.McpSinumerikOne.resx
 6.McpSinumerikOneAssemblyInfo.vb
 7.NXSigningResource.res
 
 All the above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/DotNET/McpSinumerikOne
 
-----------
Build Steps
----------- 

 Windows
 ---------
   1. Open Microsoft Visual Studio .Net.
   2. Create an empty solution and add the existing project McpSinumerikOne.vbproj
   3. Add the following references,
   3.1. NXOpen.dll 
   3.2. NXOpen.Utilities.dll
      To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
      Go to %UGII_BASE_DIR%\nxbin\managed.  Select and add the DLL's one after the other.
      Set the copy local attribute for these DLLs to be false so you always use the versions
      from the NX install.
   4. Add the signing process in the Build Events:
   4.1. Right Mouse Button on the McpSinumerikOne project node in the solution explorer
        -> Properties. Open tab Compile. Click on button Build Events... in the lower right corner.
   4.2. Add / Adjust the following command in the Post-build event command line:
        "<NX install dir>\NXBIN\SignDotNet.exe" $(TargetPath)
   4.3. Update in the file McpSinumerikOneAssemblyInfo.vb the entry AssemblyVersion and
        AssemblyFileVersion to reflect the proper version.
   5. Enable debugging of the source code of the DLL.
   5.1. Set as start action the launch of NX.
        Right Mouse Button on the McpSinumerikOne project node in the solution explorer
        -> Properties. Open tab Debug. Select in section "Start action" the radio button
        "Start external program:" and browse for ugraf.exe in your <NX install dir>.
   5.2. Activate the native code debugging.
        Right Mouse Button on the McpSinumerikOne project node in the solution explorer
        -> Properties. Open tab Debug. In section "Debugger engines" set the checkbox
        "Enable native code debugging".
   6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
      right click on project name and select Build.
   7. This will create a DLL called mcp_SinumerikOne.dll in the bin/Release or bin/Debug directory
      as per selected configuration.
   
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
  1. Add the MCP_FILE keyword in the machine dat file in the
     ${UGII_CAM_LIBRARY_INSTALLED_MACHINES_DIR}MyMachine for example: 
     MCP_FILE, ${UGII_CAM_LIBRARY_INSTALLED_MACHINES_DIR}MyMachine\cse_driver\mcp_SinumerikOne.dll
  2. Copy the mcp_SinumerikOne.dll to the path that is defined by MCP_FILE keyword
     in the machine dat file
  3. Start NX manually (or from the Visual Studio with F5).
  4. Open the part file, go to Start -> Manufacturing
  5. Click on Simulate Machine and switch to: "Virtual Controller Program Simulation" or
     "External Program Simulation".
     or
     Select any operation in ONT and select "Machine Code Based Simulation"

  
-----
Note:
-----
 "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
