/*******************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
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

You can specify a routing level for stock objects and Fitting Parts
that is used to determine the connection compatibility and display
of these objects.

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

routing level - A routing level allows you to organize various fittings
and stock present in a routing assembly into groups of connectable objects.
By default all routing stock and standard parts will be created on the
default routing level. Use routing levels to create nested stock.

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

/*
 * - the charx expression parser error messages
 */
#define UF_ROUTE_CHARX_EXPR_unknown             ERROR_ROUTE_base + 165
#define UF_ROUTE_CHARX_EXPR_err_num_eq_eq       ERROR_ROUTE_base + 166
#define UF_ROUTE_CHARX_EXPR_err_num_eq_rel      ERROR_ROUTE_base + 167
#define UF_ROUTE_CHARX_EXPR_err_num_eq_none     ERROR_ROUTE_base + 168 
#define UF_ROUTE_CHARX_EXPR_err_num_eq_str      ERROR_ROUTE_base + 169
#define UF_ROUTE_CHARX_EXPR_err_num_num_eq      ERROR_ROUTE_base + 170
#define UF_ROUTE_CHARX_EXPR_err_num_num_rel     ERROR_ROUTE_base + 171
#define UF_ROUTE_CHARX_EXPR_err_num_num_num     ERROR_ROUTE_base + 172
#define UF_ROUTE_CHARX_EXPR_err_num_num_str     ERROR_ROUTE_base + 173
#define UF_ROUTE_CHARX_EXPR_err_num_range_eq    ERROR_ROUTE_base + 174
#define UF_ROUTE_CHARX_EXPR_err_num_range_rel   ERROR_ROUTE_base + 175
#define UF_ROUTE_CHARX_EXPR_err_num_range_range ERROR_ROUTE_base + 176
#define UF_ROUTE_CHARX_EXPR_err_num_range_str   ERROR_ROUTE_base + 177
#define UF_ROUTE_CHARX_EXPR_err_num_rel_eq      ERROR_ROUTE_base + 178
#define UF_ROUTE_CHARX_EXPR_err_num_rel_rel     ERROR_ROUTE_base + 179
#define UF_ROUTE_CHARX_EXPR_err_num_rel_none    ERROR_ROUTE_base + 180
#define UF_ROUTE_CHARX_EXPR_err_num_rel_range   ERROR_ROUTE_base + 181
#define UF_ROUTE_CHARX_EXPR_err_num_rel_str     ERROR_ROUTE_base + 182
#define UF_ROUTE_CHARX_EXPR_err_num_none        ERROR_ROUTE_base + 183
#define UF_ROUTE_CHARX_EXPR_err_num_str         ERROR_ROUTE_base + 184
#define UF_ROUTE_CHARX_EXPR_err_str_eq_eq       ERROR_ROUTE_base + 185
#define UF_ROUTE_CHARX_EXPR_err_str_eq_rel      ERROR_ROUTE_base + 186
#define UF_ROUTE_CHARX_EXPR_err_str_eq_none     ERROR_ROUTE_base + 187
#define UF_ROUTE_CHARX_EXPR_err_str_quote_eq    ERROR_ROUTE_base + 188
#define UF_ROUTE_CHARX_EXPR_err_str_quote_rel   ERROR_ROUTE_base + 189
#define UF_ROUTE_CHARX_EXPR_err_str_quote_quote ERROR_ROUTE_base + 190
#define UF_ROUTE_CHARX_EXPR_err_str_quote_str   ERROR_ROUTE_base + 191
#define UF_ROUTE_CHARX_EXPR_err_str_str_eq      ERROR_ROUTE_base + 192
#define UF_ROUTE_CHARX_EXPR_err_str_str_rel     ERROR_ROUTE_base + 193
#define UF_ROUTE_CHARX_EXPR_err_str_str_quote   ERROR_ROUTE_base + 194
#define UF_ROUTE_CHARX_EXPR_err_str_str_str     ERROR_ROUTE_base + 195
#define UF_ROUTE_CHARX_EXPR_err_str_none        ERROR_ROUTE_base + 196
#define UF_ROUTE_CHARX_EXPR_err_str_rel_rel     ERROR_ROUTE_base + 197

#define UF_ROUTE_err_max                        ERROR_ROUTE_base + 198

/* Error string definition section */
#define UF_ROUTE_str_invalid_route_start            \
        "%s: Invalid object specified for route start %d"
#define UF_ROUTE_str_invalid_route_end              \
        "%s: Invalid object specified for route end %d"

#define UF_ROUTE_AV_CORNERS_NONE  0
#define UF_ROUTE_AV_CORNERS_BEND  ((byte)(1<<0))
#define UF_ROUTE_AV_CORNERS_COPE  ((byte)(1<<1))
#define UF_ROUTE_AV_CORNERS_MITER ((byte)(1<<2))
#define UF_ROUTE_AV_CORNERS_SBEND ((byte)(1<<3))

#define UF_ROUTE_AV_CURVES_NONE    0
#define UF_ROUTE_AV_CURVES_LINES   ((byte)(1<<0))
#define UF_ROUTE_AV_CURVES_ARCS    ((byte)(1<<1))
#define UF_ROUTE_AV_CURVES_SPLINES ((byte)(1<<2))

#define UF_ROUTE_AV_UNITS_IN 0
#define UF_ROUTE_AV_UNITS_MM 1

#define UF_ROUTE_CHARX_TYPE_UNKNOWN     UF_EPLIB_CHARX_TYPE_UNKNOWN
#define UF_ROUTE_CHARX_TYPE_INT         UF_EPLIB_CHARX_TYPE_INT
#define UF_ROUTE_CHARX_TYPE_REAL        UF_EPLIB_CHARX_TYPE_REAL
#define UF_ROUTE_CHARX_TYPE_STR         UF_EPLIB_CHARX_TYPE_STR
#define UF_ROUTE_CHARX_TYPE_ANY         UF_EPLIB_CHARX_TYPE_ANY
#define UF_ROUTE_CHARX_TYPE_REF         UF_EPLIB_CHARX_TYPE_REF
#define UF_ROUTE_CHARX_TYPE_ANY_REF     UF_EPLIB_CHARX_TYPE_ANY_REF
#define UF_ROUTE_CHARX_TYPE_INT_EXPR    UF_EPLIB_CHARX_TYPE_INT_EXPR
#define UF_ROUTE_CHARX_TYPE_REAL_EXPR   UF_EPLIB_CHARX_TYPE_REAL_EXPR
#define UF_ROUTE_CHARX_TYPE_STR_EXPR    UF_EPLIB_CHARX_TYPE_STR_EXPR

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

#define UF_ROUTE_DR_MODE_CONCURRENT  0
#define UF_ROUTE_DR_MODE_INTERACTIVE 1
#define UF_ROUTE_DR_MODE_BATCH       2

#define UF_ROUTE_DR_REASON_UNKNOWN             -1
#define UF_ROUTE_DR_REASON_CREATE_PATH          0
#define UF_ROUTE_DR_REASON_HEAL_PATH            1
#define UF_ROUTE_DR_REASON_ASSIGN_CORNER        2
#define UF_ROUTE_DR_REASON_ASSIGN_STOCK         3
#define UF_ROUTE_DR_REASON_REMOVE_STOCK         4
#define UF_ROUTE_DR_REASON_STOCK_STYLE          5
#define UF_ROUTE_DR_REASON_PLACE_PART           6
#define UF_ROUTE_DR_REASON_CREATE_FAB           7
#define UF_ROUTE_DR_REASON_QUALIFY_PART         8
#define UF_ROUTE_DR_REASON_MOVE_PATH            9
#define UF_ROUTE_DR_REASON_COPY_PATH           10
#define UF_ROUTE_DR_REASON_DELETE_PATH         11
#define UF_ROUTE_DR_REASON_SUBDIVIDE_SEG       12
#define UF_ROUTE_DR_REASON_SIMPLIFY_PATH       13
#define UF_ROUTE_DR_REASON_REMOVE_PART         14
#define UF_ROUTE_DR_REASON_MOVE_PART           15
#define UF_ROUTE_DR_REASON_EDIT_CHARX          16
#define UF_ROUTE_DR_REASON_INTERACTIVE         17
#define UF_ROUTE_DR_REASON_BATCH               18
#define UF_ROUTE_DR_REASON_ORIENT_STOCK        19
#define UF_ROUTE_DR_REASON_UNIFY_PATH          20
#define UF_ROUTE_DR_REASON_TRANSFORM_PATH      21
#define UF_ROUTE_DR_REASON_OFFSET_PATH         22
#define UF_ROUTE_DR_REASON_AUTO_ROUTE_PIN      23
#define UF_ROUTE_DR_REASON_MANUAL_ROUTE_PIN    24
#define UF_ROUTE_DR_REASON_AUTO_ROUTE_COMP     25
#define UF_ROUTE_DR_REASON_MANUAL_ROUTE_COMP   26

#define UF_ROUTE_CB_REASON_UNKNOWN             -1
#define UF_ROUTE_CB_REASON_PLACE_PART           0
#define UF_ROUTE_CB_REASON_MOVE_PART            1
#define UF_ROUTE_CB_REASON_REMOVE_PART          2
#define UF_ROUTE_CB_REASON_MOVE_PATH            3
#define UF_ROUTE_CB_REASON_COPY_PATH            4
#define UF_ROUTE_CB_REASON_DELETE_PATH          5
#define UF_ROUTE_CB_REASON_TRANSFORM_PATH       6
#define UF_ROUTE_CB_REASON_OFFSET_PATH          7
#define UF_ROUTE_CB_REASON_ASSIGN_STOCK         8
#define UF_ROUTE_CB_REASON_WIRE_ROUTE_MANUAL    9
#define UF_ROUTE_CB_REASON_WIRE_ROUTE_AUTO      10
#define UF_ROUTE_CB_REASON_WIRE_COMP_MANUAL     11
#define UF_ROUTE_CB_REASON_WIRE_COMP_AUTO       12
#define UF_ROUTE_CB_REASON_WIRE_UNROUTE         13
#define UF_ROUTE_CB_REASON_WIRE_UNCOMP          14
#define UF_ROUTE_CB_REASON_WIRE_TERMINALS       15
#define UF_ROUTE_CB_REASON_CHOOSE_PART          16
#define UF_ROUTE_CB_REASON_CREATE_CONNECTION    17
#define UF_ROUTE_CB_REASON_EDIT_CONNECTION      18
#define UF_ROUTE_CB_REASON_UNASSIGN_STOCK       19
#define UF_ROUTE_CB_REASON_CREATE_RUN           20
#define UF_ROUTE_CB_REASON_RUN_PRE_DELETE       21
#define UF_ROUTE_CB_REASON_REPLACE_STOCK        22

#define UF_ROUTE_USER_PREF_TYPE_ANY       UF_STYLER_NO_VALUE
#define UF_ROUTE_USER_PREF_TYPE_STR       UF_STYLER_STRING_VALUE
#define UF_ROUTE_USER_PREF_TYPE_STR_ARRAY UF_STYLER_STRING_PTR_VALUE
#define UF_ROUTE_USER_PREF_TYPE_INT       UF_STYLER_INTEGER_VALUE
#define UF_ROUTE_USER_PREF_TYPE_INT_ARRAY UF_STYLER_INTEGER_PTR_VALUE
#define UF_ROUTE_USER_PREF_TYPE_DBL       UF_STYLER_REAL_VALUE
#define UF_ROUTE_USER_PREF_TYPE_DBL_ARRAY UF_STYLER_REAL_PTR_VALUE

