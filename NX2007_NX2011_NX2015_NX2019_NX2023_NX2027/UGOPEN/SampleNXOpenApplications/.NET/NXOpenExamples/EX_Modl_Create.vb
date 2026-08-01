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

Module EX_Modl_Create

    Dim theSession As Session
    Dim theUfSession As UFSession

    Public Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_Modl_Create.log", FileMode.Create, FileAccess.Write)
        Dim stream As New StreamWriter(fs) ' create a stream writer 
        stream.WriteLine("--Log entry goes here--")
        stream.Flush() ' update underlying file

        If File.Exists("EX_Modl_Create.prt") Then
            stream.WriteLine("Remove EX_Modl_Create.prt file from <Project Folder>\\bin\\Debug !!")
            stream.WriteLine("EX_Modl_Create.prt already exists. !!")
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
            Dim part_name As String = "EX_Modl_Create"
            Dim units As Integer = 2

            theUfSession.Part.[New](part_name, units, UFPart)
            stream.WriteLine("New part : {0} ", part_name, " Created")

            Dim count, Type, norm_dir As Integer

            Dim cyl_obj_id, Face, feature_id, Body As NXOpen.Tag
            Dim face_id As NXOpen.Tag = NXOpen.Tag.Null

            Dim face_list() As NXOpen.Tag
            Dim origin() As Double = {0.0, 0.0, 0.0}
            Dim direction() As Double = {0.0, 0.0, 1.0}
            Dim center(3) As Double
            Dim dir(3) As Double
            Dim box(6) As Double
            Dim radius, rad_data As Double
            Dim location() As Double = {0.0, 0.0, 2.0}
            Dim height As String = "4.0"
            Dim diam As String = "2.0"
            Dim gr_diam As String = "1.0"
            Dim width As String = "1.0"

            theUfSession.Modl.CreateList(face_list)
            stream.WriteLine("Successful:Modl.CreateList")

            theUfSession.Modl.CreateCyl1(FeatureSigns.Nullsign, origin, height, diam, direction, cyl_obj_id)
            stream.WriteLine("Successful:Modl.CreateCyl1")

            theUfSession.Modl.AskFeatBody(cyl_obj_id, Body)
            stream.WriteLine("Successful:Modl.AskFeatBody")
            stream.WriteLine("Body is : {0}", Body)

            theUfSession.Modl.AskBodyFaces(Body, face_list)
            stream.WriteLine("Successful:Modl.AskBodyFaces")
            stream.WriteLine("Face_list is : {0}", face_list)

            theUfSession.Modl.AskListCount(face_list, count)
            stream.WriteLine("Successful:Modl.AskListCount")
            stream.WriteLine("Count is: {0}", count)

            For l As Integer = 0 To count - 1
                theUfSession.Modl.AskListItem(face_list, l, Face)
                stream.WriteLine("face is : {0}", Face)
                theUfSession.Modl.AskFaceData(Face, Type, center, dir, box, radius, rad_data, norm_dir)
                stream.WriteLine("face data is: {0},{1},{2}", radius, rad_data, norm_dir)
                If (Type = UFConstants.UF_cylinder_type) Then
                    face_id = Face
                End If
            Next

            theUfSession.Modl.CreateRectGroove(location, direction, gr_diam, width, face_id, feature_id)
            stream.WriteLine("Successful:Modl.CreateRectGroove")

            'Save the Part
            theUfSession.Part.Save()
        Catch ex As Exception
            stream.WriteLine("EXCEPTION: ", ex.Message)
            Return 1
        End Try
        Return 0
       
    End Function

End Module


