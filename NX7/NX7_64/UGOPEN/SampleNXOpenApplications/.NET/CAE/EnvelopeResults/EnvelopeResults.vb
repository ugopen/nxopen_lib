' EnvelopeResults.vb - Sort across load cases for Max/Min/Absolute Max
'
' '
'
'------------------------------------------------------------
Option Strict Off
Imports System
Imports System.IO
Imports System.Windows.Forms

Imports NXOpen
Imports NXOpen.UF
Imports NXOpen.BlockStyler

Module EnvelopeResults

    Dim DEBUG As Integer = 0

    Dim theSession As Session = Session.GetSession()
    Dim theUFSession As UFSession = UFSession.GetUFSession()
    Dim theLW As NXOpen.ListingWindow = theSession.ListingWindow()
    Dim theUI As NXOpen.UI = NXOpen.UI.GetUI()
    Dim theNXMessageBox As NXMessageBox = theUI.NXMessageBox

    Dim outputFile As String
    Dim iAnalysisDatasetLabel As Integer = 1

    Dim results As CAE.Result
    Dim loadCases() As String
    Dim iSelectedCases() As Integer = {0}
    Dim resultType As CAE.Result.Type
    Dim component As CAE.Result.Component

    Dim StartTime As Date = Now

    Sub Main()

        theLW.Open()
        theLW.WriteLine("Starting Envelope Results")

        ' Check for open part
        If theSession.Parts.BaseWork Is Nothing Then
            theNXMessageBox.Show("Processing Results 2", NXMessageBox.DialogType.Error, "A Part Must be loaded")
            Return
        End If

        ' Get Results file/location - FUTURE - prompt for results attached to current sim
        Dim resultsFile As String = GetResultFileName()
        If resultsFile Is Nothing Then
            Return
        End If
        theLW.WriteLine(vbNewLine + "Results file: " + resultsFile + vbNewLine)

        ' Generate output universal file name
        outputFile = Left(resultsFile, resultsFile.LastIndexOf(".")) + Replace(resultsFile, ".", "_", resultsFile.LastIndexOf(".") + 1) + ".unv"
        theLW.WriteLine(" Output file: " + outputFile + vbNewLine)

        ' Close any post using these results
        theSession.Post.UnloadResultFile(resultsFile)

        ' Delete any existing file of the same name
        If (System.IO.File.Exists(outputFile)) Then
            System.IO.File.Delete(outputFile)
            theLW.WriteLine("** Deleting existing sort output file **")
        End If

        ' Create results object for the results file and ensure it is valid
        results = GetImportedResults(resultsFile)
        If (results Is Nothing) Then
            theNXMessageBox.Show("Processing Results 3", NXMessageBox.DialogType.Error, "Unable to create Results Object from Solution")
            Return
        End If

        ' Prompt for loadcases, results type and component to sort over
        Dim theEnvelopeResults As envelopeResults = Nothing

        Try

            theEnvelopeResults = New envelopeResults()
            ' The following method shows the dialog immediately
            theEnvelopeResults.Show()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            theEnvelopeResults.Dispose()
        End Try

        ' Clean up results object
        theSession.ResultManager.DeleteResult(results)

        'Report processing time
        Dim EndTime As Date = Date.Now
        Dim difference As TimeSpan = EndTime.Subtract(StartTime)

        theLW.WriteLine(vbNewLine + "End Time: " + EndTime.ToLongTimeString)
        theLW.WriteLine("  Total processing time: " + Math.Round(difference.TotalSeconds).ToString + " seconds" + vbNewLine)

        theUFSession.Ui.SetStatus("Envelope Results finished")
        theLW.WriteLine(vbNewLine + "Envelope Results Finished..." + vbNewLine)

    End Sub

    Sub DoIt()

        theLW.WriteLine(vbNewLine + "Selected sort criteria:")
        theLW.WriteLine(vbTab + "Result Type:  " + resultType.ToString)
        theLW.WriteLine(vbTab + "  Component:  " + component.ToString)

        StartTime = Date.Now
        theLW.WriteLine(vbNewLine + "Start Time: " + StartTime.ToLongTimeString)

        If resultType.Location = CAE.Result.Location.Nodal Then
            getNodalEnvelope()
        ElseIf resultType.Location = CAE.Result.Location.Element Then
            getElementalEnvelope()
        ElseIf resultType.Location = CAE.Result.Location.ElementNodal Then
            getElementNodalEnvelope()
        End If

    End Sub

    Sub getNodalEnvelope()

        Dim nNodes As Integer = results.AskNumNodes
        Dim theNodalEnvelope(nNodes - 1) As nodalEnvelope
        Dim initialize As Boolean = True

        For Each loadCaseIdx As Integer In iSelectedCases
            theLW.WriteLine(vbNewLine + "Processing load case " + (loadCaseIdx + 1).ToString)
            theUFSession.Ui.SetStatus("Processing load case " + (loadCaseIdx + 1).ToString)

            Dim iterationIdx As Integer = 0
            Dim scale As Double = 1.0

            Dim resultsAccess As CAE.ResultAccess = GetResultAccess(results, resultType, component, loadCaseIdx, iterationIdx, scale)
            If (resultsAccess Is Nothing) Then
                theNXMessageBox.Show("Processing Results 4", NXMessageBox.DialogType.Error, "Unable to create ResultsAccess Object from Solution")
                Return
            End If

            theLW.WriteLine("  Number of nodes: " + nNodes.ToString)
            theUFSession.Ui.UpdateListingWindow()

            For iNode As Integer = 0 To nNodes - 1
                Dim iNodeLabel As Integer = results.AskNodeLabel(iNode + 1)
                Dim value As Double = resultsAccess.AskNodalResult(iNode + 1)

                If (DEBUG) Then theLW.WriteLine("Node: " + iNodeLabel.ToString + " value: " + value.ToString)

                theNodalEnvelope(iNode).nodeId = iNodeLabel

                If (initialize OrElse value > theNodalEnvelope(iNode).maxVal) Then
                    theNodalEnvelope(iNode).maxVal = value
                    theNodalEnvelope(iNode).maxLc = loadCaseIdx + 1
                End If

                If (initialize OrElse value < theNodalEnvelope(iNode).minVal) Then
                    theNodalEnvelope(iNode).minVal = value
                    theNodalEnvelope(iNode).minLc = loadCaseIdx + 1
                End If

                If (initialize OrElse Math.Abs(value) > Math.Abs(theNodalEnvelope(iNode).absVal)) Then
                    theNodalEnvelope(iNode).absVal = value
                    theNodalEnvelope(iNode).absLc = loadCaseIdx + 1
                End If

            Next iNode

            initialize = False

        Next loadCaseIdx

        If DEBUG Then
            theLW.WriteLine(vbNewLine + "Element/Node ID" + vbTab + "Max Value" + vbTab + "Max Case" + vbTab + "Min Value" + vbTab + "Min Case" + vbTab + "Abs Value" + vbTab + "Abs Case")
            For iNode As Integer = 0 To nNodes - 1
                Dim maxStr As String = Format(theNodalEnvelope(iNode).maxVal, "0.0000E+00") + vbTab + Format(theNodalEnvelope(iNode).maxLc, "######")
                Dim minStr As String = Format(theNodalEnvelope(iNode).minVal, "0.0000E+00") + vbTab + Format(theNodalEnvelope(iNode).minLc, "######")
                Dim absStr As String = Format(theNodalEnvelope(iNode).absVal, "0.0000E+00") + vbTab + Format(theNodalEnvelope(iNode).absLc, "######")
                theLW.WriteLine(vbTab + Format(theNodalEnvelope(iNode).nodeId, "##########") + vbTab + vbTab + maxStr + vbTab + vbTab + minStr + vbTab + vbTab + absStr)
            Next
        End If

        theUFSession.Ui.SetStatus("Sort complete. Writing results to universal file")
        theLW.WriteLine(vbNewLine + "Sort complete. Writing results to universal file")
        theUFSession.Ui.UpdateListingWindow()

        writeNodalEnvelope(theNodalEnvelope)

    End Sub

    Sub getElementalEnvelope()

        Dim nElements As Integer = results.AskNumElements
        Dim theElemEnvelope(nElements - 1) As elemEnvelope
        Dim initialize As Boolean = True

        For Each loadCaseIdx As Integer In iSelectedCases
            theLW.WriteLine(vbNewLine + "Processing load case " + (loadCaseIdx + 1).ToString)
            theUFSession.Ui.SetStatus("Processing load case " + (loadCaseIdx + 1).ToString)

            Dim iterationIdx As Integer = 0
            Dim scale As Double = 1.0

            Dim resultsAccess As CAE.ResultAccess = GetResultAccess(results, resultType, component, loadCaseIdx, iterationIdx, scale)
            If (resultsAccess Is Nothing) Then
                theNXMessageBox.Show("Processing Results 4", NXMessageBox.DialogType.Error, "Unable to create ResultsAccess Object from Solution")
                Return
            End If

            theLW.WriteLine("  Number of elements: " + nElements.ToString)
            theUFSession.Ui.UpdateListingWindow()

            For iElement As Integer = 0 To nElements - 1
                Dim iElementLabel As Integer = results.AskElementLabel(iElement + 1)
                Dim value As Double = resultsAccess.AskElementResult(iElement + 1)

                If (DEBUG) Then theLW.WriteLine("Element: " + iElementLabel.ToString + " value: " + value.ToString)

                theElemEnvelope(iElement).elemId = iElementLabel

                If (initialize OrElse value > theElemEnvelope(iElement).maxVal) Then
                    theElemEnvelope(iElement).maxVal = value
                    theElemEnvelope(iElement).maxLc = loadCaseIdx + 1
                End If

                If (initialize OrElse value < theElemEnvelope(iElement).minVal) Then
                    theElemEnvelope(iElement).minVal = value
                    theElemEnvelope(iElement).minLc = loadCaseIdx + 1
                End If

                If (initialize OrElse Math.Abs(value) > Math.Abs(theElemEnvelope(iElement).absVal)) Then
                    theElemEnvelope(iElement).absVal = value
                    theElemEnvelope(iElement).absLc = loadCaseIdx + 1
                End If

            Next iElement

            initialize = False

        Next loadCaseIdx

        If DEBUG Then
            theLW.WriteLine(vbNewLine + "Element/Node ID" + vbTab + "Max Value" + vbTab + "Max Case" + vbTab + "Min Value" + vbTab + "Min Case" + vbTab + "Abs Value" + vbTab + "Abs Case")
            For iElement As Integer = 0 To nElements - 1
                Dim maxStr As String = Format(theElemEnvelope(iElement).maxVal, "0.0000E+00") + vbTab + Format(theElemEnvelope(iElement).maxLc, "######")
                Dim minStr As String = Format(theElemEnvelope(iElement).minVal, "0.0000E+00") + vbTab + Format(theElemEnvelope(iElement).minLc, "######")
                Dim absStr As String = Format(theElemEnvelope(iElement).absVal, "0.0000E+00") + vbTab + Format(theElemEnvelope(iElement).absLc, "######")
                theLW.WriteLine(vbTab + Format(theElemEnvelope(iElement).elemId, "##########") + vbTab + vbTab + maxStr + vbTab + vbTab + minStr + vbTab + vbTab + absStr)
            Next
        End If

        theUFSession.Ui.SetStatus("Sort complete. Writing results to universal file")
        theLW.WriteLine(vbNewLine + "Sort complete. Writing results to universal file")
        theUFSession.Ui.UpdateListingWindow()

        writeElementalEnvelope(theElemEnvelope)

    End Sub

    Sub getElementNodalEnvelope()

        Dim nElements As Integer = results.AskNumElements()
        Dim theElemNodalEnvelope(nElements - 1) As elemNodalEnvelope
        Dim initialize As Boolean = True

        For Each loadCaseIdx As Integer In iSelectedCases
            theLW.WriteLine(vbNewLine + "Processing load case " + (loadCaseIdx + 1).ToString)
            theUFSession.Ui.SetStatus("Processing load case " + (loadCaseIdx + 1).ToString)

            Dim iterationIdx As Integer = 0
            Dim scale As Double = 1.0

            Dim resultsAccess As CAE.ResultAccess = GetResultAccess(results, resultType, component, loadCaseIdx, iterationIdx, scale)
            If (resultsAccess Is Nothing) Then
                theNXMessageBox.Show("Processing Results 4", NXMessageBox.DialogType.Error, "Unable to create ResultsAccess Object from Solution")
                Return
            End If

            theLW.WriteLine("  Number of elements: " + nElements.ToString)
            theUFSession.Ui.UpdateListingWindow()

            Dim valueIdx As Integer = 0
            For iElement As Integer = 0 To nElements - 1
                Dim iElementLabel As Integer = results.AskElementLabel(iElement + 1)
                If DEBUG Then theLW.WriteLine("Element: " + iElementLabel.ToString)

                Dim values(0) As Double
                Dim iNodeLabels(0) As Integer
                resultsAccess.AskElementNodalResult(iElement + 1, iNodeLabels, values)

                If (values Is Nothing) Then
                    theNXMessageBox.Show("Processing Results 5", NXMessageBox.DialogType.Error, "No Doubles array")
                    Return
                End If

                theElemNodalEnvelope(iElement).elemId = iElementLabel

                Dim nValues As Integer = values.Length
                Dim nNodes As Integer = iNodeLabels.Length

                If (initialize) Then ReDim theElemNodalEnvelope(iElement).nodes(nNodes - 1)

                For iNode As Integer = 0 To nNodes - 1
                    Dim iNodeLabel As Integer = results.AskNodeLabel(iNodeLabels(iNode))
                    If DEBUG Then theLW.WriteLine(vbTab + "Node: " + iNodeLabel.ToString + "  Value: " + values(iNode).ToString)

                    theElemNodalEnvelope(iElement).nodes(iNode).nodeId = iNodeLabel

                    If (initialize OrElse values(iNode) > theElemNodalEnvelope(iElement).nodes(iNode).maxVal) Then
                        theElemNodalEnvelope(iElement).nodes(iNode).maxVal = values(iNode)
                        theElemNodalEnvelope(iElement).nodes(iNode).maxLc = loadCaseIdx + 1
                    End If

                    If (initialize OrElse values(iNode) < theElemNodalEnvelope(iElement).nodes(iNode).minVal) Then
                        theElemNodalEnvelope(iElement).nodes(iNode).minVal = values(iNode)
                        theElemNodalEnvelope(iElement).nodes(iNode).minLc = loadCaseIdx + 1
                    End If

                    If (initialize OrElse Math.Abs(values(iNode)) > Math.Abs(theElemNodalEnvelope(iElement).nodes(iNode).absVal)) Then
                        theElemNodalEnvelope(iElement).nodes(iNode).absVal = values(iNode)
                        theElemNodalEnvelope(iElement).nodes(iNode).absLc = loadCaseIdx + 1
                    End If

                Next iNode

            Next iElement

            initialize = False

        Next loadCaseIdx

        If DEBUG Then
            theLW.WriteLine(vbNewLine + "Element ID" + vbTab + "Node ID" + vbTab + "Max Value" + vbTab + "Max Case" + vbTab + "Min Value" + vbTab + "Min Case" + vbTab + "Abs Value" + vbTab + "Abs Case")
            For iElement As Integer = 0 To nElements - 1
                theLW.WriteLine(vbTab + theElemNodalEnvelope(iElement).elemId.ToString)
                For iNode As Integer = 0 To theElemNodalEnvelope(iElement).nodes.Length - 1
                    Dim maxStr As String = Format(theElemNodalEnvelope(iElement).nodes(iNode).maxVal, "0.0000E+00") + vbTab + Format(theElemNodalEnvelope(iElement).nodes(iNode).maxLc, "######")
                    Dim minStr As String = Format(theElemNodalEnvelope(iElement).nodes(iNode).minVal, "0.0000E+00") + vbTab + Format(theElemNodalEnvelope(iElement).nodes(iNode).minLc, "######")
                    Dim absStr As String = Format(theElemNodalEnvelope(iElement).nodes(iNode).absVal, "0.0000E+00") + vbTab + Format(theElemNodalEnvelope(iElement).nodes(iNode).absLc, "######")
                    theLW.WriteLine(vbTab + vbTab + Format(theElemNodalEnvelope(iElement).nodes(iNode).nodeId, "##########") + vbTab + vbTab + maxStr + vbTab + vbTab + minStr + vbTab + vbTab + absStr)
                Next iNode
            Next iElement
        End If

        theUFSession.Ui.SetStatus("Sort complete. Writing results to universal file")
        theLW.WriteLine(vbNewLine + "Sort complete. Writing results to universal file")
        theUFSession.Ui.UpdateListingWindow()

        writeElementNodalEnvelope(theElemNodalEnvelope)

    End Sub

    Sub writeNodalEnvelope(ByRef theNodalEnvelope() As nodalEnvelope)
        Dim sw As StreamWriter = New StreamWriter(outputFile)

        Dim anyOf As Char() = "/\".ToCharArray()
        Dim parentFile As String = Right(outputFile, (outputFile.Length - outputFile.LastIndexOfAny(anyOf)) - 1)
        parentFile = Left(parentFile, parentFile.LastIndexOf("."))
        parentFile = StrReverse(Replace(StrReverse(parentFile), "_", ".", , 1))

        If (DEBUG) Then theLW.WriteLine(vbNewLine + "ParentFile: " + parentFile)

        Dim name As String = resultType.Quantity.ToString + " - " + resultType.Location.ToString

        Dim sortCases As String = Nothing
        For Each iCase As Integer In iSelectedCases
            sortCases = sortCases + (iCase + 1).ToString + ", "
        Next
        sortCases = Left(sortCases, sortCases.LastIndexOf(","))

        Dim idLine(4) As String
        idLine(0) = "Generated from results in " + parentFile
        idLine(1) = " Criteria:  Max Value from load cases " + sortCases
        idLine(2) = "   Result:  " + resultType.Quantity.ToString + " - " + resultType.Location.ToString
        idLine(3) = "Component:  " + component.ToString
        idLine(4) = "  Section:  " + resultType.Section.ToString

        Dim iType As Integer = GetUnvResultType()

        Dim nNodes As Integer = theNodalEnvelope.Length

        ' Write Max value dataset
        Dim iSetId = 1
        write2414Header(sw, 1, name, idLine, iType, 1, iSetId)
        For iNode As Integer = 0 To nNodes - 1
            sw.WriteLine("{0,10}", theNodalEnvelope(iNode).nodeId)
            sw.WriteLine("{0,13:0.000000E+00}", theNodalEnvelope(iNode).maxVal)
        Next
        sw.WriteLine("    -1")

        ' Write Max loadcase dataset
        iSetId += 1
        idLine(1) = " Criteria:  Max Value ID's from load cases " + sortCases
        write2414Header(sw, 1, name, idLine, iType, 1, iSetId)
        For iNode As Integer = 0 To nNodes - 1
            sw.WriteLine("{0,10}", theNodalEnvelope(iNode).nodeId)
            sw.WriteLine("{0,13:0.000000E+00}", theNodalEnvelope(iNode).maxLc)
        Next
        sw.WriteLine("    -1")

        ' Write Min value dataset
        iSetId += 1
        idLine(1) = " Criteria:  Min Value from load cases " + sortCases
        write2414Header(sw, 1, name, idLine, iType, 2, iSetId)
        For iNode As Integer = 0 To nNodes - 1
            sw.WriteLine("{0,10}", theNodalEnvelope(iNode).nodeId)
            sw.WriteLine("{0,13:0.000000E+00}", theNodalEnvelope(iNode).minVal)
        Next
        sw.WriteLine("    -1")

        ' Write Min loadcase dataset
        iSetId += 1
        idLine(1) = " Criteria:  Min Value ID's from load cases " + sortCases
        write2414Header(sw, 1, name, idLine, iType, 2, iSetId)
        For iNode As Integer = 0 To nNodes - 1
            sw.WriteLine("{0,10}", theNodalEnvelope(iNode).nodeId)
            sw.WriteLine("{0,13:0.000000E+00}", theNodalEnvelope(iNode).minLc)
        Next
        sw.WriteLine("    -1")

        ' Write Abs value dataset
        iSetId += 1
        idLine(1) = " Criteria:  Max Abs Value from load cases " + sortCases
        write2414Header(sw, 1, name, idLine, iType, 3, iSetId)
        For iNode As Integer = 0 To nNodes - 1
            sw.WriteLine("{0,10}", theNodalEnvelope(iNode).nodeId)
            sw.WriteLine("{0,13:0.000000E+00}", theNodalEnvelope(iNode).absVal)
        Next
        sw.WriteLine("    -1")

        ' Write Abs loadcase dataset
        iSetId += 1
        idLine(1) = " Criteria:  Max Abs Value ID's from load cases " + sortCases
        write2414Header(sw, 1, name, idLine, iType, 3, iSetId)
        For iNode As Integer = 0 To nNodes - 1
            sw.WriteLine("{0,10}", theNodalEnvelope(iNode).nodeId)
            sw.WriteLine("{0,13:0.000000E+00}", theNodalEnvelope(iNode).absLc)
        Next
        sw.WriteLine("    -1")

        sw.Close()

    End Sub

    Sub writeElementalEnvelope(ByRef theElemEnvelope() As elemEnvelope)

        Dim sw As StreamWriter = New StreamWriter(outputFile)

        Dim anyOf As Char() = "/\".ToCharArray()
        Dim parentFile As String = Right(outputFile, (outputFile.Length - outputFile.LastIndexOfAny(anyOf)) - 1)
        parentFile = Left(parentFile, parentFile.LastIndexOf("."))
        parentFile = StrReverse(Replace(StrReverse(parentFile), "_", ".", , 1))

        If (DEBUG) Then theLW.WriteLine(vbNewLine + "ParentFile: " + parentFile)

        Dim name As String = resultType.Quantity.ToString + " - " + resultType.Location.ToString

        Dim sortCases As String = Nothing
        For Each iCase As Integer In iSelectedCases
            sortCases = sortCases + (iCase + 1).ToString + ", "
        Next
        sortCases = Left(sortCases, sortCases.LastIndexOf(","))

        Dim idLine(4) As String
        idLine(0) = "Generated from results in " + parentFile
        idLine(1) = " Criteria:  Max Value from load cases " + sortCases
        idLine(2) = "   Result:  " + resultType.Quantity.ToString + " - " + resultType.Location.ToString
        idLine(3) = "Component:  " + component.ToString
        idLine(4) = "  Section:  " + resultType.Section.ToString

        Dim iType As Integer = GetUnvResultType()

        Dim nElements As Integer = theElemEnvelope.Length

        ' Write Max value dataset
        Dim iSetId = 1
        write2414Header(sw, 2, name, idLine, iType, 1, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}{1,10}", theElemEnvelope(iElement).elemId, 1)
            sw.WriteLine("{0,13:0.000000E+00}", theElemEnvelope(iElement).maxVal)
        Next
        sw.WriteLine("    -1")

        ' Write Max loadcase dataset
        iSetId += 1
        idLine(1) = " Criteria:  Max Value ID's from load cases " + sortCases
        write2414Header(sw, 2, name, idLine, iType, 1, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}{1,10}", theElemEnvelope(iElement).elemId, 1)
            sw.WriteLine("{0,13:0.000000E+00}", theElemEnvelope(iElement).maxLc)
        Next
        sw.WriteLine("    -1")

        ' Write Min value dataset
        iSetId += 1
        idLine(1) = " Criteria:  Min Value from load cases " + sortCases
        write2414Header(sw, 2, name, idLine, iType, 2, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}{1,10}", theElemEnvelope(iElement).elemId, 1)
            sw.WriteLine("{0,13:0.000000E+00}", theElemEnvelope(iElement).minVal)
        Next
        sw.WriteLine("    -1")

        ' Write Min loadcase dataset
        iSetId += 1
        idLine(1) = " Criteria:  Min Value ID's from load cases " + sortCases
        write2414Header(sw, 2, name, idLine, iType, 2, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}{1,10}", theElemEnvelope(iElement).elemId, 1)
            sw.WriteLine("{0,13:0.000000E+00}", theElemEnvelope(iElement).minLc)
        Next
        sw.WriteLine("    -1")

        ' Write Abs value dataset
        iSetId += 1
        idLine(1) = " Criteria:  Max Abs Value from load cases " + sortCases
        write2414Header(sw, 2, name, idLine, iType, 3, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}{1,10}", theElemEnvelope(iElement).elemId, 1)
            sw.WriteLine("{0,13:0.000000E+00}", theElemEnvelope(iElement).absVal)
        Next
        sw.WriteLine("    -1")

        ' Write Abs loadcase dataset
        iSetId += 1
        idLine(1) = " Criteria:  Max Abs Value ID's from load cases " + sortCases
        write2414Header(sw, 2, name, idLine, iType, 3, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}{1,10}", theElemEnvelope(iElement).elemId, 1)
            sw.WriteLine("{0,13:0.000000E+00}", theElemEnvelope(iElement).absLc)
        Next
        sw.WriteLine("    -1")

        sw.Close()

    End Sub

    Sub writeElementNodalEnvelope(ByRef theElemNodalEnvelope() As elemNodalEnvelope)

        Dim sw As StreamWriter = New StreamWriter(outputFile)

        Dim anyOf As Char() = "/\".ToCharArray()
        Dim parentFile As String = Right(outputFile, (outputFile.Length - outputFile.LastIndexOfAny(anyOf)) - 1)
        parentFile = Left(parentFile, parentFile.LastIndexOf("."))
        parentFile = StrReverse(Replace(StrReverse(parentFile), "_", ".", , 1))

        If (DEBUG) Then theLW.WriteLine(vbNewLine + "ParentFile: " + parentFile)

        Dim name As String = resultType.Quantity.ToString + " - " + resultType.Location.ToString

        Dim sortCases As String = Nothing
        For Each iCase As Integer In iSelectedCases
            sortCases = sortCases + (iCase + 1).ToString + ", "
        Next
        sortCases = Left(sortCases, sortCases.LastIndexOf(","))

        Dim idLine(4) As String
        idLine(0) = "Generated from results in " + parentFile
        idLine(1) = " Criteria:  Max Value from load cases " + sortCases
        idLine(2) = "   Result:  " + resultType.Quantity.ToString + " - " + resultType.Location.ToString
        idLine(3) = "Component:  " + component.ToString
        idLine(4) = "  Section:  " + resultType.Section.ToString

        Dim iType As Integer = GetUnvResultType()

        Dim nElements As Integer = theElemNodalEnvelope.Length

        ' Write Max value dataset
        Dim iSetId = 1
        write2414Header(sw, 3, name, idLine, iType, 1, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}         1{1,10}         1{2,10}", theElemNodalEnvelope(iElement).elemId, theElemNodalEnvelope(iElement).nodes.Length, 1)
            For iNode As Integer = 0 To theElemNodalEnvelope(iElement).nodes.Length - 1
                sw.WriteLine("{0,13:0.000000E+00}", theElemNodalEnvelope(iElement).nodes(iNode).maxVal)
            Next iNode
        Next iElement
        sw.WriteLine("    -1")

        ' Write Max loadcase dataset
        iSetId += 1
        idLine(1) = " Criteria:  Max Value ID's from load cases " + sortCases
        write2414Header(sw, 3, name, idLine, iType, 1, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}         1{1,10}         1{2,10}", theElemNodalEnvelope(iElement).elemId, theElemNodalEnvelope(iElement).nodes.Length, 1)
            For iNode As Integer = 0 To theElemNodalEnvelope(iElement).nodes.Length - 1
                sw.WriteLine("{0,13:0.000000E+00}", theElemNodalEnvelope(iElement).nodes(iNode).maxLc)
            Next iNode
        Next iElement
        sw.WriteLine("    -1")

        ' Write Min value dataset
        iSetId += 1
        idLine(1) = " Criteria:  Min Value from load cases " + sortCases
        write2414Header(sw, 3, name, idLine, iType, 2, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}         1{1,10}         1{2,10}", theElemNodalEnvelope(iElement).elemId, theElemNodalEnvelope(iElement).nodes.Length, 1)
            For iNode As Integer = 0 To theElemNodalEnvelope(iElement).nodes.Length - 1
                sw.WriteLine("{0,13:0.000000E+00}", theElemNodalEnvelope(iElement).nodes(iNode).minVal)
            Next iNode
        Next iElement
        sw.WriteLine("    -1")

        ' Write min loadcase dataset
        iSetId += 1
        idLine(1) = " Criteria:  Min Value ID's from load cases " + sortCases
        write2414Header(sw, 3, name, idLine, iType, 2, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}         1{1,10}         1{2,10}", theElemNodalEnvelope(iElement).elemId, theElemNodalEnvelope(iElement).nodes.Length, 1)
            For iNode As Integer = 0 To theElemNodalEnvelope(iElement).nodes.Length - 1
                sw.WriteLine("{0,13:0.000000E+00}", theElemNodalEnvelope(iElement).nodes(iNode).minLc)
            Next iNode
        Next iElement
        sw.WriteLine("    -1")

        ' Write absolute value dataset
        iSetId += 1
        idLine(1) = " Criteria:  Max Abs Value from load cases " + sortCases
        write2414Header(sw, 3, name, idLine, iType, 3, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}         1{1,10}         1{2,10}", theElemNodalEnvelope(iElement).elemId, theElemNodalEnvelope(iElement).nodes.Length, 1)
            For iNode As Integer = 0 To theElemNodalEnvelope(iElement).nodes.Length - 1
                sw.WriteLine("{0,13:0.000000E+00}", theElemNodalEnvelope(iElement).nodes(iNode).absVal)
            Next iNode
        Next iElement
        sw.WriteLine("    -1")

        ' Write absolute loadcase dataset
        iSetId += 1
        idLine(1) = " Criteria:  Max Abs Value ID's from load cases " + sortCases
        write2414Header(sw, 3, name, idLine, iType, 3, iSetId)
        For iElement As Integer = 0 To nElements - 1
            sw.WriteLine("{0,10}         1{1,10}         1{2,10}", theElemNodalEnvelope(iElement).elemId, theElemNodalEnvelope(iElement).nodes.Length, 1)
            For iNode As Integer = 0 To theElemNodalEnvelope(iElement).nodes.Length - 1
                sw.WriteLine("{0,13:0.000000E+00}", theElemNodalEnvelope(iElement).nodes(iNode).absLc)
            Next iNode
        Next iElement
        sw.WriteLine("    -1")

        sw.Close()

    End Sub

    Sub getResultsType(ByRef resultTypes() As NXOpen.CAE.Result.Type, ByRef resultTypeDesc() As String)
        ' Loop through all selected loadcases and build list that is the intersection
        ' of the results types available in all of them

        Dim iterationIdx As Integer = 0
        Dim lc0Types() As NXOpen.CAE.Result.Type = Nothing
        Dim lc0TypeDesc() As String = Nothing
        Dim lcTypes() As NXOpen.CAE.Result.Type = Nothing
        Dim lcTypeDesc() As String = Nothing

        If (iSelectedCases.Length = 1) Then

            results.AskResultTypes(iSelectedCases(0), iterationIdx, resultTypes, resultTypeDesc)

        Else
            ' Get list of result types for first selected case
            results.AskResultTypes(iSelectedCases(0), iterationIdx, lc0Types, lc0TypeDesc)

            ' Get list of result types for remaining selected cases.
            ' Keep only the types that are the intersection of all selected cases
            Dim iDelete(lc0Types.Length - 1) As Integer

            For iLoadCase As Integer = 1 To iSelectedCases.Length - 1
                results.AskResultTypes(iSelectedCases(iLoadCase), iterationIdx, lcTypes, lcTypeDesc)

                If (DEBUG = 2) Then theLW.WriteLine(vbNewLine + "Load Case " + (iSelectedCases(iLoadCase) + 1).ToString + " result type intersection " + lcTypes.Length.ToString + " Results Types:")
                For iType As Integer = 0 To lc0Types.Length - 1
                    If (DEBUG = 2) Then theLW.WriteLine("   " + iType.ToString + " - " + lc0TypeDesc(iType))

                    If (Array.IndexOf(Of CAE.Result.Type)(lcTypes, lc0Types(iType)) = -1) Then
                        If (DEBUG = 2) Then theLW.WriteLine("  This type does not exist in the current load case")
                        iDelete(iType) = 1
                    End If

                Next iType

            Next iLoadCase

            ReDim resultTypes(lc0Types.Length - 1)
            ReDim resultTypeDesc(lc0Types.Length - 1)
            Dim resIdx As Integer = 0

            For iType As Integer = 0 To lc0Types.Length - 1
                If (iDelete(iType) <> 1) Then
                    If (DEBUG = 2) Then theLW.WriteLine("resIdx: " + resIdx.ToString + "   " + iType.ToString + " - " + lc0TypeDesc(iType))

                    resultTypes(resIdx) = lc0Types(iType)
                    resultTypeDesc(resIdx) = lc0TypeDesc(iType)
                    resIdx += 1
                End If
            Next

            ReDim Preserve resultTypes(resIdx - 1)
            ReDim Preserve resultTypeDesc(resIdx - 1)

            If (DEBUG = 2) Then
                theLW.WriteLine(vbNewLine + "Results Types: " + resultTypes.Length.ToString)
                For iType As Integer = 0 To resultTypeDesc.Length - 1
                    theLW.WriteLine("   " + iType.ToString + " - " + resultTypeDesc(iType))
                Next
            End If

        End If

    End Sub

    Sub getComponent(ByVal resultType As NXOpen.CAE.Result.Type, ByVal loadCaseIdx As Integer, ByRef comps() As NXOpen.CAE.Result.Component, ByRef compNames() As String)
        Dim part As BasePart = theSession.Parts.BaseWork

        Dim iterationIdx As Integer = 0

        Dim theResultManager As CAE.ResultManager = theSession.ResultManager()

        If (theResultManager Is Nothing) Then
            theNXMessageBox.Show("Processing Results", NXMessageBox.DialogType.Error, "No valid ResultManager")
            Return
        End If

        Dim resultParameter As CAE.ResultParameters = theResultManager.CreateResultParameters()
        resultParameter.SetLoadcaseIteration(loadCaseIdx, iterationIdx)
        resultParameter.SetResultType(resultType)

        Dim resultsAccess As CAE.ResultAccess = theResultManager.CreateResultAccess(results, resultParameter)

        If (resultsAccess Is Nothing) Then
            theNXMessageBox.Show("Processing Results", NXMessageBox.DialogType.Error, "Could not create Results Access Object for Solution results")
            Return
        End If

        resultsAccess.AskResultComponents(comps)
        Dim nComps As Integer = comps.Length
        ReDim compNames(nComps - 1)

        If DEBUG = 2 Then theLW.WriteLine(vbNewLine + "Number of components: " + nComps.ToString)
        For iComp As Integer = 0 To nComps - 1
            If DEBUG = 2 Then theLW.WriteLine("   " + iComp.ToString + " - " + comps(iComp).ToString)
            compNames(iComp) = comps(iComp).ToString
        Next

    End Sub

    Sub write2414Header(ByVal sw As StreamWriter, ByVal iLocation As Integer, ByVal name As String, ByVal idLine() As String, ByVal iType As Integer, ByVal iSolSetID As Integer, ByVal iBoundaryConditionID As Integer)
        sw.WriteLine("{0,6}", -1)
        sw.WriteLine("{0,6}", 2414)
        sw.WriteLine("{0,10}", iAnalysisDatasetLabel)
        sw.WriteLine("{0,-80}", Left(name, 80))
        sw.WriteLine("{0,10}", iLocation)
        sw.WriteLine("{0,-80}", Left(idLine(0), 80))
        sw.WriteLine("{0,-80}", Left(idLine(1), 80))
        sw.WriteLine("{0,-80}", Left(idLine(2), 80))
        sw.WriteLine("{0,-80}", Left(idLine(3), 80))
        sw.WriteLine("{0,-80}", Left(idLine(4), 80))
        sw.WriteLine("         1         1         1{0,10}         2         1", iType)
        sw.WriteLine("         0         0{0,10}{1,10}{2,10}         0         0         0", iSolSetID, iBoundaryConditionID, iBoundaryConditionID + 1)
        sw.WriteLine("       500         0")
        sw.WriteLine(" 0.00000E+000 0.00000E+000 0.00000E+000 0.00000E+000 0.00000E+000 0.00000E+000")
        sw.WriteLine(" 0.00000E+000 0.00000E+000 0.00000E+000 0.00000E+000 0.00000E+000 0.00000E+000")

        iAnalysisDatasetLabel += 1

    End Sub

    Function GetResultFileName()

        Dim resultsFile As String = Nothing

        Try

            Dim openFileDialog As New OpenFileDialog()

            If theSession.Parts.BaseWork IsNot Nothing Then

                Dim testFile As System.IO.FileInfo = My.Computer.FileSystem.GetFileInfo(theSession.Parts.BaseWork.FullPath())
                openFileDialog.InitialDirectory = testFile.DirectoryName

            End If

            openFileDialog.Title = "Select solver results file"
            openFileDialog.Filter = "Nastran file(*.op2)|*.op2|ABAQUS file(*.fil)|*.fil|ABAQUS file(*.odb)|*.odb|All files (*.*)|*.*"
            openFileDialog.FilterIndex = 1
            openFileDialog.RestoreDirectory = True

            If openFileDialog.ShowDialog() = DialogResult.OK Then
                resultsFile = openFileDialog.FileName()

            End If

        Catch E As Exception
            theNXMessageBox.Show("Processing Results", NXMessageBox.DialogType.Error, E.Message)
        End Try

        Return resultsFile

    End Function

    Function GetImportedResults(ByRef file As String) As CAE.Result

        Dim results As CAE.Result = Nothing

        Dim part As BasePart = theSession.Parts.BaseWork

        Dim theResultManager As CAE.ResultManager = theSession.ResultManager()

        If (theResultManager Is Nothing) Then
            theNXMessageBox.Show("Processing Results 7", NXMessageBox.DialogType.Error, "No valid ResultManager")
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

        Dim importedResults As CAE.ImportedResult = theResultManager.CreateImportedResult(file, unitSystem)
        If (importedResults Is Nothing) Then
            theNXMessageBox.Show("Processing Results 8", NXMessageBox.DialogType.Error, "Could not Access Solution Results")
            Return Nothing
        End If

        results = CType(importedResults, CAE.Result)

        Return results

    End Function

    Function GetResultAccess(ByRef results As CAE.Result, ByVal resultType As CAE.Result.Type, ByVal component As CAE.Result.Component, ByVal loadCaseIdx As Integer, ByVal iterationIdx As Integer, ByVal scale As Double) As CAE.ResultAccess

        Dim part As BasePart = theSession.Parts.BaseWork

        Dim theResultManager As CAE.ResultManager = theSession.ResultManager()

        If (theResultManager Is Nothing) Then
            theNXMessageBox.Show("Processing Results", NXMessageBox.DialogType.Error, "No valid ResultManager")
            Return Nothing
        End If

        Dim unit_length As Unit = Nothing
        If part.PartUnits() = BasePart.Units.Millimeters Then
            unit_length = CType(part.UnitCollection.FindObject("MilliMeter"), Unit)
        Else
            unit_length = CType(part.UnitCollection.FindObject("Inch"), Unit)
        End If

        Dim averaging As CAE.Result.Averaging
        averaging.DoAveraging = False
        averaging.AverageAcrossPropertyIds = True
        averaging.AverageAcrossMaterialIds = True
        averaging.AverageAcrossElementTypes = True
        averaging.AverageAcrossFeatangle = True
        averaging.AverageAcrossAnglevalue = 45.0
        averaging.IncludeInternalElementContributions = True

        Dim resultParameter As CAE.ResultParameters = theResultManager.CreateResultParameters()
        resultParameter.SetLoadcaseIteration(loadCaseIdx, iterationIdx)
        resultParameter.SetResultType(resultType)
        resultParameter.SetResultComponent(component)
        resultParameter.SetScale(scale)
        resultParameter.SetUnit(unit_length)

        ' Not sure if the rest are needed
        resultParameter.SetSectionPlyLayer(0, 0, 0)
        resultParameter.SetAveragingCriteria(averaging)
        resultParameter.SetCoordinateSystem(CAE.Result.CoordinateSystem.AbsoluteRectangular)
        resultParameter.SetElementValueCriterion(CAE.Result.ElementValueCriterion.Average)
        resultParameter.SetComplexCriterion(CAE.Result.Complex.Amplitude)
        resultParameter.SetPhaseAngle(0.0)

        Dim solResultsAccess As CAE.ResultAccess = theResultManager.CreateResultAccess(results, resultParameter)

        If (solResultsAccess Is Nothing) Then
            theNXMessageBox.Show("Processing Results", NXMessageBox.DialogType.Error, "Could not create Results Access Object for Solution results")
            Return Nothing
        End If

        solResultsAccess.SetParameters(resultParameter)

        Return solResultsAccess

    End Function

    Function GetUnvResultType()

        Dim iType As Integer = 94

        Select Case resultType.Quantity
            Case CAE.Result.Quantity.Stress
                iType = 2
            Case CAE.Result.Quantity.Strain
                iType = 3
            Case CAE.Result.Quantity.ElementForce
                iType = 4
            Case CAE.Result.Quantity.Temperature
                iType = 5
            Case CAE.Result.Quantity.HeatFlux
                iType = 6
            Case CAE.Result.Quantity.StrainEnergy
                iType = 7
            Case CAE.Result.Quantity.Displacement
                iType = 8
            Case CAE.Result.Quantity.Rotation
                iType = 8
            Case CAE.Result.Quantity.ReactionForce
                iType = 9
            Case CAE.Result.Quantity.ShellResultants
                iType = 27
            Case Else
                iType = 94
        End Select

        If (DEBUG) Then theLW.WriteLine(vbNewLine + "Result Type: " + resultType.Quantity.ToString + " UNV type set to: " + iType.ToString + vbNewLine)

        Return iType

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

    Public Structure nodalEnvelope
        Dim nodeId As Integer
        Dim maxVal As Double
        Dim maxLc As Integer
        Dim minVal As Double
        Dim minLc As Integer
        Dim absVal As Double
        Dim absLc As Integer
    End Structure

    Public Structure elemEnvelope
        Dim elemId As Integer
        Dim maxVal As Double
        Dim maxLc As Integer
        Dim minVal As Double
        Dim minLc As Integer
        Dim absVal As Double
        Dim absLc As Integer
    End Structure

    Public Structure elemNodalEnvelope
        Dim elemId As Integer
        Dim nodes() As nodalEnvelope
    End Structure

    '------------------------------------------------------------------------------
    'Represents Block Styler application class
    '------------------------------------------------------------------------------
    Public Class envelopeResults
        'class members (from Block Styler)
        Private Shared theSession As Session
        Private Shared theUI As UI
        Public Shared theenvelopeResults As envelopeResults
        Private theDialogName As String
        Private theDialog As NXOpen.BlockStyler.BlockDialog
        Private group0 As NXOpen.BlockStyler.UIBlock ' Block type: Group
        Private list_box0 As NXOpen.BlockStyler.ListBox ' Block type: List Box
        Private enum0 As NXOpen.BlockStyler.UIBlock ' Block type: Enumeration
        Private enum01 As NXOpen.BlockStyler.UIBlock ' Block type: Enumeration
        'class members (user defined)
        Public resultTypes() As CAE.Result.Type
        Public components() As CAE.Result.Component


