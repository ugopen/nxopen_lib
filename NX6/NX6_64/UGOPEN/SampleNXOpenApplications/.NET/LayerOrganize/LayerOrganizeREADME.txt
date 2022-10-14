This example moves the items on the work layer onto different layers based on the standards specified in layer_standards.txt.

The layer_standards.txt file contains rules that tell which NXOpen classes or UF types should be placed on each layer.  Each rule starts with an integer layer id or the name of a layer category, followed by a colon, followed by a list of the NXOpen classes or UF types that should be moved to that layer.


HOW TO RUN THE EXAMPLE
- You will need to edit layer_organize.vb to indicate the path to layer_standards.txt.  Edit the line in layer_organize.vb that creates a new StreamReader for layer_standards.txt and change "layer_standards.txt" to the full path to the layer_standards.txt file.
- Open a part.  (An example part named layer_organize_test_part.prt has been provided.)  The part should contain each layer category that is named in the layer_standards.txt file.  If your part does not have all the layer categories specified in layer_standards.txt, you can run create_layer_categories.vb to create them.
- So that you will be able to verify the changes made by running layer_organize.vb, go to Format - Layer Settings.  If you are using the example part, you will see many Categories and only Layer 1 listed in the layer/status field as the Work layer.
- Run layer_organize.vb using Tools - Journal - Play.  Hit Browse and find the vb file.
- After the file has run, you can verify the changes by again going to Format - Layer Settings.  Highlight one of the Categories, such as CURVES, then hit Selectable.  Hit Apply.  The curves should appear on the graphics and they will be selectable.  You can do this with any of the categories.


DESIGN NOTES
The code that actually moves the objects is just the calls to workPart.Layers.MoveObjects, which are just two lines out of the entire example.  The rest of the code is for parsing the layer_standards.txt file and organizing the objects into lists of objects to pass into MoveObjects, based on the object type.  The LayerToClassMap class parses the layer_standards.txt file and builds a map that pairs each NXOpen class or UF type with the layer that objects of that type should be placed into.  The .NET System.Reflection functionality is used to read the NXOpen class hierarchy and System.Text.RegularExpressions is used to help parse the layer_standards.txt file.  In the main subroutine, after the layer_standards.txt file is parsed, the objects on the work layer are organized into lists based on which layer the object should be move to.  A separate list is created for each layer.  The ListOfObjectsToMove class contains these lists.  For each object, LayerToClassMap.FindLayerForNXClass and FindLayerForUFType are used to find out what layer the object should be moved to.  After the objects have been organized into lists, workPart.Layers.MoveObjects is called on each list to move the objects to the correct layer.


SYNTAX OF THE layer_standards.txt FILE

Comments are denoted with "#" and have the format: #<text># or #<text><end of line>
Each specification is of the form

<layer identifier>:
	<class specification>(,<class specification>)*

<layer identifier> is
[layer ]<layer_id or layer_category_name>

For example:
layer 20:
20: # equivalent to the above line
DATUMS: # the layer category named DATUMS

No other information must appear on the line containing the <layer identifier>.

<class specification> is either the name of an NX Open class or is the name of a UF object type and subtype.

For example:
Arc # the NXOpen Arc class
UF_drafting_entity_type # the UF UF_drafting_entity_type and any subtype
UF_drafting_entity_type.UF_draft_line_subtype 
# the UF UF_drafting_entity_type type and UF_draft_line_subtype
drafting_entity.draft_line # equivalent to the line above

The <class specification> may span several lines.


