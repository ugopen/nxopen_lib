/*==================================================================================================

            Copyright (c) 2004 UGS PLM Solutions.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example to show how to use NXOpen and NXOpen.UF APIs.
 
*/

import nxopen.*;
import nxopen.uf.*;
import java.io.*;


public class InterOP
{
    public static void main(String[] args) throws Exception
    {
        Session theSession =null;
		UFSession theUfSession =null;
		try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUfSession = (UFSession)SessionFactory.get("UFSession");
                        
            theUfSession.ui().openListingWindow();
            theUfSession.ui().writeListingWindow("Session and UFSession are created.");

            Part part1 = theSession.parts().newDisplay("AcrThru3PtsInterOP", Part.Units.INCHES);
    
            UFPart ufPart1= theUfSession.part();
            //To obtain tag from NX Object, use tag() method on that object.
            ufPart1.rename(part1.tag(),"RenamedInterOPArc");
            boolean boolFamilyInstances = ufPart1.isFamilyInstance(part1.tag()); 
    

            //Fetching Bool(Out)
            if(boolFamilyInstances)
            {
                //Passing Bool(In)
                ufPart1.updateFamilyInstance(part1.tag(),0,true);
                Tag theAskFamilyInstanceData=ufPart1.askFamilyInstance(part1.tag());   
                ufPart1.updateFamilyInstance(theAskFamilyInstanceData, 0, true);
            } 
            ufPart1.isModified( part1.tag());
            //Fetching int (Out)
            int hashKode =ufPart1.hashCode(); 
            theUfSession.ui().writeListingWindow("\nHashcode: "+hashKode);
            String nameData = ufPart1.askPartName(part1.tag());
    
            int askNumParts=ufPart1.askNumParts(); 
            theUfSession.ui().writeListingWindow("\nPartNumber:"+askNumParts);
    
            theUfSession.ui().writeListingWindow("\nPartName:"+nameData);
    
            int unitData = ufPart1.askUnits(part1.tag());
            theUfSession.ui().writeListingWindow("\nPartName :"+ unitData);
    
            double point_coord1[]=new double[3];
                            point_coord1[0]=5.0;
                            point_coord1[1]=10.0;
                            point_coord1[2]=0.0;
            UFCurve ufCurve= theUfSession.curve();
    
            Tag pointData= ufCurve.createPoint(point_coord1);
            //pointData
            double point_coord2[]=new double[3];
                            point_coord2[0]=10.0;
                            point_coord2[1]=5.0;
                            point_coord2[2]=0.0;
            double point_coord3[]=new double[3];
                            point_coord3[0]=15.0;
                            point_coord3[1]=10.0;
                            point_coord3[2]=0.0;
    
                    
            double point_coord4[]=new double[3];
                                                            point_coord4[0]=-5.0;
                                                            point_coord4[1]=10.0;
                                                            point_coord4[2]=0.0;
                            double point_coord5[]=new double[3];
                                                                            point_coord5[0]=-10.0;
                                                                            point_coord5[1]=15.0;
                                                                            point_coord5[2]=0.0;
                            double point_coord6[]=new double[3];
                                                            point_coord6[0]=-15.0;
                                                            point_coord6[1]=10.0;
                                                            point_coord6[2]=0.0;
                                            
    
                                    
            Tag createArcThru3ptsData2=   ufCurve.createArcThru3pts(1,point_coord4,point_coord5,point_coord6);
            //Passing Int(In)           
            Tag createArcThru3ptsData1=   ufCurve.createArcThru3pts(1,point_coord1,point_coord2,point_coord3);                    
            Tag  tag_Createsimplified[]=new Tag[2];
            tag_Createsimplified[0]=createArcThru3ptsData2;
            tag_Createsimplified[1]=createArcThru3ptsData1;
                                    
            //Convert Tag obtained from UF API, to an NXOpen Object 
            TaggedObjectManager theTaggedObjectManager= theSession.taggedObjectManager();
            Curve theCurve=(Curve)theTaggedObjectManager.get(createArcThru3ptsData2);
            int arrInt[]=new int[2];
            arrInt[0]=10;
            arrInt[1]=10;
            
            int color=theCurve.color();
            theUfSession.ui().writeListingWindow("\nCurve color =" +color );
    
            UFCurveLineArc ufCurveLie =theUfSession.curveLineArc();
            ufCurveLie.getClass(); 

            double len=theCurve.getLength();
            theUfSession.ui().writeListingWindow("\nCurve Length =" +len );
            theUfSession.ui().writeListingWindow("\nFinished:");
            theUfSession.modeling().update();
            theUfSession.part().save();
        }
        catch (Exception ex)
        {
			if(theUfSession!=null)
			{
				StringWriter s = new StringWriter();
				PrintWriter p = new PrintWriter(s);
				p.println("Caught exception " + ex );
				ex.printStackTrace(p);
				theUfSession.ui().writeListingWindow("\nFailed");
				//theUFSession.ui().writeListingWindow("\n"+ex.getMessage());
				theUfSession.ui().writeListingWindow("\n"+s.getBuffer().toString());
			}
				
        }

    }

    public static int getUnloadOption() { 
        return BaseSession.LibraryUnloadOption.IMMEDIATELY; 
    }
}
