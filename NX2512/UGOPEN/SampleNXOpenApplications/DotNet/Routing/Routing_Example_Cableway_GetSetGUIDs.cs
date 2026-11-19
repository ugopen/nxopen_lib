/*==================================================================================================
                                       Copyright 2021 Siemens
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    An example program that gets and sets Globally Unique Identifiers (GUID) on control points
    and cableway network point occurrences.


==================================================================================================*/
using System;
using NXOpen;
using NXOpen.Routing;
using NXOpen.MechanicalRouting;
using NXOpen.UF;

namespace MechanicalRouting
{
    public class GetSetGUIDs
    {
        //------------------------------------------------------------------------------------------
        public static int Main( string[] args )
        {
            UI ui = UI.GetUI();
            try
            {
                // Allow control points and points.
                Selection.MaskTriple[] entityMasks = setupEntityMasks();

                TaggedObject selectedObject;
                Point3d      position;
                Selection.Response response = ui.SelectionManager.SelectTaggedObject( "Select a control point, segment, point, curve, or port", "Selection",
                                                                                      Selection.SelectionScope.AnyInAssembly,
                                                                                      Selection.SelectionAction.ClearAndEnableSpecific,
                                                                                      false, false, entityMasks,
                                                                                      out selectedObject, out position );
                if ( response == Selection.Response.Ok ||
                     response == Selection.Response.ObjectSelected ||
                     response == Selection.Response.ObjectSelectedByName )
                {
                    processSelection( selectedObject );
                }
            }
            catch ( NXException ex )
            {
                ui.NXMessageBox.Show( "Error", NXMessageBox.DialogType.Error, ex.Message );
            }
            catch ( Exception ex )
            {
                ui.NXMessageBox.Show( "Error", NXMessageBox.DialogType.Error, ex.Message );
            }

            return 0;
        }

        //-----------------------------------------------------------------------------------------
        // Sets up the selection entity masks to allow:
        //
        //  - Control Points
        //  - Segments
        //  - Points
        //  - Curves
        //  - Ports
        static Selection.MaskTriple[] setupEntityMasks()
        {
            Selection.MaskTriple[] entityMasks = new Selection.MaskTriple[5];

            entityMasks[0].Type = UFConstants.UF_route_control_point_type;
            entityMasks[0].Subtype = 0;
            entityMasks[0].SolidBodySubtype = 0;

            entityMasks[1].Type = UFConstants.UF_point_type;
            entityMasks[1].Subtype = UFConstants.UF_point_subtype;
            entityMasks[1].SolidBodySubtype = 0;

            entityMasks[2].Type = UFConstants.UF_line_type;
            entityMasks[2].Subtype = 0;
            entityMasks[2].SolidBodySubtype = 0;

            entityMasks[3].Type = UFConstants.UF_circle_type;
            entityMasks[3].Subtype = 0;
            entityMasks[3].SolidBodySubtype = 0;

            entityMasks[4].Type = UFConstants.UF_route_port_type;
            entityMasks[4].Subtype = 0;
            entityMasks[4].SolidBodySubtype = 0;

            return entityMasks;
        }

        //------------------------------------------------------------------------------------------
        private static void processSelection( TaggedObject selectedTaggedObject )
        {
            // Depending on the object selected, there are various means of changing the GUID.
            //
            //  Cableways:
            //      Control Point     - Call GenerateNewGuid.
            //      Segment           - Call GenerateNewGuid.
            //
            //  Equipment (e.g. tee or elbow):
            //      Point occurrence  - Call AddGuidToObjectAttribute with CABLEWAY_EQUIPMENT_POINT_GUID.
            //      Curve occurrence  - Call AddGuidToObjectAttribute with CABLEWAY_EQUIPMENT_SEGMENT_GUID.
            //
            //  Hanger:
            //      Port occurrence   - Call AddGuidToObjectAttribute with CABLEWAY_HANGER_SEGMENT_GUID.

            NXObject selectedObject = (NXObject)selectedTaggedObject;

            if ( selectedObject.GetType() == typeof( ControlPoint ) )
            {
                // The GUID for a control point can be accessed directly through the GUID property.
                AddGuidToControlPoint( (ControlPoint)selectedObject );
            }
            else if ( selectedObject.GetType() == typeof( ArcSegment ) ||
                      selectedObject.GetType() == typeof( LineSegment ) ||
                      selectedObject.GetType() == typeof( SplineSegment ) )
            {
                // The GUID for a segment can be accessed directly through the GUID property.
                AddGuidToSegment( (ISegment)selectedObject );
            }
            else if ( selectedObject.GetType() == typeof( NXOpen.Point ) )
            {
                // The GUID for a point from a component with qualified cableway network curves
                // (e.g. a tee or elbow) is stored as an attribute on the point occurrence
                // named CABLEWAY_EQUIPMENT_POINT_GUID.
                AddGuidToObjectAttribute( selectedObject, "CABLEWAY_EQUIPMENT_POINT_GUID" );
            }
            else if ( selectedObject.GetType().IsSubclassOf( typeof( NXOpen.Curve ) ) )
            {
                // The GUID for a curve from a component with qualified cableway network curves
                // (e.g. a tee or elbow) is stored as an attribute on the curve occurrence
                // named CABLEWAY_EQUIPMENT_SEGMENT_GUID.
                AddGuidToObjectAttribute( selectedObject, "CABLEWAY_EQUIPMENT_SEGMENT_GUID" );
            }
            else if ( selectedObject.GetType().IsSubclassOf( typeof( NXOpen.Routing.Port ) ) )
            {
                // The GUID for a port from a component with qualified cableway network curves
                // (e.g. a tee or elbow) is stored as an attribute on the port occurrence
                // named CABLEWAY_HANGER_SEGMENT_GUID.
                AddGuidToObjectAttribute( selectedObject, "CABLEWAY_HANGER_SEGMENT_GUID" );
            }
            else
            {
                UI.GetUI().NXMessageBox.Show( "Wrong Object Type", NXMessageBox.DialogType.Information,
                                              "This program does not handle objects of type " + selectedObject.GetType().ToString() );
            }
        }