#define UF_ROUTE_PART_FILE_NAME_STR       "PART_NAME"
#define UF_ROUTE_MEMBER_NAME_STR          "MEMBER_NAME"
#define UF_ROUTE_PART_NUMBER_STR          "PART_NUMBER"
#define UF_ROUTE_SYMBOL_NAME_STR          "SYMBOL_PART_NAME"
#define UF_ROUTE_DIAMETER_STR             "DIAMETER"
#define UF_ROUTE_WEIGHT_VALUE_STR         "WEIGHT"
#define UF_ROUTE_WEIGHT_UNITS_STR         "WEIGHT_UNITS"
#define UF_ROUTE_ANGLE_STR                "ELBOW_ANG"
#define UF_ROUTE_DESCRIPTION_STR          "DESCRIPTION"
#define UF_ROUTE_MATERIAL_STR             "MATERIAL"
#define UF_ROUTE_SCHEDULE_STR             "SCHEDULE"
#define UF_ROUTE_RATING_STR               "RATING"
#define UF_ROUTE_CLASS_STR                "CLASS"
#define UF_ROUTE_NPS_STR                  "NPS"
#define UF_ROUTE_NPS_OUT_STR              "NPS_OUT"
#define UF_ROUTE_NPS_BRANCH_STR           "NPS_BRANCH"
#define UF_ROUTE_INSLEN_STR               "INSLEN"

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

/**************************
 ** Structures and Types **
 **************************/

typedef UF_EPLIB_charx_t UF_ROUTE_charx_t, *UF_ROUTE_charx_p_t;

typedef UF_EPLIB_part_lib_part_t UF_ROUTE_part_lib_part_t,
    *UF_ROUTE_part_lib_part_p_t;

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

/* System Interface Description */
struct UF_ROUTE_system_interface_s
{
    char *name;
    char *description;
    char *parameters;
    char *bitmap;
    int   type;
    int   process_id;
};
typedef struct UF_ROUTE_system_interface_s UF_ROUTE_system_interface_t,
               *UF_ROUTE_system_interface_p_t;
/* Corner Preference Structure */
struct UF_ROUTE_corner_pref_s {
    int     type;
    logical use_bend_ratio;
    double  bend_ratio;
    double  bend_radius;
    int radius_units;
    tag_t   dir;        /* Only used for miter with one segment */
    char *bend_table_entry;
};
typedef struct UF_ROUTE_corner_pref_s UF_ROUTE_corner_pref_t,
               *UF_ROUTE_corner_pref_p_t;


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
} ;
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

typedef int (*UF_ROUTE_tcl_proc_f_t) ( void *client_data, /* <I> */
                                      void *interp, /* <I> */
                                      int argc, /* <I> */
                                      char *argv[] /* <I> */);
typedef struct ROUTE_place_solution_s *UF_ROUTE_place_solution_p_t;

typedef struct ROUTE_application_view_s UF_ROUTE_application_view_t,
*UF_ROUTE_application_view_p_t;

typedef struct ROUTE_plugin_s UF_ROUTE_plugin_t , *UF_ROUTE_plugin_p_t;


typedef struct UF_ROUTE_bend_segment_info_s
        UF_ROUTE_bend_segment_info_t, *UF_ROUTE_bend_segment_info_p_t;

struct UF_ROUTE_bend_segment_info_s{
    tag_t       stock_tag;                          /* Tag of stock */
    tag_t       segment;                            /* Segment tag */
    logical     is_straight;                        /* TRUE - segment is straight, FALSE otherwise */
    double      length;                             /* Length of segment */
    tag_t       end_rcps[2];                        /* Start and end rcps, do not use for 
                                                       S-Bends and bends greater than or 
                                                       equal to 180 degrees. */
    tag_t       bend_corner;                        /* Bend corner tag */
    double      bend_radius;                        /* Radius of the bend */
    double      bend_pos[3];                        /* Position of the bend rcp */
    double      normal[2][3];                       /* Normal of curve at start and end points */
    UF_ROUTE_bend_segment_info_p_t     previous;    /* Previous segment in list */
    UF_ROUTE_bend_segment_info_p_t     next;        /* Next segment in list */
    double      rcp_pos[2][3];                      /* Locations of RCP in ABS coordinates, use this
                                                       instead of the end_rcps for S-Bends and bends
                                                       greater than or equal to 180 degrees. */
};


/* For XYZ bend reports, the first bend value (xc[0],yc[0],zc[0]), is
at one endpoint of the stock body, and the last bend value
(xc[num_bends-1],yc[num_bends-1],zc[num_bends-1]) is the other endpoint
of the stock body.  The other bend values are the location in work
coordinates of the bend rcps associated with each bend,
or the location of where the bend rcps would be if they existed. */
typedef struct UF_ROUTE_bend_report_xyz_s {
    int     num_bends;      /* Number of bends in report */
    double  *xc;             /*<len:num_bends>X position of bend rcp in work coords */
    double  *yc;             /*<len:num_bends>Y position of bend rcp in work coords */
    double  *zc;             /*<len:num_bends>Z position of bend rcp in work coords */
    double  *radii;          /*<len:num_bends>Radius of bend */
    double  total_length;   /* Total length of stock */
} UF_ROUTE_bend_report_xyz_t,  *UF_ROUTE_bend_report_xyz_p_t;


/* For YBC bend reports,
Y       -   The value is the length along the stock
            before the bend.
B       -   The B value is the rotation angle about the Y-axis
            of the stock.
C       -   The C value is the bend angle.
Radii   -   The radius of the bend.

The last bend value (y[num_bends-1],...,radii[num_bends-1])
isn't actually a bend, the only valid value is the y value, which is the
length after the last bend.
All values are relative, meaning they are calculated from the previous bend.
So if bend1 has B value of 90 degrees, and bend2 has a B value of 90 degrees
then the pipe has rotated 180 degrees about the y axis.
*/
typedef struct UF_ROUTE_bend_report_ybc_s {
    int     num_bends;      /* Total number of bends */
    double  *y;             /* <len:num_bends>Length along y axis */
    double  *b;             /* <len:num_bends>Rotation angle (degrees) about the y axis */
    double  *c;             /* <len:num_bends>Rotation angle (degrees) about the z axis */
    double  *radii;         /* <len:num_bends>Radius of the bend */
    double  total_length;   /* Total length of the stock */
} UF_ROUTE_bend_report_ybc_t,  *UF_ROUTE_bend_report_ybc_p_t;

/* For MIL98 bend reports, the mil-d-9898  spec is followed.
All values are absolute, they are cumulative.

C       -   The distance before the bend, from the start of the cable
            to the beginning point of the bend.
F       -   The radius of the bend.
E       -   The turn angle, this is the angle about the y axis, relative
            to initial position (cumulation of the B value in YBC).
G       -   The bend angle. (The C value in YBC).
Y       -   The Y value from the YBC format.

See MIL-D-9898C for more information.
*/
typedef struct UF_ROUTE_bend_report_mil98_s {
    int     num_bends;      /* Number of bends */
    double  *c;/*<len:num_bends>*/
    double  *f;/*<len:num_bends>*/
    double  *e;/*<len:num_bends>*/
    double  *g;/*<len:num_bends>*/
    double  *y;/*<len:num_bends>*/
    double  total_length;   /* Total length of the stock */
} UF_ROUTE_bend_report_mil98_t,  *UF_ROUTE_bend_report_mil98_p_t;

/*
    The UF_ROUTE_bundle_data_s structure is the structure that is used
    to pass information to and receive information from a user written
    bundle diameter calculation routine. In Wiring, you may define
    a "Plug-in" for the routine that calculates the set of curves that
    should be used to model the cross section of the wire bundle based
    on the number of wires in the bundle (and their diameters). This
    is the structure that is supplied to your bundle diameter routine.


*/

typedef struct UF_ROUTE_bundle_data_s {
    int     num_wires;
    tag_t   *wires; /* <len:num_wires> */
    int     num_stock_data;
    tag_t  *stock_data; /* <len:num_stock_data> */
    int     num_cross_sections;
    tag_t  *cross_sections;/* <len:num_cross_sections> */
    int     num_anchors;
    tag_t  *anchors;/* <len:num_anchors> */
} UF_ROUTE_bundle_data_t, *UF_ROUTE_bundle_data_p_t;


/* The UF_ROUTE_cda_data_s is the structure that holds the data required to
   run the cable drawing automation program as a user-function utility from
   the wiring interface. This structure indicates the number of records
   selected and the selected connection list tags in the Rlist navigator
*/
typedef struct UF_ROUTE_cda_data_s {
    int num_recs;
    tag_t *recs; /* <len:num_recs> */
} UF_ROUTE_cda_data_t, *UF_ROUTE_cda_data_p_t;

/* The UF_ROUTE_iman_bom_data_s is the structure used to implement the
   Routing Team Center Engineering BOM post piping parts list callback.
   It is currently empty but may be implemented in the future. */
typedef struct UF_ROUTE_iman_bom_data_s {
    logical place_holder;
}UF_ROUTE_iman_bom_data_t, *UF_ROUTE_iman_bom_data_p_t;

/* The UF_ROUTE_pcf_gen_data_s is the structure used to implement a pcf file
   generation utility.  The Piping Component File is then used by Alias -
   Isogen to create an isometric drawing.  The structure is currently empty
   byt may be implemented in the future. */
typedef struct UF_ROUTE_pcf_gen_data_s {
    int placeholder;
} UF_ROUTE_pcf_gen_data_t, *UF_ROUTE_pcf_gen_data_p_t;

/* The following structure is used for the TEMP_STOCK_COMPONENT_NAME
    and STOCK_COMPONENT_NAME plugins determining stock component names.

    See UF_UGMGR_encode_part_filename for details on Team Center Engineering
    specific arguments ( item_revision, item_type and item_name ).
 */
struct UF_ROUTE_component_name_plugin_s
{
    /* Input:   Tag of the stock object */
    tag_t   stock;

    /* Output:  TRUE if part needs to be renamed,
                FALSE part should remain as it is. */
    logical rename_part;

    /* Output:  Path of file ("" == current directory) not used in Team Center Engineering,
                this is the path to the directory where stock components are to be
                be stored.  This may be a relative path (to the current directory),
                or an absolute path. */
    char    path_name[UF_CFI_MAX_FILE_NAME_SIZE]; /* <len:UF_CFI_MAX_FILE_NAME_SIZE> */

    /* Output:  item folder ("" == default folder), only used for Team Center Engineering,
                this is the name of the folder that the stock
                components will be placed into. */
    char    folder_name[UF_CFI_MAX_FILE_NAME_SIZE]; /* <len:UF_CFI_MAX_FILE_NAME_SIZE> */

    /* Output:  Name of file ("" == no name generated,
                default user exit will be called) */
    char    file_name[UF_CFI_MAX_FILE_NAME_SIZE]; /* <len:UF_CFI_MAX_FILE_NAME_SIZE> */

    /* Output:  item revision , only used for Team Center Engineering ("" == no revision generated,
                default user exit will be called) */
    char    item_revision[UF_UGMGR_PARTREV_SIZE+1]; /* <len:UF_UGMGR_PARTREV_SIZE+1> */

