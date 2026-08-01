ReassignElements.vb - Move elements into new meshes

   Description:
   This program will move elements out of one or more meshes and create 
   one or more new meshes that can be given new or different properties.
   This program leverages the following three commands in NX Advanced
   Simulation:
      o Element copy and translate
      o Delete elements
      o Merge nodes
   The program will copy the desired elements in place (i.e. delta = 0.0)
   creating one or more new meshes. The original elements will be deleted 
   and then the nodes are merged for all meshes. When complete, you can
   move the new meshes into whatever Mesh Collectors you like (drag-n-drop).
 
   Instructions:
   1) This program must be run inside a FEM
   2) Create a group of all the elements you wish to reassign. Name this 
      group "ReassignElements".
   3) Run this VB script and it will take the elements in the ReassignElements
      group and create new meshes, delete the original elements and merge the 
      nodes.

   Known Issues:
   1) The elements get renumbered – so if you need the element ID labels to 
      be retained, this will not work for you.
   2) For parabolic shells, the location of the mid-nodes get changed. This was 
      a quirk in the node merge step, and this has been fixed in NX603. In NX603 
      the location of shell mid-nodes will not get modified during node merge. 
   3) The node merge can be slow on larger models, because it is checking for a
      merge condition of every node in the model. If running this script on a big
      model, you may want to comment out the node merge step in this script, and 
      instead merge nodes interactivel (only in the area where the elements have
      been copied.)

