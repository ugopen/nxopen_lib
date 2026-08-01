Imports System
Imports NXOpen
Imports NXOpen.Selection
Imports NXOpenUI

' NX Open example showing how to use the SelectionManager
' to let the user pick NX objects. The specific type of 
' object to be selected is defined using a mask triple.
Module NXOpenSample
  Sub Main ()

    Dim theSession = Session.GetSession()
    Dim theUI = UI.GetUI()

    Dim workPart = theSession.Parts.Work

    Dim selection = theUI.SelectionManager
    Dim selectedObject As TaggedObject
    Dim cursor As Point3d

    Dim cue = "Please select a line to be hidden"
    Dim title = "Select Lines"
    Dim scope = SelectionScope.AnyInAssembly
    Dim action = SelectionAction.ClearAndEnableSpecific
    Dim keepHighlighted = False
    Dim includeFeatures = False
    Dim lineMask = New MaskTriple(NXOpen.UF.UFConstants.UF_line_type, 0, 0)
    Dim maskArray(1) As MaskTriple
    maskArray(0) = lineMask

    Dim resp = selection.SelectTaggedObject(cue, title, scope, action,
      includeFeatures, keepHighlighted, maskArray, selectedObject, cursor)


    If resp <> Response.Back resp <> Response.Cancel Then
      Dim dispObj = CType(selectedObject, DisplayableObject)
      dispObj.Blank()
    End If

  End Sub
End Module
