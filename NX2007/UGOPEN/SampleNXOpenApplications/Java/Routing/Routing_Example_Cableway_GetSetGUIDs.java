/*=================================================================================================
                                       Copyright 2021 Siemens
===================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    An example program that gets and sets Globally Unique Identifiers (GUID) on control points
    and cableway network point occurrences.


=================================================================================================*/
import java.rmi.RemoteException;

import nxopen.Curve;
import nxopen.NXException;
import nxopen.NXMessageBox;
import nxopen.NXObject;
import nxopen.Point;
import nxopen.Selection;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.TaggedObject;
import nxopen.UI;
import nxopen.routing.*;
import nxopen.mechanicalrouting.*;
import nxopen.uf.UFConstants;

public class Routing_Example_Cableway_GetSetGUIDs
{
    //---------------------------------------------------------------------------------------------
    // Called from File->Execute->NX Open.
    public static void main(String[] argv) throws Exception
    {
        UI ui = (UI)SessionFactory.get( "UI" );

        try
        {
            // Allow control points and points.
            Selection.MaskTriple[] entityMask = setupEntityMasks();
            
            Selection.SelectTaggedObjectData selection = ui.selectionManager().selectTaggedObject( "Select a control point, segment, point, curve, or port", "Selection", 
                                                                                                     Selection.SelectionScope.ANY_IN_ASSEMBLY,
                                                                                                     Selection.SelectionAction.CLEAR_AND_ENABLE_SPECIFIC,
                                                                                                     false, false, entityMask );
            if ( selection.response == Selection.Response.OK ||
                 selection.response == Selection.Response.OBJECT_SELECTED || 
                 selection.response == Selection.Response.OBJECT_SELECTED_BY_NAME )
            {
                processSelection( selection.object );
            }
        }
        catch ( NXException ex)
        {
            ui.nxmessageBox().show( "Error", NXMessageBox.DialogType.ERROR, ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            ui.nxmessageBox().show( "Error", NXMessageBox.DialogType.ERROR, ex.getMessage() );
        }
    }

    //-----------------------------------------------------------------------------------------
    // Sets up the selection entity masks to allow:
    //
    //  - Control Points
    //  - Segments
    //  - Points
    //  - Curves
    //  - Ports
    private static Selection.MaskTriple[] setupEntityMasks()
    {
        final Selection.MaskTriple[] entityMasks = new Selection.MaskTriple[]
        {
            new Selection.MaskTriple( UFConstants.UF_route_control_point_type, 0, 0 ),
            new Selection.MaskTriple( UFConstants.UF_point_type, UFConstants.UF_point_subtype, 0 ),
            new Selection.MaskTriple( UFConstants.UF_line_type, 0, 0 ),
            new Selection.MaskTriple( UFConstants.UF_circle_type, 0, 0 ),
            new Selection.MaskTriple( UFConstants.UF_route_port_type, 0, 0 )
        };

        return entityMasks;
    }
    
    //---------------------------------------------------------------------------------------------
    public static void processSelection( TaggedObject selectedTaggedObject ) throws NXException, RemoteException
    {
        UI        ui               = (UI)SessionFactory.get( "UI" );
        NXObject  selectedObject  = (NXObject)selectedTaggedObject;
        
        if ( selectedObject instanceof ControlPoint )
        {
            // The GUID for a control point can be accessed directly through the GUID property.
            addGuidToControlPoint( (ControlPoint)selectedObject );
        }
        else if ( selectedObject instanceof ISegment )
        {
            // The GUID for a segment can be accessed directly through the GUID property.
            addGuidToSegment( (ISegment)selectedObject );
        }
        else if ( selectedObject instanceof Point )
        {
            // The GUID for a point from a component with qualified cableway network curves
            // (e.g. a tee or elbow) is stored as an attribute on the point occurrence
            // named CABLEWAY_EQUIPMENT_POINT_GUID.
            addGuidToObjectAttribute( selectedObject, "CABLEWAY_EQUIPMENT_POINT_GUID" );
        }
        else if ( selectedObject instanceof Curve )
        {
            // The GUID for a curve from a component with qualified cableway network curves
            // (e.g. a tee or elbow) is stored as an attribute on the curve occurrence
            // named CABLEWAY_EQUIPMENT_SEGMENT_GUID.
            addGuidToObjectAttribute( selectedObject, "CABLEWAY_EQUIPMENT_SEGMENT_GUID" );
        }
        else if (selectedObject instanceof Port )
        {
            // The GUID for a port of a hanger is stored as an attribute on the port occurrence
            // named CABLEWAY_HANGER_SEGMENT_GUID since a hanger is represented as a
            // zero length segment in Capital Router.
            addGuidToObjectAttribute( selectedObject, "CABLEWAY_HANGER_SEGMENT_GUID" );
        }
        else
        {
            ui.nxmessageBox().show( "Wrong Object Type", NXMessageBox.DialogType.INFORMATION, 
                                    "This program does not handle objects of type " + selectedObject.getClass().toString() );
        }
    }

    //--------------------------------------------------------------------------------------------------
    private static void addGuidToControlPoint
    (
        ControlPoint controlPoint
    ) throws RemoteException, NXException
    {
        if ( controlPoint.isOccurrence() )
        {
            controlPoint = (ControlPoint)controlPoint.prototype();
        }

        String originalGuid = controlPoint.guid();

        controlPoint.generateNewGuid();
        
        String newGuid = controlPoint.guid();            

        UI ui = (UI)SessionFactory.get( "UI" );
        ui.nxmessageBox().show( "Control Point", NXMessageBox.DialogType.INFORMATION, 
                                "Control Point's original GUID was '" + originalGuid + "'\n" +
                                "Changed it to '" + newGuid + "'" );
    }

    //--------------------------------------------------------------------------------------------------
    private static void addGuidToSegment
    (
        ISegment segment
    ) throws RemoteException, NXException
    {
        if ( segment.isOccurrence() )
        {
            segment = (ISegment)segment.prototype();
        }

        String originalGuid = segment.getGuid();

        segment.generateNewSegmentGuid();

        String newGuid = segment.getGuid();

        UI ui = (UI)SessionFactory.get( "UI" );
        ui.nxmessageBox().show( "Control Point", NXMessageBox.DialogType.INFORMATION, 
                                "Control Point's original GUID was '" + originalGuid + "'\n" +
                                "Changed it to '" + newGuid + "'" );
    }
    
    //--------------------------------------------------------------------------------------------------
    private static void addGuidToObjectAttribute
    (
        NXObject nxObject,
        String   attributeName 
    ) throws NXException, RemoteException
    {
        UI             ui         = (UI)SessionFactory.get( "UI" );
        Session        session    = (Session)SessionFactory.get("Session" );
        RoutingManager routingMgr = RoutingManagerFactory.GetRoutingManager( session );

        String originalGuid = getStringAttributeValueFromObject( nxObject, attributeName );

        routingMgr.addGuidToObjectAttribute( nxObject, attributeName );

        String newGuid = getStringAttributeValueFromObject( nxObject, attributeName );

        ui.nxmessageBox().show( "Object Occurrence", NXMessageBox.DialogType.INFORMATION,
                                "Object's original GUID was '" + originalGuid + "'\n" +
                                "Changed it to " + newGuid );
    }
    
    //----------------------------------------------------------------------------------------------
    // Returns the string value of the attribute or null if it does not exist.
    private static String getStringAttributeValueFromObject
    (
        NXObject nxObject,
        String   attributeName
    ) throws RemoteException, NXException
    {
        NXObject.AttributeInformation attributeInformation = getAttributeFromObject( nxObject, attributeName );
        if ( attributeInformation == null || attributeInformation.type != NXObject.AttributeType.STRING )
            return null;
                    
        return attributeInformation.stringValue;
    }

    //----------------------------------------------------------------------------------------------
    // Returns true and the attribute information object of the attribute if the attribute exists.
    // Returns false if not.
    private static NXObject.AttributeInformation getAttributeFromObject
    (
        NXObject nxObject,
        String   attributeName
    ) throws RemoteException, NXException
    {
        return getAttributeFromList( nxObject.getUserAttributes(), attributeName );
    }

    //----------------------------------------------------------------------------------------------
    // Returns true and the attribute information object of the attribute if the attribute is in the list.
    // Returns false if not.
    // NOTE: The attribute name comparison is case insensitive.
    private static NXObject.AttributeInformation getAttributeFromList
    (
        NXObject.AttributeInformation[] attributes,
        String                          attributeName
    )
    {
        for ( nxopen.NXObject.AttributeInformation attribute : attributes )
        {
            // Watch out for attributes with no title.
            if ( attribute.title.length() == 0 )
                continue;

            // NOTE: This does not look for aliases on the attribute titles.
            if ( attribute.title.compareToIgnoreCase( attributeName ) == 0 )
            {
                return attribute;
            }
        }

        return null;
    }

    //---------------------------------------------------------------------------------------------
    public static int getUnloadOption(String arg)
    {
        // Unloads the image immediately after execution within NX
        return Session.LibraryUnloadOption.IMMEDIATELY;
    }
}