    /* Output:  item type, only used for Team Center Engineering  */
    char    item_type[UF_UGMGR_FTYPE_SIZE+1]; /* <len:UF_UGMGR_FTYPE_SIZE+1> */

    /* Output:  item name, only used for Team Center Engineering. */
    char    item_name[UF_UGMGR_FNAME_SIZE+1]; /* <len:UF_UGMGR_FNAME_SIZE+1> */

    /* Output:  component name, the name of the component in UG. */
    char    component_name[UF_CFI_MAX_PATH_NAME_SIZE]; /* <len:UF_CFI_MAX_PATH_NAME_SIZE> */

};


typedef struct UF_ROUTE_component_name_plugin_s
    UF_ROUTE_component_name_plugin_t, *UF_ROUTE_component_name_plugin_p_t;

/* Structure passed to the STOCK_COMPONENT_LOOKUP plugin. */
struct UF_ROUTE_component_reuse_plugin_s
{
    /* Input:   Tag of the stock object */
    tag_t   stock;

    /* Output:  Tag of the part to replace the
                stock component with. */
    tag_t   new_stock_component;
};
typedef struct UF_ROUTE_component_reuse_plugin_s
    UF_ROUTE_component_reuse_plugin_t, *UF_ROUTE_component_reuse_plugin_p_t;


/* Structure passed to the STOCK_COMPONENT_LOCKED plugin. */
struct UF_ROUTE_component_lock_plugin_s
{
    /* Input:   Tag of the stock object */
    tag_t   stock;

    /* Output:  TRUE if stock component can be modified,
                FALSE otherwise. */
    logical is_modifiable;
};
typedef struct UF_ROUTE_component_lock_plugin_s
    UF_ROUTE_component_lock_plugin_t, *UF_ROUTE_component_lock_plugin_p_t;


/* Structure passed to the ALLOW_DEFAULT_ELBOW_PLACEMENT plugin. */
struct UF_ROUTE_allow_default_fitting_plugin_s
{
    /*  Input:  The rcp to place the fitting at.  */
    tag_t                           rcp;

    /* Input:   Specification characteristics.  Each specification characteristic
     *          can have one or more possible values.  Default part selection ensures
     *          that every matching part has atleast one of the values from a
     *          multi valued specification characteristic.
     *          Eg: If FITTING_MATERIAL is a specification characteristic and
     *              has values COPPER, STEEL - all matching parts have a
     *              FITTING_MATERIAL value of either COPPER or STEEL.
     */
    int                             num_spec_charx;
    UF_EPLIB_multi_val_charx_p_t    spec_charx; /*len:num_spec_charx*/

    /* Input:   Part descriptor characteristics that are not in the specification
    *           characteristic list.  Part descriptor characteristics can
     *          only be single valued. These characteristics help uniquely
     *          determine the default fitting to place.
     */
    UF_ROUTE_part_lib_part_t        match_criteria;

    /* Input:   Part library table to use for determining the default fitting. */
    UF_EPLIB_part_table_p_t         default_fitting_table;

    /* Output:  if TRUE, default elbow placement at the input RCP is valid */
    logical                         allow_placement;

    /* Output:  if TRUE, forces placement of the part specified in the
     *          the override_fitting definition. */
    logical                         force_override;

    /* Output:  Only used if force_override is TRUE.  Fully specifies the default fitting
     *          to place [include values of all selection characteristics].
     */
    UF_ROUTE_part_lib_part_t        override_fitting;
};

typedef struct UF_ROUTE_allow_default_fitting_plugin_s
    UF_ROUTE_allow_default_fitting_plugin_t, *UF_ROUTE_allow_default_fitting_plugin_p_t;

struct UF_ROUTE_retrieve_eplib_data_s
{
    UF_EPLIB_part_lib_p_t   library;
    int                     error_code;
};

typedef struct UF_ROUTE_retrieve_eplib_data_s
            UF_ROUTE_retrieve_eplib_data_t, *UF_ROUTE_retrieve_eplib_data_p_t;


struct UF_ROUTE_cb_fab_data_s
{
        char   file_name[UF_ATTR_MAX_STRING_LEN];       /* file name, eg "C:\Temp\my_new_fab.prt"  */
        int    num_charx;                               /* number of charx */
        UF_ROUTE_charx_p_t   charx;                     /* charx list  */
};    
typedef struct UF_ROUTE_cb_fab_data_s UF_ROUTE_cb_fab_data_t, *UF_ROUTE_cb_fab_data_p_t;

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
extern UFUNEXPORT int UF_ROUTE_load_app_view(
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
extern UFUNEXPORT int UF_ROUTE_unload_app_view(
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
extern UFUNEXPORT int UF_ROUTE_set_current_app_view(
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
extern UFUNEXPORT int UF_ROUTE_ask_app_view_filename(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of Application View
                                        structure
                                        */
char ** filename  /* <OF>
                  Filename of the application view.
                  */
);


/**********************************************************************
Returns a string containing the name of the Application View.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_name(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of Application View
                                        structure
                                        */
char   ** name  /* <OF>
                Name of the Application View.
                */
);


/**********************************************************************
Returns a string containing the description of the Application View.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_desc(
UF_ROUTE_application_view_t  * app_view ,/* <I>
                                         Address of Application View
                                                structure
                                        */
char   ** description  /* <OF>
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
extern UFUNEXPORT int UF_ROUTE_ask_app_view_curves(
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
Returns an integer value which is a bit mask indicating the allowable
corner types for the given Application View. The bits set in this value
can be tested using symbols defined in uf_route.h. These are:
        UF_ROUTE_AV_CORNERS_BEND, UF_ROUTE_AV_CORNERS_COPE,
        UF_ROUTE_AV_CORNERS_MITER and UF_ROUTE_AV_CORNERS_SBEND.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_corners(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of the Application View
                                        structure
                                        */
int  * curves  /* <O>
               Flags indicating allowed corner
               types
               */
);


/**********************************************************************
Inquires the type of part library used by the given application view.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_plib_type(
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
Returns strings containing the shared library path and the entry point
function in the shared library.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_ext_plib(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of Application View
                                        structure
                                        */
char  ** library ,/* <OF>
                  Name of external library.
                  */
char   ** entry  /* <OF>
                 Name of entry point within the
                 given external shared library
                 */
);


/**********************************************************************
Inquires the part library view used by the given application view. This
should only be called if the part library type is
UF_ROUTE_LIBRARY_TYPE_VIEW.

Environment: Internal  and  External

See Also:  UF_ROUTE_ask_app_view_plib_type

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_plib_view(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Application view to query
                                        */
UF_EPLIB_part_library_view_p_t *part_lib_view  /* <OF>
                                               Part library view used by
                                               application view.
                                               */
);

/**********************************************************************
Returns the number of system interfaces and an array of these
interfaces.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_sys_ints(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of Application View
                                        structure
                                        */
int  * num_system_interfaces ,/* <O>
                              Number of system interfaces.
                              */
UF_ROUTE_system_interface_p_t * system_interfaces  /* <OF,len:num_system_interfaces>
                                                   Array of system interfaces.
                                                   */
);


/**********************************************************************
Inquires the default stock and anchor of the application view.  Either
or both may be returned as NULL. The default stock only makes
sense when the FILE_SELECTION type of part library is being used.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_def_stock(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Application View to query
                                        */
char ** stock ,/* <OF>
               Name of default stock
               */
char ** anchor  /* <OF>
                Name of default anchor
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
extern UFUNEXPORT int UF_ROUTE_ask_app_view_def_style(
UF_ROUTE_application_view_t * app_view ,/* <I>
                                        Address of the Application View
                                        structure
                                        */
int * style  /* <O>
             Default stock style
             */
);

/**********************************************************************
Returns the intersection of the required stock characteristcs and required
part characteristics for the current discipline of the application view.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_req_charx(
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
Returns the intersection of the optional stock characteristcs and optional
part characteristics for the current discipline of the application view.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_opt_charx(
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

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_app_view_fab_charx(
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
extern UFUNEXPORT int UF_ROUTE_load_app_view_list(
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
extern UFUNEXPORT int UF_ROUTE_ask_anchor_position(
tag_t anchor_tag ,/* <I>
                  Anchor to query
                  */
double position[3]  /* <O>
                    Position of anchor (ABS)
                    */
);


/**********************************************************************
When stock is assigned to a segment, or segments, an anchor is chosen
for the placment of the stock on the centerline.  This routine inquires,
for a given anchor, which stock is using this anchor for that position.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_anchor_stock(
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
extern UFUNEXPORT int UF_ROUTE_ask_anchor_stock_data(
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
extern UFUNEXPORT int UF_ROUTE_create_anchor_from_pnt(
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
extern UFUNEXPORT int UF_ROUTE_create_anchor_from_pos(
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
extern UFUNEXPORT int UF_ROUTE_is_part_anchor (
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
extern UFUNEXPORT int UF_ROUTE_ask_heal_pos(
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
extern UFUNEXPORT int UF_ROUTE_create_rcp_arc_center(
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
extern UFUNEXPORT int UF_ROUTE_create_rcp_curve_parm(
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
extern UFUNEXPORT int UF_ROUTE_create_rcp_point(
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
extern UFUNEXPORT int UF_ROUTE_create_rcp_position(
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
extern UFUNEXPORT int UF_ROUTE_ask_rcp_position(
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
extern UFUNEXPORT int UF_ROUTE_ask_rcp_segs(
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
extern UFUNEXPORT int UF_ROUTE_ask_rcp_on_port(
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
extern UFUNEXPORT int UF_ROUTE_ask_rcp_segments (
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
Returns the corner assigned to the RCP.  If no corner is assigned, then
NULL_TAG is returned.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_rcp_corner (
tag_t rcp_tag ,/* <I>
               Tag of Route Control Point.
               */
tag_p_t corner  /* <O>
                Tag of corner assigned to the RCP (or
                NULL_TAG).
               */
);

/**********************************************************************
Finds all the ports connected to a given RCP.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_rcp_ports (
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
Inquires whether the given RCP is an RCP on the end of a bend
segment. This is not the same as the bend RCP.

Return:
         Return code:
        TRUE = RCP is on a bend segment
        FALSE = RCP is not on a bend segment

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_is_rcp_bend_seg_rcp(
tag_t candidate ,/* <I>
                 Candidate RCP
                 */
tag_p_t corner  /* <O>
                Corner object or NULL_TAG
                */
);/* <NEC> */

/**********************************************************************
Creates an RCP whose position is associatively defined by an existing
port.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_rcp_at_port (
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
extern UFUNEXPORT int UF_ROUTE_create_rcp_by_wcs_off (
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
Inquires whether the given RCP has a miter corner assigned to it.

Return:
         Return code:
        TRUE = RCP has miter assigned
        FALSE = RCP has no miter assigned

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_is_rcp_miter_corner(
tag_t rcp  /* <I>
           Tag of RCP
           */
);/* <NEC> */

