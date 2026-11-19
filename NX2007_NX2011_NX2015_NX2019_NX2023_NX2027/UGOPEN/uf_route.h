/*******************************************************************************
                           Copyright 2007 UGS Corp.
                       Unpublished - All Rights Reserved



File description:

    Open C API interface to the Routing (ROUTE) module.

The Routing module within NX provides functions to model
the systems within an overall assembly which supply power, dispose of
waste, provide structural support, or enable general access to the
devices in the assembly. It is a set of common functions appropriate to
the modeling of various types of routing applications, such as Piping,
Tubing, Conduit, etc.
See the Routing User Guide for an overview of the routing design
process and a description of Routing Application Views.

Concepts and Terminology:
-------------------------
Included within the Routing module are functions to define the paths
through an assembly, to assign stock (e.g., pipes, tubes) to these paths,
and to place standard parts (e.g., tees, elbows) to connect the various
pieces of stock in the assembly.

Because Routing is a generic module which supports various
applications, you must select specific capabilities for your particular
use. This is accomplished through the "loading" of a particular
Routing Application View.  The Application View selects the specific
Routing capabilities and customizable options that are in effect
while creating and modifying Routing objects. The application view
can also define user preferences; values keyed by name are available to
you while your application is running. See UF_ROUTE_ask_user_preferences
and the application view documentation for more information.

Once an Application View has been loaded and made the current
Application View, you may use the Routing functions described in this
chapter to build your routing assembly. This involves the definition of
the paths along which stock is to be placed and the placement of
standard parts within the assembly.

Routing Control Points (RCPs) are used to define positions within the
routing assembly. RCPs are connected to one another by the creation
of routing Segments. Segments can be a simple linear connection
between RCPs or may be defined to follow an existing NX
curve. The available curve types which a Segment may follow are
defined by the Application View.

A set of connected Segments is referred to as a routing. The set of
Segments between any two RCPs is referred to as a path.

Once the Segments have been created, you may assign the stock
(pipe, tube, etc.) that should exist along those Segments. A particular
type of stock is defined within a separate NX part file and
the information about the stock is read from the stock part and
included in the current work part. Once this information has been
included in the current work part, you may assign this stock to one or
more sets of Segments within the assembly. A Stock Data object is the
NX object which maintains the common information about
the stock. A Stock object is used to point to this Stock Data object and
the Segments to which this stock has been assigned.
You may also create Bend or Miter Corners at the intersection of 2
Segments to model the bending or mitering of the stock along those
Segments. Bend corners may be created by means of a radius, a ratio to
the diameter, or through a table. Bend radius tables are specified in
the application view. You must know the table name to create the corner.

In addition to the creation of paths and the assignment of stock, you
may place standard parts such as fittings, connectors, and devices,
within the overall assembly. You add such a part as an assembly
components of the current work part and then instruct the Routing
module to "set" this part within the Routing assembly. Routing
automatically determines which Segments the component part has
been placed upon and adjusts the Segments to match the connection
points, known as routing Ports, defined within the part. Orientation
and positioning of the component is handled through the the normal
Assembly functions for adding a component.

Both Stock parts and Fitting parts must be qualified for use by the
Routing module prior to their use by the Routing functions. See the
Routing User Guide for an explanation of the Qualify Part
function. A part, either stock or fitting, need only be qualified once
prior to its use. Sample Stock and Fitting parts are provided with the
Routing product.

A Stock or Fitting part may be a NX Part Family, in which
case you must specify both the part (family) name and the member
name when defining which part to use for a particular operation.

Additional information about Stock objects and Fitting parts for use
by downstream applications may be attached to these objects through
the assignment of Routing characteristics (attributes). Examples of
Routing characteristics might include Material Type, Rating, NPS
(Nominal Pipe Size), and others specified by the Application View.

Characteristics (charx) can be assigned interactively during part qualify,
in the part library, or programmatically. A charx has a type and a title.
It also has a value, which can be a char *, double, or int. Refer to
the documentation for uf_eplib_types.h for more information on the
internals of charx.

Shown below are definitions for various terms used throughout this
documentation. Refer to the Routing User Guide for a complete
glossary of Routing terms.

Application View - A collection of specific Routing capabilities and
attributes that are available to a routing application.  Examples of routing
applications are piping, conduit, tubing, steelwork, raceway, and flexible hose.

characteristic - A datum used in Routing to maintain information which
describes routing objects and records the intended use of the objects.  This
information is used to access standard parts and for other processes such as
design rules, analysis, manufacturing, and BOM reporting.

path - The set of all RCPs (and assigned stock and fittings) between any two
RCPs within a routing.

path segment - A portion of a path between two routing control points.

port - A routing object data element used to specify a connection location,
alignment, or relative orientation with another routing object.

routing control point (RCP) - A position used to control a path.

standard part - A part that has been selected for use on a project because it
meets form, fit, and function requirements of the site.  Standard parts reside
in the standard part library.

stock data - A routing object that contains the cross-sectional and related
characteristics of a stock. There is only one stock_data object for any number
of stock of the same type. For example, all sections of 3 inch steel pipe in
the routing will reference the same stock_data object.

stock - A section of a routing assembly cut from a standard part which is sold
in standard lengths or rolls.  For example: wire, tube or pipe.

nested stock - Stock can be considered as nested when a segment is used to
define the path for more than one routing stock. These multiple stocks on
a segment could belong to the same application( e.g. Pipe inside a bigger
pipe) or different applications ( Wire or a bundle inside a conduit ).

Development Tips:
------------------
.    When creating routing objects with UF_ROUTE_create... functions, it
     is a recommended practice to add them to the current display with
     UF_DISP_add_item_to_display.  The newly created routing objects will
     then be visible in the graphics display without a display regenerate.

Routing functions:
------------------
The subroutines in this header file provide access to creation and
manipulations of routing objects in NX.

The routines in the header file  allow you to:
.    Load and set an Application View.
.    Create RCPs and Segments.
.    Assign Corners such as Bend and Miter.
.    Assign Stocks or Nested Stocks to Segments.
.    Place standard parts within the overall routing.


Retired functions:
------------------
The following functions have been retired and replaced with newer NX Open classes and methods:

    UF_ROUTE_add_terminal_ports                 Routing::MultiPort::AddTerminalPorts
    UF_ROUTE_add_virtual_ports                  Routing::MultiPort::AddVirtualPorts
    UF_ROUTE_are_ports_connectable              Routing::PortConnectionCollection::CanPortsConnect
    UF_ROUTE_ask_connection_ports               Routing::PortConnection::GetPorts
    UF_ROUTE_ask_multiport_strings              Routing::MultiPort::GetVirtualPorts
    UF_ROUTE_ask_multiport_tags                 Routing::MultiPort::GetTerminalPorts
    UF_ROUTE_ask_object_port                    Routing::PortCollection::GetObjectPorts
    UF_ROUTE_ask_part_occ_ports                 Routing::PortCollection::GetComponentPorts
    UF_ROUTE_ask_port_align_flag                Routing::Port::GetAlignmentVector
    UF_ROUTE_ask_port_align_vector              Routing::Port::GetAlignmentVector
    UF_ROUTE_ask_port_back_extension            Routing::Port::GetBackExtension
    UF_ROUTE_ask_port_back_extension_obj        Routing::Port::GetBackExtensionObject
    UF_ROUTE_ask_port_charx                     Routing::Port::GetCharacteristics
    UF_ROUTE_ask_port_clock_increment           Routing::Port::GetClockIncrement
    UF_ROUTE_ask_port_conn_port                 Routing::Port::GetConnectedPorts
    UF_ROUTE_ask_port_connected_port            Routing::Port::GetConnectedPorts
    UF_ROUTE_is_port_connected                  Routing::Port::GetConnectedPorts
    UF_ROUTE_ask_port_connection                Routing::Port::GetPortConnection
    UF_ROUTE_ask_port_cut_back_length           Routing::Port::GetCutbackLength
    UF_ROUTE_ask_port_engage_obj                Routing::IAxisPort::EngagementObject
    UF_ROUTE_ask_port_engaged_pos               Routing::Port::EngagementPosition
    UF_ROUTE_ask_port_engagement                Routing::Port::GetEngagement
    UF_ROUTE_ask_port_extension                 Routing::Port::GetForwardExtension
    UF_ROUTE_ask_port_extension_obj             Routing::Port::GetForwardExtensionObject
    UF_ROUTE_ask_port_lock_info                 Routing::Port::IsEngagementLocked and Routing::Port::IsRotationLocked
    UF_ROUTE_ask_port_multiport                 Routing::TerminalPort::MultiPort
    UF_ROUTE_ask_port_occ_of_port               Routing::Port::GetPortOccurrence
    UF_ROUTE_ask_port_part_occ                  Routing::Port::GetComponent
    UF_ROUTE_ask_port_position                  Routing::Port::Position
    UF_ROUTE_ask_port_rotate_flag               Routing::Port::GetRotationVector
    UF_ROUTE_ask_port_rotate_vector             Routing::Port::GetRotationVector
    UF_ROUTE_ask_port_segment                   Routing::StockPort::GetSegment
    UF_ROUTE_ask_port_on_segment                Routing::StockPort::GetSegment
    UF_ROUTE_ask_port_stock                     Routing::StockPort::GetStock
    UF_ROUTE_ask_port_terminal_ports            Routing::MultiPort::GetTerminalPorts
    UF_ROUTE_ask_rcp_at_term_port               Routing::Port::GetControlPoint
    UF_ROUTE_ask_terminal_multiport             Routing::TerminalPort::MultiPort
    UF_ROUTE_ask_terminal_port_uid              Routing::TerminalPort::PinIdentifier
    UF_ROUTE_check_design_rules                 Routing::RouteManager::CheckDesignRules
    UF_ROUTE_connect_port                       Routing::TerminalPort::Connect
    UF_ROUTE_create_design_rule_vio             Routing::DesignRule::CreateViolation
    UF_ROUTE_create_multiport_from_position     Routing::MutliPortCollection::CreateMultiPort
    UF_ROUTE_create_port_at_segend              Routing::StockPortCollection::CreateStockPort
    UF_ROUTE_create_port_lock                   Routing::Port::LockEngagement or Routing::Port::LockRotation
    UF_ROUTE_delete_port_lock                   Routing::Port::LockEngagement or Routing::Port::LockRotation
    UF_ROUTE_disconnect_port                    Routing::Port::Disconnect
    UF_ROUTE_find_port_charx                    Routing::Port::GetCharacteristics
    UF_ROUTE_find_terminal_port                 Routing::Port::GetTerminalPorts
    UF_ROUTE_is_port_fixture_port               Use the FixturePort class type to determine if this is a Fixture Port.
    UF_ROUTE_is_port_multi                      Use the MultiPort class type to determine if this is a MultiPort.
    UF_ROUTE_is_port_terminal                   Use the TerminalPort class type to determine if this is a Terminal Port.
    UF_ROUTE_remove_terminal_ports              Routing::MultiPort::RemoveTerminalPorts
    UF_ROUTE_remove_virtual_ports               Routing::MultiPort::RemoveVirtualPorts
    UF_ROUTE_set_port_back_extension            Routing::Port::SetBackExtension
    UF_ROUTE_set_port_back_extension_obj        Routing::Port::SetBackExtensionObject
    UF_ROUTE_set_port_clock_increment           Routing::Port::SetClockIncrement
    UF_ROUTE_set_port_engagement                Routing::IAxisPort::SetEngagement
    UF_ROUTE_set_port_engagement_obj            Routing::IAxisPort::EngagementObject
    UF_ROUTE_set_port_extension                 Routing::IAxisPort::ForwardExtension
    UF_ROUTE_set_port_extension_obj             Routing::IAxisPort::ForwardExtensionObject
    UF_ROUTE_set_port_id                        Routing::Port::SetCharacteristic to set the UNIQUE_ID characteristic.
    UF_ROUTE_set_port_lock_rotation_flag        Routing::Port::LockRotation
    UF_ROUTE_set_port_rot_by_point              Routing::Port::LockRotation
    UF_RULE_add_rule_violations                 Routing::DesignRule::CreateViolation
    UF_RULE_add_violation_objects               Routing::DesignRuleViolation::AddObjects
    UF_RULE_ask_object_violations               Routing::DesignRuleManager::GetObjectViolations
    UF_RULE_ask_override_reason                 Routing::DesignRuleOverride::GetReason
    UF_RULE_ask_override_time_stamp             Routing::DesignRuleOverride::GetTimeStamp
    UF_RULE_ask_override_violations             Routing::DesignRuleOverride::GetViolation
    UF_RULE_ask_override_user                   Routing::DesignRuleOverride::GetUser
    UF_RULE_ask_rule_description                Routing::DesignRule::GetDescription
    UF_RULE_ask_rule_name                       Routing::DesignRule::Drname
    UF_RULE_ask_rule_vios                       Routing::DesignRule::GetViolations
    UF_RULE_ask_vio_objects                     Routing::DesignRuleViolation::GetObjects
    UF_RULE_ask_vio_override                    Routing::DesignRuleViolation::GetOverride
    UF_RULE_ask_vio_rule                        Routing::DesignRuleViolation::GetOwningDesignRule
    UF_RULE_ask_vio_short_desc                  Routing::DesignRuleViolation::GetShortDescription
    UF_RULE_ask_vio_time_stamp                  Routing::DesignRuleViolation::GetTimeStamp
    UF_RULE_check_rule                          Routing::RouteManager::CheckDesignRules
    UF_RULE_check_rules                         Routing::RouteManager::CheckDesignRules
    UF_RULE_create_override                     Routing::DesignRuleViolation::SetViolationOverride
    UF_RULE_create_rule                         Routing::CustomManager::AddDesignRule
    UF_RULE_create_violation                    Routing::DesignRule::CreateViolation
    UF_RULE_is_violation_overridden             Routing::DesignRuleViolation::IsRuleOverridden
    UF_RULE_is_violation_since                  Routing::DesignRuleViolation::GetTimeStamp
    UF_RULE_set_override_reason                 Routing::DesignRuleOverride::SetReason
    UF_RULE_set_override_time_stamp             Routing::DesignRuleOverride::SetTimeStamp
    UF_RULE_set_override_user                   Routing::DesignRuleOverride::SetUser
    UF_RULE_set_rule_description                Routing::DesignRule::SetDescription
    UF_RULE_set_rule_name                       Routing::DesignRule::SetName
    UF_RULE_set_rule_violations                 Routing::DesignRule::CreateViolation
    UF_RULE_set_vio_long_desc                   Routing::DesignRuleViolation::SetLongDescription
    UF_RULE_set_vio_objects                     Routing::DesignRuleViolation::AddObjects
    UF_RULE_set_vio_override                    Routing::DesignRuleViolation::SetOverride
    UF_RULE_set_vio_short_desc                  Routing::DesignRuleViolation::SetShortDescription
    UF_RULE_set_vio_time_stamp                  Routing::DesignRuleViolation::SetTimeStamp
    UF_ROUTE_bend_report_get_segment_info       Routing::BendReportManager::GetSegmentInformation
    UF_ROUTE_bend_report_reverse_direction      Routing::BendReportManager::ReverseDirection
    UF_ROUTE_bend_report_ask_number_of_bends    Routing::BendReportManager::GetNumberOfBends
    UF_ROUTE_bend_report_generate_xyz_report    Routing::BendReportManager::GenerateXyzReport
    UF_ROUTE_bend_report_generate_ybc_report    Routing::BendReportManager::GenerateYbcReport
    UF_ROUTE_bend_report_generate_mil98_report  Routing::BendReportManager::GenerateMil98Report
    UF_ROUTE_ask_loaded_bend_tables             RoutingPath::GetBendRadiusTable
    UF_ROUTE_create_bend_by_table               Routing::AssignCornerBuilder::SetRadiusFromBendTable
    UF_ROUTE_DR_MODE_CONCURRENT                 Routing::DesignRuleViolationCollection::ModeConcurrent
    UF_ROUTE_DR_MODE_INTERACTIVE                Routing::DesignRuleViolationCollection::ModeInteractive
    UF_ROUTE_DR_REASON_...                      Routing::CustomManager::DesignRuleReason...
    UF_ROUTE_CB_REASON_...                      Routing::CustomManager::CallbackReason...
    UF_ROUTE_RUN_ask_run_id_and_type            Routing::Run::GetRunId and Routing::Run::GetRunType
    UF_ROUTE_RUN_ask_from_items                 Routing::Run::GetFromItems
    UF_ROUTE_RUN_ask_to_items                   Routing::Run::GetToItems
    UF_ROUTE_RUN_ask_member_items               Routing::Run::GetMembers
    UF_ROUTE_RUN_ask_runs_in_part               Routing::RouteManager::Runs
    UF_ROUTE_RUN_set_run_id                     Routing::Run::Edit
    UF_ROUTE_RUN_set_run_type                   Routing::Run::Edit
    UF_ROUTE_set_characteristics                Call the SetCharacteristic2 method on th eRouting object.
    UF_ROUTE_delete_characteristics             Call the DeleteCharacterstics method on the Routing object.
    UF_ROUTE_ask_characteristics                Call the GetCharacteristics method on the Routing object.
    UF_ROUTE_load_part_by_charx                 Routing::RouteManager::LoadPart
    UF_ROUTE_ask_charx_env                      Preferences::RoutingApplicationView::GetOptionalCharacteristics and GetRequiredCharacteristics.
    UF_ROUTE_set_charx_env                      Preferences::RoutingCharacteristics::UpdateStockCharacteristicValues
    UF_ROUTE_update_charx_env                   Preferences::RoutingCharacteristics::UpdateStockCharacteristicValues
    UF_ROUTE_match_charx_in_plib                Preferences::RoutingPartLibrary::MatchCriteria
    UF_ROUTE_free_match_results                 Language specific memory management.
    UF_ROUTE_free_charx_array                   Language specific memory management.
    UF_ROUTE_find_terminal_charx                Routing::TerminalPort::FindPortIntegerCharacteristic or FindPortRealCharacteristic or FindPortStringCharacteristic.
    UF_ROUTE_find_title_in_charx                Call the GetCharacteristics method on the Routing object.
    UF_ROUTE_ask_obj_corner_info                Routing::BendCornerCollection::GetBendAssociatedToSegment
    UF_ROUTE_ask_obj_bend_radius                Routing::BendCornerCollection::GetBendCornersFromObjects, then Routing::BendCorner::BendRadius
    UF_ROUTE_ask_bend_radius                    Routing::BendCorner::BendRadius
    UF_ROUTE_ask_bend_rcp                       Routing::BendCorner::Rcp or Routing::MiterCorner::Rcp
    UF_ROUTE_ask_bend_segment                   Routing::BendCorner::GetSegment or Routing::MiterCorner::GetSegments
    UF_ROUTE_create_bend_by_radius              Routing::BendCornerCollection::CreateCorner 
    UF_ROUTE_create_bend_by_ratio               Routing::BendCornerCollection::CreateCorner
    UF_ROUTE_create_miter_corner                Routing::MiterCornerCollection::AssignCorner 
    UF_ROUTE_remove_corner                      Delete the corner segment.
    UF_ROUTE_is_rcp_bend_seg_rcp                Routing::BendCornerCollection::GetBendAssociatedToSegment
    UF_ROUTE_is_rcp_miter_corner                Routing::BendCornerCollection::GetBendAssociatedToSegment
    UF_ROUTE_ask_rcp_corner                     Routing::BendCornerCollection::GetBendAssociatedToSegment
    UF_ROUTE_ask_segment_bend_crnr              Routing::BendCornerCollection::GetBendAssociatedToSegment
    UF_ROUTE_ask_anchor_position                Routing::Anchor::Position
    UF_ROUTE_ask_anchor_stock                   Routing::Anchor::GetStock
    UF_ROUTE_ask_anchor_stock_data              Routing::Anchor::GetStockData
    UF_ROUTE_create_anchor_from_pnt             Routing::AnchorCollection.CreateAnchor
    UF_ROUTE_create_anchor_from_pos             Routing::AnchorCollection.CreateAnchor
    UF_ROUTE_is_part_anchor                     Use the Anchor class type to determine if this is an Anchor.
    UF_ROUTE_ask_stock_anchor                   Routing::Stock::GetAnchor
    UF_ROUTE_ask_stock_data_anchors             Routing::StockData::GetAnchors
    UF_ROUTE_ask_part_num_rcps                  Routing::ControlPointCollection
    UF_ROUTE_ask_part_rcps                      Routing::ControlPointCollection
    UF_ROUTE_ask_rcp_on_port                    Routing::Port::GetControlPoint
    UF_ROUTE_ask_rcp_ports                      Routing::PortCollection:GetObjectPorts
    UF_ROUTE_ask_rcp_position                   Routing::ControlPoint::Position
    UF_ROUTE_ask_rcp_segments                   Routing::ControlPoint::GetRcpSegments
    UF_ROUTE_ask_rcp_segs                       Routing::ControlPoint::GetRcpSegments
    UF_ROUTE_create_rcp_arc_center              Routing::ControlPointCollection::CreateControlPoint
    UF_ROUTE_create_rcp_at_port                 Routing::ControlPointCollection::CreateControlPoint
    UF_ROUTE_create_rcp_by_wcs_off              Routing::ControlPointCollection::CreateControlPoint
    UF_ROUTE_create_rcp_by_work_pos             Routing::ControlPointCollection::CreateControlPoint
    UF_ROUTE_create_rcp_curve_parm              Routing::ControlPointCollection::CreateControlPoint
    UF_ROUTE_create_rcp_on_rcp                  Routing::ControlPointCollection::CreateControlPoint
    UF_ROUTE_create_rcp_point                   Routing::ControlPointCollection::CreateControlPoint
    UF_ROUTE_create_rcp_position                Routing::ControlPointCollection::CreateControlPoint
    UF_ROUTE_merge_rcps                         Routing::RouteManager::MergeDuplicateRcps
    UF_ROUTE_simplify_rcps                      Routing::SimplifyPathBuilder
    UF_ROUTE_add_segment_to_stock               Routing::Stock::AddSegments
    UF_ROUTE_ask_part_num_segs                  Routing::SegmentManager::Segments
    UF_ROUTE_ask_part_segs                      Routing::SegmentManager::Segments
    UF_ROUTE_ask_seg_curve                      Routing::ISegment::FollowCurve
    UF_ROUTE_ask_seg_rcps                       Routing::ISegment::GetEndRcps
    UF_ROUTE_ask_segment_bundle_stock           Routing::ISegment::GetSegmentStock
    UF_ROUTE_ask_segment_end_idx                Routing::ISegment::GetEndRcps
    UF_ROUTE_ask_segment_end_pnts               Routing::ISegment::GetEndPoints
    UF_ROUTE_ask_segment_int_part               Routing::ISegment::GetIsSegmentInterior
    UF_ROUTE_ask_segment_int_parts              Routing::ISegment::GetIsSegmentInterior
    UF_ROUTE_ask_segment_length                 Routing::ISegment::Length
    UF_ROUTE_ask_segment_stock                  Routing::ISegment::GetSegmentStock
    UF_ROUTE_ask_stock_segments                 Routing::Stock::GetSegments
    UF_ROUTE_ask_wire_segments                  Routing::Wire::GetSegments
    UF_ROUTE_create_seg_on_curve                Routing::SegmentManager::CreateSegment
    UF_ROUTE_create_seg_thru_rcps               Routing::SegmentManager::CreateSegment
    UF_ROUTE_is_segment                         Use the Segment class type to determine if this is a Segment.
    UF_ROUTE_is_terminal_segment                Routing::ISegment::GetIsTerminalSegment
    UF_ROUTE_remove_seg_from_stock              Routing::Stock::RemoveSegments
    UF_ROUTE_is_segment_inside_part             Routing::ISegment::GetIsSegmentInterior
    UF_ROUTE_ask_heal_pos                       Routing::HealPath
    UF_ROUTE_ask_part_search_path               LoadOptions::GetSearchDirectories
    UF_ROUTE_set_part_search_path               LoadOptions::SetSearchDirectories
    UF_ROUTE_find_part_in_path                  PartCollection::Open
    UF_ROUTE_align_stock                        Routing::Stock::AlignStock
    UF_ROUTE_ask_app_view_curves                Preferences::RoutingPath::GetAllowedCurves
    UF_ROUTE_ask_app_view_def_style             Preferences::RoutingStock::DefaultStockStyle
    UF_ROUTE_ask_app_view_desc                  Preferences::RoutingApplicationView::Description
    UF_ROUTE_ask_app_view_fab_charx             Preferences::RoutingApplicationView::GetFabricationCharacteristics
    UF_ROUTE_ask_app_view_filename              Preferences::RoutingApplicationView::Filename
    UF_ROUTE_ask_app_view_name                  Preferences::RoutingApplicationView::Name
    UF_ROUTE_ask_app_view_opt_charx             Preferences::RoutingApplicationView::GetOptionalCharacteristics
    UF_ROUTE_ask_app_view_plib_type             All part libraries are of type "part library view".
    UF_ROUTE_ask_app_view_req_charx             Preferences::RoutingApplicationView::GetRequiredCharacteristics
    UF_ROUTE_ask_built_in_path_objs             NXOpen::Routing::BuiltInPath::GetCurves
    UF_ROUTE_ask_built_in_paths                 Routing::BuiltInPathCollection
    UF_ROUTE_ask_cross_curves                   Routing::CrossSection::GetCrossCurves
    UF_ROUTE_ask_cross_offsets                  Routing::CrossSection::Offset
    UF_ROUTE_ask_cross_stock_data               Routing::CrossSection::GetStockData
    UF_ROUTE_ask_cross_style                    Routing::CrossSection::Style
    UF_ROUTE_ask_current_app_view               Preferences::RoutingApplicationView
    UF_ROUTE_ask_harness_comps                  Routing::AssemblyDefinition::GetSingleDeviceChildren
    UF_ROUTE_ask_harness_wires                  Electrical::HarnessDefinition::GetChildConnections
    UF_ROUTE_ask_length_tolerance               Routing::RouteManager::GetLengthTolerance
    UF_ROUTE_ask_multiport_terminals            Routing::MultiPort::GetTerminalPorts
    UF_ROUTE_ask_part_duplicate_rcps            Routing::RouteManager::MergeDuplicateRcps
    UF_ROUTE_ask_part_duplicate_segs            Routing::RouteManager::MergeDuplicateRcps
    UF_ROUTE_ask_part_part_type                 Routing::RouteManager::PartTypeFlag
    UF_ROUTE_ask_places_transform               Routing::PlacementSolutionsBuilder
    UF_ROUTE_ask_route_end                      Routing::Path::ControlPointEnd
    UF_ROUTE_ask_route_objs                     Routing::Path::GetSegmentList
    UF_ROUTE_ask_route_start                    Routing::Path::ControlPointStart
    UF_ROUTE_ask_segment_branch_angle           Formboard::OrientBranchBuilder::RotationAngle
    UF_ROUTE_ask_segment_end_props              Routing::ISegment::GetEndRcps
    UF_ROUTE_ask_segment_paths                  Routing::Path::GetSegmentList
    UF_ROUTE_ask_segment_routes                 Routing::Path::GetSegmentList
    UF_ROUTE_ask_segment_wires                  Routing::Path::GetSegmentList
    UF_ROUTE_ask_segments_is_path               Routing::Path::GetSegmentList
    UF_ROUTE_ask_segments_paths                 Routing::Path::GetSegmentList
    UF_ROUTE_ask_stock_body                     Routing::Stock::GetBodies
    UF_ROUTE_ask_stock_cross_sect               Routing::Stock::GetCrossSection
    UF_ROUTE_ask_stock_data_cross               Routing::StockData::GetCrossSection
    UF_ROUTE_ask_stock_data_stock               Routing::StockData::GetStocks
    UF_ROUTE_ask_stock_feature                  Routing::Stock::GetFeatures
    UF_ROUTE_ask_stock_harness                  Routing::Stock::GetHarnessDevice
    UF_ROUTE_ask_stock_part_occ                 Routing::Stock::GetComponent
    UF_ROUTE_ask_stock_ports                    Routing::Stock::GetPorts
    UF_ROUTE_ask_stock_profile_port             Routing::Stock::GetPorts
    UF_ROUTE_ask_stock_rotation                 Routing::Stock::GetRotationAngle
    UF_ROUTE_ask_stock_stock_data               Routing::Stock::GetStockData
    UF_ROUTE_ask_stock_style                    Routing::Stock::GetStockStyle
    UF_ROUTE_ask_stock_units                    Use the part units.
    UF_ROUTE_ask_stock_wires                    Routing::Stock::GetHarnessDevice
    UF_ROUTE_ask_user_preferences               Preferences::RoutingApplicationView::RoutingUserPreferences
    UF_ROUTE_ask_wire_harness                   Routing::Stock::GetHarnessDevice
    UF_ROUTE_ask_wire_stock                     Routing::Wire::GetStock
    UF_ROUTE_assign_stock                       Routing::PathStockBuilder
    UF_ROUTE_assign_stock_style                 Routing::StockBuilder::StockStyle
    UF_ROUTE_compute_stock_length               Routing::StockDevice::StockLength
    UF_ROUTE_convert_to_stock_as_components     Routing::StockCollection::ConvertToStockAsComponents
    UF_ROUTE_create_built_in_path               Routing::BuiltInPathCollection::CreateBuiltInPath
    UF_ROUTE_create_cross_section               Routing::CrossSectionCollection::CreateCrossSection
    UF_ROUTE_create_round_cross_section         Routing::CrossSectionCollection::CreateCrossSection
    UF_ROUTE_find_path                          Routing::SegmentManager::GetShortestPathBetweenControlPoints
    UF_ROUTE_free_array_of_tag_lists            Language specific memory management.
    UF_ROUTE_free_places                        Language specific memory management.
    UF_ROUTE_free_user_prefs_data               Language specific memory management.
    UF_ROUTE_get_next_connections               Routing::SegmentManager::GetShortestPathBetweenControlPoints
    UF_ROUTE_is_part_fabrication                Routing::RouteManager::PartTypeFlag
    UF_ROUTE_is_part_occ_route_part             Routing::RouteManager::PartTypeFlag
    UF_ROUTE_is_stock_interior                  Routing::ISegment::GetIsSegmentInterior
    UF_ROUTE_is_wire_on_segment                 Routing::Path::GetSegmentList
    UF_ROUTE_load_app_view                      Preferences::RoutingApplicationView::LoadAppView
    UF_ROUTE_load_app_view_list                 Preferences::RoutingApplicationView::LoadAppView
    UF_ROUTE_load_part_by_name                  Routing::RouteManager::LoadPart
    UF_ROUTE_load_stock_by_charx                Routing::RouteManager::LoadPart
    UF_ROUTE_remove_stock                       Routing::PathStockBuilder
    UF_ROUTE_set_built_in_path_objs             Routing::BuiltInPath::CreateSegments
    UF_ROUTE_set_current_app_view               Preferences::RoutingApplicationView::LoadAppView
    UF_ROUTE_set_part_in_stock                  Routing::PlacePartBuilder
    UF_ROUTE_set_stock_style                    Routing::Stock::SetStockStyle
    UF_ROUTE_set_user_preferences               Preferences::RoutingApplicationView::RoutingUserPreferences
    UF_ROUTE_simplify_segments                  Routing::SimplifyPathBuilder
    UF_ROUTE_solve_places                       Routing::PlacePartBuilder
    UF_ROUTE_stock_ask_name                     Routing::Stock::Name
    UF_ROUTE_transform_objects                  Routing::TransformPathBuilder
    UF_ROUTE_unload_app_view                    Application views cannot be unloaded.Use LoadAppView to load another application view.


There are no direct replacements for UF_ROUTE_check_min_bend_radius and UF_ROUTE_check_min_str_length.
You can register the example NX Open bend radius Design Rules found in UFD_Routing_BendRadiusDesignRules.cxx 
in the UGROUTE_MECH kit. Follow the directions in the example and in the Routing Application View (APV) file 
to register the examples. Or you can write your own version of these rules by following the examples in
UFD_Routing_BendRadiusDesignRules.cxx.

UF_ROUTE_fix_stale_stock has been deleted.  This functionality was been removed from the product
in NX5.  There is no replacement call for this function.

******************************************************************************/
#ifndef UF_ROUTE_H_INCLUDED
#define UF_ROUTE_H_INCLUDED

