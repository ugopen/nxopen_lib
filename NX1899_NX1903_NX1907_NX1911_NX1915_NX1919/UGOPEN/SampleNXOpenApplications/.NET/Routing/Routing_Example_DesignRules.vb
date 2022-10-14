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
    Dim listingWindow As ListingWindow = Nothing
    Dim customManager As CustomManager = Nothing
    Dim createPathRuleId As Integer = 0
    Dim subdivideSegmentRuleId As Integer = 0

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

        RegisterDesignRules()

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

        RegisterDesignRules()
    End Sub

    '------------------------------------------------------------------------------------------
    ' Called by both Main And Startup to register the Design Rules.
    Sub RegisterDesignRules()

        Dim createPathName As String = "Create Path"
        Dim subdivideSegmentName As String = "Subdivide Segment"
        Dim createPathDescription As String = "The Create Path design rule makes sure each segment on the path is not too long."
        Dim subdivideSegmentDescription As String = "The Subdivide Segment design rule makes sure each new segment is not too short."

        createPathRuleId = customManager.AddDesignRule(customManager.DesignRuleReason.CreatePath, createPathName, createPathDescription, AddressOf CreatePathDesignRule)
        createPathRuleId = customManager.AddDesignRule(customManager.DesignRuleReason.SubdivideSegment, subdivideSegmentName, subdivideSegmentDescription, AddressOf SubdivideSegmentDesignRule)

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
    ' Tells NX when to unload your application.
    ' For Routing callbacks, plugins, And Design Rules, this MUST return AtTermination.
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination
    End Function

End Module
