-------------------------------------------------------------------------------

              Copyright (c) 2012  Siemens PLM Software
                Unpublished - All rights reserved


   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
		         Creates a very simple UDO example
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

  UDO's require registration of classes and callbacks that must remain registered
  for the entire NX session.  Therefore UDO code must always specify the unload
  option "at termination".  Likewise, these samples must be compiled before execution
  and may NEVER be run as a journal.  Journals unload immediately, and ignore the
  "at termination" unload option.  If you try to run a UDO program as a journal 
  it will register callbacks, and unload as soon as the journal completes execution.  
  NX will crash if it tries to execute a callback which is no longer available.

--------------
Files required
--------------

 1. SimpleUDO.vb (or SimpleUDO.cs if building the C# example)
	
-----------
Build Steps
-----------

Windows
-------
1. Open Microsoft Visual Studio .Net.

2. Create a new VB (or C#) project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
 	    2.2 Select Vb Project (or CSharp Project) using the NX Open AppWizard, Class Library Application, Enter name as SimpleUDO. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL). 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb (or *.cs) files from the new project by clicking MB3 on respective file and 
   clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the SimpleUDO.vb (or SimpleUDO.cs) file to the project by selecting the Project pull down and select "Add Existing Item...". 
   Select the file using the popup window.

5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an executable called SimpleUDO.dll in the Debug directory.

Linux
-------
   -NA-

----------------------------
Settings before Launching NX
----------------------------
   -NA-
   
----------------------------
Settings after Launching NX
----------------------------

 1. Change the Role to Advanced.

--------------------------
Example execution steps
--------------------------

 1. Execute the Shared Library and invoke it through File->Execute->NX Open... Menu. 
   
    Once you have successfully finished with "Build Steps" to create the shared library (dll), 
    follow the steps below:

        1.1 Start NX.
  
        1.2 Invoke Shared Library SimpleUDO.dll through  File->Execute->NX Open Menu (Ctrl+U).
		
		1.3 First it will display new pop-up message dialog "Registering VB UDO Class", click->OK.
            OR 
            If it is a C# dll then it will display Information window with message "Registering C# UDO Class".
        
        1.4 It will launch the New Screen Position dialog, which ask for screen position, Click on screen.
	        It will create the new .NET UDO Class Example.
        
-----
Note:
-----
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
