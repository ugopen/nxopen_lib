'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

-------------------------------------------------------------------------------
		Block Styler MatrixOperations Example
-------------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates usage of Block Styler Application in NX.
The set of APIs designed for Block Styler application are property based. While using 
these APIs one must be aware about the Block, its associated properties and their datatype.
This program uses various UI Blocks like 

DoubleTable, 
Enumeration, 
Double, 
Toggle,   
SpecifyVector, 
AngularDim.

This example also illustrates the usage of DoubleTable with respect to Matrix Operations
using UFunc Open API matrix functions in conjunction with NXOpen C++ API.

--------------
Files required
--------------

    1. MatrixOperations.cpp
    2. MatrixOperations.hpp
    3. MatrixOperations.dlx 

The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/MatrixOperations.


------------
Build Steps
------------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NXOpen AppWizard.
      This is described in the Automation -> NXOpen -> Open for C/C++ ->
	  Open C Reference Guide -> Overview -> Setting up your system -> Windows Operating System Setup. 
      When setting the Application Settings, select "Create an Internal application" 
      and select C++ as the language. 

   2. Remove all the existing files from project.
   
   3. Add the  MatrixOperations.cpp, MatrixOperations.hpp to Source Files and Header Files respectively 
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called  MatrixOperations.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp  MatrixOperations.cpp
      uflink UFDLL= MatrixOperations.dll

   This will create  MatrixOperations.dll in the current directory.

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link =>  MatrixOperations
   7. Do not add any subroutines or libraries.
       
   This will create  MatrixOperations.so in the current directory.

   Exit out of ufmenu.

----------------------------
Settings before Launching NX
----------------------------
The dlx file must be placed in one of the following locations:
   1. From where NX session is launched
   2. $UGII_USER_DIR/application
   3. For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

----------------------------
Settings after Launching NX
----------------------------
   1. Change the Role to Advanced if not set.

-----------------------
Example execution steps
-----------------------
    1. Start NX.

    2. Create new part.

    3. Invoke  MatrixOperations.dll ( MatrixOperations.so on Linux) file using  File->Execute->NX Open... menu command.

    4. The above step will launch  MatrixOperations dialog.

    5. Then the Dialog will allows you to perform Matrix Operations like 

	5.1  Multiplication 
	5.2  Addition 
	5.3  Determinant
	5.4  Transpose
	5.5  OrthoNormalize
	5.6  RotateAboutAxis
	5.7  VectorMultiply
	5.8  X-direction Vector
	5.9  Y-direction Vector
    5.10 Z-direction Vector
	
-----
Note:
-----
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	 
 
