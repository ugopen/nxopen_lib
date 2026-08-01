'=============================================================================
'
'   Copyright 2009 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION

'     This program will rename operations selected in the ONT by replacing
'     one string with another.
'
'     This can be used as a boiler plate to set other tool parameters.
' ============================================================================'=============================================================================
 
Option Strict Off
Imports System
Imports System.IO
Imports System.Windows.Forms
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module RenameCAMops

    Dim theSession As Session
    Dim theUfSession As UFSession
    Dim FindString As String = ""
    Dim ReplaceString As String = ""

    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim WorkPart As Part = theSession.Parts.Work

        Dim setupTag As Tag
        Dim selectedTags() As NXOpen.Tag
        Dim selectedCount As Integer

        ' If there is a work part only then we can go further
        If WorkPart IsNot Nothing Then

            theUfSession.Cam.InitSession()
            theUfSession.Setup.AskSetup(setupTag)

            ' If there is a setup only then we go further
            If setupTag <> 0 Then
                ' Get the selected nodes from the Operation Navigator
                theUfSession.UiOnt.AskSelectedNodes(selectedCount, selectedTags)

                If selectedCount = 0 Then
                    MsgBox("No operations selected.", MsgBoxStyle.Exclamation, "Rename Operations")
                    Exit Sub
                End If

                'Get user input for search and replace text
                'Get the old string
                FindString = InputBox("Find what:", "Rename operations")
                'Abort if no search text was specified.
                If FindString = "" Then
                    MsgBox("Rename operation aborted!", MsgBoxStyle.Exclamation, "Rename Operations")
                    Exit Sub
                End If
                ' All uppercase
                FindString = ucase(FindString)

                ' Get the new string
                ReplaceString = InputBox("Replace '" & FindString & "' with:", "Rename Operations")

                'Write info to info screen
                theSession.ListingWindow.Open()
                theSession.ListingWindow.WriteLine("=================================================================")
                theSession.ListingWindow.WriteLine("Replacing '" & FindString & "' with '" & ReplaceString & "'")
                theSession.ListingWindow.WriteLine("The following Operations were renamed:")
                theSession.ListingWindow.WriteLine("-----------------------------------------------------------------")
                'theSession.ListingWindow.WriteLine(" ")

                Dim ptr As IntPtr = New System.IntPtr
                Dim cycle_cb_fn As UFNcgroup.CycleCbFT = New UFNcgroup.CycleCbFT(AddressOf cycle_cb)

                Dim i As Integer
                'Loop over the selected nodes to take action
                For i = 0 To selectedCount - 1
                    ' The selected item needs to be checked to take action
                    action(selectedTags(i))
                    ' Now if the selected item is a Group object then we need to cycle objects inside it
                    theUfSession.Ncgroup.CycleMembers(selectedTags(i), cycle_cb_fn, ptr)
                Next i
                theSession.ListingWindow.WriteLine("=========================== DONE ================================")
            End If

        End If
    End Sub


    Function cycle_cb(ByVal camObjectTag As Tag, ByVal ptr As IntPtr) As Boolean

        Dim answer As Boolean
        ' Every item needs to be checked to take action
        answer = action(camObjectTag)
        Return answer

    End Function

    Function action(ByVal camObjectTag As Tag) As Boolean

        Dim camObject As NXObject = NXObjectManager.Get(camObjectTag)

        'Check if the object is a Operation
        If TypeOf camObject Is CAM.Operation Then
            'Get the current operation name
            Dim CurrentName As String = camObject.Name()
            'Replace the name section
            Dim NewName As String = Replace(CurrentName, FindString, ReplaceString)
            If NewName <> CurrentName Then
                'theSession.ListingWindow.WriteLine("Renamed: " & CurrentName & " to " & NewName)
                theSession.ListingWindow.WriteLine(CurrentName & "  -->  " & NewName)
                'theSession.ListingWindow.WriteLine(" ")
                'Check if new name does not exceed 30 characters
                Dim Lengte As Integer = NewName.Length
                If Lengte > 30 Then
                    theSession.ListingWindow.WriteLine("*** ERROR *** Operation name more than 30 characters. Operation " & CurrentName & " NOT renamed!")
                    theSession.ListingWindow.WriteLine(" ")
                    GoTo renamed
                End If
                'Rename the current operation
                camObject.SetName(NewName)
            End If
        End If
renamed:
        Return True
    End Function

End Module


















