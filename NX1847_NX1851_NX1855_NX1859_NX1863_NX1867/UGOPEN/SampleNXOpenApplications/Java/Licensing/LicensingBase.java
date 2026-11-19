/*==================================================================================================

            Copyright 2010 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example of java journal
 
*/

import nxopen.*;

public class LicensingBase 
{

    /**
       Journal record as of NX75 that creates a part, creates a sketch with a line in it, and saves the part.
    */
    public static void doWork(Session theSession) throws Exception
    {
        // ----------------------------------------------
        //   Menu: File->New...
        // ----------------------------------------------
        int markId1;
        markId1 = theSession.setUndoMark(nxopen.Session.MarkVisibility.VISIBLE, "Start");
        
        FileNew fileNew1;
        fileNew1 = theSession.parts().fileNew();
        
        theSession.setUndoMarkName(markId1, "84New Dialog");
        
        int markId2;
        markId2 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "84New");
        
        fileNew1.setTemplateFileName("model-plain-1-mm-template.prt");
        
        fileNew1.setApplicationName("ModelTemplate");
        
        fileNew1.setUnits(nxopen.Part.Units.MILLIMETERS);
        
        fileNew1.setNewFileName("line.prt");
        
        fileNew1.setMasterFileName("");
        
        fileNew1.setUseBlankTemplate(false);
        
        fileNew1.setMakeDisplayedPart(true);
        
        NXObject nXObject1;
        nXObject1 = fileNew1.commit();
        
        Part workPart = theSession.parts().work();
        Part displayPart = theSession.parts().display();
        theSession.deleteUndoMark(markId2, null);
        
        fileNew1.destroy();
        
        int markId3;
        markId3 = theSession.setUndoMark(nxopen.Session.MarkVisibility.VISIBLE, "Enter Modeling");
        
