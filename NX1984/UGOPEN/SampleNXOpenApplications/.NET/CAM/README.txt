==================================================================================

             Copyright (c) 2010  Siemens PLM Software
               Unpublished - All rights reserved

  

==================================================================================
APPLICATION: OntSelectionBoilerPlate Overview
==================================================================================

Purpose of this Example: 
-------------------------
The files in this folder are sample CAM programs. They can be run as is, 
but they are intended to be examples that you can modify for your own use. 
These are run from within an interactive NX session.

These programs show how to modify CAM objects selected in the Operation 
Navigator, cycle all objects and edit only specific types and subtypes, 
and how to modify an object provided by a CAM Wizard.

Each file contains a description of its function and use, and has comments 
throughout the file to guide you in adapting the program for your use.


Steps followed in this Example:
------------------------------

--None--

How to Build
------------

   Windows
   -------
      1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the NX Open for C/C++ -> Open C Reference Guide -> 
      Overview -> setting up your system.  The image being created is an external
      User Function program using C++ and Open C++ calls.
   2. Make sure configuration type of the project is Dynamic Library (.dll) . Go to 
      Project->Properties (Alt + F7), select/expand Configuration Properties->General and set
      the "Configuration type" to Dynamic Library (.dll).
   3. Make sure the output file is generated with extension .dll. Go to 
      Project->Properties (Alt + F7), select/expand Configuration Properties->Linker and set the
      "Output File" with the .dll extension.
   4. Add the OntSelectionBoilerPlate.cpp file by selecting the Project
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
      This will create an Dynamic Library called OntSelectionBoilerPlate.dll in the Debug directory.

   The uflink tool can also be used to create the Dynamic Library by following these steps:
   
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
      uflink ufdll=OntSelectionBoilerPlate.dll
      This will create OntSelectionBoilerPlate.dll in the current directory.

   Unix
   -------
    --NA--

How to Run
----------

   Windows
   -------
   CAM programs are run from within an interactive NX session. Comments in the program will help you    
   throughout the file to guide you in adapting the program for your use.
   Select operations or groups in the Operation Navigator & Run program.
   To run the program goto main menu File->Execute->NXopen, and select 
   the OntSelectionBoilerPlate.dll file. It will modify CAM objects selected in the Operation 
   Navigator, cycle all objects and edit only specific types and subtypes, 
   and modify an object provided by a CAM Wizard.

   Unix
   -------
   --NA--
