'=============================================================================
'
'                   Copyright (c) 2004 UGS PLM Solutions
'                    Unpublished - All rights reserved
'
'===============================================================================
'File description: Example for Wrapped UFUNC (NXOpen.NET)
' 
Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.UF
Imports NXOpen.Utilities

Module EX_Curve_CreateFillet

    Dim testName As String = "uf_curve_CreateFillet"

    Dim theSession As Session
    Dim theUfSession As UFSession
    Public Const UF_CURVE_2_CURVE As Integer = 0
    Public Const DEGRA As Double = 0.017453292519943282

    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_Curve_CreateFillet.log", FileMode.Create, FileAccess.Write)
        Dim w As New StreamWriter(fs) ' create a stream writer 
        w.Write("Log Entry : \r\n")
        w.WriteLine("--Log entry goes here--")
        w.Flush() ' update underlying file

        If File.Exists("EX_Curve_CreateFillet.prt") Then
            w.WriteLine("Remove EX_Curve_CreateFillet.prt file from <Project Folder>\\bin\\Debug !!")
            w.WriteLine("EX_Curve_CreateFillet.prt already exists. !!")
            w.Close()
            Return
        End If

        Dim nError As Integer = Execute(w, theUfSession)
        w.WriteLine("End of Log File")
        w.Close()

    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As NXOpen.UF.UFSession) As Integer

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim UFPart As NXOpen.Tag
        Dim part_name As String = "EX_Curve_CreateFillet"
        Dim units As Integer = 2
        Dim name As String

        Try
            theUfSession.Part.[New](part_name, units, UFPart)
            stream.WriteLine("New part : ", testName, " Created")

            Dim center(3) As Double
            Dim radius As Double
            Dim trim_opts(3) As Integer
            Dim arc_opts() As Integer = {0, 0, 0}

            Dim line_coords1 As NXOpen.UF.UFCurve.Line = New NXOpen.UF.UFCurve.Line

            Dim array1() As Double = {1.2, 0.2, 0.0}
            line_coords1.start_point = array1

            Dim array2() As Double = {-0.5, 2.5, 0.0}
            line_coords1.end_point = array2

            Dim line_coords2 As NXOpen.UF.UFCurve.Line = New NXOpen.UF.UFCurve.Line

            Dim array3() As Double = {3.2, 2.35, 0.0}
            line_coords2.start_point = array3

            Dim array4() As Double = {2.5, 3.5, 0.0}
            line_coords2.end_point = array4

            Dim arc_coords1 As NXOpen.UF.UFCurve.Arc = New NXOpen.UF.UFCurve.Arc
            arc_coords1.matrix_tag = NXOpen.Tag.Null
            arc_coords1.start_angle = 238 * DEGRA
            arc_coords1.end_angle = 357 * DEGRA

            Dim array5() As Double = {0.22, 4.3, 0.0}
            arc_coords1.arc_center = array5
            arc_coords1.radius = 2.0

            Dim arc_coords2 As NXOpen.UF.UFCurve.Arc = New NXOpen.UF.UFCurve.Arc
            arc_coords2.matrix_tag = NXOpen.Tag.Null
            arc_coords2.start_angle = 82 * DEGRA
            arc_coords2.end_angle = 175 * DEGRA

            Dim array6() As Double = {3.0, 0.43, 0.0}
            arc_coords2.arc_center = array6
            arc_coords2.radius = 2.0

            Dim line1, line2, arc1, arc2 As NXOpen.Tag
            Dim curve_objs(3) As NXOpen.Tag
            Dim fillet_obj1, fillet_obj2, wcs_tag, matrix_tag As NXOpen.Tag

            'create 2 lines 
            theUfSession.Curve.CreateLine(line_coords1, line1)
            stream.WriteLine("Successful:Curve.CreateLine")

            theUfSession.Curve.CreateLine(line_coords2, line2)
            stream.WriteLine("Successful:Curve.CreateLine")

            'create 2 arcs 
            theUfSession.Csys.AskWcs(wcs_tag)
            stream.WriteLine("Successful:Csys.AskWcs")

            theUfSession.Csys.AskMatrixOfObject(wcs_tag, matrix_tag)
            stream.WriteLine("Successful:Csys.AskMatrixOfObject")

            arc_coords1.matrix_tag = matrix_tag
            arc_coords2.matrix_tag = matrix_tag

            theUfSession.Curve.CreateArc(arc_coords1, arc1)
            stream.WriteLine("Successful:Curve.CreateArc")

            theUfSession.Curve.CreateArc(arc_coords2, arc2)
            stream.WriteLine("Successful:Curve.CreateArc")

            'create fillet between "arc1" and "line1"
            curve_objs(0) = arc1
            curve_objs(1) = line1
            center(0) = 0.0
            center(1) = 2.1
            center(2) = 0.0
            radius = 0.25
            trim_opts(0) = 1          'trim first UFCurve
            trim_opts(1) = 1         'trim second UFCurve

            theUfSession.Curve.CreateFillet(UF_CURVE_2_CURVE, curve_objs, center, radius, trim_opts, arc_opts, fillet_obj1)
            stream.WriteLine("Successful:Curve.CreateFillet")
            'create fillet between "line1" and "arc2"
            curve_objs(0) = line1
            curve_objs(1) = arc2
            center(0) = 0.8
            center(1) = 1.0
            center(2) = 0.0
            radius = 0.25
            trim_opts(0) = 1         'trim first UFCurve
            trim_opts(1) = 1         'trim second UFCurve

            theUfSession.Curve.CreateFillet(UF_CURVE_2_CURVE, curve_objs, center, radius, trim_opts, arc_opts, fillet_obj2)
            stream.WriteLine("Successful:Curve.CreateFillet")

            theUfSession.Part.Save()

        Catch ex As Exception
            stream.WriteLine("EXCEPTION: ", ex.Message)
            Return 1
        End Try

        Return 0

    End Function

    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = UFConstants.UF_UNLOAD_IMMEDIATELY
    End Function

End Module
