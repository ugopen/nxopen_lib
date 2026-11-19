Imports System
Imports NXOpen
Imports NXOpen.Selection
Imports NXOpenUI

' NX Open example showing how to use the SelectionManager
' to let the user pick faces in a part. This example uses
' mask triples to filter the selection to only allow picking
' faces.
Module NXOpenSample
  Sub Main ()

    Dim theSession = Session.GetSession()
    Dim theUI = UI.GetUI()

    Dim workPart = theSession.Parts.Work

    Dim selection = theUI.SelectionManager
    Dim selectedObject As TaggedObject
    Dim cursor As Point3d

    Dim message = "Please select a face to be hidden"
    Dim title = "Select Faces"
    Dim scope = SelectionScope.AnyInAssembly
    Dim action = SelectionAction.ClearAndEnableSpecific
    Dim keepHighlighted = False
    Dim includeFeatures = False
    Dim faceMask = New MaskTriple(NXOpen.UF.UFConstants.UF_solid_type, 0, NXOpen.UF.UFConstants.UF_solid_face_subtype)
    Dim maskArray(1) As MaskTriple
    maskArray(0) = faceMask

    Dim response = selection.SelectTaggedObject(message, title, scope, action,
      includeFeatures, keepHighlighted, maskArray, selectedObject, cursor)

    If response <> NXOpen.Selection.Response.Cancel Then
      Dim dispObj = CType(selectedObject, DisplayableObject)
      dispObj.Blank()
    End If

  End Sub
End Module
