========================================================================
'
'             Copyright (c) 2004  UGS PLM Solutions
'               Unpublished - All rights reserved
'
========================================================================
Description:
-----------
This NX Open example demonstrates the use of NXOpen using Managed C++ (.NET).  
The example opens a listing window with a text line.

To build this example:
---------------------
- Open up the project (ManagedC++.vcproj) in Visual Studio.
- Add references to NXOpen.dll, NXOpen.UF.dll,and NXOpen.Utilities.dll. 
  To do this, right click on
  "References" under the ManagedC++ project in Solution Explorer. Pick "Add
  Reference..." and then navigate to the location of the dlls. These dlls
  can be found in %UGII_ROOT_DIR%\managed.  These will be copied locally as they 
  are added to the reference list.
- Build the project using Build - Build Solution and hit OK.
- The default location for the newly created ManagedC++.dll that is created is in a 
  subdirectory called Debug.


To run this example:
-------------------
Note: you will need a .NET authoring license to run the example. See
the online documentation for details of licensing.

- Start NX.
- Go to File - Execute - NX Open or type Ctrl-U to open the "Execute NXOpen" dialog 
- Navigate to ManagedC++.dll and press OK. 

A listing window containing the text, "Running C++ the Sample Application" will
appear.

