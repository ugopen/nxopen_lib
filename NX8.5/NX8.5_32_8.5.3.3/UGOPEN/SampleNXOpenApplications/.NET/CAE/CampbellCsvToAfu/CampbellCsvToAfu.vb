' CampbellCsvToAfu.vb - Import Campbell .csv file to .afu file
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
'    - Records for the 1P and 2P lines will also be generated. 
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
'   Instructions:
'   1) A copy of CampbellCsvToAfu.dlx must be in one of the following locations:
'        1.) In the same folder as CampbellCsvToAfu.vb
'        2.) From where NX session is launched
'        3.) $UGII_USER_DIR/application
'        4.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
'            recommended. This variable is set to a full directory path to a file 
'            containing a list of root directories for all custom applications.
'            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_ROOT_DIR\menus\custom_dirs.dat
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
    Public whirlDir As New Dictionary(Of Integer, String)

    Sub Main()

        ' Check that work part is a CAE part
        Dim basePart As BasePart = theSession.Parts.BaseWork

        If (basePart Is Nothing Or Not (TypeOf basePart Is CAE.BaseFemPart Or TypeOf basePart Is CAE.SimPart)) Then
            theNXMessageBox.Show(theNXMessageBoxTitle, NXMessageBox.DialogType.Error, "Must be running in Simulation")
            Return
        End If

        freqUnits.Add("RPM", CAE.XyFunctionUnit.RpmRpm)
        freqUnits.Add("CPS", CAE.XyFunctionUnit.FrequencyHz)
        freqUnits.Add("HZ", CAE.XyFunctionUnit.FrequencyHz)
        freqUnits.Add("RAD", CAE.XyFunctionUnit.UnitlessRealNone)

        whirlDir.Add(2, "Backward")
        whirlDir.Add(3, "Forward")
        whirlDir.Add(4, "Linear")

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

        ' Determine the mode tracking format of the csv file

        Dim reader As FileIO.TextFieldParser = My.Computer.FileSystem.OpenTextFieldParser(csvFile)
        Dim modtrk2Flag As String = reader.PeekChars(4)
        reader.Dispose()

        If modtrk2Flag = "data" Then

            lw.WriteLine(vbNewLine + "Data format is MODTRK=2/3" + vbNewLine + vbNewLine)
            parseModtrk2Data(csvFile, afuFile)

        Else

            lw.WriteLine(vbNewLine + "Data format is MODTRK=1")
            parseModtrk1Data(csvFile, afuFile)

        End If

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

        If CampbellCsvToAfu_BS.options(9) Then
            createPerRevLine(afuFile, rpmData, 1)
            createPerRevLine(afuFile, rpmData, 2)
            createPerRevLine(afuFile, rpmData, 3)
            createPerRevLine(afuFile, rpmData, 4)
            createPerRevLine(afuFile, rpmData, 5)
            createPerRevLine(afuFile, rpmData, 0)
        End If

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

                    Dim xUnit As CAE.XyFunctionUnit = freqUnits.Item(CampbellCsvToAfu_BS.rUnit)
                    Dim yUnit As CAE.XyFunctionUnit = freqUnits.Item(CampbellCsvToAfu_BS.fUnit)

                    Dim afuIdLines(3) As String
                    afuIdLines(0) = csvFile

                    Select Case Left(recName, 1)
                        Case 2
                            recName += "-Eigenfrequency"
                            If CampbellCsvToAfu_BS.options(0) Then createAfuRecord(afuFile, afuIdLines, recName, CAE.XyFunctionGeneralType.CampbellDiagram, rpmData, xUnit, yValues, yUnit)

                        Case 3
                            recName += "-Damping_Values"
                            If CampbellCsvToAfu_BS.options(1) Then createAfuRecord(afuFile, afuIdLines, recName, CAE.XyFunctionGeneralType.Spectrum, rpmData, xUnit, yValues, CAE.XyFunctionUnit.Unknown)

                        Case 4
                            recName += "-Real_Part"
                            If CampbellCsvToAfu_BS.options(2) Then createAfuRecord(afuFile, afuIdLines, recName, CAE.XyFunctionGeneralType.Spectrum, rpmData, xUnit, yValues, CAE.XyFunctionUnit.Unknown)

                        Case 5
                            recName += "-Whirl_Dir"
                            If CampbellCsvToAfu_BS.options(4) Then createAfuRecord(afuFile, afuIdLines, recName, CAE.XyFunctionGeneralType.Spectrum, rpmData, xUnit, yValues, CAE.XyFunctionUnit.UnitlessScalarNone)

                        Case 6
                            recName += "-Conv_Eigenfrequency"
                            If CampbellCsvToAfu_BS.options(5) Then createAfuRecord(afuFile, afuIdLines, recName, CAE.XyFunctionGeneralType.CampbellDiagram, rpmData, xUnit, yValues, yUnit)

                        Case 7
                            recName += "-Conv_Whirl_Dir"
                            If CampbellCsvToAfu_BS.options(6) Then createAfuRecord(afuFile, afuIdLines, recName, CAE.XyFunctionGeneralType.Spectrum, rpmData, xUnit, yValues, CAE.XyFunctionUnit.UnitlessScalarNone)

                    End Select

                End If

            Next

            csvIdx += rpmCount
        Loop Until csvIdx >= csvData.Length

    End Sub

    Sub parseModtrk2Data(ByVal csvFile As String, ByVal afuFile As String)

        Dim reader As FileIO.TextFieldParser = My.Computer.FileSystem.OpenTextFieldParser(csvFile)
        reader.TextFieldType = FileIO.FieldType.Delimited
        reader.Delimiters = New String() {","}
        reader.CommentTokens = New String() {"$"}
        reader.TrimWhiteSpace = True

        Dim solId As Integer = 0

        While Not reader.EndOfData

            Dim rotorSpd As New ArrayList
            Dim eigen As New ArrayList
            Dim damping As New ArrayList
            Dim real As New ArrayList
            Dim imag As New ArrayList
            Dim whirl As New ArrayList
            Dim eigen_1 As New ArrayList
            Dim whirl_1 As New ArrayList
            Dim imag_1 As New ArrayList
            Dim real_1 As New ArrayList

            Try
                Do
                    Dim currentRow() As String = reader.ReadFields()

                    If currentRow(0).Contains("data") Then
                        Dim colID As Integer = Convert.ToInt32(currentRow(0).Substring(4))

                        If colID = 9000 Then
                            Do
                                Dim currentRow1() As String = reader.ReadFields()

                                rotorSpd.Add(Convert.ToDouble(currentRow1(0), nfi))
                                eigen.Add(Convert.ToDouble(currentRow1(1), nfi))
                                damping.Add(Convert.ToDouble(currentRow1(2), nfi))
                                real.Add(Convert.ToDouble(currentRow1(3), nfi))
                                imag.Add(Convert.ToDouble(currentRow1(4), nfi))
                                whirl.Add(Convert.ToDouble(currentRow1(5), nfi))
                                eigen_1.Add(Convert.ToDouble(currentRow1(6), nfi))

                            Loop Until reader.EndOfData

                        End If

                        solId = (colID - 10001) / 10

                    Else

                        rotorSpd.Add(Convert.ToDouble(currentRow(0), nfi))
                        eigen.Add(Convert.ToDouble(currentRow(1), nfi))
                        damping.Add(Convert.ToDouble(currentRow(2), nfi))
                        real.Add(Convert.ToDouble(currentRow(3), nfi))
                        imag.Add(Convert.ToDouble(currentRow(4), nfi))
                        whirl.Add(Convert.ToDouble(currentRow(5), nfi))
                        eigen_1.Add(Convert.ToDouble(currentRow(6), nfi))
                        whirl_1.Add(Convert.ToDouble(currentRow(7), nfi))
                        imag_1.Add(Convert.ToDouble(currentRow(8), nfi))
                        real_1.Add(Convert.ToDouble(currentRow(9), nfi))

                    End If

                Loop Until reader.PeekChars(4) = "data" Or reader.EndOfData

            Catch ex As FileIO.MalformedLineException
                MsgBox("Line " & ex.Message & "is not valid and will be skipped.")
            End Try

            ' Create the AFU record
            Dim xUnit As CAE.XyFunctionUnit = freqUnits.Item(CampbellCsvToAfu_BS.rUnit)
            Dim yUnit As CAE.XyFunctionUnit = freqUnits.Item(CampbellCsvToAfu_BS.fUnit)

            Dim afuIdLines(3) As String
            afuIdLines(0) = csvFile

            If solId < 0 Then

                If CampbellCsvToAfu_BS.options(9) Then

                    Dim recordName As String = "1_P"
                    createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.CampbellDiagram, rotorSpd.ToArray(GetType(Double)), xUnit, eigen.ToArray(GetType(Double)), yUnit)

                    recordName = "2_P-RotatingSystem"
                    createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.CampbellDiagram, rotorSpd.ToArray(GetType(Double)), xUnit, damping.ToArray(GetType(Double)), yUnit)

                    recordName = "3_P"
                    createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.CampbellDiagram, rotorSpd.ToArray(GetType(Double)), xUnit, real.ToArray(GetType(Double)), yUnit)

                    recordName = "4_P"
                    createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.CampbellDiagram, rotorSpd.ToArray(GetType(Double)), xUnit, imag.ToArray(GetType(Double)), yUnit)

                    recordName = "5_P"
                    createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.CampbellDiagram, rotorSpd.ToArray(GetType(Double)), xUnit, whirl.ToArray(GetType(Double)), yUnit)

                    ''recordName = "Color-0=Black"
                    ''createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.CampbellDiagram, rotorSpd.ToArray(GetType(Double)), xUnit, eigen_1.ToArray(GetType(Double)), yUnit)

                End If

            Else

                Dim recordPrefix As String = "SOL_" + solId.ToString

                Dim iWhirlDir As Integer = Math.Round(arrayAverage(whirl.ToArray(GetType(Double))))
                afuIdLines(1) = whirlDir.Item(iWhirlDir)

                Dim recordName As String = recordPrefix + "-Eigenfrequency"
                If CampbellCsvToAfu_BS.options(0) Then createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.CampbellDiagram, rotorSpd.ToArray(GetType(Double)), xUnit, eigen.ToArray(GetType(Double)), yUnit)

                recordName = recordPrefix + "-Damping_Values"
                If CampbellCsvToAfu_BS.options(1) Then createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.Spectrum, rotorSpd.ToArray(GetType(Double)), xUnit, damping.ToArray(GetType(Double)), CAE.XyFunctionUnit.Unknown)

                recordName = recordPrefix + "-Real_Part"
                If CampbellCsvToAfu_BS.options(2) Then createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.Spectrum, rotorSpd.ToArray(GetType(Double)), xUnit, real.ToArray(GetType(Double)), CAE.XyFunctionUnit.Unknown)

                recordName = recordPrefix + "-Imag_Part"
                If CampbellCsvToAfu_BS.options(3) Then createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.Spectrum, rotorSpd.ToArray(GetType(Double)), xUnit, imag.ToArray(GetType(Double)), CAE.XyFunctionUnit.Unknown)

                recordName = recordPrefix + "-Whirl_Dir"
                If CampbellCsvToAfu_BS.options(4) Then createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.Spectrum, rotorSpd.ToArray(GetType(Double)), xUnit, whirl.ToArray(GetType(Double)), CAE.XyFunctionUnit.UnitlessScalarNone)

                recordName = recordPrefix + "-Conv_Eigenfrequency"
                If CampbellCsvToAfu_BS.options(5) Then createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.CampbellDiagram, rotorSpd.ToArray(GetType(Double)), xUnit, eigen_1.ToArray(GetType(Double)), yUnit)

                recordName = recordPrefix + "-Conv_Whirl_Dir"
                If CampbellCsvToAfu_BS.options(6) Then createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.Spectrum, rotorSpd.ToArray(GetType(Double)), xUnit, whirl_1.ToArray(GetType(Double)), CAE.XyFunctionUnit.UnitlessScalarNone)

                recordName = recordPrefix + "-Conv_Imag_Part"
                If CampbellCsvToAfu_BS.options(7) Then createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.Spectrum, rotorSpd.ToArray(GetType(Double)), xUnit, imag_1.ToArray(GetType(Double)), CAE.XyFunctionUnit.Unknown)

                recordName = recordPrefix + "-Conv_Real_Part"
                If CampbellCsvToAfu_BS.options(8) Then createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.Spectrum, rotorSpd.ToArray(GetType(Double)), xUnit, real_1.ToArray(GetType(Double)), CAE.XyFunctionUnit.Unknown)

            End If

        End While

        reader.Dispose()

    End Sub

    Function arrayAverage(ByVal values() As Double) As Double

        Dim sum As Double = 0.0

        For Each value As Double In values
            sum += value
        Next value

        Dim average As Double = sum / values.Length

        Return average

    End Function

    Sub createPerRevLine(ByVal afuFile As String, ByVal rpm() As Double, ByVal order As Integer)

        Dim xUnit As CAE.XyFunctionUnit = freqUnits.Item(CampbellCsvToAfu_BS.rUnit)
        Dim yUnit As CAE.XyFunctionUnit = freqUnits.Item(CampbellCsvToAfu_BS.fUnit)

        Dim rUnit_to_fUnit As Double = 60

        If xUnit.CompareTo(yUnit) = 0 Then
            rUnit_to_fUnit = 1.0
        End If

        Dim absData() As Double = {0.0, rpm(rpm.Length - 1)}
        Dim ordData() As Double = {0.0, rpm(rpm.Length - 1) / rUnit_to_fUnit * order}

        Dim afuIdLines(3) As String

        ' Create 1P and 2P records in AFU
        Dim recordName As String = order.ToString + "_P"
        If order = 2 Then recordName += "-RotatingSystem"

        createAfuRecord(afuFile, afuIdLines, recordName, CAE.XyFunctionGeneralType.CampbellDiagram, absData, xUnit, ordData, yUnit)

        lw.WriteLine(recordName + " line generated")

    End Sub

    Sub createAfuRecord(ByVal afuFile As String, ByVal idLines() As String, ByVal recordName As String, ByVal fType As CAE.XyFunctionGeneralType, ByVal abscissaData() As Double, ByVal xUnit As CAE.XyFunctionUnit, ByVal ordinateData() As Double, ByVal yUnit As CAE.XyFunctionUnit)

        Dim iMaxIdStringLength As Integer = 79

        Dim afuHeaderId As CAE.AfuHeaderId = theSession.AfuManager.CreateAfuHeaderId

        If Not idLines(0) Is Nothing Then afuHeaderId.IdLine1 = Right(idLines(0), iMaxIdStringLength)
        If Not idLines(1) Is Nothing Then afuHeaderId.IdLine2 = Left(idLines(1), iMaxIdStringLength)
        If Not idLines(2) Is Nothing Then afuHeaderId.IdLine3 = Left(idLines(2), iMaxIdStringLength)
        If Not idLines(3) Is Nothing Then afuHeaderId.IdLine4 = Left(idLines(3), iMaxIdStringLength)

        Dim afuData1 As CAE.AfuData = theSession.AfuManager.CreateAfuData()

        afuData1.FileName = afuFile
        afuData1.RecordName = recordName
        afuData1.AfuHeaderId = afuHeaderId
        afuData1.SetIdInformation("x+", 1, "x+", 1)
        afuData1.SetAxisDefinition(CAE.AfuData.AbscissaType.Uneven, xUnit, CAE.AfuData.OrdinateType.Real, yUnit)
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
'       Filename:  D:\NX_Open\Campbell\BlockStyler\CampbellCsvToAfu_BS.vb
'
'        This file was generated by the NX Block UI Styler
'        Created by: tsbernar
'              Version: NX 7.5
'              Date: 03-18-2011  (Format: mm-dd-yyyy)
'              Time: 10:50 (Format: hh-mm)
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
    Public Shared options(9) As Boolean

    Private theDialogName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private group0 As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private nativeFileBrowser0 As NXOpen.BlockStyler.UIBlock' Block type: NativeFileBrowser
    Private group As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private enum0 As NXOpen.BlockStyler.UIBlock' Block type: Enumeration
    Private enum01 As NXOpen.BlockStyler.UIBlock' Block type: Enumeration
    Private group1 As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private label0 As NXOpen.BlockStyler.UIBlock' Block type: Label
    Private toggle0 As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private toggle01 As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private toggle02 As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private toggle03 As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private toggle04 As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private separator0 As NXOpen.BlockStyler.UIBlock' Block type: Separator
    Private label01 As NXOpen.BlockStyler.UIBlock' Block type: Label
    Private toggle05 As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private toggle06 As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private toggle07 As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private toggle08 As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private label02 As NXOpen.BlockStyler.UIBlock' Block type: Label
    Private separator01 As NXOpen.BlockStyler.UIBlock' Block type: Separator
    Private separator02 As NXOpen.BlockStyler.UIBlock' Block type: Separator
    Private toggle09 As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private group2 As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private nativeFileBrowser01 As NXOpen.BlockStyler.UIBlock' Block type: NativeFileBrowser
    
