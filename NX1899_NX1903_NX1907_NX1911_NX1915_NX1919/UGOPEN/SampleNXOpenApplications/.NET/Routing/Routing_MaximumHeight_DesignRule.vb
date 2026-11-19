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
'    A Visual Basic module that implements Maximum Height Violation Routing Design Rule.
'
'
'===================================================================================================
Option Strict On
Imports System
Imports System.Collections
Imports System.Collections.Generic
Imports NXOpen
Imports NXOpen.Routing
Imports NXOpen.Routing.Electrical
Imports NXOpen.Routing.CustomManager
Imports NXOpen.Preferences

Module MaxHeightDesignRules

    Dim theSession As Session = Nothing
    Dim listingWindow As ListingWindow = Nothing
    Dim customManager As CustomManager = Nothing

    Dim m_maxHeightRuleForCreatePath As Integer = 0
    Dim m_maxHeightRuleForHealPath As Integer = 0
    Dim m_maxHeightRuleForAssignCorner As Integer = 0
    Dim m_maxHeightRuleForAssignStock As Integer = 0
    Dim m_maxHeightRuleForRemovePart As Integer = 0
    Dim m_maxHeightRuleForAutoRoutePinLevel As Integer = 0
    Dim m_maxHeightRuleForManualRoutePinLevel As Integer = 0
    Dim m_maxHeightRuleForAutoRouteComponentLevel As Integer = 0
    Dim m_maxHeightRuleForManualRouteComponentLevel As Integer = 0
    Dim m_maxHeightRuleForInteractive As Integer = 0
    Dim m_maxHeightRuleForTransformPath As Integer = 0
    Dim m_maxHeightRuleForEditCharacteristic As Integer = 0

    '-----------------------------------------------------------------------------------------------
    ' Called when NX starts up to register the Design Rules.
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

        RegisterMaximumHeightDesignRules()

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

        RegisterMaximumHeightDesignRules()
    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Get the the double value from attribute
    '
    ' \param[in]
    '      attributeInfo
    '          Attribute information from which double needs to be queried
    '
    ' \return
    '      Value of attribute as double
    Function getRealValue(ByRef attributeInfo As NXObject.AttributeInformation) As Double

        Dim type As NXObject.AttributeType = attributeInfo.Type

        Select Case (type)
            Case NXObject.AttributeType.Real
                Return attributeInfo.RealValue

            Case NXObject.AttributeType.Integer
                Return System.Convert.ToDouble(attributeInfo.IntegerValue)

            Case NXObject.AttributeType.String
                Return System.Convert.ToDouble(attributeInfo.StringValue)

            Case Else
                Dim msgBox As NXMessageBox = Nothing
                msgBox.Show("Maximum Height Violation", NXMessageBox.DialogType.Information, "Invalid Attribute Type")
                Return 0.0
        End Select

    End Function
    '-----------------------------------------------------------------------------------------------
    ' Queries the overstock referencing the segment
    '
    ' \param[in]
    '      segment
    '         Segment from which referencing overstock needs to be queried.
    ' \param[in]
    '      routeManager
    '          RouteManager from the current work part
    ' \return
    '          Set of overstocks referencing the segment
    Function getOverstocksPresentOnTheSegment(ByRef segment As ISegment, ByRef routeManager As RouteManager) As SortedSet(Of Overstock)

        Dim overstockSet = New Collections.Generic.SortedSet(Of Overstock)

        Dim overstockApplicationCollection As OverstockApplicationCollection = routeManager.OverstockApplications

        For Each overstockApplication As OverstockApplication In overstockApplicationCollection

            Dim overstockSegments As ISegment() = overstockApplication.GetSegments
            For Each segmentItr In overstockSegments
                If (segmentItr.Equals(segment)) Then
                    overstockSet.Add(overstockApplication.GetOverstocks(0))
                End If
            Next
        Next

        Return overstockSet
    End Function
    '-----------------------------------------------------------------------------------------------
    ' Queries the list of stock devices routing through the segment
    '
    ' \param[in]
    '      segment
    '          Segment through which stock devices are routed.
    ' \param[in]
    '      routeManager
    '          RouteManager from the current work part
    ' \return
    '      stockDevices
    '          List of stock stock devices referencing the segment
    Function getStockDevicesRoutedThroughSegment(ByRef segment As ISegment, ByRef routeManager As RouteManager) As List(Of StockDevice)

        Dim stockDevicesRoutingThroughSegment As New List(Of StockDevice)

        Dim allStockDevices As ElectricalStockDeviceCollection = routeManager.ElectricalStockDevice

        For Each stockDevice As StockDevice In allStockDevices

            Dim wireObject As Wire = CType(stockDevice.NxEquivalent, Wire)
            If wireObject Is Nothing Then
                Continue For
            End If

            Dim stockDeviceSegments As ISegment() = wireObject.GetSegments

            For Each singleSegment In stockDeviceSegments
                If singleSegment IsNot segment Then
                    Continue For
                End If
                If Not stockDevicesRoutingThroughSegment.Contains(stockDevice) Then
                    stockDevicesRoutingThroughSegment.Add(stockDevice)
                End If
            Next

        Next

        Return stockDevicesRoutingThroughSegment

    End Function
    '-----------------------------------------------------------------------------------------------
    ' Gets the real value of input attribute, if present on the object
    '
    ' \param[in]
    '      nxObject
    '          Object from which attribute value needs to be queried
    ' \param[in]
    '      attributeName
    '          Title or name of attribute that needs to be queried.
    ' \return
    '          Value of the attribute
    Function getAttributeValue(ByRef nxObject As NXObject, ByVal attributeName As String) As Double

        Dim attributesInfoList As NXObject.AttributeInformation() = nxObject.GetUserAttributes()

        For Each attributesInfo As NXObject.AttributeInformation In attributesInfoList
            If (attributesInfo.Title = attributeName) Then
                Return getRealValue(attributesInfo)
            End If
        Next
        Return 0

    End Function
    '-----------------------------------------------------------------------------------------------
    ' This method gives diameter of maximum size connection amongst the stock devices routing through the segment
    '
    ' \param[in]
    '      segment
    '          Segment through which connections are routed
    ' \param[in]
    '      stockDevices
    '          List of stock devices routed through the segment
    ' \return
    '          Maximum size diameter 
    Function getValueToCheckMaxHeightViolationForStockDevice(ByRef segment As ISegment, ByRef stockDevices As List(Of StockDevice)) As Double

        Dim largestDiameter As Double = 0

        For Each stockDevice In stockDevices
            Dim maxValue As Double = 0.0
            Dim stockDef As StockDefinition = Nothing

            Dim electricalStockDevice As ElectricalStockDevice = CType(stockDevice, ElectricalStockDevice)

            If electricalStockDevice IsNot Nothing Then
                Dim cableDefinition As CableDefinition = electricalStockDevice.FindTopmostCableDefinition
                If cableDefinition IsNot Nothing Then

                    Dim cableDevice As CableDevice = Nothing
                    cableDevice = CType(cableDefinition.GetReferencingDevice, CableDevice)

                    If cableDevice Is Nothing Then
                        Continue For
                    End If

                    stockDef = cableDevice.StockDefinition
                Else
                    stockDef = electricalStockDevice.StockDefinition
                End If
            End If
            maxValue = stockDef.OuterDiameter

            If maxValue > (largestDiameter + 0.00001) Then
                largestDiameter = maxValue
            End If

        Next

        Return largestDiameter

    End Function
    '-----------------------------------------------------------------------------------------------
    ' Check the maximum diameter of connection routing through given segment against the maximum allowed height.
    '
    ' Creates a violation for the given reason if connection diameter exceeds specified Maximum Height value.
    '
    ' \param[in]
    '      routeManager
    '          RouteManager from current work part
    '
    ' \param[in]
    '      customManager
    '          CustomManager to create design Rule violation.
    '
    ' \param[in]
    '      segment
    '          Routing Segment to be check for Maximum Height violation
    '
    ' \param[in]
    '      reason
    '          Design Rule reason for which Maximum Height Violation needs to be checked.
    Sub checkForMaximumHeightViolation(ByRef routeManager As RouteManager, ByRef customManager As CustomManager,
                                       ByVal segment As ISegment, ByVal reason As CustomManager.DesignRuleReason)

        Dim maxHeightAttributeName As String = "CABLETRAY_MAXHEIGHT"
        Dim segmentObject As NXObject = CType(segment, NXObject)

        'Get value of allowed Maximum Height or Specified Maximum Height
        Dim specifiedMaxHeightValue As Double = getAttributeValue(segmentObject, maxHeightAttributeName)
        If Math.Abs(specifiedMaxHeightValue) < 0.00001 Then
            Return
        End If

        ' Get list of Stock Devices routing through the segment
        Dim stockDevicesRoutingThroughSegment As List(Of StockDevice) = getStockDevicesRoutedThroughSegment(segment, routeManager)

        ' Get max value diameter of connection routing through the segment
        Dim largestDiameter As Double = getValueToCheckMaxHeightViolationForStockDevice(segment, stockDevicesRoutingThroughSegment)

        ' Get Overstocks referencing the segment
        Dim overstockSet As Collections.Generic.SortedSet(Of Overstock) = getOverstocksPresentOnTheSegment(segment, routeManager)

        ' If Overstocks are present on segment, get maximum value of diameter including overstock
        If (overstockSet.Count > 0) Then
            Dim totalThickness As Double = 0.0
            For Each overstock In overstockSet
                totalThickness += overstock.GetThickness.Value
            Next
            largestDiameter += (2 * totalThickness)
        End If

        ' If current value of diameter is greater than specified maximum height value then raise violation.
        If largestDiameter > (specifiedMaxHeightValue + 0.00001) Then
            Dim objects() As Curve = New Curve() {CType(segment, Curve)}
            Dim description As String = "The stock exceeds the maximum height allowed for this segment. The current height is " & Convert.ToString(largestDiameter) & ".The allowed height is " & Convert.ToString(specifiedMaxHeightValue) & "."
            customManager.CreateViolationForReason("Maximum Height Violation", reason, "The segment violates Maximum Height Rule.", description, objects)
        End If

        overstockSet.Clear()
        stockDevicesRoutingThroughSegment.Clear()

    End Sub

    '------------------------------------------------------------------------------------------
    ' Called by both Main And Startup to register the Design Rules.
    Sub RegisterMaximumHeightDesignRules()

        Dim maxHeightViolationTitle As String = "Maximum Height Violation"
        Dim maxHeightViolationDescription As String = "The Maximum Height design rule makes sure the diameter of each individual connection is within the permissible limit of value specified by attribute CABLETRAY_MAXHEIGHT."

        ' Add Design rule for the reasons for which Design needs to be executed.
        m_maxHeightRuleForCreatePath = customManager.AddDesignRule(customManager.DesignRuleReason.CreatePath, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForHealPath = customManager.AddDesignRule(customManager.DesignRuleReason.HealPath, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForAssignCorner = customManager.AddDesignRule(customManager.DesignRuleReason.AssignCorner, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForAssignStock = customManager.AddDesignRule(customManager.DesignRuleReason.AssignStock, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForRemovePart = customManager.AddDesignRule(customManager.DesignRuleReason.RemovePart, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForAutoRoutePinLevel = customManager.AddDesignRule(customManager.DesignRuleReason.AutoRoutePinLevel, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForManualRoutePinLevel = customManager.AddDesignRule(customManager.DesignRuleReason.ManualRoutePinLevel, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForAutoRouteComponentLevel = customManager.AddDesignRule(customManager.DesignRuleReason.AutoRouteComponentLevel, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForManualRouteComponentLevel = customManager.AddDesignRule(customManager.DesignRuleReason.ManualRouteComponentLevel, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForInteractive = customManager.AddDesignRule(customManager.DesignRuleReason.Interactive, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForTransformPath = customManager.AddDesignRule(customManager.DesignRuleReason.TransformPath, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)
        m_maxHeightRuleForEditCharacteristic = customManager.AddDesignRule(customManager.DesignRuleReason.EditCharacteristic, maxHeightViolationTitle, maxHeightViolationDescription, AddressOf CreateMaximumHeightDesignRule)

    End Sub
    '-----------------------------------------------------------------------------------------------
    Sub CreateMaximumHeightDesignRule(ByVal reason As DesignRuleReason, ByVal nxObjects As NXObject())

        If reason = DesignRuleReason.Interactive Then

            ' For interactive checks, check all the segments in the work part.
            Dim segmentManager As SegmentManager = theSession.Parts.Work.SegmentManager
            Dim segmentCollection As ISegmentCollection = segmentManager.Segments

            For Each segment As ISegment In segmentCollection
                checkForMaximumHeightViolation(theSession.Parts.Work.RouteManager, theSession.RouteCustomManager, segment, reason)
            Next

            Return
        End If

        ' Otherwise, check the segments in the given list of objects.
        For Each nxObject As NXObject In nxObjects
            If TypeOf nxObject Is Routing.ISegment Then
                checkForMaximumHeightViolation(theSession.Parts.Work.RouteManager, theSession.RouteCustomManager, CType(nxObject, ISegment), reason)
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
