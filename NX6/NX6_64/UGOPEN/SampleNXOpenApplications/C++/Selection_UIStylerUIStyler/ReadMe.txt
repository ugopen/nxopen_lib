-------------------------------------------------------------------------------
		UIStyler Selection Example
-------------------------------------------------------------------------------


Description:
------------
This example demonstrates the Selection capability of NXOpen UIStyler.
Running this example will launch a dialog which creates Edge Blend on the selected edges.

---------------------------------------
How to Build C++ examples
---------------------------------------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NX Open AppWizard.
      This is described in the NX Open for C/C++ -> Open C Reference Guide -> 
      Overview -> setting up your system.  The image being created is an external
      User Function program using C++ and Open C++ calls.
   2. Add the UIStylerSelectionExample.cxx file by selecting the Project
      pulldown and select "Add Existing Item...".  Select the file using the popup
      window.
   3. Build the external image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
   This will create an executable called UIStylerSelectionExample.exe in the Debug directory.

   The uflink tool can also be used to create the executable by following these steps:
   1. Open an NX command prompt window.
   2. Change directories to the directory containing the source code.
   3. Compile and link using uflink:
      uflink ufexe=UIStylerSelectionExample.exe
   This will create UIStylerSelectionExample.exe in the current directory.

   Unix
   -------
   Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu)
   Compile and link an exernal user function program.  Answer the first question for
     linking with an "e" (Link internal/external user function (i/e):) and select "y" for 
     the next input - Link a UG/Open++ Image (y/n).  This will create an external
     user function executable which has been linked against the Open++ and C++ libraries.
  

   This will create an executable called UIStylerSelectionExample.

--------------------------------------
How to Run C++ Examples
--------------------------------------

Once you have successfully finished with "How to Build C++ examples" steps, it will create executable called 
UistylerselectionExample.dll in debug dir of the project dir.
	1. Start NX.
	2. Open Block.prt file
	2. Go to File -> Execute ->NX Open.
	3. You will lead to window called "Execute User Function". 
	4. Navigate to the location of the dll file.  It will be in the <Project      
         Folder>\debug\ directory under the C++ project.
	5. Select UistylerselectionExample.dll file and Click ok. This will pop 
	   up UIStylerSelectionExample.dlg file. 
	6. Select any edge/s (One of the edge of the Block is not selectable),
	   enter appropriate blend radius value and Ok the dialog, this will blend the selected edges.