/**********************************************************************
Creates (or finds) an RCP at a work position in the WCS.

Environment: Internal  and  External

See Also:  UF_ROUTE_create_rcp_position

History:
 **********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_rcp_by_work_pos (
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
extern UFUNEXPORT int UF_ROUTE_create_rcp_on_rcp (
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
extern UFUNEXPORT int UF_ROUTE_simplify_rcps(
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
extern UFUNEXPORT int UF_ROUTE_create_seg_on_curve(
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
Creates a segment between two existing RCPs

Environment: Internal  and  External

See Also:


History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_seg_thru_rcps(
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
extern UFUNEXPORT int UF_ROUTE_ask_seg_rcps(
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
extern UFUNEXPORT int UF_ROUTE_ask_seg_curve(
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
extern UFUNEXPORT int UF_ROUTE_ask_segment_length(
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
extern UFUNEXPORT int UF_ROUTE_ask_segment_end_pnts(
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
extern UFUNEXPORT int UF_ROUTE_ask_segment_int_part(
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
extern UFUNEXPORT int UF_ROUTE_ask_segment_int_parts(
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
extern UFUNEXPORT int UF_ROUTE_ask_segment_stock(
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
Returns the bend corner that this segment represents. The corner is
NULL_TAG if segment is not a bend segment.

Environment: Internal  and  External

See Also:

History:Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_bend_crnr(
tag_t segment ,/* <I>
               Tag of segment to query.
               */
tag_p_t corner  /* <O>
                Tag of bend corner (or NULL_TAG).
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
extern UFUNEXPORT logical UF_ROUTE_are_segments_tangent(
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
extern UFUNEXPORT int UF_ROUTE_ask_segment_end_idx(
tag_t segment ,/* <I>
               Tag of segment ot query.
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
extern UFUNEXPORT int UF_ROUTE_ask_segment_end_props(
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
extern UFUNEXPORT logical UF_ROUTE_is_segment_inside_part(
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
extern UFUNEXPORT int UF_ROUTE_simplify_segments(
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
extern UFUNEXPORT int UF_ROUTE_add_segment_to_stock(
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
extern UFUNEXPORT int UF_ROUTE_remove_seg_from_stock(
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
Assigns a Bend corner. The radius for the bend is determined by
multiplying the given ratio times the diameter of the stock. The
stock's diameter is determined from a characteristic assigned to the
Stock Data object associated with the stock. The characteristic title
should be that returned by routine UF_ROUTE_ask_app_view_diameter.

If the input object is the RCP, corner, or Segment associated with an
existing bend corner, the corner and associated Segment is updated
with the new radius. If the assignment is to an RCP or Corner of a
Miter corner, the old corner is removed and a new Bend corner is
created.

Environment: Internal  and  External

See Also:


History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_bend_by_ratio(
tag_t obj_id ,/* <I>
              Object identifier of an existing RCP, or a
              Bend segment or a Corner.
              */
double ratio ,/* <I>
              Ratio of stock diameter to bend radius
              assigned to the Bend corner.
              */
tag_t * corner ,/* <O>
                Object identifier of the newly created
                Corner.
                */
tag_t * seg  /* <O>
             Object identifier of the Bend corner
             segment.
             */
);

/**********************************************************************
Assigns a Bend corner with the given radius to the input object. If the
input object is the RCP, corner, or Segment associated with an existing
bend corner, the corner and associated Segment is updated with the
new radius. If the assignment is to an RCP or Corner of a Miter
corner, the old corner is removed and a new Bend corner is created.

Environment: Internal  and  External

See Also:


History:Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_bend_by_radius(
tag_t obj_id ,/* <I>
              Object identifier of an existing RCP, or a
              Bend segment or a Corner.
              */
double radius ,/* <I>
               Radius of the Bend Corner.
               */
tag_t *corner ,/* <O>
              Object identifier of the newly created
              Corner.
              */
tag_t * seg  /* <O>
             Object identifier of the Bend corner
             segment.
             */
);

/**********************************************************************
Assigns a Miter corner to the input object. The assignment can
involve the removal of an existing Corner and the creation of a new
Corner.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_miter_corner(
tag_t obj_id ,/* <I>
              Object identifier of an existing RCP, or Bend
              segment or a Miter Corner.
              */
tag_t * corner  /* <O>
                Object identifier of the newly created Corner.
                */
);

/**********************************************************************
Returns the "corner" information such as type, RCP id and the Corner
object id when supplied with any one of the following:
   The RCP at which the corner was created.
   The Corner object id obtained after calling one of the
      UF_ROUTE_create_bend or UF_ROUTE_create_miter routines.
   The Segment created as a result of the Bend corner. Miter corner
      does not create a segment. The input may be an existing RCP, a
      Bend segment or a Corner object.

Return:
     TRUE object is some kind of corner
     FALSE otherwise.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_ask_obj_corner_info(
tag_t obj_id ,/* <I>
              Object identifier to interrogate. Can be an RCP,
              a Bend Segment, or a Corner (Bend or Miter)
              object .
              */
int * crn_typ ,/* <O>
               Corner type such as
               UF_ROUTE_CORNER_NONE
               UF_ROUTE_CORNER_BEND
               UF_ROUTE_CORNER_MITER
               */
tag_t * crn_rcp ,/* <O>
                 Object Identifier of the RCP at this Corner
                 only, else NULL_TAG
                 */
tag_t * crn_obj  /* <O>
                 Object Identifier of the Corner object. This is
                 equal to obj_id if the input is a Corner. If the
                 input is an RCP or Bend Segment this is the
                 Corner object to that RCP or segment
                 */
);/* <NEC> */


/**********************************************************************
Returns the Bend segment object identifier for a given Bend corner.
When a Bend Corner is created at the intersection of two Segments,
via the UF_ROUTE_create_bend_by_radius or
UF_ROUTE_create_bend_by_ratio routine, two new objects are
created. One is the Bend Corner object, which holds the information
about the corner, e.g., the radius, and the other is a Routing Segment
which models the bend or fillet between the two original Segments.
Returns the tag of this bend segment.

Environment: Internal  and  External

See Also:  UF_ROUTE_create_bend_by_radius
           UF_ROUTE_create_bend_by_ratio

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_bend_segment(
tag_t bend_obj ,/* <I>
                Object identifier of the Bend corner object
                */
tag_t * seg_id  /* <O>
                Object identifier of the segment that corresponds to
                the Bend.
                */
);

/**********************************************************************
Removes the Corner, be it a Bend or a Miter.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_remove_corner(
tag_t corner  /* <I>
              Object identifier of the Corner, Bend or
              Miter.
              */
);

/**********************************************************************
Returns the "bend corner"  radius when supplied with any one of the
following:
    . The RCP at which the Bend was created.
    . The Bend Corner object id obtained after calling one of the
      UF_ROUTE_create_bend routines.
    . The segment created as a result of the Bend Corner.


Return:
         Returns :
        True = If the obj_id is a valid bend object.
        False = invalid object.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_ask_obj_bend_radius(
tag_t obj_id ,/* <I>
              Object identifier to interrogate. Can be a RCP,
              a Bend segment, or a Corner (only bend
              corner) object.
              */
double * radius  /* <O>
                 Radius at the Bend Corner.
                 */
);/* <NEC> */

/**********************************************************************
Inquire of a bend, which RCP it is associated with.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_bend_rcp(
tag_t bend_tag ,/* <I>
                Tag of bend
                */
tag_t * rcp  /* <O>
             Tag of rcp which has bend corner assigned
             */
);

/**********************************************************************
Returns the radius of a bend.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_bend_radius(
tag_t bend_tag ,/* <I>
                Tag of bend object to query
                */
double * radius  /* <O>
                 Bend radius of bend
                 */
);

/**********************************************************************
Sets the characteristics to the given routing object.

Environment: Internal  and  External

See Also:


History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_characteristics(
tag_t obj_id ,/* <I>
              Object identifier of the routing object.
              */
int  charx_count ,/* <I>
                  Count of the characteristics.
                  */
UF_ROUTE_charx_p_t list  /* <I,len:charx_count>
                         List of all characteristics.
                         */
);

/**********************************************************************
Returns the characteristics data of a routing object.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_characteristics(
tag_t obj_id ,/* <I>
              Object identifier of the routing object.
              */
int c_type ,/* <I>
            Type of characteristic desired. Valid values
            are:
            UF_ROUTE_CHARX_TYPE_INT
            UF_ROUTE_CHARX_TYPE_REAL
            UF_ROUTE_CHARX_TYPE_STR
            UF_ROUTE_CHARX_TYPE_ANY
            */
int * charx_count ,/* <O>
                   Count of the characteristics.
                   */
UF_ROUTE_charx_p_t * list  /* <OF,len:charx_count,free:UF_ROUTE_free_charx_array>
                           List of all characteristics. The allocated list
                           must be freed by calling UF_ROUTE_free_charx_array.
                           */
);

/**********************************************************************
Deletes a list of  characteristics from a given routing object.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_delete_characteristics(
tag_t  obj_id ,/* <I>
               Object identifier of the routing object whose
               characteristics needs to be deleted.
               */
int charx_count ,/* <I>
                 Number of characteristics to be deleted.
                 */
UF_ROUTE_charx_p_t list  /* <I,len:charx_count>
                         List of  characteristics to be deleted.
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
     tne tag of the anchor and cross section objects which match
     the given anchor name and stock style.

 In either situation, the stock data, anchor, and cross section
 objects may then be used to assign stock of this type to segments
 within the routing.

 Environment: Internal  and  External

 See Also:

 History:
 *********************************************************************/
extern UFUNEXPORT int UF_ROUTE_load_stock_by_charx (
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
extern UFUNEXPORT int UF_ROUTE_load_stock_data(
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
without the need to "load" another. Stock will be created on the current
routing level. In order to create stock on other routing levels, use
UF_ROUTE_assign_stock_on_level.

Environment: Internal  and  External

See Also:  UF_ROUTE_load_stock_data
 UF_ROUTE_assign_stock_on_level


History: Original release was in V13.0.
 *********************************************************************/
extern UFUNEXPORT int UF_ROUTE_assign_stock(
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
Assigns stock to a set of segments. The segments need not belong to
the same path. This function uses the Stock Data, Anchor, and Cross
Section objects returned by "loading" the stock. Once the stock has
been "loaded", using UF_ROUTE_load_stock_data, several calls to
UF_ROUTE_assign_stock_on_level may be made (for various sets of segments)
without the need to "load" another. Stock will be created on the specified
routing level.

Environment: Internal  and  External

See Also:  UF_ROUTE_load_stock_data

History: Original release was in V17.0.
 *********************************************************************/
extern UFUNEXPORT int UF_ROUTE_assign_stock_on_level(
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
tag_t * segments,  /* <I,len:seg_count>
                  Array of segments tags to assign stock.
                  */
char *level     /* <I>
                  Routing level for the stock to be created
                  or UF_ROUTE_DEFAULT_LEVEL
               */
);

/************************************************************************
Set the routing level for the given object. The routing level is a
character string which determines which stock and fittings may be
connected to one another. Only stock and fittings (components) with the
same routing level are connected to one another.

Environment: Internal and External
See Also:
History: New in V18

************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_object_level(
tag_t obj,     /* <I>
                  Object identifier of the stock or fitting
                  whose routing level should be set
               */
char *level    /* <I>
                  Routing level
               */
);

/************************************************************************
Ask the routing level for the given object. The routing level is a
character string which determines which stock and fittings may be
connected to one another. Only stock and fittings (components) with the
same routing level are connected to one another.

Environment: Internal and External
See Also:
History: New in V18

************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_object_level(
tag_t obj,     /* <I>
                  Object identifier of the stock or fitting
                  whose routing level is returned
               */
char **level   /* <OF>
                  Routing level - This is the address of the character
                  string representing the level and must be freed by
                  the caller using UF_free.
               */
);

/************************************************************************
Ask the current routing level. The routing level is a character string
which determines which stock and fittings may be connected to one another.
Only stock and fittings (components) with the same routing level are
connected to one another.

Environment: Internal and External
See Also:
History: New in V18

************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_current_level(
char  **level  /* <OF>
                  The current (default) routing level to be
                  assigned to newly created stock or parts
                  added to the assembly. Must be freed by the
                  caller using UF_free.
               */
);

