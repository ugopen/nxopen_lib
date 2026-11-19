'===================================================================================================
'               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
'===================================================================================================
'
'    NOTE:  NX Development provides programming examples for illustration only.
'    NX Development assumes you are familiar with the programming language
'    demonstrated in these examples, and the tools used to create and debug NX/Open
'    programs. GTAC support professionals can help explain the functionality of
'    a particular procedure, but neither GTAC nor NX Development will modify
'    these examples to provide added functionality or construction procedures.
'
'File description:
'
'    A Visual Basic module that implements example Routing plugins.
'
'
'===================================================================================================
Option Strict On
Imports System
Imports System.Windows.Forms
Imports NXOpen
Imports NXOpen.Routing
Imports NXOpen.Routing.Electrical
Imports NXOpen.Routing.CustomManager
Imports NXOpen.Preferences
Imports System.Collections.Generic
Imports NXOpen.Utilities

Module Plugins

    Dim theSession As Session = Nothing
    Dim listingWindow As ListingWindow = Nothing
    Dim customManager As CustomManager = Nothing
    Dim createPathRuleId As Integer = 0
    Dim subdivideSegmentRuleId As Integer = 0

    '-----------------------------------------------------------------------------------------------
    ' Called when NX starts up to register the plugins.
    Function Startup(ByVal args As String()) As Integer

        If theSession Is Nothing Then
            theSession = Session.GetSession()
        End If

        If listingWindow Is Nothing Then
            listingWindow = theSession.ListingWindow
        End If

        If customManager Is Nothing Then
            customManager = theSession.RouteCustomManager()
        End If

        RegisterPlugins()

        Startup = 0
    End Function

    '------------------------------------------------------------------------------------------
    ' Called from File->Execute->NX Open. Useful for testing.
    Sub Main()

        If theSession Is Nothing Then
            theSession = Session.GetSession()
        End If

        If listingWindow Is Nothing Then
            listingWindow = theSession.ListingWindow
        End If

        If customManager Is Nothing Then
            customManager = theSession.RouteCustomManager()
        End If

        RegisterPlugins()
    End Sub

    '------------------------------------------------------------------------------------------
    ' Called by both Main And Startup to register the plugins.
    Sub RegisterPlugins()

        customManager.SetHrnPreImportPlugin(AddressOf ImportExportPlugin)
        customManager.SetHrnPostExportPlugin(AddressOf ImportExportPlugin)
        customManager.SetCmpPreImportPlugin(AddressOf ImportExportPlugin)
        customManager.SetCmpPostExportPlugin(AddressOf ImportExportPlugin)
        customManager.SetPlmXmlPreImportPlugin(AddressOf ImportExportPlugin)
        customManager.SetPlmXmlPostExportPlugin(AddressOf ImportExportPlugin)
        customManager.SetPlmXmlRouteNodeNamePlugin(AddressOf RouteNodeNamePlugin)
        customManager.SetPlmXmlRouteSectionNamePlugin(AddressOf RouteSectionNamePlugin)
        customManager.SetWrappedOverstockLengthCalculationPlugin(AddressOf WrappedOverstockLengthCalculationPlugin)
        customManager.SetFilterBlankingPlugin(AddressOf FilterBlankingPlugin)
        customManager.SetBomPlugin(AddressOf BomPlugin)
        customManager.SetAutoRoutePlugin(AddressOf AutoRoutePlugin)
        customManager.SetManualRoutePlugin(AddressOf ManualRoutePlugin)
        customManager.SetUnroutePlugin(AddressOf UnroutePlugin)
        customManager.SetNavigatorObjectSelectedPlugin(AddressOf NavigatorObjectSelectedPlugin)
        customManager.SetValidateFormboardPlugin(AddressOf ValidateFormboardPlugin)
        customManager.SetDisciplineChangedPlugin(AddressOf DisciplineChangedPlugin)
        customManager.SetSpecificationChangedPlugin(AddressOf SpecificationChangedPlugin)
        customManager.SetSortConnectionsPlugin(AddressOf SortConnectionsPlugin)
        customManager.SetChoosePartPlugin(AddressOf ChoosePartPlugin)

    End Sub

    '-----------------------------------------------------------------------------------------------
    Sub ImportExportPlugin(ByVal fileName As String)
        Echo("*** ImportExportPlugin called with " + fileName + "." + vbCrLf)
    End Sub

    '-----------------------------------------------------------------------------------------------
    Function RouteNodeNamePlugin() As String
        Echo("*** RouteNodeNamePlugin called")

        Return "RNx"
    End Function

    '-----------------------------------------------------------------------------------------------
    Function RouteSectionNamePlugin() As String
        Echo("*** RouteSectionNamePlugin called")

        Return "RSx"
    End Function

    '-----------------------------------------------------------------------------------------------
    Function WrappedOverstockLengthCalculationPlugin(ByVal overstock As Overstock) As Double
        Echo("*** Wrapped Overstock Length Calculation plugin called with overstock tag " + overstock.Tag.ToString())

        Return 10.0
    End Function

    '-----------------------------------------------------------------------------------------------
    Function FilterBlankingPlugin(ByVal segmentOrComponent As NXObject, ByVal logicalAttributeTitle As String, ByVal logicalAttributeValue As String, ByVal variableBuildString As String) As Boolean

        Echo("*** Filter Blanking plugin called with object tag tag " + segmentOrComponent.Tag.ToString())

        Dim electricalPreferences As RoutingElectrical = theSession.Preferences.RoutingApplicationView.RoutingElectrical

        Dim apvAttributeTitle As String = electricalPreferences.GetFilterBlankingAttribute

        Echo("    APV Attribute Title    : " + apvAttributeTitle)
        Echo("    Logical Attribute Title: " + logicalAttributeTitle)

        If logicalAttributeTitle <> apvAttributeTitle Then
            Echo("    (Not the same attribute titles. Ignoring this object.)")
            Return False
        End If

        logicalAttributeValue = logicalAttributeValue.ToUpper()

        Dim blankTheObject As Boolean = logicalAttributeValue Is "YES" Or
                                        logicalAttributeValue Is "TRUE" Or
                                        logicalAttributeValue Is "1"

        Echo("    Logical Attribute Value: " + logicalAttributeValue)
        Echo("    Variable Build String  : " + variableBuildString)

        If (blankTheObject) Then
            Echo("    Blank the object!")
        End If

        Echo("")

        FilterBlankingPlugin = blankTheObject

    End Function

    '-----------------------------------------------------------------------------------------------
    Sub BomPlugin()
        Echo("*** BomPlugin called." + vbCrLf)
    End Sub

    '-----------------------------------------------------------------------------------------------
    Function AutoRoutePlugin(ByVal connections As Connection()) As Integer
        Echo(vbCrLf + "*** Autoroute plugin called with " + connections.Length.ToString() + " connections.")

        For Each connection As Connection In connections
            Echo("  Connection Tag " + connection.Tag.ToString())
        Next

        AutoRoutePlugin = 0
    End Function

    '-----------------------------------------------------------------------------------------------
    Function ManualRoutePlugin(ByVal connections As Connection()) As Integer
        Echo(vbCrLf + "*** ManualRoute plugin called with " + connections.Length.ToString() + " connections.")

        For Each connection As Connection In connections
            Echo("  Connection Tag " + connection.Tag.ToString())
        Next

        ManualRoutePlugin = 0
    End Function

    '-----------------------------------------------------------------------------------------------
    Function UnroutePlugin(ByVal connections As Connection()) As Integer
        Echo(vbCrLf + "*** Unroute plugin called with " + connections.Length.ToString() + " connections.")

        For Each connection As Connection In connections
            Echo("  Connection Tag " + connection.Tag.ToString())
        Next

        UnroutePlugin = 0
    End Function

    '-----------------------------------------------------------------------------------------------
    Sub NavigatorObjectSelectedPlugin(ByVal navigatorType As NavigatorType, ByVal selectionType As SelectionType, ByVal selectedObjects As NXObject())

        Dim message As String = vbCrLf + "*** NavigatorObjectSelectedPlugin called with " + selectedObjects.Length.ToString()

        If selectionType = selectionType.Selected Then
            message += " selected"
        Else
            message += " deselected"
        End If

        If navigatorType = navigatorType.Connection Then
            message += " in the Connection Navigator."
        Else
            message += " in the Component Navigator."
        End If

        Echo(message)

        For Each selectedObject As NXObject In selectedObjects
            Echo("    Object tag " + selectedObject.Tag.ToString())
        Next

    End Sub

    '-----------------------------------------------------------------------------------------------
    Function ValidateFormboardPlugin(ByVal harnessDevices As HarnessDevice()) As Boolean
        Echo(vbCrLf + "*** ValidateFormboard plugin called with " + harnessDevices.Length.ToString() + " harness devices.")

        For Each harnessDevice As HarnessDevice In harnessDevices
            Echo("    Harness tag " + harnessDevice.Tag.ToString())
        Next

        ValidateFormboardPlugin = True
    End Function

    '-----------------------------------------------------------------------------------------------
    Sub DisciplineChangedPlugin(ByVal previousDisciplineName As String, ByVal newDisciplineName As String)
        Echo("*** Visual Basic Discipline Changed plugin called.")
        Echo("    Previous discipline name '" + previousDisciplineName + "'")
        Echo("    New discipline name      '" + newDisciplineName + "'")
    End Sub

    '-----------------------------------------------------------------------------------------------
    Sub SpecificationChangedPlugin(ByVal previousSpecificationName As String, ByVal newSpecificationName As String)
        Echo("*** Visual Basic Specification Changed plugin called.")
        Echo("    Previous specification name '" + previousSpecificationName + "'")
        Echo("    New specification name      '" + newSpecificationName + "'")
    End Sub

    '-----------------------------------------------------------------------------------------------
    Sub SortConnectionsPlugin(ByVal dataObject As SortConnectionsPluginData)
        Dim stockDevices() As ElectricalStockDevice = Nothing
        dataObject.GetStockDevicesToSort(stockDevices)

        Echo("*** VB Sort Connections plugin called with " + stockDevices.Length.ToString() + " stock devices.")

        Dim stockDeviceTags(stockDevices.Length - 1) As Tag
        Dim index = 0
        For Each stockDevice As ElectricalStockDevice In stockDevices
            Echo("  Stock Device Tag " + stockDevice.Tag.ToString() + ".")
            stockDeviceTags(index) = stockDevice.Tag
            index += 1
        Next

        Array.Sort(stockDeviceTags)

        Echo("")
        Dim sortedStockDevices(stockDevices.Length - 1) As ElectricalStockDevice

        index = 0
        For Each stockDeviceTag As Tag In stockDeviceTags
            Echo("  Sorted Stock Device Tag " + stockDeviceTag.ToString() + ".")
            sortedStockDevices(index) = CType(NXObjectManager.Get(stockDeviceTag), ElectricalStockDevice)
            index += 1
        Next

        dataObject.SetSortedStockDevices(sortedStockDevices)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Implements an example Choose Part plugin that is used by the Place Part command.
    '
    ' You will have to add a reference to the Assemblies Framework System.Windows.Forms to use
    ' the OpenFileDialog class shown in this example.
    Function ChoosePartPlugin(ByVal dataObject As ChoosePartPluginData) As Integer

        Dim openFileDialog As OpenFileDialog = New OpenFileDialog()

        openFileDialog.Title = "Choose a part to place"
        openFileDialog.DefaultExt = "prt"
        openFileDialog.Filter = "part files (*.prt)|*.prt|All files (*.*)|*.*"
        openFileDialog.CheckFileExists = True
        openFileDialog.CheckPathExists = True

        Dim result As DialogResult = openFileDialog.ShowDialog()
        If (result = DialogResult.Cancel) Then
            Return -1
        End If

        Dim fullPath As String = openFileDialog.FileName

        ' At this point, you could open the part to get some of the part attributes from it.
        ' For this example, we are just going to return a few default values to Routing.
        dataObject.SetPartName(fullPath)
        dataObject.SetPartNumber("ExamplePartNumber001")
        dataObject.SetMemberName("") ' No member name since this Is Not a member Of a part family.

        ' Some example attributes.
        Dim exampleCharacteristics As CharacteristicList = theSession.Preferences.RoutingApplicationView.PartPreferences.PartLibrary.CreateCriteria()
        exampleCharacteristics.SetCharacteristic("USER_CHARX_TITLE1", "User_charx_value1")
        exampleCharacteristics.SetCharacteristic("USER_CHARX_TITLE2", "User_charx_value2")

        dataObject.SetCharacteristics(exampleCharacteristics)

        Return 0

    End Function

    '-----------------------------------------------------------------------------------------------
    ' Writes the given string to the Listing Window and the syslog.
    '
    ' \param[in]
    '      stringToWrite
    '          The string to write.
    Sub Echo(ByVal stringToWrite As String)

        If Not listingWindow.IsOpen Then
            listingWindow.Open()
        End If

        listingWindow.WriteFullline(stringToWrite)

        Dim syslog As LogFile = Session.GetSession().LogFile
        syslog.WriteLine(stringToWrite)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Tells NX when to unload your application.
    ' For Routing callbacks, plugins, And Design Rules, this MUST return AtTermination.
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination
    End Function

End Module
