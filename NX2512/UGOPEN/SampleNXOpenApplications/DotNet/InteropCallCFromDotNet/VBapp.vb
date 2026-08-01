'=============================================================================
'                  Copyright (c) 2009 Siemens
'                      All rights reserved
'===============================================================================
'
'Description: wrappers to UFapp
'
' 
'=============================================================================*/

Imports System
Imports System.Runtime.InteropServices

Public Class wrappers
Const UFAPP_DLLNAME As String = "UFLegacyApp.dll"

'************************************************************************************
' Hookup to a function in UFapp

<DllImport(UFAPP_DLLNAME, EntryPoint:="UFappFunction1", _
CallingConvention:=CallingConvention.Cdecl, CharSet:=CharSet.Ansi)> _
Shared Function UFappFunction1() As Integer
End Function

'************************************************************************************
' Hookup to another function in UFapp


<DllImport(UFAPP_DLLNAME, EntryPoint:="UFappFunction2", _
CallingConvention:=CallingConvention.Cdecl, CharSet:=CharSet.Ansi)> _
Shared Function UFappFunction2(ByVal value As Integer, ByVal str As String) As Integer
End Function

End Class
