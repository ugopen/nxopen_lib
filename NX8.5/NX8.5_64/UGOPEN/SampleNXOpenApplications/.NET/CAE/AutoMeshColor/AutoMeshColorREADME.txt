 AutoMeshColor.vb - Change element display color based on mesh, collector, physical or material

   Description:
   This program will modify the color of all meshes in the .fem based on a user specified
   criteria. When executed, the user will be presented with a form containing 4 options:
     1) By Mesh - each mesh will have it's color modified
     2) By Collector - All meshes in the same collector will be colored the same
     3) By Physical - All meshes with the same physical property will be colored the same
     4) By Material - All meshes with the same material property will be colored the same

   Colors are assigned via a 'color wheel'. This is an integer array containing the NX color
   palette numbers to cycle through. If there are more meshes/collectors/physicals/materials than
   there are colors defined in the color wheel, then the wheel is reset to the beginning and
   duplicate colors will be used. The NX color palette is included as a comment at the bottom of
   this file for reference. The user can modify the definition of myColorWheel() using these
   values.

   Instructions:
   1) Place a copy of enumBlock.dlx in the %UGII_USER_DIR%\application folder
   2) Run this program from within a FEM file in NX Advanced Simulation
      - Use Tools > Journal > Play to execute AutoMeshColor.vb
   3) The program will prompt you for the method to set colors by


 Caveats (as of NX 6.0.2)
  1) By Collector, By Physical and By Material options only work in a FEM part
      - Collector cannot be programmatically determined without access to a MeshManager object,
        which is only available in the .fem
  2) By Collector, By Physical and By Material options do not work for manual meshes
      - Collector cannot be programmatically determined without access to a MeshManager object,
        which does not exist for manual meshes generated in NX
  3) By Collector, By Physical and By Material options do not work for imported meshes
      - Collector cannot be programmatically determined without access to a MeshManager object,
        which does not exist for meshes that weren't generated in NX
  4) By Collector, By Physical and By Material options set the color of the individual meshes
     and not the parent collector
      - Collector color cannot be set programatically
  5) In all cases, the individual mesh color is being modified. There is no method to set the
     collector color directly.

