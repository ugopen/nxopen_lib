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
'    A Visual Basic module that implements example Routing Design Rules.
'
'
'===================================================================================================
Option Strict On
Imports System
Imports NXOpen
Imports NXOpen.Routing
Imports NXOpen.Routing.Electrical
Imports NXOpen.Routing.CustomManager
Imports NXOpen.Preferences

Module DesignRules

    Dim theSession As Session = Nothing
    Dim customManager As CustomManager = Nothing
    Dim createPathRuleId As Integer = 0
    Dim subdivideSegmentRuleId As Integer = 0
    Dim modularConnectorRuleId As Integer = 0

    '-----------------------------------------------------------------------------------------------
    ' Called when NX starts up to register the Design Rules.
    Function Startup(ByVal args As String()) As Integer

        If theSession Is Nothing Then
            theSession = Session.GetSession()
        End If

        If customManager Is Nothing Then
            customManager = theSession.RouteCustomManager()
        End If

        RegisterDesignRules()

        Startup = 0
    End Function

    '------------------------------------------------------------------------------------------
    ' Called from File->Execute->NX Open. Useful for testing.
    Sub Main()

        If theSession Is Nothing Then
            theSession = Session.GetSession()
        End If

        If customManager Is Nothing Then
            customManager = theSession.RouteCustomManager()
        End If

        RegisterDesignRules()
    End Sub

    '------------------------------------------------------------------------------------------
    ' Called by both Main And Startup to register the Design Rules.
    Sub RegisterDesignRules()

        Dim createPathName As String = "Create Path"
        Dim subdivideSegmentName As String = "Subdivide Segment"
        Dim modularConnectorName As String = "Modular Connector"
        Dim createPathDescription As String = "The Create Path design rule makes sure each segment on the path is not too long."
        Dim subdivideSegmentDescription As String = "The Subdivide Segment design rule makes sure each new segment is not too short."
        Dim modularConnectorDescription As String = "The Modular Connector rule makes sure modular connectors are plugged into the correct position on the parent shell."

        createPathRuleId = customManager.AddDesignRule(customManager.DesignRuleReason.CreatePath, createPathName, createPathDescription, AddressOf CreatePathDesignRule)
        subdivideSegmentRuleId = customManager.AddDesignRule(customManager.DesignRuleReason.SubdivideSegment, subdivideSegmentName, subdivideSegmentDescription, AddressOf SubdivideSegmentDesignRule)
        modularConnectorRuleId = customManager.AddDesignRule(customManager.DesignRuleReason.Interactive, modularConnectorName, modularConnectorDescription, AddressOf ModularConnectorDesignRule)

    End Sub

    '-----------------------------------------------------------------------------------------------
    Sub CreatePathDesignRule(ByVal reason As DesignRuleReason, ByVal nxObjects As NXObject())
        Dim createPathName As String = "Create Path"

        Dim maximumLength As Double = 1000.0

        If reason = DesignRuleReason.Interactive Then

            ' For interactive checks, check all the segments in the work part.
            Dim segmentManager As SegmentManager = theSession.Parts.Work.SegmentManager
            Dim segmentCollection As ISegmentCollection = segmentManager.Segments

            For Each segment As ISegment In segmentCollection
                CheckForLongSegments(createPathName, maximumLength, segment)
            Next

            Return
        End If

        ' Otherwise, check the segments in the given list of objects.
        For Each nxObject As NXObject In nxObjects
            If TypeOf nxObject Is SplineSegment Then
                CheckForLongSegments(createPathName, maximumLength, CType(nxObject, ISegment))
            End If

        Next

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Checks the length of the given segment against the maximum allowed length.
    '
    ' Creates a violation for the given reason if the segment Is too long.
    '
    ' \param[in]
    '      maximumLength
    '          The longest length allowed.
    '
    ' \param[in]
    '      segment
    '          The segment to check.
    Sub CheckForLongSegments(ByVal designRuleName As String, ByVal maximumLength As Double, ByVal segment As ISegment)

        If segment.Length < maximumLength Then
            Return
        End If

        Dim objects() As Curve = New Curve() {CType(segment, Curve)}

        customManager.CreateViolationForReason(designRuleName,
                                               customManager.DesignRuleReason.CreatePath,
                                               "This path is too long.",
                                               "Long paths need to be broken up and supported by clamps.",
                                               objects)
    End Sub

    '-----------------------------------------------------------------------------------------------
    Sub SubdivideSegmentDesignRule(ByVal reason As DesignRuleReason, ByVal nxObjects As NXObject())
        Dim subdivideSegmentName As String = "Subdivide Segment"

        Dim userPreferences As RoutingUserPreferences = theSession.Preferences.RoutingApplicationView.RoutingUserPreferences

        Dim minimumLength As Double = 0.0
        If Not userPreferences.GetDoublePreference("ROUTE_ELEC_MIN_STRAIGHT_LENGTH_COEFF", minimumLength) Then
            minimumLength = 10.0
        End If

        If reason = DesignRuleReason.Interactive Then

            ' For interactive checks, check all the segments in the work part.
            Dim segmentManager As SegmentManager = theSession.Parts.Work.SegmentManager
            Dim segmentCollection As ISegmentCollection = segmentManager.Segments

            For Each segment As ISegment In segmentCollection
                CheckForShortSegments(subdivideSegmentName, minimumLength, segment)
            Next

            Return

        End If

        ' Otherwise, check the segments in the given list of objects.
        For Each nxObject As NXObject In nxObjects
            If TypeOf nxObject Is SplineSegment Then
                CheckForShortSegments(subdivideSegmentName, minimumLength, CType(nxObject, ISegment))
            End If

        Next

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Checks the length of the given segment against the minimum allowed length.
    '
    ' Creates a violation for the given reason if the segment Is too short.
    '
    ' \param[in]
    '      maximumLength
    '          The shortest length allowed.
    '
    ' \param[in]
    '      segment
    '          The segment to check.
    Sub CheckForShortSegments(ByVal designRuleName As String, ByVal maximumLength As Double, ByVal segment As ISegment)

        If segment.Length > maximumLength Then
            Return
        End If

        Dim objects() As Curve = New Curve() {CType(segment, Curve)}

        customManager.CreateViolationForReason(designRuleName,
                                               customManager.DesignRuleReason.SubdivideSegment,
                                               "This segment is too short.",
                                               "Short segments violate our design standards.",
                                               objects)
    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Safely gets the value of a string characteristic if it exists on the route object.
    '
    ' \param[in]
    '      routeObject 
    '          The object from which to get the characteristic.
    '
    ' \param[in]
    '      characteristicName 
    '          The name of the characteristic to get.
    '
    ' \return
    '      The string value of the characteristic. Will be null if the characteristic does Not exist
    '      Or Is Not a string.
    Function getCharacteristicFromObject(routeObject As RouteObject, characteristicName As String) As String

        Dim characteristicValue As String = Nothing

        Dim characteristics As CharacteristicList = routeObject.GetCharacteristics()
        Dim characteristicsInfo() As CharacteristicList.CharacteristicInformation = characteristics.GetCharacteristicTitlesByType(NXObject.AttributeType.Any)

        For Each characteristicInfo As CharacteristicList.CharacteristicInformation In characteristicsInfo

            If characteristicName = characteristicInfo.Name And
                characteristicInfo.Type = NXObject.AttributeType.String Then
                characteristicValue = characteristics.GetStringCharacteristic(characteristicName)
            End If

        Next

        getCharacteristicFromObject = characteristicValue

    End Function

    '-----------------------------------------------------------------------------------------------
    ' Returns the names of the ports to which the connector Is connected through a port connection.
    '
    ' \param[in]
    '      connector 
    '          The connector to check.
    '
    ' \return
    '      The names of the ports to which this connector Is connected. Will be null if the connector
    '      Is Not assigned to a component Or if the component's ports are not connected to any other
    '      ports.
    Function getConnectedPortNames(connector As ConnectorDevice) As String()

        If Not connector.IsAssigned Then
            Return Nothing
        End If

        Dim assignedComponent As Assemblies.Component = CType(connector.NxEquivalent, Assemblies.Component)
        If assignedComponent Is Nothing Then
            Return Nothing
        End If

        Dim routeManager As RouteManager = theSession.Parts.Work.RouteManager
        Dim assignedComponentPorts() As Port = routeManager.Ports.GetComponentPorts(assignedComponent)
        If assignedComponentPorts Is Nothing Then
            Return Nothing
        End If

        Dim connectedPortNames As New List(Of String)()

        Dim portConnections As PortConnectionCollection = routeManager.PortConnections
        For Each assignedComponentPort As Port In assignedComponentPorts

            Dim portConnection As PortConnection = portConnections.GetConnectionFromPort(assignedComponentPort)
            If portConnection Is Nothing Then
                Continue For
            End If

            Dim port1 As Port = Nothing
            Dim port2 As Port = Nothing
            portConnection.GetPorts(port1, port2)

            ' We know the port on the connector, so get the name from the other port in the connection.
            If assignedComponentPort Is port1 Then
                connectedPortNames.Add(port2.Name)
            Else
                connectedPortNames.Add(port1.Name)
            End If

        Next

        getConnectedPortNames = connectedPortNames.ToArray

    End Function

    '-----------------------------------------------------------------------------------------------
    Sub ModularConnectorDesignRule(reason As DesignRuleReason, nxObjects() As NXObject)

        If reason <> customManager.DesignRuleReason.Interactive Then
            Return
        End If

        Dim RouteManager As RouteManager = theSession.Parts.Work.RouteManager
        Dim connectors As ConnectorDeviceCollection = RouteManager.ConnectorDevices

        ' For every Connector Device that Is assigned And has a modular connector parent,
        ' check that the assigned component Is at the correct position (i.e. the correct port).
        For Each connector As ConnectorDevice In connectors

            If Not connector.IsAssigned Then
                Continue For
            End If

            Dim parentConnectorName As String = getCharacteristicFromObject(connector, UF.UFConstants.UF_RLIST_PARENT_ID_NAME)
            If (parentConnectorName Is Nothing) Then
                Continue For
            End If

            Dim parentPortName As String = getCharacteristicFromObject(connector, UF.UFConstants.UF_RLIST_PARENT_POSITION_NAME)
            If (parentPortName Is Nothing) Then
                Continue For
            End If

            Dim connectedCorrectly As Boolean = False
            Dim portNamesForMessage As String = Nothing
            Dim connectedPortNames() As String = getConnectedPortNames(connector)

            For Each connectedPortName As String In connectedPortNames

                portNamesForMessage += connectedPortName + ", "

                If connectedPortName = parentPortName Then
                    connectedCorrectly = True
                End If
            Next

            If Not connectedCorrectly Then

                Dim objects() As NXObject = New NXObject() {CType(connector.NxEquivalent, NXObject)}

                Dim message As String = "Connector " + connector.Name
                message += " is connected to port(s) " + portNamesForMessage
                message += "but should be connected to port " + parentPortName
                message += " on connector " + parentConnectorName + "."

                customManager.CreateViolationForReason("Modular Connector", reason,
                                                       "Component connected to wrong port.",
                                                       message, objects)
            End If

        Next

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Tells NX when to unload your application.
    ' For Routing callbacks, plugins, And Design Rules, this MUST return AtTermination.
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination
    End Function

End Module
