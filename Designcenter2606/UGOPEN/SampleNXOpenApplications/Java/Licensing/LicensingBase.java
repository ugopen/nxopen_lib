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
        
        nxopen.FileNew fileNew1;
        fileNew1 = theSession.parts().fileNew();
        
        theSession.setUndoMarkName(markId1, "New Dialog");
        
        int markId2;
        markId2 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "New");
        
        theSession.deleteUndoMark(markId2, null);
        
        int markId3;
        markId3 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "New");
        
        fileNew1.setTemplateFileName("model-plain-1-mm-template.prt");
        
        fileNew1.setUseBlankTemplate(false);
        
        fileNew1.setApplicationName("ModelTemplate");
        
        fileNew1.setUnits(nxopen.Part.Units.MILLIMETERS);
        
        fileNew1.setRelationType("");
        
        fileNew1.setUsesMasterModel("No");
        
        fileNew1.setTemplateType(nxopen.FileNewTemplateType.ITEM);
        
        fileNew1.setTemplatePresentationName("Model");
        
        fileNew1.setItemType("");
        
        fileNew1.setSpecialization("");
        
        fileNew1.setCanCreateAltrep(false);
        
        fileNew1.setNewFileName("line.prt");
        
        fileNew1.setMasterFileName("");
        
        fileNew1.setMakeDisplayedPart(true);
        
        fileNew1.setDisplayPartOption(nxopen.DisplayPartOption.ALLOW_ADDITIONAL);
        
        nxopen.NXObject nXObject1;
        nXObject1 = fileNew1.commit();
        
        nxopen.Part workPart = theSession.parts().work();
        nxopen.Part displayPart = theSession.parts().display();
        theSession.deleteUndoMark(markId3, null);
        
        fileNew1.destroy();
        
        theSession.applicationSwitchImmediate("UG_APP_MODELING");
        
        // ----------------------------------------------
        //   Menu: Insert->Sketch
        // ----------------------------------------------
        int markId4;
        markId4 = theSession.setUndoMark(nxopen.Session.MarkVisibility.VISIBLE, "Enter Sketch");
        
        int markId5;
        markId5 = theSession.setUndoMark(nxopen.Session.MarkVisibility.VISIBLE, "Update Model from Sketch");
        
        theSession.beginTaskEnvironment();
        
        int markId6;
        markId6 = theSession.setUndoMark(nxopen.Session.MarkVisibility.VISIBLE, "Start");
        
        nxopen.Sketch nullNXOpen_Sketch = null;
        nxopen.SketchInPlaceBuilder sketchInPlaceBuilder1;
        sketchInPlaceBuilder1 = workPart.sketches().createSketchInPlaceBuilder2(nullNXOpen_Sketch);
        
        nxopen.Point3d origin1 = new nxopen.Point3d(0.0, 0.0, 0.0);
        nxopen.Vector3d normal1 = new nxopen.Vector3d(0.0, 0.0, 1.0);
        nxopen.Plane plane1;
        plane1 = workPart.planes().createPlane(origin1, normal1, nxopen.SmartObject.UpdateOption.WITHIN_MODELING);
        
        sketchInPlaceBuilder1.setPlaneReference(plane1);
        
        nxopen.Unit unit1 = ((nxopen.Unit)workPart.unitCollection().findObject("MilliMeter"));
        nxopen.Expression expression1;
        expression1 = workPart.expressions().createSystemExpressionWithUnits("0", unit1);
        
        nxopen.Expression expression2;
        expression2 = workPart.expressions().createSystemExpressionWithUnits("0", unit1);
        
        nxopen.SketchAlongPathBuilder sketchAlongPathBuilder1;
        sketchAlongPathBuilder1 = workPart.sketches().createSketchAlongPathBuilder(nullNXOpen_Sketch);
        
        nxopen.SimpleSketchInPlaceBuilder simpleSketchInPlaceBuilder1;
        simpleSketchInPlaceBuilder1 = workPart.sketches().createSimpleSketchInPlaceBuilder();
        
        theSession.setUndoMarkName(markId6, "Create Sketch Dialog");
        
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
        
        int markId7;
        markId7 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "Create Sketch");
        
        theSession.deleteUndoMark(markId7, null);
        
        int markId8;
        markId8 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "Create Sketch");
        
        theSession.preferences().sketch().setCreateInferredConstraints(false);
        
        theSession.preferences().sketch().setContinuousAutoDimensioning(false);
        
        theSession.preferences().sketch().setDimensionLabel(nxopen.preferences.SketchPreferences.DimensionLabelType.EXPRESSION);
        
        theSession.preferences().sketch().setTextSizeFixed(false);
        
        theSession.preferences().sketch().setFixedTextSize(3.0);
        
        theSession.preferences().sketch().setDisplayParenthesesOnReferenceDimensions(true);
        
        theSession.preferences().sketch().setDisplayReferenceGeometry(false);
        
        theSession.preferences().sketch().setDisplayShadedRegions(true);
        
        theSession.preferences().sketch().setFindMovableObjects(true);
        
        theSession.preferences().sketch().setConstraintSymbolSize(3.0);
        
        theSession.preferences().sketch().setDisplayObjectColor(false);
        
        theSession.preferences().sketch().setDisplayObjectName(true);
        
        theSession.preferences().sketch().setEditDimensionOnCreation(true);
        
        theSession.preferences().sketch().setCreateDimensionForTypedValues(true);
        
        theSession.preferences().sketch().setAddRemoteFindingAfterSnap(true);
        
        nxopen.NXObject nXObject2;
        nXObject2 = simpleSketchInPlaceBuilder1.commit();
        
        nxopen.Sketch sketch1 = ((nxopen.Sketch)nXObject2);
        nxopen.features.Feature feature1;
        feature1 = sketch1.feature();
        
        int markId9;
        markId9 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "update");
        
        int nErrs1;
        nErrs1 = theSession.updateManager().doUpdate(markId9);
        
        sketch1.activate(nxopen.Sketch.ViewReorient.TRUE);
        
        theSession.preferences().sketch().setFindMovableObjects(true);
        
        nxopen.SketchFindMovableObjectsBuilder sketchFindMovableObjectsBuilder1;
        sketchFindMovableObjectsBuilder1 = workPart.sketches().createFindMovableObjectsBuilder();
        
        nxopen.NXObject nXObject3;
        nXObject3 = sketchFindMovableObjectsBuilder1.commit();
        
        sketchFindMovableObjectsBuilder1.destroy();
        
        nxopen.SketchFindIssuesBuilder sketchFindIssuesBuilder1;
        sketchFindIssuesBuilder1 = workPart.sketches().createFindIssuesBuilder();
        
        sketchFindIssuesBuilder1.setZoomScale(0.17879913789679108);
        
        nxopen.NXObject nXObject4;
        nXObject4 = sketchFindIssuesBuilder1.commit();
        
        sketchFindIssuesBuilder1.destroy();
        
        workPart.modelingViews().workView().setScale(0.17879913789679108);
        
        theSession.deleteUndoMark(markId8, null);
        
        theSession.setUndoMarkName(markId6, "Create Sketch");
        
        sketchInPlaceBuilder1.destroy();
        
        sketchAlongPathBuilder1.destroy();
        
        simpleSketchInPlaceBuilder1.destroy();
        
        try
        {
        // Expression is still in use.
        workPart.expressions().delete(expression2);
        }
        catch (NXException ex)
        {
        ex.assertErrorCode(1050029);
        }
        
        try
        {
        // Expression is still in use.
        workPart.expressions().delete(expression1);
        }
        catch (NXException ex)
        {
        ex.assertErrorCode(1050029);
        }
        
        plane1.destroyPlane();
        
        theSession.deleteUndoMarksUpToMark(markId5, null, true);
        
        int markId10;
        markId10 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "Open Sketch");
        
        theSession.activeSketch().setName("SKETCH_000");
        
        // ----------------------------------------------
        //   Menu: Insert->Curve->Line->Line...
        // ----------------------------------------------
        int markId11;
        markId11 = theSession.setUndoMark(nxopen.Session.MarkVisibility.VISIBLE, "Start");
        
        nxopen.SketchLineBuilder sketchLineBuilder1;
        sketchLineBuilder1 = workPart.sketches().createLineBuilder();
        
        sketchLineBuilder1.setSnapRadius(32.555153239571631);
        
        theSession.setUndoMarkName(markId11, "Line Dialog");
        
        nxopen.Point3d startpoint1 = new nxopen.Point3d(-153.8970880416112, 122.08182464839361, 0.0);
        sketchLineBuilder1.snapStartPoint(startpoint1);
        
        nxopen.Point3d endpoint1 = new nxopen.Point3d(291.51659946343705, -204.94948744003048, 0.0);
        sketchLineBuilder1.snapEndPoint(endpoint1);
        
        sketchLineBuilder1.length().setValue(550.0);
        
        sketchLineBuilder1.angle().setValue(324.0);
        
        sketchLineBuilder1.length().setFormula("550");
        
        sketchLineBuilder1.angle().setFormula("324");
        
        int markId12;
        markId12 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "Line");
        
        nxopen.NXObject nXObject5;
        nXObject5 = sketchLineBuilder1.commit();
        
        theSession.deleteUndoMark(markId12, null);
        
        sketchLineBuilder1.angle().setFormula("0");
        
        theSession.setUndoMarkName(markId11, "Line");
        
        theSession.setUndoMarkVisibility(markId11, null, nxopen.Session.MarkVisibility.VISIBLE);
        
        sketchLineBuilder1.destroy();
        
        int markId13;
        markId13 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "preOperationMark");
        
        nxopen.SketchFindMovableObjectsBuilder sketchFindMovableObjectsBuilder2;
        sketchFindMovableObjectsBuilder2 = workPart.sketches().createFindMovableObjectsBuilder();
        
        nxopen.NXObject nXObject6;
        nXObject6 = sketchFindMovableObjectsBuilder2.commit();
        
        sketchFindMovableObjectsBuilder2.destroy();
        
        nxopen.SketchFindIssuesBuilder sketchFindIssuesBuilder2;
        sketchFindIssuesBuilder2 = workPart.sketches().createFindIssuesBuilder();
        
        sketchFindIssuesBuilder2.setZoomScale(0.17879913789679108);
        
        nxopen.NXObject nXObject7;
        nXObject7 = sketchFindIssuesBuilder2.commit();
        
        sketchFindIssuesBuilder2.destroy();
        
        theSession.deleteUndoMark(markId13, null);
        
        int markId14;
        markId14 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "Start");
        
        nxopen.SketchLineBuilder sketchLineBuilder2;
        sketchLineBuilder2 = workPart.sketches().createLineBuilder();
        
        sketchLineBuilder2.length().setFormula("550");
        
        sketchLineBuilder2.angle().setFormula("0");
        
        sketchLineBuilder2.relativeAngle().setFormula("0");
        
        sketchLineBuilder2.setSnapRadius(32.555153239571631);
        
        nxopen.Line line3 = ((nxopen.Line)theSession.activeSketch().findObject("Curve Line1"));
        nxopen.Point3d firstpoint1 = new nxopen.Point3d(294.95934690622147, -203.28188876086011, 0.0);
        sketchLineBuilder2.setChainPoint(line3, firstpoint1);
        
        theSession.setUndoMarkName(markId14, "Line Dialog");
        
        // ----------------------------------------------
        //   Menu: Task->Finish Sketch
        // ----------------------------------------------
        sketchLineBuilder2.destroy();
        
        theSession.undoToMark(markId14, null);
        
        theSession.deleteUndoMark(markId14, null);
        
        theSession.activeSketch().calculateStatus();
        
        theSession.preferences().sketch().setSectionView(false);
        
        int markId15;
        markId15 = theSession.setUndoMark(nxopen.Session.MarkVisibility.INVISIBLE, "Deactivate Sketch");
        
        theSession.activeSketch().deactivate(nxopen.Sketch.ViewReorient.TRUE, nxopen.Sketch.UpdateLevel.MODEL);
        
        theSession.deleteUndoMarksSetInTaskEnvironment();
        
        theSession.endTaskEnvironment();
        
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
