--------------------------------------------------------------------------------

  Copyright 2014 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.

 
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
                            SOAConnectionExample2
--------------------------------------------------------------------------------

-------------
Description:
-------------
This example is designed to show how to obtain a pointer to the SOA connection
that UGManager session is using.

1. Initialize a UGManager session using Open C API UF_UGMGR_initialize().
2. Using NXOpen API, obtain a pointer to the SOA connection that NX is using.
3. Print information about the connection.
4. Terminate the UGManager session using Open C API UF_UGMGR_terminate().


----------------
Files required:
----------------

   Example files
   --------------
   1. SOAConnectionExample2.cpp

   Example file listed above is located at $(UGII_BASE_DIR)/ugopen/SampleNXOpenApplications/C++/SOAConnectionExample2

   Teamcenter SOA include header files
   ------------------------------------
   The include header files in zipped format are located at $(UGII_BASE_DIR)/ugmanager/soa/TcSoaIncludes.zip

   Teamcenter SOA libraries (for Windows only)
   --------------------------------------------
   The libraries (.lib files) in zipped format are located at $(UGII_BASE_DIR)/ugmanager/soa/TcSoaLibs.zip

   makefile (for Linux only)
   --------------------------
   1. SOAConnectionExample2_makefile

   The above makefile is located at $(UGII_BASE_DIR)/ugopen/SampleNXOpenApplications/C++/SOAConnectionExample2


-------------
Build steps:
-------------

   Windows
   --------
    1. Using Visual Studio - create a new project named "SOAConnectionExample2" using the NX Open AppWizard
        - This is described in the NX Open for C/C++ -> Open C Reference Guide -> Overview -> setting up your system
        - Ensure that the image being created is an external User Function program
    2. Make sure configuration type of the project is Application (.exe)
        - Go to Project->Properties... (Alt + F7), select/expand Configuration Properties->General
        - The "Configuration type" should be set to Application (.exe)
    3. Make sure the output file is generated with extension .exe
        - Go to Project->Properties... (Alt + F7), select/expand Configuration Properties->Linker
        - The "Output File" should be set with .exe extension
    4. Remove the cpp file automatically created by the AppWizard
        - Select the file in Solution Explorer
        - Go to Project pulldown and select "Exclude From Project"
    5. Add the example file to the project
        - Copy the example file to the project folder
        - Go to the Project pulldown and select "Add Existing Item..."
        - Select the .cpp file using the popup window
    6. Add $(UGII_BASE_DIR)\ugopen and the folder containing the SOA include header files as the include directories
        - In the project folder, create a new folder named "soa_includes"
        - In the "soa_includes" folder, copy the TcSoaIncludes.zip and unzip it
        - Go to Project->Properties... (Alt + F7), select/expand Configuration Properties->C/C++
        - On right side window select "Additional Include Directories" pulldown
        - Add $(UGII_BASE_DIR)\ugopen and the "soa_includes" folder to the existing list
    7. In the Property window, in Configuration Properties->C/C++, add the following options:
          i. Under "Preprocessor", add "IPLIB=none" to the "Preprocessor Definitions"
         ii. Under "Code Generation", set "Runtime Library" to "Multi-Threaded DLL (/MD)"
        iii. Under "Language", set "Enable Run-Time Type Information" to "Yes (/GR)"
         iv. Under "Command Line", in "Additional Options", add /FI"soa_includes\msvcpragmas.h"
    8. Add the folder containing the SOA libraries (.lib files) as additional library directory
        - In the project folder, create a new folder named "soa_libs"
        - In the "soa_libs" folder, copy the TcSoaLibs.zip and unzip it
        - Go to Project->Properties... (Alt + F7), select/expand Configuration Properties->Linker->General
        - Add the "soa_libs" folder to the "Additional Library Directories"
    9. Add the service libraries that this example depends on as additional dependencies
        - Go to Project->Properties... (Alt + F7), select/expand Configuration Properties->Linker->Input
        - Add the following to the "Additional Dependencies": libtcsoacommon.lib libtcsoaclient.lib
          libtcsoacorestrong.lib libtcsoaquerystrong.lib
   10. Build the executable by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution"

    This will create an executable called SOAConnectionExample2.exe in the project.

   Linux
   ------
    1. Start up an NX command prompt window
    2. Create a new directory named "project"; 'cd' to this directory
    3. Copy all the necessary files to this directory
        - Copy the example file
        - Copy the makefile SOAConnectionExample2_makefile
        - Create a new directory named "soa_includes"
        - Unzip the TcSoaIncludes.zip to the "soa_includes" directory
    4. Ensure the following environment variables are set
          i. UGII_BASE_DIR - this should be set to the NX installation directory
         ii. LD_LIBRARY_PATH - this should be set to $(UGII_BASE_DIR)/ugii
        iii. UGII_USERFCN - this should be set to $(UGII_BASE_DIR)/ugii
    5. Build using the makefile, by running the below command:
            make -f SOAConnectionExample2_makefile

    This will create an executable called SOAConnectionExample2 in the current directory.


---------------------------
Settings before execution:
---------------------------
Set the following environment variables specific to the database:

   1. UGII_UGMGR_COMMUNICATION=HTTP
        This is required to initialize the communication with Teamcenter over the web in four-tier environment

   2. UGII_UGMGR_HTTP_URL=<URL>
        The URL is required to specify the Teamcenter web server and the application name of the web server in four-tier environment

The four tier services must be started and available on the network.


-----------------
Execution steps:
-----------------

   Windows
   --------
   Once you have successfully finished with "How to build" steps, it will create executable
   called SOAConnectionExample2.exe.

   1. Execution through Visual Studio:
        i. Add the arguments to the project. Go to Project->Properties... (Alt + F7),
           select/expand Configuration Properties->Debugging.
           Add "-pim=yes -u=username -p=password" to Command Arguments.
       ii. Click on Debug->Start or Start icon.

   2. Execution using executable:
        i. From an NX command prompt window give the command:
             SOAConnectionExample2.exe -pim=yes -u=<username> -p=<password>

   Some information from the SOA connection will be output on the console wondow.

   Linux
   ------
   Once you have successfully finished with "How to build" steps, it will create executable
   called SOAConnectionExample2.

   1. Execution using executable:
        i. From an NX command prompt window give the command:
             ./SOAConnectionExample2 -pim=yes -u=<username> -p=<password>

   Some information from the SOA connection will be output on the console wondow.


------
Note:
------
NXOpen application must be signed before its release. If not signed the application may not get executed.
For more details on signing the application refer to NXOpen Programmer's Guide.

