Imports Snap, Snap.Create
Imports System.Drawing.Color

Public Class MyProgram

    Public Shared Sub Main()

      Dim p As Position(,) = New Position(2,2) {}
      Dim h As double = 0.4
      p(0,0) = {0,0,0}  :  p(0,1) = {0,1,0}  :  p(0,2) = {0,2,0}  
      p(1,0) = {1,0,h}  :  p(1,1) = {1,1,h}  :  p(1,2) = {1,2,h}  
      p(2,0) = {2,0,0}  :  p(2,1) = {2,1,h}  :  p(2,2) = {2,2,h}  
      Dim patchBody As NX.Body = BezierPatch(p)
      Dim face As NX.Face = patchBody.Faces(0)

      Dim nu As Integer = 10  :     Dim uStep As Double = 1.0/nu
      Dim nv As Integer = 10  :     Dim vStep As Double = 1.0/nv

      Dim diameter = 0.1    ' Tool diameter
      Dim length   = 0.5    ' Tool length

      Dim u, v As Double
      Dim point As Position
      Dim axis As Vector
      
      For i As Integer = 0 To nu
        For j As Integer = 0 To nv
          u = i*uStep
          v = j*vStep
          point = face.Position(u,v)                 ' Point on surface
          axis  = face.Normal(u,v)                   ' Surface normal = tool axis
          ShowTool(diameter, length, point, axis)    ' Display the tool at this position
        Next j
      Next i   

End Sub

    Shared Sub ShowTool(ByVal diameter As Double, ByVal length As Double, ByVal point As Position, ByVal axis As Vector)
      Dim toolCenter As Position = point + 0.5* diameter*axis
      Dim toolSphere As NX.Body = Sphere(toolCenter, diameter)
      Dim toolShaft As NX.Body = Cylinder(toolCenter, axis, length, diameter)
      Dim tool As NX.Body = Unite(toolSphere, toolShaft)
      tool.Color = Green
      Dim angle As Double = Vector.Angle(axis, Vector.AxisZ)
      If angle >  8 Then tool.Color = Orange
      If angle > 15 Then tool.Color = Red
    End Sub

End Class
