' ==================================================================================================
'
'            Copyright (c) 2004 UGS PLM Solutions.
'                   Unpublished - All rights reserved
'
'====================================================================================================
'File description:
'
'Test script EX_Curve_CreateSplineThruPts
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

Module EX_Curve_CreateSplineThruPts

    Dim createMaster As Boolean = False ' set to True if creating a master file
    Dim testName As String = "EX_Curve_CreateSplineThruPts"

    Dim theSession As Session
    Dim theUfSession As UFSession

    Public Const UF_CURVE_CRVATR_NONE As Integer = -1
    Public Const UF_CURVE_SLOPE_NONE As Integer = -1


    Public Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_Curve_CreateSplineThruPts.log", FileMode.Create, FileAccess.Write)
        Dim w As New StreamWriter(fs) ' create a stream writer 
        w.Write("Log Entry : \r\n")
        w.WriteLine("--Log entry goes here--")
        w.Flush() ' update underlying file

        If File.Exists("EX_Curve_CreateSplineThruPts.prt") Then
            w.WriteLine("Remove EX_Curve_CreateSplineThruPts.prt file from <Project Folder>\\bin\\Debug !!")
            w.WriteLine("EX_Curve_CreateSplineThruPts.prt already exists. !!")
            w.Close()
            Return
        End If

        Dim nError As Integer = Execute(w, theUfSession)
        w.WriteLine("End of Log File")
        w.Close()

    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As NXOpen.UF.UFSession) As Integer
        Try
            Dim PartTag As NXOpen.Tag
            Dim units As Integer = [UFConstants].ENGLISH
            Dim PartName As String

            theUfSession.Part.[New](testName, units, PartTag)
            theUfSession.Part.AskPartName(PartTag, PartName)
            stream.WriteLine("New Part File Created :-" + testName)

            'B-spline parameters
            stream.WriteLine("CreateSplineThruPts Data Creation:-")
            Dim degree As Integer = 3
            Dim periodicity As Integer = 0
            Dim num_points As Integer = 5

            ' Point/slope UFCurve attribute array *
            Dim point_data(num_points) As UFCurve.PtSlopeCrvatr

            '' Arrays of user's defining point data 
            Dim parameters() As Double = {0.0, 0.17, 0.32, 0.45, 1.29}
            Dim points() As Double = {1.1, 0.532, 2.0, 1.524, 0.6789, 2.3, 2.0, 0.9, 3.5956, 2.3456, 1.3456, 3.789, 3.1, 2.4567, 3.3214}

            Dim slopeTypes() As Integer = {[UFConstants].UF_CURVE_SLOPE_DIR, [UFConstants].UF_CURVE_SLOPE_AUTO, UF_CURVE_SLOPE_NONE, [UFConstants].UF_CURVE_SLOPE_DIR, [UFConstants].UF_CURVE_SLOPE_VEC}
            Dim slopeVecs() As Double = {1.23, 5.0506, 4.036, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 0.5, 1.0, -2.0, 1.0}
            Dim crvatrTypes() As Integer = {UF_CURVE_CRVATR_NONE, [UFConstants].UF_CURVE_CRVATR_AUTO_DIR, UF_CURVE_CRVATR_NONE, [UFConstants].UF_CURVE_CRVATR_VEC, [UFConstants].UF_CURVE_CRVATR_VEC}
            Dim crvatrVecs() As Double = {0.0, 0.0, 0.0, 1.0, 2.578, 5.67, 0.0, 0.0, 0.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0}

            Dim save_def_data As Integer = 1
            Dim spline_tag As Tag

            For i As Integer = 0 To num_points - 1
                point_data(i) = New UFCurve.PtSlopeCrvatr
                Dim tempPoints(2) As Double
                tempPoints(0) = points(3 * i)
                tempPoints(1) = points(3 * i + 1)
                tempPoints(2) = points(3 * i + 2)
                point_data(i).point = tempPoints
                point_data(i).slope_type = slopeTypes(i)
                Dim tempSlope(2) As Double
                tempSlope(0) = slopeVecs(3 * i)
                tempSlope(1) = slopeVecs(3 * i + 1)
                tempSlope(2) = slopeVecs(3 * i + 2)
                point_data(i).slope = tempSlope
                point_data(i).crvatr_type = crvatrTypes(i)
                Dim tempCrvatr(2) As Double
                tempCrvatr(0) = crvatrVecs(3 * i)
                tempCrvatr(1) = crvatrVecs(3 * i + 1)
                tempCrvatr(2) = crvatrVecs(3 * i + 2)
                point_data(i).crvatr = tempCrvatr
            Next
            stream.WriteLine("Successful")
            'Create B-spline UFCurve 
            stream.WriteLine("Create Spine Through Points= ")
            theUfSession.Curve.CreateSplineThruPts(degree, periodicity, num_points, point_data, parameters, save_def_data, spline_tag)
            stream.WriteLine("Successful")

            'Ask spline thr points parameters
            stream.WriteLine("Query Spine Through Points= ")
            Dim ask_degree As Integer
            Dim ask_periodicity As Integer
            Dim ask_num_points As Integer
            Dim ask_parameters() As Double
            Dim ask_point_data() As UFCurve.PtSlopeCrvatr
            theUfSession.Curve.AskSplineThruPts(spline_tag, ask_degree, ask_periodicity, ask_num_points, ask_point_data, ask_parameters)
            stream.WriteLine("Successful")
            stream.WriteLine("SplineThruPts Data")
            stream.WriteLine("degree= " + ask_degree.ToString)
            stream.WriteLine("periodicity= " + ask_periodicity.ToString)
            stream.WriteLine("num_points= " + ask_num_points.ToString)
            stream.Write("parameters= {")
            For J As Integer = 0 To ask_parameters.Length - 1
                stream.Write(ask_parameters(J).ToString)
                if(J < ask_parameters.Length - 1)
                    stream.Write(",")
                End if
            Next
            stream.WriteLine("}")

            stream.Write("point_data= {")
            For i As Integer = 0 To ask_point_data.Length - 1
                stream.Writeline("------------point_data[{0}]", i)
                stream.Write("point {")
                For j As Integer = 0 To ask_point_data(i).point.Length - 1
                    stream.Write(ask_point_data(i).point(j))
                    if(j < ask_point_data(i).point.Length - 1)
                        stream.Write(",")
                    End if
                Next
                stream.WriteLine("}")
                stream.Writeline("slope_type " + ask_point_data(i).slope_type.ToString)
                stream.Write("slope {")
                For k As Integer = 0 To ask_point_data(i).slope.Length - 1
                    stream.Write(ask_point_data(i).slope(k))
                    if(k < ask_point_data(i).slope.Length - 1)
                        stream.Write(",")
                    End if
                Next
                stream.WriteLine("}")
                stream.Writeline("crvatr_type " + ask_point_data(i).crvatr_type.ToString)
                stream.Write("crvatr {")
                For l As Integer = 0 To ask_point_data(i).crvatr.Length - 1
                    stream.Write(ask_point_data(i).crvatr(l))
                    if(l < ask_point_data(i).crvatr.Length - 1)
                        stream.Write(",")
                    End if
                Next
                stream.Writeline("}")
            Next

            theUfSession.Part.Save()

        Catch ex As Exception
            stream.WriteLine("EXCEPTION: ", ex.Message)
            Return 1
        End Try
        Return 0

    End Function

End Module