#Region "Block Styler Dialog Designer generator code"
        '------------------------------------------------------------------------------
        'Constructor for NX Styler class
        '------------------------------------------------------------------------------
        Public Sub New()
            Try

                theSession = Session.GetSession()
                theUI = UI.GetUI()
                theDialogName = "envelopeResults.dlx"
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
#End Region

        '------------------------------- DIALOG LAUNCHING ---------------------------------
        '
        '    Before invoking this application one needs to open any part/empty part in NX
        '    because of the behavior of the blocks.
        '
        '    Make sure the dlx file is in one of the following locations:
        '        1.) From where NX session is launched
        '        2.) $UGII_USER_DIR/application
        '        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        '            recommended. This variable is set to a full directory path to a file 
        '            containing a list of root directories for all custom applications.
        '            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_ROOT_DIR\menus\custom_dirs.dat
        '
        '    You can create the dialog using one of the following way:
        '
        '    1. Journal Replay
        '
        '        1) Replay this file through Tool->Journal->Play Menu.
        '
        '    2. USER EXIT
        '
        '        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
        '        2) Invoke the Shared Library through File->Execute->NX Open menu.
        '
        '------------------------------------------------------------------------------
        Public Shared Sub Main()
            Try

                theenvelopeResults = New envelopeResults()
                ' The following method shows the dialog immediately
                theenvelopeResults.Show()

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            Finally
                theenvelopeResults.Dispose()
            End Try
        End Sub
        '------------------------------------------------------------------------------
        ' This method specifies how a shared image is unloaded from memory
        ' within NX. This method gives you the capability to unload an
        ' internal NX Open application or user  exit from NX. Specify any
        ' one of the three constants as a return value to determine the type
        ' of unload to perform:
        '
        '
        '    Immediately : unload the library as soon as the automation program has completed
        '    Explicitly  : unload the library from the "Unload Shared Image" dialog
        '    AtTermination : unload the library when the NX session terminates
        '
        '
        ' NOTE:  A program which associates NX Open applications with the menubar
        ' MUST NOT use this option since it will UNLOAD your NX Open application image
        ' from the menubar.
        '------------------------------------------------------------------------------
        Public Shared Function GetUnloadOption(ByVal arg As String) As Integer
            'Return CType(Session.LibraryUnloadOption.Explicitly, Integer)
            Return CType(Session.LibraryUnloadOption.Immediately, Integer)
            ' Return CType(Session.LibraryUnloadOption.AtTermination, Integer)
        End Function
        '------------------------------------------------------------------------------
        ' Following method cleanup any housekeeping chores that may be needed.
        ' This method is automatically called by NX.
        '------------------------------------------------------------------------------
        Public Shared Function UnloadLibrary(ByVal arg As String) As Integer
            Try

                Return 0

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
        End Function

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
                list_box0 = CType(theDialog.TopBlock.FindBlock("list_box0"), NXOpen.BlockStyler.ListBox)
                enum0 = theDialog.TopBlock.FindBlock("enum0")
                enum01 = theDialog.TopBlock.FindBlock("enum01")

                ' Set the property lists
                Dim propertyList As BlockStyler.PropertyList = Nothing

                loadCases = results.AskLoadcases

                propertyList = list_box0.GetProperties
                propertyList.SetInteger("Height", 10)
                propertyList.SetStrings("ListItems", loadCases)
                propertyList.SetIntegerVector("SelectedItems", iSelectedCases)
                propertyList.Dispose()

                Dim resultTypeDesc() As String = Nothing
                getResultsType(resultTypes, resultTypeDesc)

                propertyList = enum0.GetProperties
                propertyList.SetEnumMembers("Value", resultTypeDesc)
                propertyList.Dispose()

                Dim componentNames() As String = Nothing
                getComponent(resultTypes(0), iSelectedCases(0), components, componentNames)

                propertyList = enum01.GetProperties
                propertyList.SetEnumMembers("Value", componentNames)
                propertyList.Dispose()

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

                '---- Enter your callback code here -----

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

                '---- Enter your callback code here -----
                group0 = theDialog.TopBlock.FindBlock("group0")
                list_box0 = CType(theDialog.TopBlock.FindBlock("list_box0"), NXOpen.BlockStyler.ListBox)
                enum0 = theDialog.TopBlock.FindBlock("enum0")
                enum01 = theDialog.TopBlock.FindBlock("enum01")

                Dim propertyList As BlockStyler.PropertyList = Nothing

                propertyList = list_box0.GetProperties
                iSelectedCases = propertyList.GetIntegerVector("SelectedItems")
                propertyList.Dispose()

                propertyList = enum0.GetProperties
                Dim resultIdx As Integer = propertyList.GetEnum("Value")
                propertyList.Dispose()

                propertyList = enum01.GetProperties
                Dim componentIdx As Integer = propertyList.GetEnum("Value")
                propertyList.Dispose()

                resultType = resultTypes(resultIdx)
                component = components(componentIdx)

                DoIt()

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

                group0 = theDialog.TopBlock.FindBlock("group0")
                list_box0 = CType(theDialog.TopBlock.FindBlock("list_box0"), NXOpen.BlockStyler.ListBox)
                enum0 = theDialog.TopBlock.FindBlock("enum0")
                enum01 = theDialog.TopBlock.FindBlock("enum01")

                Dim propertyList As BlockStyler.PropertyList = Nothing

                If block Is list_box0 Then
                    '---- Enter your code here -----
                    propertyList = list_box0.GetProperties
                    iSelectedCases = propertyList.GetIntegerVector("SelectedItems")
                    propertyList.Dispose()

                    Dim resultTypeDesc() As String = Nothing
                    getResultsType(resultTypes, resultTypeDesc)

                    propertyList = enum0.GetProperties
                    propertyList.SetEnumMembers("Value", resultTypeDesc)
                    propertyList.Dispose()

                    Dim componentNames() As String = Nothing
                    getComponent(resultTypes(0), iSelectedCases(0), components, componentNames)

                    propertyList = enum01.GetProperties
                    propertyList.SetEnumMembers("Value", componentNames)
                    propertyList.Dispose()

                ElseIf block Is enum0 Then
                    '---- Enter your code here -----
                    propertyList = list_box0.GetProperties
                    iSelectedCases = propertyList.GetIntegerVector("SelectedItems")
                    propertyList.Dispose()

                    Dim resultTypeDesc() As String = Nothing
                    getResultsType(resultTypes, resultTypeDesc)

                    propertyList = enum0.GetProperties
                    Dim resultIdx As Integer = propertyList.GetEnum("Value")
                    propertyList.Dispose()

                    Dim componentNames() As String = Nothing
                    getComponent(resultTypes(resultIdx), iSelectedCases(0), components, componentNames)

                    propertyList = enum01.GetProperties
                    propertyList.SetEnumMembers("Value", componentNames)
                    propertyList.Dispose()

                ElseIf block Is enum01 Then
                    '---- Enter your code here -----

                End If

                'propertyList.Dispose()

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

                '---- Enter your callback code here -----
                apply_cb()

            Catch ex As Exception

                '---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
            End Try
            ok_cb = 0
        End Function

    End Class
End Module
