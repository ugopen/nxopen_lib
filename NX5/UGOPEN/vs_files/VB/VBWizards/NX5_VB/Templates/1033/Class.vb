Option Strict Off  

Imports NXOpen
Imports NXOpen.UF
Imports NXOpen.UI
Imports NXOpen.Utilities

'------------------------------------------------------------
'
'  Module MyProject
'
'      (Add description here)
'------------------------------------------------------------
Module MyProject


'------------------------------------------------------------
'
'  Main()
'
'      (Add description here)
'
'------------------------------------------------------------
Sub Main()

    'Add your code here


End Sub

'------------------------------------------------------------
'
'  GetUnloadOption()
'
'     Used to tell NX when to unload this library
'
'     Available options include:
'       Session.LibraryUnloadOption.Immediately
'       Session.LibraryUnloadOption.Explicitly
'       Session.LibraryUnloadOption.AtTermination
'
'     Any programs that register callbacks must use 
'     AtTermination as the unload option.
'------------------------------------------------------------
Public Function GetUnloadOption(ByVal dummy As String) As Integer
    GetUnloadOption = Session.LibraryUnloadOption.Immediately
End Function



End Module

