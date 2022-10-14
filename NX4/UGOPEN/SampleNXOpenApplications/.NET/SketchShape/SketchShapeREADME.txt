This example creates shapes on various sketches.

HOW TO RUN THE EXAMPLE

- Open the example part that has been provided.
- Start NX and activate a sketch by using the Edit -> Sketch command. 
- Run sketch_shape_journal.vb.
- You will be prompted to select a shape and a preview image will be shown.  Click Next after selecting the shape.  
- You will be prompted for the names and values of dimensions.  The dimension that you are changing will be highlighted in the preview image.  You can change which dimension you are editing by clicking on the dimension text in the preview image.
- Click Create to create the shape. 


DESIGN NOTES

What is remarkable about the example is the way that the journal record capabilities were used to create the example.  The code that actually creates the shapes was created by recording the creation of the shape in the journal, making some minor edits, and then adding code at the end to change the key dimensions of the shape.  This code to create the shapes is located in the Execute methods of the KeyholeShapeCreator, Shape2Creator, SlotShapeCreator, and Shape4Creator classes.  All the other code in the example is just code for the GUI for the example.  By using the journal record capability, creating this example was much, much quicker and easier than it could have been if it were created by coding with user function.

The edits that were applied to the journal code were 1. transform the coordinates into the coordinate system of the active sketch, so that the shape is created in the plane of the active sketch; 2. comment out most of the calls to Update, to optimize performance, comment out the creation of undo marks, and add one undo mark at the beginning of the Execute method; and 3. call UF SetReferenceStatus on curves that should be reference curves.  In order to do the first two types of edits, the perl script transform_script.pl was used.  (Perl is open source software that can be downloaded free of charge from http://www.perl.org.)  Commenting out Updates is done only to optimize performance.  Not commenting out any Updates is always safe, but will mean that the performance of the journal will be less than optimal.  One of the calls to Update needed to be uncommented out for one of the shapes.  This happened because the Sketch.AddGeometry infers coincident constraints based on the location of other curves in the sketch, so Update needed to be performed so that the curves would be in the correct place in order to infer coincident constraints.  In applying this approach to other journals, you may need to experiment with commenting and uncommenting out Updates in order to find out which Updates can be commented out without changing the meaning of the journal.  