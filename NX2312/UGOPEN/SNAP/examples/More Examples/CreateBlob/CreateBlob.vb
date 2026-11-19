Option Infer On
Imports Snap, Snap.Create

Public Class BlobDialog : Inherits UI.BlockForm

    ' The various members of a BlobDialog object
    Dim pointBlock As UI.Block.SpecifyPoint  ' A SpecifyPoint block to get the center
    Dim separator As UI.Block.Separator     ' A separator (horizontal line across dialog)
    Dim xLengthBlock As UI.Block.Double        ' Block to get length of semi-axis in x-direction     
    Dim yLengthBlock As UI.Block.Double        ' Block to get length of semi-axis in y-direction    
    Dim zLengthBlock As UI.Block.Double        ' Block to get length of semi-axis in z-direction    
    Dim rhoxyBlock As UI.Block.Double        ' Block to get sharpness in xy-direction      
    Dim rhozBlock As UI.Block.Double        ' Block to get sharpness in  z-direction

    Dim blob As NX.Body() = Nothing             ' The current blob (4 Bezier patches)

    ' Constructor to create a new BlobDialog
    Public Sub New()

        Me.Title = "Create Blob"    ' Title of dialog

        'Define the blocks we want on our dialog
        pointBlock = New UI.Block.SpecifyPoint()
        pointBlock.Label = "Center point"
        separator = New UI.Block.Separator()
        xLengthBlock = SpinControl("X semi-axis", 60, 5, 100, 5)
        yLengthBlock = SpinControl("Y semi-axis", 40, 5, 100, 5)
        zLengthBlock = SpinControl("Z semi-axis", 20, 5, 100, 5)
        rhoxyBlock = SpinControl("Rho XY", 0.7, 0.05, 0.95, 0.05)
        rhozBlock = SpinControl("Rho Z", 0.5, 0.05, 0.95, 0.05)

        ' Add all the blocks to the dialog
        Me.AddBlocks(pointBlock, separator, xLengthBlock, yLengthBlock, zLengthBlock, rhoxyBlock, rhozBlock)

    End Sub

    ' The main function
    Public Shared Sub Main()

        Dim dialog = New BlobDialog()   ' Create a dialog
        dialog.Show()                   ' Display it

    End Sub

    ' Function that gets called when user clicks Apply
    Public Overrides Sub OnApply()

        UpdateTheBlob()

    End Sub

    ' Function that gets called when user does anything in dialog
    Public Overrides Sub OnUpdate(changedBlock As UI.Block.General)

        If blob IsNot Nothing Then NX.NXObject.Delete(blob) ' Delete the existing blob
        UpdateTheBlob()                                        ' Create a new one

    End Sub

    ' Creates a specialized Double block with spin controls
    Public Function SpinControl(label As String, initialValue As Double, min As Double, max As Double, inc As Double) As UI.Block.Double

        Dim spin = New UI.Block.Double(label, initialValue)
        spin.PresentationStyle = UI.Block.NumberPresentationStyle.Spin
        spin.MinimumValue = min
        spin.MaximumValue = max
        spin.Increment = inc
        Return spin

    End Function

    ' Utility function for updating
    Public Sub UpdateTheBlob()

        Dim center = pointBlock.Position
        Dim a = xLengthBlock.Value
        Dim b = yLengthBlock.Value
        Dim c = zLengthBlock.Value
        Dim rhoXY = rhoxyBlock.Value
        Dim rhoZ = rhozBlock.Value
        blob = CreateBlob(center, a, b, c, rhoXY, rhoZ)

    End Sub

    ' Create four patches to form the blob shape
    Public Function CreateBlob(center As Position, a As Double, b As Double, c As Double, rhoXY As Double, rhoZ As Double) As NX.Body()

        Dim poles(2, 2) As Position     ' Poles of new surface
        poles(0, 0) = center + New Vector(a, 0, 0)
        poles(0, 1) = center + New Vector(a, b, 0)
        poles(0, 2) = center + New Vector(0, b, 0)

        poles(1, 0) = center + New Vector(a, 0, c)
        poles(1, 1) = center + New Vector(a, b, c)
        poles(1, 2) = center + New Vector(0, b, c)

        poles(2, 0) = center + New Vector(0, 0, c)
        poles(2, 1) = center + New Vector(0, 0, c)
        poles(2, 2) = center + New Vector(0, 0, c)

        Dim wXY = rhoXY / (1 - rhoXY)
        Dim wZ = rhoZ / (1 - rhoZ)

        Dim w(2, 2) As Double     ' Weights of surface
        w(0, 0) = 1 : w(0, 1) = wXY : w(0, 2) = 1
        w(1, 0) = wZ : w(1, 1) = wXY * wZ : w(1, 2) = wZ
        w(2, 0) = 1 : w(2, 1) = wXY : w(2, 2) = 1

        ' Create a rational Bezier patch in the positive octant
        Dim p1 = BezierPatch(poles, w)

        ' Create mirroring transformations
        Dim mirrorX = Geom.Transform.CreateReflection(Vector.AxisX, center.X)
        Dim mirrorY = Geom.Transform.CreateReflection(Vector.AxisY, center.Y)

        ' Create another three patches by mirroring
        Dim p2 = p1.Copy(mirrorY)
        Dim p3 = p1.Copy(mirrorX)
        Dim p4 = p2.Copy(mirrorX)

        Dim blob As NX.Body() = {p1, p2, p3, p4}

        Return blob

    End Function

End Class
