'==================================================================================================
'                                       Copyright 2021 Siemens
'==================================================================================================
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
'    An example program that gets And sets Globally Unique Identifiers (GUID) On control points
'    And cableway network point occurrences.
'
'
'==================================================================================================
Option Strict On
Imports System
Imports NXOpen
Imports NXOpen.MechanicalRouting
Imports NXOpen.Routing
Imports NXOpen.UF

Module GetSetGUIDs

    '----------------------------------------------------------------------------------------------
    Sub Main()

        Dim ui As UI = ui.GetUI()

        Try
            ' Allow control points And points.
            Dim entityMask() As Selection.MaskTriple = setupEntityMasks()

            Dim selectedObject As TaggedObject = Nothing
            Dim position As Point3d
            Dim response As Selection.Response

            response = ui.SelectionManager.SelectTaggedObject("Select a control point, segment, or point", "Selection",
                                                               Selection.SelectionScope.AnyInAssembly,
                                                               Selection.SelectionAction.ClearAndEnableSpecific,
                                                               False, False, entityMask,
                                                               selectedObject, position)

            If (response = Selection.Response.Ok Or
                 response = Selection.Response.ObjectSelected Or
                 response = Selection.Response.ObjectSelectedByName) Then
                processSelection(selectedObject)
            End If

        Catch ex As NXException
            ui.NXMessageBox.Show("Error", NXMessageBox.DialogType.Error, ex.Message)
        Catch ex As Exception
            ui.NXMessageBox.Show("Error", NXMessageBox.DialogType.Error, ex.Message)
        End Try

    End Sub

    '----------------------------------------------------------------------------------------------
    ' Sets up the selection entity masks to allow:
    '
    '  - Control Points
    '  - Segments
    '  - Points
    '  - Curves
    '  - Ports
    Private Function setupEntityMasks() As Selection.MaskTriple()

        Dim entityMasks(5) As Selection.MaskTriple

        entityMasks(0).Type = UFConstants.UF_route_control_point_type
        entityMasks(0).Subtype = 0
        entityMasks(0).SolidBodySubtype = 0

        entityMasks(1).Type = UFConstants.UF_point_type
        entityMasks(1).Subtype = UFConstants.UF_point_subtype
        entityMasks(1).SolidBodySubtype = 0

        entityMasks(2).Type = UFConstants.UF_line_type
        entityMasks(2).Subtype = 0
        entityMasks(2).SolidBodySubtype = 0

        entityMasks(3).Type = UFConstants.UF_circle_type
        entityMasks(3).Subtype = 0
        entityMasks(3).SolidBodySubtype = 0

        entityMasks(4).Type = UFConstants.UF_route_port_type
        entityMasks(4).Subtype = 0
        entityMasks(4).SolidBodySubtype = 0

        Return entityMasks
    End Function

    '----------------------------------------------------------------------------------------------
    Private Sub processSelection(selectedTaggedObject As TaggedObject)

        Dim selectedObject As NXObject = CType(selectedTaggedObject, NXObject)

        If (TypeOf selectedObject Is ControlPoint) Then

            ' The GUID for a control point can be accessed directly through the GUID property.
            AddGuidToControlPoint(CType(selectedObject.Prototype, ControlPoint))

        ElseIf (TypeOf selectedObject Is ArcSegment Or
                TypeOf selectedObject Is LineSegment Or
                TypeOf selectedObject Is SplineSegment) Then

            ' The GUID for a segment can be accessed directly through the GUID property.
            AddGuidToSegment(CType(selectedObject.Prototype, ISegment))

        ElseIf (TypeOf selectedObject Is Point) Then

            ' The GUID for a point from a component with qualified cableway network curves
            ' (e.g. a tee Or elbow) Is stored as an attribute on the point occurrence
            ' named CABLEWAY_EQUIPMENT_POINT_GUID.
            AddGuidToObjectAttribute(selectedObject, "CABLEWAY_EQUIPMENT_POINT_GUID")

        ElseIf (TypeOf selectedObject Is Curve) Then

            ' The GUID for a point from a component with qualified cableway network curves
            ' (e.g. a tee Or elbow) Is stored as an attribute on the point occurrence
            ' named CABLEWAY_EQUIPMENT_SEGMENT_GUID.
            AddGuidToObjectAttribute(selectedObject, "CABLEWAY_EQUIPMENT_SEGMENT_GUID")

        ElseIf (TypeOf selectedObject Is Port) Then

            ' The GUID for a point from a component with qualified cableway network curves
            ' (e.g. a tee Or elbow) Is stored as an attribute on the point occurrence
            ' named CABLEWAY_HANGER_SEGMENT_GUID.
            AddGuidToObjectAttribute(selectedObject, "CABLEWAY_HANGER_SEGMENT_GUID")

        End If


    End Sub

    '-----------------------------------------------------------------------------------------------
    Private Sub AddGuidToControlPoint(controlPoint As ControlPoint)

        If (controlPoint.IsOccurrence) Then
            controlPoint = CType(controlPoint.Prototype, ControlPoint)
        End If

        Dim originalGuid As String = controlPoint.Guid

        controlPoint.GenerateNewGuid()

        Dim newGUid As String = controlPoint.Guid

        UI.GetUI().NXMessageBox.Show("Control Point", NXMessageBox.DialogType.Information,
                                     "Control Point's original GUID was '" + originalGuid + "'" + vbCrLf +
                                     "Changed it to '" + newGUid + "'")
    End Sub

    '-----------------------------------------------------------------------------------------------
    Private Sub AddGuidToSegment(segment As ISegment)

        If (segment.IsOccurrence) Then
            segment = CType(segment.Prototype, ISegment)
        End If

        Dim originalGuid As String = segment.Guid

        segment.GenerateNewGuid()

        Dim newGUid As String = segment.Guid

        UI.GetUI().NXMessageBox.Show("Segment", NXMessageBox.DialogType.Information,
                                     "Segment's original GUID was '" + originalGuid + "'" + vbCrLf +
                                     "Changed it to '" + newGUid + "'")

    End Sub

    '-----------------------------------------------------------------------------------------------
    Private Sub AddGuidToObjectAttribute(nxObject As NXObject, attributeName As String)

        Dim session As Session = session.GetSession()
        Dim routingMgr As RoutingManager = RoutingManager.GetRoutingManager(session)

        Dim originalGuid As String = GetStringAttributeValueFromObject(nxObject, attributeName)

        routingMgr.AddGuidToObjectAttribute(nxObject, attributeName)

        Dim newGuid As String = GetStringAttributeValueFromObject(nxObject, attributeName)

        UI.GetUI().NXMessageBox.Show("Object Occurrence", NXMessageBox.DialogType.Information,
                                      "Object's original GUID was '" + originalGuid + "'" + vbCrLf +
                                      "Changed it to '" + newGuid + "'")
    End Sub

    '----------------------------------------------------------------------------------------------
    ' Returns the string value of the attribute Or null if it does Not exist.
    Private Function GetStringAttributeValueFromObject(ByVal nxObject As NXObject,
                                                 ByVal attributeName As String) As String

        Dim attributeInformation As NXObject.AttributeInformation = Nothing

        If GetAttributeFromObject(nxObject, attributeName, attributeInformation) Then
            Return attributeInformation.StringValue
        End If

        Return Nothing

    End Function

    '----------------------------------------------------------------------------------------------
    ' Returns true And the attribute information object of the attribute if the attribute exists.
    ' Returns false if Not.
    Private Function GetAttributeFromObject(ByVal nxObject As NXObject,
                                            ByVal attributeName As String,
                                            ByRef attributeInformation As NXObject.AttributeInformation) As Boolean

        If (GetAttributeFromList(nxObject.GetUserAttributes(), attributeName, attributeInformation)) Then
            Return True
        End If

        Return False

    End Function

    '----------------------------------------------------------------------------------------------
    ' Returns true And the attribute information object of the attribute if the attribute Is in the list.
    ' Returns false if Not.
    ' NOTE: The attribute name comparison Is Case insensitive.
    Private Function GetAttributeFromList(ByVal attributes() As NXObject.AttributeInformation,
                                          ByVal attributeName As String,
                                          ByRef attributeInformation As NXObject.AttributeInformation) As Boolean

        For Each attribute As NXObject.AttributeInformation In attributes

            Dim ucAttributeName As String = attributeName.ToUpper

            Dim titleString As String = attribute.Title

            ' Watch out for attributes with no title.
            If titleString.Length() = 0 Then
                Continue For
            End If

            titleString = titleString.ToUpper()

            ' NOTE: This does not look for aliases on the attribute titles.
            If titleString = ucAttributeName Then
                attributeInformation = attribute
                Return True
            End If
        Next

        Return False

    End Function

    '----------------------------------------------------------------------------------------------
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        ' Unloads the image immediately after execution within NX
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination
    End Function

End Module
