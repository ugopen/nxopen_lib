' NX 3.0.0.16
' Journal created by peborge on Thu May 27 16:33:27 2004 Eastern Daylight Time
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
part1 = theSession.Parts.NewDisplay("prefs", Part.Units.Inches)

' ----------------------------------------------
'   Menu: Preferences->Sketch...
' ----------------------------------------------
theSession.Preferences.Sketch.DefaultSketchNamePrefix = "SKT_"

theSession.Preferences.Sketch.DefaultVertexNamePrefix = "VRT_"

theSession.Preferences.Sketch.DefaultLineNamePrefix = "LIN_"

theSession.Preferences.Sketch.DefaultArcNamePrefix = "ARC_"

theSession.Preferences.Sketch.DefaultConicNamePrefix = "CON_"

theSession.Preferences.Sketch.DefaultSplineNamePrefix = "SPL_"

theSession.Preferences.Sketch.TextHeight = 0.2

theSession.Preferences.Sketch.DecimalPlaces = 2

' ----------------------------------------------
'   Menu: Preferences->Work Plane...
' ----------------------------------------------
Dim workPlanePreferences1 As WorkPlane
workPlanePreferences1 = theSession.Parts.Work.Preferences.Workplane

workPlanePreferences1.GridType = WorkPlane.Grid.Polar

workPlanePreferences1.GridUnitAngularSpacing = 10

workPlanePreferences1.GridLineEveryAngularSpacing = 1

workPlanePreferences1.GridEmphasisAngularSpacing = 3

' ----------------------------------------------
'   Menu: Tools->Journal->Stop
' ----------------------------------------------

End Sub
End Module
