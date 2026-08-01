-------------------------------------------------------------------------------


          Copyright 2016 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
           Block Styler Tree List Width Demo example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates ability to resize the width of dialogs created using Block UI Styler.
Similarly it will demonstrate the functionality of MaximumWidth, MinimumWidth and CanStretchWidth properties of TreeList block.

--------------
Files required
--------------

    1. TreeListWidthDemo.vb
    2. TreeListWidthDemo.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/TreeListWidthDemo)
    3. Any Part file.
    
-----------
Build Steps
-----------   
    
 Windows
 -------
1. Open Microsoft Visual Studio .Net.

2. Create a new Vb project using the NX Open AppWizard. 
   Create new project as:
        2.1 File->New->Project.
        2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as TreeListWidthDemo. Click Next
        2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
        2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

3. Remove all *.vb files from created project by clicking MB3 on respective file and 
   clicking 'Delete' on popup menu.You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
4. Add the TreeListWidthDemo.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
   the popup window.
        
5. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

This will create an shared library TreeListWidthDemo.dll in the Debug directory.
    
Linux
-----
Not applicable

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

    2. Open any part file. There should be atleast one feature available in that part.

    3. Launch the dialog by using any one of the methods mentioned below:

        a. Using the menu, Tools->Journal->Play... 
               - Invoke TreeListWidthDemo.vb file using Tools->Journal->Play.
        b. By creating a shared Library and invoking it through File->Execute->NX Open Menu.
           (Refer Build steps to create a shared library that is TreeListWidthDemo.dll)
    
    4. This will launch the “Tree List Width Demo” dialog. User can see that width related
       properties of TreeList block are used from initialize_cb().

    5. To set new values of width related properties user has to change there values in initialize_cb() 
       function and then invoke TreeListWidthDemo.vb file using Tools->Journal->Play.

    6. This will launch the "Tree List Width Demo” dialog with new values of width related properties
          of TreeList block from initialize_cb(). 

    7. Also there is a "Dialog Sizing" property for Block UI Styler dialog. The values for this property are "Follow Policy"
       and "Allow Resize". User has to set this property to "Allow Resize", so that dialog retains its widths 
       by retaining the width of TreeList block from initialize_cb().
          
    8. If user enters negative values for any of the width related properties, the value would be changed to zero
          and default width would be used for dialog. The default width for TreeList block is 200 pixels.
-----
Note:
-----
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
    