#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
        
            ''theSession = Session.GetSession()
            ''theUI = UI.GetUI()

            theDialogName = IO.Path.ChangeExtension(theSession.ExecutingJournal, "dlx")

            If Not File.Exists(theDialogName) Then
                theDialogName = "CampbellCsvToAfu.dlx"
            End If

            theDialog = theUI.CreateDialog(theDialogName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddOkHandler(AddressOf ok_cb)
            theDialog.AddUpdateHandler(AddressOf update_cb)
            theDialog.AddInitializeHandler(AddressOf initialize_cb)
            theDialog.AddFocusNotifyHandler(AddressOf focusNotify_cb)
            theDialog.AddKeyboardFocusNotifyHandler(AddressOf keyboardFocusNotify_cb)
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
    End Function
    
    '------------------------------------------------------------------------------
    'This method shows the dialog on the screen
    '------------------------------------------------------------------------------
    Public Sub Show()
        Try
        
            theDialog.Show
        
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
            label02 = CType(theDialog.TopBlock.FindBlock("label02"), NXOpen.BlockStyler.UIBlock)
            separator01 = CType(theDialog.TopBlock.FindBlock("separator01"), NXOpen.BlockStyler.UIBlock)
            separator02 = CType(theDialog.TopBlock.FindBlock("separator02"), NXOpen.BlockStyler.UIBlock)
            toggle09 = CType(theDialog.TopBlock.FindBlock("toggle09"), NXOpen.BlockStyler.UIBlock)
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

            group1.GetProperties.SetString("Label", "Processing Options")

            label0.GetProperties.SetString("Label", "Analysis System (REFSYS)")

            toggle0.GetProperties.SetString("Label", "Eigenfrequencies")
            toggle01.GetProperties.SetString("Label", "Damping Values")
            toggle02.GetProperties.SetString("Label", "Real part of eigensolution")
            toggle03.GetProperties.SetString("Label", "Imaginary part of eigensolution*")
            toggle04.GetProperties.SetString("Label", "Whirl Direction")

            label01.GetProperties.SetString("Label", "Converted System")

            toggle05.GetProperties.SetString("Label", "Eigenfrequencies")
            toggle06.GetProperties.SetString("Label", "Whirl Direction")
            toggle07.GetProperties.SetString("Label", "Imaginary part of eigensolution*")
            toggle08.GetProperties.SetString("Label", "Real part of eigensolution*")

            label02.GetProperties.SetString("Label", "                    * MODTRK=2/3 only")

            toggle09.GetProperties.SetString("Label", "Per Rev Lines (1P, 2P, etc.)")

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
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'Callback Name: apply_cb
    '------------------------------------------------------------------------------
    Public Function apply_cb() As Integer
        Dim errorCode as Integer = 0
        Try
        
            '---- Enter your callback code here -----
            csvFile = nativeFileBrowser0.GetProperties.GetString("Path")

            rUnit = enum0.GetProperties.GetEnumAsString("Value")

            fUnit = enum01.GetProperties.GetEnumAsString("Value")

            options(0) = toggle0.GetProperties.GetLogical("Value")
            options(1) = toggle01.GetProperties.GetLogical("Value")
            options(2) = toggle02.GetProperties.GetLogical("Value")
            options(3) = toggle03.GetProperties.GetLogical("Value")
            options(4) = toggle04.GetProperties.GetLogical("Value")
            options(5) = toggle05.GetProperties.GetLogical("Value")
            options(6) = toggle06.GetProperties.GetLogical("Value")
            options(7) = toggle07.GetProperties.GetLogical("Value")
            options(8) = toggle08.GetProperties.GetLogical("Value")
            options(9) = toggle09.GetProperties.GetLogical("Value")

            afuFile = nativeFileBrowser01.GetProperties.GetString("Path")

            doIt()

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
            
            ElseIf block Is label02 Then
            '---- Enter your code here -----
            
            ElseIf block Is separator01 Then
            '---- Enter your code here -----
            
            ElseIf block Is separator02 Then
            '---- Enter your code here -----
            
            ElseIf block Is toggle09 Then
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
        Dim errorCode as Integer = 0
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
    
    '------------------------------------------------------------------------------
    'Callback Name: focusNotify_cb
    'This callback is executed when any block (except the ones which receive keyboard entry such as Integer block) receives focus.
    '------------------------------------------------------------------------------
    Public Sub focusNotify_cb(ByVal block As BlockStyler.UIBlock, ByVal focus As Boolean)
        Try
        
            '---- Enter your callback code here -----
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'Callback Name: keyboardFocusNotify_cb
    'This callback is executed when block which can receive keyboard entry, receives the focus.
    '------------------------------------------------------------------------------
    Public Sub keyboardFocusNotify_cb(ByVal block As BlockStyler.UIBlock, ByVal focus As Boolean)
        Try
        
            '---- Enter your callback code here -----
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
End Class
