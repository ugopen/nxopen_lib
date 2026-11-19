=============================================================================
Copyright 2018 Siemens Product Lifecycle Management Software Inc.
All Rights Reserved.


========================================================================
        TeamcenterIntegrationCreatePartWithRequiredAttributes
========================================================================

Description:
------------
This is an example to show how to create a part in NX with item type that has
required attributes defined in Teamcenter. These attributes must be specified
to be able to create part.

We will be using OOTB Business Object with name "CAE0Config"
"CAE0Config" has Display name "CAE Configuration"

It has two extra required attributes :
1) "Item:revision:ItemRevision:cae0ConfigType"
2) "Item:revision:ItemRevision:cae0VisibleScope"

other than the default required attributes for Item : "DB_PART_NO", "DB_PART_REV", "DB_PART_NAME"

TC Business Object Properties are Attributes in NX Terminology

In our example all our required attributes on "CAE0Config" are of type String,
    So we are not explicitly checking attribute type here before assignment
    But user may have integer, boolean, real etc. attributes. 
    And corresponding type values of AttributeInformation Struct should be updated for assignment

By assigning values to the required attributes we are going to create Item of type "CAE0Config" in Teamcenter 

Steps:
 * Initialize a UGManager session using Open C API UF_UGMGR_initialize().
 * Get NX Open Session and NX Open PDM Session objects
 * Create PartOperationCreateBuilder
 * Using  PartOperationCreateBuilder Create LogicalObject for TC-Business Object "CAE0Config"
 * The LogicalObject has associated  UserAttributeSourceObjects which store actual attributes
 * From LogicalObject get UserAttributeSourceObjects, which store the actual attributes for it
 * UserAttributeSourceObjects is asked to return attributes which include unset attributes
 * From Attributes filter out the required Attributes for assignment of value
 * For required attributes set the desired values
 * Validate and commit LogicalObject
 * Terminate the UGManager session using Open C API UF_terminate().

Files Required: 
---------------
    TeamcenterIntegrationCreatePartWithRequiredAttributes.cpp
    located at $(UGII_BASE_DIR)/ugopen/SampleNXOpenApplications/CPP/TeamcenterIntegrationCreatePartWithRequiredAttributes

Build Steps:
------------
    Windows:
    --------
    1. Using Visual Studio - create a new project named "TeamcenterIntegrationCreatePartWithRequiredAttributes" using the NX Open AppWizard
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

    7. In the Property window, in Configuration Properties->C/C++, add the following options:
          i. Under "Code Generation", set "Runtime Library" to "Multi-Threaded DLL (/MD)"
         ii. Under "Language", set "Enable Run-Time Type Information" to "Yes (/GR)"

    8. Build the executable by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution"

    This will create an executable called TeamcenterIntegrationCreatePartWithRequiredAttributes.exe in the project.


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
   called TeamcenterIntegrationCreatePartWithRequiredAttributes.exe.

   1. Execution through Visual Studio:
        i. Add the arguments to the project. Go to Project->Properties... (Alt + F7),
           select/expand Configuration Properties->Debugging.
           Add "-pim=yes -u=username -p=password" to Command Arguments.
       ii. Click on Debug->Start or Start icon.

   2. Execution using executable:
        i. From an NX command prompt window give the command:
             TeamcenterIntegrationCreatePartWithRequiredAttributes.exe -pim=yes -u=<username> -p=<password>

------
Note:
------
NXOpen application must be signed before its release. If not signed the application may not get executed.
For more details on signing the application refer to NXOpen Programmer's Guide.
