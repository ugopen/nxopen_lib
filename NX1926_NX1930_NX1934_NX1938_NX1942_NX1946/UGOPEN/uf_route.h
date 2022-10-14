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

struct UF_ROUTE_app_view_desc_s
{
    char *name;
    char *filename;
};
typedef struct UF_ROUTE_app_view_desc_s UF_ROUTE_app_view_desc_t,
               *UF_ROUTE_app_view_desc_p_t;

/* Characteristic description */
struct UF_ROUTE_char_desc_s
{
    char *name;
    int   type;
};
typedef struct UF_ROUTE_char_desc_s UF_ROUTE_char_desc_t,
               *UF_ROUTE_char_desc_p_t;

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

typedef struct ROUTE_place_solution_s *UF_ROUTE_place_solution_p_t;

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
Loads an application view structure from a data file. It does not set
the Application View. Multiple Application Views may be loaded but
only one of them can be made current. Call
UF_ROUTE_set_current_app_view to set this Application View in the
session. Since memory is allocated in this function,
UF_ROUTE_unload_app_view must be called to free memory. Do
NOT use UF_free to free this memory.

If only a simple file name is specified in the filename variable, the
data file is looked for in:

         UGII_ROUTING_APP_VIEW_DIR    (An environment variable)
         UGII_BASE_DIR/ugrouting/

Environment: Internal  and  External

See Also:  UF_ROUTE_set_current_app_view
            UF_ROUTE_unload_app_view



History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_load_app_view
(
char * filename ,/* <I>
                 Name of the application view definition file.
                 */
UF_ROUTE_application_view_p_t * app_view  /* <OF,free:UF_ROUTE_unload_app_view>
                                          Filled application view data.
                                          This must be freed by calling
                                          UF_ROUTE_unload_app_view.
                                          */
);

/**********************************************************************
Frees data allocated during loading of the Application View using
UF_ROUTE_load_app_view. Once the Application View has been
freed then the current Application View must be set to NULL using
UF_ROUTE_set_current_app_view.

Environment: Internal  and  External

See Also:


History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_unload_app_view
(
UF_ROUTE_application_view_p_t app_view  /* <I>
                                        Application view data to be freed.
                                        */
);/* <NON_NXOPEN> */

/**********************************************************************
Returns the current application view after
UF_ROUTE_set_current_app_view has been used to set the
application view.

Return:
    Returns the current application view which may be NULL.

Environment: Internal  and  External

See Also:  UF_ROUTE_set_current_app_view


History:Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT UF_ROUTE_application_view_t * UF_ROUTE_ask_current_app_view( void );/* <NEC> */

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
Returns a string containing the filename of the application view.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_filename
(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of Application View
                                        structure
                                        */
char ** filename  /* <O>
                  Filename of the application view.
                  */
);

/**********************************************************************
Returns a string containing the name of the Application View.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_name
(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of Application View
                                        structure
                                        */
char   ** name  /* <O>
                Name of the Application View.
                */
);

/**********************************************************************
Returns a string containing the description of the Application View.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_desc
(
UF_ROUTE_application_view_t  * app_view ,/* <I>
                                         Address of Application View
                                                structure
                                        */
char   ** description  /* <O>
                       Application View description.
                      */
);

/**********************************************************************
Returns an integer value which is a bit mask indicating the allowable
curve types for the given Application View. The bits set in this value
can be tested using symbols defined in uf_route.h. These are:
UF_ROUTE_AV_CURVES_LINES,
UF_ROUTE_AV_CURVES_ARCS, and
UF_ROUTE_AV_CURVES_SPLINES.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_curves
(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of the Application View
                                        structure
                                        */
int  * curves  /* <O>
               Flags indicating allowed curve
               types
               */
);

/**********************************************************************
Inquires the type of part library used by the given application view.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_plib_type
(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Application view to query
                                        */
int * type  /* <O>
            Part library type:
            UF_ROUTE_LIBRARY_TYPE_FILE_SELECT
            UF_ROUTE_LIBRARY_TYPE_VIEW
            UF_ROUTE_LIBRARY_TYPE_EXTERNAL
            */
);

/**********************************************************************
Returns the default stock style defined in the application view. The
style could be one of
UF_ROUTE_STYLE_NONE,
UF_ROUTE_STYLE_SOLID, or
UF_ROUTE_STYLE_DETAIL.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_def_style
(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of the Application View
                                        structure
                                        */
int * style  /* <O>
             Default stock style
             */
);

/**********************************************************************
Returns the intersection of the required stock characteristics and required
part characteristics for the current discipline of the application view.

This routine is deprecated. Please use NXOpen::Preferences::RoutingApplicationView::GetRequiredCharacteristics.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_req_charx
(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of Application View
                                        structure
                                        */
int   * num_charx ,/* <O>
                   Number of required
                   characteristics
                   */
UF_ROUTE_char_desc_p_t * charx  /* <OF,len:num_charx>
                                Required characteristics
                                */
);

/**********************************************************************
Returns the intersection of the optional stock characteristics and optional
part characteristics for the current discipline of the application view.

This routine is deprecated. Please use NXOpen::Preferences::RoutingApplicationView::GetOptionalCharacteristics.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_opt_charx
(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of Application View
                                        structure
                                        */
int  * num_charx ,/* <O>
                  Number of optional characteristics
                  */
UF_ROUTE_char_desc_p_t * charx  /* <OF,len:num_charx>
                                Optional characteristics
                                */
);

/**********************************************************************
Returns the number of fabrication characteristics and a structure
containing the characteristic types, values and titles. These
characteristics must be set for any fabrication created out of a Routing
assembly.

This routine is deprecated. Please use NXOpen::Preferences::RoutingApplicationView::GetFabricationCharacteristics.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_fab_charx
(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of Application View
                                        structure
                                        */
int * num_charx ,/* <O>
                 Number of fabrication
                 characteristics.
                 */
UF_ROUTE_char_desc_p_t *        entry  /* <OF,len:num_charx>
                                       Structure containing the
                                       characteristic types, titles and
                                       values.
                                       */
 );

/**********************************************************************
Load the list of application view descriptions.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_load_app_view_list
(
int              *num_app_views,  /* <O>
                                  num_app_views - Number of application
                                  views
                                  */
UF_ROUTE_app_view_desc_p_t *app_views
                                  /* <OF,len:num_app_views>
                                  app_views - Allocated array of application
                                  view descriptions (Array of Name/File
                                  pair structures).  This array should be
                                  freed by calling UF_free.
                                  */
);

/**********************************************************************
Returns the position (in absolute coordinates) of an anchor.  If the tag
is an occurrence of an anchor, then the position of the occurrence is
returned.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_anchor_position
(
tag_t anchor_tag ,/* <I>
                  Anchor to query
                  */
double position[3]  /* <O>
                    Position of anchor (ABS)
                    */
);

/**********************************************************************
When stock is assigned to a segment, or segments, an anchor is chosen
for the placement of the stock on the centerline.  This routine inquires,
for a given anchor, which stock is using this anchor for that position.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_anchor_stock
(
tag_t anchor_tag ,/* <I>
                  Tag of anchor to query
                  */
int * num_stocks ,/* <O>
                  The number of stock objects using this anchor
                  (should be 1)
                  */
tag_t ** stocks  /* <OF,len:num_stocks>
                 The array of stock objects. Use UF_free to
                 deallocate memory when no longer required.
                 */
);

/**********************************************************************
A stock data object has 0 or more anchor objects associated with it to
choose from when assigning it as stock.  This routine allows you to
query an anchor object for any stock data objects which may reference it.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_anchor_stock_data
(
tag_t anchor_tag ,/* <I>
                  Tag of anchor to query
                  */
int * num_stock_data ,/* <O>
                      Count of stock data objects returned
                      */
tag_t ** stock_datas  /* <OF,len:num_stock_data>
                      Array of stock data objects.  This must be freed
                      by calling UF_free.
                      */
);
/**********************************************************************
Creates a new anchor associative to the position of an existing point.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_anchor_from_pnt
(
tag_t object_in_part ,/* <I>
                      Object in part to create new anchor
                      NULL_TAG = work part
                      */
tag_t ref_point ,/* <I>
                 Tag of point object
                 */
tag_t * anchor  /* <O>
                Tag of new anchor
                */
);
/**********************************************************************
Creates an anchor given a set of coordinates.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_anchor_from_pos
(
tag_t object_in_part ,/* <I>
                      Tag of object in part to create new object
                      NULL_TAG = work part
                      */
double point_pos[3] ,/* <I>
                     Absolute position to create anchor
                     */
tag_t * anchor  /* <O>
                Tag of created anchor
                */
);

/**********************************************************************
Determine if the supplied object is a Routing anchor.

Environment: Internal  and  External

See Also:

History: Original release was in V19.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_is_part_anchor
(
tag_t object ,/* <I>
            Object to query.
            */
logical *is_anchor /* <O>
                    True if the object is a Routing part anchor; false otherwise
                    */
);

