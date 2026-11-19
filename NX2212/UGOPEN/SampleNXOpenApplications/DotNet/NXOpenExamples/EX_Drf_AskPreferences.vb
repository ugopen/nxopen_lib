' ==================================================================================================
'
'            Copyright (c) 2004 UGS PLM Solutions.
'                   Unpublished - All rights reserved
'
'====================================================================================================
'File description:
'
'Test script EX_Drf_AskPreferences
'
'====================================================================================================
'   Date      Name                    Description of Change
'   11-May-2004      Manoj Gupta             Updated Namespace Changes
'   23-Jun-2004      Atul Jawale             Add GetUnloadOption()
'   29-Jun-2004      Atul Jawale             Updated Error Messages
'   16-May-2005      Trupti Sahasrabudhe     Convert C# Example to VB.Net
'$HISTORY$
'====================================================================================================
Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.Features
Imports NXOpen.Preferences
Imports NXOpen.UF

Module EX_Drf_AskPreferences

    Dim theSession As Session
    Dim theUfSession As UFSession

    Public Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_Drf_AskPreferences.log", FileMode.Create, FileAccess.Write)
        Dim stream As New StreamWriter(fs) ' create a stream writer 
        stream.WriteLine("--Log entry goes here--")
        stream.Flush() ' update underlying file

        If File.Exists("EX_Drf_AskPreferences.prt") Then
            stream.WriteLine("Remove EX_Drf_AskPreferences.prt file from <Project Folder>\\bin\\Debug !!")
            stream.WriteLine("EX_Drf_AskPreferences.prt already exists. !!")
            stream.Close()
            Return
        End If

        Dim nError As Integer = Execute(stream, theUfSession)
        stream.WriteLine("End of Log File")
        stream.Close()

    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As NXOpen.UF.UFSession) As Integer

        Dim UFPart As NXOpen.Tag
        Dim part_name As String = "EX_Drf_AskPreferences"
        Dim units As Integer = 2

        theUfSession.Part.[New](part_name, units, UFPart)
        stream.WriteLine("New part: {0} ", part_name, " Created")

        Dim mpi_array(99) As Integer
        Dim mpr_array(69) As Double

        Dim rad_symbol, dia_symbol As String

        Dim part_tag As NXOpen.Tag = Tag.Null
        Dim dimension_tag As NXOpen.Tag = Tag.Null

        part_tag = theUfSession.Part.AskDisplayPart()
        stream.WriteLine("Dimension Creation method: 1- Automatic Text\n")
        stream.WriteLine("                           2- Automatic Text, Appended Text\n")
        stream.WriteLine("                           3- Manual Text\n")
        stream.WriteLine("                            4-Manual Text, Appended Text.\n")
        stream.WriteLine("Dimension Tag    Creation symbol\n\n")
        'cycle for dimensions 
        theUfSession.Obj.CycleObjsInPart(part_tag, UFConstants.UF_dimension_type, dimension_tag)
        'find dimension creation parameters
        theUfSession.Drf.AskPreferences(mpi_array, mpr_array, rad_symbol, dia_symbol)

        For i As Integer = 0 To 99 - 1
            stream.WriteLine(mpi_array(i))
            If (i Mod 3 <> 0) Then
                stream.WriteLine("")
            End If
        Next


        For l As Integer = 0 To 51 - 1
            stream.WriteLine(mpi_array(l))
            If (l Mod 3 <> 0) Then
                stream.WriteLine("")
            End If
        Next

        mpi_array(6) = 4 'Set Tolerance type 
        mpi_array(12) = 2 'Set Tolerance site 

        mpr_array(24) = 0.02  'Set Upper Tolerance 
        mpr_array(25) = 0.02  'Set Lower Tolerance 

        theUfSession.Drf.AskPreferences(mpi_array, mpr_array, rad_symbol, dia_symbol)

        For l As Integer = 0 To 99 - 1
            stream.WriteLine(mpi_array(l))
            If (l Mod 3 <> 0) Then
                stream.WriteLine()
            End If
        Next

        For l As Integer = 0 To 51 - 1
            stream.WriteLine(mpi_array(l))
            If (l Mod 3 <> 0) Then
                stream.WriteLine()
            End If
        Next

        stream.WriteLine("")
        stream.WriteLine("")
        theUfSession.Part.Save()

        Return 0

    End Function

End Module


