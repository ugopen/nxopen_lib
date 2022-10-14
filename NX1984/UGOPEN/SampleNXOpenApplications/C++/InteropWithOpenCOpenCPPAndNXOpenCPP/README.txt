==================================================================================

             Copyright (c) 2010  Siemens PLM Software
               Unpublished - All rights reserved

  

==================================================================================
CONSOLE APPLICATION: InteropWithOpenCOpenCPPAndNXOpenCPP Project Overview
==================================================================================

Purpose of this Example: 
-------------------------

This example is designed to show the interoperability between Open C, 
Open C++, and NX Open C++ APIs. User has to initialize, UG Session 
using Open C++ as well as NX Open C++, session also.

Specifically what we have done is,
	
	We have initialized the session and created new part using Open C++ APIs and save 
	This same part with NX Open C++ APIs and terminate the session using Open C API.
	Then in between we have created objects using NX Open C++ API and requesting 
	information for these objects using Open C APIs, used this requested information 
	to create objects using Open C++ APIs. 
	We have also created an arc using Open C++ APIs then requesting parameters using 
	NX Open C++ APIs. Saved the using NXOpen C++ APIs.

Steps followed in this Example
------------------------------
Here, we have followed the following steps:

1. Initialize the session using Open C++ API, UgSession::initialize(). 
   User has to initialize, UG Session using Open C++ as well as NX Open C++, 
   session also (NXOpen::Session::GetSession()).
2. Get the session using NX Open C++ API, NXOpen::Session::GetSession();
3. Create new part using Open C++ API, UgPart::create(), 
   So, the newly created part now is the work part. 
4. Create Line using NXOpen Automation API, CreateLine(). 
5. Requesting Line object data using Open C API, UF_CURVE_ask_line_data(). To get the tag of 
   the line, used GetTag() method on the Line object. This tag can be used with Open C APIs.
6. Create Line using Open C++ API, UgLine::create(). 
7. Create an Arc using Open C++ API, UgArc::create().
8. Request parameters of an Arc using, GetRadius(), GetStartAngle(), GetEndAngle().
9. Save the part using NXOpen automation APIs.
10. Terminate session using Open C, UF_terminate().

How to Build
------------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the NX Open for C/C++ -> Open C Reference Guide -> 
      Overview -> setting up your system.  The image being created is an external
      User Function program using C++ and Open C++ calls.
   2. Make sure configuration type of the project is Application (.exe). Go to 
      Project->Properties (Alt + F7), select/expand Configuration Properties->General and set
      the "Configuration type" to Application (.exe).
   3. Make sure the output file is generated with extension .exe. Go to 
      Project->Properties (Alt + F7), select/expand Configuration Properties->Linker and set the
      "Output File" with the .exe extension.
   4. Add the InteropWithOpenCOpenCPPAndNXOpenCPP.cpp file by selecting the Project
      pulldown and select "Add Existing Item...".  Select the file using the popup
      window.
   5. Add $(UGII_BASE_DIR)\ugopenpp as one of the include directories. Go to Tools->Options, 
      select/expand Projects and Solution->VC++ Directories. On right side window select 
      "Include files" option available under "Show Directories for:" pulldown. Add $(UGII_BASE_DIR)\ugopenpp 
      to the existing list.
   6. Add libopenpp.lib and libvmathpp.lib libraries to the project. Go to Project->Properties (Alt + F7), 
      select/expand Configuration Properties->Linker->Input. Provide libopenpp.lib and libvmathpp.lib
      in the "Additional Dependencies" row.
   7. Build the external image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
   This will create an executable called InteropWithOpenCOpenCPPAndNXOpenCPP.exe in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
      uflink ufexe=InteropWithOpenCOpenCPPAndNXOpenCPP.exe
   This will create InteropWithOpenCOpenCPPAndNXOpenCPP.exe in the current directory.

   Unix
   -------
   Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu)
   Compile and link an exernal user function program.  Answer the first question for
     linking with an "e" (Link internal/external user function (i/e):) and select "y" for 
     the next input - Link a UG/Open++ Image (y/n).  This will create an external
     user function executable which has been linked against the Open++ and C++ libraries.
  

   This will create an executable called InteropWithOpenCOpenCPPAndNXOpenCPP.

How to Run
----------

   Windows
   -------
   Once you have successfully finished with "How to build" steps, it will create executable called
   InteropWithOpenCOpenCPPAndNXOpenCPP.exe on windows in Debug folder.

   1. Executing this project thru Visual Studio :
	1. Click on Debug->Start or Start icon.

	The part file InteropWithOpenCOpenCPPAndNXOpenCPP.prt will be created in project folder. 
	Open the prt file in NX to view the output.

   2. Executing this project using executable :
	1. Execute exe file from an NX command prompt window.

	The part file InteropWithOpenCOpenCPPAndNXOpenCPP.prt will be created in "Debug" foler under project 
	directory. Open the prt file in NX to view the output.

   Unix
   -------
   Once you have successfully finished with "How to build" steps for unix, it will create executable called
   InteropWithOpenCOpenCPPAndNXOpenCPP in your current working directory.
   
   1. Execute exe file from an NX command prompt window.

      	The part file InteropWithOpenCOpenCPPAndNXOpenCPP.prt will be created in current working directory.
	Open the prt file in NX to view the output.
