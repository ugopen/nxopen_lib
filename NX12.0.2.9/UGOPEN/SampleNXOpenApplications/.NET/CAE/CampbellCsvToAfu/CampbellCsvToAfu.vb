' CampbellCsvToAfu.vb - Import Campbell .csv file to .afu file
'
' 
'
'   Description:
'   This program is used to import Campbell diagram data from a .csv file generated
'   by a NX Nastran Rotordynamics solution.
'
'   MODTRK=1:
'    - Due to limitations with Nastran OP4 formatting, Campbell diagram data
'   is written from NX Nastran to the .csv file 7 columns at a time. The 
'   NX Function Toolkit can import a .csv file into an .afu file, but it
'   expects that all data for each RPM is on the same row. This program
'   will read the OUTPUT4 .csv file, reformat the data and import it into
'   an .afu file. The records will be named using the column header in
'   the .csv file
'
'    - Records for the 1P and 2P lines may also be generated. 
'
'   MODTRK=2/3:
'    - Updated format containing 10 columns of data for each mode
'
'   The user will be prompted to select the .csv results file and the
'   units for the ordinate and abscissa via a Block Styler dialog
'
'   The .afu output file will be named the same as the .csv input file
'
'   This program can be executed in a fem or sim part.
' 
' 
'
'   Instructions:
'   1) A copy of CampbellCsvToAfu.dlx must be in one of the following locations:
'        1.) In the same folder as CampbellCsvToAfu.vb
'        2.) From where NX session is launched
'        3.) $UGII_USER_DIR/application
'        4.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
'            recommended. This variable is set to a full directory path to a file 
'            containing a list of root directories for all custom applications.
'            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
'
'   2) Run this program from within a FEM or SIM file in NX Advanced Simulation
'      - Use 'Tools > Journal > Play' to run CampbellCsvToAfu.vb
'
'   3) The program will prompt for the existing .csv results file to use and the units of
'      the data in that file.
'
'   Known Issues:
'

Option Strict Off
Imports System
Imports System.IO
Imports System.Collections
Imports System.Collections.Generic
Imports System.Globalization

Imports NXOpen
Imports NXOpenUI
Imports NXOpen.BlockStyler

