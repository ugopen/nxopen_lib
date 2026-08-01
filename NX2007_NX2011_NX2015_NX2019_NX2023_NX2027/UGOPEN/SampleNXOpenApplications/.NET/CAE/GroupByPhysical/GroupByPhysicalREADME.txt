GroupByPhysical.vb - Group elements (meshes) by Physical Property

  Description:
  This program is used to create groups of elements with a common Physical Property Table

  This program automatically sorts through all meshes in a FEM and determines
  the physical property table. It then will create a group named
  PHYS_<physcial property name> if one does not exist. Otherwise it adds the
  current mesh to the existing group.

  It is assumed that this program will be run in a FEM file.

  Instructions:
  1) Run this program from a FEM file in NX Advanced Simulation 
     - Use Tools > Journal > Play to execute ElementGroupByPhysical.vb

  If desired, a new button may be created on a tool bar. An image is provided 
  "GroupByPhysical.bmp" for the button. To create a new button, select the customize 
  option from any down-pointing arrow at the end of an NX toolbar. On the Commands tab, 
  scroll down to find "New Button". In the right window pane, select "New User Command" 
  and drag it to the desired toolbar. Right-click on the new button to set the options 
  for the new button. Use Change Button Image to set the button image to the included 
  bmp. You must choose Edit Action and set the path to the dll. Also, in the Edit 
  Action form, the type must be set to "User Function"
