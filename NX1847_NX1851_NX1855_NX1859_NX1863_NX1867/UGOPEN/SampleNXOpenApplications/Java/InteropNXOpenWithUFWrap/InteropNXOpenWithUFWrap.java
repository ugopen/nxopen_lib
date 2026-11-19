/*==================================================================================================

            Copyright (c) 2004 UGS PLM Solutions.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example to show how to create Arc.
 
*/

import nxopen.*;
import nxopen.uf.*;
import java.io.PrintWriter;
import java.io.StringWriter;


public class InteropNXOpenWithUFWrapper 
{
   
    public static void main(String[] args) throws Exception
    {
        Session theSession=null ;
        UFSession theUFSession=null ;

        try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUFSession = (UFSession)SessionFactory.get("UFSession");
            UFCurve ufCurve = theUFSession.curve();
            UFCurve.Arc ufArc = new UFCurve.Arc();
            UFPart ufPart = theUFSession.part();
            UFCsys ufCsys = theUFSession.csys();
            Part part1 = theSession.parts().newDisplay("InteropNXOpenWithUFWrapper", Part.Units.MILLIMETERS);

            Point3d arcStartPoint = new Point3d(-2.45197396411307, 3.58206319143819, 0.0);
            Point3d arcEndPoint = new Point3d(5.32514590979158, -1.0012853802839, 0.0);
            Line line1 = theSession.parts().work().curves().createLine(point3d1, point3d2);
            UFCurve.Line line_coords = theUFSession.curve().askLineData(line1.tag());
            /* Fill out the data structure */
            ufArc.startAngle = 0.0;
            ufArc.endAngle = 3.0;
            ufArc.arcCenter=new double[3];
            ufArc.arcCenter[0] = 0.0;
            ufArc.arcCenter[1] = 0.0;
            ufArc.arcCenter[2] = 1.0;
            ufArc.radius = 2.0;

            Tag wcsData = ufCsys.askWcs();
            ufArc.matrixTag = ufCsys.askMatrixOfObject(wcsData);
            Tag arcTag = ufCurve.createArc(ufArc);
            Arc NXArc = (Arc) theSession.taggedObjectManager().get(arcTag);

            double startAngle = NXArc.startAngle();
            double endAngle = NXArc.endAngle();
            Point3d arcCenter = NXArc.centerPoint();

        }
        catch (Exception ex)
        {
            if(theUFSession!=null)
            {
                StringWriter s = new StringWriter();
                PrintWriter p = new PrintWriter(s);
                theUFSession.ui().openListingWindow();
                p.println("Caught exception " + ex );
                ex.printStackTrace(p);
                theUFSession.ui().writeListingWindow("\nFailed");
                //theUFSession.ui().writeListingWindow("\n"+ex.getMessage());
                theUFSession.ui().writeListingWindow("\n"+s.getBuffer().toString());
            }
        
        
        }
    }

     public static int getUnloadOption() { 
        return BaseSession.LibraryUnloadOption.IMMEDIATELY; 
    }
}
