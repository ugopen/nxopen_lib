/*==================================================================================================

            Copyright (c) 2004 UGS PLM Solutions.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example to show how to create Arc thru 3 points.
 
*/

import nxopen.*;
import nxopen.uf.*;
import java.io.PrintWriter;
import java.io.StringWriter;


public class CreateArcThru3pts 
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
            UFPart  ufPart = theUFSession.part();
            
            TaggedObjectManager theTaggedObjectManager= theSession.taggedObjectManager();
        
            Part part1 = theSession.parts().newDisplay("CreateArcThru3pts", Part.Units.INCHES);
            
            double point_coord1[] = new double[3];
            point_coord1[0] = 5.0;
            point_coord1[1] = 10.0;
            point_coord1[2] = 0.0;

            double point_coord2[] = new double[3];
            point_coord2[0] = 10.0;
            point_coord2[1] = 5.0;
            point_coord2[2] = 0.0;
            double point_coord3[] = new double[3];
            point_coord3[0] = 15.0;
            point_coord3[1] = 10.0;
            point_coord3[2] = 0.0;
                                        
            double point_coord4[] = new double[3];
            point_coord4[0] = -5.0;
            point_coord4[1] = 10.0;
            point_coord4[2] = 0.0;
            double point_coord5[] = new double[3];
            point_coord5[0] = -10.0;
            point_coord5[1] = 15.0;
            point_coord5[2] = 0.0;
            double point_coord6[] = new double[3];
            point_coord6[0] = -15.0;
            point_coord6[1] = 10.0;
            point_coord6[2] = 0.0;

            Tag pointData = ufCurve.createPoint(point_coord1);
            Tag createArcThru3ptsData2 = ufCurve.createArcThru3pts(1,point_coord4,point_coord5,point_coord6);
            Tag createArcThru3ptsData1 = ufCurve.createArcThru3pts(1,point_coord1,point_coord2,point_coord3);
            
            Curve theCurve = (Curve)theTaggedObjectManager.get(createArcThru3ptsData2);
            
            theUFSession.modeling().update();
            theUFSession.view().fitView(theUFSession.view().askWorkView(),1.0);
            theUFSession.ui().writeListingWindow("\nArc is created");
            ufPart.save();

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