Module CampbellCsvToAfu

    Public theSession As Session = Session.GetSession()
    Public lw As ListingWindow = theSession.ListingWindow

    Public theUI As UI = UI.GetUI
    Public theNXMessageBox As NXMessageBox = theUI.NXMessageBox
    Public theNXMessageBoxTitle As String = "Campbell CSV to AFU"

    ' The csv file written by NX Nastran is written in the english number format "en-US", 
    ' where the "." (period) is used for the decimal symbol and the "," (comma) for list separator
    ' so we define this Globalization class to handle converting to this format in locales that may
    ' have other number formats.
    Dim nfi As Globalization.NumberFormatInfo = New Globalization.CultureInfo("en-US", False).NumberFormat

    Public freqUnits As New Dictionary(Of String, Integer)

    Dim whirlDir As New Dictionary(Of Integer, String)
    Dim perRevRecordNames As New Dictionary(Of Integer, String)
    Dim csvColNames As New Dictionary(Of Integer, String)

    Dim afuFunctionType As New Dictionary(Of Integer, CAE.XyFunctionGeneralType)
    Dim xUnit As CAE.XyFunctionUnit
    Dim afuYunit As New Dictionary(Of Integer, CAE.XyFunctionUnit)

    Sub Main()

        ' Check that work part is a CAE part
        Dim basePart As BasePart = theSession.Parts.BaseWork

        If (basePart Is Nothing Or Not (TypeOf basePart Is CAE.BaseFemPart Or TypeOf basePart Is CAE.SimPart)) Then
            theNXMessageBox.Show(theNXMessageBoxTitle, NXMessageBox.DialogType.Error, "Must be running in Simulation")
            Return
        End If

        ' Populate the frequency units list
        freqUnits.Add("RPM", CAE.XyFunctionUnit.RpmRpm)
        freqUnits.Add("CPS", CAE.XyFunctionUnit.FrequencyHz)
        freqUnits.Add("HZ", CAE.XyFunctionUnit.FrequencyHz)
        freqUnits.Add("RAD", CAE.XyFunctionUnit.UnitlessRealNone)

        ' Populate the whirl direction list
        whirlDir.Add(2, "Backward")
        whirlDir.Add(3, "Forward")
        whirlDir.Add(4, "Linear")

        ' Populate the per rev record name list
        perRevRecordNames.Add(0, "0_P")
        perRevRecordNames.Add(1, "1_P-Fixed")
        perRevRecordNames.Add(2, "2_P-Rotating")
        perRevRecordNames.Add(3, "3_P")
        perRevRecordNames.Add(4, "4_P")
        perRevRecordNames.Add(5, "5_P")

        ' Populate the column name, function type and units lists
        ' Undefined units will be set to the user specified unit (selected
        '   via the block styler dialog)
        csvColNames.Add(2, "-Eigenfrequency")
        afuFunctionType.Add(2, CAE.XyFunctionGeneralType.CampbellDiagram)

        csvColNames.Add(3, "-Damping_Values")
        afuFunctionType.Add(3, CAE.XyFunctionGeneralType.General)
        afuYunit.Add(3, CAE.XyFunctionUnit.Unknown)

        csvColNames.Add(4, "-Real_Part")
        afuFunctionType.Add(4, CAE.XyFunctionGeneralType.General)

        csvColNames.Add(5, "-Imag_Part")
        afuFunctionType.Add(5, CAE.XyFunctionGeneralType.General)

        csvColNames.Add(6, "-Whirl_Dir")
        afuFunctionType.Add(6, CAE.XyFunctionGeneralType.General)
        afuYunit.Add(6, CAE.XyFunctionUnit.UnitlessIntegerNone)

        csvColNames.Add(7, "-Conv_Eigenfrequency")
        afuFunctionType.Add(7, CAE.XyFunctionGeneralType.CampbellDiagram)

        csvColNames.Add(8, "-Conv_Whirl_Dir")
        afuFunctionType.Add(8, CAE.XyFunctionGeneralType.General)
        afuYunit.Add(8, CAE.XyFunctionUnit.UnitlessIntegerNone)

        csvColNames.Add(9, "-Conv_Imag_Part")
        afuFunctionType.Add(9, CAE.XyFunctionGeneralType.General)

        csvColNames.Add(10, "-Conv_Real_Part")
        afuFunctionType.Add(10, CAE.XyFunctionGeneralType.General)


        ' Launch the dialog
        CampbellCsvToAfu_BS.Main()

    End Sub

    Sub doIt()

        lw.Open()

        Dim csvFile As String = CampbellCsvToAfu_BS.csvFile
        lw.WriteLine("Input CSV File:  " + csvFile)

        ''Dim afuFile As String = CampbellCsvToAfu_BS.afuFile
        Dim afuFile As String = IO.Path.ChangeExtension(csvFile, ".afu")

        ' Check to see if file exists. If it does, prompt to delete it
        If (File.Exists(afuFile)) Then

            Dim title As String = "AFU File Exists"
            Dim message As String = "AFU File " + afuFile + " already exists." + vbNewLine + vbNewLine _
                                  + "YES to delete and create new file" + vbNewLine _
                                  + "NO to append records to existing file"

            Dim result As Integer = theUI.NXMessageBox.Show(title, NXMessageBox.DialogType.Question, message)

            If (result = 1) Then
                ' Delete the existing file
                theSession.AfuManager.DeleteAfuFile(afuFile)
                ' Create the new file
                theSession.AfuManager.CreateNewAfuFile(afuFile)
                lw.WriteLine("Overwriting existing AFU File: " + afuFile)

            Else
                lw.WriteLine("Appending to existing AFU File: " + afuFile)
            End If

        Else

            lw.WriteLine("Output AFU File: " + afuFile)

        End If

        ' Get the frequency and RPM units
        Dim xUnitName As String = CampbellCsvToAfu_BS.rUnit
        Dim yUnitName As String = CampbellCsvToAfu_BS.fUnit

        xUnit = freqUnits.Item(xUnitName)
        Dim yUnit As CAE.XyFunctionUnit = freqUnits.Item(yUnitName)

        For i As Integer = 2 To 10
            If Not afuYunit.ContainsKey(i) Then afuYunit.Add(i, yUnit)
        Next i

        lw.WriteLine(vbNewLine + "RPM Units:        " + xUnitName)
        lw.WriteLine("Frequency Units:  " + yUnitName)

        lw.WriteLine(vbNewLine)
        If CampbellCsvToAfu_BS.solOutputFilter Then
            lw.WriteLine("Selected Solutions: All")
        Else
            Dim solString As String = Nothing
            For Each iSol As Integer In CampbellCsvToAfu_BS.solOutputList
                solString += " " + iSol.ToString
            Next iSol
            lw.WriteLine("Selected Solutions: " + solString)
        End If

        ' Determine the mode tracking format of the csv file
        Dim reader As FileIO.TextFieldParser = My.Computer.FileSystem.OpenTextFieldParser(csvFile)

        Do Until reader.EndOfData

            Dim modtrk1Flag As String = reader.PeekChars(13).Trim
            Dim modtrk2Flag As String = reader.PeekChars(4)

            If modtrk1Flag = "10001" Then

                lw.WriteLine(vbNewLine + "Data format: MODTRK=1")
                reader.Dispose()
                parseModtrk1Data(csvFile, afuFile)

            ElseIf modtrk2Flag = "data" Then

                lw.WriteLine(vbNewLine + "Data format: MODTRK=2/3" + vbNewLine + vbNewLine)

                ' Parse the data
                Dim csvData As New SortedList(Of Integer, SortedList(Of Integer, List(Of Double)))(parseModtrk2Data(reader, csvFile, afuFile))

                ' Write records to the AFU file
                storeModtrk2Data(afuFile, csvFile, csvData)

            Else

                reader.ReadLine()

            End If

        Loop

        reader.Dispose()

        lw.WriteLine(vbNewLine + "Processing complete")

    End Sub

    Sub parseModtrk1Data(ByVal csvFile As String, ByVal afuFile As String)

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

        ' Create the per-rev lines
        For Each iOrder As Integer In CampbellCsvToAfu_BS.perRevOutputList
            createPerRevLine(afuFile, rpmData, iOrder)
        Next iOrder
        If CampbellCsvToAfu_BS.perRevOutputList.Count > 0 Then lw.WriteLine(vbNewLine)

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

                    Dim afuIdLines(3) As String
                    afuIdLines(0) = csvFile

                    Dim iDataType As Integer = Integer.Parse(Left(recName, 1))

                    Dim iSolId As Integer = Integer.Parse(recName) - iDataType * 10000

                    Select Case iDataType

                        Case 5, 6, 7
                            iDataType += 1

                    End Select

                    recName += csvColNames(iDataType)
                    If CampbellCsvToAfu_BS.outputOptions.Contains(iDataType) And _
                       (CampbellCsvToAfu_BS.solOutputFilter Or CampbellCsvToAfu_BS.solOutputList.Contains(iSolId)) Then

                        createAfuRecord(afuFile, afuIdLines, recName, afuFunctionType(iDataType), _
                                        rpmData, xUnit, yValues, afuYunit(iDataType))

                    End If

                End If

            Next

            csvIdx += rpmCount

        Loop Until csvIdx >= csvData.Length

    End Sub

    Function parseModtrk2Data(ByVal reader As FileIO.TextFieldParser, ByVal csvFileName As String, ByVal afuFileName As String) As SortedList(Of Integer, SortedList(Of Integer, List(Of Double)))

        reader.TextFieldType = FileIO.FieldType.Delimited
        reader.Delimiters = New String() {","}
        reader.CommentTokens = New String() {"$"}
        reader.TrimWhiteSpace = True

        Dim iSolId As Integer = 0

        Dim csvData As New SortedList(Of Integer, SortedList(Of Integer, List(Of Double)))

        Do

            Try
                Do

                    Dim currentRow As New List(Of String)(reader.ReadFields)

                    ' Remove trailing blank fields
                    For i As Integer = currentRow.Count - 1 To 0 Step -1
                        If currentRow(i) = "" Then
                            currentRow.RemoveAt(i)
                        Else
                            Exit For
                        End If
                    Next i

                    If currentRow(0).Contains("data") Then

                        Dim iColId As Integer = Convert.ToInt32(currentRow(0).Substring(4))

                        iSolId = (iColId - 10001) / 10

                        If csvData.ContainsKey(iSolId) Then
                            theNXMessageBox.Show(theNXMessageBoxTitle, NXMessageBox.DialogType.Error, _
                                                 "Duplicate column ID's exist: " + iColId.ToString + vbNewLine + _
                                                 "First duplicate at line " + (reader.LineNumber - 1).ToString)
                            Exit Do
                        Else
                            csvData.Add(iSolId, New SortedList(Of Integer, List(Of Double)))
                        End If

                    Else

                        For iCol As Integer = 0 To currentRow.Count - 1

                            Dim iColId As Integer = iCol + 1
                            If iSolId = -100 Then iColId -= 1

                            If Not csvData(iSolId).ContainsKey(iColId) Then csvData(iSolId).Add(iColId, New List(Of Double))

                            csvData(iSolId)(iColId).Add(Convert.ToDouble(currentRow(iCol), nfi))

                        Next iCol

                    End If

                Loop Until reader.PeekChars(4) = "data" Or reader.EndOfData

            Catch ex As FileIO.MalformedLineException
                MsgBox("Line " & ex.Message & "is not valid and will be skipped.")
            End Try

        Loop Until reader.EndOfData

        reader.Dispose()

        Return csvData

    End Function

    Sub storeModtrk2Data(ByVal afuFileName As String, ByVal csvFileName As String, _
                         ByVal functionData As SortedList(Of Integer, SortedList(Of Integer, List(Of Double))))

        ' Properties common to all records
        Dim afuIdLines(3) As String
        afuIdLines(0) = csvFileName

        ' Write per-rev lines if requested
        For Each iOrder As Integer In CampbellCsvToAfu_BS.perRevOutputList

            If iOrder = 0 Then

                ' Generate a 0.0 Y value for every X value
                Dim yValList As New List(Of Double)
                For Each xVal As Double In functionData(-100)(0)
                    yValList.Add(0.0)
                Next xVal

                createAfuRecord(afuFileName, afuIdLines, perRevRecordNames(iOrder), afuFunctionType(2), _
                     functionData(-100)(0).ToArray, xUnit, _
                     yValList.ToArray, afuYunit(2))

            Else

                createAfuRecord(afuFileName, afuIdLines, perRevRecordNames(iOrder), afuFunctionType(2), _
                                functionData(-100)(0).ToArray, xUnit, _
                                functionData(-100)(iOrder).ToArray, afuYunit(2))

            End If

        Next iOrder


        ' Remove the per rev lines from the data
        functionData.Remove(-100)

        ' Write solution data
        For Each iCol As Integer In CampbellCsvToAfu_BS.outputOptions

            For Each iSolId As Integer In functionData.Keys

                If CampbellCsvToAfu_BS.solOutputFilter Or CampbellCsvToAfu_BS.solOutputList.Contains(iSolId) Then

                    ' Average the whirl direction across all RPM's for this solution
                    Dim iWhirlDir As Integer = Math.Round(arrayAverage(functionData(iSolId)(6).ToArray))

                    afuIdLines(1) = whirlDir.Item(iWhirlDir)

                    Dim recordName As String = "SOL_" + iSolId.ToString + csvColNames(iCol)

                    createAfuRecord(afuFileName, afuIdLines, recordName, afuFunctionType(iCol), _
                                    functionData(iSolId)(1).ToArray, xUnit, _
                                    functionData(iSolId)(iCol).ToArray, afuYunit(iCol))

                End If

            Next iSolId

        Next iCol

    End Sub

    Function arrayAverage(ByVal values() As Double) As Double

        Dim sum As Double = 0.0

        For Each value As Double In values
            sum += value
        Next value

        Dim average As Double = sum / values.Length

        Return average

    End Function

    Sub createPerRevLine(ByVal afuFile As String, ByVal rpm() As Double, ByVal iOrder As Integer)

        Dim xUnit As CAE.XyFunctionUnit = freqUnits.Item(CampbellCsvToAfu_BS.rUnit)
        Dim yUnit As CAE.XyFunctionUnit = freqUnits.Item(CampbellCsvToAfu_BS.fUnit)

        Dim rUnit_to_fUnit As Double = 60

        If xUnit.CompareTo(yUnit) = 0 Then
            rUnit_to_fUnit = 1.0
        End If

        Dim absData() As Double = {0.0, rpm(rpm.Length - 1)}
        Dim ordData() As Double = {0.0, rpm(rpm.Length - 1) / rUnit_to_fUnit * iOrder}

        Dim afuIdLines(3) As String

        createAfuRecord(afuFile, afuIdLines, perRevRecordNames(iOrder), CAE.XyFunctionGeneralType.CampbellDiagram, absData, xUnit, ordData, yUnit)

        lw.WriteLine(perRevRecordNames(iOrder) + " line generated")

    End Sub

    Sub createAfuRecord(ByVal afuFile As String, ByVal idLines() As String, ByVal recordName As String, ByVal fType As CAE.XyFunctionGeneralType, ByVal abscissaData() As Double, ByVal xUnit As CAE.XyFunctionUnit, ByVal ordinateData() As Double, ByVal yUnit As CAE.XyFunctionUnit)

        Dim iMaxIdStringLength As Integer = 79

        Dim afuHeaderId As CAE.AfuHeaderId = theSession.AfuManager.CreateAfuHeaderId

        If Not idLines(0) Is Nothing Then afuHeaderId.IdLine1 = Right(idLines(0), iMaxIdStringLength)
        If Not idLines(1) Is Nothing Then afuHeaderId.IdLine2 = Left(idLines(1), iMaxIdStringLength)
        If Not idLines(2) Is Nothing Then afuHeaderId.IdLine3 = Left(idLines(2), iMaxIdStringLength)
        If Not idLines(3) Is Nothing Then afuHeaderId.IdLine4 = Left(idLines(3), iMaxIdStringLength)

        afuHeaderId.Reference = "x+"
        afuHeaderId.ReferenceId = 1
        afuHeaderId.Response = "x+"
        afuHeaderId.ResponseId = 1

        Dim afuData1 As CAE.AfuData = theSession.AfuManager.CreateAfuData(CAE.AfuData.AbscissaType.Uneven)

        afuData1.FileName = afuFile
        afuData1.RecordName = recordName
        afuData1.AfuHeaderId = afuHeaderId
        afuData1.SetAbscissaAndOrdinateAxisDefinition(xUnit, CAE.AfuData.OrdinateType.Real, yUnit, CAE.XyFunctionUnit.Unknown)
        afuData1.SetRealData(abscissaData, ordinateData)

        Try

            Dim createTime1 As String = theSession.AfuManager.CreateRecord(CAE.XyFunctionMacroType.General, fType, afuData1)

        Catch ex As Exception

            If String.Compare(ex.Message, "This record already exists.") = 0 Then

                lw.WriteLine("*** Record " + recordName + " already exists")

                Dim currentTime As Date = Now

                afuData1.RecordName = recordName + "_" + currentTime.Hour.ToString + currentTime.Minute.ToString + currentTime.Second.ToString + currentTime.Millisecond.ToString

                Dim createTime1 As String = theSession.AfuManager.CreateRecord(CAE.XyFunctionMacroType.General, fType, afuData1)

            End If

        End Try

        lw.WriteLine("Creating record " + afuData1.RecordName)

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

