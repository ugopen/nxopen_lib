' ==================================================================================================
'
'            Copyright (c) 2004 UGS PLM Solutions.
'                   Unpublished - All rights reserved
'
'====================================================================================================
'File description: Example for Wrapped UFUNC (NXOpen.NET)
' 
'====================================================================================================
Option Strict Off
Imports System
Imports System.IO
Imports System.Runtime.InteropServices
Imports NXOpen
Imports NXOpen.Features
Imports NXOpen.Preferences
Imports NXOpen.UF

Module EX_Modl_CreateExtruded

    Dim theSession As Session
    Dim theUfSession As UFSession

    Public Const PI As Double = 3.1415926535897931

    Public Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_Modl_CreateExtruded.log", FileMode.Create, FileAccess.Write)
        Dim stream As New StreamWriter(fs) ' create a stream writer 
        stream.WriteLine("--Log entry goes here--")
        stream.Flush() ' update underlying file

        If File.Exists("EX_Modl_CreateExtruded.prt") Then
            stream.WriteLine("Remove EX_Modl_CreateExtruded.prt file from <Project Folder>\\bin\\Debug !!")
            stream.WriteLine("EX_Modl_CreateExtruded.prt already exists. !!")
            stream.Close()
            Return
        End If

        Dim nError As Integer = Execute(stream, theUfSession)
        stream.WriteLine("End of Log File")
        stream.Close()

    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As NXOpen.UF.UFSession) As Integer
        Try
            Dim UFPart As NXOpen.Tag
            Dim part_name As String = "EX_Modl_CreateExtruded"
            Dim units As Integer = 2
            Dim name As String

            theUfSession.Part.[New](part_name, units, UFPart)
            stream.WriteLine("New part : ", part_name, " Created")

            Dim l1_endpt1() As Double = {-1.4476606170268, 2.3788333712953, 0.0}
            Dim l1_endpt2() As Double = {1.5471310496399, 2.2539419253757, 0.0}
            Dim l2_endpt1() As Double = {-1.4476606170268, 1.2548103580189, 0.0}
            Dim l2_endpt2() As Double = {1.5471310496399, 1.3797018039385, 0.0}
            Dim l3_endpt1() As Double = {-1.4710981170268, 1.8168218646571, 0.0}
            Dim l3_endpt2() As Double = {1.5289018829732, 1.8168218646571, 0.0}
            Dim direction() As Double = {0.0, 0.0, 1.0}
            Dim ref_pt(3) As Double
            Dim arc1_start_ang As Double = (PI / 180) * 87.611984536731
            Dim arc1_end_ang As Double = (PI / 180) * 272.38801546327
            Dim arc1_rad As Double = 0.5625
            Dim arc2_start_ang As Double = (PI / 180) * 272.38801546327
            Dim arc2_end_ang As Double = (PI / 180) * 447.61198453673
            Dim arc2_rad As Double = 0.4375
            Dim taper_angle As String = "0.0"
            Dim limit1() As String = {"1.0", "1.25"}
            Dim i As Integer
            Dim count As Integer = 4
            Dim objarray(5) As NXOpen.Tag
            Dim wcs_tag, matrix_tag As NXOpen.Tag
            Dim loop_list(), features() As NXOpen.Tag
            Dim line1 As NXOpen.UF.UFCurve.Line = New NXOpen.UF.UFCurve.Line
            Dim line2 As NXOpen.UF.UFCurve.Line = New NXOpen.UF.UFCurve.Line
            Dim line3 As NXOpen.UF.UFCurve.Line = New NXOpen.UF.UFCurve.Line
            Dim arc1 As NXOpen.UF.UFCurve.Arc = New NXOpen.UF.UFCurve.Arc
            Dim arc2 As NXOpen.UF.UFCurve.Arc = New NXOpen.UF.UFCurve.Arc

            line1.start_point = l1_endpt1
            line1.end_point = l1_endpt2
            line2.start_point = l2_endpt1
            line2.end_point = l2_endpt2
            line3.start_point = l3_endpt1
            line3.end_point = l3_endpt2

            arc1.start_angle = arc1_start_ang
            arc1.end_angle = arc1_end_ang
            arc1.arc_center = l3_endpt1
            arc1.radius = arc1_rad

            arc2.start_angle = arc2_start_ang
            arc2.end_angle = arc2_end_ang
            arc2.arc_center = l3_endpt2
            arc2.radius = arc2_rad

            theUfSession.Curve.CreateLine(line1, objarray(0))
            stream.WriteLine("Successful:Curve.CreateLine")

            theUfSession.Curve.CreateLine(line2, objarray(1))
            stream.WriteLine("Successful:Curve.CreateLine")

            theUfSession.Curve.CreateLine(line3, objarray(4))
            stream.WriteLine("Successful:Curve.CreateLine")

            theUfSession.Csys.AskWcs(wcs_tag)
            stream.WriteLine("Successful:Csys.AskWcs")

            theUfSession.Csys.AskMatrixOfObject(wcs_tag, matrix_tag)
            stream.WriteLine("Successful:Csys.AskMatrixOfObject")

            arc1.matrix_tag = matrix_tag
            arc2.matrix_tag = matrix_tag
            theUfSession.Curve.CreateArc(arc1, objarray(2))
            stream.WriteLine("Successful:Curve.CreateArc")

            theUfSession.Curve.CreateArc(arc2, objarray(3))
            stream.WriteLine("Successful:Curve.CreateArc")

            'Create loop list
            Dim arr_loop_list As System.Collections.ArrayList = New System.Collections.ArrayList
            For i = 0 To count - 1
                arr_loop_list.Add(objarray(i))
            Next
            Dim t As System.Type
            t = GetType(NXOpen.Tag)
            loop_list = arr_loop_list.ToArray(t)

            'while sending parameters to this function the order was 
            'loop_list, taper_angle, limit1, ref_pt, FeatureSigns.Nullsign, direction, out features
            'as above .. there were some compilation problem due to function prototype match.
            'Atul changed the order as follows in order to compile it successfully.
            'loop_list, taper_angle, limit1, ref_pt, direction, FeatureSigns.Nullsign, out features
            theUfSession.Modl.CreateExtruded(loop_list, taper_angle, limit1, ref_pt, direction, FeatureSigns.Nullsign, features)
            stream.WriteLine("Successful:Modl.CreateExtruded")

            'Save the Part
            theUfSession.Part.Save()
        Catch ex As Exception
            stream.WriteLine("EXCEPTION: ", ex.Message)
            Return 1
        End Try

        Return 0
    End Function

End Module