/************************************************************************
Set the current routing level. The routing level is a character string
which determines which stock and fittings may be connected to one another.
Only stock and fittings (components) with the same routing level are
connected to one another.

Environment: Internal and External
See Also:
History: New in V18

************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_current_level(
char   *level  /* <I>
                  The current (default) routing level to be
                  assigned to newly created stock or parts
                  added to the assembly
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
extern UFUNEXPORT int UF_ROUTE_remove_stock(
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
extern UFUNEXPORT int UF_ROUTE_set_stock_style(
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_diameter(
tag_t stock ,/* <I>
             Object identifier of the Stock.
             */
double * diameter  /* <O>
                   Diameter of the Stock.
                   */
);

/**********************************************************************
Returns the units asociated with the supplied stock. Routing
allows stock of a particlular unit, e.g., millimeters, to be assigned to
the segments of a part of different units, e.g., inches.
 Routing stock created prior to V14.0.1 does not have
the units information and any such stock returns 0 as its units value.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_units (
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
extern UFUNEXPORT int UF_ROUTE_ask_object_stock(
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_stock_data(
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_ports(
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_segments(
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_feature (
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_body (
tag_t stock_tag ,/* <I>
                 Tag of tock object to query
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_style (
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_cross_sect (
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_anchor (
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
extern UFUNEXPORT int UF_ROUTE_assign_stock_style (
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
extern UFUNEXPORT int UF_ROUTE_compute_stock_length(
tag_t stock ,/* <I>
             Tag of stock object
             */
double * total_path_length  /* <O>
                            Length of stock
                            */
);

/**********************************************************************
Update all out-of-date stock objects.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_fix_stale_stock( void );

/**********************************************************************
Inquires the current rotation of the stock object.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_stock_rotation (
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_profile_port (
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
extern UFUNEXPORT logical UF_ROUTE_is_stock_equal (
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
extern UFUNEXPORT int UF_ROUTE_solve_places(
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
This routine returns the origin and cys matrix data
associated with a Routing "placement" solution returned by
UF_ROUTE_solve_places.

First use UF_ROUTE_solve_places to get solutions, then call this
routine to obtain the origin and csys arrays that should be
applied to the part instance with UF_ASSEM_reposition_instance.

Environment: Internal  and  External
See Also:
History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_places_transform (
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
extern UFUNEXPORT int UF_ROUTE_free_places(
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
extern UFUNEXPORT int UF_ROUTE_set_part_in_stock(
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
extern UFUNEXPORT int UF_ROUTE_load_part_by_name(
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
Loads the given part, or part family member if member name is
among the list of characteristics, into the current session. The part is
loaded but NOT made the current work part. The returned part tag
may subsequently be used by the Assembly functions to add this part
as a component to the assembly for later "placement" within the
routing.

If the part is already loaded the routine finds the part. If member
name is among the list of characteristics, the routine will establish it if
it is an instance of the part.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_load_part_by_charx(
int  num_charx ,/* <I>
                Number of characteristics.
                */
UF_ROUTE_charx_t  charx[] ,/* <I,len:num_charx>
                           Array of characteristics associated with a part
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
extern UFUNEXPORT logical UF_ROUTE_is_part_occ_route_part(
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_data_cross(
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_data_anchors(
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_data_stock(
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

/**********************************************************************
Executes design rules based upon the given mode and reason.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_check_design_rules(
int mode ,/* <I>
          Design rule mode
          */
int reason ,/* <I>
            Design rule reason.
            */
int num_objects ,/* <I>
                 Number of objects to check (can be 0)
                 */
tag_t * objects ,/* <I,len:num_objects>
                 Tags of objects to check
                 */
int * num_violations ,/* <O>
                      The number of violations generated by the
                      check.
                      */
tag_t ** violations  /* <OF,len:num_violations>
                     The tags of the violations. To be freed
                     using UF_free.
                     */
);

/**********************************************************************
Creates a design rule violation. This rule is most likely to be called
from a design rule checking function.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_design_rule_vio(
tag_t rule ,/* <I>
            Tag of rule which has been violated.
            */
char * short_description ,/* <I>
                          Terse description of the violation.
                          */
char * long_description ,/* <I>
                         Verbose description of the violation.
                         */
int num_objects ,/* <I>
                 Number of objects in violation
                 */
tag_t * Objects ,/* <I,len:num_objects>
                 Array of objects in violation.
                 */
tag_t * violation  /* <O>
                   New violation object.
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

History :Orginal release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_user_preferences(
int n_pref ,/* <I>
            Number of preferences to query.
            */
UF_ROUTE_user_preference_t * prefs  /* <OF,len:n_pref>
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
extern UFUNEXPORT int UF_ROUTE_set_user_preferences(
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
extern UFUNEXPORT int UF_ROUTE_free_user_prefs_data(
int n_prefs ,/* <I>
             Number of preferences in data
             */
UF_ROUTE_user_preference_p_t prefs  /* <I,len:n_prefs>
                                    User preference data to free.
                                    */
);

/* Characteristics Environment */

/**********************************************************************
Replaces the current characteristic environment with the supplied set
of characteristics.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_charx_env(
int  num_charx ,/* <I>
                Number of characteristics supplied
                */
UF_ROUTE_charx_t charx[]  /* <I,len:num_charx>
                          Array of characteristics supplied.
                          */
);

/**********************************************************************
Updates the current characteristic environment with the given
characteristics by updating existing values in the environment and
adding new values.

Environment: Internal  and  External

See Also:

History:
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_update_charx_env(
int num_charx ,/* <I>
               Number of characteristics
               supplied.
               */
UF_ROUTE_charx_t  charx[]  /* <I,len:num_charx>
                           Array of characteristics
                           */
);

/**********************************************************************
Returns the number of characteristics and the array containing
characteristic titles, values and types.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_charx_env(
int * num_charx ,/* <O>
                 Number of the characteristics.
                 */
UF_ROUTE_charx_p_t * charx  /* <OF,len:num_charx>
                            List of all characteristics.
                            */
);

/**********************************************************************
Matches part entries in the part library based on the given set of
characteristics. If start is not NULL, it should be the name of the
node in the part library hierarchy at which to start the search.

Environment: Internal  and  External

See Also:  UF_ROUTE_free_match_results

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_match_charx_in_plib(
char * start ,/* <I>
              Name of the start node in the part
              library view tree.
              */
int num_criteria ,/* <I>
                  Number of characteristics being
                  matched
                  */
UF_ROUTE_charx_p_t criteria ,/* <I,len:num_criteria>
                             Array of match characteristics.
                             */
int * num_matches ,/* <O>
                   Number of matches found.
                   */
UF_ROUTE_part_lib_part_p_t * matches  /* <OF,len:num_matches,free:UF_ROUTE_free_match_results>
                                      Array of matches. To be freed using
                                      UF_ROUTE_free_match_results.
                                      */
);

/**********************************************************************
Frees the memory associated with the result of a part library match.
These values should not have been changed since being returned from
the match function (UF_ROUTE_match_charx_in_plib).

Environment: Internal  and  External

See Also:  UF_ROUTE_match_charx_in_plib

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_free_match_results(
int num_matches ,/* <I>
                 Number of matches to be freed
                 */
UF_ROUTE_part_lib_part_p_t matches  /* <I,len:num_matches>
                                    Array of matches to be freed
                                    */
);/* <NON_NXOPEN> */

/**********************************************************************
Returns all the port occurrences on the given part occurrence.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_part_occ_ports(
tag_t part_tag ,/* <I>
                Object identifier of a part occurrence.
                */
int * num_ports ,/* <O>
                 Number of port occurrences in the given part
                 occurrence.
                 */
tag_t ** ports  /* <OF,len:num_ports>
                Tags of port occurrences of the part occurrence
                else NULL_TAG. Allocated array must be
                freed with UF_free.
                */
);

/**********************************************************************
Returns the tag of the part_occurrence containing the given port
occurrence. If the port tag given is not an occurrence, NULL_TAG is
returned.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_part_occ(
tag_t port_tag ,/* <I>
                Object identifier of the port.
                */
tag_t * part_occ  /* <O>
                  Occurrence tag of the part to which this port
                  belongs.
                  */
);

/**********************************************************************
Returns the tag of the port occurrence of given extract port
If the port tag given is an occurrence, NULL_TAG is returned

Environment: Internal  and  External

See Also:

History: Original release was in NX3
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_occ_of_port(
tag_t port_tag ,/* <I>
                Object identifier of the port.
                */
tag_t * port_occ  /* <O>
                  Corresponding Occurrence tag of this port
                  */
);

/**********************************************************************
Returns the tag of the connection object of the port. If this port is not
connected,  NULL_TAG is returned.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_connection(
tag_t port_tag ,/* <I>
                Object identifier of the port.
                */
tag_t * connection  /* <O>
                    Connection tag at this port else if the port is
                    not connected then NULL_TAG.
                    */
);

/**********************************************************************
Finds the tags of the two ports of a connection object.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_connection_ports(
tag_t conn_tag ,/* <I>
                Object identifier of the connection.
                */
tag_t * ports  /* <O>
               Array of the two port tags at this
               connection.
               */
);

/**********************************************************************
Finds a Routing characteristic of the given title for the supplied
port occurrence. If the given port occurrence does not have the given
characteristic, the port's part occurrence is queried for the
characteristic.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_find_port_charx(
char * charx_name ,/* <I>
                   Name of the characteristic to be found
                   */
int type ,/* <I>
          Type of the characteristic to be found, e.g.,
          UF_ROUTE_CHARX_TYPE_INT
          */
tag_t port ,/* <I>
            Tag of the port occurrence to be queried
            */
UF_ROUTE_charx_p_t charx  /* <O>
                          Address of charx structure (allocated by the
                          caller) which will be filled in with the value
                          of the characteristic.
                          */
);

/**********************************************************************
Returns the position of a port.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_position(
tag_t port_tag ,/* <I>
                Tag of port to query.
                */
double position[3]  /* <O>
                    Position of port.
                    */
);

/**********************************************************************
Inquire whether the given port uses an alignment vector.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_align_flag(
tag_t port_tag ,/* <I>
                Port to query
                */
logical * flag  /* <O>
                Port alignment flag:
                TRUE = Port uses an alignment vector.
                FALSE = Port does not use an alignment vector.
                */
);

/**********************************************************************
Returns the alignment vector of a port.

Environment: Internal  and  External

See Also:  UF_ROUTE_ask_port_align_flag

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_align_vector(
tag_t port_tag ,/* <I>
                Tag of port to query
                */
double vector[3]  /* <O>
                  Alignment vector of port
                  */
);

/**********************************************************************
Inquires whether the given port uses a rotation vector.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_rotate_flag(
tag_t port_tag ,/* <I>
                Port to query.
                */
logical * flag  /* <O>
                Port rotation flag.
                */
);

