--------------------------------------------------------------------------------

  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.

 
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
                            SOAConnectionExample
--------------------------------------------------------------------------------

-------------
Description:
-------------
This example is designed to show how to create a SOA connection with a
Teamcenter Server and then get some information by making server calls.

1. Initialize a UGManager session using Open C API UF_UGMGR_initialize().
2. Get the Tcserver Connect String and Discriminator.
3. Create a new SOA connection using the Connect String.
4. Log in to the connection by supplying username and password.
5. Make server calls and output the contents of the user's Home folder.
6. Make server calls and output a query result.
7. Logout of the connection.
8. Terminate the UGManager session using Open C API UF_UGMGR_terminate().


----------------
Files required:
----------------

   Example files
   --------------
   1. SOAConnectionExample_AppCredentialManager.cpp
   2. SOAConnectionExample_AppCredentialManager.hpp
   3. SOAConnectionExample_AppSession.cpp
   4. SOAConnectionExample_AppSession.hpp
   5. SOAConnectionExample_HomeFolder.cpp
   6. SOAConnectionExample_HomeFolder.hpp
   7. SOAConnectionExample_Query.cpp
   8. SOAConnectionExample_Query.hpp
   9. SOAConnectionExample.cpp

   Example files listed above are located at $(UGII_BASE_DIR)/ugopen/SampleNXOpenApplications/C++/SOAConnectionExample

   Teamcenter SOA include header files
   ------------------------------------
   The include header files in zipped format are located at $(UGII_BASE_DIR)/ugmanager/soa/TcSoaIncludes.zip

   Teamcenter SOA libraries (for Windows only)
   --------------------------------------------
   The libraries (.lib files) in zipped format are located at $(UGII_BASE_DIR)/ugmanager/soa/TcSoaLibs.zip

   makefile (for Linux only)
   --------------------------
   1. SOAConnectionExample_makefile

   The above makefile is located at $(UGII_BASE_DIR)/ugopen/SampleNXOpenApplications/C++/SOAConnectionExample


-------------
Build steps:
-------------

   Windows
   --------
    1. Using Visual Studio - create a new project named "SOAConnectionExample" using the NX Open AppWizard
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
    5. Add all the example files (.cpp and .hpp) files to the project
        - Copy all the example files (.cpp and .hpp files) to the project folder
        - Go to the Project pulldown and select "Add Existing Item..."
        - Select all the .cpp and .hpp files using the popup window
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

    This will create an executable called SOAConnectionExample.exe in the project.

   Linux
   ------
    1. Start up an NX command prompt window
    2. Create a new directory named "project"; 'cd' to this directory
    3. Copy all the necessary files to this directory
        - Copy all the example files (.cpp and .hpp files)
        - Copy the makefile SOAConnectionExample_makefile
        - Create a new directory named "soa_includes"
        - Unzip the TcSoaIncludes.zip to the "soa_includes" directory
    4. Ensure the following environment variables are set
          i. UGII_BASE_DIR - this should be set to the NX installation directory
         ii. LD_LIBRARY_PATH - this should be set to $(UGII_BASE_DIR)/ugii
        iii. UGII_USERFCN - this should be set to $(UGII_BASE_DIR)/ugii
    5. Build using the makefile, by running the below command:
            make -f SOAConnectionExample_makefile

    This will create an executable called SOAConnectionExample in the current directory.


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
   called SOAConnectionExample.exe.

   1. Execution through Visual Studio:
        i. Add the arguments to the project. Go to Project->Properties... (Alt + F7),
           select/expand Configuration Properties->Debugging.
           Add "-pim=yes -u=username -p=password" to Command Arguments.
       ii. Click on Debug->Start or Start icon.

   2. Execution using executable:
        i. From an NX command prompt window give the command:
             SOAConnectionExample.exe -pim=yes -u=<username> -p=<password>

   The program will prompt for the username and password for creating the new SOA connection.
   The contents of the Home folder will be output on the console wondow.
   The query results will be output on the console window.

   Linux
   ------
   Once you have successfully finished with "How to build" steps, it will create executable
   called SOAConnectionExample.

   1. Execution using executable:
        i. From an NX command prompt window give the command:
             ./SOAConnectionExample -pim=yes -u=<username> -p=<password>

   The program will prompt for the username and password for creating the new SOA connection.
   The contents of the Home folder will be output on the console wondow.
   The query results will be output on the console window.


------
Note:
------
NXOpen application must be signed before its release. If not signed the application may not get executed.
For more details on signing the application refer to NXOpen Programmer's Guide.

