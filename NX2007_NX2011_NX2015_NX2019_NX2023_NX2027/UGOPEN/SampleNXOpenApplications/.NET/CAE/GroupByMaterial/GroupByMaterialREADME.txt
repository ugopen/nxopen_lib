GroupByMaterial.vb - Group elements (meshes) by Material

  Description:
  This program is used to create groups of elements with a common assigned material

  This program automatically sorts through all meshes in a FEM and determines
  their material. It then will create a group if one does not exist. Otherwise it will add
  the mesh to the existing group.
  
  Groups will be named following these rules:
  1) Elements with an assigned material (either explicity assigned or inherited) will be named
     MAT_<material name>
  2) If the material is inherited but not assigned, the group will be named "MAT_Inherited - Not Assigned"
  3) If the material is NOT inherited and not assigned, the group will be named "MAT_NULL"

  The group names above are intended to help determine if a model has all material assignments
  easily and quickly.

  It is assumed that this program will be run in a FEM file.

  Instructions:
  1) Run this program from a FEM file in NX Advanced Simulation 
     - Use Tools > Journal > Play to execute ElementGroupByMaterial.vb

  If desired, a new button may be created on a tool bar. An image is provided 
  "GroupByMaterial.bmp" for the button. To create a new button, select the
  customize option from any down-pointing arrow at the end of an NX toolbar
  On the Commands tab, scroll down to find "New Button". In the right window pane,
  select "New User Command" and drag it to the desired toolbar. Right-click on the
  new button to set the options for the new button. Use Change Button Image to set
  the button image to the included bmp. You must choose Edit Action and set the path
  to the dll. Also, in the Edit Action form, the type must be set to "User Function".
