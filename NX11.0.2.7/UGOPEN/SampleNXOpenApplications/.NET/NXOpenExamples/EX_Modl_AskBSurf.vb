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

Module EX_Modl_AskBSurf

    Dim theSession As Session
    Dim theUfSession As UFSession

    Public Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_Modl_AskBSurf.log", FileMode.Create, FileAccess.Write)
        Dim stream As New StreamWriter(fs) ' create a stream writer 
        stream.WriteLine("--Log entry goes here--")
        stream.Flush() ' update underlying file

        If File.Exists("EX_Modl_AskBSurf.prt") Then
            stream.WriteLine("Remove EX_Modl_AskBSurf.prt file from <Project Folder>\\bin\\Debug !!")
            stream.WriteLine("EX_Modl_AskBSurf.prt already exists. !!")
            stream.Close()
            Return
        End If

        Dim nError As Integer = Execute(stream, theUfSession)
        stream.WriteLine("End of Log File")
        stream.Close()

    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As NXOpen.UF.UFSession) As Integer

        Try
            Dim PartTag As NXOpen.Tag
            Dim units As Integer = [UFConstants].ENGLISH
            Dim PartName As String = "EX_Modl_AskBSurf"

            theUfSession.Part.[New](PartName, units, PartTag)
            theUfSession.Part.AskPartName(PartTag, PartName)
            stream.Write("New Part File Created :-" + PartName)
            Dim knot_fixup, pole_fixup As Integer
            Dim bcurv1, bcurv2, bsurf As Tag

            Dim bsurf_idata() As Integer = {4, 4, 4, 4}
            Dim bsurf_uknot() As Double = {0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0}
            Dim bsurf_vknot() As Double = {0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0}
            Dim bsurf_poles() As Double = {0.0, 0.0, 6.0, 1.0, 2.0, 2.0, 6.0, 1.0, 5.0, 1.5, 6.0, 1.0, 8.0, 3.0, 6.0, 1.0, 0.0, 2.0, 4.0, 1.0, 2.0, 4.0, 4.0, 1.0, 5.0, 3.5, 4.0, 1.0, 8.0, 5.0, 4.0, 1.0, 0.0, 2.0, 2.0, 1.0, 2.0, 4.0, 2.0, 1.0, 5.0, 3.5, 2.0, 1.0, 8.0, 5.0, 2.0, 1.0, 0.0, 0.0, 0.0, 1.0, 2.0, 2.0, 0.0, 1.0, 5.0, 1.5, 0.0, 1.0, 8.0, 3.0, 0.0, 1.0}
            Dim bcurv1_idata() As Integer = {3, 3}
            Dim bcurv1_knots() As Double = {0.0, 0.0, 0.0, 1.0, 1.0, 1.0}
            Dim bcurv1_poles() As Double = {-0.5, -2.5, 3.5, 1.0, 2.5, -2.5, 3.5, 1.0, 2.5, -2.5, 6.5, 1.0}
            Dim bcurv2_idata() As Integer = {8, 4}
            Dim bcurv2_knots() As Double = {-0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6}
            Dim bcurv2_poles() As Double = {3.0, -2.5, 2.0, 1.0, 4.0, -2.5, 1.0, 1.0, 7.0, -2.5, 1.0, 1.0, 6.0, -2.5, 3.0, 1.0, 3.0, -2.5, 3.0, 1.0, 3.0, -2.5, 2.0, 1.0, 4.0, -2.5, 1.0, 1.0, 7.0, -2.5, 1.0, 1.0}
            Dim proj_vector() As Double = {0.0, 1.0, 0.0}
            Dim ptdata() As Double = {1.312, 1.896, 4.8, 4.464, 3.312, 2.4}

            'double'] gap_pts
            'double tol = 0.001

            ' Create the b-surface.
            stream.Write("Create the b-surface using Modl.CreateBsurf:-")
            theUfSession.Modl.CreateBsurf(bsurf_idata(0), bsurf_idata(1), bsurf_idata(2), bsurf_idata(3), bsurf_uknot, bsurf_vknot, bsurf_poles, bsurf, knot_fixup, pole_fixup)
            stream.WriteLine("Successful")

            ' Ask b-surface
            stream.Write("Query the b-surface using Modl.AskBsurf:-")
            Dim bSurfData As UFModl.Bsurface
            theUfSession.Modl.AskBsurf(bsurf, bSurfData)
            stream.WriteLine("Successful")

            'Create the spline1.
            stream.Write("Create the Spline-1 using Modl.CreateSpline:-")
            theUfSession.Modl.CreateSpline(bcurv1_idata(0), bcurv1_idata(1), bcurv1_knots, bcurv1_poles, bcurv1, knot_fixup, pole_fixup)
            stream.WriteLine("Successful")

            'Create the spline2.
            stream.Write("Create the Spline-2 using Modl.CreateSpline:-")
            theUfSession.Modl.CreateSpline(bcurv2_idata(0), bcurv2_idata(1), bcurv2_knots, bcurv2_poles, bcurv2, knot_fixup, pole_fixup)
            stream.WriteLine("Successful")

            'Query Spline Data
            stream.Write("Query the Spline using Curve.AskSplineData:-")
            Dim cSpline As UFCurve.Spline
            theUfSession.Curve.AskSplineData(bcurv2, cSpline)
            stream.WriteLine("Successful")

            stream.WriteLine("Spline Data:-")
            stream.WriteLine("Start Param =" + cSpline.start_param.ToString)
            stream.WriteLine("End Param=" + cSpline.end_param.ToString)
            stream.WriteLine("Is Rational=" + cSpline.is_rational.ToString)
            stream.WriteLine("Order=" + cSpline.order.ToString)
            stream.WriteLine("Number of Poles=" + cSpline.num_poles.ToString)

            For I As Integer = 0 To (cSpline.poles.Length / 4) - 1
                stream.WriteLine("Pole[{0},0]= {1}", I, cSpline.poles(I, 0).ToString)
                stream.WriteLine("Pole[{0},1]= {1}", I, cSpline.poles(I, 1).ToString)
                stream.WriteLine("Pole[{0},2]= {1}", I, cSpline.poles(I, 2).ToString)
                stream.WriteLine("Pole[{0},3]= {1}", I, cSpline.poles(I, 3).ToString)
            Next

            theUfSession.Modl.Update()

            'Save the Part
            theUfSession.Part.Save()

        Catch ex As Exception
            stream.WriteLine("EXCEPTION: ", ex.Message)
            Return 1
        End Try
        
        Return 0
    End Function

End Module


