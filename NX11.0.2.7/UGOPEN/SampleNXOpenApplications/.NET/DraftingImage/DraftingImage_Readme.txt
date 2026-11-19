'===================================================================================
'
'          Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
'                     Unpublished - All rights reserved
'
' 
'  
'===================================================================================

------------------------------------------------------------------------------------
                        Drafting Image Example
------------------------------------------------------------------------------------

-----------
Description 
-----------

    This example demonstrates how to use drafting image collection and export function.   

--------------
Files required
--------------

    1. DraftingImage_Sample.vb
    2. DraftingImage_Sample.prt
    
-----------
Build Steps
-----------
   Windows
   -------
   1. Open Microsoft Visual Studio.

   2. Create new project as:
		2.1. File->New->Project.
		2.2. Select Visual Basic Projects using the NX Open AppWizard, Class Library Application, Enter
			 name as DraftingImage. Click Next
		2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
			 and select 'NXOpen.UI API'. 
		2.4. Select to activate the application explicitly(Main) and to unload the application when NX session terminates. Click Finish.

   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.

   4. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'. Select the file drawing_cycle.vb ($UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\DraftingImage)
      and add it. 
	  
   5. Add the following reference,
		5.1. System.Windows.Forms
        To do this Go to Project->Add Reference-> .NET Tab->Under the Component Name; Select 'System.Windows.Forms' and hit Ok.
   		5.2. NX Open References
        Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
        To do this, right click on "References" under the DraftingImage project in Solution Explorer. 
        Pick "Add Reference..." and then navigate to the location of the dlls. 
        These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.

   6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   7. This will create an executable called DraftingImage.dll in the \bin\Release directory.    
   
   Linux
   -------
   -NA-

----------------------------
Settings before Launching NX
----------------------------

    Set system environment variable UGII_TMP_DIR to a file directory.

----------------------------
Settings after Launching NX
----------------------------

    Change the Role to Advanced.

--------------------------
Example execution steps
--------------------------
    
        1. Start NX.
        
        2. Open part file "DraftingImage_Sample.prt".
        
            (Open-> find "DraftingImage_Sample.prt" -> OK).
        
        3. Play journal "DraftingImage_Sample.vb".
            
            (Tools-> Journal-> Play-> Browse-> find "DraftingImage_Sample.vb" -> OK-> Run).
        
        4. Look for image file exported inside the directory specified by system environment variable UGII_TMP_DIR.
        
-----
Notes:
-----
        1. NXOpen application must be signed before its release. If not signed the application may not get executed.
		     For more details on signing the application refer to NXOpen Programmer's Guide.

        2. The original image files are also provided as references.
           They are:
             DraftingImageSample_JPG.jpg
             DraftingImageSample_PNG.png
             DraftingImageSample_TIF.tif
        
