-------------------------------------------------------------------------------


          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                           Sketch Shape Example 
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates creation of various shapes in the Sketch Task Environment.

--------------
Files required
--------------

     1. sketch_shape_journal.vb
     2. sketch_test_part.prt(This file is located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\SketchShape)
     3. transform_script.pl(This file is located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\SketchShape)
     4. sk1.jpg (This file should be placed at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\SketchShape\images)
     5. sk2.jpg (This file should be placed at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\SketchShape\images)
     6. sk3.jpg (This file should be placed at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\SketchShape\images)
     7. sk4.jpg (This file should be placed at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\SketchShape\images)
        
-----------
Build Steps
-----------
     Windows
     -------
    1. Open Microsoft Visual Studio

    2. Create a new Vb project using the NX Open AppWizard. 
       Create new project as:
            2.1 File->New->Project.
 	        2.2 Select Vb Project using the NX Open AppWizard, Class Library Application, Enter name as sketch_shape. Click Next
            2.3 Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'and select 'NXOpen.UI API'. 
            2.4 Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

    3. Remove all *.vb files from created project by clicking MB3 on respective file and 
       clicking 'Delete' on popup menu.You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
    4. Add the sketch_shape_journal.vb to the project by selecting the Project pull down and select "Add Existing Item...". Select the file using 
       the popup window.

    5. Add the following references,
	    5.1. System.Windows.Forms
	    5.2. System.Drawing
	         To do this Go to Project->Add Reference-> .NET Tab->Under the Component Name; Select 'System.Windows.Forms' & hit Ok.In the same manner add System.Drawing. 
        5.3. NX Open References
             Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
             To do this, right click on "References" under the sketch_shape project in Solution Explorer. 
             Pick "Add Reference..." and then navigate to the location of the dlls. 
             These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.
        
    6. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

    This will create a shared library sketch_shape.dll in the Release directory.

    Linux
    -----
    N/A
    
----------------------------
Settings before Launching NX
----------------------------
    N/A
    
----------------------------
Settings after Launching NX
----------------------------
    1. Change the Role to Advanced.

-----------------------
Example Execution Steps
-----------------------
    1. Start NX.
        
    2. Open sketch_test_part.prt.
        
    3. Start the Modeling Application (Ctrl+M).
        
    4. Activate a sketch by using the Edit -> Sketch command. Highlight the "Open in Sketch Task Environment" icon in the Direct Sketch toolbar. 
       (If you
        
    5. Follow any one of the methods mentioned below:

        5.1 Invoke sketch_shape_journal.vb file using Tools->Journal->Play (Alt+F8).
               
        5.2 By creating Shared Library and invoke sketch_shape.dll through File->Execute->NX Open Menu (Ctrl+U).
            
    6. You will be prompted to select a shape and a preview image will be shown.Click Next after selecting the shape.   
        
    7. You will be prompted for the names and values of dimensions.The dimension that you are changing will be highlighted in the preview image. 
       You can change which dimension you are editing by clicking on the dimension text in the preview image.
       Click  on Create.The selected shape will be created. 
 
-----
Note:
-----
    1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
        For more details on signing the application refer to NXOpen Programmer's Guide."

    2. What is remarkable about the example is the way that the journal record capabilities were used to create the example. 
       The code that actually creates the shapes was created by recording the creation of the shape in the journal, making some minor edits, 
       and then adding code at the end to change the key dimensions of the shape.  This code to create the shapes is located in the 
       Execute methods of the KeyholeShapeCreator, Shape2Creator, SlotShapeCreator, and Shape4Creator classes.  All the other code in the 
       example is just code for the GUI for the example.  By using the journal record capability, creating this example was much, much quicker and easier than it could have been if it were created by coding with user function.

    3. The edits that were applied to the journal code were:
        a. transform the coordinates into the coordinate system of the active sketch, so that the shape is created in the plane of the active sketch; 
        b. comment out most of the calls to Update, to optimize performance, comment out the creation of undo marks, and add one undo mark at the beginning of the Execute method; and 
        c. call UF SetReferenceStatus on curves that should be reference curves.  In order to do the first two types of edits, the perl script transform_script.pl was used.  
           (Perl is open source software that can be downloaded free of charge from http://www.perl.org.)  Commenting out Updates is done only to optimize performance.  
           Not commenting out any Updates is always safe, but will mean that the performance of the journal will be less than optimal.  
           One of the calls to Update needed to be uncommented out for one of the shapes.  This happened because the Sketch.AddGeometry infers coincident constraints based on the
           location of other curves in the sketch, so Update needed to be performed so that the curves would be in the correct place in order to infer coincident constraints.  
           In applying this approach to other journals, you may need to experiment with commenting and uncommenting out Updates in order to find out which Updates can be commented out without changing the meaning of the journal.  

'=================================End=========================================
