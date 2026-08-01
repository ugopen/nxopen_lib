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

Module EX_Modl_CreateBlend

    Dim theSession As Session
    Dim theUfSession As UFSession

    Public Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_Modl_CreateBlend.log", FileMode.Create, FileAccess.Write)
        Dim stream As New StreamWriter(fs) ' create a stream writer 
        stream.WriteLine("--Log entry goes here--")
        stream.Flush() ' update underlying file

        If File.Exists("EX_Modl_CreateBlend.prt") Then
            stream.WriteLine("Remove EX_Modl_CreateBlend.prt file from <Project Folder>\\bin\\Debug !!")
            stream.WriteLine("EX_Modl_CreateBlend.prt already exists. !!")
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
            Dim part_name As String = "EX_Modl_CreateBlend"
            Dim units As Integer = 2
            Dim name As String
            Dim retcod As Integer
            Dim faceted_model As NXOpen.Tag

            theUfSession.Part.[New](part_name, units, UFPart)
            stream.WriteLine("New part : ", part_name, " Created")


            Dim block_tag As NXOpen.Tag
            Dim list1() As NXOpen.Tag
            Dim corner_point(3) As Double
            Dim edge_lengths() As String = {"1.0", "2.0", "3.0"}
            Dim block_feature_tag As NXOpen.Tag
            Dim faceting_params As UFFacet.Parameters = New UFFacet.Parameters
            Dim ecount As Integer
            Dim blend1 As NXOpen.Tag
            Dim list2() As NXOpen.Tag
            Dim pt1() As Double = {0.0, 0.0, 0.0}
            Dim pt2() As Double = {0.0, 0.0, 0.0}

            Dim allow_smooth As Integer = 0
            Dim allow_cliff As Integer = 0
            Dim allow_notch As Integer = 0
            Dim vrb_tol As Double = 0.0

            'First create a UFPart in which we will initially create a block.

            theUfSession.Assem.SetWorkPart(UFPart)
            stream.WriteLine("Successful:Assem.SetWorkPart")

            corner_point(0) = 0.0
            corner_point(1) = 0.0
            corner_point(2) = 0.0

            theUfSession.Modl.CreateBlock1(FeatureSigns.Nullsign, corner_point, edge_lengths, block_feature_tag)
            stream.WriteLine("Successful:Modl.CreateBlock1")

            theUfSession.Modl.AskFeatBody(block_feature_tag, block_tag)
            stream.WriteLine("Successful:AskFeatBody")

            'Get the edges of the body.  Get the count of the edge list.
            'This will be used to get the four 'vertical' corners of the block for
            'blending. Check return codes.

            theUfSession.Modl.AskBodyEdges(block_tag, list1)
            stream.WriteLine("Successful:Modl.AskBodyEdges")

            theUfSession.Modl.AskListCount(list1, ecount)
            stream.WriteLine("Successful:Modl.AskListCount")


            Dim arr_list2 As System.Collections.ArrayList = New System.Collections.ArrayList
            For i As Integer = 0 To ecount - 1
                Dim edge As NXOpen.Tag            ' edge object 
                Dim vcount As Integer             'count of vertices in edge 
                ' Get the edge (list item) and check return code.  
                theUfSession.Modl.AskListItem(list1, i, edge)
                stream.WriteLine("Successful:Modl.AskListItem")

                'Get the edge vertices.  Check return code.  
                theUfSession.Modl.AskEdgeVerts(edge, pt1, pt2, vcount)
                stream.WriteLine("Successful:Modl.AskEdgeVerts")

                If (System.Math.Abs(System.Math.Abs(pt1(2) - pt2(2)) - 3.0) < 0.001) Then
                    arr_list2.Add(edge)
                End If
            Next
            Dim t As System.Type
            t = GetType(NXOpen.Tag)
            list2 = arr_list2.ToArray(t)

            theUfSession.Modl.CreateBlend("0.009246", list2, allow_smooth, allow_cliff, allow_notch, vrb_tol, blend1)
            stream.WriteLine("Successful:Modl.CreateBlend")

            'Save the Part
            theUfSession.Part.Save()
        Catch ex As Exception
            stream.WriteLine("EXCEPTION: ", ex.Message)
            Return 1
        End Try
        Return 0

    End Function

End Module


