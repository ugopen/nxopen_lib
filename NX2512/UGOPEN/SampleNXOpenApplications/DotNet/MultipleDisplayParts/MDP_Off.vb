' ===================================================================
'
'             Copyright (c) 2016  Siemens PLM 
'               Unpublished - All rights reserved
'
' ===================================================================
' *******************************************************************
'  Description

'
'  
'
' *******************************************************************
Imports System
Imports NXOpen


Module NXJournal
Sub Main (ByVal args() As String) 

	Dim theSession As NXOpen.Session = NXOpen.Session.GetSession()
	Dim theUI As NXOpen.UI = NXOpen.UI.GetUI()
	Dim theMessageBox = theUI.NXMessageBox

	theSession.Parts.SetAllowMultipleDisplayedParts(false)

	Dim theMDPStatus As NXOpen.PartCollection.MultipleDisplayedPartStatus = theSession.Parts.AllowMultipleDisplayedParts

	theMessageBox.Show("Multiple Display Part Status",  NXOpen.NXMessageBox.DialogType.Information, "The status is " +theMDPStatus.toString())


End Sub
End Module