/**********************************************************************
Returns the rotation vector of a port.

Environment: Internal  and  External

See Also: UF_ROUTE_ask_port_rotate_flag

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_rotate_vector(
tag_t port_tag ,/* <I>
                Tag of port to query.
                */
double vector[3]  /* <O>
                  rotation vector of port.
                  */
);

/**********************************************************************
Inquires the engagment distance of a port, i.e. the distance behind the
port that another fitting or stock may engage.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_engagement(
tag_t port_tag ,/* <I>
                Tag of port to query.
                */
double * distance  /* <O>
                   Engagement distance
                   */
);

/**********************************************************************
Inquires the associative scalar object which defines the engagement
distance of a port.

Environment: Internal  and  External

See Also: UF_SO_ask_double_of_scalar
          UF_SO_set_double_of_scalar

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_engage_obj(
tag_t port_tag ,/* <I>
                Tag of port
                */
tag_t * engage_obj  /* <O>
                    Tag of scalar object defining the engagement
                    distance.
                    */
);

/**********************************************************************
Returns the tag of the stock object to which the port is attached. If the
port does not belong to a stock, NULL_TAG is returned. Only connection
ports are considered, not fixture ports.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_stock(
tag_t port_tag ,/* <I>
                Object identifier of the port.
                */
tag_t * stock_tag  /* <O>
                   Tag of the stock object.
                   */
);

/**********************************************************************
If the port position and alignment are derived from a segment, return
that segment.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_segment(
tag_t port_tag ,/* <I>
                Tag of port to query.
                */
tag_t * segment  /* <O>
                 Tag of segment.
                 */
);

/**********************************************************************
Inquires the port derived by the segment and the given end index.

Environment: Internal  and  External

See Also: UF_ROUTE_ask_segment_end_idx

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_on_segment (
tag_t segment ,/* <I>
               Segment to query.
               */
int segend ,/* <I>
            Segment end index.
            */
tag_t * port  /* <O>
              Port derived by the segment at the given end.
              */
);

/**********************************************************************
Determine if the supplied port is a fixture port. Fixture ports differ from
fitting ports in that they do not subdivide the segment upon which the part
containing the port is placed. They are used to model the "connection"
point of "fixture" type parts such as clamps or other support fixtures.

Environment: Internal  and  External

See Also:

History: Original release was in V17.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_is_port_fixture_port (
tag_t port ,/* <I>
            Port to query.
            */
logical *is_fixture /* <O>
                    True if the port is a fixture port and false otherwise
                    */
);

/**********************************************************************
Creates a port at the specified end of a segment.  The position of the
port is associated with the end RCP.  The alignment direction of the
port is associated with the slope of the segment at the end.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_port_at_segend (
tag_t segment ,/* <I>
               Tag of segment
               */
int segend ,/* <I>
            End index (0 or 1)
            */
logical rotate_flag ,/* <I>
                     Does the port have a rotation vector?
                     */
tag_t * port  /* <O>
              Tag of created port
              */
);

/**********************************************************************
Creates a port associative to an existing axis object. The port origin
corresponds to the AXIS origin, and the alignment vector corresponds
to the AXIS direction.  The port is assumed to have no rotation
vector.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_port_from_axis(
tag_t ref_axis ,/* <I>
                Tag of reference AXIS
                */
tag_t * port  /* <O>
              Tag of created port
              */
);

/**********************************************************************
Creates a port using a coordinate system. The position of the
coordinate system defines the position of the port. The Z direction of
the coordinate system defines the alignment vector of the port, and
the Y direction of the coordinate system defines the rotation vector (if
rotate_flag == TRUE) of the port.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_port_from_csys(
logical rotate_flag ,/* <I>
                     Does the port have a rotation vector?
                     TRUE = Has a rotation vector
                     FALSE = Does not have a rotation vector.
                     */
logical fixture_flag ,/* <I>
                      Is the port a fixture port?
                      TRUE = Port is a fixture port.
                      FALSE = Port is not a fixture port.
                      */
tag_t ref_csys ,/* <I>
                Reference coordinate system
                */
tag_t * port  /* <O>
              Tag of created port
              */
);

/**********************************************************************
Attempts to connect a port to other available ports.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_connect_port(
tag_t port ,/* <I>
            Tag of port
            */
tag_t * connection  /* <O>
                    Tag of connection (or NULL_TAG)
                    */
);

/**********************************************************************
Disconnects the port from any connection which it may include.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_disconnect_port(
tag_t port  /* <I>
            Port to disconnect
            */
);

/**********************************************************************
Determines whether two ports would make a valid connection.  Which
means they satisfy the following conditions: The port positions are
equivalent, the port alignment vectors are colinear and opposed, the
port rotation vectors (if defined) match, and neither port is interior to
a part.

Return:
         TRUE    =       Ports make a valid connection
         FALSE   =       Ports make invalid connection

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_are_ports_connectable(
tag_t port1 ,/* <I>
             Port to test
             */
tag_t port2  /* <I>
             Port to test
             */
);/* <NEC> */


/**********************************************************************
Inquires the position of the port taking into account the engagement
distance.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_engaged_pos(
tag_t port ,/* <I>
            Tag of port to query.
            */
double position[3]  /* <O>
                    The engaged position of the port.
                    */
);


/**********************************************************************
Inquires the port to which a given port is connected.

Return:
         Return code:
        TRUE = curr_port is connected
        FALSE = curr_port is not connected

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_ask_port_conn_port (
tag_t curr_port ,/* <I>
                 Port to query.
                 */
tag_t * connected_port  /* <O>
                        Tag of connected port or NULL_TAG.
                        */
);/* <NEC> */

/**********************************************************************
 * Query if a port is a terminal port.
 *
 * Return:
 *     TRUE if the port is terminal
 *     FALSE otherwise
 *
 * Environment: Internal and External
 *
 * See Also:  UF_ROUTE_is_port_multi
 *
 * History: Originally released in V16.0
 *
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_is_port_terminal(
tag_t port /* <I> tag of port to query */
);/* <NEC> */

/**********************************************************************
 * Query if a port is a multiport.
 *
 * Return:
 *      TRUE if the port is a multiport
 *      FALSE otherwise
 *
 * Environment: Internal and External
 *
 * See Also:  UF_ROUTE_is_port_terminal
 *
 * History: Originally released in V16.0
 *
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_is_port_multi(
tag_t port /* <I> tag of port to query */
);/* <NEC> */

/**********************************************************************
 * Add given terminal ports to the given port
 *
 * Environment: Internal and External
 *
 * See Also:  UF_ROUTE_add_virtual_ports
 *
 * History: Originally released in V16.0
 *
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_add_terminal_ports(tag_t multi,   /* <I>
                                               Tag of  multiport
                                               */
                                int num_terms, /* <I>
                                               Number of terminal ports
                                               */
                                tag_t *terms   /* <I,len:num_terms>
                                               Array of terminal port tags
                                               */
);

/**********************************************************************
 * Add given virtual ports to the given port
 *
 * Environment: Internal and External
 *
 * See Also:  UF_ROUTE_add_virtual_ports
 *
 * History: Originally released in V16.0
 *
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_add_virtual_ports(tag_t multi,     /* <I>
                                                Tag of  multiport
                                                */
                               int num_terms,   /* <I>
                                                Number of virtual ports
                                                */
                               char **terms     /* <I,len:num_terms>
                                                Array of virtual port
                                                unique ids
                                                */
);

/**********************************************************************
 * Remove virtual ports from the multiport
 *
 * Environment: Internal and External
 *
 * See Also:  UF_ROUTE_remove_terminal_ports
 *
 * History: Originally released in V16.0
 *
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_remove_virtual_ports(tag_t multi,  /* <I>
                                                       multiport
                                                       */
                                         int num_terms,/* <I>
                                                       Number of virtual ports
                                                       */
                                         char **terms  /* <I,len:num_terms>
                                                       Array of virtual ports
                                                       unique ids
                                                       */
);

/**********************************************************************
 * Remove terminal ports from the multiport
 *
 * Environment: Internal and External
 *
 * See Also:  UF_ROUTE_remove_virtual_ports
 *
 * History: Originally released in V16.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_remove_terminal_ports(tag_t multi,  /* <I>
                                                        multiport
                                                        */
                                         int num_terms, /* <I>
                                                        Number of terminal ports
                                                        */
                                          tag_t *terms  /* <I,len:num_terms>
                                                        Array of terminal port
                                                        tags
                                                        */
);

/**********************************************************************
 * Queries the multiport of the given terminal port
 *
 * Environment: Internal and External
 *
 * See Also:  UF_ROUTE_remove_virtual_ports
 *
 * History: Originally released in V16.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_terminal_multiport(tag_t terminal /* <I>
                                                          Terminal port to query
                                                          */,
                                           tag_t *multi /* <O>
                                                        Multiport
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
extern UFUNEXPORT int UF_ROUTE_ask_multiport_terminals(
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
 * Finds the terminal port on the given multiport
 *
 * Return:
 *     TRUE if a terminal or virtual port is found, else FALSE
 * Environment: Internal and External
 * See Also:
 * History: Originally released in V16.0
 ***********************************************************************/
extern UFUNEXPORT logical UF_ROUTE_find_terminal_port(
tag_t multi,         /* <I>
                     Multiport to search
                     */
char *id,            /* <I>
                     ID of the terminal port
                     */
tag_t *tag           /* <O>
                     Pointer to tag of a terminal port, if found.
                     */
);


/**********************************************************************
Modifies the stock object rotation about the segment to point in the
direction of the given vector.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_align_stock (
tag_t stock ,/* <I>
             Stock object to modify
             */
double rotate_vec[3]  /* <I>
                      New vector for rotation
                      */
);

/**********************************************************************
Sets the rotation vector of a port by passing a point at which the
rotation vector should point.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_port_rot_by_point(
double pnt_pos[3] ,/* <I>
                   Position for rotation
                   */
tag_t port_tag  /* <I>
                Tag of port
                */
);

/**********************************************************************
Executes the Routing minimum bend radius design rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_check_min_bend_radius(
tag_t rule ,/* <I>
            Tag of the rule to be checked
            */
char * coefficient ,/* <I>
                    Name of the user preference which
                    specifies the minimum bend ratio
                    */
UF_ROUTE_design_rule_data_p_t rule_data  /* <I>
                                         Design Rule data
                                         */
);

/**********************************************************************
Executes the Routing minimum straight length design rule.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_check_min_str_length(
tag_t rule ,/* <I>
            Tag of the rule to be checked
            */
char * coefficient ,/* <I>
                    Name of the user preference which
                    specifies the minimum straight length
                    coefficient
                    */
UF_ROUTE_design_rule_data_p_t rule_data  /* <I>
                                         Design Rule data
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
extern UFUNEXPORT int UF_ROUTE_ask_part_part_type(
tag_t r_part ,/* <I>
              The tag of a part occurrence, RM_part or
              PART_part to be inquired.
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
extern UFUNEXPORT int UF_ROUTE_is_part_fabrication(
tag_t fab_part ,/* <I>
                The tag of a part occurrence, RM_part or
                PART_part to be inquired.
                */
logical *fab  /* <O>
             Logical set to TRUE if the part is a Routing
             fabrication part and FALSE otherwise.
             */
);