/**************
 ** Includes **
 **************/
/******************************************************************************

******************************************************************************/

#include <uf_defs.h>            /* For MAX_LINE_SIZE, TRUE/FALSE, etc.*/
#include <uf_attr.h>
#include <uf_eplib_types.h>     /* Part library definitions */
#include <uf_ui_types.h>
#include <uf_styler.h>
#include <uf_rlist.h>
#include <uf_route_ugopenint.h>
#include <uf_ugmgr_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/************
 ** Macros **
 ************/

/* Characteristic Macros */
#define UF_ROUTE_COMP_ID_CHARX_TITLE   UF_RLIST_COMP_ID_CHARX_TITLE
#define UF_ROUTE_PORT_ID_CHARX_TITLE   UF_RLIST_PORT_ID_CHARX_TITLE
#define UF_ROUTE_CUT_BACK_LENGTH_CHARX_TITLE      "CUT_BACK_LENGTH"
#define UF_ROUTE_EXTENSION_LENGTH_CHARX_TITLE     "EXTENSION_LENGTH"
#define UF_ROUTE_PROXY_PORT_CHARX      "PROXY_PORT"
#define UF_ROUTE_LENGTH_CHARX_TITLE    "LENGTH"
#define UF_ROUTE_OVERSTOCK_WRAPPED_LENGTH_CHARX_TITLE    "WRAPPED_LENGTH"

