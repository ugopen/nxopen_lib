file2points.vb example

This example shows a journal which allows the user to select
a text file and create a set of points in the work part
from the data in the file. It is a reimplementation of
the file2points grip program in Visual Basic .Net and show
using the .Net open file dialog together with .Net IO to
read a text file. The grip program is provided for comparison.

HOW TO RUN THE EXAMPLE
- Open a part or a new part.
- Run the .vb file from the journal manager dialog.
- You will be prompted for an input file.  This file should 
contain the points that you want to create.  An example has been 
provided = points.txt.  Its contents are described below.
- Select the input file and hit OK.
- The points from the file will be created in the part.


DESIGN NOTES
This uses the .Net Windows Forms open file dialog to select
a .txt file. The file is read a line at a time and the
line is parsed into 3 doubles. Points are created using
this data.

The points are created invisible and must be made visible explicitly.


FILE FORMAT
The text file read should have one point per line. Each
point is a comma separated list of three numbers. An Example
to create points at the corners of a square is:

--- start of file ---
0,0,0
1,0,0
1,1,0
0,1,0
--- end of file ---
