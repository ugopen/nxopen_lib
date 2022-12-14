'=============================================================================
'
'   Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION

'     This program will cycle through all the planar type operations in the part and
'     set some corner parameters in the cutting dialog. The detailed steps:
'          Ask current smoothing option
'          Turn on smoothing
'          Set Radius = 50 %Tool
'          Set Stepover limit = 150%
'          Retore previous smoothing option
'
'     This can be used as a boiler plate to set other cutting parameters.
' ============================================================================
 
Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module CutParams

    Dim theSession As Session
    Dim theUfSession As UFSession


    Sub Main()

        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim WorkPart As Part = TheSession.Parts.Work

        Dim setupTag As Tag
        Dim camObjectTag As Tag
        Dim programRootTag As Tag

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

            Dim operationBuilder As CAM.MillOperationBuilder

            If operationSubtype = 110 Then             ' This is a Planar Milling Operation so create a Planar Milling Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreatePlanarMillingBuilder(camObject)
            ElseIf operationSubtype = 260 Then         ' This is a Cavity Milling Operation so create a Cavity Milling Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateCavityMillingBuilder(camObject)
            ElseIf operationSubtype = 261 Then         ' This is a Face Milling Operation so create a Face Milling Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateFaceMillingBuilder(camObject)
            ElseIf operationSubtype = 263 Then         ' This is a Z Level Milling Operation so create a Z Level Milling Builder
                operationBuilder = WorkPart.CamSetup.CAMOperationCollection.CreateZLevelMillingBuilder(camObject)
            End If

            ' Check if there is a valid Builder
            If operationBuilder IsNot Nothing Then

                ' Get the current smoothing option
                Dim SmoothingOptions As Integer = operationBuilder.CutParameters.CornerControl.SmoothingOption

                ' Set the smoothing option to all passes, and set the parameters
                operationBuilder.CutParameters.CornerControl.SmoothingOption = CAM.CornerControlBuilder.SmoothingOptions.AllPasses
                operationBuilder.CutParameters.CornerControl.FilletingRadius.Value = 50.0
                operationBuilder.CutParameters.CornerControl.FilletingRadius.Intent = CAM.ParamValueIntent.ToolDep
                operationBuilder.CutParameters.StepoverLimit.Value = 150.0

                'Commit the change to the operation( this is the equivalent of OK'ing the operation dialog )
                operationBuilder.Commit()

                ' Set the smoothing option back to the original setting
                operationBuilder.CutParameters.CornerControl.SmoothingOption = SmoothingOptions

                'Commit the change to the operation( this is the equivalent of OK'ing the operation dialog )
                operationBuilder.Commit()

                'Destroy the builder its job is done(cleanup memory)
                operationBuilder.Destroy()

            End If

        End If

        Return True
    End Function

End Module



















