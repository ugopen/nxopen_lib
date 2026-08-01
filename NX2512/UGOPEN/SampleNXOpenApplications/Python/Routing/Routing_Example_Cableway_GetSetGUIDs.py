#===================================================================================================
#                                       Copyright 2021 Siemens
#===================================================================================================
#
#    NOTE:  NX Development provides programming examples for illustration only.
#    NX Development assumes you are familiar with the programming language
#    demonstrated in these examples, and the tools used to create and debug NX/Open
#    programs. GTAC support professionals can help explain the functionality of
#    a particular procedure, but neither GTAC nor NX Development will modify
#    these examples to provide added functionality or construction procedures.
#
#File description:
#
#    An example program that gets and sets Globally Unique Identifiers (GUID) on control points
#    and cableway network point occurrences.
#
#
#==================================================================================================
import NXOpen
import NXOpen.Routing
import NXOpen.MechanicalRouting
import NXOpen.UF

#--------------------------------------------------------------------------------------------------
# Returns true and the attribute information object of the attribute if the attribute is in the list.
# Returns false if not.
# NOTE: The attribute name comparison is case insensitive.
def getAttributeFromList( attributes, attributeName ):
    
    for attribute in attributes:
        # Watch out for attributes with no title.
        if len( attribute.Title ) == 0:
            continue

        # NOTE: This does not look for aliases on the attribute titles.
        if attribute.Title.lower() == attributeName.lower():
            return attribute

    return None

#--------------------------------------------------------------------------------------------------
# Returns true and the attribute information object of the attribute if the attribute exists.
# Returns false if not.
def getAttributeFromObject( nxObject, attributeName ):
 
    return getAttributeFromList( nxObject.GetUserAttributes(), attributeName )

#--------------------------------------------------------------------------------------------------
# Returns the string value of the attribute or null if it does not exist.
def getStringAttributeValueFromObject( nxObject, attributeName ):
    
    attributeInformation = getAttributeFromObject( nxObject, attributeName );
    
    if attributeInformation == None or attributeInformation.Type != NXOpen.NXObject.AttributeType.String:
        return None;
        			
    return attributeInformation.StringValue

#--------------------------------------------------------------------------------------------------
def addGuidToControlPoint( controlPoint ):
  
    if controlPoint.IsOccurrence:
        controlPoint = NXOpen.Routing.ControlPoint( controlPoint.Prototype )
  
    originalGuid = controlPoint.GetGuid;
    
    controlPoint.GenerateNewGuid();

    newGuid = controlPoint.GetGuid;

    NXOpen.UI.GetUI().NXMessageBox.Show( "Control Point", NXOpen.NXMessageBox.DialogType.Information,
                                         "Control Point's original GUID was '" + originalGuid + "'\n" +
                                         "Changed it to " + newGuid );

    
#--------------------------------------------------------------------------------------------------
def addGuidToSegment( segment ):
  
    if segment.IsOccurrence:
        segment = NXOpen.Routing.ISegment( segment.Prototype )
        
    originalGuid = segment.GetGuid;
    
    segment.GenerateNewGuid();

    newGuid = segment.GetGuid;

    NXOpen.UI.GetUI().NXMessageBox.Show( "Segment", NXOpen.NXMessageBox.DialogType.Information,
                                         "Segment's original GUID was '" + originalGuid + "'\n" +
                                         "Changed it to " + newGuid );
  
#--------------------------------------------------------------------------------------------------
def addGuidToObjectAttribute( nxObject, attributeName ):

    session    = NXOpen.Session.GetSession()
    routingMgr = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager( session );

    originalGuid = getStringAttributeValueFromObject( nxObject, attributeName );

    routingMgr.AddGuidToObjectAttribute( nxObject, attributeName );

    newGuid = getStringAttributeValueFromObject( nxObject, attributeName );

    NXOpen.UI.GetUI().NXMessageBox.Show( "Object Occurrence", NXOpen.NXMessageBox.DialogType.Information,
                                         "Object's original GUID was '" + originalGuid + "'\n" +
                                         "Changed it to " + newGuid );

