/*==================================================================================================
                               Copyright 2026 Siemens
====================================================================================================

    NOTE:  Designcenter Development provides programming examples for illustration only.
    Designcenter Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NXOpen
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor Designcenter Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A Java class that creates a Sketch and adds geometry, constraints, and dimensions to it using NX Open.  
    This class also contains handwritten code to illustrate interoperability between NX Open for Java and Java UF.

==================================================================================================*/

import nxopen.*;
import nxopen.uf.*;

/** Creates a sample sketch for use with this example */
public class CreateASketch
{
  public static void main(String [] args) throws NXException, java.rmi.RemoteException
  {
    Session theSession = (Session)SessionFactory.get("Session");
    UFSession theUFSession = (UFSession)SessionFactory.get("UFSession");
    
    Part part1;
    part1 = theSession.parts().newDisplay("newpart", nxopen.Part.Units.MILLIMETERS);
    
    int session_UndoMarkId3;
    session_UndoMarkId3 = theSession.setUndoMark(nxopen.Session.MarkVisibility.VISIBLE, "Enter Sketcher");
    
    theSession.beginTaskEnvironment();
    
    Point3d point3d2 = new Point3d(0.0, 0.0, 0.0);
    Point3d point3d3 = new Point3d(0.0, 1.0, 0.0);
    DatumAxis datumAxis1;
    datumAxis1 = theSession.parts().work().datums().createFixedDatumAxis(point3d2, point3d3);
    
    nxopen.features.Feature features_Feature2;
    features_Feature2 = datumAxis1.feature();
    
    Point3d point3d4 = new Point3d(0.0, -75.4282407407407, 0.0);
    Point3d point3d5 = new Point3d(0.0, 75.4282407407407, 0.0);
    datumAxis1.setEndPoints(point3d4, point3d5);
    
    Part workPart = theSession.parts().work();
    
    Sketch nullSketch = null;
    SketchInPlaceBuilder sketchInPlaceBuilder1;
    sketchInPlaceBuilder1 = workPart.sketches().createSketchInPlaceBuilder2(nullSketch);

    nxopen.Point3d origin1 = new nxopen.Point3d(0.0, 0.0, 0.0);
    nxopen.Vector3d normal1 = new nxopen.Vector3d(0.0, 0.0, 1.0);
    nxopen.Plane plane1;
    plane1 = workPart.planes().createPlane(origin1, normal1, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);
    sketchInPlaceBuilder1.setPlaneReference(plane1);

    nxopen.Unit unit1 = ((nxopen.Unit)workPart.unitCollection().findObject("MilliMeter"));
    nxopen.Expression expression1_1;
    expression1_1 = workPart.expressions().createSystemExpressionWithUnits("0", unit1);
    nxopen.Expression expression2_1;
    expression2_1 = workPart.expressions().createSystemExpressionWithUnits("0", unit1);

    nxopen.SketchAlongPathBuilder sketchAlongPathBuilder1;
    sketchAlongPathBuilder1 = workPart.sketches().createSketchAlongPathBuilder(nullSketch);

    nxopen.SimpleSketchInPlaceBuilder simpleSketchInPlaceBuilder1;
    simpleSketchInPlaceBuilder1 = workPart.sketches().createSimpleSketchInPlaceBuilder();

    simpleSketchInPlaceBuilder1.setUseWorkPartOrigin(false);

    nxopen.Point3d coordinates1 = new nxopen.Point3d(0.0, 0.0, 0.0);
    nxopen.Point point1;
    point1 = workPart.points().createPoint(coordinates1);

    nxopen.Point3d origin2 = new nxopen.Point3d(0.0, 0.0, 0.0);
    nxopen.Matrix3x3 matrix1 = new nxopen.Matrix3x3();
    matrix1.xx = 1.0;
    matrix1.xy = 0.0;
    matrix1.xz = 0.0;
    matrix1.yx = 0.0;
    matrix1.yy = 1.0;
    matrix1.yz = 0.0;
    matrix1.zx = 0.0;
    matrix1.zy = 0.0;
    matrix1.zz = 1.0;
    nxopen.Plane plane2;
    plane2 = workPart.planes().createFixedTypePlane(origin2, matrix1, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);

    nxopen.Point3d coordinates2 = new nxopen.Point3d(0.0, 0.0, 0.0);
    nxopen.Point point2;
    point2 = workPart.points().createPoint(coordinates2);

    nxopen.Point3d origin3 = new nxopen.Point3d(0.0, 0.0, 0.0);
    nxopen.Vector3d vector1 = new nxopen.Vector3d(0.0, 0.0, 1.0);
    nxopen.Direction direction1;
    direction1 = workPart.directions().createDirection(origin3, vector1, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);

    nxopen.Point3d origin4 = new nxopen.Point3d(0.0, 0.0, 0.0);
    nxopen.Vector3d vector2 = new nxopen.Vector3d(1.0, 0.0, 0.0);
    nxopen.Direction direction2;
    direction2 = workPart.directions().createDirection(origin4, vector2, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);

    nxopen.Point3d origin5 = new nxopen.Point3d(0.0, 0.0, 0.0);
    nxopen.Matrix3x3 matrix2 = new nxopen.Matrix3x3();
    matrix2.xx = 1.0;
    matrix2.xy = 0.0;
    matrix2.xz = 0.0;
    matrix2.yx = 0.0;
    matrix2.yy = 1.0;
    matrix2.yz = 0.0;
    matrix2.zx = 0.0;
    matrix2.zy = 0.0;
    matrix2.zz = 1.0;
    nxopen.Plane plane3;
    plane3 = workPart.planes().createFixedTypePlane(origin5, matrix2, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);

    nxopen.Xform xform1;
    xform1 = workPart.xforms().createXformByPlaneXDirPoint(plane3, direction2, point2, nxopen.SmartObject.UpdateOption.WITHIN_MODELING, 0.625, false, false);

    nxopen.CartesianCoordinateSystem cartesianCoordinateSystem1;
    cartesianCoordinateSystem1 = workPart.coordinateSystems().createCoordinateSystem(xform1, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);

    simpleSketchInPlaceBuilder1.setCoordinateSystem(cartesianCoordinateSystem1);

    nxopen.Point point3;
    point3 = simpleSketchInPlaceBuilder1.sketchOrigin();
    simpleSketchInPlaceBuilder1.setSketchOrigin(point3);

    NXObject nXObject2;
    nXObject2 = simpleSketchInPlaceBuilder1.commit();

    Sketch sketch1 = ((Sketch)nXObject2);

    sketchInPlaceBuilder1.destroy();
    sketchAlongPathBuilder1.destroy();
    simpleSketchInPlaceBuilder1.destroy();

    try
    {
        workPart.expressions().delete(expression2_1);
    }
    catch (NXException ex)
    {
        ex.assertErrorCode(1050029);
    }

    try
    {
        workPart.expressions().delete(expression1_1);
    }
    catch (NXException ex)
    {
        ex.assertErrorCode(1050029);
    }

    plane1.destroyPlane();
    
    nxopen.features.Feature features_Feature4;
    features_Feature4 = sketch1.feature();
    
    int integer1;
    integer1 = theSession.updateManager().doUpdate(session_UndoMarkId3);
    
    sketch1.activate(nxopen.Sketch.ViewReorient.TRUE);
    
    Point3d point3d10 = new Point3d(-20.0, 0.0, 0.0);
    Point3d point3d11 = new Point3d(20.0, 0.0, 0.0);
    Line line1;
    line1 = theSession.parts().work().curves().createLine(point3d10, point3d11);
    
    theSession.activeSketch().addGeometry(line1, nxopen.Sketch.InferConstraintsOption.INFER_COINCIDENT_CONSTRAINTS);
    
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry1 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry1.geometry = line1;
    sketch_ConstraintGeometry1.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry1.splineDefiningPointIndex = 0;
    SketchGeometricConstraint sketchGeometricConstraint1;
    sketchGeometricConstraint1 = theSession.activeSketch().createHorizontalConstraint(sketch_ConstraintGeometry1);
    
    //theSession.activeSketch().update();

    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry2 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry2.geometry = line1;
    sketch_ConstraintGeometry2.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry2.splineDefiningPointIndex = 0;
    SketchGeometricConstraint sketchGeometricConstraint2;
    sketchGeometricConstraint2 = theSession.activeSketch().createFixedConstraint(sketch_ConstraintGeometry2);
    
    //theSession.activeSketch().update();

    Point3d point3d12 = new Point3d(-20.0, 0.0, 0.0);
    Point3d point3d13 = new Point3d(0.0, 26.5672927829651, 0.0);
    Line line2;
    line2 = theSession.parts().work().curves().createLine(point3d12, point3d13);
    
    theSession.activeSketch().addGeometry(line2, nxopen.Sketch.InferConstraintsOption.INFER_COINCIDENT_CONSTRAINTS);
    
    //theSession.activeSketch().update();
    
    Point3d point3d14 = new Point3d(0.0, 26.5672927829651, 0.0);
    Point3d point3d15 = new Point3d(19.9999999999999, -4.2632564145606e-014, 0.0);
    Line line3;
    line3 = theSession.parts().work().curves().createLine(point3d14, point3d15);
    
    theSession.activeSketch().addGeometry(line3, nxopen.Sketch.InferConstraintsOption.INFER_COINCIDENT_CONSTRAINTS);
    
    //theSession.activeSketch().update();
    
    Point3d point3d16 = new Point3d(0.0, 10.6811674124539, 0.0);
    NXMatrix nXMatrix1 = (NXMatrix)theSession.parts().work().nxmatrices().findObject("WCS");
    Arc arc1;
    arc1 = theSession.parts().work().curves().createArc(point3d16, nXMatrix1, 1.96529386026943, 0.0, ( 180.0 * Math.PI/180.0 ));
    
    theSession.activeSketch().addGeometry(arc1, nxopen.Sketch.InferConstraintsOption.INFER_COINCIDENT_CONSTRAINTS);
   
    // ------------------------------
    // Handwritten code added to illustrate interoperability between 
    // NX Open for Java and Java UF
    
    // Create an arc using UF
    UFCurve.Arc arcCreationData = new UFCurve.Arc();
    arcCreationData.arcCenter = new double [] {0, 0, 0};
    arcCreationData.startAngle = 0;
    arcCreationData.endAngle = 2*Math.PI;
    arcCreationData.radius = 1.0;
    arcCreationData.matrixTag = nXMatrix1.tag();
    Tag arc2Tag = theUFSession.curve().createArc(arcCreationData);
    // Obtain the NX Open object corresponding to the tag obtained from UF
    Arc arc2 = (Arc)theSession.taggedObjectManager().get(arc2Tag);

    // Add the arc created by UF to the sketch using NX Open
    theSession.activeSketch().addGeometry(arc2);
    
    // Make the UF-created arc concentric with an arc created with NX Open
    Sketch.ConstraintGeometry constraintGeometry1 = new Sketch.ConstraintGeometry();
    constraintGeometry1.geometry = arc1;
    constraintGeometry1.pointType = Sketch.ConstraintPointType.NONE;
    Sketch.ConstraintGeometry constraintGeometry2 = new Sketch.ConstraintGeometry();
    constraintGeometry2.geometry = arc2;
    constraintGeometry2.pointType = Sketch.ConstraintPointType.NONE;
    theSession.activeSketch().createConcentricConstraint(constraintGeometry1, constraintGeometry2);

    // Use UF to make an arc into a reference curve.  The arc was created with NX Open
    theUFSession.sket().setReferenceStatus(theSession.activeSketch().tag(), arc1.tag(), nxopen.uf.UFSket.ReferenceStatus.REFERENCE);
    
    // End of handwritten code
    // ------------------------------
    
    
    //theSession.activeSketch().update();
    
    Point3d point3d17 = new Point3d(-3.1956916483077, 22.8222306906741, 0.0);
    Point3d point3d18 = new Point3d(3.19569164830769, 22.8222306906741, 0.0);
    nxopen.Sketch.FilletData sketch_FilletData1;
    sketch_FilletData1 = theSession.activeSketch().fillet(line2, line3, point3d17, point3d18, 4.0, nxopen.Sketch.TrimInputOption.TRUE, nxopen.Sketch.CreateDimensionOption.FALSE, nxopen.Sketch.AlternateSolutionOption.FALSE);
    
    //theSession.activeSketch().update();
    
    Point3d point3d19 = new Point3d(-15.4535548592714, 5.26812997957728, 0.0);
    Point3d point3d20 = new Point3d(-13.0567861230406, 0.463829665043484, 0.0);
    nxopen.Sketch.FilletData sketch_FilletData2;
    sketch_FilletData2 = theSession.activeSketch().fillet(line2, line1, point3d19, point3d20, 3.0, nxopen.Sketch.TrimInputOption.TRUE, nxopen.Sketch.CreateDimensionOption.FALSE, nxopen.Sketch.AlternateSolutionOption.FALSE);
    
    //theSession.activeSketch().update();
    
    Point3d point3d21 = new Point3d(15.2889783044614, 6.35023391052672, 0.0);
    Point3d point3d22 = new Point3d(12.0932866561537, -0.0554998421849802, 0.0);
    nxopen.Sketch.FilletData sketch_FilletData3;
    sketch_FilletData3 = theSession.activeSketch().fillet(line3, line1, point3d21, point3d22, 4.0, nxopen.Sketch.TrimInputOption.TRUE, nxopen.Sketch.CreateDimensionOption.FALSE, nxopen.Sketch.AlternateSolutionOption.FALSE);
    
    //theSession.activeSketch().update();
    
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry3 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry3.geometry = line2;
    sketch_ConstraintGeometry3.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry3.splineDefiningPointIndex = 0;
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry4 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry4.geometry = line1;
    sketch_ConstraintGeometry4.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry4.splineDefiningPointIndex = 0;
    SketchGeometricConstraint sketchGeometricConstraint3;
    sketchGeometricConstraint3 = theSession.activeSketch().createEqualLengthConstraint(sketch_ConstraintGeometry3, sketch_ConstraintGeometry4);
    
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry5 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry5.geometry = line2;
    sketch_ConstraintGeometry5.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry5.splineDefiningPointIndex = 0;
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry6 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry6.geometry = line3;
    sketch_ConstraintGeometry6.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry6.splineDefiningPointIndex = 0;
    SketchGeometricConstraint sketchGeometricConstraint4;
    sketchGeometricConstraint4 = theSession.activeSketch().createEqualLengthConstraint(sketch_ConstraintGeometry5, sketch_ConstraintGeometry6);
    
    //theSession.activeSketch().update();
    
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry7 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry7.geometry = sketch_FilletData2.fillets[0];
    sketch_ConstraintGeometry7.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry7.splineDefiningPointIndex = 0;
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry8 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry8.geometry = arc1;
    sketch_ConstraintGeometry8.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry8.splineDefiningPointIndex = 0;
    SketchGeometricConstraint sketchGeometricConstraint5;
    sketchGeometricConstraint5 = theSession.activeSketch().createEqualRadiusConstraint(sketch_ConstraintGeometry7, sketch_ConstraintGeometry8);
    
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry9 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry9.geometry = sketch_FilletData2.fillets[0];
    sketch_ConstraintGeometry9.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry9.splineDefiningPointIndex = 0;
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry10 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry10.geometry = sketch_FilletData1.fillets[0];
    sketch_ConstraintGeometry10.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry10.splineDefiningPointIndex = 0;
    SketchGeometricConstraint sketchGeometricConstraint6;
    sketchGeometricConstraint6 = theSession.activeSketch().createEqualRadiusConstraint(sketch_ConstraintGeometry9, sketch_ConstraintGeometry10);
    
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry11 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry11.geometry = sketch_FilletData2.fillets[0];
    sketch_ConstraintGeometry11.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry11.splineDefiningPointIndex = 0;
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry12 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry12.geometry = sketch_FilletData3.fillets[0];
    sketch_ConstraintGeometry12.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry12.splineDefiningPointIndex = 0;
    SketchGeometricConstraint sketchGeometricConstraint7;
    sketchGeometricConstraint7 = theSession.activeSketch().createEqualRadiusConstraint(sketch_ConstraintGeometry11, sketch_ConstraintGeometry12);
    
    //theSession.activeSketch().update();
    
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry13 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry13.geometry = arc1;
    sketch_ConstraintGeometry13.pointType = nxopen.Sketch.ConstraintPointType.ARC_CENTER;
    sketch_ConstraintGeometry13.splineDefiningPointIndex = 0;
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry14 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry14.geometry = line1;
    sketch_ConstraintGeometry14.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry14.splineDefiningPointIndex = 0;
    SketchGeometricConstraint sketchGeometricConstraint8;
    sketchGeometricConstraint8 = theSession.activeSketch().createMidpointConstraint(sketch_ConstraintGeometry13, sketch_ConstraintGeometry14);
    
    //theSession.activeSketch().update();
    
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry15 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry15.geometry = arc1;
    sketch_ConstraintGeometry15.pointType = nxopen.Sketch.ConstraintPointType.ARC_CENTER;
    sketch_ConstraintGeometry15.splineDefiningPointIndex = 0;
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry16 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry16.geometry = line2;
    sketch_ConstraintGeometry16.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry16.splineDefiningPointIndex = 0;
    SketchGeometricConstraint sketchGeometricConstraint9;
    sketchGeometricConstraint9 = theSession.activeSketch().createMidpointConstraint(sketch_ConstraintGeometry15, sketch_ConstraintGeometry16);
    
    //theSession.activeSketch().update();
    
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry17 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry17.geometry = arc1;
    sketch_ConstraintGeometry17.pointType = nxopen.Sketch.ConstraintPointType.ARC_CENTER;
    sketch_ConstraintGeometry17.splineDefiningPointIndex = 0;
    nxopen.Sketch.ConstraintGeometry sketch_ConstraintGeometry18 = new nxopen.Sketch.ConstraintGeometry();
    sketch_ConstraintGeometry18.geometry = datumAxis1;
    sketch_ConstraintGeometry18.pointType = nxopen.Sketch.ConstraintPointType.NONE;
    sketch_ConstraintGeometry18.splineDefiningPointIndex = 0;
    nxopen.Sketch.ConstraintGeometryHelp sketch_ConstraintGeometryHelp1 = new nxopen.Sketch.ConstraintGeometryHelp();
    sketch_ConstraintGeometryHelp1.type = nxopen.Sketch.ConstraintGeometryHelpType.POINT;
    sketch_ConstraintGeometryHelp1.point.x = 0.0;
    sketch_ConstraintGeometryHelp1.point.y = 0.0;
    sketch_ConstraintGeometryHelp1.point.z = 0.0;
    sketch_ConstraintGeometryHelp1.parameter = 0.0;
    SketchHelpedGeometricConstraint sketchHelpedGeometricConstraint1;
    sketchHelpedGeometricConstraint1 = theSession.activeSketch().createPointOnCurveConstraint(sketch_ConstraintGeometry17, sketch_ConstraintGeometry18, sketch_ConstraintGeometryHelp1);
    
    theSession.activeSketch().update();
    
    nxopen.Sketch.DimensionGeometry sketch_DimensionGeometry1 = new nxopen.Sketch.DimensionGeometry();
    sketch_DimensionGeometry1.geometry = arc1;
    sketch_DimensionGeometry1.assocType = nxopen.Sketch.AssocType.TANGENCY;
    sketch_DimensionGeometry1.assocValue = 10;
    sketch_DimensionGeometry1.helpPoint.x = 0.0;
    sketch_DimensionGeometry1.helpPoint.y = 0.0;
    sketch_DimensionGeometry1.helpPoint.z = 0.0;
    Point3d point3d23 = new Point3d(27.4834063272053, 12.9740102494349, 0.0);
    Expression nullExpression = null;
    SketchDimensionalConstraint sketchDimensionalConstraint1;
    sketchDimensionalConstraint1 = theSession.activeSketch().createDiameterDimension(sketch_DimensionGeometry1, point3d23, nullExpression);
    
    nxopen.annotations.Dimension annotations_Dimension1;
    annotations_Dimension1 = sketchDimensionalConstraint1.associatedDimension();
    
    Expression expression1;
    expression1 = sketchDimensionalConstraint1.associatedExpression();
    
    expression1.setRightHandSide("8");
    
    //theSession.activeSketch().update();
    
    nxopen.Sketch.DimensionGeometry sketch_DimensionGeometry2 = new nxopen.Sketch.DimensionGeometry();
    sketch_DimensionGeometry2.geometry = line1;
    sketch_DimensionGeometry2.assocType = nxopen.Sketch.AssocType.START_POINT;
    sketch_DimensionGeometry2.assocValue = 0;
    sketch_DimensionGeometry2.helpPoint.x = 0.0;
    sketch_DimensionGeometry2.helpPoint.y = 0.0;
    sketch_DimensionGeometry2.helpPoint.z = 0.0;
    nxopen.Sketch.DimensionGeometry sketch_DimensionGeometry3 = new nxopen.Sketch.DimensionGeometry();
    sketch_DimensionGeometry3.geometry = line1;
    sketch_DimensionGeometry3.assocType = nxopen.Sketch.AssocType.END_POINT;
    sketch_DimensionGeometry3.assocValue = 0;
    sketch_DimensionGeometry3.helpPoint.x = 0.0;
    sketch_DimensionGeometry3.helpPoint.y = 0.0;
    sketch_DimensionGeometry3.helpPoint.z = 0.0;
    Point3d point3d24 = new Point3d(31.5777685361, -12.4110354457119, 0.0);
    SketchDimensionalConstraint sketchDimensionalConstraint2;
    sketchDimensionalConstraint2 = theSession.activeSketch().createDimension(nxopen.Sketch.ConstraintType.HORIZONTAL_DIM, sketch_DimensionGeometry2, sketch_DimensionGeometry3, point3d24, nullExpression);
    
    nxopen.annotations.Dimension annotations_Dimension2;
    annotations_Dimension2 = sketchDimensionalConstraint2.associatedDimension();
    
    Expression expression2;
    expression2 = sketchDimensionalConstraint2.associatedExpression();
    
    expression2.setRightHandSide("25");
    
    theSession.activeSketch().update();
    
    theSession.activeSketch().deactivate(nxopen.Sketch.ViewReorient.TRUE, nxopen.Sketch.UpdateLevel.MODEL);
    
    theSession.deleteUndoMarksSetInTaskEnvironment();
    
    theSession.endTaskEnvironment();
    
  
  }
  
  public static final int getUnloadOption() { return BaseSession.LibraryUnloadOption.IMMEDIATELY; }
  
}
