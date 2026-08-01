 DeformMeshFromResultFile.vb - Deform a mesh based on results file

   Description:
   This program is used to deform a mesh based on a results file. 
   This program  will ask you for the results file and will read its contents 
   and translate the nodes in the FEM by the given displacement amounts.  It is 
   assumed that this program will be executed in a fem part and that the results 
   matches FE model in this FEM.
 
   Instructions:
   1) Place a copy of SelectLoadCase.dlx in the %UGII_USER_DIR%\application folder
   2) Run this program (DeformMeshFromResultFile.vb) from within a FEM file in NX 
      Advanced Simulation. This is done via the Tools > Journal > Play command.
   3) The program will prompt you for the results file previously solved for.
      o It is assumed the node ID's in the results file match the nodes in the
        FEM file. 
   4) The program will read the results file and for each node in the file it
      will reposition the node to it's given result location.
