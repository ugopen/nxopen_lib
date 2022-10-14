'=============================================================================
'
'   Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION

'     This program will cycle through all the planar type operations in the part and
'     set the Minimum Clearance Value of the Closed Engage to zero part units.
'
'     This can be used as a boiler plate to set other NCM parameters.
' ============================================================================
        ' 
Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module NCMParams

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

            Dim planarOperationBuilder As CAM.PlanarOperationBuilder

            If operationSubtype = 110 Then             ' This is a Planar Milling Operation so create a Planar Milling Builder
                planarOperationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreatePlanarMillingBuilder(camObject)
            ElseIf operationSubtype = 260 Then         ' This is a Cavity Milling Operation so create a Cavity Milling Builder
                planarOperationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateCavityMillingBuilder(camObject)
            ElseIf operationSubtype = 261 Then         ' This is a Face Milling Operation so create a Face Milling Builder
                planarOperationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateFaceMillingBuilder(camObject)
            ElseIf operationSubtype = 263 Then         ' This is a Z Level Milling Operation so create a Z Level Milling Builder
                planarOperationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateZLevelMillingBuilder(camObject)
            ElseIf operationSubtype = 266 Then         ' This is a Variable Axis Z Level Milling Operation so create a Variable Axis Z Level Milling Builder
                planarOperationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateVazlMillingBuilder(camObject)
            End If

            ' Check if there is a valid Builder
            If planarOperationBuilder IsNot Nothing Then

                Dim ncmBuilder As CAM.NcmPlanarBuilder

                'From the Operation Builder get the Non Cutting Builder
                ncmBuilder = planarOperationBuilder.NonCuttingBuilder

                ' Because the operations we are interested in all belong to the Planar Operation family
                ' the NCM Builder should be a NcmPlanr Builder
                ' Check to make sure that is the case
                If TypeOf ncmBuilder Is CAM.NcmPlanarBuilder Then

                    'Set the Minimum Clearance Value of the Closed Engage to zero
                    ncmBuilder.EngageClosedAreaBuilder.MinClearanceBuilder.Value = 0.0

                    'Also make sure that the intent is set to PartUnits rather than % Tool Diameter
                    ncmBuilder.EngageClosedAreaBuilder.MinClearanceBuilder.Intent = CAM.ParamValueIntent.PartUnits

                    'Commit the change to the operation( this is the equivalent of OK'ing the operation dialog )
                    planarOperationBuilder.Commit()

                End If

                'Destroy the builder when its job is done(cleanup memory)
                planarOperationBuilder.Destroy()

            End If

        End If

        Return True
    End Function

End Module


















