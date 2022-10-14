' ==================================================================================================
'
'            Copyright (c) 2004 UGS PLM Solutions.
'                   Unpublished - All rights reserved
'
'====================================================================================================
'File description:
'
'Test script EX_DirPath
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

Module EX_DirPath

    Dim theSession As Session
    Dim theUfSession As UFSession

    Public Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_DirPath.log", FileMode.Create, FileAccess.Write)
        Dim stream As New StreamWriter(fs) ' create a stream writer 
        stream.WriteLine("--Log entry goes here--")
        stream.Flush() ' update underlying file

        If File.Exists("EX_DirPath.prt") Then
            stream.WriteLine("Remove EX_DirPath.prt file from <Project Folder>\\bin\\Debug !!")
            stream.WriteLine("EX_DirPath.prt already exists. !!")
            stream.Close()
            Return
        End If

        Dim nError As Integer = Execute(stream, theUfSession)
        stream.WriteLine("End of Log File")
        stream.Close()

    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As NXOpen.UF.UFSession) As Integer

        Dim UFPart As NXOpen.Tag
        Dim part_name As String = "EX_DirPath"
        Dim units As Integer = 2

        theUfSession.Part.[New](part_name, units, UFPart)
        stream.WriteLine("New part: {0} ", part_name, " Created")

        Dim numdir As Integer = 0
        Dim path() As String
        Dim retTag As NXOpen.Tag

        theUfSession.Dirpath.CreateFromEnv("UGII_BASE_DIR", retTag)
        theUfSession.Dirpath.AskDirs(retTag, numdir, path)

        For i As Integer = 0 To numdir - 1
            stream.WriteLine("Dir Path: {0}", path(i))
        Next

        Dim a_path As NXOpen.Tag
        Dim dirs() As String = {"/dir1", "/dir2"}
        theUfSession.Dirpath.CreateFromDirs(2, dirs, a_path)
        theUfSession.Dirpath.AskDirs(a_path, numdir, path)

        For ii As Integer = 0 To numdir - 1
            stream.WriteLine("Dir Path: {0}", path(ii))
        Next

        Dim dirs1() As String = {"/dir3", "/dir4"}
            theUfSession.Dirpath.AppendFromDirs(a_path, 2, dirs1)

        theUfSession.Dirpath.AskDirs(a_path, numdir, path)

        Dim curr_dir As String
        theUfSession.Dirpath.AskCurrDir(a_path, curr_dir)
        stream.WriteLine("Current Dir: {0}" + curr_dir)

        Dim nth_dir As String
        stream.WriteLine("Index" + " Nth Dir")

        For index As Integer = 0 To numdir - 1
            theUfSession.Dirpath.AskNthDir(a_path, index, nth_dir)
            stream.Write(index)
            stream.WriteLine(nth_dir)
        Next
        theUfSession.Part.Save()
        Return 0

    End Function

End Module