'==============================================================================
'  WARNING!!  This file is overwritten by the Block UI Styler while generating
'  the automation code. Any modifications to this file will be lost after
'  generating the code again.
'
'       Filename:  D:\NX_Open\Campbell\application\CampbellCsvToAfu_BS.vb
'
'        This file was generated by the NX Block UI Styler
'        Created by: tsbernar
'              Version: NX 7.5
'              Date: 03-22-2013  (Format: mm-dd-yyyy)
'              Time: 17:13 (Format: hh-mm)
'
'==============================================================================

'==============================================================================
'  Purpose:  This TEMPLATE file contains VB.NET source to guide you in the
'  construction of your Block application dialog. The generation of your
'  dialog file (.dlx extension) is the first step towards dialog construction
'  within NX.  You must now create a NX Open application that
'  utilizes this file (.dlx).
'
'  The information in this file provides you with the following:
'
'  1.  Help on how to load and display your Block UI Styler dialog in NX
'      using APIs provided in NXOpen.BlockStyler namespace
'  2.  The empty callback methods (stubs) associated with your dialog items
'      have also been placed in this file. These empty methods have been
'      created simply to start you along with your coding requirements.
'      The method name, argument list and possible return values have already
'      been provided for you.
'==============================================================================

'------------------------------------------------------------------------------
'These imports are needed for the following template code
'------------------------------------------------------------------------------
''Option Strict Off
''Imports System
''Imports NXOpen
''Imports NXOpen.BlockStyler