/**********************************************************************
Adds a new TCL function to the active Routing TCL translator.
This function currently may only be called from a design rule. Also,
the new function is only active during the design rule invocation.
Each invocation of design rule checking has a NEW translator.

Environment: Internal  and  External

See Also:

History: Original release was in V15.0.
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_extend_translator(
char * tcl_name ,/* <I>
                 Name of new TCL function
                 */
UF_ROUTE_tcl_proc_f_t func ,/* <I>
                            Function to call for given TCL function name
                            */
void * client_data  /* <I>
                    Pointer to data to pass to function
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
extern UFUNEXPORT int UF_ROUTE_create_cross_section(
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
extern UFUNEXPORT int UF_ROUTE_create_round_cross_section(
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
extern UFUNEXPORT int UF_ROUTE_ask_cross_curves(
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
extern UFUNEXPORT int UF_ROUTE_ask_cross_style(
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
extern UFUNEXPORT int UF_ROUTE_ask_cross_offsets(
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
extern UFUNEXPORT int UF_ROUTE_ask_cross_stock_data(
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
extern UFUNEXPORT int UF_ROUTE_set_part_search_path(
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
extern UFUNEXPORT int UF_ROUTE_ask_part_search_path(
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
extern UFUNEXPORT int UF_ROUTE_find_part_in_path(
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
extern UFUNEXPORT int UF_ROUTE_calc_abs_minmax_box(
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
extern UFUNEXPORT int UF_ROUTE_unset_shadow_for_view(
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
extern UFUNEXPORT int UF_ROUTE_is_port_connected(
tag_t port_tag,        /* <I>
                       Tag of the port examined.
                       */
logical  *is_connected /* <O>
                       true if connected else false
                       */
);
/**********************************************************************
This function frees the allocated charx array. Must use after every
call to UF_ROUTE_ask_characteristics

Environment: Internal  and  External

See Also:

History:
***********************************************************************/
extern UFUNEXPORT  int UF_ROUTE_free_charx_array (
int    num_charx,               /* <I>
                                Number of Charx values
                                */
UF_ROUTE_charx_p_t charx_list   /* <I,len:num_charx>
                                Array of the characteristics
                                */
);/* <NON_NXOPEN> */

/**********************************************************************
Create an Isometric Drawing for the selected part

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_iso_drawing (
tag_t part_tag /* <I>
               Tag of the part to be represented in the isometric
               drawing.
               */
);

/*********************************************************************
Detach the segments from their follow curves by removing the associativity
between the segments and their follow curves, removing the associativity
between the guide curve and the follow curve, and either making their rcps
absolute or redefining them in terms of the follow curve of another segment
that we are not detaching

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_detach_segments (
int segment_count,  /* <I>
                    The number of segments to be detached
                    */

tag_p_t segments    /* <I,len:segment_count>
                    An array of tags of the segments to be detached
                    */
);

/*****************************************************************************
Finds a path between two segments and returns an array of tags consisting
of the segments and part occurrences that make up the path.  The array of
tags returned is in order from begin to end.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_find_path(
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
extern UFUNEXPORT int UF_ROUTE_ask_length_tolerance(
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

typedef struct UF_ROUTE_tag_list_s
{
    unsigned int      num_alloc;  /* Number of elements allocated for the Variable
                                     length Array of tags
                                   */
    unsigned int      num_used;   /* Currently used Number of elements in array
                                   */
    tag_t             *array;     /*  <len:num_alloc>Variable length array of tags
                                   */

} UF_ROUTE_tag_list_t, *UF_ROUTE_tag_list_p_t ;

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
                                        may be only of types UF_route_part_type_type,
                                        UF_route_control_point_type or
                                        UF_route_segment_type.
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
                                       including those that could'nt be merged
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

/*****************************************************************************

  Finds the index of the charx whose title matches the title passed in.  If
  the index is -1 the title was not found in the charx.

  Environment: Internal and External
  See Also:
  History: New in V17

 *****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_find_title_in_charx
(
    int                 num_charx,  /* <I>    number of charx */
    UF_ROUTE_charx_p_t  charx,      /* <I,len:num_charx>
                                        array of charx to search */
    char*               title,      /* <I>    title to search for */
    int*                index       /* <O>    Index into charx that matches title */
);


/**********************************************************************

Ask a specific charx value from a port. If the information is not found
attached to the port, the part is queried.

Environment: Internal  and  External
See Also:
History: Released in V17.0

 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_charx(
    char *charx_name,   /* <I> , the name of the charx to get */
    int   expected_type,/* <I> , the expected type of the charx*/
    tag_t port_tag,     /* <I> , the tag of the port to query*/
    UF_ROUTE_charx_p_t desired_charx /* <O> , the charx value returned*/);



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

Ask the hanresses associated with a wire.

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

Queries the name of the charx of which virtual port names are considered
values.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_multiport_termname(
    tag_t port_tag  /* <I> , the tag of the port to query*/,
    char  **name    /* <OF>, the name of the virutal port, free using UF_free */);


/**********************************************************************

Queries the virtual port names of the given multiport .

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_multiport_strings(
    tag_t   port_tag,       /* <I> , the tag of the port*/
    int     *num_strings,   /* <O> , the number of strings*/
    const char ***strings   /* <OF,len:num_strings>
                               the array of names, don't free the
                               individual strings, just call UF_free(strings); */);


/**********************************************************************

Gets the tags of the virtual ports associated with the multiport.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_multiport_tags(
    tag_t   port_tag,   /* <I> , the tag of the port*/
    int     *num_tags,  /* <O> , the number of tags*/
    tag_t   **tags      /* <OF,len:num_tags>,
                            the array of virtual ports,
                            use UF_free to free up the array.*/ );

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
extern UFUNEXPORT int UF_ROUTE_ask_segment_branch_angle(
    tag_t   segment,        /* <I>, the segment to query */
    double  *branch_angle   /* <O>, the branch angle. */ );

/**********************************************************************

Find the multiport associated with the given port.
If given port is a multiport, return itself.  If its
a terminal port, return its multiport.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_multiport(
    tag_t port      /* <I>, the port to query */,
    tag_t *multi    /* <O>, the tag of the mutiport assiated with the port */ );


/**********************************************************************

Find terminal ports associated with the given port.
If given port is a multiport, return all terminal
ports. If its a terminal port, return itself.  If the
input port is an occurrence, return occurrences of
terminal ports in given ports part occurrence tree.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_terminal_ports(
    tag_t port,        /* <I> , the port to query*/
    int  *num_terms,   /* <O> , the number of associated terminal ports*/
    tag_t **terms      /* <OF,len:num_terms>
                          the array of terminal ports,
                          use UF_free to free up the array.*/
    );


/**********************************************************************

Find the characteristic of specified type and name
for the given terminal port.  The characteristic is
looked for in the following order:
1) input terminal tag
2) the terminal's prototype if the input terminal is an occurrence.
3) the terminal's multiport
4) the terminal's part occurrence

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_find_terminal_charx(
    char  *charx_name,      /* <I> , the name of the charx to search for*/
    int   charx_type,       /* <I> , the type of the charx */
    tag_t terminal,         /* <I> , the tag of the terminal port being asked*/
    UF_ROUTE_charx_p_t charx/* <O> , the desired charx*/);


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

Looks at characteristics of given port to determine
the cut back length.  If cut back length is not found, look at component of
the port for same characteristic.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_cut_back_length
(
   tag_t port,              /* <I> Tag of port beings asked */
   double *cut_back_length  /* <O> Cut back length          */
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

Find the "uid" value for the characteristic
ROUTE_PORT_ID_CHARX_TITLE of given terminal port.  If not
found on the terminal, look for it on its prototype if it
is an occurrence.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_terminal_port_uid(
    tag_t   terminal    /* <I> , the terminal port being asked*/,
    char    **uid       /* <OF>, the uid of the terminal port. Use UF_free to free. */);


/**********************************************************************

This function will query a terminal port to find out
the tag of the rcp located at its position.
Three methods are used. First the direct derivation
is checked.  Second, the method to identify terminal
wires is used (Smart Point -> BCURVE -> ROUTE_segment
-> segment_ends ).  Last, if the terminal port is at
the same location of a multiport, the multiport is
queried through the use of ES_ROUTE_ask_rcp_on_port

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_rcp_at_term_port(
    tag_t port  /* <I> , the terminal port to query*/,
    tag_t *rcp  /* <O> , the rcp at the terminal port*/,
    logical* at /* <O> , true if there is an rcp at the term port*/);


/**********************************************************************

Finds the port connected to a given port within the work part.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_connected_port (
    tag_t curr_port,        /* <I> , the current port or port occ*/
    tag_t *connected_port,  /* <O> , the conected port or NULL_TAG*/
    logical *connected      /* <O> , true if current port is connected*/);


/**********************************************************************

Ask any stock on a given segment that belongs to specified wire harness.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_segment_bundle_stock(
    tag_t segment /* <I> , the segment  to query*/,
    tag_t harness /* <I> , the harness to query*/,
    tag_t *stock  /* <O> , the stock tag*/ );


/**********************************************************************

This function extracts the stock fields for the stock report. This function
cycles through all routed records of the connection list and finds the
fields common to all these records. These fields for each record are
determined from the stock-data charx.

Environment: Internal  and  External
See Also:
History: Released in V17.0
 ***********************************************************************/
extern UFUNEXPORT int UF_RLIST_find_stock_flds
(
    tag_t conn_list,            /* <I> , Connection list tag */
    int *num_strs,              /* <O> , Number of strings*/
    UF_ROUTE_charx_p_t *strs    /* <OF,len:num_strs>,
                                   Array of strings,
                                   must be freed by calling UF_free */
);

/**********************************************************************
This function returns the clock angle increment value for a port.
The clocking increment value on a port is used to determine the valid clocking
angle values.  The valid clocking angles are the angle values that can
be used for setting the angle between the rotation vectors of two
ports that are connected to each other.

Environment: Internal  and  External
See Also:
History: Released in V18.0
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_clock_increment(
    tag_t   port,        /* <I>  The port to query. */
    double  *increment   /* <O>  The increment of the clock angle. */
);

/**********************************************************************
This function sets the clock angle increment value for a port.

Environment: Internal  and  External
See Also:
History: Released in V18.0
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_port_clock_increment(
    tag_t   port,       /* <I>  The port to modify. */
    double  increment   /* <I>  The increment of the clock angle. */
);

/**********************************************************************

This function locks two components together using mating conditions.
The given port occurrence is a port that is connected to a port that
is part of another component.  The component of the passed in port
is the from (or child) of the mating condition.  The lock rotation
flag indicates whether or not the child component will be able to
rotate.

If an error occurs, UF_ROUTE_err_invalid_port_mate will be returned.

Environment: Internal and External
See Also:
History: Released in V18.0
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_port_lock(
    tag_t   from_port_occ, /* <I> From (child) port occurrence tag. */
    logical lock_rotation  /* <I> Lock rotation. */
);

/**********************************************************************

This function deletes a lock between two components.  The passed in object
is the from (or child) port or part occurrence.

If an error occurs, UF_ROUTE_err_invalid_port_mate will be returned.

Environment: Internal and External
See Also:
History: Released in V18.0
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_delete_port_lock(
    tag_t   from_occ    /* <I> child port occ, or part occ */
);


