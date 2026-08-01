Option Strict Off
Imports System
Imports NXOpen

Module NXJournal
Sub Main

        Dim theSession As Session = Session.GetSession()
        Dim workPart As Part = theSession.Parts.Work

        Dim displayPart As Part = theSession.Parts.Display

        ' ----------------------------------------------
        '   Creates a diamemter dimension on an arc
        ' ----------------------------------------------
        Dim markId1 As Session.UndoMarkId = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Create Dimension")

        Dim dimensionData1 As Annotations.DimensionData = workPart.Annotations.NewDimensionData()
        Dim associativity1 As Annotations.Associativity = workPart.Annotations.NewAssociativity()
        Dim cylinder1 As Features.Cylinder = CType(workPart.Features.FindObject("CYLINDER(0)"), Features.Cylinder)
 
        associativity1.FirstObject = CType(cylinder1.FindObject("EDGE * 3 * 1"), Edge)
        associativity1.SecondObject = Nothing
        associativity1.ObjectView = CType(workPart.DraftingViews.FindObject("TOP@1"), Drawings.BaseView)
        associativity1.PointOption = Annotations.AssociativityPointOption.None
        associativity1.LineOption = Annotations.AssociativityLineOption.None

        Dim associativity2(0) As Annotations.Associativity
        associativity2(0) = associativity1
        dimensionData1.SetAssociativity(1, associativity2)

        Dim origin As Point3d = New Point3d(50, 50, 0.0)

        Dim diameterDimension As Annotations.DiameterDimension = workPart.Dimensions.CreateDiameterDimension(dimensionData1, origin)
        diameterDimension.LeaderOrientation = Annotations.LeaderOrientation.FromLeft

        dimensionData1.Dispose()
        associativity1.Dispose()

End Sub
End Module
