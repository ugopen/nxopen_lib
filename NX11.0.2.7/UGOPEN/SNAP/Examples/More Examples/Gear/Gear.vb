Option Infer On
Imports Snap, Snap.Create
Imports System.Collections.Generic 

Public Class GearDialog : Inherits UI.BlockForm

   ' Declarations of the blocks on a GearDialog
   Dim numTeethBlock       As UI.Block.Integer      ' The number of teeth in the gear
   Dim pressureAngleBlock  As UI.Block.Double       ' The pressure angle. This determines the shape of the gear teeth
   Dim diameterPitchBlock  As UI.Block.Double       ' The diametral pitch of the gear 
   Dim thicknessBlock      As UI.Block.Double       ' The thickness of the gear
   Dim solidOptionBlock    As UI.Block.Enumeration  ' Choice of curves or solid

   ' Constructor for a GearDialog object
   Public Sub New()

      Me.Title = "Create Gear"                      ' Text to be shown in title bar of dialog
      Me.Cue   = "Please enter gear parameters"     ' Text to be shown in cue line

      numTeethBlock = New UI.Block.Integer("Number of teeth", 20)
      pressureAngleBlock = New UI.Block.Double("Pressure angle", 20)
      diameterPitchBlock = New UI.Block.Double("Diametral pitch", 8)
      thicknessBlock = New UI.Block.Double("Thickness", 0.25)
      solidOptionBlock = New UI.Block.Enumeration("Create curves or solid", UI.Block.EnumPresentationStyle.RadioBox)
      solidOptionBlock.Items = { "Curves", "Solid" }
      solidOptionBlock.Layout = UI.Block.Layout.Horizontal

      ' Add all the blocks to the BlockForm
      Me.AddBlocks(numTeethBlock, pressureAngleBlock, diameterPitchBlock, thicknessBlock, solidOptionBlock)

   End Sub

   Public Shared Sub Main()

      ' Create and display a Gear dialog
      Dim myForm = New GearDialog()
      myForm.Show()

   End Sub

   Public Overrides Sub OnApply()

       ' Create gear profile curves      
      Dim profile = CreateGearProfile(numTeethBlock.Value, pressureAngleBlock.Value, diameterPitchBlock.Value)

      ' Extrude profile curves to create solid gear if desired
      If solidOptionBlock.SelectedItem = "Solid"
         Extrude(profile, Vector.AxisZ, thicknessBlock.Value)
      End If

   End Sub

    ' Create gear profile
   Private Shared Function CreateGearProfile(numTeeth As Integer, pressureAngle As Double, diametralPitch As Double) As NX.Curve()

      ' The radius of the pitch circle (from which other dimensions are derived)
      Dim pitchR =  numTeeth / (2 * diametralPitch)

      ' The base circle is used to construct the involute curve used for the tooth shape
      Dim baseR = pitchR * Snap.Math.CosD(pressureAngle) 

      ' Calculate inner and outer circles that delimit tooth shapes
      Dim factor = 1.157                              ' Sometimes 1.0 or 1.25 is used, instead of 1.157
      Dim moduleValue = 1.0/diametralPitch            ' The "module" value 
      Dim outerR = pitchR + moduleValue               ' Radius at tips of teeth (addendum radius)
      Dim rootR  = pitchR - factor * moduleValue      ' Radius at base of teeth (dedendum radius) 

      ' Create pitch circle            
      Dim pitchCircle = Circle(Position.Origin, pitchR)
      pitchCircle.LineFont = Globals.Font.Dashed

      ' Generate tooth side
      Dim toothSide As NX.Spline = CreateToothSide(baseR, rootR, outerR)

      ' Create a single tooth
      Dim tooth As NX.Curve() = CreateTooth(pitchCircle, toothSide, outerR, diametralPitch, numTeeth)

      ' Rotate single tooth to generate the 2D outline of the gear
      Dim profile As NX.Curve() = RotateTooth(tooth, numTeeth)

      Return profile

   End Function

   ' Create the side curve of the tooth (an involute plus maybe a linear extension)
   Private Shared Function CreateToothSide(baseR As Double, rootR As Double, outerR As Double) As NX.Spline

      Dim involute, side As NX.Spline
      Dim data1, data2 As Double()

      Dim m As Integer = 9    ' The degree of the spline curve

      If rootR > baseR Then  ' Easy case -- tooth side is just an involute
         data1 = { baseR, rootR, outerR }
         side = BezierCurveFit(AddressOf InvoluteFunction, data1, m)

      Else  ' We need a radial line to extend the involute
         data2 = { baseR, baseR, outerR }
         involute = BezierCurveFit(AddressOf InvoluteFunction, data2, m)
         Dim extensionLine = Line(baseR, 0, rootR, 0)
         side = JoinCurves(extensionLine, involute)
         NX.NXObject.Delete(involute, extensionLine)
      End If
   
      Return side

   End Function

   ' Calculates positions on a segment of an involute curve   
   Private Shared Function InvoluteFunction(data As Object, u As Double) As Position

      ' Note that the involute curve here is parameterised by radial distance from the origin (r).
      ' The more common approach is to parameterise by angle (theta) but this causes a
      ' singularity at the start point (derivative vector has zero length), which leads 
      ' to a nasty Bezier curve whose first and second poles coincide.

      Dim params  As Double() = CType(data, Double())

      Dim a   = params(0)         ' Radius of base circle of involute
      Dim r0  = params(1)         ' Radial parameter value at start point of involute segment
      Dim r1  = params(2)         ' Radial parameter value at end   point of involute segment
      Dim r = r0 + u * (r1 - r0)

      Dim theta As Double = System.Math.Sqrt(r*r - a*a)/a
      Dim x As Double = a * ( System.Math.Cos(theta) + theta * System.Math.Sin(theta) )
      Dim y As Double = a * ( System.Math.Sin(theta) - theta * System.Math.Cos(theta) )

      return new Position(x, y, 0)

   End Function


   ' Create a single tooth
   Private Shared Function CreateTooth(pitchCircle As NX.Arc, side1 As NX.Curve, outerR As Double, diametralPitch As Double, teethNum As Double) As NX.Curve()

      ' Calculate the rotation angle
      Dim circularPitch As Double = System.Math.PI / diametralPitch
      Dim toothThickness = circularPitch / 2
      Dim angle As Double = -(toothThickness / 2) / pitchCircle.Radius * (180 / System.Math.PI)
      Dim intPoint As Position = Compute.Intersect(pitchCircle, side1)(0)
      Dim cang As Double = intPoint.PolarTheta
      angle = angle - System.Math.Abs(cang)

      ' Rotate tooth side
      Dim rotation As Geom.Transform = Geom.Transform.CreateRotation(Position.Origin, angle)
      side1.Move(rotation)

      ' Create other side of tooth by reflection in x-axis
      Dim axisX As Geom.Surface.Plane = New Geom.Surface.Plane(Position.Origin, Vector.AxisY)
      Dim mirror As Geom.Transform = Geom.Transform.CreateReflection(axisX)
      Dim side2 As NX.Curve = side1.Copy(mirror)

      ' Create arc for outer edge of tooth
      Dim p2 As New Position(outerR, 0, 0)
      Dim p1 = side1.EndPoint
      Dim p3 = p1.Copy(mirror)
      Dim outer = Arc(p1, p2, p3)

      ' Create line for inner edge of tooth
      p2 = side2.StartPoint
      rotation = Geom.Transform.CreateRotation(Position.Origin, 360 / teethNum)
      p1 = side1.StartPoint.Copy(rotation)
      Dim inner = Line(p1, p2)

      Dim tooth As NX.Curve() = { side1, side2, outer, inner }

      Return tooth

   End Function

   ' Rotate single tooth to get complete gear profile
   Private Shared Function RotateTooth(tooth As NX.Curve(), teethNum As Integer) As NX.Curve()

      Dim rotation As Geom.Transform
      Dim curveList As New List(Of NX.Curve)(tooth)
      Dim angle As Double

      For Each curve In tooth
         For i = 1 To teethNum - 1
            angle = i * (360.0/teethNum)
            rotation = Geom.Transform.CreateRotation(Position.Origin, angle)
            curveList.Add( curve.Copy(rotation) )
         Next i
      Next

      Return curveList.ToArray()

   End Function

End Class