/**********************************************************************

This function returns information about a lock on a part occurrence
given the from or to (child or parent) port occurrence that was used
to create the lock.

If an error occurs, UF_ROUTE_err_invalid_port_mate will be returned.

Environment: Internal and External
See Also:
History: Released in V18.0
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_lock_info(
    tag_t   port_occ,           /* <I> The FROM or TO port occurrence */
    logical *is_locked,         /* <O> TRUE if given port participates in a lock */
    logical *is_rotation_locked,/* <O> TRUE if rotation is locked */
    logical *is_from_port       /* <O> TRUE if given port is the FROM port */
);


/**********************************************************************

This function is used to set the lock rotation flag of a  port lock.
If the passed in flag is true, and the ports involved in the lock
both have rotation vectors, then the child component will not be
able to rotate. If the flag is false, then the child component
of the lock will be able to rotate freely.

If an error occurs, UF_ROUTE_err_invalid_port_mate will be returned.

Environment: Internal and External
See Also:
History: Released in V18.0
***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_port_lock_rotation_flag(
    tag_t   port_occ,           /* <I> The FROM or TO port occurrence */
    logical rotation_locked     /* <I> Lock rotation flag. */
);


/*****************************************************************************

This function initializes a bend segment info structure with the
bend data from a given solid body, segment or stock tag.
Call UF_ROUTE_bend_report_free_segment_info to free up the bend_segs structure.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_bend_report_get_segment_info(
    tag_t                           pipe_tag,       /* <I> Segment, solid body, or stock tag */
    UF_ROUTE_bend_segment_info_p_t *bend_segs       /* <OF,free:UF_ROUTE_bend_report_free_segment_info>
                                                       Stock bend info. */
);

/*****************************************************************************

This function reverses the order of bends in a stock bend info structure.
Call UF_ROUTE_bend_report_free_segment_info to free up the
reversed_bend_segs structure.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_bend_report_reverse_direction(
    UF_ROUTE_bend_segment_info_p_t  bend_segs,          /* <I>  Stock bend info */
    UF_ROUTE_bend_segment_info_p_t  *reversed_bend_segs /* <OF,free:UF_ROUTE_bend_report_free_segment_info>
                                                           Stock bend info in reverse order */
);

/*****************************************************************************

This function returns the number of bend segments in the given stock bend info.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_bend_report_ask_number_of_bends(
    UF_ROUTE_bend_segment_info_p_t  bend_segs,  /* <I>  Stock bend info */
    int*                            num_bends   /* <O>  Number of bends */
);



/*****************************************************************************

This function frees a bend segment info structure that is returned from
a call to UF_ROUTE_bend_report_get_segment_info.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_bend_report_free_segment_info(
    UF_ROUTE_bend_segment_info_p_t bend_segs    /* <I>Stock bend info. */
);/* <NON_NXOPEN> */


/*****************************************************************************

This function takes the data returned from a call to
UF_ROUTE_bend_report_get_segment_info, and returns a data structure containing
the bend report information in the XYZ format.
Call UF_ROUTE_bend_report_free_xyz_report to free up the returned data.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_bend_report_generate_xyz_report(
    UF_ROUTE_bend_segment_info_p_t  bend_segs,  /*<I>   Stock bend info. */
    UF_ROUTE_bend_report_xyz_p_t    *xyz_data   /*<OF,free:UF_ROUTE_bend_report_free_xyz_report>
                                                  XYZ bend report */
);


/*****************************************************************************

This function frees a xyz bend report structure that is returned from
a call to UF_ROUTE_bend_report_generate_xyz_report.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_bend_report_free_xyz_report(
    UF_ROUTE_bend_report_xyz_p_t xyz_data   /*<I>   XYZ bend report */
);/* <NON_NXOPEN> */

/*****************************************************************************

This function takes the data returned from a call to
UF_ROUTE_bend_report_get_segment_info, and returns a data structure containing
the bend report information in the YBC format.
Call UF_ROUTE_bend_report_free_ybc_report to free up the returned data.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_bend_report_generate_ybc_report(
    UF_ROUTE_bend_segment_info_p_t  bend_segs,  /*<I>   Stock bend info. */
    UF_ROUTE_bend_report_ybc_p_t    *ybc_data   /*<OF,free:UF_ROUTE_bend_report_free_ybc_report>
                                                  YBC bend report */
);


/*****************************************************************************

This function frees a ybc bend report structure that is returned from
a call to UF_ROUTE_bend_report_generate_ybc_report.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_bend_report_free_ybc_report(
    UF_ROUTE_bend_report_ybc_p_t    ybc_data   /*<I>  YBC bend report */
);/* <NON_NXOPEN> */

/*****************************************************************************

This function takes the data returned from a call to
UF_ROUTE_bend_report_get_segment_info, and returns a data structure containing
the bend report information in the MIL98 format.
Call UF_ROUTE_bend_report_free_mil98_report to free up the returned data.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_bend_report_generate_mil98_report(
    UF_ROUTE_bend_segment_info_p_t  bend_segs,      /*<I>   Stock bend info */
    UF_ROUTE_bend_report_mil98_p_t  *mil98_data     /*<OF,free:UF_ROUTE_bend_report_free_mil98_report>
                                                      MIL98 bend report */
);

/*****************************************************************************

This function frees a mil98 bend report structure that is returned from
a call to UF_ROUTE_bend_report_generate_mil98_report.

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_bend_report_free_mil98_report(
    UF_ROUTE_bend_report_mil98_p_t mil98_data       /* <I> MIL98 bend report */
);/* <NON_NXOPEN> */

/*****************************************************************************

This function returns the extension value for a port.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_extension(
    tag_t       port,   /* <I>, the port */
    double*     ext     /* <O>, the port extension */
);

/*****************************************************************************

This function returns the extension object for a port.
The returned object is a UF_scalar_type.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_extension_obj(
    tag_t       port,   /* <I>, the port */
    tag_t*      ext     /* <O>, the port extension object */
);

/*****************************************************************************

This function sets the extension value for a port.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_port_extension(
    tag_t       port,   /* <I>, the port */
    double      ext     /* <I>, the port extension */
);

/*****************************************************************************

This function sets the extension object for a port.
The object must be a UF_scalar_type.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_port_extension_obj(
    tag_t       port,   /* <I>, the port */
    tag_t       ext     /* <I>, the port extension object */
);

/*****************************************************************************

This function returns the back extension value for a port.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_back_extension(
    tag_t       port,   /* <I>, the port */
    double*     ext     /* <O>, the port back extension */
);

/*****************************************************************************

This function returns the back extension object for a port.
The returned object is a UF_scalar_type.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_port_back_extension_obj(
    tag_t       port,   /* <I>, the port */
    tag_t*      ext     /* <O>, the port back extension object */
);

/*****************************************************************************

This function sets the back extension value for a port.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_port_back_extension(
    tag_t       port,   /* <I>, the port */
    double      ext     /* <I>, the port extension */
);

/*****************************************************************************

This function sets the back extension object for a port.
The object must be a UF_scalar_type.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_port_back_extension_obj(
    tag_t       port,   /* <I>, the port */
    tag_t       ext     /* <I>, the port back extension object */
);

/*****************************************************************************

This function sets the engagement value for a port.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_port_engagement(
    tag_t       port,   /* <I>, the port */
    double      eng     /* <I>, the port engagement*/
);

/*****************************************************************************

This function sets the engagement object for a port.
The object must be a UF_scalar_type.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_port_engagement_obj(
    tag_t       port,   /* <I>, the port */
    tag_t       eng     /* <I>, the port engagement object*/
);


/*****************************************************************************

Use this function to find the ports attached to an object. The object can
be a segment, stock, port, rcp, or part. Success is indicated by a non-zero
count of ports. The function always returns ERROR_OK. The array of ports must
be freed by the user with UF_free.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_object_port(
    tag_t object,    /* <I> object */
    int *num_ports,  /* <O> count of ports */
    tag_t **ports    /* <OF,len:num_ports>
                        array of ports, this must be freed by calling
                        UF_free */
);


/*****************************************************************************

This function will provide a list of the names of all the currently loaded
bend radius tables. Use UF_free_string_array to free the array of names.
An error of UF_ROUTE_err_table_not_loaded means that there are no
tables loaded in the current application view.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_ask_loaded_bend_tables(
                int *num_tables, /* <O> number of entries */
                char ***tables    /* <OF,len:num_tables>
                                     array of table names.  This must be
                                     freed by calling UF_free_string_array */
                );

/*****************************************************************************

This function will create a bend corner at the given junction. The parameters
of the corner are gotten from the given table name and the (largest)
diameter stock at the junction. If a corner already exists, it will be removed/
modified to the new type.

Environment: Internal and External

See Also:

History: Released in V18.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_bend_by_table(
tag_t obj_id ,/* <I>
              Object identifier of an existing RCP, or a
              Bend segment or a Corner.
              */
char *table,/* <I>
              Table name to pull radius from.
              */
tag_t * corner ,/* <O>
                Object identifier of the newly created
                Corner.
                */
tag_t * seg  /* <O>
             Object identifier of the Bend corner
             segment.
             */
);

/**********************************************************************
 * Function Name: UF_ROUTE_is_stock_interior
 *
 * Function Description: This function queries a stock to see if it is
 *     "inside" any part in the current assembly.  The stock is only
 *     interior if it's segment(s) are interior to a part in the same
 *     routing level.
 *
 * Environment: Internal and External
 *
 * See Also:
 *
 * History: Released in V20
 *
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_is_stock_interior(
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
extern UFUNEXPORT int UF_ROUTE_reuse_stock_part(
    tag_t   stock   /* <I>    Tag of the stock object. */
);

/*****************************************************************************

This function is used to change the name of a stock component part.

Environment: Internal and External

See Also:

History: Released in V19.0
*****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_set_stock_part_name(
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
extern UFUNEXPORT int UF_ROUTE_ask_stock_part_occ(
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
extern UFUNEXPORT int UF_ROUTE_convert_to_stock_as_components(
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
*  UF_ROUTE_set_port_id
*
*  DESCRIPTION:
*       Used to set the unique id charx of given port.
*       Return value : 0 ==> OK, != 0 ==> Error
*                      -2 ==> Illegal object type
*                      -5 ==> Unique id charx of port assignment operation failure.
*
* Environment: Internal and External
*
* See Also:
*
* History: Released in NX
*
*/
extern UFUNEXPORT int UF_ROUTE_set_port_id (
        tag_t     obj_id,         /* <I> port object */
        char     *port_id         /* <I> unique id charx of port to be set */
);

/**********************************************************************
 * Function Name: UF_ROUTE_mig_create_multi_port
 *
 * Function Description:
 *     Create a multiport in the specified part.
 *
 * Environment: Internal
 *
 * See Also:
 *
 * History: Released in V20
 *
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_create_multiport_from_position(
    tag_t part,             /* <I> Tag of part to create port. When a NULL_TAG is passed,
                                   port will be created in current work part */
    double position[3],     /* <I> Positon of port in absolute csys */
    logical align_flag,     /* <I> Port alignment flag:
                                   TRUE = Port uses an alignment vector.
                                   FALSE = Port does not use an alignment vector. */
    double align_vector[3], /* <I> Alignment vector of port */
    logical fixture_port,   /* <I> Is the port a fixture port?
                                   TRUE = Port is a fixture port.
                                   FALSE = Port is not a fixture port.    */
    char *term_id,          /* <I> Terminal Id*/
    tag_t *port_tag         /* <O> Tag of created port*/
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

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_ROUTE_H_INCLUDED */