/**********************************************************************
Locates the rcp position coordinates in context to the work view
coordinate system for a standard heal path.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_heal_pos
(
int method ,/* <I>
            The type of standard heal path to be
            created.
            */
double  end_pos[2][3] ,/* <I>
                       The position of the ends to be joined by
                       the heal path in work coordinates.
                       */
double  end_uvecs[2][3] ,/* <I>
                         Unit vectors associated with the objects
                         being joined. Directed away from the
                         object.
                         */
double extensions[2] ,/* <I>
                      The length of the extension segments
                      which will be created between end
                      positions and the standard heal path.
                      */
int * num_pos ,/* <O>
               The number of rcps created in the
               standard heal path.
               */
double * heal_pos[3]  /* <OF,len:num_pos>
                      Array of  positions of where the rcps are
                      created in the standard heal path. Must be
                      freed using UF_free.
                      */
);
/**********************************************************************
Creates a new RCP at the center of the given arc or circular edge.
This RCP is derived from the given curve and moves if the curve is
moved. If a previously created RCP exists at this location, it is
returned.

Environment: Internal  and  External

See Also:

History:
**********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_rcp_arc_center
(
tag_t arc ,/* <I>
           Object identifier of an existing arc or circular edge.
           */
tag_t * new_rcp  /* <O>
                 Object identifier of the newly created RCP. In case
                 an RCP exists at this location then the object
                 identifier of this RCP is returned.
                 */
);

/**********************************************************************

Creates a new RCP at a point corresponding to the given parameter
value along the given curve. If a previously created RCP exists at this
location, it is returned.

This routine should be used to create the RCPs at the ends of any
Segment which you create using UF_ROUTE_create_seg_on_curve.
This is to insure that if the curve is transformed or moved, both the
Segment and its RCPs also move with the curve.

Environment: Internal  and  External

See Also:  UF_ROUTE_create_seg_on_curve


History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_rcp_curve_parm
(
tag_t curve ,/* <I>
             Object identifier of an existing curve.
             */
double parm ,/* <I>
             Normalized curve parameter at which to create the
             RCP. The value should be between 0 and 1,
             inclusive.
             */
tag_t * new_rcp  /* <O>
                 Object identifier of the newly created RCP. The
                 RCP location is derived from the given curve and
                 parameter and the RCP's position updates if the
                 curve is moved. In case an RCP exists at this
                 location then the object identifier of this RCP is
                 returned.
                 */
);

/**********************************************************************
Creates a new RCP attached to the existing point if no previous RCP
exists at this location. Else it returns the previously created RCP.

Environment: Internal  and  External

See Also:


History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_rcp_point
(
tag_t point ,/* <I>
             Object identifier of an existing point.
             */
tag_t * new_rcp  /* <O>
                 Object identifier of the newly created RCP at this
                 point. The RCP location is derived from this point
                 at each update. In case an RCP exists at this
                 location then the object identifier of this RCP is
                 returned.
                 */
);

/**********************************************************************
Creates a new RCP at the given location if no previous RCP exists.
If an RCP already exists it returns the previously created RCP.

Environment: Internal  and  External

See Also:  UF_ROUTE_create_rcp_by_work_pos


History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_rcp_position
(
double pos[3] ,/* <I>
                Location of RCP in absolute display coords.
               */
tag_t * new_rcp  /* <O>
                 Object identifier of the newly created RCP
                 at this location. In case an RCP exists at
                 this location then the object identifier of
                 this RCP is returned
                 */
);

/**********************************************************************
Obtains the position of the RCP in absolute coordinate system.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_rcp_position
(
tag_t rcp_id ,/* <I>
              Object Identifier of the RCP to inquire
              */
double   rcp_pos[3]  /* <O>
                     Position of the RCP in absolute csys.
                    */
);

/**********************************************************************
Returns the number of segments and their tags attached to a given
RCP.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_rcp_segs
(
tag_t rcp_id ,/* <I>
              Object identifier of the RCP.
              */
int * num_segs ,/* <O>
                Number of segments at this RCP
                */
tag_t ** segments  /* <OF,len:num_segs>
                   Pointer to an allocated array of segments.
                   This must be freed using UF_free.
                   */
);

/**********************************************************************
Inquires about any RCP that is associated with the port.  This can be
either from one of the segment ends of the segment from which the
port is derived, or from an RCP that is derived from this port.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_rcp_on_port
(
tag_t port_tag ,/* <I>
                Tag of port to query.
                */
tag_t * rcp_tag  /* <O>
                 Tag of RCP (or NULL_TAG).
                 */
);

/**********************************************************************
Inquires the segments attached to a given RCP.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_rcp_segments
(
tag_t rcp_tag ,/* <I>
               Tag of Route Control Point to query
               */
int * num_segs ,/* <O>
                Number of segments returned
                */
tag_t ** segments  /* <OF,len:num_segs>
                   Array of segments. Use UF_free to deallocate
                   memory when no longer required.
                   */
);

/**********************************************************************
Finds all the ports connected to a given RCP.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_rcp_ports
(
tag_t rcp ,/* <I>
           Tag of Route Control Point to query.
           */
int * num_ports ,/* <O>
                 Number of ports returned.
                 */
tag_t ** ports  /* <OF,len:num_ports>
                Array of ports. Use UF_free to deallocate memory
                when no longer required.
                */
);

/**********************************************************************
Creates an RCP whose position is associatively defined by an existing
port.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_rcp_at_port
(
tag_t port ,/* <I>
            Tag of reference port
            */
tag_t * new_rcp ,/* <O>
                 tag of created/found RCP
                 */
logical check_existing_rcp ,/* <I>
                            TRUE = use existing RCP at specified position
                            FALSE = always create a new RCP
                            */
logical * found_existing_rcp  /* <O>
                              TRUE = existing RCP found and used
                              FALSE =  new RCP was created
                              */
);

/**********************************************************************
Creates (or finds) and RCP at the position derived by specifying an
existing RCP or port plus a wcs offset from that port.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_rcp_by_wcs_off
(
tag_t object ,/* <I>
              Reference RCP or port( in the work part )
              */
double offset[3] ,/* <I>
                  Offset in absolute WCS
                  */
tag_t * new_rcp ,/* <O>
                 Tag of new or found RCP
                 */
logical check_existing_rcp ,/* <I>
                            TRUE = use existing RCP at specified position
                            FALSE = always create a new RCP
                            */
logical * found_existing_rcp  /* <O>
                              TRUE = existing RCP found and used
                              FALSE = new RCP was created
                              */
);

/**********************************************************************
Creates (or finds) an RCP at a work position in the WCS.

Environment: Internal  and  External

See Also:  UF_ROUTE_create_rcp_position

History:
 **********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_rcp_by_work_pos
(
double work_pos[3] ,/* <I>
                    Position in absolute work part coords
                    */
tag_t * new_rcp ,/* <O>
                 Tag of created RCP
                 */
logical check_existing_rcp ,/* <I>
                            TRUE = use existing RCP at specified position
                            FALSE = always create a new RCP
                            */
logical * found_existing_rcp  /* <O>
                              TRUE = existing RCP found and used
                              FALSE =  new RCP was created
                              */
);

/**********************************************************************
Creates an RCP in the work part whose position is associative to an
occurrence of an RCP.

Environment: Internal  and  External

See Also:

History:
 **********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_rcp_on_rcp
(
tag_t occ_rcp ,/* <I>
               Tag of reference rcp occurrence
               */
tag_t * new_rcp ,/* <O>
                 Tag of created/found RCP
                 */
logical check_existing_rcp ,/* <I>
                            TRUE = use existing RCP at specified position
                            FALSE = always create a new RCP
                            */
logical * found_existing_rcp  /* <O>
                              TRUE = existing RCP found and used
                              FALSE =  new RCP was created
                              */
);

/**********************************************************************
Of the given RCPs, remove any that are unnecessary, i.e. they are
placed in a straight line with the adjacent RCPs.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_simplify_rcps
(
int count ,/* <I>
           Count of RCPs
           */
tag_t rcps[]  /* <I,len:count>
              Array of RCPs
              */
);

/**********************************************************************
Creates a segment between two RCPs on the curve and follows its
profile. The RCPs supplied to this routine should be created with the
UF_ROUTE_create_rcp_curve_parm.

Environment: Internal  and  External

See Also :  UF_ROUTE_create_rcp_curve_parm


History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_seg_on_curve
(
tag_t curve ,/* <I>
             Object Identifier of the curve to follow
             while creating the segment.
             */
tag_t rcp1 ,/* <I>
            Object Identifier of the start RCP on the
            curve.
            */
tag_t rcp2 ,/* <I>
            Object Identifier of the end RCP on the
            curve.
            */
tag_t * new_segment  /* <O>
                     Object identifier of newly created segment.
                     */
);

/**********************************************************************
Creates a segment between two existing RCPs and creates DCM3 segment if dcm3 is active

Environment: Internal  and  External

See Also:


History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_seg_thru_rcps
(
tag_t rcp1 ,/* <I>
            Object Identifier of the start RCP.
            */
