' ===================================================================
'
'                   Copyright (c) 2010 UGS
'               Unpublished - All rights reserved
'
'  
' ===================================================================

Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.Preferences

Module NXJournal
Sub Main

Dim theSession As Session = Session.GetSession()
' ----------------------------------------------
'   Menu: File->New...
' ----------------------------------------------
Dim part1 As Part
part1 = theSession.Parts.NewDisplay("prefs", Part.Units.millimeters)

Dim workPart As Part = theSession.Parts.Work

Dim displayPart As Part = theSession.Parts.Display

' ----------------------------------------------
'   Menu: Preferences->Sketch...
' ----------------------------------------------
theSession.Preferences.Sketch.DefaultSketchNamePrefix = "SKT_"

theSession.Preferences.Sketch.DefaultVertexNamePrefix = "VRT_"

theSession.Preferences.Sketch.DefaultLineNamePrefix = "LIN_"

theSession.Preferences.Sketch.DefaultArcNamePrefix = "ARC_"

theSession.Preferences.Sketch.DefaultConicNamePrefix = "CON_"

theSession.Preferences.Sketch.DefaultSplineNamePrefix = "SPL_"

' ----------------------------------------------
'   Menu: Preferences->Grid and Work Plane...
' ----------------------------------------------
Dim workPlane1 As Preferences.WorkPlane
workPlane1 = workPart.Preferences.Workplane

workPlane1.GridType = Preferences.WorkPlane.Grid.Polar

Dim polarGridSize1 As Preferences.WorkPlane.PolarGridSize
polarGridSize1.RadialGridSize.MajorGridSpacing = 75.0
polarGridSize1.RadialGridSize.MinorLinesPerMajor = 3
polarGridSize1.RadialGridSize.SnapPointsPerMinor = 5
polarGridSize1.AngularGridSize.MajorGridSpacing = 45.0
polarGridSize1.AngularGridSize.MinorLinesPerMajor = 4
polarGridSize1.AngularGridSize.SnapPointsPerMinor = 2
workPlane1.SetPolarGridSize(polarGridSize1)

workPlane1.ShowGrid = True

workPlane1.ShowLabels = False

workPlane1.SnapToGrid = False

workPlane1.GridOnTop = False

workPlane1.RectangularShowMajorLines = False

workPlane1.PolarShowMajorLines = True

workPlane1.GridColor = 130

        theSession.Preferences.EmphasisVisualization.WcsWorkPlaneEmphasis = False

' ----------------------------------------------
'   Menu: Tools->Journal->Stop
' ----------------------------------------------

End Sub
End Module
