Imports System
Imports NXOpen
Imports NXOpen.Selection
Imports NXOpenUI

' NX Open example showing how to use the SelectionManager
' to let the user pick NX objects
Module NXOpenSample
  Sub Main ()

    Dim theSession = Session.GetSession()
    Dim theUI = UI.GetUI()

    Dim workPart = theSession.Parts.Work

    Dim selManager = theUI.SelectionManager
    Dim selectedObject As TaggedObject
    Dim cursor As Point3d

    Dim message = "Please select a curve to be hidden"
    Dim title = "Select Curves"
    Dim scope = SelectionScope.AnyInAssembly
    Dim action = SelectionAction.ClearAndEnableSpecific
    Dim keepHighlighted = False
    Dim typeArray As SelectionType() = {SelectionType.Curves}

    Dim response = selManager.SelectTaggedObject(message, title, scope, keepHighlighted, 
      typeArray, selectedObject, cursor) 

    If response <> Response.Cancel And 
        response <> Response.Back Then
      Dim dispObj = CType(selectedObject, DisplayableObject)
      dispObj.Blank()
    End If

  End Sub
End Module
