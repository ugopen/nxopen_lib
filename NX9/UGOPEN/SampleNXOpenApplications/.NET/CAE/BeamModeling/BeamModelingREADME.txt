BeamModeling.vb - Illustrates the use of NX Open calls that replace User Functions that were available before the Beam Modeling functionality was redesigned in NX 7.5.

Description:

This program shows how you can create a beam section of each type: standard NX Nastran section, a face of solid section,
general geometry section (created from sketches) and one using key-in properties.
It creates one mesh each using one of the above sections. It also shows how to edit the section offsets/orientations in a mesh.
Finally, it shows how to query for the dimensions of the standard section or the computed properties of any type of section.

To understand the program, please refer to Digital Simulation->Open CAE documentation->Solver Environment documentation. Each solver environment has a Standard Beam Cross Sections reference that provides the mapping between the automation (neutral) names of standard beam section dimensions and their displayed names as seen in the UI. Internally, a beam section dimension is identified by its neutral name, and therefore the author of an NX Open program must know it in order to create a beam section or query the dimension of an existing beam section.