tag_t rcp2 ,/* <I>
            Object Identifier of the end RCP.
            */
tag_t * new_segment  /* <O>
                     Object identifier of newly created segment.
                     */
);

/**********************************************************************
Returns the tags of the end RCPs for a given segment.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_seg_rcps
(
tag_t  segment ,/* <I>
                Object identifier of the segment.
                */
tag_t  rcp[2]  /* <O>
               Object identifiers of the end RCPs.
               */
);

/**********************************************************************
Finds the curve which a segment is "following"

Environment: Internal  and  External

See Also:  UF_ROUTE_create_seg_on_curve

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_seg_curve
(
tag_t  segment ,/* <I>
                Object identifier of the segment.
                */
tag_t * curve  /* <O>
               Object identifier of the follow curve. If the given
               segment does not follow a curve, NULL_TAG is
               returned.
               */
);

/**********************************************************************
Returns the length of the Segment.

Environment: Internal  and  External

See Also:

History:
*********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_length
(
tag_t segment ,/* <I>
               Object identifier of the Segment.
               */
double * length  /* <O>
                 Length of the segment
                 */
);

/**********************************************************************
Returns the start and end positions of a segment.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_end_pnts
(
tag_t segment ,/* <I>
               Tag of segment to query.
               */
double start[3] ,/* <O>
                 Position of start of segment.
                 */
double end[3]  /* <O>
               Position of end of segment.
               */
);

/**********************************************************************
Inquires the part (fitting) to which the segment is interior.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_int_part
(
tag_t segment ,/* <I>
               Tag of segment to query.
               */
tag_p_t part  /* <O>
              Tag of part occurrence
              */
);

/**********************************************************************
Inquires the parts (fittings) to which the segment is interior.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_int_parts
(
tag_t segment ,/* <I>
               Tag of segment to query.
               */
int   *num_parts, /* <O>
                    Number of part_occurrences
                 */
tag_p_t *parts  /* <OF,len:num_parts>
              Array of part occurrences
              */
);

/**********************************************************************
Returns the Stock object(s) associated with the specified Segment.
Can return an empty list, which indicates that no Stock was assigned
to the Segment.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_stock
(
tag_t segment ,/* <I>
               Tag of segment to query.
               */
int * num_stock ,/* <O>
                 Number of stock objects returned.
                 */
tag_t ** stock  /* <OF,len:num_stock>
                Array of stock objects. Use UF_free to deallocate
                memory when no longer required.
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
Inquires whether the given RCP is segment end 0 or segment end 1.
This index is used by some other UF_ROUTE functions.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_end_idx
(
tag_t segment ,/* <I>
               Tag of segment to query.
               */
tag_t end_object ,/* <I>
                  Tag of RCP at segment end.
                  */
int * index  /* <O>
             End index of RCP on segment (0 or 1).
             */
);

/**********************************************************************
Returns curve parameters of segment at given end index.

Environment: Internal  and  External

See Also :  UF_ROUTE_ask_segment_end_idx

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_end_props
(
tag_t segment ,/* <I>
               Segment to query
               */
int end ,/* <I>
         End of segment to query
         */
double * parameter ,/* <O>
                    Curve parameter at end
                    */
double * norm_parameter ,/* <O>
                         Normalized parameter at end
                         */
double point[3] ,/* <O>
                 Position of end
                 */
double tangent[3]  /* <O>
                   Tangent vector at end
                   */
);
/**********************************************************************
Inquires whether the segment is within the extent of the given part
occurrence.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_is_segment_inside_part
(
tag_t segment ,/* <I>
               Tag of segment
               */
tag_t part_occ  /* <I>
                Part occurrence
                */
);/* <NEC> */

/**********************************************************************
Attempts to combine segments which are colinear and whose
intermediate rcp's do not branch.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_simplify_segments
(
int count ,/* <I>
           Count of segments passed
           */
tag_t segments[] ,/* <I,len:count>
                    Array of segments
                    */
int *num_new_segments ,/* <O>
                       Count of segments returned
                       */
tag_t ** new_segments  /* <OF,len:num_new_segments>
                       Array of segments created. Use UF_free to
                       deallocate memory when no longer required.
                       */
);

/**********************************************************************
Adds a segment to a given stock object; this is basically the operation
of assigning the stock to the segment.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_add_segment_to_stock
(
tag_t stock ,/* <I>
             Stock object to modify
             */
tag_t segment  /* <I>
               Segment to add to the stock
               */
);

/**********************************************************************
Removes the given segment from all of the given stock objects.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_remove_seg_from_stock
(
tag_t seg ,/* <I>
           Tag of segment
           */
int num_stock ,/* <I>
               Count of stock objects
               */
tag_t *stock  /* <I,len:num_stock>
              Array of stock objects
              */
);

/**********************************************************************
 This function uses the supplied characteristics (charx) to
 locate or retrieve the corresponding stock data. The structure
 input to this function (specifying the stock charx) must contain
 a PART_NAME charx and, if the part is a PART FAMILY part, the
 MEMBER_NAME.

 The output of a call to UF_ROUTE_match_charx_in_plib may be used
 to load the UF_ROUTE_part_lib_part_p_t structure.

     If stock matching the given charx already exists
     within the work part, the tag of the stock data, anchor,
     and cross section objects matching the charx, anchor name,
     and style given as input will be returned.

     If there is no stock data object in the work part matching
     the supplied charx, the PART_NAME (and optionally MEMBER_NAME)
     charx is used to locate the stock part.

     The stock data information from this stock part is then
     imported (retrieved) into the current work part and the
     tag of the stock data object is returned. Also returned are
     the tag of the anchor and cross section objects which match
     the given anchor name and stock style.

 In either situation, the stock data, anchor, and cross section
 objects may then be used to assign stock of this type to segments
 within the routing.

 Environment: Internal  and  External

 See Also:

 History:
 *********************************************************************/
extern UFUNEXPORT int UF_ROUTE_load_stock_by_charx
(
UF_ROUTE_part_lib_part_p_t  stock, /* <I>
                                   Pointer to a UF_ROUTE_part_lib_part_p_t
                                   structure filled in with the PART_NAME,
                                   MEMBER_NAME, and other characteristics
                                   corresponding to the stock to be used.
                                   */
char  *anchor_name,                /* <I>
                                   the name of the anchor in the stock
                                   data to be used. May be NULL.
                                   */
int   stock_style,                 /* <I>
                                   the stock style integer which
                                   determines which cross section
                                   of the stock data to use.One of:
                                   UF_ROUTE_STYLE_NONE
                                   UF_ROUTE_STYLE_SIMPLE
                                   UF_ROUTE_STYLE_DETAIL
                                   */
tag_t *stock_data_tag,             /* <O>
                                   the tag of the stock data object
                                   */
tag_t *anchor_tag,                 /* <O>
                                   the tag of the anchor object
                                   */
tag_t *cross_tag                   /* <O>
                                   the tag of the cross section object
                                   */
);

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
Assigns stock to a set of segments. The segments need not belong to
the same path. This function uses the Stock Data, Anchor, and Cross
Section objects returned by "loading" the stock. Once the stock has
been "loaded", using UF_ROUTE_load_stock_data, several calls to
UF_ROUTE_assign_stock may be made (for various sets of segments)
without the need to "load" another.

Environment: Internal  and  External

See Also:  UF_ROUTE_load_stock_data


History: Original release was in V13.0.
 *********************************************************************/
extern UFUNEXPORT int UF_ROUTE_assign_stock
(
tag_t stock_data_tag ,/* <I>
                      Object identifier of the stock data
                      obtained after loading the stock by
                      UF_ROUTE_load_stock_data( ).
                      */
tag_t anchor_tag ,/* <I>
                  Object identifier of the stock anchor
                  obtained after loading the stock.
                  */
tag_t cross_tag ,/* <I>
                 Object Identifier of the cross section tag
                 obtained after loading stock.
                 */
int seg_count ,/* <I>
               Number of segments to assign this stock.
               */
tag_t * segments  /* <I,len:seg_count>
                  Array of segments tags to assign stock.
                  */
);


/**********************************************************************
Removes the stock from the given segments. The segments need not
belong to the same path. An update of routing objects is performed
after removal of the stock by this routine.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_remove_stock
(
int num_segs ,/* <I>
              Number of segment objects.
              */
tag_t * segments  /* <I,len:num_segs>
                  An array of segment objects.
                  */
);

/**********************************************************************
Allows stock style to be assigned to the stock of segments.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 **********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_stock_style
(
int new_style ,/* <I>
               New setting for the stock style. May be set
               to:
               UF_ROUTE_STYLE_NONE,
               UF_ROUTE_STYLE_SIMPLE,
               UF_ROUTE_STYLE_DETAIL
               */
int num_stocks ,/* <I>
                Number of stock objects
                */
