'===================================================================================================
'                                      Copyright 2020 Siemens
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
'    A Visual Basic module that implements example Routing Cableway plugins.
'
'
'===================================================================================================
Option Strict On
Imports NXOpen
Imports NXOpen.Assemblies
Imports NXOpen.RoutingCommon

Module Plugins

    Dim theSession As Session = Nothing
    Dim listingWindow As ListingWindow = Nothing
    Dim customManager As CustomManager = Nothing

    '-----------------------------------------------------------------------------------------------
    ' Called when NX starts up to register the plugins.
    Function Startup(ByVal args As String()) As Integer

        If theSession Is Nothing Then
            theSession = Session.GetSession()
        End If

        If listingWindow Is Nothing Then
            listingWindow = theSession.ListingWindow
        End If

        ' Calling CreateRoutingSession Is required before registering Routed System Designer (RSD)
        ' plugins, callbacks, Or design rules to ensure the Routing libraries are properly loaded.
        theSession.CreateRoutingSession()

        If customManager Is Nothing Then
            customManager = theSession.RoutingCustomManager()
        End If

        customManager.SetRSDApplicationEnterPlugin(AddressOf ApplicationEnter)
        customManager.SetRSDApplicationExitPlugin(AddressOf ApplicationExit)

        Startup = 0
    End Function

    '-----------------------------------------------------------------------------------------------
    ' Called from File->Execute->NX Open. Useful for testing.
    Sub Main()

        If theSession Is Nothing Then
            theSession = Session.GetSession()
        End If

        If listingWindow Is Nothing Then
            listingWindow = theSession.ListingWindow
        End If

        ' Calling CreateRoutingSession Is required before registering Routed System Designer (RSD)
        ' plugins, callbacks, Or design rules to ensure the Routing libraries are properly loaded.
        theSession.CreateRoutingSession()

        If customManager Is Nothing Then
            customManager = theSession.RoutingCustomManager()
        End If

        customManager.SetRSDApplicationEnterPlugin(AddressOf ApplicationEnter)
        customManager.SetRSDApplicationExitPlugin(AddressOf ApplicationExit)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Called when you enter one of the Routed System Designer (RSD) applications.
    ' When entering the Mechanical application, registers the DisciplineChanged plugin.
    Sub ApplicationEnter(application As CustomManager.Application)
        Echo("C++ Application Enter")

        If application = customManager.Application.Electrical Then
            Echo("Entering the Electrical application ")
        Else
            ' When entering the Mechanical application, register a "discipline changed" plugin to
            ' watch for a change to the Cableway discipline.
            Echo("Entering the Mechanical application ")

            theSession.RouteCustomManager.SetDisciplineChangedPlugin(AddressOf DisciplineChanged)
        End If

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Called when you enter one of the Routed System Designer (RSD) applications.
    ' Unregisters the DisciplineChanged plugin.
    Sub ApplicationExit(application As CustomManager.Application)
        Echo("C++ Application Exit")

        If application = customManager.Application.Electrical Then
            Echo("Exiting the Electrical application ")
        Else
            Echo("Exiting the Mechanical application ")
        End If

        ' When exiting any Routing application, remove the "discipline changed" plugin And the
        ' "Cableways" plugins
        theSession.RouteCustomManager.RemoveDisciplineChangedPlugin()

        DeregisterPlugins()
    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Called when you change the discipline. Registers the Cableway plugins listed above
    ' if the New discipline Is the cableway discipline. Otherwise, it deregisters the plugins.
    Sub DisciplineChanged(previousDisciplineName As String, newDisciplineName As String)
        Echo("C++ DisciplineChanged")

        Dim cablewayDisciplineName As String = theSession.OptionsManager.GetStringValue("RSD_Cableway_Discipline_Name")

        ' Register all the Cableways plugins if the New discipline Is the Cableways discipline.
        If (cablewayDisciplineName = newDisciplineName) Then
            Echo("  Registering Cableway plugins.")
            RegisterPlugins()
        Else
            Echo("  Deregistering Cableway plugins.")
            DeregisterPlugins()
        End If

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Called by both Main And Startup to register the plugins.
    Sub RegisterPlugins()

        customManager.SetCablewayXmlFileNamePlugin(AddressOf CablewayXmlFileName)
        customManager.SetCablewayUniqueNodeNamePlugin(AddressOf CablewayNodeName)
        customManager.SetCablewayUniqueSegmentNamePlugin(AddressOf CablewaySegmentName)
        customManager.SetCablewayDeviceIdentifierPlugin(AddressOf CablewayDeviceIdentifier)
        customManager.SetCablewayPreExportPlugin(AddressOf CablewayPreExport)
        customManager.SetCablewayPostExportPlugin(AddressOf CablewayPostExport)
        customManager.SetCablewayAreaNamePlugin(AddressOf CablewayAreaName)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Called by ApplicationExit to deregister the plugins.
    Sub DeregisterPlugins()

        customManager.RemoveCablewayXmlFileNamePlugin()
        customManager.RemoveCablewayUniqueNodeNamePlugin()
        customManager.RemoveCablewayUniqueSegmentNamePlugin()
        customManager.RemoveCablewayDeviceIdentifierPlugin()
        customManager.RemoveCablewayPreExportPlugin()
        customManager.RemoveCablewayPostExportPlugin()
        customManager.RemoveCablewayAreaNamePlugin()

    End Sub
    '-----------------------------------------------------------------------------------------------
    ' Called before Routing exports a Cableway XML file to return the name of the XML file
    ' into which to write the Cableway data.
    Function CablewayXmlFileName() As String
        Echo("CablewayXmlFileName")

        Dim dt As DateTime = New DateTime()
        Dim dateString As String = dt.Year.ToString() + "_" + dt.Month.ToString("D2") + "_" + dt.Day.ToString("D2")
        Dim timeString As String = dt.Hour.ToString("D2") + "_" + dt.Minute.ToString("D2")

        Return "RoutingCablewayExport_" + dateString + "_" + timeString + ".xml"
    End Function

    '-----------------------------------------------------------------------------------------------
    ' Called while Routing exports a Cableway XML file to create a New, unique identifier
    ' for the given control point.
    '
    ' \param[in]
    '      areaName
    '          The name of the area under which the cableway part And node object live.
    '
    ' \param[in]
    '      cablewaySubassembly
    '          The cableway subassembly that owns the node object.
    '
    ' \param[in]
    '      nodeObjectOccurrence
    '          The control point or point occurrence that needs a unique ID.
    '
    ' \return
    '      The unique ID for this control point.
    Function CablewayNodeName(areaName As String, cablewaySubassembly As Assemblies.Component, nodeObjectOccurrence As NXObject) As String
        Echo("CablewayNodeName")

        ' If the node object occurrence already has a name, just return it.
        If (nodeObjectOccurrence.Name.Length > 0) Then
            Return nodeObjectOccurrence.Name
        End If

        Static nodeCounter As Integer = 0

        nodeCounter += 1

        Return nodeObjectOccurrence.Tag.ToString() + "_" + nodeCounter.ToString()

    End Function

    '-----------------------------------------------------------------------------------------------
    ' Called while Routing exports a Cableway XML file to create a New, unique identifier
    ' for the given segment.
    '
    ' \param[in]
    '      areaName
    '          The name of the area under which the cableway part And segment live.
    '
    ' \param[in]
    '      cablewaySubassembly
    '          The cableway subassembly that owns the segment object.
    '
    ' \param[in]
    '      segmentObject
    '          The segment occurrence Or hanger component that needs a unique ID.
    '
    ' \return
    '      The unique ID for this segment.
    Function CablewaySegmentName(areaName As String, cablewaySubassembly As Assemblies.Component, segmentObject As NXObject) As String
        Echo("CablewaySegmentName")

        Dim segmentPrototype As INXObject = segmentObject.Prototype

        ' When given the entity occurrence of a Routing segment Or a curve, check the curve name for an
        ' existing unique ID.
        If TypeOf segmentPrototype Is NXOpen.Routing.ArcSegment Or
           TypeOf segmentPrototype Is NXOpen.Routing.LineSegment Or
           TypeOf segmentPrototype Is NXOpen.Routing.SplineSegment Or
           TypeOf segmentPrototype Is NXOpen.Arc Or
           TypeOf segmentPrototype Is NXOpen.Line Or
           TypeOf segmentPrototype Is NXOpen.Spline Then

            Dim uniqueID As String = segmentObject.Name
            If (uniqueID.Length > 0) Then
                Return uniqueID
            End If
        End If

        ' When given a hanger component that must be represented as a zero-length segment,
        ' look for the CABLEWAY_HANGER_ID attribute on the component.
        If TypeOf segmentPrototype Is NXOpen.Routing.ArcSegment Then
            Dim uniqueID As String = segmentObject.GetStringUserAttribute("CABLEWAY_HANGER_ID", -1)
            If (uniqueID.Length > 0) Then
                Return uniqueID
            End If
        End If

        ' Otherwise, create a New unique ID And return it.
        Static segmentCounter As Integer = 0

        segmentCounter += 1

        Return segmentObject.Tag.ToString() + "_" + segmentCounter.ToString()
    End Function

    '-----------------------------------------------------------------------------------------------
    ' Called while Routing exports a Cableway XML file to identify if the given component
    ' Is a device that should be exported.
    '
    ' \param[in]
    '      component
    '          The component to check.
    '
    ' \return
    '      The device ID to use for this component in the Cableway XML file.
    '      Returns an empty string if this device should Not be exported.
    Function CablewayDeviceIdentifier(ByVal component As Component) As String
        Echo("CablewayDeviceIdentifier")

        Dim deviceID As String = ""
        If component.HasUserAttribute("Electrical_Device_ID", NXObject.AttributeType.String, -1) Then
            deviceID = component.GetStringUserAttribute("Electrical_Device_ID", -1)
        End If

        Return deviceID
    End Function

    '-----------------------------------------------------------------------------------------------
    ' Called just after Routing exports a Cableway XML file.
    '
    ' \param[in]
    '      xmlFileName
    '          The name of the XML file Routing just exported.
    Sub CablewayPreExport(ByVal xmlFileName As String)

        Echo("CablewayPreExport called with " + xmlFileName)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Called just after Routing exports a Cableway XML file.
    '
    ' \param[in]
    '      xmlFileName
    '          The name of the XML file Routing just exported.
    Sub CablewayPostExport(ByVal xmlFileName As String)

        Echo("CablewayPostExport called with " + xmlFileName)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Called during Cableway export to create an area name for a given component And all
    ' the components under it.
    '
    ' \param[in]
    '      component
    '          The component to check.
    '
    ' \return
    '      The area name to use for all the devices, hangers, nodes, segments, etc., found
    '      under this component.
    Function CablewayAreaName(ByVal component As Component) As String
        Echo("CablewayAreaName")

        Dim areaName As String = ""
        If component.HasUserAttribute("Electrical_Device_Area", NXObject.AttributeType.String, -1) Then
            areaName = component.GetStringUserAttribute("Electrical_Device_Area", -1)
        End If

        Return areaName
    End Function

    '-----------------------------------------------------------------------------------------------
    ' Writes the given string to the Listing Window and the log file.
    '
    ' \param[in]
    '      stringToWrite
    '          The string to write.
    Sub Echo(ByVal stringToWrite As String)

        If Not listingWindow.IsOpen Then
            listingWindow.Open()
        End If

        listingWindow.WriteFullline(stringToWrite)

        Dim logFile As LogFile = Session.GetSession().LogFile
        logFile.WriteLine(stringToWrite)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Tells NX when to unload your application.
    ' For Routing callbacks, plugins, And Design Rules, this MUST return AtTermination.
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination
    End Function

End Module
