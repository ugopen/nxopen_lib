========================================================================
'
'  Copyright 2011 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
========================================================================
Description:
-----------
This NX Open example demonstrates the use of NXOpen using Managed C++ (.NET).  
The example opens a listing window with a text line.

To build this example:
---------------------
- Open up the project (ManagedCpp.vcproj) in Visual Studio.
- Add references to NXOpen.dll, NXOpen.UF.dll,and NXOpen.Utilities.dll. 
  To do this, right click on
  "References" under the ManagedC++ project in Solution Explorer. Pick "Add
  Reference..." and then navigate to the location of the dlls. These dlls
  can be found in %UGII_ROOT_DIR%\managed.  Set the copy local attribute
  for these DLLs to be false so you always use the versions from the NX install.
- Build the project using Build - Build Solution and hit OK.
- The default location for the newly created ManagedCpp.dll that is created is in a 
  subdirectory called Debug.


To run this example:
-------------------
Note: you will need a .NET authoring license to run the example. See
the online documentation for details of licensing.

- Start NX.
- Go to File - Execute - NX Open or type Ctrl-U to open the "Execute NXOpen" dialog 
- Navigate to ManagedCpp.dll and press OK. 

A listing window containing the text, "Running the C++  Sample Application" will
appear.

Signing the example:
--------------------
The NXSigningResource.res has been setup to be embedded into the dll.  So after building this example you can run the %UGII_ROOT_DIR%\SignLibrary.exe utility to sign this DLL.

To set this up for generic managed C++ solution, go to the project property pages and add the path to 'NXSigningResource.res' in: Configuration Properties -> Linker -> Input -> Embed Managed Resource File (the equivalent command-line option is /ASSEMBLYRESOURCE:file).
