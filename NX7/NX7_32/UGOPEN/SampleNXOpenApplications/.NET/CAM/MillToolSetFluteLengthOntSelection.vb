'=============================================================================
'
'   Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION

'     This program will edit a tool selected in the ONT and if it is a mill tool
'     set flute length = tool length.
'
'     This can be used as a boiler plate to set other tool parameters.
' ============================================================================
 
Option Strict Off
Imports System
Imports System.IO
Imports System.Windows.Forms
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module flutelength

    Dim theSession As Session
    Dim theUfSession As UFSession


    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim WorkPart As Part = TheSession.Parts.Work

        Dim setupTag As Tag
        Dim camObjectTag As Tag
        Dim selectedTags() As NXOpen.Tag
        Dim selectedCount As Integer

        theUfSession.Cam.InitSession()
        theUfSession.Setup.AskSetup(setupTag)

        ' If there is a setup only then we go further
        If setupTag <> 0 Then

            ' Get the selected nodes from the Operation Navigator
            theUfSession.UiOnt.AskSelectedNodes(selectedCount, selectedTags)

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
        Dim WorkPart As Part = TheSession.Parts.Work

        'Check if the object is a Tool
        If TypeOf camObject Is CAM.Tool Then

            Dim cutterType As Integer
            Dim cutterSubtype As Integer
            theUFSession.Cutter.AskTypeAndSubtype(camObjectTag, cutterType, cutterSubtype)

            'Check if the object is a Mill Tool(Type 1 is Mill)
            If cutterType = 1 Then

                'Create a mill tool builder so that we can modify its parameters
                Dim millToolBuilder = WorkPart.CamSetup.CAMGroupCollection.CreateMillToolBuilder(camObject)

                If millToolBuilder IsNot Nothing Then

                    'Informational messge box
                    MessageBox.Show("Tool is " & camObject.Name() & " Flute length was " & millToolBuilder.TlFluteLnBuilder.Value & " and is now set to " & millToolBuilder.TlHeightBuilder.Value)

                    'Set the Flute length to the Tool Length
                    millToolBuilder.TlFluteLnBuilder.Value = millToolBuilder.TlHeightBuilder.Value

                    'Commit the change
                    millToolBuilder.Commit()

                    'Destroy the builder when its job is done(cleanup memory)
                    millToolBuilder.Destroy()

                End If

            End If

        End If

        Return True
    End Function

End Module

















