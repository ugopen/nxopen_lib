
' ===================================================================
'
'                   Copyright (c) 2005 UGS
'               Unpublished - All rights reserved
'
'  
' ===================================================================
Option Strict Off
Imports System
Imports NXOpen

'**** Added Code *****
Imports NXOpen.UF
Imports NXOpenUI
'^^^^^^^^^^^^^^^^^^^^^

Module NXJournal
    Sub Main()

        ' **** Added Code ****
        Dim sketch1 As Sketch = SelectSketch()
        If sketch1 Is Nothing Then
            Return
        End If
        '^^^^^^^^^^^^^^^^^^^^^

        Dim theSession As Session = Session.GetSession()
        Dim workPart As Part = theSession.Parts.Work

        Dim displayPart As Part = theSession.Parts.Display

        ' ----------------------------------------------
        '   Menu: Insert->Design Features->Extrude...
        ' ----------------------------------------------
        Dim markId1 As Session.UndoMarkId
        markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim section1 As Section
        section1 = workPart.Sections.CreateSection(0.00095, 0.001, 0.5)

        Dim nullFeatures_Feature As Features.Feature = Nothing

        Dim extrudeBuilder1 As Features.ExtrudeBuilder
        extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(nullFeatures_Feature)

        extrudeBuilder1.Section = section1

        Dim limits1 As GeometricUtilities.Limits
        limits1 = extrudeBuilder1.Limits

        Dim featureOptions1 As GeometricUtilities.FeatureOptions
        featureOptions1 = extrudeBuilder1.FeatureOptions

        Dim linearLimits1 As GeometricUtilities.LinearLimits = CType(limits1, GeometricUtilities.LinearLimits)

        Dim extend1 As GeometricUtilities.Extend
        extend1 = linearLimits1.StartExtend

        Dim extend2 As GeometricUtilities.Extend
        extend2 = linearLimits1.EndExtend

        Dim booleanOperation1 As GeometricUtilities.BooleanOperation
        booleanOperation1 = extrudeBuilder1.BooleanOperation

        Dim direction1 As Direction
        direction1 = extrudeBuilder1.Direction

        Dim featureOffset1 As GeometricUtilities.FeatureOffset
        featureOffset1 = extrudeBuilder1.Offset

        ' **** Removed Code ****
        ' Dim simpleDraft1 As GeometricUtilities.SimpleDraft
        'simpleDraft1 = extrudeBuilder1.Draft

        Dim featureOptions2 As GeometricUtilities.FeatureOptions
        featureOptions2 = extrudeBuilder1.FeatureOptions

        ' **** Removed Code ****
        'extend1.SetValue("0")

        'extend2.SetValue("1")

        'Dim inputBox As NXInputBox = New NXInputBox
        '^^^^^^^^^^^^^^^^^^^^^

        extend1.Value.RightHandSide = (NXInputBox.GetInputString("Set the Start Limit: ", _
                                                      "Extrude Limit", _
                                                      "0"))
        extend2.Value.RightHandSide = (NXInputBox.GetInputString("Set the End Limit: ", _
                                                    "Extrude Limit", _
                                                    "1"))
        '^^^^^^^^^^^^^^^^^^^^^

        featureOffset1.StartOffset.RightHandSide = "0"

        featureOffset1.EndOffset.RightHandSide = "0.25"

        featureOffset1.Option = GeometricUtilities.Type.NonsymmetricOffset
        ' **** Removed Code ****
        'simpleDraft1.SetDraftAngle("2")

        'simpleDraft1.DraftType = GeometricUtilities.SimpleDraft.SimpleDraftType.SimpleFromStart

        ' **** Added Code ****

        extrudeBuilder1.Draft.DraftOption = GeometricUtilities.SimpleDraft.SimpleDraftType.SimpleFromStart

        extrudeBuilder1.Draft.FrontDraftAngle.RightHandSide = "0"

        theSession.SetUndoMarkName(markId1, "Extrude")

        Dim markId2 As Session.UndoMarkId
        markId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, Nothing)

        theSession.UndoToMark(markId2, Nothing)

        Dim features1(0) As Features.Feature

        ' **** Removed Code ****
        'Dim sketchFeature1 As Features.SketchFeature = CType(workPart.Features.FindObject("SKETCH(4)"), Features.SketchFeature)

        'features1(0) = sketchFeature1
        '^^^^^^^^^^^^^^^^^^^^^^^

        ' **** Added Code ****


        features1(0) = sketch1.Feature
        '^^^^^^^^^^^^^^^^^^^^^^^

        Dim curveFeatureRule1 As CurveFeatureRule
        curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)

        section1.AllowSelfIntersection(False)

        Dim rules1(0) As SelectionIntentRule
        rules1(0) = curveFeatureRule1

        ' **** Removed Code ****
        'Dim sketch1 As Sketch = CType(workPart.Sketches.FindObject("SKETCH_000"), Sketch)

        'Dim arc1 As Arc = CType(sketch1.FindObject("Curve Arc1"), Arc)
        '^^^^^^^^^^^^^^^^^^^^^^^

        ' **** Added Code ****

        Dim geoms() As NXObject = sketch1.GetAllGeometry()
        Dim nXObject1 As NXObject = geoms(0)
        '^^^^^^^^^^^^^^^^^^^^^

        Dim nullNXObject As NXObject = Nothing

        Dim helpPoint1 As Point3d = New Point3d(4.0, 1.07416298997847, 1.75440985394924)

        ' **** Removed Code ****
        'section1.AddToSection(rules1, arc1, nullNXObject, nullNXObject, helpPoint1, Section.Mode.Create)
        '^^^^^^^^^^^^^^^^^^^^^

        ' **** Added Code ****

        section1.AddToSection(rules1, nXObject1, nullNXObject, nullNXObject, helpPoint1, Section.Mode.Create)
        '^^^^^^^^^^^^^^^^^^^^^

        theSession.DeleteUndoMark(markId2, Nothing)

        Dim direction2 As Direction
        direction2 = workPart.Directions.CreateDirection(sketch1, Sense.Forward, SmartObject.UpdateOption.WithinModeling)

        extrudeBuilder1.Direction = direction2

        Dim markId3 As Session.UndoMarkId
        markId3 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Extrude")

        ' **** Removed Code ****
        'Dim feature1 As Features.Feature
        'feature1 = extrudeBuilder1.CommitFeature()
        'theSession.DeleteUndoMark(markId3, Nothing)
        'extrudeBuilder1.Destroy()


        ' **** Added Code ****
		Dim exceptionThrown as Boolean = false
        Dim feature1 As Features.Feature
		Try
			feature1 = extrudeBuilder1.CommitFeature()
			
		Catch ex As Exception
	
			exceptionThrown = True	
			extrudeBuilder1.Destroy()
			section1.Destroy()
			theSession.UndoToMark(markId1, Nothing)
            theSession.DeleteUndoMark(markId1, Nothing)
			
			UI.GetUI().NXMessageBox.Show("Quick Extrude", NXMessageBox.DialogType.Error, ex.ToString)
			
       End Try
		
	   if exceptionThrown <> true then
			
			extrudeBuilder1.Destroy()
		
			theSession.DeleteUndoMark(markId3, Nothing)

	   End if
        	
    End Sub

    ' **** Added Code ****
    Public Function SelectSketch() As Sketch

        Dim ui As UI = ui.GetUI
        Dim message As String = "Select sketch"
        Dim title As String = "Selection"

        Dim scope As Selection.SelectionScope = Selection.SelectionScope.WorkPart
        Dim keepHighlighted As Boolean = False
        Dim includeFeatures As Boolean = True

        Dim selectionAction As Selection.SelectionAction = _
            Selection.SelectionAction.ClearAndEnableSpecific

        Dim selectionMask_array(1) As Selection.MaskTriple
        With selectionMask_array(0)
            .Type = UFConstants.UF_sketch_type
            .Subtype = 0
            .SolidBodySubtype = 0
        End With

        Dim selectedObject As TaggedObject = Nothing
        Dim cursor As Point3d

        ui.SelectionManager.SelectTaggedObject(message, title, scope, _
                                         selectionAction, includeFeatures, _
                                         keepHighlighted, selectionMask_array, _
                                         selectedObject, cursor)

        Dim sketch As Sketch = CType(selectedObject, Sketch)

        If sketch Is Nothing Then
            Return Nothing
        End If

        Return sketch

    End Function
    '^^^^^^^^^^^^^^^^^^^^^
End Module






