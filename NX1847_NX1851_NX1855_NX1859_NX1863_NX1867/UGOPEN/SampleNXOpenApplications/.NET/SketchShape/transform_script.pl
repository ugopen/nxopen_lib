#
#          Copyright (c) 2004 UGS PLM Solutions
#                  All rights reserved
#          Written by V.A.L.

# This script was tested with perl version 5.8.0.

use strict;

if ( not $ARGV[0] or $ARGV[0] =~ /^-([?hH]) / )
{
   print <<USAGE;
Usage:
    transform_script.pl <name of journal file>

Does substitutions on a recorded journal file that operates on an 
active sketch, in order to make the journal applicable to other sketches and
to improve the journals performance.
The result is written to a file named <name of journal file>.out.vb.
In order to used this script on journal file, the journal file should be:
1. unedited
2. recorded entirely while in the sketcher task environment
3. you should not have activated a different sketch while recording the journal
4. you should not have invoked undo while creating the journal
This script will comment out calls to Update.  You may need to uncomment out
some of these calls.
USAGE
    exit 0;
}

open IN, $ARGV[0] or die;

my @lines = <IN>;
close IN;

foreach my $line (@lines)
{
    # Put opening statements at the beginning of the journal
    if ( $line =~ /Dim theUI As UI = UI\.GetUI\(\)/ )
    {
        $line = <<EOF;
Dim workPart As Part = theSession.Parts.Work
Dim activeSketch As Sketch = Session.ActiveSketch
Dim transform As Transform = New Transform(activeSketch.Origin, activeSketch.Orientation.Element)
theSession.SetUndoMark(Session.MarkVisibility.Visible, \"Create shape\")
EOF
        next;
    }
    # change theSession.ActiveSketch and theSession.Parts.Work to activeSketch and workPart
    # This is not neccessary, but makes the journal look nicer
    $line =~ s/theSession\.ActiveSketch/activeSketch/g;
    $line =~ s/theSession\.Parts\.Work/workPart/g;
    
    # apply transform to every coordinate
    $line =~ s/(New Point3d\([^)]*\))/transform.Apply($1)/g;
    # apply transform to every point in any Sketch.ConstraintGeometryHelp structure
    if ($line =~ /(sketch_ConstraintGeometryHelp\d+)\.parameter = / )
    {
        my $varName = $1;
        $line .= "$varName.point = transform.Apply($varName.point)\n\n";
    }
    
    # Replace workPart.FindObject("NXMATRIX WCS") with activeSketch.Orientation
    # This is not necessary, but make the journal look nicer
    $line =~ s/CType\(workPart\.FindObject\(\"NXMATRIX WCS\"\),\s*NXMatrix\)/activeSketch.Orientation/g;
    
    # Comment out activeSketch.Update to improve performance
    $line =~ s/^(\s*)(activeSketch\.Update)/$1' $2/;
    
    # Comment out the manipulation of undo marks
    if ( $line =~ /(Dim session_UndoMarkId\d+ As Session\.UndoMarkId)|(theSession\.(SetUndoMark|DeleteUndoMark|SetUndoMarkVisibility))/ )
    {
        $line =~ m/^\s*/;
        my $whiteSpace = $&;
        $line = $';    
        $line = "${whiteSpace}' $line";
    }
}

open OUT, ">$ARGV[0].out.vb" or die;

print OUT @lines;

close OUT;
