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

Module EX_Ui_ListingWindow

    Dim theSession As Session
    Dim theUfSession As UFSession
    Dim listingWindow As NXOpen.ListingWindow

    Public Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        listingWindow = theSession.ListingWindow()

        ' Open Listing Window
        listingWindow.Open()
        listingWindow.WriteLine("Log Entry :")
        listingWindow.WriteLine("--Log entry goes here--")

        If (File.Exists("EX_Ui_ListingWindow.prt")) Then
            listingWindow.WriteLine("Remove EX_Ui_ListingWindow.prt file from <Project Folder> !!")
            listingWindow.WriteLine("EX_Ui_ListingWindow.prt already exists. !!")
            Return
        End If

        Dim nError As Integer = Execute()
        If (nError = 0) Then
            listingWindow.WriteLine("Successful")
        Else
            listingWindow.WriteLine("Failed")
        End If

        listingWindow.WriteLine("End of Log File")
    End Sub

    Function Execute() As Integer
        Dim UFPart As Tag
        Dim part_name As String = "EX_Ui_ListingWindow"
        Dim units As Integer = 2
        Dim name As String

        theUfSession.Part.[New](part_name, units, UFPart)
        theUfSession.Part.AskPartName(UFPart, name)
        listingWindow.WriteLine("Loaded: " + name)

        Dim block_orig() As Double = {0.0, 0.0, 0.0}
        Dim block_len() As String = {"1", "2", "3"}
        Dim feature_name As String = ""
        Dim blk_obj As Tag

        theUfSession.Modl.CreateBlock1(FeatureSigns.Nullsign, block_orig, block_len, blk_obj)
        theUfSession.Modl.AskFeatName(blk_obj, feature_name)
        listingWindow.WriteLine("Feature Name is " + feature_name)

        theUfSession.Part.Save()

        Return 0
    End Function
End Module

