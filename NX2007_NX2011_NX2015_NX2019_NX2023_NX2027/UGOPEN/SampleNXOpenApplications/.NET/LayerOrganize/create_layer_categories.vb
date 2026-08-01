' NX 3.0.0.14
' Journal created by vlucas on Fri Apr 30 14:12:41 2004 Eastern Daylight Time
Option Strict Off
Imports System
Imports NXOpen

Module NXJournal

    Function CategoryExists(ByVal theSession As Session, ByVal categoryName As String) As Boolean
        Try
            Return Not theSession.Parts.Work.LayerCategories.FindObject(categoryName) Is Nothing
        Catch ex As Exception
            Return False
        End Try

    End Function

    Sub Main()

        Dim theSession As Session = Session.GetSession()
        ' ----------------------------------------------
        '   Menu: Format->Layer Settings...
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------

        If Not CategoryExists(theSession, "SOLIDS") Then

            Dim integerArray1(9) As Integer
            integerArray1(0) = 30
            integerArray1(1) = 31
            integerArray1(2) = 32
            integerArray1(3) = 33
            integerArray1(4) = 34
            integerArray1(5) = 35
            integerArray1(6) = 36
            integerArray1(7) = 37
            integerArray1(8) = 38
            integerArray1(9) = 39
            Dim layerCategory1 As Layer.Category
            layerCategory1 = theSession.Parts.Work.LayerCategories.CreateCategory("SOLIDS", "", integerArray1)

        End If

        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        If Not CategoryExists(theSession, "SKETCHES") Then

            Dim integerArray2(9) As Integer
            integerArray2(0) = 40
            integerArray2(1) = 41
            integerArray2(2) = 42
            integerArray2(3) = 43
            integerArray2(4) = 44
            integerArray2(5) = 45
            integerArray2(6) = 46
            integerArray2(7) = 47
            integerArray2(8) = 48
            integerArray2(9) = 49
            Dim layerCategory2 As Layer.Category
            layerCategory2 = theSession.Parts.Work.LayerCategories.CreateCategory("SKETCHES", "", integerArray2)

        End If
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        If Not CategoryExists(theSession, "CURVES") Then

            Dim integerArray3(9) As Integer
            integerArray3(0) = 50
            integerArray3(1) = 51
            integerArray3(2) = 52
            integerArray3(3) = 53
            integerArray3(4) = 54
            integerArray3(5) = 55
            integerArray3(6) = 56
            integerArray3(7) = 57
            integerArray3(8) = 58
            integerArray3(9) = 59
            Dim layerCategory3 As Layer.Category
            layerCategory3 = theSession.Parts.Work.LayerCategories.CreateCategory("CURVES", "", integerArray3)

        End If
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        If Not CategoryExists(theSession, "REFGEOMS") Then

            Dim integerArray4(9) As Integer
            integerArray4(0) = 60
            integerArray4(1) = 61
            integerArray4(2) = 62
            integerArray4(3) = 63
            integerArray4(4) = 64
            integerArray4(5) = 65
            integerArray4(6) = 66
            integerArray4(7) = 67
            integerArray4(8) = 68
            integerArray4(9) = 69
            Dim layerCategory4 As Layer.Category
            layerCategory4 = theSession.Parts.Work.LayerCategories.CreateCategory("REFGEOMS", "", integerArray4)

        End If
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        If Not CategoryExists(theSession, "DRAFTINGOBJS") Then

            Dim integerArray5(9) As Integer
            integerArray5(0) = 70
            integerArray5(1) = 71
            integerArray5(2) = 72
            integerArray5(3) = 73
            integerArray5(4) = 74
            integerArray5(5) = 75
            integerArray5(6) = 76
            integerArray5(7) = 77
            integerArray5(8) = 78
            integerArray5(9) = 79
            Dim layerCategory5 As Layer.Category
            layerCategory5 = theSession.Parts.Work.LayerCategories.CreateCategory("DRAFTINGOBJS", "", integerArray5)

        End If
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        If Not CategoryExists(theSession, "MANUFACTURING") Then

            Dim integerArray6(19) As Integer
            integerArray6(0) = 80
            integerArray6(1) = 81
            integerArray6(2) = 82
            integerArray6(3) = 83
            integerArray6(4) = 84
            integerArray6(5) = 85
            integerArray6(6) = 86
            integerArray6(7) = 87
            integerArray6(8) = 88
            integerArray6(9) = 89
            integerArray6(10) = 90
            integerArray6(11) = 91
            integerArray6(12) = 92
            integerArray6(13) = 93
            integerArray6(14) = 94
            integerArray6(15) = 95
            integerArray6(16) = 96
            integerArray6(17) = 97
            integerArray6(18) = 98
            integerArray6(19) = 99
            Dim layerCategory6 As Layer.Category
            layerCategory6 = theSession.Parts.Work.LayerCategories.CreateCategory("MANUFACTURING", "", integerArray6)

        End If
        ' ----------------------------------------------
        '   Dialog Begin Layer Category
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Layer Settings
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Menu: Tools->Journal->Stop
        ' ----------------------------------------------

    End Sub
End Module