/***************
** Constants **
***************/
/***************************************************************************
  
  ***************************************************************************/

/**************************************************************************
  Error codes
***************************************************************************/

#define ERROR_ROUTE_base                        1525000
#define UF_ROUTE_ERROR_BASE                     ERROR_ROUTE_base
#define UF_ROUTE_err_unknown                    ERROR_ROUTE_base + 1
#define UF_ROUTE_err_cannot_write_to_occ        ERROR_ROUTE_base + 2
#define UF_ROUTE_err_wrong_entity_type          ERROR_ROUTE_base + 3
#define UF_ROUTE_err_invalid_entity_data        ERROR_ROUTE_base + 4
#define UF_ROUTE_err_syntax_error               ERROR_ROUTE_base + 5
#define UF_ROUTE_err_cfi_error                  ERROR_ROUTE_base + 6
#define UF_ROUTE_err_not_a_preference           ERROR_ROUTE_base + 7
#define UF_ROUTE_err_table_not_loaded           ERROR_ROUTE_base + 8
#define UF_ROUTE_err_out_of_range               ERROR_ROUTE_base + 9
#define UF_ROUTE_err_program_error              ERROR_ROUTE_base + 10
#define UF_ROUTE_err_subseg_bcorner_seg         ERROR_ROUTE_base + 11
#define UF_ROUTE_err_subseg_neg_arclen          ERROR_ROUTE_base + 12
#define UF_ROUTE_err_subseg_big_arclen          ERROR_ROUTE_base + 13
#define UF_ROUTE_err_subseg_neg_ratio           ERROR_ROUTE_base + 14
#define UF_ROUTE_err_subseg_neg_numseg          ERROR_ROUTE_base + 15
#define UF_ROUTE_err_subseg_neg_chordal         ERROR_ROUTE_base + 16
#define UF_ROUTE_err_subseg_start_pct           ERROR_ROUTE_base + 17
#define UF_ROUTE_err_subseg_end_pct             ERROR_ROUTE_base + 18
#define UF_ROUTE_err_subseg_bad_segment         ERROR_ROUTE_base + 19
#define UF_ROUTE_err_subseg_pct_order           ERROR_ROUTE_base + 20
#define UF_ROUTE_err_no_app_view                ERROR_ROUTE_base + 21
#define UF_ROUTE_err_subseg_wrong_method        ERROR_ROUTE_base + 22
#define UF_ROUTE_err_subseg_curve_dir           ERROR_ROUTE_base + 23
#define UF_ROUTE_err_subseg_screen_point        ERROR_ROUTE_base + 24
#define UF_ROUTE_err_no_cross_section           ERROR_ROUTE_base + 25
#define UF_ROUTE_err_null_pointer               ERROR_ROUTE_base + 26
#define UF_ROUTE_err_bad_rcp                    ERROR_ROUTE_base + 27
#define UF_ROUTE_err_bend_fillet_error          ERROR_ROUTE_base + 28
#define UF_ROUTE_err_invalid_corner_type        ERROR_ROUTE_base + 29
#define UF_ROUTE_err_bad_crn_object             ERROR_ROUTE_base + 30
#define UF_ROUTE_err_invalid_rcp_crnr           ERROR_ROUTE_base + 31
#define UF_ROUTE_err_bend_on_follow             ERROR_ROUTE_base + 32
#define UF_ROUTE_err_bend_at_bend               ERROR_ROUTE_base + 33
#define UF_ROUTE_err_neg_bend_radius            ERROR_ROUTE_base + 34
#define UF_ROUTE_err_bad_bend_radius            ERROR_ROUTE_base + 35
#define UF_ROUTE_err_charx_type                 ERROR_ROUTE_base + 36
#define UF_ROUTE_err_charx_object               ERROR_ROUTE_base + 37
#define UF_ROUTE_err_charx_count                ERROR_ROUTE_base + 38
#define UF_ROUTE_err_charx_title                ERROR_ROUTE_base + 39
#define UF_ROUTE_err_charx_oper                 ERROR_ROUTE_base + 40
#define UF_ROUTE_err_load_app_view              ERROR_ROUTE_base + 41
#define UF_ROUTE_err_load_part_lib_view         ERROR_ROUTE_base + 42
#define UF_ROUTE_err_load_part_table            ERROR_ROUTE_base + 43
#define UF_ROUTE_err_no_stock_data              ERROR_ROUTE_base + 44
#define UF_ROUTE_err_no_part_name_attr          ERROR_ROUTE_base + 45
#define UF_ROUTE_err_bad_bend_ratio             ERROR_ROUTE_base + 46
#define UF_ROUTE_err_no_stock_for_ratio         ERROR_ROUTE_base + 47
#define UF_ROUTE_err_seg_stock_mismatch         ERROR_ROUTE_base + 48
#define UF_ROUTE_err_stock_has_no_diam          ERROR_ROUTE_base + 49
#define UF_ROUTE_err_crnr_segs_tangent          ERROR_ROUTE_base + 50
#define UF_ROUTE_err_cant_determine_rad         ERROR_ROUTE_base + 51
#define UF_ROUTE_err_mult_stk_for_ratio         ERROR_ROUTE_base + 52
#define UF_ROUTE_err_heal_invalid_ext           ERROR_ROUTE_base + 53
#define UF_ROUTE_err_heal_invalid_pos           ERROR_ROUTE_base + 54
#define UF_ROUTE_err_heal_num_pos               ERROR_ROUTE_base + 55
#define UF_ROUTE_err_heal_parallel_vecs         ERROR_ROUTE_base + 56
#define UF_ROUTE_err_no_part_families           ERROR_ROUTE_base + 57
#define UF_ROUTE_err_dr_file_not_found          ERROR_ROUTE_base + 58
#define UF_ROUTE_err_invalid_dr_mode            ERROR_ROUTE_base + 59
#define UF_ROUTE_err_up_invalid_type            ERROR_ROUTE_base + 60
#define UF_ROUTE_err_cross_secn_style           ERROR_ROUTE_base + 61
#define UF_ROUTE_err_no_charx_for_object        ERROR_ROUTE_base + 62
#define UF_ROUTE_err_no_common_req_charx        ERROR_ROUTE_base + 63
#define UF_ROUTE_err_neg_engagement             ERROR_ROUTE_base + 64
#define UF_ROUTE_err_no_stkdata_found           ERROR_ROUTE_base + 65
#define UF_ROUTE_err_stock_convert              ERROR_ROUTE_base + 66
#define UF_ROUTE_err_stock_import               ERROR_ROUTE_base + 67
#define UF_ROUTE_err_no_rout_plist_exist        ERROR_ROUTE_base + 68
#define UF_ROUTE_err_marked_as_no_report        ERROR_ROUTE_base + 69
#define UF_ROUTE_err_root_and_work_diff         ERROR_ROUTE_base + 70
#define UF_ROUTE_err_no_part                    ERROR_ROUTE_base + 71
#define UF_ROUTE_err_same_values                ERROR_ROUTE_base + 72
#define UF_ROUTE_err_no_class                   ERROR_ROUTE_base + 73
#define UF_ROUTE_err_invalid_route_start        ERROR_ROUTE_base + 74
#define UF_ROUTE_err_invalid_route_end          ERROR_ROUTE_base + 75
#define UF_ROUTE_err_invalid_placer_type        ERROR_ROUTE_base + 76
#define UF_ROUTE_err_invalid_cope_crn           ERROR_ROUTE_base + 77
#define UF_ROUTE_err_zero_length_segment        ERROR_ROUTE_base + 78
#define UF_ROUTE_err_member_not_found           ERROR_ROUTE_base + 79
#define UF_ROUTE_err_stock_prt_not_found        ERROR_ROUTE_base + 80
#define UF_ROUTE_err_no_gasket_udo_created      ERROR_ROUTE_base + 81
#define UF_ROUTE_err_no_bolt_udo_created        ERROR_ROUTE_base + 82
#define UF_ROUTE_err_no_nut_udo_created         ERROR_ROUTE_base + 83
#define UF_ROUTE_err_no_weld_ring_pref          ERROR_ROUTE_base + 84
#define UF_ROUTE_err_no_gasket_charx            ERROR_ROUTE_base + 85
#define UF_ROUTE_err_no_user_pref               ERROR_ROUTE_base + 86
#define UF_ROUTE_err_no_weld_ring_udo           ERROR_ROUTE_base + 87
#define UF_ROUTE_err_no_weld_ring_assigned      ERROR_ROUTE_base + 88
#define UF_ROUTE_err_no_weld_ring_charx         ERROR_ROUTE_base + 89
#define UF_ROUTE_err_no_bolt_charx              ERROR_ROUTE_base + 90
#define UF_ROUTE_err_no_fab_created             ERROR_ROUTE_base + 91
#define UF_ROUTE_err_rcurve_start_loc           ERROR_ROUTE_base + 92
#define UF_ROUTE_err_rcurve_end_loc             ERROR_ROUTE_base + 93
#define UF_ROUTE_err_rcurve_start_ext           ERROR_ROUTE_base + 94
#define UF_ROUTE_err_rcurve_end_ext             ERROR_ROUTE_base + 95
#define UF_ROUTE_err_rcurve_start_slope         ERROR_ROUTE_base + 96
#define UF_ROUTE_err_rcurve_end_slope           ERROR_ROUTE_base + 97
#define UF_ROUTE_err_rcurve_start_assoc         ERROR_ROUTE_base + 98
#define UF_ROUTE_err_rcurve_end_assoc           ERROR_ROUTE_base + 99
#define UF_ROUTE_err_neg_extension              ERROR_ROUTE_base + 100
#define UF_ROUTE_err_no_explicit_path           ERROR_ROUTE_base + 101
#define UF_ROUTE_err_neg_cut_back_length        ERROR_ROUTE_base + 102
#define UF_ROUTE_err_zero_cut_back_length       ERROR_ROUTE_base + 103
#define UF_ROUTE_err_excess_cut_back_length     ERROR_ROUTE_base + 104
#define UF_ROUTE_err_no_mass_assertion          ERROR_ROUTE_base + 105
#define UF_ROUTE_err_invalid_weight_units       ERROR_ROUTE_base + 106
#define UF_ROUTE_err_bad_rte_charx_typ          ERROR_ROUTE_base + 107
#define UF_ROUTE_err_bad_rte_syn_charx_typ      ERROR_ROUTE_base + 108
#define UF_ROUTE_err_bad_gen_charx_typ          ERROR_ROUTE_base + 109
#define UF_ROUTE_err_bad_gen_syn_charx_typ      ERROR_ROUTE_base + 110
#define UF_ROUTE_err_unify_nochange             ERROR_ROUTE_base + 111
#define UF_ROUTE_err_no_path_found              ERROR_ROUTE_base + 112
#define UF_ROUTE_err_intersection_at_bend       ERROR_ROUTE_base + 113
#define UF_ROUTE_err_no_charx_on_port           ERROR_ROUTE_base + 114
#define UF_ROUTE_err_no_flange_conn_data        ERROR_ROUTE_base + 115
#define UF_ROUTE_err_invalid_port_mate          ERROR_ROUTE_base + 116
#define UF_ROUTE_err_brt_invalid_file           ERROR_ROUTE_base + 117
#define UF_ROUTE_err_brt_invalid_table          ERROR_ROUTE_base + 118
#define UF_ROUTE_err_brt_no_table_entry         ERROR_ROUTE_base + 119
#define UF_ROUTE_err_brt_no_diameter_entry      ERROR_ROUTE_base + 120
#define UF_ROUTE_err_brt_warning_in_table       ERROR_ROUTE_base + 121
#define UF_ROUTE_err_prev19_stock               ERROR_ROUTE_base + 122
#define UF_ROUTE_err_bad_down_direction         ERROR_ROUTE_base + 123
#define UF_ROUTE_err_unknown_segset_method      ERROR_ROUTE_base + 124
#define UF_ROUTE_err_no_segments_in_path        ERROR_ROUTE_base + 125
#define UF_ROUTE_err_zero_length_path           ERROR_ROUTE_base + 126
#define UF_ROUTE_err_no_continuous_path         ERROR_ROUTE_base + 127
#define UF_ROUTE_err_start_beyond_end           ERROR_ROUTE_base + 128
#define UF_ROUTE_err_length_beyond_end          ERROR_ROUTE_base + 129
#define UF_ROUTE_err_length_beyond_path_end     ERROR_ROUTE_base + 130
#define UF_ROUTE_err_negative_gap_length        ERROR_ROUTE_base + 131
#define UF_ROUTE_err_unknown_overstock_type     ERROR_ROUTE_base + 132
#define UF_ROUTE_err_unable_deref_charx         ERROR_ROUTE_base + 133
#define UF_ROUTE_err_too_many_paths             ERROR_ROUTE_base + 134
#define UF_ROUTE_err_negative_start_offset      ERROR_ROUTE_base + 135
#define UF_ROUTE_err_negative_end_offset        ERROR_ROUTE_base + 136
#define UF_ROUTE_err_invalid_num_pieces         ERROR_ROUTE_base + 137
#define UF_ROUTE_err_invalid_piece_len          ERROR_ROUTE_base + 138
#define UF_ROUTE_err_create_fmbd_failure        ERROR_ROUTE_base + 139
#define UF_ROUTE_err_fmbd_data_failure          ERROR_ROUTE_base + 140
#define UF_ROUTE_err_data_not_loaded            ERROR_ROUTE_base + 141
#define UF_ROUTE_err_cannot_create_rout_plist   ERROR_ROUTE_base + 142
#define UF_ROUTE_err_charx_not_found            ERROR_ROUTE_base + 143
#define UF_ROUTE_err_all_charx_not_deleted      ERROR_ROUTE_base + 144
#define UF_ROUTE_err_entities_not_supported     ERROR_ROUTE_base + 145
#define UF_ROUTE_err_rcp_is_not_occ             ERROR_ROUTE_base + 146
#define UF_ROUTE_err_bad_parameter_1            ERROR_ROUTE_base + 147
#define UF_ROUTE_err_bad_parameter_2            ERROR_ROUTE_base + 148
#define UF_ROUTE_err_bad_parameter_3            ERROR_ROUTE_base + 149
#define UF_ROUTE_err_bad_parameter_4            ERROR_ROUTE_base + 150
#define UF_ROUTE_err_bad_parameter_5            ERROR_ROUTE_base + 151
#define UF_ROUTE_err_bad_parameter_6            ERROR_ROUTE_base + 152
#define UF_ROUTE_err_bad_obj_sdata              ERROR_ROUTE_base + 153
#define UF_ROUTE_err_cannot_copy                ERROR_ROUTE_base + 154
#define UF_ROUTE_err_bad_discipline             ERROR_ROUTE_base + 155
#define UF_ROUTE_err_bad_specification          ERROR_ROUTE_base + 156
#define UF_ROUTE_err_node_not_found             ERROR_ROUTE_base + 157
#define UF_ROUTE_err_terminal_already_exists    ERROR_ROUTE_base + 158
#define UF_ROUTE_err_terminal_not_found         ERROR_ROUTE_base + 159
#define UF_ROUTE_err_plmxml_no_electrical_data  ERROR_ROUTE_base + 160
#define UF_ROUTE_err_plmxml_invalid_file        ERROR_ROUTE_base + 161
#define UF_ROUTE_err_connection_in_multiple_harnesses  ERROR_ROUTE_base + 162
#define UF_ROUTE_err_unimplemented_method       ERROR_ROUTE_base + 163
#define UF_ROUTE_err_kinked_flex                ERROR_ROUTE_base + 164
#define UF_ROUTE_err_fold_creation_fail         ERROR_ROUTE_base + 165

