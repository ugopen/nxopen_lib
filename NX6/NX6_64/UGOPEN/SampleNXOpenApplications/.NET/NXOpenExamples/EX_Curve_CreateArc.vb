' ==================================================================================================
'
'            Copyright (c) 2004 UGS PLM Solutions.
'                   Unpublished - All rights reserved
'
'====================================================================================================
'File description:
'Example to show how to create Arc using UF .NET Wrappers: uf_curve_CreateArc
' 
Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.UF
Imports NXOpen.Utilities



Module EX_Curve_CreateArc

    Dim testName As String = "EX_Curve_CreateArc"

    Dim theSession As Session
    Dim theUfSession As UFSession

    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim stream As StreamWriter = New StreamWriter(testName + ".log")
        Dim prtFileName As String = New String(testName + ".prt")
        Dim prtFile As FileInfo = New FileInfo(prtFileName)
        prtFile = New FileInfo(prtFileName)
        stream.WriteLine("Log Entry : ")
        stream.WriteLine("--Log entry goes here--")

        If prtFile.Exists() Then
            stream.WriteLine("Remove " + prtFileName + " EX_Curve_CreateArc.prt file from <Project Folder> !!")
            stream.WriteLine(prtFileName + " already exists. !!")
            stream.WriteLine("End of Log File")
            stream.Close()
            Return
        End If

        Dim nError As Integer = Execute(stream, theUfSession)
        stream.WriteLine("End of Log File")
        stream.Close()

    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As UFSession) As Integer
        Dim PartTag As Tag
        Dim units As Integer = UFConstants.ENGLISH
        Dim PartName As String

        theUfSession.Part.[New](testName, units, PartTag)
        theUfSession.Part.AskPartName(PartTag, PartName)
        stream.WriteLine("New Part File Created :- " + PartName)

        Dim arc, wcs As Tag
        Dim arc_coords As UFCurve.Arc = New UFCurve.Arc

        'Fill out the data structure */
        arc_coords.start_angle = 0.0
        arc_coords.end_angle = 3.0
        Dim array() As Double = {0.0, 0.0, 1.0}
        arc_coords.arc_center = array
        'arc_coords.arc_center(0) = 0.0
        'arc_coords.arc_center(1) = 0.0
        'arc_coords.arc_center(2) = 1.0
        arc_coords.radius = 2.0

        stream.WriteLine("Creating Arc:-")
        theUfSession.Csys.AskWcs(wcs)
        theUfSession.Csys.AskMatrixOfObject(wcs, arc_coords.matrix_tag)
        theUfSession.Curve.CreateArc(arc_coords, arc)
        stream.WriteLine("Successful")

        stream.WriteLine("Querying Arc:-")
        Dim created_arc_coords As UFCurve.Arc = New UFCurve.Arc
        theUfSession.Curve.AskArcData(arc, created_arc_coords)
        stream.Write("arc_center= {")
        stream.Write(created_arc_coords.arc_center(0).ToString())
        stream.Write(",")
        stream.Write(created_arc_coords.arc_center(1).ToString())
        stream.Write(",")
        stream.Write(created_arc_coords.arc_center(2).ToString())
        stream.WriteLine("}")

        stream.WriteLine("start_angle= " + created_arc_coords.start_angle.ToString)
        stream.WriteLine("end_angle= " + created_arc_coords.end_angle.ToString)
        stream.WriteLine("radius= " + created_arc_coords.radius.ToString)

        'Save the Part
        theUfSession.Part.Save()
        Return 0

    End Function

    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = UFConstants.UF_UNLOAD_IMMEDIATELY
    End Function

End Module
