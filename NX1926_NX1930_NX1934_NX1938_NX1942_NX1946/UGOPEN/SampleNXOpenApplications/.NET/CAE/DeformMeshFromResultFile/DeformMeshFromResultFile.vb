' DeformMeshFromResultFile.vb - Deform a mesh based on results file
'
' 
'
'------------------------------------------------------------
Option Strict Off
Imports System
Imports System.IO
Imports System.Windows.Forms
Imports NXOpen
Imports NXOpen.UF
Imports NXOpen.BlockStyler


Module DeformMeshFromResultFile


    Dim theSession As Session = Session.GetSession()
    Dim theUFSession As UFSession = UFSession.GetUFSession()
    Dim theLW As NXOpen.ListingWindow = theSession.ListingWindow()
    Dim theUI As NXOpen.UI = NXOpen.UI.GetUI()
    Dim theNXMessageBox As NXMessageBox = theUI.NXMessageBox



    Sub Main()

        Doit()

    End Sub

    Sub Doit()

        Dim scale As Double = 1.0

        Dim basePart As BasePart = theSession.Parts.BaseWork

        If basePart Is Nothing Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "FemPart must be loaded")
            Return
        End If

        If Not TypeOf basePart Is CAE.FemPart Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "Not a valid FemPart")
            Return
        End If

        Dim femPart As CAE.FemPart = CType(basePart, CAE.FemPart)

        Dim resultsFile As String = Nothing

        Try
            Dim openFileDialog As New OpenFileDialog()

            openFileDialog.Title = "Select solver results file"
            openFileDialog.Filter = "Nastran file(*.op2)|*.op2|ABAQUS file(*.fil)|*.fil|ABAQUS file(*.odb)|*.odb|All files (*.*)|*.*"
            openFileDialog.FilterIndex = 1
            openFileDialog.RestoreDirectory = True

            If openFileDialog.ShowDialog() = DialogResult.OK Then
                resultsFile = openFileDialog.FileName()
            Else
                Return
            End If

        Catch E As Exception
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, E.Message)
        End Try

        Dim results As CAE.Result = GetResults(resultsFile)

        If (results Is Nothing) Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "Unable to create Results Object from Solution")
            Return
        End If

        Dim loadCase As CAE.Loadcase = Nothing
        Dim iteration As CAE.Iteration = Nothing

        iteration = GetLoadCaseAndIteration(results, loadCase, scale)

        Dim resultType As CAE.ResultType = GetDisplacementResultType(iteration)

        Dim resultAccess As CAE.ResultAccess = GetResultAccess(results, resultType, scale)

        If (resultAccess Is Nothing) Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "Unable to create ResultsAccess Object from Solution")
            Return
        End If

        Dim femModel As CAE.FEModel = femPart.BaseFEModel

        If (femModel Is Nothing) Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "No valid FeModel in Sim")
            Return
        End If

        Dim nodesRepositionBuilder As CAE.NodesRepositionBuilder
        nodesRepositionBuilder = femModel.NodeElementMgr.CreateNodesRepositionBuilder()
        Dim fenodeLabelMap As CAE.FENodeLabelMap = femModel.FenodeLabelMap()

        Dim StartTime As Date = Now
        Dim EndTime As Date
        Dim difference As TimeSpan

        Dim nodeOffset As Integer = 0
        Dim elemOffset As Integer = 0
        Dim csysOffset As Integer = 0

        Dim nNodes As Integer = results.AskNumNodes()

        Dim comps(0) As NXOpen.CAE.Result.Component
        resultAccess.AskResultComponents(comps)
        Dim nComps As Integer = comps.Length
        Dim iComp As Integer
        Dim iNode As Integer = 1
        Do Until (iNode = nNodes + 1)

            Dim iNodes(0) As Integer
            iNodes(0) = iNode

            Dim iNodeLabel As Integer = results.AskNodeLabel(iNode)
            Dim position As NXOpen.Point3d() = results.AskNodeCoordinates(iNodes)

            Dim feNode As CAE.FENode = fenodeLabelMap.GetNode(iNodeLabel)

            If (feNode Is Nothing) Then
                theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "Could not find node")
                Return
            End If


            Dim values(0) As Double
            resultAccess.AskNodalResultAllComponents(iNode, values)

            If (values Is Nothing) Then
                theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "No Doubles array")
                Return
            End If

            Dim newLocation As Point3d
            ' Iterate through a collection
            iComp = 0
            For Each compValue As Double In values
                If (comps(iComp) = CAE.Result.Component.X) Then
                    newLocation.X = position(0).X + compValue
                End If

                If (comps(iComp) = CAE.Result.Component.Y) Then
                    newLocation.Y = position(0).Y + compValue
                End If
                If (comps(iComp) = CAE.Result.Component.Z) Then
                    newLocation.Z = position(0).Z + compValue
                End If

                iComp = iComp + 1
            Next

            nodesRepositionBuilder.SetNodePosition(feNode, newLocation)

            iNode = iNode + 1

        Loop

        nodesRepositionBuilder.Commit()
        nodesRepositionBuilder.Destroy()

        EndTime = Now
        difference = EndTime.Subtract(StartTime)

        Dim nodesPerSecond As Integer = nNodes / difference.TotalSeconds
        Dim tmpStr As String = " Nodes processed = " + nNodes.ToString() + " in " + difference.TotalSeconds.ToString() + " seconds, Nodes per sec = " + nodesPerSecond.ToString()


        theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Information, tmpStr)

        theSession.ResultManager().DeleteResult(results)

    End Sub

    Function GetResults(ByRef file As String) As CAE.Result

        Dim results As CAE.Result = Nothing

        Dim part As BasePart = theSession.Parts.BaseWork

        Dim theResultManager As CAE.ResultManager = theSession.ResultManager()

        If (theResultManager Is Nothing) Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "No valid ResultManager")
            Return Nothing
        End If

        Dim unit_sec As Unit = CType(part.UnitCollection.FindObject("Second"), Unit)
        Dim unit_radian As Unit = CType(part.UnitCollection.FindObject("Radian"), Unit)

        Dim unitSystem As NXOpen.CAE.Result.ResultBasicUnit

        ' This is an assumption that results units math the part, but we should
        ' probably ask user to specify this
        If part.PartUnits() = BasePart.Units.Millimeters Then

            Dim unit_mm As Unit = CType(part.UnitCollection.FindObject("MilliMeter"), Unit)
            Dim unit_kg As Unit = CType(part.UnitCollection.FindObject("Kilogram"), Unit)
            Dim unit_C As Unit = CType(part.UnitCollection.FindObject("Celsius"), Unit)
            Dim unit_microJ As Unit = CType(part.UnitCollection.FindObject("MicroJoule"), Unit)

            unitSystem.AngleUnit = unit_radian
            unitSystem.LengthUnit = unit_mm
            unitSystem.MassUnit = unit_kg
            unitSystem.TemperatureUnit = unit_C
            unitSystem.ThermalenergyUnit = unit_microJ
            unitSystem.TimeUnit = unit_sec
        Else
            Dim unit_lbm As Unit = CType(part.UnitCollection.FindObject("PoundMass"), Unit)
            Dim unit_in As Unit = CType(part.UnitCollection.FindObject("Inch"), Unit)
            Dim unit_F As Unit = CType(part.UnitCollection.FindObject("Fahrenheit"), Unit)
            Dim unit_ThermalEnergyEng As Unit = CType(part.UnitCollection.FindObject("ThermalEnergy_English1"), Unit)

            unitSystem.AngleUnit = unit_radian
            unitSystem.LengthUnit = unit_in
            unitSystem.MassUnit = unit_lbm
            unitSystem.TemperatureUnit = unit_F
            unitSystem.ThermalenergyUnit = unit_ThermalEnergyEng
            unitSystem.TimeUnit = unit_sec

        End If

        Dim importedResults As CAE.ImportedResult = Nothing

        Try
            importedResults = theResultManager.CreateImportedResult(file, unitSystem)
        Catch ex As Exception
            Return Nothing
        End Try

        If (importedResults Is Nothing) Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "Could not Access Solution Results")
            Return Nothing
        End If

        results = CType(importedResults, CAE.Result)

        Return results

    End Function
   Function GetResults(ByRef solution As CAE.SimSolution) As CAE.Result

        Dim results As CAE.Result = Nothing

        Dim part As BasePart = theSession.Parts.BaseWork

        Dim theResultManager As CAE.ResultManager = theSession.ResultManager()

        If (theResultManager Is Nothing) Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "No valid ResultManager")
            Return Nothing
        End If

        Dim solresults As CAE.SolutionResult = theResultManager.CreateSolutionResult(solution)

        If (solresults Is Nothing) Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "Could not Access Solution Results")
            Return Nothing
        End If

        results = CType(solresults, CAE.Result)


        Return results

    End Function

    Function GetDisplacementResultType(ByRef iteration As CAE.Iteration) As CAE.ResultType


        If (iteration Is Nothing) Then
            Return Nothing
        End If

        Dim baseResultTypes As CAE.BaseResultType() = iteration.GetResultTypes()

        For Each baseResultType As CAE.BaseResultType In baseResultTypes
            Dim resultType As CAE.ResultType = CType(baseResultType, CAE.ResultType)
            If (resultType.Quantity = CAE.Result.Quantity.Displacement) Then
                Return resultType
            End If


        Next

        Return Nothing

    End Function
    Function GetLoadCaseAndIteration(ByRef results As CAE.Result, ByRef selectedLoadCase As CAE.Loadcase, ByRef scale As Double) As CAE.Iteration



        Dim selectedIteration As CAE.Iteration = Nothing

        Dim nLoadCases = results.AskNumLoadcases()
        If nLoadCases > 0 Then

            Dim loadCaseSelect As LoadCaseSelectUI = Nothing
            Try

                loadCaseSelect = New LoadCaseSelectUI(results, scale)
                ' The following method shows the dialog immediately
                loadCaseSelect.Show()
                scale = loadCaseSelect.m_scale


                selectedLoadCase = CType(loadCaseSelect.m_selectedLoadCase, CAE.Loadcase)
                selectedIteration = CType(loadCaseSelect.m_selectediteration, CAE.Iteration)

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            Finally
                If loadCaseSelect IsNot Nothing Then
                    loadCaseSelect.Dispose()
                End If

            End Try

        End If
        Return selectedIteration

    End Function

    Function GetResultAccess(ByRef results As CAE.Result, ByRef resultType As CAE.ResultType, ByVal scale As Double) As CAE.ResultAccess


        Dim part As BasePart = theSession.Parts.BaseWork

        Dim theResultManager As CAE.ResultManager = theSession.ResultManager()

        If (theResultManager Is Nothing) Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "No valid ResultManager")
            Return Nothing
        End If
        Dim unit_length As Unit = Nothing

        If part.PartUnits() = BasePart.Units.Millimeters Then
            unit_length = CType(part.UnitCollection.FindObject("MilliMeter"), Unit)
        Else
            unit_length = CType(part.UnitCollection.FindObject("Inch"), Unit)
        End If

        Dim resultParameter As CAE.ResultParameters = theResultManager.CreateResultParameters()

        resultParameter.SetGenericResultType(resultType)

        Dim averaging As CAE.Result.Averaging
        averaging.DoAveraging = False
        averaging.AverageAcrossPropertyIds = True
        averaging.AverageAcrossMaterialIds = True
        averaging.AverageAcrossElementTypes = True
        averaging.AverageAcrossFeatangle = True
        averaging.AverageAcrossAnglevalue = 45.0
        averaging.IncludeInternalElementContributions = True


        resultParameter.SetResultComponent(CAE.Result.Component.Magnitude)
        'resultParameter.SetResultDataSection(CAE.Result.Section.All)
        resultParameter.SetSectionPlyLayer(0, 0, 0)
        resultParameter.SetAveragingCriteria(averaging)
        resultParameter.SetCoordinateSystem(CAE.Result.CoordinateSystem.AbsoluteRectangular)
        resultParameter.SetElementValueCriterion(CAE.Result.ElementValueCriterion.Average)
        resultParameter.SetComplexCriterion(CAE.Result.Complex.Amplitude)
        resultParameter.SetPhaseAngle(0.0)
        resultParameter.SetScale(scale)
        resultParameter.SetUnit(unit_length)


        Dim solResultsAccess As CAE.ResultAccess = theResultManager.CreateResultAccess(results, resultParameter)
        If (solResultsAccess Is Nothing) Then
            theNXMessageBox.Show("DeformMesh", NXMessageBox.DialogType.Error, "Could not create Results Access Object for Solution results")
        End If

        theResultManager.DeleteResultParameters(resultParameter)

        Return solResultsAccess

    End Function


    Public Function GetUnloadOption(ByVal dummy As String) As Integer

        'Unloads the image immediately after execution within NX
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Immediately

        '----Other unload options-------
        'Unloads the image when the NX session terminates
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination

        'Unloads the image explicitly, via an unload dialog
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Explicitly
        '-------------------------------

    End Function

    '------------------------------------------------------------------------------
    'Represents Block Styler application class
    '------------------------------------------------------------------------------
    Public Class LoadCaseSelectUI
        'class members
        Private Shared theSession As Session
        Private Shared theUI As UI
        Public Shared theDeformMeshFromResultFileUI As LoadCaseSelectUI
        Public m_selectedLoadCaseIdx As Integer
        Public m_selectedIterationIdx As Integer
        Public m_selectedLoadCase As CAE.BaseLoadcase
        Public m_selectediteration As CAE.BaseIteration
        Public m_scale As Double
        Private m_results As CAE.Result
        Private theDialogName As String
        Private theDialog As NXOpen.BlockStyler.BlockDialog
        Private group0 As NXOpen.BlockStyler.UIBlock ' Block type: Group
        Private group01 As NXOpen.BlockStyler.UIBlock ' Block type: Group
        Private loadcase As NXOpen.BlockStyler.ListBox ' Block type: List Box
        Private iteration As NXOpen.BlockStyler.ListBox ' Block type: List Box
        Private scaleValue As NXOpen.BlockStyler.UIBlock ' Block type: Double


        '------------------------------------------------------------------------------
        'Constructor for NX Styler class
        '------------------------------------------------------------------------------

        Public Sub New(ByRef results As CAE.Result, ByVal scale As Double)
            Try

                m_results = results
                m_scale = scale

                m_selectedLoadCaseIdx = 0
                m_selectedIterationIdx = 0
                m_selectedLoadCase = m_results.GetLoadcases()(0)
                m_selectediteration = m_selectedLoadCase.GetIterations()(0)

                theSession = Session.GetSession()
                Dim journal As String = theSession.ExecutingJournal
                Dim testFile As System.IO.FileInfo
                testFile = My.Computer.FileSystem.GetFileInfo(journal)
                Dim folderPath As String = testFile.DirectoryName


                ' dialog is expect to to be next to vb file. 
                theDialogName = My.Computer.FileSystem.CombinePath(folderPath, "SelectLoadCase.dlx")

                testFile = My.Computer.FileSystem.GetFileInfo(theDialogName)
                If Not testFile.Exists Then
                    theDialogName = "SelectLoadCase.dlx"
                End If
                theUI = UI.GetUI()
                theDialog = theUI.CreateDialog(theDialogName)

                theDialog.AddApplyHandler(AddressOf apply_cb)
                theDialog.AddOkHandler(AddressOf ok_cb)
                theDialog.AddUpdateHandler(AddressOf update_cb)
                theDialog.AddInitializeHandler(AddressOf initialize_cb)
                theDialog.AddDialogShownHandler(AddressOf dialogShown_cb)

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                Throw ex
            End Try
        End Sub


        '------------------------------------------------------------------------------
        'This method shows the dialog on the screen
        '------------------------------------------------------------------------------
        Public Sub Show()
            Try

                theDialog.Show()

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
        End Sub

        '------------------------------------------------------------------------------
        'Method Name: Dispose
        '------------------------------------------------------------------------------
        Public Sub Dispose()
            If theDialog IsNot Nothing Then
                theDialog.Dispose()
                theDialog = Nothing
            End If
        End Sub

        '------------------------------------------------------------------------------
        '---------------------Block Styler Callback Functions--------------------------
        '------------------------------------------------------------------------------

        '------------------------------------------------------------------------------
        'Callback Name: initialize_cb
        '------------------------------------------------------------------------------
        Public Sub initialize_cb()
            Try


                group0 = theDialog.TopBlock.FindBlock("group0")
                group01 = theDialog.TopBlock.FindBlock("group01")

                loadcase = CType(theDialog.TopBlock.FindBlock("loadcase"), NXOpen.BlockStyler.ListBox)
                iteration = CType(theDialog.TopBlock.FindBlock("iteration"), NXOpen.BlockStyler.ListBox)
                scaleValue = theDialog.TopBlock.FindBlock("scaleValue")


                Dim propertyList As BlockStyler.PropertyList
                propertyList = theDialog.TopBlock.GetProperties()
                propertyList.SetString("Label", "Select results case to use")

                propertyList = group0.GetProperties()
                propertyList.SetString("Label", "Select Load Cases to use")

                propertyList = group01.GetProperties()
                propertyList.SetString("Label", "Select iteration to use")

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
        End Sub


        '------------------------------------------------------------------------------
        'Callback Name: dialogShown_cb
        'This callback is executed just before the dialog launch. Thus any value set 
        'here will take precedence and dialog will be launched showing that value. 
        '------------------------------------------------------------------------------
        Public Sub dialogShown_cb()
            Try

                Dim propertyList As BlockStyler.PropertyList

                propertyList = loadcase.GetProperties()

                propertyList.SetStrings("ListItems", m_results.AskLoadcases())

                Dim selected As Integer() = {m_selectedLoadCaseIdx}

                propertyList.SetIntegerVector("SelectedItems", selected)

                propertyList = iteration.GetProperties()
                propertyList.SetStrings("ListItems", m_results.AskIterations(m_selectedLoadCaseIdx))

                selected(0) = m_selectedIterationIdx

                propertyList.SetIntegerVector("SelectedItems", selected)

                propertyList = scaleValue.GetProperties()
                propertyList.SetDouble("Value", m_scale)


            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
        End Sub

        '------------------------------------------------------------------------------
        'Callback Name: apply_cb
        '------------------------------------------------------------------------------
        Public Function apply_cb() As Integer
            Try

                Dim propertyList As BlockStyler.PropertyList

                propertyList = loadcase.GetProperties()
                Dim selected As Integer() = propertyList.GetIntegerVector("SelectedItems")
                If selected.Length > 0 Then
                    m_selectedLoadCaseIdx = selected(0)

                Else
                    m_selectedLoadCaseIdx = 0  ' did not pick anything
                End If

                propertyList = iteration.GetProperties()
                selected = propertyList.GetIntegerVector("SelectedItems")
                If selected.Length > 0 Then
                    m_selectedIterationIdx = selected(0)
                Else
                    m_selectedIterationIdx = 0  ' did not pick anything
                End If

                propertyList = scaleValue.GetProperties()
                m_scale = propertyList.GetDouble("Value")

                m_selectedLoadCase = m_results.GetLoadcases()(m_selectedLoadCaseIdx)
                m_selectediteration = m_selectedLoadCase.GetIterations()(m_selectedIterationIdx)

                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Information, "Select OK to comfirm Load case selection")

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
            apply_cb = 0
        End Function

        '------------------------------------------------------------------------------
        'Callback Name: update_cb
        '------------------------------------------------------------------------------
        Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
            Try

                If block Is loadcase Then

                    Dim propertyList As BlockStyler.PropertyList

                    propertyList = block.GetProperties()

                    Dim selectedLoadCase As Integer() = propertyList.GetIntegerVector("SelectedItems")
                    If selectedLoadCase.Length > 0 Then
                        m_selectedLoadCaseIdx = selectedLoadCase(0)
                    Else
                        m_selectedLoadCaseIdx = 0  ' did not pick anything
                    End If

                    propertyList = iteration.GetProperties()
                    propertyList.SetStrings("ListItems", m_results.AskIterations(m_selectedLoadCaseIdx))
                    Dim selectedIteration(0) As Integer

                    If m_selectedIterationIdx > m_results.AskNumIterations(m_selectedLoadCaseIdx) Then
                        selectedIteration(0) = m_selectedIterationIdx
                    Else
                        m_selectedIterationIdx = 0
                        selectedIteration(0) = 0
                    End If

                    propertyList.SetIntegerVector("SelectedItems", selectedIteration)


                ElseIf block Is iteration Then
                    Dim propertyList As BlockStyler.PropertyList

                    propertyList = block.GetProperties()
                    Dim selectedIteration As Integer() = propertyList.GetIntegerVector("SelectedItems")
                    If selectedIteration.Length > 0 Then
                        m_selectedIterationIdx = selectedIteration(0)
                    Else
                        m_selectedIterationIdx = 0  ' did not pick anything
                    End If

                ElseIf block Is scaleValue Then
                    '---- Enter your code here -----

                End If

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
            update_cb = 0



        End Function

        '------------------------------------------------------------------------------
        'Callback Name: ok_cb
        '------------------------------------------------------------------------------
        Public Function ok_cb() As Integer
            Try

                'apply_cb()

                loadcase = CType(theDialog.TopBlock.FindBlock("loadcase"), NXOpen.BlockStyler.ListBox)
                scaleValue = theDialog.TopBlock.FindBlock("scaleValue")

                Dim propertyList As BlockStyler.PropertyList

                propertyList = loadcase.GetProperties()
                Dim selected As Integer() = propertyList.GetIntegerVector("SelectedItems")
                If selected.Length > 0 Then
                    m_selectedLoadCaseIdx = selected(0)
                Else
                    m_selectedLoadCaseIdx = 0  ' did not pick anything
                End If

                propertyList = iteration.GetProperties()
                selected = propertyList.GetIntegerVector("SelectedItems")
                If selected.Length > 0 Then
                    m_selectedIterationIdx = selected(0)
                Else
                    m_selectedIterationIdx = 0  ' did not pick anything
                End If

                propertyList = scaleValue.GetProperties()
                m_scale = propertyList.GetDouble("Value")

                m_selectedLoadCase = m_results.GetLoadcases()(m_selectedLoadCaseIdx)
                m_selectediteration = m_selectedLoadCase.GetIterations()(m_selectedIterationIdx)

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
            ok_cb = 0
        End Function

    End Class
End Module


