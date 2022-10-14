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


public class CreateArc 
{
   
    public static void main(String[] args) throws Exception
    {
        Session theSession=null ;
        UFSession theUFSession=null ;

        try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUFSession = (UFSession)SessionFactory.get("UFSession");
            theUFSession.ui().openListingWindow();
            theUFSession.ui().writeListingWindow("Session and UFSession are created");
            UFCurve ufCurve = theUFSession.curve();
            UFCurve.Arc ufArc = new UFCurve.Arc();
            UFPart ufPart = theUFSession.part();
            UFCsys ufCsys = theUFSession.csys();
            Part part1 = theSession.parts().newDisplay("CreateArc", Part.Units.INCHES);

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
            Tag arcData = ufCurve.createArc(ufArc);
            UFCurve.Arc theAskArcData=  ufCurve.askArcData(arcData);
            theUFSession.ui().writeListingWindow("\nX Coordinate: "+theAskArcData.arcCenter[0]+"\n");
            theUFSession.ui().writeListingWindow("Y Coordinate: "+theAskArcData.arcCenter[1]+"\n");
            theUFSession.ui().writeListingWindow("Z Coordinate: "+theAskArcData.arcCenter[2]+"\n");
            theUFSession.ui().writeListingWindow("Start Angle: "+theAskArcData.startAngle+"\n");
            theUFSession.ui().writeListingWindow("End Angle: "+theAskArcData.endAngle+"\n");
            theUFSession.ui().writeListingWindow("arcRadius: "+theAskArcData.radius);
            theUFSession.ui().writeListingWindow("\nCreated successfully");

        }
        catch (Exception ex)
        {
            if(theUFSession!=null)
            {
                StringWriter s = new StringWriter();
                PrintWriter p = new PrintWriter(s);
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
