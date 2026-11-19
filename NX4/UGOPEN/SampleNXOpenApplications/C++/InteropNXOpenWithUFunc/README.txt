========================================================================
    CONSOLE APPLICATION : InteropNXOpenWithUFunc Project Overview
========================================================================

Purpose of this example : 
-------------------------

This example is designed to show the interoperability between "C" based Open C APIs and
"C++" based NX Open C++ APIs. 

The example creates a new part using Open C APIs.  The example then creates geometry 
using Open C APIs and the requests information for these objects using NX Open C++ APIs 
and vice versa.  Then, the example save this part with the NX Open C++ API.

Steps followed in this example
------------------------------
Here, we have followed the follwing steps :

1. Create new part using Open C API, UF_PART_new(). So, the newly created part now is the 
   work part. 
2. Create a line using NX Open C++ API, CreateLine(). 
3. Requesting line object data using Open C API, UF_CURVE_ask_line_data(). To get the tag of 
   the line, use Tag() method on the Line object. This tag can be used with Open C APIs.
4. Create an arc using Open C API, UF_CURVE_create_arc(). 
5. Create NX Open C++ Arc object using arc tag returned by Open C API, 
   (NXOpen::Arc*)NXOpen::NXObjectManager::Get(arc).
6. Get the arc parameters using NX Open C++ APIs.
7. Save the part using NX Open C++ APIs.

How to Build
------------
   Windows
   -------
   1. Open Microsoft Visual Studio .NET 2003.
   2. Open InteropNXOpenWithUFunc.vcproj thru File Menu->Open->Project.
   3. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Build or Rebuild OR Go to Build Menu -> Build Solution or Ctrl + Shift + B.
   This will create an executable called InteropNXOpenWithUFunc.exe in the project's "Debug" folder

   Unix
   -------
   Run make.
   This will create an executable called InteropNXOpenWithUFunc.
   
How to Run
----------
Run the executable file from the command prompt.  The example can also be run from a debugger like Visual Studio.

The example creates a part file InteropNXOpenWithUFunc.prt in the directory where the executable is located.
The part file can be opened for viewing in NX.
