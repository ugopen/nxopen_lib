' CampbellCsvToAfu.vb - Import Campbell .csv file to .afu file
'
' 
'

Option Strict Off
Imports System
Imports System.IO
Imports System.Collections
Imports System.Globalization
Imports System.Windows.Forms

Imports NXOpen
Imports NXOpenUI

Module Module1

    Dim theSession As Session = Session.GetSession()
    Dim lw As ListingWindow = theSession.ListingWindow

    ' The csv file written by NX Nastran is written in the english number format "en-US", 
    ' where the "." (period) is used for the decimal symbol and the "," (comma) for list separator
    ' so we define this Globalization class to handle converting these number in locales that may
    ' have other number formats.
    Dim nfi As Globalization.NumberFormatInfo = New Globalization.CultureInfo("en-US", False).NumberFormat

    Sub Main()

        lw.Open()

        ' Get .csv file to process
        Dim openFileDialog As New OpenFileDialog
        openFileDialog.Filter = "csv files (*.csv)|*.csv|All Files (*.*)|*.*"
        openFileDialog.FilterIndex = 1
        openFileDialog.Title = "Select NX Nastran Rotordynamics .csv Output File"
        openFileDialog.InitialDirectory = theSession.Parts.BaseDisplay.FullPath
        openFileDialog.CheckFileExists = True

        If openFileDialog.ShowDialog = DialogResult.OK Then

            Dim csvFile As String = openFileDialog.FileName

            ' Generate afu filename
            Dim afuFile As String = Left(csvFile, InStrRev(csvFile, ".")) + "afu"

            ' Check to see if file exists. If it does, prompt to delete it
            If (File.Exists(afuFile)) Then

                Dim title As String = "File Exists"
                Dim message As String = "AFU File " + afuFile + " already exists." + vbNewLine + vbNewLine + "OK to delete?"
                Dim result As MsgBoxResult = MsgBox(message, MsgBoxStyle.OkCancel, title)

                If (result = MsgBoxResult.Ok) Then
                    theSession.AfuManager.DeleteAfuFile(afuFile)
                Else
                    Return
                End If

            End If

            ' Create the afu file
            theSession.AfuManager.CreateNewAfuFile(afuFile)
            lw.WriteLine("Creating AFU File: " + afuFile)

            parseData(csvFile, afuFile)

        End If

    End Sub

    Sub parseData(ByVal csvFile As String, ByVal afuFile As String)

        Dim csvData() As String = System.IO.File.ReadAllLines(csvFile)
        Dim csvIdx As Integer = 0

        Dim values() As String

        ' Find start of RPM data
        Do
            values = Split(csvData(csvIdx), ",")
            csvIdx += 1
        Loop Until values(0) = "        10001"

        ' Get RPM Data
        Dim rpmList As New ArrayList()
        Do
            values = Split(csvData(csvIdx), ",")
            csvIdx += 1
            rpmList.Add(Trim(values(0)))
        Loop Until (Left(values(0), 6) = "      ")

        csvIdx -= 1
        rpmList.RemoveAt(rpmList.Count - 1)

        Dim rpmCount As Integer = rpmList.Count

        Dim rpmData(rpmCount - 1) As Double
        For rpmIdx As Integer = 0 To rpmCount - 1
            rpmData(rpmIdx) = Convert.ToDouble(rpmList.Item(rpmIdx), nfi)
        Next

        lw.WriteLine(vbNewLine + "Data stored for " + rpmCount.ToString + " RPM values" + vbNewLine + vbNewLine)

        createPerRevLine(afuFile, rpmData, 1.0)
        createPerRevLine(afuFile, rpmData, 2.0)

        lw.WriteLine(vbNewLine)

        ' Loop through the rest of the data
        Dim data(rpmCount - 1)() As String

        Do
            Dim labels() As String = Split(csvData(csvIdx), ",")
            csvIdx += 1

            Dim Idx As Integer = 0
            For i As Integer = csvIdx To csvIdx + rpmCount - 1
                Dim temp() As String = Split(csvData(i), ",")
                data(Idx) = Split(csvData(i), ",")
                Idx += 1
            Next

            Dim yValues(rpmCount) As Double
            For j As Integer = 0 To labels.Length - 2
                For i As Integer = 0 To rpmCount - 1
                    yValues(i) = Convert.ToDouble(data(i)(j), nfi)
                Next

                Dim recName As String = Trim(labels(j))

                If (recName <> 50000 And recName <> 70000) Then

                    Select Case Left(recName, 1)
                        Case 2
                            recName += "-Eigenfrequency"
                        Case 3
                            recName += "-Damping_Values"
                        Case 4
                            recName += "-Real_Part"
                        Case 5
                            recName += "-Whirl_Direction"
                        Case 6
                            recName += "-Converted_Eigenfrequency"
                        Case 7
                            recName += "-Converted_Whirl_Direction"
                    End Select

                    lw.WriteLine("Creating record " + recName)
                    createAfuRecord(afuFile, recName, rpmData, yValues)

                End If

            Next

            csvIdx += rpmCount
        Loop Until csvIdx >= csvData.Length

    End Sub

    Sub createPerRevLine(ByVal afuFile As String, ByVal rpm() As Double, ByVal scale As Double)

        Dim ordData(rpm.Length - 1) As Double

        ' Generate 1P and 2P lines
        For rpmIdx As Integer = 0 To rpm.Length - 1
            ordData(rpmIdx) = rpm(rpmIdx) / 60 * scale
        Next

        ' Create 1P and 2P records in AFU
        Dim recordName As String = scale.ToString + "P"
        createAfuRecord(afuFile, recordName, rpm, ordData)

        lw.WriteLine(recordName + " line generated")

    End Sub

    Sub createAfuRecord(ByVal afuFile As String, ByVal recordName As String, ByVal abscissaData() As Double, ByVal ordinateData() As Double)

        Dim afuData1 As CAE.AfuData
        afuData1 = theSession.AfuManager.CreateAfuData()

        afuData1.FileName = afuFile
        afuData1.RecordName = recordName
        afuData1.SetIdInformation("x+", 1, "x+", 1)
        afuData1.SetAxisDefinition(CAE.AfuData.AbscissaType.Uneven, CAE.XyFunctionUnit.RpmRpm, CAE.AfuData.OrdinateType.Real, CAE.XyFunctionUnit.FrequencyHz)
        afuData1.SetRealData(abscissaData, ordinateData)

        Dim createTime1 As String
        createTime1 = theSession.AfuManager.CreateRecord(CAE.XyFunctionMacroType.General, CAE.XyFunctionGeneralType.CampbellDiagram, afuData1)

        afuData1.Dispose()

    End Sub

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

End Module

