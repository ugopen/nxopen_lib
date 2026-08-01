'=============================================================================
'
'   Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION

'     This program is called from the wizard  demo_MillToolSetFluteLengthWizdObject.xml
'     to show how a wizard can create an object, and call an API program to modify it.
'
'     This program will edit a tool that the wizard creates, and if it is a mill tool
'     set flute length = tool length.
'
'     This can be used as a boiler plate to set other tool parameters.
' ============================================================================
        ' 
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

        ' If there is a work part only then we can go further
        If WorkPart IsNot Nothing Then

            Dim camObjectTag As Tag

            ' If there is a setup only then we go further
            theUFSession.Cam.WizardAskCurrentObject(camObjectTag)
            If camObjectTag <> 0 Then
                action(camObjectTag)
            End If

        End If
    End Sub

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

