#define UF_ROUTE_err_segment_endpoints_not_at_rcp ERROR_ROUTE_base + 198
#define UF_ROUTE_err_no_elbow_ang                 ERROR_ROUTE_base + 199
#define UF_ROUTE_err_copying_to_non_dcm3_part     ERROR_ROUTE_base + 200
#define UF_ROUTE_err_copying_to_dcm3_part         ERROR_ROUTE_base + 201
#define UF_ROUTE_err_cant_find_pl_format_file     ERROR_ROUTE_base + 202
#define UF_ROUTE_err_cant_import_pl_format_file   ERROR_ROUTE_base + 203
#define UF_ROUTE_err_no_electrical_data_in_file   ERROR_ROUTE_base + 204

#define UF_ROUTE_err_not_enough_points_for_qp     ERROR_ROUTE_base + 205
#define UF_ROUTE_err_no_free_space_around_point   ERROR_ROUTE_base + 206
#define UF_ROUTE_err_no_path_between_points       ERROR_ROUTE_base + 207

#define UF_ROUTE_err_no_builder                   ERROR_ROUTE_base + 208
#define UF_ROUTE_err_unimplemented_interface      ERROR_ROUTE_base + 209
#define UF_ROUTE_err_dcm3_spline_failure          ERROR_ROUTE_base + 210