tag_t * stock_tags  /* <I,len:num_stocks>
                    Array of stock tags for which style has to
                    be modified.
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
Returns the units associated with the supplied stock. Routing
allows stock of a particular unit, e.g., millimeters, to be assigned to
the segments of a part of different units, e.g., inches.
 Routing stock created prior to V14.0.1 does not have
the units information and any such stock returns 0 as its units value.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_units
(
tag_t stock_tag ,/* <I>
                 Tag of stock object to query
                 */
int * units  /* <O>
             Units of the stock. This value will be either:
             UF_METRIC, UF_ENGLISH, or 0
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
Returns the Stock Data object of the Stock. This function can be used
to retrieve all the characteristics related to a Stock object. Use
UF_ROUTE_ask_characteristics on the Stock object followed by
UF_ROUTE_ask_characteristics on the Stock Data object to read all
the specific as well as the common characteristics of a Stock.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_stock_data
(
tag_t stock ,/* <I>
             Object identifier of the Stock.
             */
tag_t * stock_data  /* <O>
                    Stock Data object of the Stock.
                    */
);

/**********************************************************************
Returns the two end ports of the Stock.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_ports
(
tag_t stock ,/* <I>
             Object identifier of the Stock.
             */
tag_t  ports[2]  /* <O>
                 Two end ports of the Stock.
                 */
);

/**********************************************************************
Returns the number and tags of the Routing segments to which the
given stock object has been assigned.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_segments
(
tag_t stock ,/* <I>
             Object identifier of the Stock.
             */
int * num_segments ,/* <O>
                    Number of segments for which this Stock
                    is applied.
                    */
tag_t **segments  /* <OF,len:num_segments>
                  Array of segments to which this Stock
                  applies. Use UF_free to free this
                  allocated array.
                  */
);

/**********************************************************************
Returns the feature which represents the stock object.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_feature
(
tag_t stock_tag ,/* <I>
                 Tag of stock object
                 */
tag_t * feature  /* <O>
                 Tag of feature
                 */
);

/**********************************************************************
Returns the solid body which represents the stock object.  There may
be no stock object (NULL_TAG) if the stock style is assigned as
simple.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_body
(
tag_t stock_tag ,/* <I>
                 Tag of stock object to query
                 */
tag_t * body  /* <O>
              Tag of body representing stock object.  May be
              NULL_TAG.
              */
);

/**********************************************************************
Returns the stock style assigned to the stock object.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_style
(
tag_t stock_tag ,/* <I>
                 Tag of stock object to query.
                 */
int * style  /* <O>
             Stock style:
             UF_ROUTE_STYLE_NONE
             UF_ROUTE_STYLE_SOLID
             UF_ROUTE_STYLE_DETAIL
             */
);

/**********************************************************************
Inquires the current cross section object being referenced from the
stock data, which is being used to determine the swept body of the
stock.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_cross_sect
(
tag_t stock_tag ,/* <I>
                 Tag of stock object
                 */
tag_t * cross_section  /* <O>
                       Tag of cross section object being used by the stock.
                       NULL_TAG if no cross section is being used.
                       */
);

/**********************************************************************
Returns the current anchor being used by the stock object.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_anchor
(
tag_t stock_tag ,/* <I>
                 Tag of stock to query
                 */
tag_t * anchor  /* <O>
                Tag of anchor object
                */
);

/**********************************************************************
Sets the stock style of the given stock objects.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
**********************************************************************/
extern UFUNEXPORT int UF_ROUTE_assign_stock_style
(
int new_style ,/* <I>
               Style to assign
               */
int num_stocks ,/* <I>
                Count of stock objects being passed in
                */
tag_p_t stock_tags  /* <I,len:num_stocks>
                    Array of stock objects
                    */
);

/**********************************************************************
Computes the length of the stock object.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_compute_stock_length
(
tag_t stock ,/* <I>
             Tag of stock object
             */
double * total_path_length  /* <O>
                            Length of stock
                            */
);

/**********************************************************************
Inquires the current rotation of the stock object.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_rotation
(
tag_t stock_tag ,/* <I>
                 Tag of stock to query
                 */
double * rotation  /* <O>
                   Stock rotation (radians)
                   */
);

/**********************************************************************
Inquire which end of the stock the profile curves are placed to create
the stock feature. The index is 0 or 1 as would be returned by
UF_ROUTE_ask_stock_ports.

Environment: Internal  and  External

See Also:  UF_ROUTE_ask_stock_ports

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_profile_port
(
tag_t stock_tag ,/* <I>
                 Tag of stock to query
                 */
int * profile_port  /* <O>
                    Index of stock port at which the profile curves are
                    placed: 0 or 1.
                    */
);

/**********************************************************************
Tests whether two stock objects are equivalent.  Two stock objects are
equivalent if they reference the same stock data, the same anchor, and
all characteristic values are equal.

Return:
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
Find all the possible ways to position a routing part using
the given placement object. The initial call to this
routine should have num_places==0 and places == NULL. This
routine can then be called multiple times (with different placement
objects) to generate additional solutions.

Environment: Internal  and  External

See Also:

History:
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_solve_places
(
tag_t                         placer,    /* <I>
                                         Tag of the "placement" object.
                                         Should be a RCP, arc or circular edge,
                                         line, port, or another Routing
                                         part occurrence.
                                         */
tag_t                         part_occ,  /* <I>
                                         Part occurrence to solve
                                         */
int                          *num_places,/* <O>
                                         Updated with new number of
                                         placements found
                                         */
UF_ROUTE_place_solution_p_t **places     /* <OF,len:num_places,free:UF_ROUTE_free_places>
                                         Function_to_free = UF_ROUTE_free_places
                                         Additional solutions appended to
                                         current list (Initial call should
                                         have places == NULL).
                                         The "places" structure should
                                         be freed with UF_ROUTE_free_places
                                         */
);
/**********************************************************************
This routine returns the origin and CSYS matrix data
associated with a Routing "placement" solution returned by
UF_ROUTE_solve_places.

First use UF_ROUTE_solve_places to get solutions, then call this
routine to obtain the origin and csys arrays that should be
applied to the part instance with UF_ASSEM_reposition_instance.

Environment: Internal  and  External
See Also:
History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_places_transform
(
UF_ROUTE_place_solution_p_t places, /* <I>
                                    UF_ROUTE_place_solution_p_t pointer
                                    returned by UF_ROUTE_solve_places
                                    */
double origin[3],                   /* <O>
                                    Origin data for
                                    UF_ASSEM_reposition_instance
                                    */
double csys_matrix[6]               /* <O>
                                    CSYS   data for
                                    UF_ASSEM_reposition_instance
                                    */
);
/**********************************************************************
This routine should be used to free the data returned by the
UF_ROUTE_solve_places routine.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_free_places
(
int                     num_places, /* <I>
                                    number of "places" entries
                                    */
UF_ROUTE_place_solution_p_t *places /* <I,len:num_places>
                                    array of placement objects
                                    */
);
/**********************************************************************
This function "sets" the given part occurrence into the routing. This
routine determines which Segments the part occurrence lies upon and
matches any Ports from the part to these Segments. The Segments are
subdivided at these points and any stock along the Segments is
connected to the Ports of the part. The part should be placed at the
proper position and orientation using UF_ASSEM calls.

Environment: Internal  and  External

See Also:


History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_part_in_stock
(
tag_t occ  /* <I>
           Occurrence id of the part in the current
           work part.
           */
);

/**********************************************************************
Loads the given part, or part family member if member name is not
NULL, into the current session. The part is loaded but NOT made the
current work part. The returned part tag may subsequently be used by
the Assembly functions to add this part as a component to the
assembly for later "placement" within the routing.

Environment: Internal  and  External

See Also:  UF_ROUTE_set_part_in_stock


History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_load_part_by_name
(
char * part_name ,/* <I>
                  Name of the part to load. This may be the name
                  of a simple part file or the name of a Part
                  Family part.
                  */
char * member_name ,/* <I>
                    Part Family member name if the part specified
                    by part_name is a Part Family, else NULL.
                    */
tag_t *  part  /* <O>
               Part tag of the loaded part or NULL_TAG if it
               was not loaded.
               */
);

/**********************************************************************
Returns True if the given part occurrence is a part occurrence of a
Routing part. A part is considered a Routing part if a Routing object,
for example, an RCP, or Port, or Segment, etc., exists in the part.

Return:
         Return code:
         True = The object is a routing part occ that
         contains one or more routing objects.
         False = The object occurrence is not a routing
         part.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_is_part_occ_route_part
(
tag_t  obj_id  /* <I>
               Object identifier of the routing part occurrence
               object.
               */
);/* <NEC> */

/**********************************************************************
Returns all the cross section objects associated with a stock data
object.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_data_cross
(
tag_t stock_data_tag ,/* <I>
                      Tag of stock data object to query.
                      */
int * num_cross_sections ,/* <O>
                          Count of cross sections returned.
                          */
