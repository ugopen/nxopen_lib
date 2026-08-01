'=============================================================================
'
'   Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION

        ' This program will cycle through all the holemaking operations in the part and
        ' turn on collision checking.
'
'     This can be used as a boiler plate to set other holemaking parameters.
' ============================================================================

Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module HoleMakingOperation

    Dim theSession As Session
    Dim theUfSession As UFSession

    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim WorkPart As Part = TheSession.Parts.Work

        Dim setupTag As Tag
        Dim camObjectTag As Tag
        Dim programRootTag As Tag

        ' If there is a work part only then we can go further
        If WorkPart IsNot Nothing Then

            theUfSession.Cam.InitSession()
            theUfSession.Setup.AskSetup(setupTag)

            ' If there is a setup only then we go further
            If setupTag <> 0 Then

                Dim ptr As IntPtr = New System.IntPtr
                Dim cycle_cb_fn As UFNcgroup.CycleCbFT = New UFNcgroup.CycleCbFT(AddressOf cycle_cb)

                ' Get the Program View's Root
                theUfSession.Setup.AskProgramRoot(setupTag, programRootTag)

                If programRootTag <> 0 Then
                    'Cycle throught the Program and find every object 
                    theUfSession.Ncgroup.CycleMembers(programRootTag, cycle_cb_fn, ptr)
                End If

            End If

        End If
    End Sub

    'This is the fucntion that is called on every object encountered in the cycling
    Function cycle_cb(ByVal camObjectTag As Tag, ByVal ptr As IntPtr) As Boolean

        Dim camObject As NXObject = NXObjectManager.Get(camObjectTag)
        Dim WorkPart As Part = TheSession.Parts.Work

        'Check if the object is an Operation
        If TypeOf camObject Is CAM.Operation Then
            Dim operationType As Integer
            Dim operationSubtype As Integer

            'Get the type and subtype of the operation
            theUFSession.Obj.AskTypeAndSubtype(camObjectTag, operationType, operationSubtype)

            Dim operationBuilder As CAM.HoleMakingBuilder
            If operationSubtype = 600 Then         ' This is a Holemaking Operation so create a Holemaking Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateHoleMakingBuilder(camObject)
            End If

            ' Check if there is a valid Builder
            If operationBuilder IsNot Nothing Then

                ' Turn on collision checking
                operationBuilder.CutParameters.CheckIpwCollisions = True

                'Commit the change to the operation( this is the equivalent of OK'ing the operation dialog )
                operationBuilder.Commit()

                'Destroy the builder when its job is done(cleanup memory)
                operationBuilder.Destroy()

            End If

        End If

        Return True
    End Function

End Module


