#define UF_ROUTE_err_sheet_bodies_in_different_plane          ERROR_ROUTE_base + 211
#define UF_ROUTE_err_body_outside_other_body                  ERROR_ROUTE_base + 212
#define UF_ROUTE_err_transition_sweep_failure                 ERROR_ROUTE_base + 213
#define UF_ROUTE_err_no_cut_elbow_name_generated              ERROR_ROUTE_base + 214

#define UF_ROUTE_UCorner_err_segment_not_alive                               ERROR_ROUTE_base + 215
#define UF_ROUTE_UCorner_err_segment_not_arc_and_line                        ERROR_ROUTE_base + 216
#define UF_ROUTE_UCorner_err_prev_or_next_of_UBend_segment_not_line_segment  ERROR_ROUTE_base + 217
#define UF_ROUTE_UCorner_err_touch_constraints_between_two_parallel_segments ERROR_ROUTE_base + 218
#define UF_ROUTE_UCorner_err_segment_and_prev_not_perpendicular              ERROR_ROUTE_base + 219
#define UF_ROUTE_UCorner_err_segment_and_next_not_perpendicular              ERROR_ROUTE_base + 220
#define UF_ROUTE_UCorner_err_pre_and_next_segments_not_parallel              ERROR_ROUTE_base + 221
#define UF_ROUTE_UCorner_err_UBend_segment_prev_next_not_in_plane            ERROR_ROUTE_base + 222
#define UF_ROUTE_err_root_node_not_found                                     ERROR_ROUTE_base + 223

#define UF_ROUTE_err_max                                      ERROR_ROUTE_base + 224

/* Error string definition section */
#define UF_ROUTE_str_invalid_route_start            \
        "%s: Invalid object specified for route start %d"
#define UF_ROUTE_str_invalid_route_end              \
        "%s: Invalid object specified for route end %d"

#define UF_ROUTE_AV_CORNERS_NONE  0
#define UF_ROUTE_AV_CORNERS_BEND  ((uint8_t)(1<<0))
#define UF_ROUTE_AV_CORNERS_COPE  ((uint8_t)(1<<1))
#define UF_ROUTE_AV_CORNERS_MITER ((uint8_t)(1<<2))
#define UF_ROUTE_AV_CORNERS_SBEND ((uint8_t)(1<<3))
#define UF_ROUTE_AV_CORNERS_UBEND ((uint8_t)(1<<4))
#define UF_ROUTE_AV_CORNERS_MITEREDBEND ((uint8_t)(1<<5))

#define UF_ROUTE_AV_CURVES_NONE    0
#define UF_ROUTE_AV_CURVES_LINES   ((uint8_t)(1<<0))
#define UF_ROUTE_AV_CURVES_ARCS    ((uint8_t)(1<<1))
#define UF_ROUTE_AV_CURVES_SPLINES ((uint8_t)(1<<2))

#define UF_ROUTE_AV_UNITS_IN 0
#define UF_ROUTE_AV_UNITS_MM 1

#define UF_ROUTE_HEAL_METHOD_DIRECT    0
#define UF_ROUTE_HEAL_METHOD_INTERSECT 1
#define UF_ROUTE_HEAL_METHOD_XYZ       2
#define UF_ROUTE_HEAL_METHOD_XZY       3
#define UF_ROUTE_HEAL_METHOD_YXZ       4
#define UF_ROUTE_HEAL_METHOD_YZX       5
#define UF_ROUTE_HEAL_METHOD_ZXY       6
#define UF_ROUTE_HEAL_METHOD_ZYX       7

#define UF_ROUTE_LIBRARY_TYPE_FILE_SELECT 0
#define UF_ROUTE_LIBRARY_TYPE_VIEW        1
#define UF_ROUTE_LIBRARY_TYPE_EXTERNAL    2

#define UF_ROUTE_SI_TYPE_PROGRAM_WAIT   0
#define UF_ROUTE_SI_TYPE_PROGRAM_NOWAIT 1
#define UF_ROUTE_SI_TYPE_UFUNC          2
#define UF_ROUTE_SI_TYPE_GRIP           3
#define UF_ROUTE_SI_TYPE_INTERNAL       4

#define UF_ROUTE_CORNER_NONE        -1
#define UF_ROUTE_CORNER_BEND        0
#define UF_ROUTE_CORNER_MITER       1
#define UF_ROUTE_CORNER_COPE        2
#define UF_ROUTE_CORNER_BEND_TABLE  4

#define UF_ROUTE_STYLE_NONE     0
#define UF_ROUTE_STYLE_SIMPLE   1
#define UF_ROUTE_STYLE_DETAIL   2


#define UF_ROUTE_DR_DELETE_OPTION_DO_DELETE     0
#define UF_ROUTE_DR_DELETE_OPTION_DONT_DELETE   1

#define UF_ROUTE_USER_PREF_TYPE_ANY       UF_STYLER_NO_VALUE
#define UF_ROUTE_USER_PREF_TYPE_STR       UF_STYLER_STRING_VALUE
#define UF_ROUTE_USER_PREF_TYPE_STR_ARRAY UF_STYLER_STRING_PTR_VALUE
#define UF_ROUTE_USER_PREF_TYPE_INT       UF_STYLER_INTEGER_VALUE
#define UF_ROUTE_USER_PREF_TYPE_INT_ARRAY UF_STYLER_INTEGER_PTR_VALUE
#define UF_ROUTE_USER_PREF_TYPE_DBL       UF_STYLER_REAL_VALUE
#define UF_ROUTE_USER_PREF_TYPE_DBL_ARRAY UF_STYLER_REAL_PTR_VALUE

#define UF_ROUTE_PART_FILE_NAME_STR                     "PART_NAME"
#define UF_ROUTE_MEMBER_NAME_STR                        "MEMBER_NAME"
#define UF_ROUTE_PART_NUMBER_STR                        "PART_NUMBER"
#define UF_ROUTE_SYMBOL_NAME_STR                        "SYMBOL_PART_NAME"
#define UF_ROUTE_DIAMETER_STR                           "DIAMETER"
#define UF_ROUTE_WEIGHT_VALUE_STR                       "WEIGHT"
#define UF_ROUTE_WEIGHT_UNITS_STR                       "WEIGHT_UNITS"
#define UF_ROUTE_ANGLE_STR                              "ELBOW_ANG"
#define UF_ROUTE_DESCRIPTION_STR                        "DESCRIPTION"
#define UF_ROUTE_MATERIAL_STR                           "MATERIAL"
#define UF_ROUTE_SCHEDULE_STR                           "SCHEDULE"
#define UF_ROUTE_RATING_STR                             "RATING"
#define UF_ROUTE_CLASS_STR                              "CLASS"
#define UF_ROUTE_NPS_STR                                "NPS"
#define UF_ROUTE_NPS_OUT_STR                            "NPS_OUT"
#define UF_ROUTE_NPS_BRANCH_STR                         "NPS_BRANCH"
#define UF_ROUTE_INSLEN_STR                             "INSLEN"
#define UG_ROUTE_LENGTH_STR                             "LENGTH"
#define UG_ROUTE_WIDTH_STR                              "WIDTH"
#define UG_ROUTE_START_OFFSET_STR                       "START_OFFSET"
#define UG_ROUTE_END_OFFSET_STR                         "END_OFFSET"
#define UG_ROUTE_SEGMENT_XFORM_REF_INFO                 "ROUTE_XFORM_REF_INFO"
#define UG_ROUTE_INSIDE_PERPENDICULAR_CURVE             "ROUTE_INSIDE_PERPENDICULAR_CURVE"

/*
    
*/
#define UF_ROUTE_LENGTH_STR                             "LENGTH"
#define UF_ROUTE_WIDTH_STR                              "WIDTH"
#define UF_ROUTE_THICKNESS_STR                          "THICKNESS"
#define UF_ROUTE_DEFAULT_PLATFORM_GRATE_SYMBOL_NAME_STR "DEFAULT_PLATFORM_GRATE_SYMBOL"

/*
    UF_ROUTE_BLOCK_UNIFY_STR and UF_ROUTE_DIRECT_MOUNT_TYPE_STR are defined to
    have the titles of attributes which can be applied on routing parts through
    .ptb files. In code, there will be some decisions taken based on the value
    or existence of these attributes for example:

        A unify path operation will be blocked when it comes across any
        part that has an attribute of "NX_BLOCK_UNIFY" or "DIRECT_MOUNT_TYPE"

    If a part being placed has a characteristic with the title "NX_BLOCK_UNIFY",
    then its value is checked before a unify path operation. If the characteristic
    is enabled, then the unify path operation is not done. Only the value "TRUE"
    (case sensitive) can be used to enable the characteristic.

    If a part being placed has a characteristic with the title "DIRECT_MOUNT_TYPE",
    then NX assumes that the given part is of the direct mount type and will
    make decisions based on that, for example:

    If a direct mount part is placed on another direct mount part with a flange
    in between, then that flange will be removed and the part will be mounted
    directly on the first part. When such a pair of direct mount parts are found,
    then a unify path operation is also blocked.
*/
#define UF_ROUTE_BLOCK_UNIFY_STR                         "NX_BLOCK_UNIFY"
#define UF_ROUTE_DIRECT_MOUNT_TYPE_STR                   "DIRECT_MOUNT_TYPE"

/*
    If a part is placed using the "Instance Name Lookup" functionality, then a
    characteristic title of "INSTANCE_NAME" is added. Based on the presence of
    this characteristic, a unify path operation will be blocked.
*/
#define UF_ROUTE_INSTANCE_NAME_STR                      "INSTANCE_NAME"

#define UF_ROUTE_PART_TYPE_PART             0
#define UF_ROUTE_PART_TYPE_STOCK            1
#define UF_ROUTE_PART_TYPE_FABRICATION      2
#define UF_ROUTE_PART_TYPE_STOCK_COMPONENT  3
#define UF_ROUTE_PART_TYPE_WIRE_COMPONENT   4
#define UF_ROUTE_PART_TYPE_OVERSTOCK        5
#define UF_ROUTE_PART_TYPE_LOGICAL          6
#define UF_ROUTE_PART_TYPE_TEMPLATE_ASSY    7
#define UF_ROUTE_PART_TYPE_CONNECTOR        8
#define UF_ROUTE_PART_TYPE_SPLICE           9
#define UF_ROUTE_PART_TYPE_DEVICE           10
#define UF_ROUTE_PART_TYPE_FILLER           11
#define UF_ROUTE_PART_TYPE_UNKNOWN        (-1)

/* Create Terminals Preferences */
#define UF_ROUTE_CREATE_ALL_TERMINALS     0
#define UF_ROUTE_CREATE_LISTED_TERMINALS  1
#define UF_ROUTE_CREATE_ROUTED_TERMINALS  2

#define UF_ROUTE_DEFAULT_LEVEL "0"

/*
    Minimum value for Bend Ratio for Assign Bend Corner
    
*/
#define UF_ROUTE_MIN_BEND_RATIO 0.5

/* Used by the NAVIGATOR_OBJECT_SELECTED and SEGMENT_SELECTED plugins to indicate if the
   objects are selected or deselected. See the Application View (APV) file for more information.
*/
enum UF_ROUTE_selection_type_e
{
    UF_ROUTE_selection_type_deselected = 0,
    UF_ROUTE_selection_type_selected
};
typedef enum UF_ROUTE_selection_type_e UF_ROUTE_selection_type_t, *UF_ROUTE_selection_type_p_t;

/**************************
 ** Structures and Types **
 **************************/

/**/
#ifndef UF_EPLIB_part_lib_part_t_defined
#define UF_EPLIB_part_lib_part_t_defined
typedef struct UF_EPLIB_part_lib_part_s UF_ROUTE_part_lib_part_t,
    *UF_ROUTE_part_lib_part_p_t;
#endif

/**/
#ifndef UF_ROUTE_app_view_desc_t_defined
#define UF_ROUTE_app_view_desc_t_defined
struct UF_ROUTE_app_view_desc_s
{
    char *name;
    char *filename;
};
typedef struct UF_ROUTE_app_view_desc_s UF_ROUTE_app_view_desc_t,
               *UF_ROUTE_app_view_desc_p_t;
