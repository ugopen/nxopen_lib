==================================================================================

             Copyright (c) 2010  Siemens PLM Software
               Unpublished - All rights reserved

  
==================================================================================
    CONSOLE APPLICATION : InteropNXOpenWithUFunc Project Overview
==================================================================================

Purpose of this example : 
-------------------------

This example is designed to show the interoperability between "C" based Open C APIs and
"C++" based NX Open C++ APIs. 

The example creates a new part using Open C APIs.  The example then creates geometry 
using Open C APIs and the requests information for these objects using NX Open C++ APIs 
and vice versa.  Then, the example save this part with the NX Open C++ API.

Steps followed in this example
------------------------------
Here, we have followed the following steps :

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
   1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the NX Open for C/C++ -> Open C Reference Guide -> 
      Overview -> setting up your system.  The image being created is an external
      User Function program using C++ and Open C++ calls.  Make sure you set the
      type to "An external application that runs independent of NX (EXE)" under 
      the Application Settings.
   2. Add the InteropNXOpenWithUFunc.cpp file by selecting the Project
      pulldown and select "Add Existing Item...".  Select the file using the popup
      window.
   3. Build the external image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
   This will create an executable called InteropNXOpenWithUFunc.exe in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
      uflink ufexe=InteropNXOpenWithUFunc.exe
   This will create InteropNXOpenWithUFunc.exe in the current directory.



   Unix
   -------
   Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu)
   Compile and link an external user function program.  Answer the first question for 
     linking with an "e" (Link internal/external user function (i/e):) and select "y" for
     the next input - Link a UG/Open++ image (y/n).  This will create an external
     user function executable that has been linked against the Open++ and C++ libraries.

   This will create an executable called InteropNXOpenWithUFunc.
   
How to Run
----------
Run the executable file from the NX command prompt window.  The example can also be run from a debugger like Visual Studio.

The example creates a part file InteropNXOpenWithUFunc.prt in the directory from where the executable is executed.
The part file can be opened for viewing in NX.
