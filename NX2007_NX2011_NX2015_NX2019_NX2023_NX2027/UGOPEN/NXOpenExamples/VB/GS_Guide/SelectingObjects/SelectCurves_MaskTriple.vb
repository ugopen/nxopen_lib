Imports System
Imports NXOpen
Imports NXOpen.Selection
Imports NXOpenUI

' NX Open example showing how to use the SelectionManager
' to let the user pick NX objects. This example uses a mask
' triple array to filter the selection to several different
' types of NX objects.
Module NXOpenSample
  Sub Main ()

    Dim theSession = Session.GetSession()
    Dim theUI = UI.GetUI()

    Dim workPart = theSession.Parts.Work

    Dim selection = theUI.SelectionManager
    Dim selectedObjects() As TaggedObject
    Dim cursor As Point3d
    'Dim view As View

    Dim cue = "Please select the curves to be hidden"
    Dim title = "Select Curves"
    Dim scope = SelectionScope.AnyInAssembly
    Dim action = SelectionAction.ClearAndEnableSpecific
    Dim keepHighlighted = False
    Dim includeFeatures = False
    Dim lineMask = New MaskTriple(NXOpen.UF.UFConstants.UF_line_type, 0, 0)
    Dim circleMask = New MaskTriple(NXOpen.UF.UFConstants.UF_circle_type, NXOpen.UF.UFConstants.UF_all_subtype, 0)
    Dim conicMask = New MaskTriple(NXOpen.UF.UFConstants.UF_conic_type, NXOpen.UF.UFConstants.UF_all_subtype, 0)
    Dim spCurveMask = New MaskTriple(NXOpen.UF.UFConstants.UF_spcurve_type, NXOpen.UF.UFConstants.UF_all_subtype, 0)
    Dim maskArray(4) As MaskTriple
    maskArray(0) = lineMask 
    maskArray(1) = circleMask 
    maskArray(2) = conicMask 
    maskArray(3) = spCurveMask 

    Dim response = selection.SelectTaggedObjects(cue, title, scope, action,
      includeFeatures, keepHighlighted, maskArray, selectedObjects)

    If response <> Response.Back And response <> Response.Cancel Then
      For Each selectedObject In SelectedObjects
        Dim dispObj = CType(selectedObject, DisplayableObject)
        dispObj.Blank()
      Next selectedObject
    End If

  End Sub
End Module
