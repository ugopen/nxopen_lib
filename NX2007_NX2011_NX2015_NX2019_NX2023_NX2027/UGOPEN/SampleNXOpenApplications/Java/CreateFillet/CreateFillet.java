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

public class CreateFillet
{
    public static final double DEGRA = .01745329251994328;
    public static final int UF_CURVE_2_CURVE = 0;
    
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
            Tag partData = ufPart.newPart("CreateFillet", 2);
            if(partData == null)
            {
                theUFSession.ui().writeListingWindow("null Tag");
            }
                        
            String partNameData = ufPart.askPartName(partData);
            theUFSession.ui().writeListingWindow("Part file specification :    "+ partNameData);

            double[] center= new double[3];
            double radius;
            int[] trimOpts = new int[3];
            int[] arcOpts={0,0,0};
            UFCurve.Line lineCoords1 = new UFCurve.Line();
            lineCoords1.startPoint = new double[3];
            lineCoords1.startPoint[0] = 1.2;
            lineCoords1.startPoint[1] = 0.2;
            lineCoords1.startPoint[2] = 0.0;
            lineCoords1.endPoint = new double[3];
            lineCoords1.endPoint[0] = -0.5;
            lineCoords1.endPoint[1] = 2.5;
            lineCoords1.endPoint[2] = 0.0;
            
            UFCurve.Arc arcCoords1 = new UFCurve.Arc();        
            arcCoords1.matrixTag = Tag.NULL;
            arcCoords1.startAngle =238*DEGRA ;
            arcCoords1.endAngle = 357*DEGRA;
            arcCoords1.arcCenter = new double[3];
            arcCoords1.arcCenter[0] = 0.22;
            arcCoords1.arcCenter[1] = 4.3;
            arcCoords1.arcCenter[2] = 0.0;
            arcCoords1.radius = 2.0;

            UFCurve.Arc arcCoords2 = new UFCurve.Arc();        
            arcCoords2.matrixTag = Tag.NULL;
            arcCoords2.startAngle = 82*DEGRA ;
            arcCoords2.endAngle = 175*DEGRA;
            arcCoords2.arcCenter=new double[3];
            arcCoords2.arcCenter[0] = 3.0;
            arcCoords2.arcCenter[1] = 0.43;
            arcCoords2.arcCenter[2] = 0.0;
            arcCoords2.radius = 2.0;
            
            Tag line1,line2,arc1,arc2;
            nxopen.Tag[] curveObjs= new Tag[3];
            Tag fillet_obj1,fillet_obj2;

            
            /* create a line */
            Tag lineData1 = ufCurve.createLine(lineCoords1);

            /* create 2 arcs */
            Tag wcsData = theUFSession.csys().askWcs();
            Tag matrixData = theUFSession.csys().askMatrixOfObject(wcsData);
            arcCoords1.matrixTag = matrixData;
            arcCoords2.matrixTag = matrixData;

            Tag arcData1 = ufCurve.createArc(arcCoords1);
            Tag arcData2 = ufCurve.createArc(arcCoords2);

            /*create fillet between "arc1" and "line1"*/
            curveObjs[0] = arcData1;
            curveObjs[1] = lineData1;
            curveObjs[2] = Tag.NULL;
            center[0] = 0.0;
            center[1] = 2.1;
            center[2] = 0.0;
            radius = .25;
            trimOpts[0] = 1;          /*trim first UFCurve*/
            trimOpts[1] = 1;         /*trim second UFCurve*/
            
            Tag filletData1 = ufCurve.createFillet(UF_CURVE_2_CURVE,curveObjs,
            center, radius, trimOpts, arcOpts);
            /*create fillet between "line1" and "arc2"*/
            curveObjs[0] = lineData1;
            curveObjs[1] = arcData2;
            curveObjs[2] = Tag.NULL;
            center[0] = 0.8;
            center[1] = 1.0;
            center[2] = 0.0;
            radius = .25;
            trimOpts[0] = 1;          /*trim first UFCurve*/
            trimOpts[1] = 1;         /*trim second UFCurve*/
            
            Tag filletDat2 = ufCurve.createFillet(UF_CURVE_2_CURVE,curveObjs,
            center, radius, trimOpts, arcOpts);
            theUFSession.ui().writeListingWindow("\nPart file Created Successfully");
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
