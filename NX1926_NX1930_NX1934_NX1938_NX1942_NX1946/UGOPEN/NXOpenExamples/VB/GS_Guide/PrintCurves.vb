Imports System
Imports NXOpen

' Example to demonstrate cycling over a collection of NX objects
Module NXOpenSample
  Sub Main () 
    Dim theSession = Session.GetSession()
    Dim workPart = theSession.Parts.Work

    Dim numCurves As Integer = 0
    Dim curveLength As Double
    For Each curve In workPart.Curves
      numCurves = numCurves + 1
      curveLength = curve.GetLength()
      Guide.InfoWriteLine("Curve " & numCurves & " has length " & curveLength)
    Next curve
    Guide.InfoWriteLine("Work part has " & numCurves & " curves.")
  End Sub
End Module