tag_t ** cross_sections  /* <OF,len:num_cross_sections>
                         Array of cross section objects. Use UF_free to
                         deallocate memory when no longer required.
                         */
);

/**********************************************************************
Returns the anchors which are associated with a particular stock data.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_data_anchors
(
tag_t stock_data_tag ,/* <I>
                      Tag of stock data object
                      */
int * num_anchors ,/* <O>
                   Count of anchors returned.
                   */
tag_t **anchors  /* <OF,len:num_anchors>
                 Array of anchors. Use UF_free to deallocate
                 memory when no longer required.
                 */
);

/**********************************************************************
Returns all the stock objects referencing the given stock data object.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_data_stock
(
tag_t stock_data_tag ,/* <I>
                      Tag of stock data object to query.
                      */
int * num_stock ,/* <O>
                 Count of stock objects returned.
                 */
tag_t ** stock  /* <OF,len:num_stock>
                Array of stock objects. Use UF_free to deallocate
                memory when no longer required.
                */
);

/* User Preferences */

/**********************************************************************
Fills in an array of preference structures. The key and type fields must
be set in each structure and the function returns the value for each
preference. If the preference is not found, the key value is set to
UF_ROUTE_USER_PREF_TYPE_ANY and the integer value set to 0.

Environment: Internal  and  External

See Also:  UF_ROUTE_set_user_preferences

History :Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_user_preferences
(
int n_pref ,/* <I>
            Number of preferences to query.
            */
UF_ROUTE_user_preference_t * prefs  /* <OF,len:n_pref,free:UF_ROUTE_free_user_prefs_data>
                                    Array of preference structures. The key
                                    and type fields must be set in each
                                    structure for the query.
                                    UF_ROUTE_free_user_prefs_data must be
                                    called to free the data allocated inside
                                    of the prefs array after this function call.
                                    */
);

/**********************************************************************
Sets the values of the user preferences.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_user_preferences
(
int n_prefs ,/* <I>
             Number of preferences to modify/add.
             */
UF_ROUTE_user_preference_p_t  prefs  /* <I/O,len:n_prefs>
                                     Array of preference structures.
                                     */
);

/**********************************************************************
Frees all data associated with a user preferences query.

Environment: Internal  and  External

See Also:

History:Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_free_user_prefs_data
(
int n_prefs ,/* <I>
             Number of preferences in data
             */
UF_ROUTE_user_preference_p_t prefs  /* <I,len:n_prefs>
                                    User preference data to free.
                                    */
);


/**********************************************************************
 * Query the terminal and virtual ports of the given multiport.
 *
 * Environment: Internal and External
 *
 * See Also:
 *
 * History: Originally released in V16.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_multiport_terminals
(
tag_t multi,        /* <I>
                    Multiport to query
                    */
int *num_terms,     /* <O>
                    Number of terminal ports
                    */
tag_t **terms,      /* <OF,len:num_terms>
                    Array of terminal port tags.  This must be freed
                    by calling UF_free.
                    */
int *num_virts,     /* <O>
                    Number of virtual ports
                    */
const char ***virts /* <OF,len:num_virts>
                    Array of virtual port identifiers.  This array
                    must be freed by calling UF_free.
                    */
);

/**********************************************************************
Modifies the stock object rotation about the segment to point in the
direction of the given vector.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_align_stock
(
tag_t stock ,/* <I>
             Stock object to modify
             */
double rotate_vec[3]  /* <I>
                      New vector for rotation
                      */
);

/**********************************************************************
Determines the Routing type of the given part. The type returned will
be one of:
    UF_ROUTE_PART_TYPE_PART
    UF_ROUTE_PART_TYPE_STOCK
    UF_ROUTE_PART_TYPE_FABRICATION,
or  UF_ROUTE_PART_TYPE_UNKNOWN if the part is not a
Routing part or if the part is not loaded.

Environment: Internal  and  External

See Also: UF_ROUTE_is_part_fabrication

History: Original release was in V14.0.
**********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_part_part_type
(
tag_t r_part ,/* <I>
              The tag of part or part occurrence to be inquired.
              */
int *type  /* <O>
          The type of Routing part
          */
);

/**********************************************************************
Determines if the given part is a Routing fabrication part.

Environment: Internal  and  External

See Also:  UF_ROUTE_ask_part_part_type

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_is_part_fabrication
(
tag_t fab_part ,/* <I>
                The tag of part or part occurrence to be inquired.
                */
logical *fab  /* <O>
             Logical set to TRUE if the part is a Routing
             fabrication part and FALSE otherwise.
             */
);

/**********************************************************************
Creates a Routing Cross Section object

A Cross Section object defines the set of "profile" curves that
are swept along a Routing path to represent the "stock", i.e.,
pipe, wire, tube, etc. These curves should be defined to be
in the XY plane, centered about the origin. A copy of the curves
is transformed to the start of the set of segments for a stock
and then swept along the segments to model the stock.

Environment: Internal  and  External

See Also:

History: Original release was in V18.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_cross_section
(
    tag_t  object_in_part,  /* <I>
                            Tag of an existing object which defines which
                            part the cross section will be created in
                            */
    int    style,           /* <I>
                            Routing stock style - one of
                                UF_ROUTE_STYLE_SIMPLE
                                UF_ROUTE_STYLE_DETAIL
                            */
    tag_t exprs[],           /* <I,len:2>
                            Tags of 2 expressions which define the offsets
                            to be applied to the curves when sweeping the
                            curves along the path. Positive offset is "away"
                            from the origin. Negative offset is "toward"
                            the origin.
                            */
    int    num_curves,      /* <I>
                            The number of curves in the "profile" or
                            "cross section"
                            */
    tag_t curves[],          /* <I,len:num_curves>
                            Tags of the curves
                            */
    tag_t *cross            /* <O>
                            Tag of the created cross section object
                            */
);

/**********************************************************************
Creates a Round Routing Cross Section object

This is a simplified version of the UF_ROUTE_create_cross_section routine
which will create a cross section consisting of a single curve (a circle
of the specified diameter).

Environment: Internal  and  External

See Also:

History: Original release was in V18.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_round_cross_section
(
    tag_t  object_in_part,  /* <I>
                            Tag of an existing object which defines which
                            part the cross section will be created in
                            */
    int    style,           /* <I>
                            Routing stock style - one of
                                UF_ROUTE_STYLE_SIMPLE
                                UF_ROUTE_STYLE_DETAIL
                            */
    double diameter,        /* <I>
                            The diameter of the circle created
                            */
    char  *offsets[2],      /* <I>
                            Array of 2 strings which define the offsets
                            to be applied to the curves when sweeping the
                            curves along the path. Positive offset is "away"
                            from the origin. Negative offset is "toward"
                            the origin. Example, ".25" or "-.35". These are
                            used to create expressions and as such may be
                            any string that is valid for the right hand side
                            of an expression, e.g., "radius * ( 3 / 16 )".
                            */
    tag_t *cross            /* <O>
                            Tag of the created cross section object
                            */
);

/**********************************************************************
Inquire the curves associated with a cross section.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_cross_curves
(
tag_t cross_tag ,/* <I>
                 Cross section object to query.
                 */
int * num_curves ,/* <O>
                  Number of curves in the cross section.
                  */
tag_t ** curves  /* <OF,len:num_curves>
                 Array of cross section curves. Use UF_free to
                 deallocate memory when no longer required.
                 */
);

/**********************************************************************
Returns the stock style for the specified cross section.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_cross_style
(
tag_t cross_tag ,/* <I>
                 Cross section object to query
                 */
int * style  /* <O>
             Style this cross section is associated with:
             UF_ROUTE_STYLE_SIMPLE
             UF_ROUTE_STYLE_DETAIL
             */
);

/**********************************************************************
Returns the cross section offset values.  These are the values used to
thicken the cross section about the cross section curves.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_cross_offsets
(
tag_t cross_tag ,/* <I>
                 Tag of cross section to query.
                 */
double offsets[2]  /* <O>
                   Cross section offset values.
                   */
);

/**********************************************************************
Returns all stock data objects referencing the given cross section
object.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_cross_stock_data
(
tag_t cross_tag ,/* <I>
                 Cross section object to query
                 */
int * num_stock_data ,/* <O>
                      Number of stock data objects
                      */
tag_t ** stock_data_tags  /* <OF,len:num_stock_data>
                          Array of stock data objects. Use UF_free to
                          deallocate memory when no longer required.
                          */
);

/*************************************************************************
Sets the tag of a search path.

Environment: Internal  and  External

See Also:  UF_DIRPATH_create_from_env
           UF_DIRPATH_create_from_dirs
           UF_DIRPATH_append
           UF_DIRPATH_append_from_dirs
           UF_DIRPATH_append_from_env

History: Original release was in V15.0.
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_part_search_path
(
tag_t dirpath  /* <I>
               tag of search path
               */
);

