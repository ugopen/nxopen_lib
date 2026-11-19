'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
						Assembly Viewer Example
------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates the use of the NX Open Assemblies
namespace. It provides a simple viewer that displays the tree structure of an assembly.
The color of the selected component can be changed by pressing the "Set Color" button.


--------------
Files required
--------------
   1. AssemblyViewer.cs 
   2. AssemblyViewer.csproj
   3. AssemblyViewerAssemblyInfo.cs
   4. toycar_assy.prt   
   5. toycar_axle.prt   
   6. toycar_axle_assy.prt  
   7. toycar_body.prt  
   8. toycar_wheel.prt  
  
  All the above mentioned files are  located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\AssemblyViewer
  Note: the UGII_BASE_DIR is expanded in the SYSLOG if the system does not recognize the environment variable.

-------------------------
Build steps
-------------------------

Windows
-------
    1. Open up the Assembly Viewer C# project (AssemblyViewer.csproj) in Visual Studio.
	
    2. Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
       To do this, right click on "References" under the Assembly Viewer project in Solution Explorer. 
       Pick "Add Reference..." and then navigate to the location of the dlls. 
       These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.
	
    3. Build the project using Build -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
       right click on project name and select Build.
	
    4. This will create an executable called AssemblyViewer.dll in the \bin\Release directory.

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
You will need a .NET authoring license to run the example. See
the online documentation for details of licensing.

     Journal execution
     ------------------
      -NA-

      Shared Library execution
      ------------------------
      1. Start NX.

      2. Open assembly toycar_assy.prt 

      3. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.

      4. Browse (to \bin\Release directory) and select the AssemblyViewer.dll and execute.

      5. Assembly Viewer will pop-up. Expand all nodes in the viewer.
         It should display the following Parts.
           ROOT
             +-SPARE_WHEEL
             +-REAR_AXLE
             |      +-TOYCAR_AXLE
             |      +-LEFT_WHEEL
             |      +-RIGHT_WHEEL
             +-FRONT_AXLE
             |      +-TOYCAR_AXLE
             |      +-LEFT_WHEEL
             |      +-RIGHT_WHEEL
             +-BODY

      6. Select any component, this will cause it to be highlight.

         When 'All Components' option is selected, all instances of the part will 
         be highlighted. For example, if you select the LEFT_WHEEL component of the
         FRONT_AXLE subassembly. Then the corresponding LEFT_WHEEL in the REAR_AXLE 
         will also be highlighted.

      7. Select the color from the combo box and press 'Set Color'. The selected 
         component will be set with the defined color.
         Note: Set color will work only for single components and not for 'All Components'

------
Notes
------
1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
   For more details on signing the application refer to NXOpen Programmer's Guide."

2. Enhancements that can be done to this example are:

    - Add the ability to select a Component from the screen as well as from the tree view
    - Add a popup menu to the tree view
    - Add additional functionality. E.g. ReplaceReferenceSet() or MoveComponent()

'=================================End=========================================
