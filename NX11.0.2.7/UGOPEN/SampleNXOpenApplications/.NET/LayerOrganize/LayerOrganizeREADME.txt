'=============================================================================
'
'                   Copyright (c) 2012 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================
-------------------------------------------------------------------------------
                      Layer Organize Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example moves the items on the work layer onto different layers based on the standards specified in layer_standards.txt.

The layer_standards.txt file contains rules that tell which NXOpen classes or UF types should be placed on each layer.  
Each rule starts with an integer layer id or the name of a layer category, followed by a colon, followed by a list of 
the NXOpen classes or UF types that should be moved to that layer.


--------------
Files required
--------------

	1. create_layer_categories.vb
	2. layer_organize.vb
	3. layer_organize_test_part.prt
	4. layer_standards.txt
	
The above listed files are located at
$UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\LayerOrganize

   
------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio

   2. Create new project as:
      2.1. File->New->Project.
 	  2.2. Select Visual Basic Projects using the NX Open AppWizard, Class Library Application, Enter
           name as LayerOrganize. Click Next
      2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
           and select 'NXOpen.UI API'. 
      2.4. Select to activate the application explicitly and to unload the application when NX session terminates. Click Finish.

   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.

   4. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'.  Navigate to and add the FilloutTitleBlock.vb file.

   5. Add the following reference,
	  5.1. System.Windows.Forms
      5.2. System.Drawing
		   To do this, right click on "References" under the project in Solution
		   Explorer. Pick Add Reference->.NET Tab->under component name,
		   select System.Windows.Forms. Repeat the process and select System.Drawing
      5.3. NX Open References
           Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
           To do this, right click on "References" under the LayerOrganize project in Solution Explorer. 
           Pick "Add Reference..." and then navigate to the location of the dlls. 
           These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.
   		
   6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   7. This will create an executable called LayerOrganize.dll in the \bin\Release directory.

   Linux
   -------
   -NA-


----------------------------
Settings before Launching NX
----------------------------
	1. You will need to edit layer_organize.vb to indicate the path to layer_standards.txt.  
	   Edit the line in layer_organize.vb that creates a new StreamReader for layer_standards.txt and 
       change "layer_standards.txt" to the full path to the layer_standards.txt file.

----------------------------
Settings after Launching NX
----------------------------
    1. Change the Role to Advanced.

   
--------------------------
Example execution steps
--------------------------
    Journal execution
     ------------------
    1. Open a part.  (An example part named layer_organize_test_part.prt has been provided.)  
       The part should contain each layer category that is named in the layer_standards.txt file.  
	   If your part does not have all the layer categories specified in layer_standards.txt, you can run create_layer_categories.vb to create them.

    2. So that you will be able to verify the changes made by running layer_organize.vb, go to Format -> Layer Settings.  
	   If you are using the example part, you will see many Categories and only Layer 1 listed in the layer/status field as the Work layer.

    3. Using Tools->Journal->Play or (Alt+F8)

    3. Select layer_organize.vb and Run

    4. After the file has run, you can verify the changes by again going to Format -> Layer Settings.
	   Highlight one of the Categories, such as CURVES, then hit Selectable.  Hit Apply.  
	   The curves should appear on the graphics and they will be selectable.  You can do this with any of the categories.

    Shared Library execution
    ------------------------
    1. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.

    2. Browse and select the LayerOrganize.dll and execute.
      
    3. Follow point no.4, mentioned above in 'Journal execution'.


-----
Note:
-----
	1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
	    For more details on signing the application refer to NXOpen Programmer's Guide."
	
	2. User will require a .NET authoring license to run the example. See the online documentation for details of licensing.
	   
	3. The code that actually moves the objects is just the call to workPart.Layers.MoveDisplayableObjects, which are just two lines out of the entire example.  The rest of the code is for parsing the layer_standards.txt file and organizing the objects into lists of objects to pass into MoveDisplayableObjects, based on the object type.  The LayerToClassMap class parses the layer_standards.txt file and builds a map that pairs each NXOpen class or UF type with the layer that objects of that type should be placed into.  The .NET System.Reflection functionality is used to read the NXOpen class hierarchy and System.Text.RegularExpressions is used to help parse the layer_standards.txt file.  In the main subroutine, after the layer_standards.txt file is parsed, the objects on the work layer are organized into lists based on which layer the object should be move to.  A separate list is created for each layer.  The ListOfObjectsToMove class contains these lists.  For each object, LayerToClassMap.FindLayerForNXClass and FindLayerForUFType are used to find out what layer the object should be moved to.  After the objects have been organized into lists, workPart.Layers.MoveDisplayableObjects is called on each list to move the objects to the correct layer.

	4. SYNTAX OF THE layer_standards.txt FILE :
	
	Comments are denoted with "#" and have the format: #<text># or #<text><end of line>
	Each specification is of the form

	<layer identifier>:
		<class specification>(,<class specification>)*

	<layer identifier> is
	[layer ]<layer_id or layer_category_name>

	For example:
	layer 20:
	20: # equivalent to the above line
	DATUMS: # the layer category named DATUMS

	No other information must appear on the line containing the <layer identifier>.

	<class specification> is either the name of an NX Open class or is the name of a UF object type and subtype.

	For example:
	Arc # the NXOpen Arc class
	UF_drafting_entity_type # the UF UF_drafting_entity_type and any subtype
	UF_drafting_entity_type.UF_draft_line_subtype 
	# the UF UF_drafting_entity_type type and UF_draft_line_subtype
	drafting_entity.draft_line # equivalent to the line above

	The <class specification> may span several lines.

'=================================End=========================================
