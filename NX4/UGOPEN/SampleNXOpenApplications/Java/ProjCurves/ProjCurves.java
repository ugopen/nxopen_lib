/*==================================================================================================

            Copyright (c) 2004 UGS PLM Solutions.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example to show how to create ProjCurves using java Wrapped UF API.
@<DEL>@ TEXT ENCLOSED within delete markers will be REMOVED
====================================================================================================
   Date      Name                    Description of Change
10-Mar-2005  Trupti Sahasrabudhe     Intial Creation
06-Apr-2005  Atul Jawale             Updated for modl class break up
21-Apr-2005  Abhishek Mishra         Updated for listing window.
04-May-2005  Trupti Sahasrabudhe       PR5169223: Remove return Data structure if it has one member
07-Jun-2005  Abhishek Mishra         Provided fix for error message	
$HISTORY$
====================================================================================================
TEXT ENCLOSED within delete markers will be REMOVED @<DEL>@ 
*/

import nxopen.*;
import nxopen.uf.*;
import java.io.PrintWriter;
import java.io.StringWriter;


public class ProjCurves
{
    public static final double DEGRA = .01745329251994328;
    public static final int UF_CURVE_2_CURVE = 0;
    

	public static void main(String[] args) throws Exception
    {
		Session     theSession = null;
		UFSession    theUFSession=null;
		try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUFSession = (UFSession)SessionFactory.get("UFSession");
            theUFSession.ui().openListingWindow();
            theUFSession.ui().writeListingWindow("Session and UFSession are created.\n");
            
            UFPart ufPart = theUFSession.part();
            Tag partData = ufPart.newPart("ProjCurves", 2);
            String partNameData = ufPart.askPartName(partData);
			theUFSession.ui().writeListingWindow("Part file specification :    "+ partNameData );

            int num_faces, i, numProjCurves;
            double[] origin={0.0,0.0,0.0};
            nxopen.Tag blockTag;
            nxopen.Tag[] curvesToProj= new nxopen.Tag[1];
            nxopen.Tag projCurveFeature;
            nxopen.Tag[] projCurves;
            nxopen.Tag definingFeature, definingTarget, definingCurve;
            String[] edgeLens={"300.0","25.0","150.0"};
            UFCurve.Line lineData= new UFCurve.Line();
            UFCurve.Proj projData = new UFCurve.Proj();
            nxopen.Tag[] faceList;
            UFModlFeatures ufModlFeatures = theUFSession.modlFeatures();
            UFModlGeneral ufModlGeneral = theUFSession.modlGeneral();
            UFModeling ufModeling = theUFSession.modeling();
            Tag blockData = ufModlFeatures.createBlock1(UFModl.FeatureSigns.NULLSIGN, origin, edgeLens);

            lineData.startPoint = new double[3];
            lineData.startPoint[0] =  25.0;
            lineData.startPoint[1] =  50.0;
            lineData.startPoint[2] =  25.0;
            lineData.endPoint = new double[3]; 
            lineData.endPoint[0]   = 275.0;
            lineData.endPoint[1]   =  50.0;
            lineData.endPoint[2]   = 125.0;

            UFCurve ufCurve = theUFSession.curve();
            Tag curveLineData = ufCurve.createLine(lineData);
            theUFSession.ui().writeListingWindow("\ncurves to project tag: \n" + curveLineData);

            
            curvesToProj[0] =  curveLineData;
            
            Tag[] featFacesData = ufModeling.askFeatFaces(blockData);
            int listCountData = ufModlGeneral.askListCount(featFacesData);
            theUFSession.ui().writeListingWindow("\nList Count: \n" + listCountData);
            for(int j =0; j < listCountData; j++)
            {
                    theUFSession.ui().writeListingWindow("\n"+ featFacesData[j]+ "\n");
            }

            projData.projType = 3;
            projData.projPnt = Tag.NULL;
            projData.projVec = new double[3];
            projData.projVec[0] = 0.0;
            projData.projVec[1] = 1.0;
            projData.projVec[2] = 0.0;
            projData.multiplicity = 2;
            
            Tag projCurvesData = ufCurve.createProjCurves(1, curvesToProj, listCountData, featFacesData, 3, projData);
                        theUFSession.ui().writeListingWindow("\nproj UFCurve feature tag: \n" + projCurvesData);
            UFCurve.AskProjCurvesData projCurvesData1 = ufCurve.askProjCurves(projCurvesData);
        
            for (i = 0; i < projCurvesData1.nCurveRefs; i++)
            {
                UFCurve.AskProjCurveParentsData projCurveParentsData = ufCurve.askProjCurveParents(projCurvesData1.curveRefs[i]);
                            theUFSession.ui().writeListingWindow("\nproj_curves[" + i + "]\n");
                            theUFSession.ui().writeListingWindow("\n  belongs to feature tag: \n" + projCurveParentsData.definingFeature);
                            theUFSession.ui().writeListingWindow("\n  was projected onto tag: \n" + projCurveParentsData.definingTarget);
                            theUFSession.ui().writeListingWindow("\n  was generated by UFCurve tag: \n" + projCurveParentsData.definingCurve);
            }
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
