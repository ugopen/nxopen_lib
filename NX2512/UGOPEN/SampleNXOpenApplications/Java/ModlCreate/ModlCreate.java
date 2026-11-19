/*==================================================================================================

            Copyright (c) 2004 UGS PLM Solutions.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example to show how to create a cylinder with groove.
 
*/

import nxopen.*;
import nxopen.uf.*;
import java.io.*;

public class ModlCreate
{
    public static void main(String[] args) throws Exception
    {
        
         Session     theSession = null;
         UFSession    theUFSession=null;
        try
        {
           
            String part_name = new String("ModlCreate");
            int units =2; 
            theSession = (Session)SessionFactory.get("Session");
            theUFSession = (UFSession)SessionFactory.get("UFSession");
            theSession.listingWindow().open();
            theSession.listingWindow().writeLine("Session and UFSession are created.\n");
            UFPart  ufPart = theUFSession.part();
            nxopen.Tag the_NewPartData= ufPart.newPart(part_name, units);
            String the_AskPartNameData =ufPart.askPartName(the_NewPartData);
            theSession.listingWindow().writeLine("Part file specification :    "+ the_AskPartNameData);
            int count;
            int i;
            int type;
            int norm_dir;
            nxopen.Tag  face, feature_id, body;
            nxopen.Tag face_id = nxopen.Tag.NULL;
            double[] origin = {0.0, 0.0, 0.0};
            double[] direction = {0.0, 0.0, 1.0};
            double[] center= new double[3];
            double[] dir= new double[3];
            double[] box= new double[6];
            double radius;
            double rad_data;
            double[] location = {0.0,0.0,2.0};
            String height = "4.0";
            String diam   = "2.0";
            String gr_diam = "1.0";
            String width = "1.0";
            nxopen.Tag[] theCreateListData=theUFSession.modlGeneral().createList();
            nxopen.Tag theCreateCyl1Data= theUFSession.modlFeatures().createCyl1(UFModl.FeatureSigns.NULLSIGN,origin,height,diam,direction);
            nxopen.Tag theAskFeatBodyData = theUFSession.modeling().askFeatBody(theCreateCyl1Data); 
            theSession.listingWindow().writeLine("\nBody is: "+ theAskFeatBodyData);
            nxopen.Tag[] theAskBodyFacesData= theUFSession.modeling().askBodyFaces(theAskFeatBodyData);
            theSession.listingWindow().writeLine("\nFace_list is: "+ theAskBodyFacesData.length);
            
            int theAskListCountData= theUFSession.modlGeneral().askListCount(theAskBodyFacesData);
            theSession.listingWindow().writeLine("\nCount is: "+ theAskListCountData);
            for(i = 0; i < theAskListCountData; i++) 
            {
                nxopen.Tag theAskListItemData= theUFSession.modlGeneral().askListItem(theAskBodyFacesData,i);
                
                theSession.listingWindow().writeLine("\nface is: "+ theAskListItemData);
                int theAskFaceTypeData= theUFSession.modeling().askFaceType(theAskListItemData);
                if(theAskFaceTypeData == UFConstants.UF_cylinder_type) 
                {
                    face_id= theAskListItemData;
                }
            }
  
            nxopen.Tag theCreateRectGroove =theUFSession.modlFeatures().createRectGroove(location,direction,gr_diam,width,face_id);
            
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
                theSession.listingWindow().writeLine("\nFailed");
                theSession.listingWindow().writeLine("\n"+s.getBuffer().toString());
            }
        }
    }

    public static int getUnloadOption() { 
        return BaseSession.LibraryUnloadOption.IMMEDIATELY; 
    }
}
