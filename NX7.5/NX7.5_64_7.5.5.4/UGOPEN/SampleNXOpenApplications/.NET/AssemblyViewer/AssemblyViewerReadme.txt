-------------------------------------------------------------------------------


          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                    	   AssemblyViewer Example
-------------------------------------------------------------------------------


Description:
------------
This example demonstrates the use of the NXOpen Assemblies
namespace. It provides a Windows Form which displays a simple tree
view of the current displayed part.


To build this example:
---------------------
- Open up the C# project (AssemblyViewer.csproj) in Visual Studio.
- Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll. 
  To do this, right click on
  "References" under the AssemblyViewer project in Solution Explorer. Pick "Add
  Reference..." and then navigate to the location of the dlls. These dlls
  can be found in %UGII_ROOT_DIR%\managed.
- Build the project using Build - Build Solution and hit OK.
- The default location for the newly created AssemblyViewer.dll that is created is in a 
  subdirectory called obj\Debug.




To run this example:
-------------------
Note: you will need a .NET authoring license to run the example. See
the online documentation for details of licensing.

- Start NX.
- Open an assembly. A simple toy car assembly is provided in the
  sample directory.
- Type Ctrl-U to open the "Execute NXOpen" dialog.
- Navigate to AssemblyViewer.dll and press OK. 

- Selecting a component will cause it to be highlit. You also have
  the option to highlight all similar components. For example, if you
  select the LEFT_WHEEL component of the FRONT_AXLE subassembly.
  then the corresponding LEFT_WHEEL in the REAR_AXLE will also be highlit.

- To change to color of the selected Component, chose a color from
  the combo box and press the "Set Color" button. Note that this
  operation will only apply to the single Component object that was
  selected.


Enhancements
------------

- Add the ability to select a Component from the screen as well as
  from the tree view

- Add a popup menu to the tree view

- Add additional functionality. E.g. ReplaceReferenceSet() or
  MoveComponent()
