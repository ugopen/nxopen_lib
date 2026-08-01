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

public class CreateBSurface 
{
    public static void main(String[] args)  throws Exception
    {
         Session theSession = null;
         UFSession theUFSession = null;
		try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUFSession = (UFSession)SessionFactory.get("UFSession");
            
            /* Open Listing Window */
            theUFSession.ui().openListingWindow();
            theUFSession.ui().openListingWindow();
            theUFSession.ui().writeListingWindow("Session and UFSession are created");
            UFPart  ufPart = theUFSession.part();
            
            String part_name = "CreateBSurface";
            int units = 2; 
            Tag partData = ufPart.newPart(part_name, units);

            String partNameData = ufPart.askPartName(partData);
            theUFSession.ui().writeListingWindow("\nLoaded: " + partNameData + "\n");
            
            int[]    bsurf_idata = {4,4,4,4};
            double[] bsurf_uknot = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0};
            double[] bsurf_vknot = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0};
            double[] bsurf_poles = {0.0,0.0,6.0,1.0,
                                       2.0,2.0,6.0,1.0,
                                       5.0,1.5,6.0,1.0,
                                       8.0,3.0,6.0,1.0,
                                       0.0,2.0,4.0,1.0,
                                       2.0,4.0,4.0,1.0,
                                       5.0,3.5,4.0,1.0,
                                       8.0,5.0,4.0,1.0,
                                       0.0,2.0,2.0,1.0,
                                       2.0,4.0,2.0,1.0,
                                       5.0,3.5,2.0,1.0,
                                       8.0,5.0,2.0,1.0,
                                       0.0,0.0,0.0,1.0,
                                       2.0,2.0,0.0,1.0,
                                       5.0,1.5,0.0,1.0,
                                       8.0,3.0,0.0,1.0} ;
            int[]    bcurv1_idata = {3,3} ;
            double[] bcurv1_knots = {0.0,0.0,0.0,1.0,1.0,1.0};
            double[] bcurv1_poles = {-0.5,-2.5,3.5,1.0,
                                        2.5,-2.5,3.5,1.0,
                                        2.5,-2.5,6.5,1.0};
            
            int[]    bcurv2_idata = {8,4} ;
            double[] bcurv2_knots = {-0.6,-0.4,-0.2,0.0,0.2,
                                        0.4, 0.6, 0.8,1.0,1.2,
                                        1.4, 1.6};
            double[] bcurv2_poles = {3.0,-2.5,2.0,1.0,
                                        4.0,-2.5,1.0,1.0,
                                        7.0,-2.5,1.0,1.0,
                                        6.0,-2.5,3.0,1.0,
                                        3.0,-2.5,3.0,1.0,
                                        3.0,-2.5,2.0,1.0,
                                        4.0,-2.5,1.0,1.0,
                                        7.0,-2.5,1.0,1.0};
            double[] proj_vector = {0.0,1.0,0.0};
            double[] ptdata = {1.312,1.896,4.8,
                                  4.464,3.312,2.4};
            
            UFModlGeneral.CreateBsurfData crBsurfData = theUFSession.modlGeneral().createBsurf(bsurf_idata[0],
                            bsurf_idata[1],
                            bsurf_idata[2],
                            bsurf_idata[3],
                            bsurf_uknot,
                            bsurf_vknot,
                            bsurf_poles);
                            
            theUFSession.ui().writeListingWindow("UFModl.CreateBsurf- Successful\n");
            theUFSession.modeling().update();
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
