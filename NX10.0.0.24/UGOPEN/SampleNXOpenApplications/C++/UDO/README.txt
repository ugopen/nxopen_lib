-------------------------------------------------------------------------------

              Copyright (c) 2012  Siemens PLM Software
                Unpublished - All rights reserved


   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
		         Creates a very Simple UDO example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates each of the following callbacks: 
 * Display 
 * Selection 
 * Attention Point 
 * Fit 
 * Edit 
 * Information 


--------------
Files required
--------------

 1. SimpleUDO.cpp  
 
------------
Build Steps
------------
 Windows
 -------
   1. Open Microsoft Visual Studio.

	2. Create a new Visual C++ project using the NX Open AppWizard. 
	Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Visual C++ Project using the NX Open AppWizard, Class Library Application, Enter name as SimpleUDO. Click Next.
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL) and Select language C++, Click Next. 
        2.4 Select to activate the application automatically and to unload the application when NX session terminates. Click Finish.

   2. Remove all the existing files from project.
   
   3. Add the SimpleUDO.cpp to Source Files. 
      by selecting the Project pull down and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called SimpleUDO.dll in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:

      ufcomp SimpleUDO.cpp
      uflink UFDLL=SimpleUDO.dll

   This will create SimpleUDO.dll in the current directory.

  
 Linux
 ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select “y” for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => SimpleUDO.
   7. Do not add any subroutines or libraries.
       
   This will create SimpleUDO.so in the current directory.

   Exit out of ufmenu.
   
----------------------------
Settings before Launching NX
----------------------------
   -NA-

----------------------------
Settings after Launching NX
----------------------------
   1. Change the Role to Advanced if not set.
   
--------------------------
Example execution steps
--------------------------

 Once you have successfully finished with "Build Steps", 
    follow the steps below:

        2.1 Start NX.
  
        2.2 Invoke Shared Library SimpleUDO.dll through  File->Execute->NX Open Menu (Ctrl+U).
       
        2.3 First it will display information window with message "Registering C++ UDO Class" 
            and then it launch the New Screen Position dialog, which ask for screen position, 
            Click on screen.
	        It will create the new C++ UDO Class Example.
        
-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
