'=============================================================================
'
'   Copyright 2009 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
'
'=============================================================================
' 
' ===========================================================================
'   DESCRIPTION

'     This program is a bioler plate for editing operations selected in the Operation Navigator.
'     It must be copied and modified to suit.
'
' ============================================================================
Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.CAM
Imports NXOpen.UF
Imports NXOpen.Utilities

Module OntSelectionBoilerPlate

    Dim theSession As Session
    Dim theUfSession As UFSession


    Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()
        Dim WorkPart As Part = theSession.Parts.Work

        ' If there is a work part only then we can go further
        If WorkPart IsNot Nothing Then

            ' If there is a setup only then do we have to go further
            If WorkPart.CAMSetup() IsNot Nothing Then

                'If Cam Session is not initialized then we have to create a session
                If theSession.IsCamSessionInitialized() = False Then
                    theSession.CreateCamSession()
                End If

                Dim selectedTags() As NXOpen.Tag
                Dim selectedCount As Integer = 0

                ' Get the selected nodes from the Operation Navigator
                theUfSession.UiOnt.AskSelectedNodes(selectedCount, selectedTags)

                Dim index As Integer = 0

                Dim answer As Boolean = False
                Dim ptr As IntPtr = New System.IntPtr
                Dim cycleCbFn As UFNcgroup.CycleCbFT = New UFNcgroup.CycleCbFT(AddressOf cycleCb)

                If selectedCount <> 0 Then
                    'Cycle all the selected objects and take required action
                    While index < selectedCount
                        ' If the object is a group then cycle through the group
                        theUfSession.Ncgroup.IsGroup(selectedTags(index), answer)
                        If answer = True Then
                            'Cycle throught the Program and find every object 
                            theUfSession.Ncgroup.CycleMembers(selectedTags(index), cycleCbFn, ptr)
                        Else
                            'Take action on the operation
                            OperationAction(selectedTags(index))
                        End If

                        ' Increment to the next object
                        index = index + 1

                    End While
                Else
                    ' Find the Program root and perform the actions on all obects in the part
                    Dim programRoot As Tag = Tag.Null
                    theUfSession.Setup.AskProgramRoot(WorkPart.CAMSetup().Tag, programRoot)
                    'Cycle throught the Program and find every object 
                    theUfSession.Ncgroup.CycleMembers(programRoot, cycleCbFn, ptr)
                End If
            End If
        End If
    End Sub

    'This is the function that is called on every object encountered in the cycling
    Function cycleCb(ByVal camObjectTag As Tag, ByVal ptr As IntPtr) As Boolean
        Dim answer As Boolean

        ' If the object is not an operation then leave without doing anything more
        theUfSession.Ncgroup.IsGroup(camObjectTag, answer)
        If answer = True Then
            Return True
        End If

        'If it is an operation then take the action
        OperationAction(camObjectTag)
        Return True

    End Function

    'This is the Funciton in which the Action is taken for an operation
    Function OperationAction(ByVal camObjectTag As Tag) As Boolean
        ' Find the object associated with the Tag
        Dim camObject As NXObject = NXObjectManager.Get(camObjectTag)
        Dim WorkPart As Part = theSession.Parts.Work
        Dim operationBuilder As CAM.OperationBuilder
        Dim response As Boolean = True

        'If it is an operation then get the proper operation builder
        operationBuilder = GetOperationBuilder(camObjectTag)

        'Now set the variables on the operation builder
        response = ActionFunction(camObject, operationBuilder)

        'Destroy the builder its job is done(cleanup memory)
        'Clean up memory
        If operationBuilder IsNot Nothing Then
            operationBuilder.Destroy()
        End If

        Return response
    End Function

    'Function to get the operation builder
    Function GetOperationBuilder(ByVal camObjectTag As Tag) As CAM.OperationBuilder
        Dim camObject As NXObject = NXObjectManager.Get(camObjectTag)
        Dim WorkPart As Part = theSession.Parts.Work
        Dim operationBuilder As CAM.OperationBuilder = Nothing

        operationBuilder = Nothing

        'Check if the object is an Operation
        If TypeOf camObject Is CAM.Operation Then
            Dim operationType As Integer
            Dim operationSubtype As Integer

            'Get the type and subtype of the operation
            theUfSession.Obj.AskTypeAndSubtype(camObjectTag, operationType, operationSubtype)

            If operationSubtype = 110 Then             ' This is a Planar Milling Operation so create a Planar Milling Builder
                operationBuilder = WorkPart.CAMSetup.CAMOperationCollection.CreatePlanarMillingBuilder(camObject)
            ElseIf operationSubtype = 260 Then         ' This is a Cavity Milling Operation so create a Cavity Milling Builder
                operationBuilder = WorkPart.CAMSetup.CAMOperationCollection.CreateCavityMillingBuilder(camObject)
            ElseIf operationSubtype = 261 Then         ' This is a Face Milling Operation so create a Face Milling Builder
                operationBuilder = WorkPart.CAMSetup.CAMOperationCollection.CreateFaceMillingBuilder(camObject)
            ElseIf operationSubtype = 263 Then         ' This is a Z Level Milling Operation so create a Z Level Milling Builder
                operationBuilder = WorkPart.CAMSetup.CAMOperationCollection.CreateZlevelMillingBuilder(camObject)
            ElseIf operationSubtype = 266 Then         ' This is a Variable Axis Z Level Milling Operation so create a Variable Axis Z Level Milling Builder
                operationBuilder = WorkPart.CAMSetup.CAMOperationCollection.CreateVazlMillingBuilder(camObject)
            ElseIf operationSubtype = 210 Then         ' This is a Fixed Axis Surface Contour Operation so create a Surface Contour Builder
                operationBuilder = WorkPart.CAMSetup.CAMOperationCollection.CreateSurfaceContourBuilder(camObject)
            ElseIf operationSubtype = 211 Then         ' This is a Variable Axis Surface Contour Operation so create Surface Contour Builder
                operationBuilder = WorkPart.CAMSetup.CAMOperationCollection.CreateSurfaceContourBuilder(camObject)
            End If
        End If
        Return operationBuilder

    End Function

    ' Function to save changes made
    Function CommitFunction(ByVal operation As CAM.Operation, ByVal operationBuilder As CAM.OperationBuilder) As Boolean
    
        Try
            'Save the changes made
            operationBuilder.Commit()
        Catch ex As NXException
            theSession.ListingWindow.Open()
            theSession.ListingWindow.WriteLine(operation.Name() & ": There is bad data in the object.")
            theSession.ListingWindow.WriteLine("EXCEPTION: " & ex.Message)
            ex.AssertErrorCode(ex.ErrorCode)
            Return False
        End Try
        
        Return True
        
    End Function
    
    ' Function to set variables in the Builder
    Function ActionFunction(ByVal operation As CAM.Operation, ByVal operationBuilder As CAM.OperationBuilder) As Boolean
        ' Check if there is a valid Builder
        If operationBuilder IsNot Nothing Then
            ' Change General Parameters
            GeneralParameters(operationBuilder)
            ' Change Cutting Parameters
            CutParameters(operationBuilder)
            ' Change Non Cutting Parameters
            NonCutParameters(operationBuilder)

            'Save the changes made
            CommitFunction(operation, operationBuilder)

            ' Tool path Generation, Post processing, Clsf Output all these will be done after
            ' the changes have been commited

            ' Prepare an array of objects
            Dim objects(1) As CAM.CAMObject
            objects(0) = operation

            ' Get the Work Part
            Dim workPart As Part = theSession.Parts.Work

            ' Get the Setup
            Dim setup As CAM.CAMSetup = workPart.CAMSetup()

            ' Prepare the units for CLSF output and Postprocessor output
            Dim outputUnits As Integer = CAMSetup.OutputUnits.Inch

            If workPart.PartUnits = BasePart.Units.Millimeters Then
                outputUnits = CAMSetup.OutputUnits.Metric
            End If

            ' Generate Tool Path
            setup.GenerateToolPath(objects)

            ' Output CLS
            ' setup.OutputClsf(objects, "CLSF_STANDARD", "test.cls", outputUnits)

            ' Post Process
            ' setup.Postprocess(objects, "Mill3ax", "test.ptp", outputUnits)

        End If

        Return True

    End Function

    ' Function to set Generate Parameters
    Function GeneralParameters(ByVal operationBuilder As CAM.OperationBuilder) As Boolean
        If TypeOf operationBuilder Is CAM.MillOperationBuilder Then
            Dim millOperationBuilder As CAM.MillOperationBuilder = operationBuilder
            ' Now we are ready to change the parameters
            Return True
        End If
        Return False
    End Function

    ' Function to set Cutting Parameters
    Function CutParameters(ByVal operationBuilder As CAM.OperationBuilder) As Boolean
        'What type of a builder is this?
        If TypeOf operationBuilder Is CAM.MillOperationBuilder Then
            Dim millOperationBuilder As CAM.MillOperationBuilder = operationBuilder
            'From the Operation Builder get the Cutting Parameters Object
            Dim cutParams As CAM.MillCutParameters = millOperationBuilder.CutParameters

            ' Now we are ready to change the parameters of cutting
            Return True
        End If
        Return False

    End Function


    ' Function to set Non Cutting Parameters
    Function NonCutParameters(ByVal operationBuilder As CAM.OperationBuilder) As Boolean
        Dim response As Boolean = False
        'What type of a builder is this?
        If TypeOf operationBuilder Is CAM.PlanarOperationBuilder Then
            Dim planarOperationBuilder As CAM.PlanarOperationBuilder = operationBuilder

            ' From the Operation Builder get the Non Cutting Builder
            Dim ncmBuilder As CAM.NcmPlanarBuilder = planarOperationBuilder.NonCuttingBuilder

            ' Now we are ready to change the Non Cutting Parameters

            response = True
        ElseIf TypeOf operationBuilder Is CAM.SurfaceContourBuilder Then
            Dim scBuilder As CAM.SurfaceContourBuilder = operationBuilder

            ' From the Operation Builder get the Non Cutting Builder
            Dim ncmBuilder As CAM.NcmScBuilder = scBuilder.NonCuttingBuilder

            ' Now we are ready to change the Non Cutting Parameters
            response = True
        End If

        Return response

    End Function
End Module















