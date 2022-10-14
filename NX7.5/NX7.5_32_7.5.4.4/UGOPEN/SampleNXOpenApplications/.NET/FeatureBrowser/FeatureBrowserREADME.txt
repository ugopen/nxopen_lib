' ===================================================================
'
'             Copyright (c) 2004  UGS PLM Solutions
'               Unpublished - All rights reserved
'
'  
' ===================================================================
This example queries all the open, fully loaded parts in the current NX session, and populates a Windows Forms dialog with information on the parts. What this example shows is how to use the more advanced Windows Forms UI elements that are not readily available in the UI Styler, such as a TreeView, ListView, and PropertyGrid.

The main form for the application shows a tree view of the open parts. Inside each part node in the tree view are a list of the features in each part. If you select a part, all the expressions for the part will be displayed in a list view in the upper right. If you select an expression in the list view, a subset of the public properties of the expression will be displayed in the property grid in the lower right. You can change the value of the selected expression by entering a new value for the expression in the expression's RightHandSide property. Click on the Update button to apply all the pending changes to the part and update the part.

The flow of the example is as follows:

o Initialize the FeatureBrowser form. During initialization
  the load event on the main form will execute the following 
  steps:
  - Query all the open, fully loaded parts in the NX session.
  - Display a list of the parts in a tree view.
  - For each part, get the features and the bodies in the part.
  - Display two subnodes called Features and Bodies under each 
    part. The Features subnode contains all the features in the
    part organized in timestamp order. The Bodies subnode contains
    all the sheet and solid bodies in the part.
  - Display the features for each part as subnodes 
    under the Features subnode for each part.
  - Display the bodies for each part as subnodes under the 
    Bodies subnode for each part.
  - For each body, get the faces and edges in the body.
  - Display two subnodes called Faces and Edges under each
    body tree node. The Faces subnode contains all the faces in
    the body. The Edges subnode contains all the edges in the 
    body.
o Various UI elements in the form have events defined to handle
  some selection events from the user. The main purpose for 
  these event handlers is to display more detailed information
  for items the user selects in the form.
  - When the user selects a part in the tree view, 
    populate the list view with a detail view of all the
    expressions in the part.
  - When the user selects a feature in the tree view,
    populate the list view with a detail view of all the
    expressions in the feature. Display a subset of the
    public properties of the feature in the property grid.
  - When the user selects an expression in the list view, 
    display a subset of the public properties of the 
    expression in the property grid.
  - When the user selects a body in the tree view, display
    a subset of the public properties of the body in the 
    property grid.

How to build the example:

- In a working directory, copy the files for the FeatureBrowser example.
- Open up the VB .NET project (FeatureBrowser.vbproj) in Visual Studio.
- Add references to NXOpen.dll, NXOpenUI.dll, NXOpen.Utilities.dll.
  To do this, click MB3 on "References" under the FeatureBrowser project in Solution
  Explorer.  Pick "Add Reference..." and then navigate to the location of the dlls.
  These NX dlls can be found in the managed subdirectory under %UGII_ROOT_DIR%.  
  Find and highlight the library, click Select and then OK on the Add Reference form.
- Select the Build->Build Solution menu command.
- The executable will be placed in a subdirectory named "bin" under the working 
  directory after the build completes.

How to run the example

- Start up an NX session and open some parts.
- Go to File - Execute - NX Open.  This will bring up the Execute User Function 
  dialog. Browse to the FeatureBrowser.exe location in the "bin" directory.  
- Select the FeatureBrowser.exe executable and click OK.  NOTE: you may have to 
  change the file type filter to *.exe to allow you to select the .exe file.