#endif

/* */
#ifndef UF_ROUTE_char_desc_s_defined
#define UF_ROUTE_char_desc_s_defined
/* Characteristic description */
struct UF_ROUTE_char_desc_s
{
    char *name;
    int   type;
};
typedef struct UF_ROUTE_char_desc_s UF_ROUTE_char_desc_t,
               *UF_ROUTE_char_desc_p_t;
#endif

typedef struct ROUTE_solver_pref_s UF_ROUTE_solver_pref_t,
                                   *UF_ROUTE_solver_pref_p_t;

/*
The following structure is used by the UF_ROUTE routines which
deal with Routing User Preferences.  You must allocate a
UF_ROUTE_user_preference_t structure for each preference you
wish to inquire upon or set.  Routing User Preferences may have one
of the following types:
UF_ROUTE_USER_PREF_TYPE_STR                        Single character string
UF_ROUTE_USER_PREF_TYPE_STR_ARRAY                  Array of character strings
UF_ROUTE_USER_PREF_TYPE_INT                        Single integer value
UF_ROUTE_USER_PREF_TYPE_INT_ARRAY                  Array of integer values
UF_ROUTE_USER_PREF_TYPE_DBL                        Single real value
UF_ROUTE_USER_PREF_TYPE_DBL_ARRAY                  Array of real values

For inquiry, you may also specify a type of UF_ROUTE_USER_PREF_TYPE_ANY
which matches a preference of any type.

The key field within the structure is a character string of the name of
the User Preference. The count field is used for the ARRAY types to
specify how many array members there are.

The value for a Routing User Preference is specified in the
appropriate member of the "value" union.

Note that the pointers in the value union when returned by the inquiry
functions are allocated by Routing and must be freed using the
UF_free functions.
*/
/* */
#ifndef UF_ROUTE_user_preference_s_defined
#define UF_ROUTE_user_preference_s_defined
union value_u
{
char   *string;
char  **strings;
int     integer;
int    *integers;
double  real;
double *reals;
};
typedef union value_u value_t;

struct UF_ROUTE_user_preference_s
{
    int   type;
    const char *key;
    int   count;
    value_t  value;
};
typedef struct UF_ROUTE_user_preference_s UF_ROUTE_user_preference_t,
               *UF_ROUTE_user_preference_p_t;

typedef struct ROUTE_prefs_s UF_ROUTE_prefs_t, *UF_ROUTE_prefs_p_t;
#endif

typedef void *(*UF_RULE_check_function_f_t)( tag_t   rule,/* <I> Rule to check */
                                             void   *data /* <I> Client data   */);

struct UF_ROUTE_design_rule_data_s
{
    int    mode;
    int    reason;
    int    num_objects;
    tag_t *objects;/* <len:num_objects>*/
};
typedef struct UF_ROUTE_design_rule_data_s UF_ROUTE_design_rule_data_t,
               *UF_ROUTE_design_rule_data_p_t;

struct UF_ROUTE_cb_data_s
{
    int     reason;
    int     num_objects;
    tag_t   *objects;
};
typedef struct UF_ROUTE_cb_data_s UF_ROUTE_cb_data_t, *UF_ROUTE_cb_data_p_t;

/* Cope Corner Data Structure */
struct UF_ROUTE_cope_data_s {
    tag_t     rcp_tag;          /* Corner for cope */
    int       num_stock;        /* Num of stock to cope */
    tag_t *   stock_tags;       /* <len:num_stock>
                                    Array of stock to cope */
};
typedef struct UF_ROUTE_cope_data_s UF_ROUTE_cope_data_t,
               *UF_ROUTE_cope_data_p_t;

/* */
#ifndef UF_ROUTE_place_solution_p_t_defined
#define UF_ROUTE_place_solution_p_t_defined
typedef struct ROUTE_place_solution_s *UF_ROUTE_place_solution_p_t;
#endif

/* */
#ifndef UF_ROUTE_application_view_t_defined
#define UF_ROUTE_application_view_t_defined
typedef struct ROUTE_application_view_s UF_ROUTE_application_view_t,
*UF_ROUTE_application_view_p_t;
#endif

typedef struct ROUTE_plugin_s UF_ROUTE_plugin_t , *UF_ROUTE_plugin_p_t;


/*
    The UF_ROUTE_bundle_data_s structure is the structure that is used
    to pass information to and receive information from a user written
    bundle diameter calculation routine. In Wiring, you may define
    a "Plug-in" for the routine that calculates the set of curves that
    should be used to model the cross section of the wire bundle based
    on the number of wires in the bundle (and their diameters). This
    is the structure that is supplied to your bundle diameter routine.


*/
struct UF_ROUTE_bundle_data_s
{
    int     num_wires;
    tag_t   *wires; /* <len:num_wires> */
    int     num_stock_data;
    tag_t  *stock_data; /* <len:num_stock_data> */
    int     num_cross_sections;
    tag_t  *cross_sections;/* <len:num_cross_sections> */
    int     num_anchors;
    tag_t  *anchors;/* <len:num_anchors> */
};
typedef struct UF_ROUTE_bundle_data_s
               UF_ROUTE_bundle_data_t, *UF_ROUTE_bundle_data_p_t;

/* The UF_ROUTE_cda_data_s is the structure that holds the data required to
   run the cable drawing automation program as a user-function utility from
   the wiring interface. This structure indicates the number of records
   selected and the selected connection list tags in the Rlist navigator
*/
struct UF_ROUTE_cda_data_s
{
    int num_recs;
    tag_t *recs; /* <len:num_recs> */
};
typedef struct UF_ROUTE_cda_data_s
               UF_ROUTE_cda_data_t, *UF_ROUTE_cda_data_p_t;

/* The UF_ROUTE_iman_bom_data_s is the structure used to implement the
   Routing Team Center Engineering BOM post piping parts list callback.
   It is currently empty but may be implemented in the future. */
struct UF_ROUTE_iman_bom_data_s
{
    logical place_holder;
};
typedef struct UF_ROUTE_iman_bom_data_s
               UF_ROUTE_iman_bom_data_t, *UF_ROUTE_iman_bom_data_p_t;


/*
   Bit mask of options used in the UF_ROUTE_pcf_gen_data_s structure's options.
*/
enum UF_ROUTE_pcf_options_e
{
    UF_ROUTE_PCF_ASK_TO_OVERWRITE_FILE = (1 << 1),
    UF_ROUTE_PCF_NEVER_OVERWRITE_FILE  = (1 << 2),
    UF_ROUTE_PCF_ALWAYS_OVERWRITE_FILE = (1 << 3)
};

typedef enum UF_ROUTE_pcf_options_e UF_ROUTE_pcf_options_t,
             *UF_ROUTE_pcf_options_p_t;


/* The UF_ROUTE_pcf_gen_data_s is the structure sent to the Piping Component File (PCF) generation
   utility.  The Piping Component File is then used by Alias' Isogen program to create an isometric
   drawing of the given components.

   If the filename is null, it is up to the PCF generation plugin to come up with a file name.

   If the components array is empty, it is up to the PCF generation plugin to either write out
   all components under the work part or prompt the user for the components to write.
*/
struct UF_ROUTE_pcf_gen_data_s
{
    const char* filename;    /* The name of the PCF file to create. May be null. */
    int         nComponents; /* The number of components in the components array. May be zero. */
    tag_t*      components;  /* The components to write to the PCF file. May be null. */
    int         options;     /* The options bit flag. See UF_ROUTE_pcf_options_e above. */
};
typedef struct UF_ROUTE_pcf_gen_data_s
               UF_ROUTE_pcf_gen_data_t, *UF_ROUTE_pcf_gen_data_p_t;

/* The following structure is used for the TEMP_STOCK_COMPONENT_NAME
    and STOCK_COMPONENT_NAME plugins determining stock component names.

    See UF_UGMGR_encode_part_filename for details on Team Center Engineering
    specific arguments ( item_revision, item_type and item_name ).
 */
struct UF_ROUTE_component_name_plugin_s
{
    tag_t   stock;
    /* Input:   Tag of the stock object */

    logical rename_part;
    /* Output:  TRUE if part needs to be renamed,
                FALSE part should remain as it is. */

    char    path_name[ MAX_FSPEC_BUFSIZE ]; /* <len:MAX_FSPEC_BUFSIZE>
       Output:  Path of file ("" == current directory) not used in Team Center Engineering,
                this is the path to the directory where stock components are to be
                be stored.  This may be a relative path (to the current directory),
                or an absolute path. */

    char    folder_name[ MAX_FSPEC_BUFSIZE ]; /* <len:MAX_FSPEC_BUFSIZE>
       Output:  item folder ("" == default folder), only used for Team Center Engineering,
                this is the name of the folder that the stock
                components will be placed into. */

    char    file_name[ UF_CFI_MAX_FILE_NAME_BUFSIZE ]; /* <len:UF_CFI_MAX_FILE_NAME_BUFSIZE>
       Output:  Name of file ("" == no name generated,
                default user exit will be called) */

    char    item_revision[UF_UGMGR_PARTREV_BUFSIZE]; /* <len:UF_UGMGR_PARTREV_BUFSIZE>
       Output:  item revision , only used for Team Center Engineering ("" == no revision generated,
                default user exit will be called) */

    char    item_type[UF_UGMGR_FTYPE_BUFSIZE]; /* <len:UF_UGMGR_FTYPE_BUFSIZE>
       Output:  item type, only used for Team Center Engineering  */

    char    item_name[UF_UGMGR_FNAME_BUFSIZE]; /* <len:UF_UGMGR_FNAME_BUFSIZE>
        Output:  item name, only used for Team Center Engineering. */

    char    component_name[ MAX_FSPEC_BUFSIZE ]; /* <len:MAX_FSPEC_BUFSIZE>
        Output:  component name, the name of the component in NX. */
};
typedef struct UF_ROUTE_component_name_plugin_s
    UF_ROUTE_component_name_plugin_t, *UF_ROUTE_component_name_plugin_p_t;

/* Structure passed to the STOCK_COMPONENT_LOOKUP plugin. */
struct UF_ROUTE_component_reuse_plugin_s
{
    tag_t   stock;
    /* Input:   Tag of the stock object */

    tag_t   new_stock_component;
    /* Output:  Tag of the part to replace the
                stock component with. */
};
typedef struct UF_ROUTE_component_reuse_plugin_s
    UF_ROUTE_component_reuse_plugin_t, *UF_ROUTE_component_reuse_plugin_p_t;

/* Structure passed to the STOCK_COMPONENT_LOCKED plugin. */
struct UF_ROUTE_component_lock_plugin_s
{
    tag_t   stock;
    /* Input:   Tag of the stock object */

    logical is_modifiable;
    /* Output:  TRUE if stock component can be modified,
                FALSE otherwise. */
};
typedef struct UF_ROUTE_component_lock_plugin_s
    UF_ROUTE_component_lock_plugin_t, *UF_ROUTE_component_lock_plugin_p_t;

/* Structure passed to the ALLOW_DEFAULT_ELBOW_PLACEMENT plugin. */
struct UF_ROUTE_allow_default_fitting_plugin_s
{
    tag_t                           rcp;
    /*  Input:  The rcp to place the fitting at.  */

    int                             num_spec_charx;
    /* Input:   Specification characteristics.  Each specification characteristic
                can have one or more possible values.  Default part selection ensures
                that every matching part has atleast one of the values from a
                multi valued specification characteristic.
                Eg: If FITTING_MATERIAL is a specification characteristic and
                    has values COPPER, STEEL - all matching parts have a
                    FITTING_MATERIAL value of either COPPER or STEEL.
     */
    UF_EPLIB_multi_val_charx_p_t    spec_charx; /*<len:num_spec_charx>*/

    UF_ROUTE_part_lib_part_t        match_criteria;
    /* Input:   Part descriptor characteristics that are not in the specification
                 characteristic list.  Part descriptor characteristics can
                only be single valued. These characteristics help uniquely
                determine the default fitting to place.
     */

    const char*         default_fitting_table;
    /* Input:   Part library table identifier to use for determining the default fitting.
                The identifier is defined in the Part Library View file for the application.
     */

    logical                         allow_placement;
    /* Output:  if TRUE, default elbow placement at the input RCP is valid */

    logical                         force_override;
    /* Output:  if TRUE, forces placement of the part specified in the
     *          the override_fitting definition. */

    UF_ROUTE_part_lib_part_t        override_fitting;
    /* Output:  Only used if force_override is TRUE.  Fully specifies the default fitting
                to place [include values of all selection characteristics].
     */
};
typedef struct UF_ROUTE_allow_default_fitting_plugin_s
    UF_ROUTE_allow_default_fitting_plugin_t, *UF_ROUTE_allow_default_fitting_plugin_p_t;