'------------------------------------------------------------------------------
'Represents Block Styler application class
'------------------------------------------------------------------------------
Public Class CampbellCsvToAfu_BS
    'class members
    ''Private Shared theSession As Session
    ''Private Shared theUI As UI
    Public Shared theCampbellCsvToAfu_BS As CampbellCsvToAfu_BS

    Public Shared csvFile As String
    Public Shared fUnit As String
    Public Shared rUnit As String
    Public Shared afuFile As String
    Public Shared outputOptions As New List(Of Integer)
    Public Shared perRevOutputList As New List(Of Integer)
    Public Shared solOutputFilter As New Boolean
    Public Shared solOutputList As New List(Of Integer)

    Private theDialogName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private group0 As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private nativeFileBrowser0 As NXOpen.BlockStyler.UIBlock ' Block type: NativeFileBrowser
    Private group As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private enum0 As NXOpen.BlockStyler.UIBlock ' Block type: Enumeration
    Private enum01 As NXOpen.BlockStyler.UIBlock ' Block type: Enumeration
    Private group1 As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private group4 As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private toggle09 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle010 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle011 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle012 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle013 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle014 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private group5 As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private label0 As NXOpen.BlockStyler.UIBlock ' Block type: Label
    Private toggle0 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle01 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle02 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle03 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle04 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private separator0 As NXOpen.BlockStyler.UIBlock ' Block type: Separator
    Private label01 As NXOpen.BlockStyler.UIBlock ' Block type: Label
    Private toggle05 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle06 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle07 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private toggle08 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private separator01 As NXOpen.BlockStyler.UIBlock ' Block type: Separator
    Private label02 As NXOpen.BlockStyler.UIBlock ' Block type: Label
    Private group3 As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private toggle015 As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private string0 As NXOpen.BlockStyler.UIBlock ' Block type: String
    Private group2 As NXOpen.BlockStyler.UIBlock ' Block type: Group
    Private nativeFileBrowser01 As NXOpen.BlockStyler.UIBlock ' Block type: NativeFileBrowser

