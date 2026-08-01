-------------------------------------------------------------------------------


          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
                       Block Styler Colored Block Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates creation of colored block using the Block Styler C++ APIs.
The set of APIs designed for Block Styler application are property based. While using 
these APIs one must be aware about the Block, its associated properties and its data types. 
Executing this example will launch a dialog which allows you to pick the point and 
color to create a block. 

--------------
Files required
--------------
1. ColoredBlock.cpp
2. ColoredBlock.hpp
3. ColoredBlock.dlx

The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/ColoredBlock.

------------
Build Steps
------------
 Windows
 -------
   1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the Automation -> NX Open -> Open for C/C++ -> 
	  Open C Reference Guide -> Overview -> Setting up your system. 
	  When setting the Application Settings,
      select "Create an Internal application" and select C++ as the language. 

   2. Remove all the existing files from project.
   
   3. Add the ColoredBlock.cpp, ColoredBlock.hpp to Source Files and Header Files respectively 
      by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called ColoredBlock.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:

      ufcomp ColoredBlock.cpp
      uflink UFDLL=ColoredBlock.dll

   This will create ColoredBlock.dll in the current directory.

  
   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => ColoredBlock.
   7. Do not add any subroutines or libraries.
       
   This will create ColoredBlock.so in the current directory.

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
   
   3. Go to File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog. Navigate to ColoredBlock.dll(ColoredBlock.so under Linux)file.
    
   4. It will launch the ColoredBlock dialog; Enter the Block parameter for the Height, Width, Length of the Block, Specify block origin and color of the Block as per the user's Interest.
	  It will create the new ColoredBlock at the specified Location.
	  
-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."	  
            
