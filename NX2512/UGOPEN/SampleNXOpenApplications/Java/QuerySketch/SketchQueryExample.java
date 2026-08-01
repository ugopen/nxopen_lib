//
//          Copyright (c) 2005 UGS Corp.
//              All rights reserved
//               Written by V.A.L.
//
//====================================================================================================
//
//====================================================================================================
//
import java.io.PrintStream;
import java.io.FileOutputStream;

import utils.SketchPrinter;
import nxopen.*;
import nxopen.uf.UFConstants;

/** Main class for this example.  See the README file for description.
 */
public class SketchQueryExample 
{
    public static void main(String[] args) throws Throwable
    {
        boolean isBatch = false;
        PrintStream out = null;
        
        //if no arguments are passed, then first argument will be an empty string.
        if(args.length == 1 && args[0].equals(""))
        {
            //No arguments were passed. So skip checking for arguments.
        }
        else
        {
            for (int i = 0; i < args.length; i++)
            {
                if ( args[i].equals("-b"))
                    isBatch = true;
                else if ( args[i].equals("-l"))
                {
                    ++i;
                    if ( args[i].equals("stdout"))
                        out = System.out;
                    else
                        out = new PrintStream(new FileOutputStream(args[i]));
                }
                else if ( args[i].equals("-h") || args[i].equals("-?"))
                {
                    System.out.println(
                            "SketchQueryExample [-b] [-l <logfile>]\n" +
                            "Flags:\n" +
                            "-b              Run in batch mode\n" +
                            "-l <filename>   Print results to the specified file.\n" +
                            "                (\"-l stdout\" will print to stdout)\n");
                    return;
                }
                else
                    throw new Exception("Invalid argument: " + args[i]);
            }
        }
       Session theSession = (Session)SessionFactory.get("Session"); 
       if ( out == null )
            out = new PrintStream(new utils.ListingWindowOutputStream(theSession.listingWindow()));
        SketchPrinter sketchPrinter = new SketchPrinter(out);
        if ( isBatch )
        {
            // Create a sample sketch and print it
            CreateASketch.main(null);
            sketchPrinter.printSketch( theSession, (Sketch)theSession.parts().work().sketches().iterator().next(), "", true);
        }
        else
        {
            // Prompt user to select a sketch and print the selected sketch
            UI theUI = (UI)SessionFactory.get("UI");
            Selection.MaskTriple mask[] = { new Selection.MaskTriple(UFConstants.UF_sketch_type, UFConstants.UF_v13_sketch_subtype, 0) };
            Selection.SelectTaggedObjectData selObj = theUI.selectionManager().selectTaggedObject("Select sketch to query", "Select sketch",
                    Selection.SelectionScope.WORK_PART, Selection.SelectionAction.CLEAR_AND_ENABLE_SPECIFIC,
                    false, false, mask );
            if ( selObj.response == Selection.Response.OBJECT_SELECTED ||
                 selObj.response == Selection.Response.OBJECT_SELECTED_BY_NAME )
                sketchPrinter.printSketch( theSession, (Sketch)selObj.object, "", false);
        }
    }
    public static final int getUnloadOption() { return BaseSession.LibraryUnloadOption.IMMEDIATELY; }
}