/***********************************************************************
Retrieves the tag of a search path.

Environment: Internal  and  External

See Also:  UF_DIRPATH_ask_dirs
           UF_DIRPATH_ask_dir_count
           UF_DIRPATH_ask_dir_index
           UF_DIRPATH_ask_nth_dir
           UF_DIRPATH_ask_prev_dir
           UF_DIRPATH_ask_curr_dir
           UF_DIRPATH_ask_next_dir

History: Original release was in V15.0.
 **********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_part_search_path
(
tag_t * path  /* <O>
              tag of search path or NULL_tag
              */
);

/************************************************************************
Finds the part described by the base name using the path appropriate
to the current path. When using interactive Routing, the path is
set based on the application view.

Environment: Internal  and  External

See Also:  UF_ROUTE_set_part_search_path
           UF_ROUTE_ask_part_search_path

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_find_part_in_path
(
char * part_name ,/* <I>
                  Base name of part to find
                  */
char ** path  /* <OF>
              Fully qualified name of part file.  This must be freed
              by calling UF_free.
              */
);

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
/**********************************************************************
Ask the if port is connected.

Environment: Internal  and  External

See Also:

History:
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_is_port_connected
(
tag_t port_tag,        /* <I>
                       Tag of the port examined.
                       */
logical  *is_connected /* <O>
                       true if connected else false
                       */
);

/**********************************************************************
Create an Isometric Drawing for the selected part

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_iso_drawing
(
tag_t part_tag /* <I>
               Tag of the part to be represented in the isometric
               drawing.
               */
);

/*****************************************************************************
Finds a path between two segments and returns an array of tags consisting
of the segments and part occurrences that make up the path.  The array of
tags returned is in order from begin to end. In order to find a correct path,
all the segments and any part occurences in between begin and end must be at
the work part level. This method will not traverse sub assemblies.
This method is used to create a path between start and end connectors.
The start and end connectors must be placed by selecting an RCP for 'Place Part'.
And that RCP must still exist for UF_ROUTE_find_path to find a path.
If the connectors are placed on a point or the RCP is removed with 'Simplify Path',
UF_ROUTE_find_path will not find a path.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_find_path
(
tag_t begin, /* <I>
             The tag of the segment at the beginning of the path
             */
tag_t end, /* <I>
           The tag of the segment at the end of the path
           */
int *path_size, /* <O>
                The size of the path; the number of tags in path_data
                */
tag_t **path_data  /* <OF,len:path_size>
                   The array of tags that represent the path. Use UF_free
                   to deallocate memory when no longer needed
                   */
);

/*****************************************************************************
Return the length tolerance used in the Routing module.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_length_tolerance
(
double *tol   /* <O>
              Tolerance used for distance and length comparisons in Routing
              */
);

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

  This routine will free the memory associated with a variable length array
  of pointers to UF_ROUTE_tag_list_t structures. Returns an error code if any
  occurs, during the operation.

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_free_array_of_tag_lists
(
    int                      num_tag_lists,        /* <I>
                                                      Number of tag_lists in
                                                      the array to be freed
                                                    */
    UF_ROUTE_tag_list_p_t    *array_of_tag_lists   /* <I,len:num_tag_lists>
                                                      Array of tag_lists to
                                                      be freed
                                                    */
);

/*****************************************************************************

  Applies either Move or Copy transformations to the given objects.
  The operation is determined by the value of the operation flag.
  The transformation matrix from the input is used for transforming
  the objects. Returns an error code if any error occurs during the
  transformation operation.

  Transformation of objects that are smart has no effect.  Call UF_SO_is_so
  to determine if an object is smart.  A segment is considered smart if its
  end RCPs are smart.

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_transform_objects
(
    tag_t           *tags,           /* <I,len:num_tags>
                                        Array of object tags. In an Assembly
                                        context, the tags corresponding to each
                                        Object Occurrence to be transformed. Objects
                                        may be only of types UF_route_part_type_type
                                        or UF_route_control_point_type.
                                      */
    int             num_tags,        /* <I>
                                        The number of the above tags
                                      */
    double          transform[4][4], /* <I>
                                        The transformation matrix to use.
                                        The structure of the transform:
                                        transform[0][0],[0][1],[0][2] - X Axis Rotation vectors
                                                 [1][0],[1][1],[1][2] - Y Axis Rotation vectors
                                                 [2][0],[2][1],[2][2] - Z Axis Rotation vectors
                                        transform[0][3],[1][3],[2][3] - Translation vector
                                        transform[3][3]               - Scale
                                      */
    logical         copy_operation,  /* <I>
                                        TRUE : Copy operation
                                        FALSE: Move operation
                                      */
    tag_t           **copy_tags      /* <OF,len:num_tags>
                                        The corresponding array of
                                        copied tags. There will be a one to one
                                        correspondence between tags of objects
                                        in the input tags list and the copy_tags array.
                                        Will be NULL for a Move operation.
                                        For a Copy operation, free using UF_free.
                                      */
);

/*****************************************************************************

  Find the number of RCPs occurring in a given part. If the part tag is
  a NULL_TAG , the current work part will taken as the default.
  Returns an error code if any error occurs in the function.

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_part_num_rcps
(
    tag_t      part,          /* <I>
                                 Part tag, can be a NULL_TAG
                               */
    int        *num_part_rcps /* <O>
                                 Number of RCPs in the part
                               */
);

/*****************************************************************************

  Find the tags of all RCPs occurring in a given part. If the part tag is
  a NULL_TAG , the current work part will taken as the default.
  Returns an error code if any error occurs in the function.

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_part_rcps
(
    tag_t      part,          /* <I>
                                 Part tag, can be a NULL_TAG
                               */
    int        *num_part_rcps,/* <O>
                                 Number of RCPs in the part, 0 if there are none.
                               */
    tag_t      **part_rcps    /* <OF,len:num_part_rcps>
                                 Array of part RCP tags, NULL if there are none.
                                 Free using UF_free.
                               */
);

/*****************************************************************************

  Find the number of segments occurring in a given part. If the part tag is
  a NULL_TAG , the current work part will taken as the default.
  Returns an error code if any error occurs in the function.

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_part_num_segs
(
    tag_t      part,           /* <I>
                                  Part tag, can be a NULL_TAG
                                */
    int        *num_part_segs  /* <O>
                                  Number of segments in the part
                                */
);

/*****************************************************************************

  Find the tags of all segments occurring in a given part. If the part tag is
  a NULL_TAG , the current work part will taken as the default.
  Returns an error code if any error occurs in the function.

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_part_segs
(
    tag_t      part,          /* <I>
                                 Part tag, can be a NULL_TAG
                               */
    int        *num_part_segs,/* <O>
                                 Number of segments in the part, 0 if there are none.
                               */
    tag_t      **part_segs    /* <OF,len:num_part_segs>
                                 Array of part segment tags, NULL if there are none.
                                 Free using UF_free.
                               */
);

/*****************************************************************************

  Find all the duplicate RCPs occurring in a given part. If part tag is
  a NULL_TAG, the current work part will be searched for duplicate RCPs. An
  output flag will indicate if any duplicate RCPs were found in the part. If
  duplicate RCPs are found, the output of lists of duplicate RCPs (at each
  location) will be appropriately populated.
  Returns an error code if any error occurs in the function.

  E.g. Consider a part containing 10 unique RCPs with tags
       10, 20, 30,..., 90, 100. If 10, 20, 30 were moved such that
       10 & 60 now lie at the same location and 20 & 30 ended up
       at the same location as 70, we would have the following
       structure of the output from this function.

       found_duplicates        -   TRUE
       num_part_dup_rcp_lists  -   2
       part_dup_rcp_lists      - [ 10 60
                                   20 30 70 ]

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_part_duplicate_rcps
(
    tag_t                  part,                    /* <I>
                                                       Part tag
                                                     */
    double                 tolerance,               /* <I>
                                                       Tolerance to be used to determine
                                                       duplicates. Defaults to Internal
                                                       tolerance limits if <= 0
                                                     */
    logical                *found_duplicates,       /* <O>
                                                       Indicates if duplicate
                                                       RCPs were found
                                                     */
    int                    *num_part_dup_rcp_lists, /* <O>
                                                       Number of locations
                                                       where duplicate RCPs
                                                       were found
                                                     */
    UF_ROUTE_tag_list_p_t  **part_dup_rcp_lists     /* <OF,len:num_part_dup_rcp_lists,free:UF_ROUTE_free_array_of_tag_lists>
                                                       Function_to_free = UF_ROUTE_free_array_of_tag_lists
                                                       Lists of duplicate RCP
                                                       tags found at each of
                                                       the above locations.
                                                       Free using
                                                       UF_ROUTE_free_array_of_tag_lists.
                                                     */
);