#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try

            ''theSession = Session.GetSession()
            ''theUI = UI.GetUI()

            theDialogName = IO.Path.ChangeExtension(theSession.ExecutingJournal, "dlx")

            If theDialogName = "" Then

                theDialogName = "CampbellCsvToAfu_BS.dlx"

            Else

                If Not IO.File.Exists(theDialogName) Then
                    theDialogName = "CampbellCsvToAfu.dlx"
                End If

            End If

            'theDialogName = "CampbellCsvToAfu_BS.dlx"

            theDialog = theUI.CreateDialog(theDialogName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddOkHandler(AddressOf ok_cb)
            theDialog.AddUpdateHandler(AddressOf update_cb)
            theDialog.AddInitializeHandler(AddressOf initialize_cb)
            theDialog.AddDialogShownHandler(AddressOf dialogShown_cb)

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)

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
    '            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
    '
    '    You can create the dialog using one of the following way:
    '
    '    1. Journal Replay
    '
    '        1) Replay this file through Tool->Journal->Play Menu.
    '
    '    2. USER EXIT
    '
    '        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
    '        2) Invoke the Shared Library through File->Execute->NX Open menu.
    '
    '------------------------------------------------------------------------------
    Public Shared Sub Main()
        Try

            theCampbellCsvToAfu_BS = New CampbellCsvToAfu_BS()
            ' The following method shows the dialog immediately
            theCampbellCsvToAfu_BS.Show()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            If theCampbellCsvToAfu_BS IsNot Nothing Then
                theCampbellCsvToAfu_BS.Dispose()
            End If
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
        Return 0
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
    '---------------------Block UI Styler Callback Functions--------------------------
    '------------------------------------------------------------------------------

    '------------------------------------------------------------------------------
    'Callback Name: initialize_cb
    '------------------------------------------------------------------------------
    Public Sub initialize_cb()
        Try

            group0 = CType(theDialog.TopBlock.FindBlock("group0"), NXOpen.BlockStyler.UIBlock)
            nativeFileBrowser0 = CType(theDialog.TopBlock.FindBlock("nativeFileBrowser0"), NXOpen.BlockStyler.UIBlock)
            group = CType(theDialog.TopBlock.FindBlock("group"), NXOpen.BlockStyler.UIBlock)
            enum0 = CType(theDialog.TopBlock.FindBlock("enum0"), NXOpen.BlockStyler.UIBlock)
            enum01 = CType(theDialog.TopBlock.FindBlock("enum01"), NXOpen.BlockStyler.UIBlock)
            group1 = CType(theDialog.TopBlock.FindBlock("group1"), NXOpen.BlockStyler.UIBlock)
            group4 = CType(theDialog.TopBlock.FindBlock("group4"), NXOpen.BlockStyler.UIBlock)
            toggle09 = CType(theDialog.TopBlock.FindBlock("toggle09"), NXOpen.BlockStyler.UIBlock)
            toggle010 = CType(theDialog.TopBlock.FindBlock("toggle010"), NXOpen.BlockStyler.UIBlock)
            toggle011 = CType(theDialog.TopBlock.FindBlock("toggle011"), NXOpen.BlockStyler.UIBlock)
            toggle012 = CType(theDialog.TopBlock.FindBlock("toggle012"), NXOpen.BlockStyler.UIBlock)
            toggle013 = CType(theDialog.TopBlock.FindBlock("toggle013"), NXOpen.BlockStyler.UIBlock)
            toggle014 = CType(theDialog.TopBlock.FindBlock("toggle014"), NXOpen.BlockStyler.UIBlock)
            group5 = CType(theDialog.TopBlock.FindBlock("group5"), NXOpen.BlockStyler.UIBlock)
            label0 = CType(theDialog.TopBlock.FindBlock("label0"), NXOpen.BlockStyler.UIBlock)
            toggle0 = CType(theDialog.TopBlock.FindBlock("toggle0"), NXOpen.BlockStyler.UIBlock)
            toggle01 = CType(theDialog.TopBlock.FindBlock("toggle01"), NXOpen.BlockStyler.UIBlock)
            toggle02 = CType(theDialog.TopBlock.FindBlock("toggle02"), NXOpen.BlockStyler.UIBlock)
            toggle03 = CType(theDialog.TopBlock.FindBlock("toggle03"), NXOpen.BlockStyler.UIBlock)
            toggle04 = CType(theDialog.TopBlock.FindBlock("toggle04"), NXOpen.BlockStyler.UIBlock)
            separator0 = CType(theDialog.TopBlock.FindBlock("separator0"), NXOpen.BlockStyler.UIBlock)
            label01 = CType(theDialog.TopBlock.FindBlock("label01"), NXOpen.BlockStyler.UIBlock)
            toggle05 = CType(theDialog.TopBlock.FindBlock("toggle05"), NXOpen.BlockStyler.UIBlock)
            toggle06 = CType(theDialog.TopBlock.FindBlock("toggle06"), NXOpen.BlockStyler.UIBlock)
            toggle07 = CType(theDialog.TopBlock.FindBlock("toggle07"), NXOpen.BlockStyler.UIBlock)
            toggle08 = CType(theDialog.TopBlock.FindBlock("toggle08"), NXOpen.BlockStyler.UIBlock)
            separator01 = CType(theDialog.TopBlock.FindBlock("separator01"), NXOpen.BlockStyler.UIBlock)
            label02 = CType(theDialog.TopBlock.FindBlock("label02"), NXOpen.BlockStyler.UIBlock)
            group3 = CType(theDialog.TopBlock.FindBlock("group3"), NXOpen.BlockStyler.UIBlock)
            toggle015 = CType(theDialog.TopBlock.FindBlock("toggle015"), NXOpen.BlockStyler.UIBlock)
            string0 = CType(theDialog.TopBlock.FindBlock("string0"), NXOpen.BlockStyler.UIBlock)
            group2 = CType(theDialog.TopBlock.FindBlock("group2"), NXOpen.BlockStyler.UIBlock)
            nativeFileBrowser01 = CType(theDialog.TopBlock.FindBlock("nativeFileBrowser01"), NXOpen.BlockStyler.UIBlock)

            theDialog.TopBlock.GetProperties.SetString("Label", "NXN Rotordynamics Plots")

            group0.GetProperties.SetString("Label", "Input File")

            nativeFileBrowser0.GetProperties.SetString("Label", "Nastran ROTCSV file")
            nativeFileBrowser0.GetProperties.SetString("Filter", "*.csv, *.txt, *.*")

            group.GetProperties.SetString("Label", "Axis Units")

            Dim unitList(freqUnits.Count - 1) As String
            freqUnits.Keys.CopyTo(unitList, 0)

            enum0.GetProperties.SetString("Label", "Rotor Speed (RUNIT)")
            enum0.GetProperties.SetEnumMembers("Value", unitList)
            enum0.GetProperties.SetEnumAsString("Value", "RPM")

            enum01.GetProperties.SetString("Label", "Freq. Output (FUNIT)")
            enum01.GetProperties.SetEnumMembers("Value", unitList)
            enum01.GetProperties.SetEnumAsString("Value", "HZ")

            group1.GetProperties.SetString("Label", "Output Options")

            group4.GetProperties.SetString("Label", "Per-Rev Lines")

            toggle09.GetProperties.SetString("Label", "0P  ")
            toggle010.GetProperties.SetString("Label", "1P  ")
            toggle010.GetProperties.SetLogical("Value", True)
            toggle011.GetProperties.SetString("Label", "2P  ")
            toggle011.GetProperties.SetLogical("Value", True)
            toggle012.GetProperties.SetString("Label", "3P  ")
            toggle013.GetProperties.SetString("Label", "4P  ")
            toggle014.GetProperties.SetString("Label", "5P  ")

            group5.GetProperties.SetString("Label", "Data Types")

            label0.GetProperties.SetString("Label", "                  Analysis System (REFSYS)")

            toggle0.GetProperties.SetString("Label", "Eigenfrequencies")
            toggle0.GetProperties.SetLogical("Value", True)
            toggle01.GetProperties.SetString("Label", "Damping Values")
            toggle02.GetProperties.SetString("Label", "Real part of eigensolution")
            toggle03.GetProperties.SetString("Label", "Imaginary part of eigensolution*")
            toggle04.GetProperties.SetString("Label", "Whirl Direction")

            label01.GetProperties.SetString("Label", "                      Converted System")

            toggle05.GetProperties.SetString("Label", "Eigenfrequencies")
            toggle05.GetProperties.SetLogical("Value", True)
            toggle06.GetProperties.SetString("Label", "Whirl Direction")
            toggle07.GetProperties.SetString("Label", "Imaginary part of eigensolution*")
            toggle08.GetProperties.SetString("Label", "Real part of eigensolution*")

            label02.GetProperties.SetString("Label", "                    * MODTRK=2/3 only")

            group3.GetProperties.SetString("Label", "Solutions")

            toggle015.GetProperties.SetString("Label", "All")
            toggle015.GetProperties.SetLogical("Value", True)

            string0.GetProperties.SetString("Label", "Format: 1,3,5-8,10     ")
            string0.GetProperties.SetEnumAsString("Width", "Standard")

            group2.GetProperties.SetString("Label", "Output File")
            group2.GetProperties.SetLogical("Show", False)

            nativeFileBrowser01.GetProperties.SetString("Label", "NX AFU file")
            nativeFileBrowser01.GetProperties.SetString("Filter", "*.afu, *.*")

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

            string0.GetProperties.SetLogical("Enable", Not toggle015.GetProperties.GetLogical("Value"))

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'Callback Name: apply_cb
    '------------------------------------------------------------------------------
    Public Function apply_cb() As Integer
        Dim errorCode As Integer = 0
        Try

            '---- Enter your callback code here -----
            csvFile = nativeFileBrowser0.GetProperties.GetString("Path")
            If csvFile = "" Then
                theNXMessageBox.Show(theNXMessageBoxTitle, NXMessageBox.DialogType.Error, "csv filename not specified")
                errorCode = 1
            End If

            rUnit = enum0.GetProperties.GetEnumAsString("Value")

            fUnit = enum01.GetProperties.GetEnumAsString("Value")

            ' Data Types
            If toggle0.GetProperties.GetLogical("Value") Then outputOptions.Add(2)
            If toggle01.GetProperties.GetLogical("Value") Then outputOptions.Add(3)
            If toggle02.GetProperties.GetLogical("Value") Then outputOptions.Add(4)
            If toggle03.GetProperties.GetLogical("Value") Then outputOptions.Add(5)
            If toggle04.GetProperties.GetLogical("Value") Then outputOptions.Add(6)
            If toggle05.GetProperties.GetLogical("Value") Then outputOptions.Add(7)
            If toggle06.GetProperties.GetLogical("Value") Then outputOptions.Add(8)
            If toggle07.GetProperties.GetLogical("Value") Then outputOptions.Add(9)
            If toggle08.GetProperties.GetLogical("Value") Then outputOptions.Add(10)

            ' Per Rev Options
            If toggle09.GetProperties.GetLogical("Value") Then perRevOutputList.Add(0)
            If toggle010.GetProperties.GetLogical("Value") Then perRevOutputList.Add(1)
            If toggle011.GetProperties.GetLogical("Value") Then perRevOutputList.Add(2)
            If toggle012.GetProperties.GetLogical("Value") Then perRevOutputList.Add(3)
            If toggle013.GetProperties.GetLogical("Value") Then perRevOutputList.Add(4)
            If toggle014.GetProperties.GetLogical("Value") Then perRevOutputList.Add(5)

            ' Solution Filter
            solOutputFilter = toggle015.GetProperties.GetLogical("Value")

            If Not solOutputFilter Then

                Dim solString As String = string0.GetProperties.GetString("Value")

                If Not solString = "" Then

                    For Each solItem As String In solString.Split(",")

                        If solItem.Contains("-") Then

                            Dim limits() As String = solItem.Split("-")
                            Dim iStart As Integer = Integer.Parse(limits(0).Trim)
                            Dim iEnd As Integer = Integer.Parse(limits(limits.Length - 1).Trim)

                            For iSol As Integer = iStart To iEnd
                                solOutputList.Add(iSol)
                            Next iSol

                        Else
                            solOutputList.Add(Integer.Parse(solItem.Trim))
                        End If

                    Next solItem

                End If

            End If

            ' AFU Filename
            afuFile = nativeFileBrowser01.GetProperties.GetString("Path")


            ' Proceed if everything is OK
            If errorCode = 0 Then doIt()


        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        apply_cb = errorCode
    End Function

    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try

            If block Is nativeFileBrowser0 Then
                '---- Enter your code here -----

                '' Cannot currently set Path to a non-existing file :(

                ''Dim csvFile As String = nativeFileBrowser0.GetProperties.GetString("Path")

                ''nativeFileBrowser01.GetProperties.SetString("Path", IO.Path.ChangeExtension(csvFile, ".afu"))

            ElseIf block Is enum0 Then
                '---- Enter your code here -----

            ElseIf block Is enum01 Then
                '---- Enter your code here -----

            ElseIf block Is toggle09 Then
                '---- Enter your code here -----

            ElseIf block Is toggle010 Then
                '---- Enter your code here -----

            ElseIf block Is toggle011 Then
                '---- Enter your code here -----

            ElseIf block Is toggle012 Then
                '---- Enter your code here -----

            ElseIf block Is toggle013 Then
                '---- Enter your code here -----

            ElseIf block Is toggle014 Then
                '---- Enter your code here -----

            ElseIf block Is label0 Then
                '---- Enter your code here -----

            ElseIf block Is toggle0 Then
                '---- Enter your code here -----

            ElseIf block Is toggle01 Then
                '---- Enter your code here -----

            ElseIf block Is toggle02 Then
                '---- Enter your code here -----

            ElseIf block Is toggle03 Then
                '---- Enter your code here -----

            ElseIf block Is toggle04 Then
                '---- Enter your code here -----

            ElseIf block Is separator0 Then
                '---- Enter your code here -----

            ElseIf block Is label01 Then
                '---- Enter your code here -----

            ElseIf block Is toggle05 Then
                '---- Enter your code here -----

            ElseIf block Is toggle06 Then
                '---- Enter your code here -----

            ElseIf block Is toggle07 Then
                '---- Enter your code here -----

            ElseIf block Is toggle08 Then
                '---- Enter your code here -----

            ElseIf block Is separator01 Then
                '---- Enter your code here -----

            ElseIf block Is label02 Then
                '---- Enter your code here -----

            ElseIf block Is toggle015 Then
                '---- Enter your code here -----

                string0.GetProperties.SetLogical("Enable", Not toggle015.GetProperties.GetLogical("Value"))

            ElseIf block Is string0 Then
                '---- Enter your code here -----

            ElseIf block Is nativeFileBrowser01 Then
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
        Dim errorCode As Integer = 0
        Try

            '---- Enter your callback code here -----
            errorCode = apply_cb()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        ok_cb = errorCode
    End Function

End Class