/* Structure passed to the SPECIFY_ITEM plugin.
 *
 * The SPECIFY_ITEM plugin selects a part, stock, elbow,
 * wire, cable, or shield conforming to the given
 * characteristics.
 *
 * The SPECIFY_ITEM plugin must filter the selected part
 * based on the current discipline and specification by
 * calling the FilterOnCurrentSpecifications routine.
 */
struct UF_ROUTE_specify_item_plugin_s
{
    int                             mode;
    /*  Input:  Specifies the type of item (e.g. part, stock, elbow, etc.)
     *          Valid values: (See uf_ui_route.h)
     *          UF_UI_ROUTE_PLV_INDEX_PARTS
     *          UF_UI_ROUTE_PLV_INDEX_STOCK,
     *          UF_UI_ROUTE_PLV_INDEX_ELBOWS
     *          UF_UI_ROUTE_PLV_INDEX_CUT_ELBOWS,
     *          UF_UI_ROUTE_PLV_INDEX_REPLACE_PART
     *          UF_UI_ROUTE_PLV_INDEX_WIRES,
     *          UF_UI_ROUTE_PLV_INDEX_CABLES
     *          UF_UI_ROUTE_PLV_INDEX_SHIELDS
     */

    const char*                     node_id;
    /*  Input:  Specifies the name/ID of the node in the
     *          Product Library View under which to look
     *          for matching characteristics.
     */

    int                             num_specifications;
    const char**                    specifications;
    /*  Input:  Specifies all of the disciplines and specifications
     *          that are currently valid.  Reserved for future use.
     */

    UF_ROUTE_part_lib_part_p_t      chosen_part;
    /*  Input:  Characteristics structure used to for item selection.
     *          Represents the characteristics from a part chosen by
     *          the user before calling the plug-in.
     *
     *  Output: Characteristics of the part the user selected while
     *          running the plug-in.
     */

    tag_t                           placer_object;
    /*  Output: Selected placement object.  A condemned point to stand in
    *           for screen position pick.  Will be a NULL_TAG in Assign
    *           Stock (UF_UI_ROUTE_PLV_INDEX_STOCK) mode.
    */

    double                          placer_object_pos[3];
    /*  Output: Placement position in Work Occurrence coordinates.
    */

    int                             error;
    /*  Output:  Zero indicates success
     */
};

typedef struct UF_ROUTE_specify_item_plugin_s
    UF_ROUTE_specify_item_plugin_t, *UF_ROUTE_specify_item_plugin_p_t;


typedef struct UF_ROUTE_characteristic_match_plugin_s
    UF_ROUTE_characteristic_match_plugin_t, *UF_ROUTE_characteristic_match_plugin_p_t;

/* Structure passed to the FIND_ROOT_NODE plugin.
 *
 * The FIND_ROOT_NODE plugin returns the lowest,
 * non-leaf INCLASS node that contains the given part.
 */
struct UF_ROUTE_find_root_node_plugin_s
{
    char                            item_id[ MAX_LINE_BUFSIZE ];
    /*  Input:  Specifies the part number (i.e. Teamcenter item ID)
     *          whose containing node the plug-in should return.
     */

    char                            node_id[ MAX_LINE_BUFSIZE ];
    /*  Output: Specifies the ID of the lowest, non-leaf,
     *          INCLASS node which contains the given part.
     */

    int                             error;
    /*  Output:  Zero indicates success
     */
};

typedef struct UF_ROUTE_find_root_node_plugin_s
    UF_ROUTE_find_root_node_plugin_t, *UF_ROUTE_find_root_node_plugin_p_t;


/* Structure passed to the UNIFY_PATH plugin.
 *
 * The UNIFY_PATH plugin should take the given tags and present the user
 * with a dialog to allow the user to select the new characteristics.
 * Then the UNIFY_PATH plugin should call the UnifyPath NXOpen routine
 * for each tag with the new characteristics.
 */
struct UF_ROUTE_unify_path_plugin_s
{
    int                             num_objects;
    tag_t*                          objects;
    /*  Input:  The array of objects to unify.
     */

    int                             error;
    /*  Output:  Zero indicates success
     */
};

typedef struct UF_ROUTE_unify_path_plugin_s
    UF_ROUTE_unify_path_plugin_t, *UF_ROUTE_unify_path_plugin_p_t;

struct UF_ROUTE_retrieve_eplib_data_s
{
    UF_EPLIB_part_lib_p_t   library;
    int                     error_code;
};

typedef struct UF_ROUTE_retrieve_eplib_data_s
            UF_ROUTE_retrieve_eplib_data_t, *UF_ROUTE_retrieve_eplib_data_p_t;

/* The duct size calculator plugins use this enumeration to tell the duct size calculator
   dialog about the attributes on the selected segments. */
enum UF_ROUTE_duct_segment_attribute_status_e
{
    UF_ROUTE_DUCT_EMPTY_ATTRIBUTES,     /* None of the selected segments have attributes. */
    UF_ROUTE_DUCT_ATTRIBUTES_NOT_EQUAL, /* The selected segments have attributes whose values don't match. */
    UF_ROUTE_DUCT_VALID_ATTRIBUTES      /* All of the selected segments have valid attributes. */
};
typedef enum UF_ROUTE_duct_segment_attribute_status_e UF_ROUTE_duct_segment_attribute_status_t,
             *UF_ROUTE_duct_segment_attribute_status_p_t;

/* The duct size calculator plugins use this enumeration to tell the duct size calculator
   dialog about any errors that may occur in a plugin.*/
enum UF_ROUTE_duct_calculator_errors_e
{
    UF_ROUTE_DUCT_ERROR_OK = 0,     /* No errors.*/
    UF_ROUTE_DUCT_NO_PLUGIN_FOUND,  /* Cannot find the plugin. Verify the plugin configuration in the application view file.*/
    UF_ROUTE_DUCT_CANT_CALCULATE    /* Cannot calculate all of the values given the input parameters.*/
};
typedef enum UF_ROUTE_duct_calculator_errors_e UF_ROUTE_duct_calculator_errors_t,
            *UF_ROUTE_duct_calculator_errors_p_t;

/* The duct size calculator dialog uses this enumeration to tell the plugin which parameter the dialog
   is sending to the plugin. The plugin should then calculate the value for this parameter. */
enum UF_ROUTE_duct_parameter_types_e
{
    UF_ROUTE_DUCT_HEIGHT,              /* maps to the height parameter of the duct*/
    UF_ROUTE_DUCT_WIDTH,               /* maps to the width parameter of the duct*/
    UF_ROUTE_DUCT_ASPECTRATIO,         /* maps to the Aspect ratio of the duct*/
    UF_ROUTE_DUCT_EQUIVALENT_DIAMETER, /* maps to the equivalent diameter of the rectangular or flat oval duct*/
    UF_ROUTE_DUCT_DIAMETER,            /* maps to the diameter of the circular duct*/
    UF_ROUTE_DUCT_AREA,                /* maps to the area parameter of the duct*/
    UF_ROUTE_DUCT_VELOCITY,            /* maps to the velocity parameter of the duct*/
    UF_ROUTE_DUCT_VOLFLOWRATE,         /* maps to the volume flow rate parameter of the duct*/
    UF_ROUTE_DUCT_SHAPE_CHANGE,        /* This enum member indicates that the user has changed the shape,
                                          so the parameters needs to be recalculated */
    UF_ROUTE_DUCT_DEFAULT              /* If no parameter is defined, default calculations will be done.*/
};

typedef enum UF_ROUTE_duct_parameter_types_e UF_ROUTE_duct_parameter_types_t,
            *UF_ROUTE_duct_parameter_types_p_t;

/* The duct size calculator dialog use this enumeration to tell the duct size calculator
   plugin the shape of the duct being calculated. */
enum UF_ROUTE_duct_shape_e
{
    UF_ROUTE_DUCT_RECTANGULAR,
    UF_ROUTE_DUCT_CIRCULAR,
    UF_ROUTE_DUCT_FLATOVAL
};

typedef enum UF_ROUTE_duct_shape_e UF_ROUTE_duct_shape_t,
            *UF_ROUTE_duct_shape_p_t;

/* The width parameter. This structure is only used by DuctSizeCalculator
*/
struct UF_ROUTE_duct_width_s
{
    double    value;
    tag_t     unit;
    logical   isLocked;
};

typedef struct UF_ROUTE_duct_width_s
    UF_ROUTE_duct_width_t, *UF_ROUTE_duct_width_p_t;

/* The height parameter. This structure is only used by DuctSizeCalculator
*/
struct UF_ROUTE_duct_height_s
{
    double    value;
    tag_t     unit;
    logical   isLocked;
};

typedef struct UF_ROUTE_duct_height_s
    UF_ROUTE_duct_height_t, *UF_ROUTE_duct_height_p_t;

/* The Aspect Ratio parameter. This structure is only used by DuctSizeCalculator
*/
struct UF_ROUTE_duct_aspectRatio_s
{
    double    value;
    logical   isLocked;
};

typedef struct UF_ROUTE_duct_aspectRatio_s
    UF_ROUTE_duct_aspectRatio_t, *UF_ROUTE_duct_aspectRatio_p_t;

/* The area parameter. This structure is only used by DuctSizeCalculator
*/
struct UF_ROUTE_duct_area_s
{
    double    value;
    logical   isLocked;
};

typedef struct UF_ROUTE_duct_area_s
    UF_ROUTE_duct_area_t, *UF_ROUTE_duct_area_p_t;

/* The Equivalent Diameter parameter. This structure is only used by DuctSizeCalculator
*/
struct UF_ROUTE_duct_eqvDiameter_s
{
    double    value;
    logical   isLocked;
};

typedef struct UF_ROUTE_duct_eqvDiameter_s
    UF_ROUTE_duct_eqvDiameter_t, *UF_ROUTE_duct_eqvDiameter_p_t;

/* The Diameter parameter. This structure is only used by DuctSizeCalculator
*/
struct UF_ROUTE_duct_diameter_s
{
    double    value;
    tag_t     unit;
    logical   isLocked;
};

typedef struct UF_ROUTE_duct_diameter_s
    UF_ROUTE_duct_diameter_t, *UF_ROUTE_duct_diameter_p_t;

/* The Volume Flow Rate parameter. This structure is only used by DuctSizeCalculator
*/
struct UF_ROUTE_duct_volFlow_s
{
    double    value;
    tag_t     unit;
    logical   isLocked;
};

typedef struct UF_ROUTE_duct_volFlow_s
    UF_ROUTE_duct_volFlow_t, *UF_ROUTE_duct_volFlow_p_t;

/* The Velocity parameter. This structure is only used by DuctSizeCalculator
*/
struct UF_ROUTE_duct_velocity_s
{
    double   value;
    tag_t    unit;
    logical  isLocked;
};

typedef struct UF_ROUTE_duct_velocity_s
    UF_ROUTE_duct_velocity_t, *UF_ROUTE_duct_velocity_p_t;

/* This structure contains all the parameters of the duct size calculator. The duct size calculator uses this structure
   to pass information to and receive information from the duct size calculator plugin.
   The duct size calculator plugin uses the UF_ROUTE_duct_parameter_types_e to know which parameter is being sent from the dialog.
   The plugin calculates the required values and updates this structure.
   Use the UF_ROUTE_duct_parameters_m macro to initialize this structure. */
struct UF_ROUTE_duct_parameters_s
{
    UF_ROUTE_duct_height_t       height;             /*Height of the duct*/
    UF_ROUTE_duct_width_t        width;              /*width of the duct*/
    UF_ROUTE_duct_diameter_t     diameter;           /*diameter of the duct*/
    UF_ROUTE_duct_area_t         area;               /*area of the duct*/
    UF_ROUTE_duct_eqvDiameter_t  equivalentDiameter; /*equivalent Diameter of the duct*/
    UF_ROUTE_duct_aspectRatio_t  aspectRatio;        /*Aspect ratio of the duct*/
    UF_ROUTE_duct_volFlow_t      volumeFlow;         /*volume Flow rate of the duct*/
    UF_ROUTE_duct_velocity_t     velocity;           /*velocity component of the duct*/
    double                       frictionLoss;       /*loss due to friction of the duct*/
    double                       velocityHead;       /*velocity of the duct*/
};