/*****************************************************************************

  Find all the duplicate segments originating in duplicate RCPs that
  occur in a given part. This routine cannot find duplicate segments that have
  the same two end rcps. If part tag is a NULL_TAG, the current work part
  will be searched for duplicate segments.
  An output flag will indicate if any duplicate segments were found in the
  part. If duplicate segments are found, the output of lists of duplicate
  segments (at each location) will be appropriately populated.
  Returns an error code if any error occurs in the function.

  E.g. Consider a part containing 10 unique segments with tags
       10, 20, 30,..., 90, 100. If 10, 20, 30 were moved such that
       10 & 60 now lie at the same location and 20 & 30 ended up
       at the same location as 70, we would have the following
       structure of the output from this function.

       found_duplicates        -   TRUE
       num_part_dup_seg_lists  -   2
       part_dup_seg_lists      - [ 10 60
                                   20 30 70 ]

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_part_duplicate_segs
(
    tag_t                  part,                    /* <I>
                                                       Part tag
                                                     */
    double                 tolerance,               /* <I>
                                                       Tolerance to be used to determine
                                                       duplicates. Defaults to Internal
                                                       tolerance limits if <= 0
                                                     */
    logical                *found_duplicates,       /* <O>
                                                       Indicates if duplicate
                                                       segments were found
                                                     */
    int                    *num_part_dup_seg_lists, /* <O>
                                                       Number of locations
                                                       where duplicate
                                                       segments were found
                                                     */
    UF_ROUTE_tag_list_p_t  **part_dup_seg_lists     /* <OF,len:num_part_dup_seg_lists,free:UF_ROUTE_free_array_of_tag_lists>
                                                       Function_to_free = UF_ROUTE_free_array_of_tag_lists
                                                       Lists of duplicate
                                                       segment tags
                                                       found at each of
                                                       the above locations.
                                                       Free using
                                                       UF_ROUTE_free_array_of_tag_lists.
                                                     */
);

/*****************************************************************************

  Function to merge duplicate RCPs occurring at the same location.
  The function will attempt to merge the coincident RCPs according to
  Merge Rules. It will output the count and tags of RCPs remaining after the
  merging. Any of the input objects that are not RCPs will be added to
  the set of remaining objects.
  All mergeable RCPs will be merged to the highest priority RCP determined
  according to the merge rules - unless a preferred RCP is explicitly specified.
  The function will not check to make sure that the RCPs to be merged lie at
  the same location - it is the caller's responsibility to ensure that!. After
  merging, the input list of RCP tags may contain tags of objects that no longer
  exist - caller should free that list immediately after this function returns.
  Returns a non-zero error code if any occurs, during the operation.
  Note : Caller should perform a Model Update using UF_MODL_update() after
         merging a set of RCPs to ensure data model consistency.

  MERGE RULES
  -----------
  # The  term  Merging refers to the transfer of all dependencies (links) from one
  object to another and the subsequent deletion of the obsoleted object.
  # RCPs to be merged will be prioritized according to their derive methods and have
  priority values defined as below
    o Port                 (4)  - i.e. derived from a port occurrence
    o Point                (3)  - i.e. derived from smart points
    o RCP                  (2)  - i.e. derived from an existing RCP
    o Absolute             (1) - i.e. derived from absolute coordinates
  # A Port RCP will have the highest priority and the Absolute derive method will
  have the least.
  # All duplicate RCPs occurring at a given location will be merged with the
  highest priority RCP among them.
  # Bend, Miter and Cope Corner RCPs cannot be merged together or with any other RCP type.
  # Bend segment RCPs cannot be merged together or with any other RCP type.

   ------------------------------------------------------------------------------
  |              | PORT          | POINT         | RCP           | ABSOLUTE      |
  |------------------------------------------------------------------------------
  |  PORT        | o Merge       | o Merge       | o Merge       | o Merge       |
  |              | o Retain Port | o Retain Port | o Retain Port | o Retain Port |
  |------------------------------------------------------------------------------|
  |  POINT       | o Merge       | o Merge       | o Merge       | o Merge       |
  |              | o Retain Port | o Retain Point| o Retain Point| o Retain Point|
  |------------------------------------------------------------------------------|
  |  RCP         | o Merge       | o Merge       | o Merge       | o Merge       |
  |              | o Retain Port | o Retain Point| o Retain RCP  | o Retain RCP  |
  |------------------------------------------------------------------------------|
  |  ABSOLUTE    | o Merge       | o Merge       | o Merge       | o Merge       |
  |              | o Retain Port | o Retain Point| o Retain RCP  | o Retain Abs. |
   ------------------------------------------------------------------------------|

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_merge_rcps
(
    int        num_rcps,            /* <I>
                                       Length of the array of
                                       coincident RCPs to be merged.
                                     */
    tag_t      *rcps,               /* <I,len:num_rcps>
                                       Array of coincident RCP tags to
                                       be merged. Should be Prototype tags.
                                     */
    tag_t      preferred_rcp,       /* <I>
                                       If specified, all RCPs will be merged to
                                       this RCP. If a NULL_TAG, the routine will
                                       determine what gets retained according
                                       to its merge rules. No merge will occur
                                       if this object is not an RCP.
                                     */
    int        *num_remaining,      /* <O>
                                       Number of RCPs remaining
                                     */
    tag_t      **remaining          /* <OF,len:num_remaining>
                                       RCPs remaining after merge operations,
                                       including those that couldn't be merged
                                       Free using UF_free
                                     */
);

/*****************************************************************************

  Ask all built-in paths in a routing part

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_built_in_paths
(
         tag_t part,      /*<I>
                           Tag of part to be queried
                          */
         int *num_paths,  /*<O>
                           Number of built-in paths
                          */
         tag_t **paths,   /*<OF,len:num_paths>
                          Array of built-in path tags
                          Free this array using UF_free
                          */
         char ***bip_names /* <OF,len:num_paths>
                             Array of built-in path names
                             Free this array using UF_free_string_array
                           */
);

/*****************************************************************************

  Ask built-in path curves

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_built_in_path_objs
(
     tag_t bip,      /*<I>
                      Tag of built-in path object
                     */
     int *num_objs,  /*<O>
                      Number of curves in path
                     */
     tag_t **objects /*<OF,len:num_objs>
                      Array of curve tags
                      Free this array using UF_free
                     */
) ;

/*****************************************************************************

  Create a new built-in path in a routing part.

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/

extern UFUNEXPORT int UF_ROUTE_create_built_in_path
(
     tag_t part,      /*<I>
                      Tag of part containing curves. When a NULL_TAG is passed,
                      built-in path will be created in current work part
                      */
     int num_objs,   /*<I>
                       Number of curves in path
                     */
     tag_t *objs,   /*<I,len:num_objs>
                     Array of curve tags
                     */

     char *name,    /* <I>
                      Built-in path name. This can be NULL.
                     */

     tag_t *bip_tag   /* <O>
                        Tag of built-in path created
                      */
);

/*****************************************************************************

  Modify the curves in a built-in path

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_built_in_path_objs
(
     tag_t bip,      /*<I>
                       Tag of built-in path
                     */
     int num_objs,   /*<I>
                      Number of built-in path curves
                     */
     tag_t *objs      /*<I,len:num_objs>
                      Array of curve tags
                      */
);

/**********************************************************************

Ask the tags of the wires that are associated with the given segment.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_wires
(
    tag_t    segment,        /* <I> , the segment to query*/
    int     *num_wires,      /* <O> , the number of wires*/
    tag_t  **wires           /* <OF,len:num_wires> ,
                                the array of wires, free with UF_free.*/
);

/**********************************************************************

Ask the tags of the wires associated with the given stock.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_wires
(
    tag_t   stock,            /* <I> , the stock to query*/
    int    *num_wires,        /* <O> , the number of wires*/
    tag_t **wires             /* <OF,len:num_wires>,
                                 the array of wires, free with UF_free*/
);

/**********************************************************************

Ask the tags of the components in the given harness.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_harness_comps
(
    tag_t  harness,         /* <I> , the harness to query*/
    int   *num_comps,       /* <O> , the number of components*/
    tag_t **comps           /* <OF,len:num_comps>,
                                the array of component tags, free with UF_free*/
);

/**********************************************************************

Ask the wires in the given harness.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_harness_wires
(
    tag_t  harness,          /* <I> , the harness to query*/
    int   *num_wires,        /* <O> , the number of wires*/
    tag_t **wires            /* <OF,len:num_wires>,
                                the array of wire tags, free with UF_free.*/
);

/**********************************************************************

Ask the harnesses associated with a wire.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_wire_harness
(
    tag_t    wire,             /* <I> , the wire to query*/
    int     *num_harness,      /* <O> , the number of harnesses*/
    tag_t  **harness           /* <OF,len:num_harness>,
                                  the array of harnesses, free with UF_free.*/
);
/**********************************************************************

Ask the stock tags associated with the wire.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_wire_stock
(
    tag_t    wire,            /* <I> , the wire to query*/
    int     *num_stock,       /* <O> , the number of stock tags*/
    tag_t  **stock            /* <OF,len:num_stock>,
                                 the array of stock tags, free with UF_free. */
);

