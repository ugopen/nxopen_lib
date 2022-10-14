' ==================================================================================================
'
'            Copyright (c) 2004 UGS PLM Solutions.
'                   Unpublished - All rights reserved
'
'====================================================================================================
'File description:
'
'Test script EX_Curve_ProjCurves
'
'====================================================================================================
'   Date      Name                    Description of Change
'06-May-2004  Trupti Sahasrabudhe     Intial Creation
'19-May-2004  Alasdair Mackintosh     Use new TestSession class to obtain Session object
'16-May-2005  Trupti Sahasrabudhe     Convert C# Example to VB.Net
'$HISTORY$
'====================================================================================================
Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.Features
Imports NXOpen.Preferences
Imports NXOpen.UF

Module EX_Curve_ProjCurves

    Dim createMaster As Boolean = False ' set to True if creating a master file
    Dim testName As String = "EX_Curve_ProjCurves"

    Dim theSession As Session
    Dim theUfSession As UFSession

    Public Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_Curve_ProjCurves.log", FileMode.Create, FileAccess.Write)
        Dim w As New StreamWriter(fs) ' create a stream writer 
        w.Write("Log Entry : \r\n")
        w.WriteLine("--Log entry goes here--")
        w.Flush() ' update underlying file

        If File.Exists("EX_Curve_ProjCurves.prt") Then
            w.WriteLine("Remove EX_Curve_ProjCurves.prt file from <Project Folder>\\bin\\Debug !!")
            w.WriteLine("EX_Curve_ProjCurves.prt already exists. !!")
            w.Close()
            Return
        End If

        Dim nError As Integer = Execute(w, theUfSession)
        w.WriteLine("End of Log File")
        w.Close()
        
    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As NXOpen.UF.UFSession) As Integer

        Dim UFPart As NXOpen.Tag
        Dim part_name As String = "EX_Curve_ProjCurves"
        Dim units As Integer = 2
        Dim name As String
        Dim num_faces, num_proj_curves As Integer
        Dim origin() As Double = {0.0, 0.0, 0.0}
        Dim block_tag As NXOpen.Tag
        Dim curves_to_proj(1) As NXOpen.Tag
        Dim proj_curve_feature As NXOpen.Tag
        Dim proj_curves() As NXOpen.Tag
        Dim defining_feature, defining_target, defining_curve As NXOpen.Tag
        Dim edge_lens() As String = {"300.0", "25.0", "150.0"}
        Dim line_data As NXOpen.UF.UFCurve.Line = New NXOpen.UF.UFCurve.Line
        Dim proj_data As NXOpen.UF.UFCurve.Proj = New NXOpen.UF.UFCurve.Proj
        Dim face_list() As NXOpen.Tag

        Try
            theUfSession.Part.[New](part_name, units, UFPart)
            stream.WriteLine("New part : ", testName, " Created")

            theUfSession.Modl.CreateBlock1(FeatureSigns.Nullsign, origin, edge_lens, block_tag)
            stream.WriteLine("Successful:Modl.CreateBlock1")

            Dim array1() As Double = {25.0, 50.0, 25.0}
            line_data.start_point = array1

            Dim array2() As Double = {275.0, 50.0, 125.0}
            line_data.start_point = array2

            theUfSession.Curve.CreateLine(line_data, curves_to_proj(0))
            stream.WriteLine("Successful:Curve.CreateLine")
            'stream.WriteLine("curves to project tag = ", curves_to_proj(0))

            theUfSession.Modl.AskFeatFaces(block_tag, face_list)
            stream.WriteLine("Successful:Modl.AskFeatFaces")

            theUfSession.Modl.AskListCount(face_list, num_faces)
            stream.WriteLine("Successful:Modl.AskListCount")

            proj_data.proj_type = 3
            Dim array3() As Double = {0.0, 1.0, 0.0}
            proj_data.proj_vec = array3
            proj_data.multiplicity = 2

            theUfSession.Curve.CreateProjCurves(1, curves_to_proj, face_list.Length, face_list, 3, proj_data, proj_curve_feature)
            stream.WriteLine("Successful:Curve.CreateProjCurves")
            'stream.WriteLine("proj UFCurve feature tag = ", proj_curve_feature)

            theUfSession.Curve.AskProjCurves(proj_curve_feature, num_proj_curves, proj_curves)
            stream.WriteLine("Successful:Curve.AskProjCurves")

            For i As Integer = 0 To num_proj_curves - 1
                theUfSession.Curve.AskProjCurveParents(proj_curves(i), defining_feature, defining_target, defining_curve)
                stream.WriteLine("Successful:Curve.AskProjCurveParents")
                'stream.WriteLine("proj_curves ", i)
                'stream.WriteLine("  belongs to feature tag = ", defining_feature)
                'stream.WriteLine("  was projected onto tag = ", defining_target)
                'stream.WriteLine("  was generated by UFCurve tag = ", defining_curve)
            Next

            theUfSession.Part.Save()

        Catch ex As Exception
            stream.WriteLine("EXCEPTION: ", ex.Message)
            Return 1
        End Try

        Return 0

    End Function

End Module