#--------------------------------------------------------------------------------------------------
# Sets up the selection entity masks to allow:
#
#  - Control Points
#  - Segments
#  - Points
#  - Curves
#  - Ports
def setupEntityMasks():
    
    entityMasks = []

    type = NXOpen.UF.UFConstants.UF_route_control_point_type;
    subtype = 0;
    solidBodySubtype = 0;
    entityMasks.append( NXOpen.Selection.MaskTriple( type, subtype, solidBodySubtype ) )

    type = NXOpen.UF.UFConstants.UF_point_type;
    subtype = NXOpen.UF.UFConstants.UF_point_subtype;
    solidBodySubtype = 0;
    entityMasks.append( NXOpen.Selection.MaskTriple( type, subtype, solidBodySubtype ) )

    type = NXOpen.UF.UFConstants.UF_line_type;
    subtype = 0;
    solidBodySubtype = 0;
    entityMasks.append( NXOpen.Selection.MaskTriple( type, subtype, solidBodySubtype ) )

    type = NXOpen.UF.UFConstants.UF_circle_type;
    subtype = 0;
    solidBodySubtype = 0;
    entityMasks.append( NXOpen.Selection.MaskTriple( type, subtype, solidBodySubtype ) )

    type = NXOpen.UF.UFConstants.UF_route_port_type;
    subtype = 0;
    solidBodySubtype = 0;
    entityMasks.append( NXOpen.Selection.MaskTriple( type, subtype, solidBodySubtype ) )

    return entityMasks

#--------------------------------------------------------------------------------------------------
def processSelection( selectedObject ):

    # Depending on the object selected, there are various means of changing the GUID.
    #
    #  Cableways:
    #      Control Point     - Call GenerateNewGuid.
    #      Segment           - Call GenerateNewGuid.
    #
    #  Equipment (e.g. tee or elbow):
    #      Point occurrence  - Call AddGuidToObjectAttribute with CABLEWAY_EQUIPMENT_POINT_GUID.
    #      Curve occurrence  - Call AddGuidToObjectAttribute with CABLEWAY_EQUIPMENT_SEGMENT_GUID.
    #
    #  Hanger:
    #      Port occurrence   - Call AddGuidToObjectAttribute with CABLEWAY_HANGER_SEGMENT_GUID.

    session         = NXOpen.Session.GetSession()
    listingWindow   = session.ListingWindow
    listingWindow.Open()

    listingWindow.WriteFullline( "Selected object is of type " + str( type( selectedObject ) ) )

    if issubclass( type( selectedObject ), NXOpen.Routing.ControlPoint ):
    
        # The GUID for a control point can be accessed directly through the GUID property.
        addGuidToControlPoint( NXOpen.Routing.ControlPoint( selectedObject.Prototype ) );

    elif issubclass( type( selectedObject ), NXOpen.Routing.LineSegment ):
    
        # The GUID for a segment can be accessed directly through the GUID property.
        addGuidToSegment( NXOpen.Routing.ISegment( selectedObject.Prototype ) );
       
    elif issubclass( type( selectedObject ), NXOpen.Point ):
        # The GUID for a point from a component with qualified cableway network curves
        # (e.g. a tee or elbow) is stored as an attribute on the point occurrence
        # named CABLEWAY_EQUIPMENT_POINT_GUID.
        addGuidToObjectAttribute( selectedObject, "CABLEWAY_EQUIPMENT_POINT_GUID" );

    elif issubclass( type( selectedObject ), NXOpen.Curve ):
        # The GUID for a curve from a component with qualified cableway network curves
        # (e.g. a tee or elbow) is stored as an attribute on the curve occurrence
        # named CABLEWAY_EQUIPMENT_SEGMENT_GUID.
        addGuidToObjectAttribute( selectedObject, "CABLEWAY_EQUIPMENT_POINT_GUID" );

    elif issubclass( type( selectedObject ), NXOpen.Routing.Port ):
        # The GUID for a port of a hanger is stored as an attribute on the port occurrence
        # named CABLEWAY_HANGER_SEGMENT_GUID since a hanger is represented as a
        # zero length segment in Capital Router.
        addGuidToObjectAttribute( selectedObject, "CABLEWAY_EQUIPMENT_POINT_GUID" );

    else:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Wrong Object Type", NXOpen.NXMessageBox.DialogType.Information,
                                             "This program does not handle objects of type " + str( type( selectedObject ) ) );

#--------------------------------------------------------------------------------------------------
def main():

    try:
        entityMasks = setupEntityMasks()
    
        output = NXOpen.UI.GetUI().SelectionManager.SelectTaggedObject( "Select a control point, segment, point, curve, or port", "Selection",
                                                                        NXOpen.SelectionSelectionScope.AnyInAssembly,
                                                                        NXOpen.SelectionSelectionAction.ClearAndEnableSpecific,
                                                                        False, False, entityMasks )
        if output[0] == NXOpen.SelectionResponse.Ok or \
           output[0] == NXOpen.SelectionResponse.ObjectSelected or \
           output[0] == NXOpen.SelectionResponse.ObjectSelectedByName:
            processSelection( output[1] )

    except NXOpen.NXException as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Error", NXOpen.NXMessageBox.DialogType.Error, str(ex) )
    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Error", NXOpen.NXMessageBox.DialogType.Error, str(ex) )

if __name__ == "__main__":
    main()
