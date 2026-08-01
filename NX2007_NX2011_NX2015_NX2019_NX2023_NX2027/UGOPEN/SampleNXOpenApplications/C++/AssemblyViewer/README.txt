'===============================================================================
'
'       Copyright 2010 Siemens Product Lifecycle Management Software Inc.
'                           All Rights Reserved.
'
'  
'=================================================================================

----------------------------------------------------------------------------------
        		                  Assembly Viewer Example
----------------------------------------------------------------------------------

-------------------
Example Description
-------------------
This example demonstrates the usage of tree list to view assembly structure.
The example displays tree structure of an assembly in the tree list of a Block Styler UI dialog.
Enables user to select the components and change its color. The component selection is allowed through both tree list nodes and NX graphic region. 

--------------
Files required
--------------

    1. AssemblyViewer.cpp
    2. AssemblyViewer.hpp
    3. AssemblyViewer.dlx 
	4. toycar_assy.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/AssemblyViewer)
    5. toycar_axle.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/AssemblyViewer)
    6. toycar_axle_assy.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/AssemblyViewer)
    7. toycar_body.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/AssemblyViewer)
    8. toycar_wheel.prt (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/AssemblyViewer)	
	
The above listed files are located at
$UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/AssemblyViewer.


-----------
Build Steps
-----------

   Windows
   -------
   1. Using Visual studio - create a new project using the NXOpen AppWizard.
      This is described in the Automation -> NXOpen -> Open for C/C++ -> 
	  Open C Reference Guide -> Overview -> Setting up your system -> Windows operating system setup. 
      When setting the Application Settings, select "Create an Internal application" 
      and select C++ as the language. 
   2. Remove all the existing files from project.
   3. Add the AssemblyViewer.cpp, AssemblyViewer.hpp to Source Files and Header files respectively 
      by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.
   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
   This will create an executable called AssemblyViewer.dll in the 'Debug' directory.
 
 The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
	
      ufcomp AssemblyViewer.cpp
      uflink UFDLL=AssemblyViewer.dll

   This will create AssemblyViewer.dll in the current directory.

   Linux
   -----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select "y" for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => AssemblyViewer
   7. Do not add any subroutines or libraries.
       
   This will create AssemblyViewer.so in the current directory.

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
	  1. Open assembly toycar_assy.prt.
      2. Invoke AssemblyViewer.dll( AssemblyViewer.so on Linux) file using  File->Execute->NXOpen... menu command.
      3. Browse and select the AssemblyViewer.dll and execute.
      4. Assembly Viewer will pop-up. Expand all nodes in the tree list.
         It should display the following Parts.
           ROOT
             +-SPARE_WHEEL
             +-REAR_AXLE
             |      +-LEFT_WHEEL
             |      +-RIGHT_WHEEL
             |      +-TOYCAR_AXLE
             +-FRONT_AXLE
             |      +-LEFT_WHEEL
             |      +-RIGHT_WHEEL
             |      +-TOYCAR_AXLE
             +-BODY
      5. Select any number of components, either through nodes selection on the tree list 
		 or through graphic region, and as a result the selected components will be highlighted.
		 Select "All Component" enum option to highlight all the instances of the part, 
		 e.g.,if the LEFT_WHEEL of FRONT_AXLE subassembly is selected then the corresponding LEFT_WHEEL of REAR_AXLE will also get highlighted. 
      6. Select the color from the color picker and press 'Set Color'. The selected 
         component will be set with the defined color.	 	
		 
-----------------------
Notes
-----------------------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
	
	
