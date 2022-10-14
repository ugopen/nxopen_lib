/*==================================================================================================

            Copyright (c) 2004 UGS PLM Solutions.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example to show how to create a Block with blending edges.
 
*/

import nxopen.*;
import nxopen.uf.*;
import java.io.*;
import java.util.*;

public class ModlCreateBlend
{
    public static void main(String[] args) throws Exception
    {
        Session     theSession = null;
		UFSession    theUFSession =null;
		try
        {
            String part_name = new String("ModlCreateBlend");
            int units =2; 
            theSession = (Session)SessionFactory.get("Session");
            theUFSession = (UFSession)SessionFactory.get("UFSession");
            theUFSession.ui().openListingWindow();
            theUFSession.ui().writeListingWindow("Session and UFSession are created");
            UFPart  ufPart = theUFSession.part();
            Tag the_NewPartData= ufPart.newPart(part_name, units);
            String the_AskPartNameData =ufPart.askPartName(the_NewPartData);
            theUFSession.ui().writeListingWindow("\nPart file specification :    "+ the_AskPartNameData);
			nxopen.Tag      block_tag;
            double[]        corner_point= new double[3];
            String []       edge_lengths = { "1.0", "2.0", "3.0" };
            nxopen.Tag      block_feature_tag;
            UFFacet.Parameters faceting_params = new UFFacet.Parameters();
            int ecount;
            nxopen.Tag      blend1;
            double[]     pt1={0.0, 0.0, 0.0};
            double[]     pt2={0.0, 0.0, 0.0}; 
            int          allow_smooth = 1;
            int          allow_cliff = 1;
            int          allow_notch = 1;
            double       vrb_tol = 1.0;
            /*First create a UFPart in which we will initially create a
                            block.*/
            theUFSession.assem().setWorkPart(the_NewPartData);
            corner_point[0] = 0.0;
            corner_point[1] = 0.0;
            corner_point[2] = 0.0;
            Tag theCreateBlock1Data= theUFSession.modlFeatures().createBlock1(UFModl.FeatureSigns.NULLSIGN,
                                                        corner_point,
                                                        edge_lengths);
            Tag theAskFeatBodyData=  theUFSession.modeling().askFeatBody(theCreateBlock1Data);

            /* Get the edges of the body.  Get the count of the edge list.
            * This will be used to get the four 'vertical' corners of the block for
            * blending. Check return codes.
            */
            Tag[] theAskBodyEdgesData = theUFSession.modeling().askBodyEdges(theAskFeatBodyData);
            int theAskListCountData = theUFSession.modlGeneral().askListCount(theAskBodyEdgesData);
            ArrayList arr_list2 = new ArrayList();
            for(int i=0; i < theAskListCountData; i++) 
            {
                int vcount;             /* count of vertices in edge */
                /* Get the edge (list item) and check return code.  */
                Tag theAskListItemData =theUFSession.modlGeneral().askListItem(theAskBodyEdgesData,i);
                /* Get the edge vertices.  Check return code.  */
                UFModeling.AskEdgeVertsData theAskEdgeVertsData =theUFSession.modeling().askEdgeVerts(theAskListItemData);
                if(Math.abs(Math.abs(theAskEdgeVertsData.point1[2] - theAskEdgeVertsData.point2[2]) - 3.0) < 0.001)
                {
                    arr_list2.add(theAskListItemData);
                }
            }
            nxopen.Tag[]    list2=new Tag[arr_list2.size()];
            for(int i=0;i<arr_list2.size();i++)
            {
                list2[i]=(Tag)arr_list2.get(i);
            }
            Tag theCreateBlendData=theUFSession.modlFeatures().createBlend("0.199246", list2, allow_smooth,allow_cliff, allow_notch, vrb_tol);
            theUFSession.ui().writeListingWindow("\nBlock with blending edges created");
            String theAskBlendParmsData =theUFSession.modlFeatures().askBlendParms(theCreateBlendData,0);
            theUFSession.ui().writeListingWindow("\nBlend Radius=" + theAskBlendParmsData);
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