/**********************************************************************

Ask the segments in the given wire.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_wire_segments
(
    tag_t    wire,             /* <I> , the wire to query*/
    int     *num_segments,     /* <O> , the number of segments*/
    tag_t  **segments          /* <OF,len:num_segments>,
                                  the array of segments, free array with UF_free */
);

/**********************************************************************

Ask the harness associated with the stock tag.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_harness
(
    tag_t stock,        /* <I> , the stock tag to query*/
    int *num_harness,   /* <O> , the number of harnesses*/
    tag_t **harness     /* <OF,len:num_harness>,
                           the array of harness tags, free array with UF_free.*/
);

/**********************************************************************

Ask a passed segment if it is a terminal segment.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_is_terminal_segment
(
    tag_t segment,    /* <I> , the segment to query*/
    logical * is_term /* <O> , true if it is terminal*/
);

/**********************************************************************

Inquire as to the ROUTE_route object(s) associated with the
specified Segment. (An empty list can be returned,
indicating that no Routes had been assigned to the Segment.)

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_routes
(
        tag_t   segment,        /* <I>  , segment to query*/
        int     *num_routes,    /* <O>  , the number of routes*/
        tag_t   **routes        /* <OF,len:num_routes> ,
                                    the array of routes,
                                    use UF_free to free up the array*/
);

/**********************************************************************

Ask the paths that the segment belongs to.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_paths
(
    tag_t        segment,            /* <I> , the segment to query */
    int          *number_of_paths,   /* <O> , the number of paths*/
    tag_p_t      *paths              /* <OF,len:number_of_paths>,
                                        the array of paths */
);

/**********************************************************************

Given a set of segments, this function
determines if they comprise a single unique
path object.  For this to be the case, there
must be a 1 to 1 mapping between the segments
passed in and the segments in the path.

Each segment will be asked its path.  If any of
the segments don't belong to a path, the
segments cannot be an offset path object.  The
offset path object that is common to all of the
segments is then checked to determine if the
number of segments passed in and the number of
segments in the path match.  If they do not,
the set of segments is not a path.  Only in the
case that all the segments belong to a common
offset path object and the number of segments
match is the set of segments that path object.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segments_is_path
(
    int     number_of_segments,           /* <I>, the number of segs to eval  */
    tag_t   *segments,                    /* <I,len:number_of_segments>,
                                             the array of segs to eval*/
    tag_t   path,                         /* <I>, the path tag */
    logical *is_path                      /* <O>, true if the segments are a path */
);

/**********************************************************************

Given a set of segments, this function
finds the path objects that are defined entirely using the given
set of segments.

Eg: Multiple Master path objects may be defined using the same
set of segments, but with different creation options. In this case
this routine may be used to make sure we are not duplicating
master paths at the time of creation.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segments_paths
(
    int     num_segments,           /* <I> , the number of segs  in this path*/
    tag_t   *segments,              /* <I,len:num_segments> ,
                                        the array of segments*/
    int     *num_paths,             /* <O> , the number of paths for these segs*/
    tag_t   **paths,                /* <OF,len:num_paths>,
                                        the array of paths,
                                        use UF_free to free up the array. */
    logical *share_path             /* <O> , true if all segs share at least one path*/
);

/**********************************************************************

Ask the passed segment its branch angle attribute.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_branch_angle
(
    tag_t   segment,        /* <I>, the segment to query */
    double  *branch_angle   /* <O>, the branch angle. */ );


/**********************************************************************

Asks end object of route.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int  UF_ROUTE_ask_route_end
(
   tag_t route, /* <I>, the route to query */
   tag_t *end   /* <O>, the end object */
);

/**********************************************************************

Asks route objects of an existing route.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int  UF_ROUTE_ask_route_objs
(
   tag_t route,     /* <I> , the route to query*/
   int *num_objs,   /* <O> , the number objects that make up the route*/
   tag_t **objs     /* <OF,len:num_objs>, the array of objects in the route.
                             Use UF_free to free up returned array.*/
);

/**********************************************************************

Asks start object of route.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int  UF_ROUTE_ask_route_start
(
   tag_t route, /* <I> , the route to query*/
   tag_t *start /* <O> , the start object*/
);


/**********************************************************************

Returns true if the given wire traverses through the given segment.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_is_wire_on_segment
(
   tag_t wire,                   /* <I>  , wire */
   tag_t segment,                /* <I>  , seg */
   logical *on_seg               /* <O>  , true if wire traverses segment */
);

/**********************************************************************

Ask any stock on a given segment that belongs to specified wire harness.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_bundle_stock
(
    tag_t segment, /* <I> the segment  to query*/
    tag_t harness, /* <I> the harness to query*/
    tag_t *stock   /* <O> the stock tag*/ );

/**********************************************************************
 * Function Name: UF_ROUTE_is_stock_interior
 *
 * Function Description: This function queries a stock to see if it is
 *     "inside" any part in the current assembly.  The stock is only
 *     interior if it's segment(s) are interior to a part.
 *
 * Environment: Internal and External
 *
 * See Also:
 *
 * History: Released in V20
 *
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_is_stock_interior
(
   tag_t stock,          /* <I> the tag of the stock to query */
   logical  *is_interior /* <O> TRUE if interior, else FALSE */ );

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

/*****************************************************************************

This function is used to get the part occurrence tag associated with a
piece of stock.

Environment: Internal and External

See Also:

History: Released in V19.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_part_occ
(
    tag_t   stock,              /* <I>  Tag of the stock object. */
    tag_t*  stock_component     /* <O>  Tag of the stock component */
);

/*****************************************************************************

This function is used to convert the work part from a old-style stock part
(stock in the work part) to a new-style stock as components part (stock
created in components).

The part specified is the part to convert, if a NULL_TAG is passed in then
the work part is converted.  The convert_subcomponents argument causes
the conversion function to be called recursively on all
subcomponents of the part being converted.  The permanent_stock argument
causes the all stock components that were created by the conversion to
have the STOCK_COMPONENT_NAME user exit applied to each one, and the
name of the stock component changed.  The reuse_stock argument causes
all stock components to have the the UF_ROUTE_reuse_stock_part call
applied to each of them.

Environment: Internal and External

See Also:

History: Released in V19.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_convert_to_stock_as_components
(
    tag_t   part,                   /* <I>  Part to convert */
    logical convert_subcomponents,  /* <I>  TRUE - convert all sub-assemblies of part,
                                            FALSE - convert only the given part  */
    logical permanent_stock,        /* <I>  TRUE - call STOCK_COMPONENT_NAME plugin on each stock
                                            FALSE - only call STOCK_COMPONENT_TEMP_NAME plugin */
    logical reuse_stock             /* <I>  TRUE - call STOCK_COMPONENT_LOOKUP plugin on each stock,
                                            FALSE - dont attempt to reuse stocks */
);

/******************************************************************************
*  UF_ROUTE_is_segment
*
*  DESCRIPTION:
*       Used to determine if a NX entity is a routing segment.
*
* Environment: Internal and External
*
* See Also:
*
* History: Released in V20
*
*/
extern UFUNEXPORT int UF_ROUTE_is_segment
(
    tag_t   object,         /* <I> entity to check */
    logical *is_segment     /* <O> Is entity a routing segment? */
);

/******************************************************************************
* UF_ROUTE_get_next_connections
*
* DESCRIPTION:
*   Determine next set of connected objects to traverse from a given rcp or
*   port occurrence (curr_conn), excluding objects based on current part
*   occurrence or segment (curr_obj).
*
* Environment: Internal and External
*
* See Also:
*
* History: Released in NX
*
******************************************************************************/
extern UFUNEXPORT int UF_ROUTE_get_next_connections
(
    tag_t       curr_conn,      /* <I> object to traverse (rcp or port occurrence) */
    tag_t       curr_obj,       /* <I> part occurrence, or segment to exclude in traversal
                                 *     (may be NULL_TAG).  This is the object traversed in
                                 *     order to get to the current traversal object.
                                 */
    int         *num_conns,     /* <O> number of connected objects */
    tag_t       **next_conns,   /* <OF,len:num_conns> array of connected objects.
                                 *      Will NOT contain any NULL_TAGs.   Use UF_free() to free.
                                 */
    tag_t       **next_objs     /* <OF,len:num_conns> array of segments or part occurrences.  Can have NULL_TAGs.
                                 *      These are the objects to traverse in order to get to the
                                 *      next set of connections.  Use UF_free() to free.
                                 */
);

/******************************************************************************
*  UF_ROUTE_stock_ask_name
*
*  DESCRIPTION:
*       Return stock name
*       Return value : 0 ==> OK, != 0 ==> Error
*
* Environment: Internal and External
*
* See Also:
*
* History: Released in NX
*
*/
extern UFUNEXPORT int UF_ROUTE_stock_ask_name
(
        tag_t   stock,         /* <I> stock tag */
        char**  name           /* <OF> Stock name */
);

#ifdef __cplusplus
}
#endif

#include <uf_retiring.h>

#undef EXPORTLIBRARY

#endif /* UF_ROUTE_H_INCLUDED */