        //--------------------------------------------------------------------------------------------------
        private static void AddGuidToControlPoint
        (
            ControlPoint controlPoint
        )
        {
            if ( controlPoint.IsOccurrence )
            {
                controlPoint = (ControlPoint)controlPoint.Prototype;
            }

            string originalGuid = controlPoint.Guid;

            controlPoint.GenerateNewGuid();

            string newGuid = controlPoint.Guid;

            UI.GetUI().NXMessageBox.Show( "Control Point", NXMessageBox.DialogType.Information,
                                          "Control Point's original GUID was '" + originalGuid + "'\n" +
                                          "Changed it to " + newGuid );
        }

        //--------------------------------------------------------------------------------------------------
        private static void AddGuidToSegment
        (
            ISegment segment
        )
        {
            if ( segment.IsOccurrence )
            {
                segment = (ISegment)segment.Prototype;
            }

            string originalGuid = segment.Guid;

            segment.GenerateNewGuid();

            string newGuid = segment.Guid;

            UI.GetUI().NXMessageBox.Show( "Segment", NXMessageBox.DialogType.Information,
                                          "Segment's original GUID was '" + originalGuid + "'\n" +
                                          "Changed it to " + newGuid );

        }

        //--------------------------------------------------------------------------------------------------
        private static void AddGuidToObjectAttribute
        (
            NXObject nxObject,
            String attributeName
        )
        {
            Session session = Session.GetSession();
            RoutingManager routingMgr = RoutingManager.GetRoutingManager( session );

            String originalGuid = GetStringAttributeValueFromObject( nxObject, attributeName );

            routingMgr.AddGuidToObjectAttribute( nxObject, attributeName );

            String newGuid = GetStringAttributeValueFromObject( nxObject, attributeName );

            UI.GetUI().NXMessageBox.Show( "Object Occurrence", NXMessageBox.DialogType.Information,
                                          "Object's original GUID was '" + originalGuid + "'\n" +
                                          "Changed it to " + newGuid );
        }

        //----------------------------------------------------------------------------------------------
        // Returns the string value of the attribute or null if it does not exist.
        private static String GetStringAttributeValueFromObject
        (
            NXObject nxObject,
            String attributeName
        )
        {
            NXObject.AttributeInformation attributeInformation;

            if ( GetAttributeFromObject( nxObject, attributeName, out attributeInformation ) )
                return attributeInformation.StringValue;

            return null;
        }

        //----------------------------------------------------------------------------------------------
        // Returns true and the attribute information object of the attribute if the attribute exists.
        // Returns false if not.
        private static bool GetAttributeFromObject
        (
            NXObject nxObject,
            String attributeName,
            out NXObject.AttributeInformation attributeInformation
        )
        {
            return GetAttributeFromList( nxObject.GetUserAttributes(), attributeName, out attributeInformation );
        }

        //----------------------------------------------------------------------------------------------
        // Returns true and the attribute information object of the attribute if the attribute is in the list.
        // Returns false if not.
        // NOTE: The attribute name comparison is case insensitive.
        private static bool GetAttributeFromList
        (
            NXObject.AttributeInformation[] attributes,
            String attributeName,
            out NXObject.AttributeInformation attributeInformation
        )
        {
            attributeInformation = new NXObject.AttributeInformation();

            foreach ( NXObject.AttributeInformation attribute in attributes )
            {
                String ucAttributeName = attributeName.ToUpper();
                String titleString = attribute.Title;

                // Watch out for attributes with no title.
                if ( titleString.Length == 0 )
                    continue;

                titleString = titleString.ToUpper();

                // NOTE: This does not look for aliases on the attribute titles.
                if ( titleString == ucAttributeName )
                {
                    attributeInformation = attribute;
                    return true;
                }
            }

            return false;
        }

        //------------------------------------------------------------------------------------------
        public static int GetUnloadOption( string arg )
        {
            // Unloads the image immediately after execution within NX
            return System.Convert.ToInt32( Session.LibraryUnloadOption.Immediately );
        }
    }
}
