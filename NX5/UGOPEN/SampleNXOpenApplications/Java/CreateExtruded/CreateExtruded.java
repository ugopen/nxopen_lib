/*==================================================================================================

            Copyright (c) 2004 UGS PLM Solutions.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example to show how to create Fillet.
 
*/

import nxopen.*;
import nxopen.uf.*;
import java.io.PrintWriter;
import java.io.StringWriter;

public class CreateExtruded
{
    public static final double PI = 3.14159265358979324;
    public static void main(String[] args) throws Exception
    {
        Session theSession = null;
        UFSession theUFSession = null;
		try
        {
             theSession = (Session)SessionFactory.get("Session");
             theUFSession = (UFSession)SessionFactory.get("UFSession");
             theUFSession.ui().openListingWindow();
             theUFSession.ui().writeListingWindow("Session and UFSession are created.\n");
            
             UFPart ufPart = theUFSession.part();
             UFCurve ufCurve = theUFSession.curve();
             Tag partData = ufPart.newPart("CreateExtruded", 2);
             if(partData == null)
             {
                theUFSession.ui().writeListingWindow("null Tag");
             }

             String partNameData = ufPart.askPartName(partData);

             double[] l1_endpt1 = {-1.4476606170268,2.3788333712953,0.0};
             double[] l1_endpt2 = { 1.5471310496399,2.2539419253757,0.0};
             double[] l2_endpt1 = {-1.4476606170268,1.2548103580189,0.0};
             double[] l2_endpt2 = { 1.5471310496399,1.3797018039385,0.0};
             double[] l3_endpt1 = {-1.4710981170268,1.8168218646571,0.0};
             double[] l3_endpt2 = { 1.5289018829732,1.8168218646571,0.0};
             double[] direction = {0.0,0.0,1.0};
             double[] ref_pt= new double[3];
             double arc1_start_ang = (PI/180)*87.611984536731;
             double arc1_end_ang   = (PI/180)*272.38801546327;
             double arc1_rad       = 0.5625;
             double arc2_start_ang = (PI/180)*272.38801546327;
             double arc2_end_ang   = (PI/180)*447.61198453673;
             double arc2_rad       = 0.4375;
             String taper_angle = "0.0";
             String[] limit1 = {"1.0", "1.25"};
             int i, count = 4;
             nxopen.Tag[] objarray= new nxopen.Tag[5];
             nxopen.Tag wcs_tag, matrix_tag;
             nxopen.Tag[] loop_list, features;
             UFCurve.Line line1 = new UFCurve.Line();
             UFCurve.Line line2 = new UFCurve.Line();
             UFCurve.Line line3 = new UFCurve.Line();
             UFCurve.Arc arc1 = new UFCurve.Arc();
             UFCurve.Arc arc2 = new UFCurve.Arc();
            
             line1.startPoint = new double[3];
             line1.startPoint[0] = l1_endpt1[0];
             line1.startPoint[1] = l1_endpt1[1];
             line1.startPoint[2] = l1_endpt1[2];
             line1.endPoint = new double[3];
             line1.endPoint[0]   = l1_endpt2[0];
             line1.endPoint[1]   = l1_endpt2[1];
             line1.endPoint[2]   = l1_endpt2[2];
            
             line2.startPoint = new double[3];
             line2.startPoint[0] = l2_endpt1[0];
             line2.startPoint[1] = l2_endpt1[1];
             line2.startPoint[2] = l2_endpt1[2];
             line2.endPoint = new double[3];
             line2.endPoint[0]   = l2_endpt2[0];
             line2.endPoint[1]   = l2_endpt2[1];
             line2.endPoint[2]   = l2_endpt2[2];
            
             line3.startPoint = new double[3];
             line3.startPoint[0] = l3_endpt1[0];
             line3.startPoint[1] = l3_endpt1[1];
             line3.startPoint[2] = l3_endpt1[2];
             line3.endPoint = new double[3];
             line3.endPoint[0]   = l3_endpt2[0];
             line3.endPoint[1]   = l3_endpt2[1];
             line3.endPoint[2]   = l3_endpt2[2];
            
             arc1.startAngle   = arc1_start_ang;
             arc1.endAngle     = arc1_end_ang;
             arc1.arcCenter = new double[3];
             arc1.arcCenter[0] = l3_endpt1[0];
             arc1.arcCenter[1] = l3_endpt1[1];
             arc1.arcCenter[2] = l3_endpt1[2];
             arc1.radius        = arc1_rad;
             arc2.startAngle   = arc2_start_ang;
             arc2.endAngle     = arc2_end_ang;
             arc2.arcCenter = new double[3];
             arc2.arcCenter[0] = l3_endpt2[0];
             arc2.arcCenter[1] = l3_endpt2[1];
             arc2.arcCenter[2] = l3_endpt2[2];
             arc2.radius        = arc2_rad;
            
             Tag lineData1 = ufCurve.createLine(line1);
             Tag lineData2 = ufCurve.createLine(line2);
             Tag lineData3 = ufCurve.createLine(line3);
             
             UFCsys ufCsys = theUFSession.csys();
             Tag wcsData = ufCsys.askWcs();
             Tag matrixOfObjectData = ufCsys.askMatrixOfObject(wcsData);
             arc1.matrixTag = matrixOfObjectData;
             arc2.matrixTag = matrixOfObjectData;
             Tag arcData1 = ufCurve.createArc(arc1);
             Tag arcData2 = ufCurve.createArc(arc2);
             
             nxopen.Tag[] loopList = new nxopen.Tag[4];              
             loopList[0] = lineData1;
             loopList[1] = lineData2;
             loopList[2] = arcData1;
             loopList[3] = arcData2;
             
             UFModl ufModl = theUFSession.modl();

             Tag[] extrudedData = ufModl.createExtruded(loopList, taper_angle, limit1,
                 ref_pt, direction, UFModl.FeatureSigns.NULLSIGN);
             theUFSession.ui().writeListingWindow("Part file is created successfully.\n");
             ufPart.save();
             
             return;
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
