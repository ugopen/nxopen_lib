'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		Feature Browser Example
------------------------------------------------------------------------------

-----------
Description
-----------
This example queries all the open, fully loaded parts in the current NX session, and 
populates a Windows Forms dialog with information on the parts. What this example shows
is how to use the more advanced Windows Forms UI elements that are not readily available
in the UI Styler, such as a TreeView, ListView, and PropertyGrid.

The main form for the application shows a tree view of the open parts. Inside each part 
node in the tree view are a list of the features in each part. If you select a part, 
all the expressions for the part will be displayed in a list view in the upper right. 
If you select an expression in the list view, a subset of the public properties of 
the expression will be displayed in the property grid in the lower right. You can 
change the value of the selected expression by entering a new value for the expression
in the expression's RightHandSide property. Click on the Update button to apply all 
the pending changes to the part and update the part.


--------------
Files required
--------------
   1. BodyFeatureSurrogate.vb
   2. BodySurrogate.vb
   3. BodyTreeNode.vb
   4. DisplayableObjectTreeNode.vb
   5. EdgeTreeNode.vb
   6. ExpressionSurrogate.vb
   7. FaceTreeNode.vb
   8. FeatureBrowser.vbproj
   9. FeatureBrowserAssemblyInfo.vb
   10. FeatureBrowserForm.resx
   11. FeatureBrowserForm.vb
   12. FeatureBrowserREADME.txt
   13. FeatureSurrogate.vb
   14. FeatureTreeNode.vb
   15. PartTreeNode.vb
  
------------
Build steps
------------
   Windows
   -------
   1. Launch Microsoft Visual Studio

   2. Open up the VB project FeatureBrowser.vbproj (Working directory should contain all the files for the FeatureBrowser example)
   
   3. Add the following references,
      3.1. NXOpen.dll 
      3.2. NXOpenUI.dll 
      3.3. NXOpen.Utilities.dll
      3.4. NXOpen.UF.dll.

      To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
      Go to %UGII_BASE_DIR%\nxbin\managed.  Select and add the DLL's one after the other.

   4. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
      right click on project name and select Build.

   5. This will create an executable called FeatureBrowser.exe in the \bin\Release directory.

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
     -NA-
        
     Shared Library execution
     ------------------------
      1. Open some parts having few features inside it.
      2. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      3. Browse and select the FeatureBrowser.exe and execute.
         NOTE: you may have to change the file type filter to *.exe to allow you to 
         select the .exe file.
      4. Feature browser dialog box should be displayed. The left hand side is a Tree
         view and the Right side displays Feature Expression and Properties list view
      5. It should list all parts that are open, fully loaded parts in the NX session
         when you select a part in the tree view, populate the list view with a detail
         view of all the expressions in the part.
      6. When the user selects an expression in the list view, it display's a subset of the
         public properties of the expression in the property grid.
      7. For each part expand the node and it should display two subnodes called Features
         and Bodies
      8. Expand Feature node and it should display all Features
         select Feature and Feature Expressions box populate the list view with a detail
         view of all the expressions in the feature. You can select the expression to
         see the properties in the properties grid.
      9. Expand Bodies node and it should display solid & sheet bodies for each part.
      10. Select a Body and its properties are displayed in the properties box. 
      11. Expand a Body and it will display two subnodes Faces and Edges.
      12. Expand Faces, Edges and it will display all the Faces and edges in the body respectively.

------
Notes
------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

'=================================End=========================================
