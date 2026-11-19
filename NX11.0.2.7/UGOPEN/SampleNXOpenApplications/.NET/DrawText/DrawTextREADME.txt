'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		Draw Text Example
------------------------------------------------------------------------------

-----------
Description
-----------
This example shows creating solid bodies in the shape of text using outlines from 
TrueType fonts. It takes advantage of the .Net framework libraries for getting the 
outlines of the characters. It also shows some simple use of user function to create splines.
This example will work with any national language.

--------------
Files required
--------------
   1. DrawText.vb

   The above listed file is located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\DrawText
   Note: the UGII_BASE_DIR is expanded in the SYSLOG if the system does not recognize the environment variable.

------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio

   2. Create new project as:
		2.1. File->New->Project.
		2.2. Select Visual Basic Projects using the NX Open AppWizard, Class Library Application, Enter
		   name as 'DrawText'. Click Next
		2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session(DLL)'
		   and select 'NXOpen.UI API'. 
		2.4. Select to activate the application Explicitly and to unload the application when NX session terminates. Click Finish.

   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.
 
   4. Add the following reference,
		4.1. System.Windows.Forms
		4.2. System.Drawing
			 To do this, right click on "References" under the project in Solution
			 Explorer. Pick Add Reference->.NET Tab->under component name,
			 select System.Windows.Forms. Repeat the process and select System.Drawing
        4.3. NX Open References
             Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
             To do this, right click on "References" under the DrawText project in Solution Explorer. 
             Pick "Add Reference..." and then navigate to the location of the dlls. 
             These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.

   5. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add Existing Item'. Navigate to and add the DrawText.vb file.
   		
   6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   7. This will create an executable called DrawText.dll in the \bin\Release directory.

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

-----------------------
Example execution steps
-----------------------
     Journal execution
     ------------------
      1. Open a part.
      2. Using Tools->Journal->Play or (Alt+F8)
      3. Select DrawText.vb and Run
      4. 'Font' dialog box will pop-up. Select font option and click OK.
      5. 'Enter String To Convert' dialog box will pop-up. Enter your text and click OK.
      6. The system will prompt you to pick a position. Select the position using 
         the mouse. The selection is in reference to the XY plane.
      7. 'Enter extrusion thickness' dialog box will pop-up. Enter the desired text
         thickness and click OK.
      8. The entered text will be displayed as a extrusion at the clicked location on 
         the XY plane with the desired thickness. An Extrude feature is created in the part navigator
        
     Shared Library execution
     ------------------------
      1. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      2. Browse and select the DrawText.dll and execute.
      3. Follow point no.4  and onwards, mentioned above in 'Journal execution'.
    
-----------------------
Notes
-----------------------
    1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
        For more details on signing the application refer to NXOpen Programmer's Guide."

    2. Design Notes-
       This makes use of Microsoft supplied classes to get the outline of text in a TrueType font in particular
       the GraphicsPathIterator class. This is done in the Main routine. The outline consists of straight
       lines and Bezier curves. Connected sets of the same type of curve are extracted and processed by either CreateLinearPath
       or CreateSplinePath. CreateSplinePath converts from Bezier representation into B-Spline representation and
       uses UFCurve's CreateSpline method to create the spline. 

       Note that the coordinates from the TrueType outline are adjusted so the text is the right way up when viewing down 
       the Z axis.

       Once the curves are created a sketch is made - this was derived from recording the creation of a sketch. Then
       all geometry is added to the sketch. The main addition is the sketch creation is retried with different sketch
       names until it succeeds to allow for the unique sketch name rule.

       The extrusion routine was also derived from recording the extrusion of a sketch and simply extrudes the result
       of the previous step along the Z axis by the user supplied depth.

-----------
CAVEATS
-----------
    1. No attempt is made to handle self intersecting outlines which can be generated by some font styles - such as strikeout
       or in some languages.

    2. The color of the first body created is different from all the other bodies which is a known problem.

    3. The screen does not always refresh between steps in the process so you may not see the curves created while
       entering the extrusion thickness.

'=================================End=========================================
