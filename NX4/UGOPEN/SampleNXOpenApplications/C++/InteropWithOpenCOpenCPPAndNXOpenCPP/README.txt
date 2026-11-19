========================================================================
CONSOLE APPLICATION: InteropWithOpenCOpenCPPAndNXOpenCPP Project Overview
========================================================================

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
   1. Open Microsoft Visual Studio .Net 2003.
   2. Open InteropWithOpenCOpenCPPAndNXOpenCPP.vcproj thru File Menu->Open->Project.
   3. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Build or Rebuild OR Go to Build Menu -> Build Solution or Ctrl + Shift + B.

   Unix
   -------
   1. Copy $(UGII_BASE_DIR)/ugopen/uflink scripts locally using 
      cp $(UGII_BASE_DIR)/ugopen/uflink .
   2. Add "-lopenpp -lvmathpp" library names in variable uguserlibs at line number 74 as,
      uguserlibs="-lufun -lnxopencpp -lopenpp -lvmathpp"
   3. Run make file as "make -f InteropWithOpenCOpenCPPAndNXOpenCPP_Makefile".

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
	1. Execute exe file on command prompt.

	The part file InteropWithOpenCOpenCPPAndNXOpenCPP.prt will be created in "Debug" foler under project 
	directory. Open the prt file in NX to view the output.

   Unix
   -------
   Once you have successfully finished with "How to build" steps for unix, it will create executable called
   InteropWithOpenCOpenCPPAndNXOpenCPP in your current working directory.
   
   1. Execute exe file on prompt.

      	The part file InteropWithOpenCOpenCPPAndNXOpenCPP.prt will be created in current working directory.
	Open the prt file in NX to view the output.