        // ----------------------------------------------
        //   Menu: Insert->Sketch Curve->Line...
        // ----------------------------------------------
        int markId4;
        markId4 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "Profile short list");
        
        int markId5;
        markId5 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "Curve");
        
        Point3d coordinates1 = new Point3d(0.0, 0.0, 0.0);
        Point point1;
        point1 = workPart.points().createPoint(coordinates1);
        
        Point3d origin1 = new Point3d(0.0, 0.0, 0.0);
        Vector3d vector1 = new Vector3d(0.0, 0.0, 1.0);
        Direction direction1;
        direction1 = workPart.directions().createDirection(origin1, vector1, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);
        
        Point3d origin2 = new Point3d(0.0, 0.0, 0.0);
        Vector3d vector2 = new Vector3d(1.0, 0.0, 0.0);
        Direction direction2;
        direction2 = workPart.directions().createDirection(origin2, vector2, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);
        
        Xform xform1;
        xform1 = workPart.xforms().createXformByPointXDirZDir(point1, direction2, direction1, nxopen.SmartObject.UpdateOption.WITHIN_MODELING, 0.625);
        
        CartesianCoordinateSystem cartesianCoordinateSystem1;
        cartesianCoordinateSystem1 = workPart.coordinateSystems().createCoordinateSystem(xform1, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);
        
        nxopen.features.Feature nullFeatures_Feature = null;
        
        nxopen.features.DatumCsysBuilder datumCsysBuilder1;
        datumCsysBuilder1 = workPart.features().createDatumCsysBuilder(nullFeatures_Feature);
        
        datumCsysBuilder1.setCsys(cartesianCoordinateSystem1);
        
        datumCsysBuilder1.setDisplayScaleFactor(1.25);
        
        nxopen.features.Feature feature1;
        feature1 = datumCsysBuilder1.commitFeature();
        
        datumCsysBuilder1.destroy();
        
        Sketch nullSketch = null;
        SketchInPlaceBuilder sketchInPlaceBuilder1;
        sketchInPlaceBuilder1 = workPart.sketches().createSketchInPlaceBuilder2(nullSketch);
        
        nxopen.Point3d origin1_1= new nxopen.Point3d(0.0, 0.0, 0.0);
        nxopen.Vector3d normal1_1 = new nxopen.Vector3d(0.0, 0.0, 1.0);
        nxopen.Plane plane1;
        plane1 = workPart.planes().createPlane(origin1_1, normal1_1, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);
        sketchInPlaceBuilder1.setPlaneReference(plane1);

        DatumPlane datumPlane1 = ((DatumPlane)workPart.datums().findObject("DATUM_CSYS(1) YZ plane"));
        
        plane1.setMethod(nxopen.PlaneTypes.MethodType.DISTANCE);
        nxopen.NXObject [] geom1  = new nxopen.NXObject[1];
        geom1[0] = datumPlane1;
        plane1.setGeometry(geom1);
        plane1.setFlip(false);
        plane1.setReverseSide(false);
        nxopen.Expression expression1_1;
        expression1_1 = plane1.expression();
        expression1_1.setRightHandSide("0");
    
        plane1.setAlternate(nxopen.PlaneTypes.AlternateType.ONE);
        plane1.evaluate();
        
        DatumAxis datumAxis1 = ((DatumAxis)workPart.datums().findObject("DATUM_CSYS(1) X axis"));
        
        nxopen.Direction direction1_1;
        direction1_1 = workPart.directions().createDirection(datumAxis1, nxopen.Sense.FORWARD, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);
        sketchInPlaceBuilder1.setAxisReference(direction1_1);

        nxopen.features.DatumCsys datumCsys1 = ((nxopen.features.DatumCsys)feature1);
        Point point2 = ((Point)datumCsys1.findObject("ENTITY 2 1 1"));
        sketchInPlaceBuilder1.setSketchOrigin(point2);
        
        sketchInPlaceBuilder1.setPlaneOption(nxopen.Sketch.PlaneOption.EXISTING_PLANE);
        
        NXObject nXObject2;
        nXObject2 = sketchInPlaceBuilder1.commit();
        
        sketchInPlaceBuilder1.destroy();
        
        Sketch sketch1 = ((Sketch)nXObject2);
        sketch1.activate(nxopen.Sketch.ViewReorient.FALSE);
        
        theSession.setUndoMarkVisibility(markId5, "Curve", nxopen.Session.MarkVisibility.VISIBLE);
        
        Point3d startPoint1 = new Point3d(-10.0627135255169, -130.580700794749, -3.5527136788005e-015);
        Point3d endPoint1 = new Point3d(-85.1781635712592, 10.6909140626799, -3.5527136788005e-015);
        Line line1;
        line1 = workPart.curves().createLine(startPoint1, endPoint1);
        
        theSession.activeSketch().addGeometry(line1, nxopen.Sketch.InferConstraintsOption.INFER_NO_CONSTRAINTS);
        
        nxopen.Sketch.DimensionGeometry dimObject1_1 = new nxopen.Sketch.DimensionGeometry();
        dimObject1_1.geometry = line1;
        dimObject1_1.assocType = nxopen.Sketch.AssocType.START_POINT;
        dimObject1_1.assocValue = 0;
        dimObject1_1.helpPoint.x = 0.0;
        dimObject1_1.helpPoint.y = 0.0;
        dimObject1_1.helpPoint.z = 0.0;
        NXObject nullNXObject = null;
        dimObject1_1.view = nullNXObject;
        nxopen.Sketch.DimensionGeometry dimObject2_1 = new nxopen.Sketch.DimensionGeometry();
        dimObject2_1.geometry = line1;
        dimObject2_1.assocType = nxopen.Sketch.AssocType.END_POINT;
        dimObject2_1.assocValue = 0;
        dimObject2_1.helpPoint.x = 0.0;
        dimObject2_1.helpPoint.y = 0.0;
        dimObject2_1.helpPoint.z = 0.0;
        dimObject2_1.view = nullNXObject;
        Point3d dimOrigin1 = new Point3d(-35.6110876852614, -53.559408243978, -3.5527136788005e-015);
        Expression nullExpression = null;
        SketchDimensionalConstraint sketchDimensionalConstraint1;
        sketchDimensionalConstraint1 = theSession.activeSketch().createDimension(nxopen.Sketch.ConstraintType.PARALLEL_DIM, dimObject1_1, dimObject2_1, dimOrigin1, nullExpression, nxopen.Sketch.DimensionOption.CREATE_AS_AUTOMATIC);
        
        SketchHelpedDimensionalConstraint sketchHelpedDimensionalConstraint1 = ((SketchHelpedDimensionalConstraint)sketchDimensionalConstraint1);
        nxopen.annotations.Dimension dimension1;
        dimension1 = sketchHelpedDimensionalConstraint1.associatedDimension();
        
        Expression expression1;
        expression1 = sketchHelpedDimensionalConstraint1.associatedExpression();
        
        nxopen.Sketch.DimensionGeometry dimObject1_2 = new nxopen.Sketch.DimensionGeometry();
        dimObject1_2.geometry = line1;
        dimObject1_2.assocType = nxopen.Sketch.AssocType.START_POINT;
        dimObject1_2.assocValue = 0;
        dimObject1_2.helpPoint.x = -10.0627135255169;
        dimObject1_2.helpPoint.y = -130.580700794749;
        dimObject1_2.helpPoint.z = -3.5527136788005e-015;
        dimObject1_2.view = nullNXObject;
        nxopen.Sketch.DimensionGeometry dimObject2_2 = new nxopen.Sketch.DimensionGeometry();
        dimObject2_2.geometry = datumAxis1;
        dimObject2_2.assocType = nxopen.Sketch.AssocType.END_POINT;
        dimObject2_2.assocValue = 0;
        dimObject2_2.helpPoint.x = 28.575;
        dimObject2_2.helpPoint.y = 0.0;
        dimObject2_2.helpPoint.z = 0.0;
        dimObject2_2.view = nullNXObject;
        Point3d dimOrigin2 = new Point3d(-67.8350017358393, -7.00525489790014, 0.0);
        SketchDimensionalConstraint sketchDimensionalConstraint2;
        sketchDimensionalConstraint2 = theSession.activeSketch().createDimension(nxopen.Sketch.ConstraintType.ANGULAR_DIM, dimObject1_2, dimObject2_2, dimOrigin2, nullExpression, nxopen.Sketch.DimensionOption.CREATE_AS_AUTOMATIC);
        
        nxopen.annotations.Dimension dimension2;
        dimension2 = sketchDimensionalConstraint2.associatedDimension();
        
        Expression expression2;
        expression2 = sketchDimensionalConstraint2.associatedExpression();
        
        theSession.preferences().sketch().setAutoDimensionsToArcCenter(false);
        
        theSession.activeSketch().update();
        
        theSession.preferences().sketch().setAutoDimensionsToArcCenter(true);
        
        // ----------------------------------------------
        //   Dialog Begin Line
        // ----------------------------------------------
        // ----------------------------------------------
        //   Menu: File->Finish Sketch
        // ----------------------------------------------
        theSession.activeSketch().deactivate(nxopen.Sketch.ViewReorient.FALSE, nxopen.Sketch.UpdateLevel.MODEL);
        
        // ----------------------------------------------
        //   Menu: File->Save
        // ----------------------------------------------
        PartSaveStatus partSaveStatus1;
        partSaveStatus1 = workPart.save(nxopen.BasePart.SaveComponents.TRUE, nxopen.BasePart.CloseAfterSave.FALSE);
        
        partSaveStatus1.dispose();
        partSaveStatus1 = null;
        
        // ----------------------------------------------
        //   Menu: File->Exit
        // ----------------------------------------------
    }
    
}
