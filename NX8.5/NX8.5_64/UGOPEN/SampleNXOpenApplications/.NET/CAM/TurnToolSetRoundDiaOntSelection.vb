'=============================================================================
'
'   Copyright 2009 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION

'     This program will edit a tool selected in the ONT and if it is a turn tool
'     set the round insert button dia to 10mm or 0.5 in.
'
'    This demonstrates setting different values based on part units.
'    This demonstrates an informational message box of the change.
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

        ' If there is a work part only then we can go further
        If WorkPart IsNot Nothing Then

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
            theSession.LogFile.WriteLine("cutterType = " & cutterType)

            'Check if the object is a Turning Tool(Type 3)
            If cutterType = 3 Then

                'Create a turn tool builder so that we can modify its parameters
                Dim turnToolBuilder = WorkPart.CamSetup.CAMGroupCollection.CreateTurnToolBuilder(camObject)

                If turnToolBuilder IsNot Nothing Then

                    'Set the buton diameter for round inserts	
		            If (WorkPart.PartUnits = part.Units.Millimeters) Then
						MessageBox.Show("Tool " & camObject.Name() & " changed Button dia from " & turnToolBuilder.ButtonDiameterBuilder.Value & " to 10 mm")
						turnToolBuilder.ButtonDiameterBuilder.Value = 10.0
		            Else
						MessageBox.Show("Tool " & camObject.Name() & " changed Button dia from " & turnToolBuilder.ButtonDiameterBuilder.Value & " to 0.5 in")
						turnToolBuilder.ButtonDiameterBuilder.Value = 0.5
		            End If

                    'Commit the change
                    turnToolBuilder.Commit()

                    'Destroy the builder when its job is done(cleanup memory)
                    turnToolBuilder.Destroy()

                End If

            End If

        End If

        Return True
    End Function

End Module

















