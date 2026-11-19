' ==================================================================================================
'
'            Copyright (c) 2004 UGS PLM Solutions.
'                   Unpublished - All rights reserved
'
'====================================================================================================
'File description:
'
'Test script EX_Curve_CreateSpline
'
' 
'====================================================================================================
Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.Features
Imports NXOpen.Preferences
Imports NXOpen.UF

Module EX_Curve_CreateSpline

    Dim createMaster As Boolean = False ' set to True if creating a master file
    Dim testName As String = "EX_Curve_CreateSpline"

    Dim theSession As Session
    Dim theUfSession As UFSession

    'Constants
    Public Const UF_OBJ_NAME_LEN As Integer = 30

    Public Sub Main()
        
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_Curve_CreateSpline.log", FileMode.Create, FileAccess.Write)
        Dim w As New StreamWriter(fs) ' create a stream writer 
        w.Write("Log Entry : \r\n")
        w.WriteLine("--Log entry goes here--")
        w.Flush() ' update underlying file

        If File.Exists("EX_Curve_CreateSpline.prt") Then
            w.WriteLine("Remove EX_Curve_CreateSpline.prt file from <Project Folder>\\bin\\Debug !!")
            w.WriteLine("EX_Curve_CreateSpline.prt already exists. !!")
            w.Close()
            Return
        End If

        Dim nError As Integer = Execute(w, theUfSession)
        w.WriteLine("End of Log File")
        w.Close()
    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As NXOpen.UF.UFSession) As Integer

        Dim UFPart As NXOpen.Tag
        Dim part_name As String = "EX_Curve_CreateSpline"
        Dim units As Integer = 2
        Dim name As String
        Dim curve_cnt As Integer = 0
        Dim curve_array As NXOpen.Tag
        Dim buf(UF_OBJ_NAME_LEN + 1) As Char
        Dim newnam As String = New String(buf)
        Dim num_infpts As Integer
        Dim range() As Double = {0.0, 100.0}
        Dim inf_pts() As Double
        Dim proj_matrx() As Double = {1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0}
        Dim knot1_fix, knot2_fix, pole1_fix, pole2_fix As Integer

        Dim bc1_knots() As Double = {-3.0 / 8.0, -2.0 / 8.0, -1.0 / 8.0, 0.0, 1.0 / 8.0, 2.0 / 8.0, 3.0 / 8.0, 4.0 / 8.0, 5.0 / 8.0, 6.0 / 8.0, 7.0 / 8.0, 1.0, 9.0 / 8.0, 10.0 / 8.0, 11.0 / 8}
        Dim bc1_poles() As Double = {2.0, 0.0, 0.0, 1.0, 4.0, 0.0, 0.0, 1.0, 3.5, 2.0, 0.0, 1.0, 6.0, 6.0, 0.0, 1.0, 2.0, 3.5, 0.0, 1.0, 0.0, 4.0, 0.0, 1.0, 0.0, 2.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 2.0, 0.0, 0.0, 1.0, 4.0, 0.0, 0.0, 1.0, 3.5, 2.0, 0.0, 1.0}

        Dim bc2_knots() As Double = {0.0, 0.0, 0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0, 1.0, 1.0}

        Dim bc2_poles() As Double = {0.0, 0.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.625, 0.0, 0.25, 0.25, 4.0, 2.0, 1.0, 1.0, 5.0, 0.0, 1.0, 1.0}

        Try
            theUfSession.Part.[New](part_name, units, UFPart)
            stream.WriteLine("New part : ", testName, " Created")

            'create two B-curves 
            theUfSession.Modl.CreateSpline(11, 4, bc1_knots, bc1_poles, curve_array, knot1_fix, pole1_fix)
            stream.WriteLine("Successful:Modl.CreateSpline")
            newnam = String.Copy("BCURVE_1")

            theUfSession.Obj.SetName(curve_array, newnam)
            stream.WriteLine("Successful:Obj.SetName")
            curve_cnt = curve_cnt + 1
            theUfSession.Modl.CreateSpline(5, 3, bc2_knots, bc2_poles, curve_array, knot2_fix, pole2_fix)
            stream.WriteLine("Successful:Modl.CreateSpline")
            newnam = String.Copy("BCURVE_2")
            theUfSession.Obj.SetName(curve_array, newnam)
            stream.WriteLine("Successful:Obj.SetName")
            curve_cnt = curve_cnt + 1

            'loop over each UFCurve and compute their inflections 
            For l As Integer = 0 To curve_cnt - 1
                'used a pre-definied projection matrix and predefined UFCurve's
                'range for the inflection points calculation
                theUfSession.Curve.AskCurveInflections(curve_array, proj_matrx, range, num_infpts, inf_pts)
                stream.WriteLine("Successful:Curve.AskCurveInflections")
                If (num_infpts > 0) Then
                    stream.WriteLine("There are {0} inflection points for UFCurve {1}", num_infpts, l + 1)
                    For k As Integer = 0 To (num_infpts * 4) - 1
                        stream.WriteLine("inf_pts[{0}] = {1}", k, inf_pts(k))
                    Next
                End If
            Next
            theUfSession.Part.Save()

        Catch ex As Exception
            stream.WriteLine("EXCEPTION: ", ex.Message)
            Return 1

        End Try
        Return 0
    End Function

End Module