/* Users of the UF_ROUTE_duct_parameters_s structure may use this macro to initialize the structure. */
#define UF_ROUTE_duct_parameters_m( duct_parameters )           \
(                                                               \
    (duct_parameters).height.value                  = 0.0,      \
    (duct_parameters).height.unit                   = NULL_TAG, \
    (duct_parameters).height.isLocked               = false,    \
    (duct_parameters).width.value                   = 0.0,      \
    (duct_parameters).width.unit                    = NULL_TAG, \
    (duct_parameters).width.isLocked                = false,    \
    (duct_parameters).diameter.value                = 0.0,      \
    (duct_parameters).diameter.unit                 = NULL_TAG, \
    (duct_parameters).diameter.isLocked             = false,    \
    (duct_parameters).area.value                    = 0.0,      \
    (duct_parameters).area.isLocked                 = false,    \
    (duct_parameters).equivalentDiameter.value      = 0.0,      \
    (duct_parameters).equivalentDiameter.isLocked   = false,    \
    (duct_parameters).aspectRatio.value             = 0.0,      \
    (duct_parameters).aspectRatio.isLocked          = false,    \
    (duct_parameters).volumeFlow.value              = 0.0,      \
    (duct_parameters).volumeFlow.unit               = NULL_TAG, \
    (duct_parameters).volumeFlow.isLocked           = false,    \
    (duct_parameters).velocity.value                = 0.0,      \
    (duct_parameters).velocity.unit                 = NULL_TAG, \
    (duct_parameters).velocity.isLocked             = false,    \
    (duct_parameters).frictionLoss                  = 0.0,      \
    (duct_parameters).velocityHead                  = 0.0       \
)

typedef struct UF_ROUTE_duct_parameters_s UF_ROUTE_ductParams_t,
              *UF_ROUTE_ductParams_p_t;
/* The plugin for Duct Reinforcement uses this enumeration to tell the dialog
 the type of reinforcement to create*/
enum UF_ROUTE_duct_reinforcement_types_e
{
    UF_ROUTE_DUCT_REINFORCEMENT_TYPE_NONE,      /* No reinforcement needs to be created on the selected duct */
    UF_ROUTE_DUCT_REINFORCEMENT_TYPE_INSIDE,    /* Inside reinforcement needs to be created on the selected duct */
    UF_ROUTE_DUCT_REINFORCEMENT_TYPE_OUTSIDE    /* Outside reinforcement needs to be created on the selected duct */
};

typedef enum UF_ROUTE_duct_reinforcement_types_e UF_ROUTE_duct_reinforcement_types_t,
            *UF_ROUTE_duct_reinforcement_types_p_t;

/* The duct reinforcement plugin evaluates the parent duct selected and determines
 the various parameters for duct reinforceemnt creation. These parameters are
 stored using the following struct.*/
struct UF_ROUTE_duct_reinforcement_parameters_s
{
    UF_ROUTE_duct_reinforcement_types_t     reinforcementType;                 /* Type of reinforcement to be applied options are None, Inside or Outside */
    logical                                 parallelStockBlockVisibility;      /* Parallel Stock Block Visibility */
    UF_ROUTE_part_lib_part_t                parallelStock;                     /* Stock to be applied parallel to axis of the duct */
    int                                     numberOfPairs;                     /* Number of pairs of parallel reinforcements to be applied */
    double                                  spacing;                           /* Space between each pair of reinforcement applied parallel to axis of the duct */
    logical                                 perpendicularStockBlockVisibility; /* Perpendicular Stock Block Visibility */
    logical                                 reinforcementTypeBlockVisibility;  /* Reinforcement Type Visibility */
    UF_ROUTE_part_lib_part_t                perpendicularStock;                /* Stock to be applied perpendicular to axis of the duct */
    double                                  interval;                          /* Interval at which perpendicular stock is to be applied */
    double                                  clearnce;                          /* Minimum clearance value from the start and end of the parent duct */
    logical                                 editMode;                          /* Is the plugin invoked during edit of duct reinforcement*/
};

typedef struct UF_ROUTE_duct_reinforcement_parameters_s UF_ROUTE_duct_reinforcement_params_t,
              *UF_ROUTE_duct_reinforcement_params_p_t;

/*********************************************************************
                      ** Function Prototypes **
 ********************************************************************/

/**********************************************************************
Sets the current Application View for the current session. This
function must be called after loading an Application View using
UF_ROUTE_load_app_view.

Environment: Internal  and  External

See Also:  UF_ROUTE_load_app_view


History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_current_app_view
(
UF_ROUTE_application_view_t * app_view  /* <I>
                                        Sets the current Application View and
                                        remains active till set again. If the
                                        current Application View is unloaded
                                        reset the current Application View to
                                        NULL.
                                        */
);

/**********************************************************************
Tests to see whether two segments are tangent to one another where
they both are connected at the given RCP.

Return:
         Return code:
        TRUE    = Segments are tangent
        FALSE   = Segments are not tangent

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_are_segments_tangent
(
tag_t segment1 ,/* <I>
                Segment to test
                */
tag_t segment ,/* <I>
               Segment to test
               */
tag_t rcp  /* <I>
           RCP common to both segments
           */
);/* <NEC> */


/**********************************************************************
Loads the stock data into the current part. The stock data tag can be
used to assign stocks to segments using UF_ROUTE_assign_stock.
Once the stock has been "loaded", several calls to
UF_ROUTE_assign_stock may be made (for various segments)
without the need to "load" another.

The Assembly Search Directory list, specified via the load_options.def
file or interactively through the File -->Options-->Load Options dialog,
is used to locate the part file for the stock.

Environment: Internal  and  External

See Also:  UF_ROUTE_assign_stock


History: Original release was in V13.0.
 *********************************************************************/
extern UFUNEXPORT int UF_ROUTE_load_stock_data
(
char * part_name ,/* <I>
                  Name of the stock part family.
                  */
char * member_name ,/* <I>
                    Name of the member part in the stock part
                    family or NULL if part_name is not a Part
                    Family.
                    */
int stock_style ,/* <I>
                 Stock style can have value of
                 UF_ROUTE_STYLE_NONE
                 UF_ROUTE_STYLE_SIMPLE or
                 UF_ROUTE_STYLE_DETAIL
                 */
tag_t * stock_data_tag ,/* <O>
                        Object Identifier of the loaded stock_data.
                        */
tag_t * anchor_tag ,/* <O>
                    Object Identifier of the anchor of the
                    stock.
                    */
tag_t * cross_tag  /* <O>
                   Object Identifier of the cross_section of
                   the stock.
                   */
);


/**********************************************************************
Returns the diameter of the Stock. Routing determines the
diameter associated with Stock by reading the DIAMETER
characteristic assigned to the Stock_Data object referenced by the
Stock object. If no such characteristic exists, 0.0 is returned as the
diameter.

Environment: Internal  and  External

See Also:

History:Original release was in V14.0.
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_diameter
(
tag_t stock ,/* <I>
             Object identifier of the Stock.
             */
double * diameter  /* <O>
                   Diameter of the Stock.
                   */
);

/**********************************************************************
Returns the stock tag assigned to the Segment or attached to the
Stock Port or the stock associated with the Stock Solid feature. The
input may be a Port of a stock, a Segment, Stock Solid feature tag or a
Curve used to define the segment that is assigned the stock. If no
stock is assigned to the segment a NULL_TAG is returned.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_object_stock
(
tag_t obj_id ,/* <I>
              Object identifier to interrogate. Can be a Port
              of a Stock, a Segment, the Stock solid feature
              or a Curve object.
              */
tag_t * stock  /* <O>
               Stock tag attached to the input object else
               NULL_TAG.
               */
);

/**********************************************************************
Tests whether two stock objects are equivalent.  Two stock objects are
equivalent if they reference the same stock data, the same anchor, and
all characteristic values are equal.

Return:UF_ROUTE_ask_stock_stock_data

         Return code:
        TRUE = Stock objects are equivalent
        FALSE = Stock objects are not equivalent

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_is_stock_equal
(
tag_t stock1 ,/* <I>
              Tag of stock object
              */
tag_t stock2  /* <I>
              Tag of stock object
              */
);/* <NEC> */

/**********************************************************************
Return the absolute min-max box that contains all the entities
in the view.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_calc_abs_minmax_box
(
tag_t dwg_view, /* <I>
                View tag
                */
double box[6]   /* <O>
                Absolute coordinates of the min_x,
                max_x, min_y, max_y, min_z, max_z
                */
);
/**********************************************************************
Unexplode the components in a view.

Environment: Internal  and  External

See Also:

History:
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_unset_shadow_for_view
(
tag_t  view   /* <I>
              Tag of the view to unexplode
              */
);

/**/
#ifndef UF_ROUTE_tag_list_s_defined
#define UF_ROUTE_tag_list_s_defined
/*****************************************************************************

  Structure used to store a variable length array of tags.

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
struct UF_ROUTE_tag_list_s
{
    unsigned int      num_alloc;  /* Number of elements allocated for the Variable
                                     length Array of tags
                                   */
    unsigned int      num_used;   /* Currently used Number of elements in array
                                   */
    tag_t             *array;     /*  <len:num_alloc>Variable length array of tags
                                   */
};
typedef struct UF_ROUTE_tag_list_s
               UF_ROUTE_tag_list_t, *UF_ROUTE_tag_list_p_t ;
#endif

/*****************************************************************************
   Used by the Branch Path Numbering plugin.
   See UFD_Routing_BranchPathNumbering.cxx for an example plugin.
*****************************************************************************/
enum UF_ROUTE_branch_path_numbering_sequence_method_e
{
    UF_ROUTE_branch_path_numbering_sequence_numbers,    /* 1, 2, 3,..... */
    UF_ROUTE_branch_path_numbering_sequence_upper_case, /* A, B, C,..... */
    UF_ROUTE_branch_path_numbering_sequence_lower_case  /* a, b, c,..... */
};
typedef enum UF_ROUTE_branch_path_numbering_sequence_method_e
             UF_ROUTE_branch_path_numbering_sequence_method_t, *UF_ROUTE_branch_path_numbering_sequence_method_p_t;

struct UF_ROUTE_branch_path_numbering_s
{
    tag_t                                            startingSegment;         /* The starting segment.                                            */
    const char*                                      prefix;                  /* The prefix to add to the ID. Can be NULL.                        */
    const char*                                      suffix;                  /* The suffix to append to the ID. Can be NULL.                     */
    UF_ROUTE_branch_path_numbering_sequence_method_t sequenceMethod;          /* The sequence method to use when numbering (e.g. 1,2,3 or a,b,c)  */
    const char*                                      startValue;              /* The starting value for the first branch.                         */
    const char*                                      firstBranchID;           /* The formula for determining the first branch's ID.               */
    const char*                                      nextBranchID;            /* The formula for determining the next branch's ID.                */
    logical                                          displayBranchPathIDs;    /* Should the plugin also create a drafting annotation?             */
    logical                                          reassignBranchPathIDs;   /* Should any existing IDs be overwritten?                          */
};
typedef struct UF_ROUTE_branch_path_numbering_s
        UF_ROUTE_branch_path_numbering_t, *UF_ROUTE_branch_path_numbering_p_t;

/* Output data structure */
struct UF_ROUTE_cb_data_out_s
{
    char   part_name[UF_ATTR_MAX_STRING_BUFSIZE];       /* part name, E.g. "pipe_flg_blind"  */
    char   member_name[UF_ATTR_MAX_STRING_BUFSIZE];     /* member name , E.g., "p3036" */
    char   part_number[UF_ATTR_MAX_STRING_BUFSIZE];     /* part number, E.g., "EDS-3002" */
    int    num_charx;                               /* number of charx */
    UF_ROUTE_part_lib_part_t* part;
    UF_ROUTE_charx_p_t   charx_list;                /* charx list  */
};
typedef struct UF_ROUTE_cb_data_out_s UF_ROUTE_cb_data_out_t, * UF_ROUTE_cb_data_out_p_t;

/*****************************************************************************

This function is used to replace a stock component with an equivalent stock
component.  This functions main purpose is for component reuse with stock
parts.

The function first calls the user exit for finding a part for reuse, and
then replaces all instances in the work part, of that part with the returned part.
If no part is returned from the user exit then nothing is done.

The input to this function is the tag of the stock object.

Environment: Internal and External

See Also:

History: Released in V19.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_reuse_stock_part
(
    tag_t   stock   /* <I>    Tag of the stock object. */
);

/*****************************************************************************

This function is used to change the name of a stock component part.

Environment: Internal and External

See Also:

History: Released in V19.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_stock_part_name
(
    tag_t   stock,      /* <I>  Tag of the stock object */
    char*   part_name   /* <I>  New name of the stock component */
);


#ifdef __cplusplus
}
#endif

#include <uf_retiring.h>

#undef EXPORTLIBRARY

#endif /* UF_ROUTE_H_INCLUDED */
