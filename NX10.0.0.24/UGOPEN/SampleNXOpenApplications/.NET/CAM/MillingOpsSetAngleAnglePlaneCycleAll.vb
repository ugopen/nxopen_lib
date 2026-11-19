'=============================================================================
'
'   Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION

'     This program will cycle through all the operations in the part and
'     sets the open area engage to angle, angle, plane if a plane named "TEST" is found.
'
'     This demonstrates:
'          Building different NCM builders for different operation types
'          Setting NCM only if a named plane is found.
'          Using a named plane "TEST" in the engage definition
'
'     This can be used as a boiler plate to set other non cutting moves.
' ============================================================================
 
Option Strict Off
Imports System
Imports System.IO
Imports System.Windows.Forms
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities
Imports NXOpen.UFUi

Module NcmParams

    Dim theSession As Session
    Dim theUfSession As UFSession

    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim WorkPart As Part = theSession.Parts.Work

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

    'This is the function that is called on every object encountered in the cycling
    Function cycle_cb(ByVal camObjectTag As Tag, ByVal ptr As IntPtr) As Boolean

        Dim camObject As NXObject = NXObjectManager.Get(camObjectTag)
        Dim WorkPart As Part = TheSession.Parts.Work
        Dim operationBuilder As CAM.OperationBuilder

        Dim answer As Boolean

        ' If the object is not an operation then leave without doing anything more
        theUfSession.Ncgroup.IsGroup(camObjectTag, answer)
        If answer = True Then
            Return True
        End If

        'If it is an operation then get the proper operation builder
        operationBuilder = GetOperationBuilder(camObjectTag)

        'Now set the NCM parameters
        SetNcmParameters(operationBuilder)

        'Destroy the builder when its job is done(cleanup memory)
        If operationBuilder IsNot Nothing Then
            'Save the changes made
            operationBuilder.Commit()
            'Clean up memory
            operationBuilder.Destroy()
        End If

        Return True
    End Function

    'Function to get the operation builder
    Function GetOperationBuilder(ByVal camObjectTag As Tag) As CAM.OperationBuilder

        Dim camObject As NXObject = NXObjectManager.Get(camObjectTag)
        Dim WorkPart As Part = theSession.Parts.Work
        Dim operationBuilder As CAM.OperationBuilder

        operationBuilder = Nothing

        'Check if the object is an Operation
        If TypeOf camObject Is CAM.Operation Then
            Dim operationType As Integer
            Dim operationSubtype As Integer

            'Get the type and subtype of the operation
            theUFSession.Obj.AskTypeAndSubtype(camObjectTag, operationType, operationSubtype)

            If operationSubtype = 110 Then             ' This is a Planar Milling Operation so create a Planar Milling Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreatePlanarMillingBuilder(camObject)
            ElseIf operationSubtype = 260 Then         ' This is a Cavity Milling Operation so create a Cavity Milling Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateCavityMillingBuilder(camObject)
            ElseIf operationSubtype = 261 Then         ' This is a Face Milling Operation so create a Face Milling Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateFaceMillingBuilder(camObject)
            ElseIf operationSubtype = 263 Then         ' This is a Z Level Milling Operation so create a Z Level Milling Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateZLevelMillingBuilder(camObject)
            ElseIf operationSubtype = 266 Then         ' This is a Variable Axis Z Level Milling Operation so create a Variable Axis Z Level Milling Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateVazlMillingBuilder(camObject)
            ElseIf operationSubtype = 210 Then         ' This is a Fixed Axis Surface Contour Operation so create a Surface Contour Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateSurfaceContourBuilder(camObject)
            ElseIf operationSubtype = 211 Then         ' This is a Variable Axis Surface Contour Operation so create Surface Contour Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateSurfaceContourBuilder(camObject)
            End If

        End If

        Return operationBuilder
    End Function


    Function SetNcmParameters(ByRef operationBuilder As CAM.OperationBuilder)

        Dim WorkPart As Part = theSession.Parts.Work
        Dim planeToUse As Xform

        For Each aPlane As Plane In theSession.Parts.BaseWork.Planes()
            If aPlane.Name = "TEST" Then
                ' The planes specified in CAM are Xform objects and so we are taking a Plane object
                ' and creating a Xform for it.
                planeToUse = theSession.Parts.Work.Xforms.CreateXform(aPlane, SmartObject.UpdateOption.AfterModeling)
            End If
        Next

        ' Check if there is a valid Builder
        If operationBuilder IsNot Nothing Then
            Dim ncmParams As CAM.NcmSubopBuilder

            'From the Operation Builder get the Non Cutting Moves Builder
            Dim planarOperationBuilder As CAM.PlanarOperationBuilder
            Dim surfaceContourBuilder As CAM.SurfaceContourBuilder

            If TypeOf operationBuilder Is CAM.PlanarOperationBuilder Then
                planarOperationBuilder = operationBuilder
                ncmParams = planarOperationBuilder.NonCuttingBuilder
            End If

            If TypeOf operationBuilder Is CAM.SurfaceContourBuilder Then
                surfaceContourBuilder = operationBuilder
                ncmParams = surfaceContourBuilder.NonCuttingBuilder
            End If

            ' Because the Non Cutting Object can be different for 
            '   Planar Operations           -   NcmPlanarBuilder
            '   Surface Contour Operations  -   NcmScBuilder
            ' we need to check which one it is before asking for data
            If TypeOf ncmParams Is CAM.NcmPlanarBuilder Then

                Dim planarNcm As CAM.NcmPlanarBuilder
                ' Because we know that the builder is a Planar Non Cutting object we will 
                ' set it to be that kind of object
                planarNcm = ncmParams

                'We have found a plane that we want to use
                If planeToUse IsNot Nothing Then
                    ' As an example the Open Area Engage is set to be Angle Angle Plane and the values are set to 
                    ' some arbitrary values.
                    planarNcm.EngageOpenAreaBuilder().EngRetType = NcmPlanarEngRetBuilder.EngRetTypes.AngAngPlane
                    planarNcm.EngageOpenAreaBuilder().SwingAngle = 30
                    planarNcm.EngageOpenAreaBuilder().RampAngle = 30
                    planarNcm.EngageOpenAreaBuilder().Plane = planeToUse
                End If

            End If

        End If

    End Function
End Module























