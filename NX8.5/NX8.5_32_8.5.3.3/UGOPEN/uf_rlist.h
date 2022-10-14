/*******************************************************************************
                  Copyright 2007 UGS Corp.
              Unpublished - All Rights Reserved





File description:

     Open C API support for the Route List (RLIST) module.
*******************************************************************************/
#ifndef UF_RLIST_H_INCLUDED
#define UF_RLIST_H_INCLUDED


/**************
 ** Includes **
 **************/
/******************************************************************************

*******************************************************************************/

#define ERROR_RLIST_base       1945000
#include <uf_defs.h>            /* For MAX_LINE_SIZE, TRUE/FALSE, etc.*/
#include <uf_attr.h>
#include <uf_eplib_types.h>     /* Part library definitions */
#include <uf_route.h>
#include <uf_styler.h>
#include <libufun_exports.h>

#include <uf_retiring.h>

#ifdef __cplusplus
extern "C" {
#endif


/************
 ** Macros **
 ************/

/* default column width definitions for ui display of field types */
#define UF_RLIST_FLD_FMT_WIDTH_INT        4
#define UF_RLIST_FLD_FMT_WIDTH_DOUBLE     6
#define UF_RLIST_FLD_FMT_WIDTH_TAG        4
#define UF_RLIST_FLD_FMT_WIDTH_STRING     16
#define UF_RLIST_FLD_FMT_WIDTH_MAX        50    /* must remain max width */

/* strings found in the configuration file */
#define UF_RLIST_FLD_FMT_STR_INT          "integer"
#define UF_RLIST_FLD_FMT_STR_DOUBLE       "real"
#define UF_RLIST_FLD_FMT_STR_TAG          "tag"
#define UF_RLIST_FLD_FMT_STR_STRING       "string"
#define UF_RLIST_FILE_FMT_TYPE_STR_COMMA  "comma_delimited"
#define UF_RLIST_FILE_FMT_TYPE_STR_SPACE  "space_delimited"
#define UF_RLIST_FILE_FMT_TYPE_STR_STEP   "STEP"
#define UF_RLIST_FILE_FMT_TYPE_STR_XML    "XML"

/* integer values which correspond to field types
 */
#define UF_RLIST_FLD_FMT_TYPE_DOUBLE      1          /* double    */
#define UF_RLIST_FLD_FMT_TYPE_UNUSED      2          /* not used  */
#define UF_RLIST_FLD_FMT_TYPE_INT         3          /* integer   */
#define UF_RLIST_FLD_FMT_TYPE_STRING      4          /* string    */
#define UF_RLIST_FLD_FMT_TYPE_TAG         5          /* tag       */

/* smart field names */
#define UF_RLIST_UNIQUE_ID_FLD_NAME       "unique_id"
#define UF_RLIST_CONN_ID_FLD_NAME         "connector_id"
#define UF_RLIST_PART_NAME_FLD_NAME       "part_name"
#define UF_RLIST_OCCUR_FLD_NAME           "occur"
#define UF_RLIST_COMP_FLD_NAME            "comp"
#define UF_RLIST_STOCK_FLD_NAME           "stock"
#define UF_RLIST_ROUTED_FLD_NAME          "routed"
#define UF_RLIST_ROUTED_LEVEL_FLD_NAME    "routed_level"
#define UF_RLIST_FROM_COMP_FLD_NAME       "from_comp"
#define UF_RLIST_FROM_CONN_FLD_NAME       "from_conn"
#define UF_RLIST_FROM_PORT_FLD_NAME       "from_port"
#define UF_RLIST_TO_COMP_FLD_NAME         "to_comp"
#define UF_RLIST_TO_CONN_FLD_NAME         "to_conn"
#define UF_RLIST_TO_PORT_FLD_NAME         "to_port"
#define UF_RLIST_LENGTH_FLD_NAME          "length"
#define UF_RLIST_ROUTE_FLD_NAME           "route"
#define UF_RLIST_FABRICATION_FLD_NAME     "fabrication"
#define UF_RLIST_CUT_LENGTH_FLD_NAME      "cut_length"
#define UF_RLIST_MULTIPLIER_FLD_NAME      "multiplier"
#define UF_RLIST_OFFSET_FLD_NAME          "offset"
#define UF_RLIST_OD_FLD_NAME              "od"
#define UF_RLIST_WIDTH_FLD_NAME           "width"
#define UF_RLIST_HEIGHT_FLD_NAME          "height"
#define UF_RLIST_COV_THK_FLD_NAME         "cover_thickness"
#define UF_RLIST_STOCK_DATA_FLD_NAME      "stock_data"
#define UF_RLIST_WIRE_SPACE_FLD_NAME      "wire_spacing"
#define UF_RLIST_CABLE_FLD_NAME           "cable_id"
#define UF_RLIST_CABLE_LOCATION_FLD_NAME  "cable_location"
#define UF_RLIST_ROUTE_WIRE_TYPE_FLD_NAME "route_wire_type"
#define UF_RLIST_CONN_TYPE                "conn_type"
#define UF_RLIST_COMP_TYPE                "comp_type"
#define UF_RLIST_CROSS_SECTION_TYPE       "cross_section"
#define UF_RLIST_WIZ_RECORD_FLD_NAME      "wizard_record"
#define UF_RLIST_PARENT_RECORD_FLD_NAME   "parent_record"
#define UF_RLIST_ROUTE_CABLE_FLD_NAME     "route_cable"
#define UF_RLIST_NUM_INT_COMPS_FLD_NAME   "num_int_comps"
#define UF_RLIST_SYSTEM_FLD_NAME          "system_level"
#define UF_RLIST_CONDUIT_PART_NUMBER_FLD_NAME      "conduit_part_number"

/* smart field defaults */
#define UF_RLIST_UNIQUE_ID_DEFAULT        ""
#define UF_RLIST_CONN_ID_DEFAULT          ""
#define UF_RLIST_PART_NAME_DEFAULT        ""
#define UF_RLIST_OCCUR_DEFAULT            UF_RLIST_OCCUR_FALSE
#define UF_RLIST_COMP_DEFAULT             NULL
#define UF_RLIST_STOCK_DEFAULT            NULL
#define UF_RLIST_ROUTED_DEFAULT           UF_RLIST_ROUTED_FALSE
#define UF_RLIST_ROUTED_LEVEL_DEFAULT     ""
#define UF_RLIST_FROM_COMP_DEFAULT        ""
#define UF_RLIST_FROM_CONN_DEFAULT        ""
#define UF_RLIST_FROM_PORT_DEFAULT        ""
#define UF_RLIST_TO_COMP_DEFAULT          ""
#define UF_RLIST_TO_CONN_DEFAULT          ""
#define UF_RLIST_TO_PORT_DEFAULT          ""
#define UF_RLIST_LENGTH_DEFAULT           0.0
#define UF_RLIST_ROUTE_DEFAULT            NULL
#define UF_RLIST_FABRICATION_DEFAULT      ""
#define UF_RLIST_CUT_LENGTH_DEFAULT       0.0
#define UF_RLIST_MULTIPLIER_DEFAULT       1.0
#define UF_RLIST_OFFSET_DEFAULT           0.0
#define UF_RLIST_OD_DEFAULT               0.0
#define UF_RLIST_WIDTH_DEFAULT            0.0
#define UF_RLIST_HEIGHT_DEFAULT           0.0
#define UF_RLIST_COV_THK_DEFAULT          0.0
#define UF_RLIST_WIRE_SPACE_DEFAULT       0.0
#define UF_RLIST_CABLE_DEFAULT            ""
#define UF_RLIST_CABLE_LENGTH_DEFAULT     0.0
#define UF_RLIST_ROUTE_WIRE_TYPE_DEFAULT  ""
#define UF_RLIST_TYPE_DEFAULT             0
#define UF_RLIST_CROSS_SECTION_DEFAULT    0
#define UF_RLIST_WIZ_RECORD_DEFAULT       0
#define UF_RLIST_NUM_INT_COMPS_DEFAULT    0
#define UF_RLIST_CONDUIT_PART_NUMBER_DEFAULT      ""

/* smart field values */
#define UF_RLIST_OCCUR_TRUE               "Y"
#define UF_RLIST_OCCUR_FALSE              "N"
#define UF_RLIST_OCCUR_AUTO               "A"
#define UF_RLIST_OCCUR_MANUAL             "M"
#define UF_RLIST_OCCUR_PROXY              "P"

#define UF_RLIST_ROUTED_AUTO              "A"
#define UF_RLIST_ROUTED_MANUAL            "M"
#define UF_RLIST_ROUTED_TRUE              "Y"
#define UF_RLIST_ROUTED_FALSE             "N"
#define UF_RLIST_ROUTED_COMPONENT         "C"
#define UF_RLIST_ROUTED_PIN               "P"
#define UF_RLIST_ROUTED_MIXED             "M"
#define UF_RLIST_ROUTED_PARTIAL           "PARTIAL"

/* Types of wires */
#define UF_RLIST_NORMAL_WIRE_TYPE         ""
#define UF_RLIST_JUMPER_WIRE_TYPE         "JUMPER"

/* Route List system defined but not updated fields */
#define UF_RLIST_COMP_NAME_FLD_NAME       "comp_name"
#define UF_RLIST_NAME_FLD_NAME            "name"
#define UF_RLIST_PART_NUMBER_FLD_NAME     "part_number"
#define UF_RLIST_COLOR_FLD_NAME           "color"
#define UF_RLIST_COLOR_RGB_FLD_NAME       "color_rgb"
#define UF_RLIST_GAUGE_FLD_NAME           "gauge"
#define UF_RLIST_WIRE_CLASS_FLD_NAME      "class"
#define UF_RLIST_WIRE_TYPE_FLD_NAME       "type"
#define UF_RLIST_CABLE_TYPE_FLD_NAME      "cable_type"
#define UF_RLIST_INT_COMP_FLD_NAME        "intermed_comp"    /* base  name, ex., intermed_comp_1*/
#define UF_RLIST_INT_CONN_FLD_NAME        "intermed_conn"    /* base  name, ex., intermed_conn_1*/
#define UF_RLIST_INT_PORT_FLD_NAME        "intermed_pin"     /* base name, ex., intermed_pin_1 */
#define UF_RLIST_MATERIAL_NAME_FLD_NAME   "material_name"
#define UF_RLIST_MATERIAL_TYPE_FLD_NAME   "material_type"
#define UF_RLIST_LINEAR_DENSITY_FLD_NAME  "linear_density"
#define UF_RLIST_MIN_LEN_ALLOWED_FLD_NAME "min_len_allowed"
#define UF_RLIST_MAX_LEN_ALLOWED_FLD_NAME "max_len_allowed"
#define UF_RLIST_MIN_BEND_RAD_FLD_NAME    "min_bend_rad"
#define UF_RLIST_SHIELDING_FLD_NAME       "shielding"
#define UF_RLIST_SPACING_FLD_NAME         "spacing"
#define UF_RLIST_SIGNAL_FLD_NAME          "signal"
#define UF_RLIST_SEPARATION_FLD_NAME      "separation"
#define UF_RLIST_LOCATION_FLD_NAME        "location"
#define UF_RLIST_RECORD_GUID_FLD_NAME     "RECORD_GUID"
#define UF_RLIST_CONDUCTOR_GUID_FLD_NAME  "CONDUCTOR_GUID"
#define UF_RLIST_REFERENCED_DEVICE_GUID_FLD_NAME  "REFERENCED_DEVICE_GUID"
#define UF_RLIST_ELEC_COMP_GUID_FLD_NAME  "ELECTRICAL_COMPONENT_GUID"
#define UF_RLIST_PRODUCT_ID_FLD_NAME      "product_id"
#define UF_RLIST_MATCH_STRING_FLD_NAME    "attribute_match_string"

/***********************************************************************/
/*  load mask options for UF_RLIST_load_objects and UF_RLIST_load_file_formats */
/***********************************************************************/

/* load objects that have to do with the connection and/or component list */
#define UF_RLIST_LOAD_CONN_LIST_TYPE            ( 1 << 1 )
#define UF_RLIST_LOAD_COMP_LIST_TYPE            ( 1 << 2 )
#define UF_RLIST_LOAD_ALL_LIST_TYPE             ( UF_RLIST_LOAD_CONN_LIST_TYPE | \
                                         UF_RLIST_LOAD_COMP_LIST_TYPE )

/*  UF_RLIST_LOAD_xxx_OBJS options should be specified
    together with LOAD_CONN_LIST_TYPE and/or LOAD_COMP_LIST_TYPE or
    LOAD_ALL_LIST_TYPE
*/

/* For the given list(s), load these objects: */
#define UF_RLIST_LOAD_LIST_OBJS                 ( 1 << 3 )
#define UF_RLIST_LOAD_FORMAT_OBJS               ( 1 << 4 )
#define UF_RLIST_LOAD_FILTER_OBJS               ( 1 << 5 )
#define UF_RLIST_LOAD_ALL_OBJS                  ( UF_RLIST_LOAD_ALL_LIST_TYPE  | \
                                         UF_RLIST_LOAD_LIST_OBJS      | \
                                         UF_RLIST_LOAD_FORMAT_OBJS    | \
                                         UF_RLIST_LOAD_FILTER_OBJS )


/* string definitions for characteristic names */
#define UF_RLIST_COMP_ID_CHARX_TITLE      "UNIQUE_ID"
#define UF_RLIST_PORT_ID_CHARX_TITLE      "UNIQUE_ID"

/* string definitions for internal table field types */
#define UF_RLIST_FLD_FMT_TBL_INT          "%3d"
#define UF_RLIST_FLD_FMT_TBL_DOUBLE       "%6.2d"
#define UF_RLIST_FLD_FMT_TBL_TAG          "%8d"
#define UF_RLIST_FLD_FMT_TBL_STRING       "%-10.10s"

#define UF_RLIST_CONN_LIST_TYPE           1    /* add new list types above    */
#define UF_RLIST_COMP_LIST_TYPE           2    /* UF_RLIST_COMP_LIST_TYPE.    */
                                               /* It must remain largest type */
#define UF_RLIST_MAX_LIST_TYPE            2    /* due to RLIST_MAX_LIST_TYPE. */

#define UF_RLIST_CFG_FILE_EXTENSION       ".cfg"
#define UF_RLIST_HRN_FILE_EXTENSION       ".hrn"
#define UF_RLIST_CMP_FILE_EXTENSION       ".cmp"
#define UF_RLIST_XML_FILE_EXTENSION       ".xml"

#define UF_RLIST_RECORD_IMPORT_REPLACE    0    /* must remain in the order    */
#define UF_RLIST_RECORD_IMPORT_UNIQUE     1    /* as displayed on the user    */
#define UF_RLIST_RECORD_IMPORT_ALL        2    /* interface button layout     */
#define UF_RLIST_RECORD_EXPORT_SELECTED   3    /* options.                    */
#define UF_RLIST_RECORD_EXPORT_ALL        4

#define UF_RLIST_FILE_FMT_TYPE_COMMA      1
#define UF_RLIST_FILE_FMT_TYPE_SPACE      2
#define UF_RLIST_FILE_FMT_TYPE_STEP       3
#define UF_RLIST_FILE_FMT_TYPE_XML        4

/* format field manipulation   */
#define UF_RLIST_FLD_MOVE_NOWHERE         0
#define UF_RLIST_FLD_MOVE_LEFT            1
#define UF_RLIST_FLD_MOVE_RIGHT           2

#define UF_RLIST_SELECTED                 0
#define UF_RLIST_ALL_ROUTED               1
#define UF_RLIST_ALL_UNROUTED             2
#define UF_RLIST_ROUTING_DESIGN           3


#define UF_RLIST_ALL_TYPES                0
#define UF_RLIST_SPECIFIED_TYPES          1

#define UF_RLIST_BLANK                    0
#define UF_RLIST_UNBLANK                  1

#define UF_RLIST_MULTIPORT_DETAIL         0
#define UF_RLIST_TERMINALS_DETAIL         1
#define UF_RLIST_COMPONENT_DETAIL         2
#define UF_RLIST_MIXED_DETAIL             3
#define UF_RLIST_PARTIAL_DETAIL           4

#define UF_RLIST_CREATE_TERMINALS         "Create Terminals"
#define UF_RLIST_DEFAULT_HRN_NAME         "Default Harness Name"
#define UF_RLIST_HRN_OVERRIDE             "Override Harness Field"
#define UF_RLIST_RPT_ROUTE_ERRS           "Report Routing Errors"
#define UF_RLIST_HIGHLIGHT_WIRE_STOCK     "Highlight Wire Stock"
#define UF_RLIST_COMP_MATCH_ATTRIBUTE     "Component Match Attribute"
#define UF_RLIST_COMP_MATCH_METHOD        "Component Match Method"
#define UF_RLIST_DEFAULT_JUMPER_LEN       "Default Jumper Length"

#define UF_RLIST_ASCENDING_SORT           1
#define UF_RLIST_DESCENDING_SORT          -1


/*****************
 ** Error codes **
 *****************/
#define UF_RLIST_ERROR_BASE                    ERROR_RLIST_base
#define UF_RLIST_err_alloc_dup_fld             ERROR_RLIST_base + 1
#define UF_RLIST_err_invalid_col_order         ERROR_RLIST_base + 2
#define UF_RLIST_err_invalid_sort_order        ERROR_RLIST_base + 3
#define UF_RLIST_err_invalid_col_width         ERROR_RLIST_base + 4
#define UF_RLIST_err_dup_fld_name              ERROR_RLIST_base + 5
#define UF_RLIST_err_dup_col_order             ERROR_RLIST_base + 6
#define UF_RLIST_err_dup_sort_order            ERROR_RLIST_base + 7
#define UF_RLIST_err_array_len_mismatch        ERROR_RLIST_base + 8
#define UF_RLIST_err_invalid_name              ERROR_RLIST_base + 9
#define UF_RLIST_err_invalid_type              ERROR_RLIST_base + 10
#define UF_RLIST_err_dup_conn_list             ERROR_RLIST_base + 11
#define UF_RLIST_err_dup_comp_list             ERROR_RLIST_base + 12
#define UF_RLIST_err_dup_filter                ERROR_RLIST_base + 13
#define UF_RLIST_err_dup_fmt_fld               ERROR_RLIST_base + 14
#define UF_RLIST_err_dup_format                ERROR_RLIST_base + 15
#define UF_RLIST_err_no_name_or_clause         ERROR_RLIST_base + 16
#define UF_RLIST_err_invalid_num_parms         ERROR_RLIST_base + 17
#define UF_RLIST_err_invalid_sec_line          ERROR_RLIST_base + 18
#define UF_RLIST_err_invalid_file_type         ERROR_RLIST_base + 19
#define UF_RLIST_err_invalid_filt_clause       ERROR_RLIST_base + 20
#define UF_RLIST_err_invalid_fmt_fld           ERROR_RLIST_base + 21
#define UF_RLIST_err_no_list_section           ERROR_RLIST_base + 22
#define UF_RLIST_err_invalid_list_line         ERROR_RLIST_base + 23
#define UF_RLIST_err_bad_record_format         ERROR_RLIST_base + 24
#define UF_RLIST_err_list_and_cfg_file         ERROR_RLIST_base + 25
#define UF_RLIST_err_multiple_lists            ERROR_RLIST_base + 26
#define UF_RLIST_err_opening_file              ERROR_RLIST_base + 27
#define UF_RLIST_err_assign_comp_to_list       ERROR_RLIST_base + 28
#define UF_RLIST_err_comp_assigned             ERROR_RLIST_base + 29
#define UF_RLIST_err_no_unique_id              ERROR_RLIST_base + 30
#define UF_RLIST_err_acomp_missing_in_prt      ERROR_RLIST_base + 31
#define UF_RLIST_err_comp_missing_in_prt       ERROR_RLIST_base + 32
#define UF_RLIST_err_acomp_uid_mismatch        ERROR_RLIST_base + 33
#define UF_RLIST_err_comp_missing_info         ERROR_RLIST_base + 34
#define UF_RLIST_err_acomp_part_mismatch       ERROR_RLIST_base + 35
#define UF_RLIST_err_acomp_duplicate_uids      ERROR_RLIST_base + 36
#define UF_RLIST_err_acomp_blanked             ERROR_RLIST_base + 37
#define UF_RLIST_err_acomp_empty_refset        ERROR_RLIST_base + 38
#define UF_RLIST_err_acomp_missing_in_list     ERROR_RLIST_base + 39
#define UF_RLIST_err_conn_missing_info         ERROR_RLIST_base + 40
#define UF_RLIST_err_conn_invalid_route        ERROR_RLIST_base + 41
#define UF_RLIST_err_conn_stock_mismatch       ERROR_RLIST_base + 42
#define UF_RLIST_err_conn_length_mismatch      ERROR_RLIST_base + 43
#define UF_RLIST_err_conn_harness_mismatch     ERROR_RLIST_base + 44
#define UF_RLIST_err_conn_invalid_tag          ERROR_RLIST_base + 45
#define UF_RLIST_err_manual_route_exists       ERROR_RLIST_base + 46
#define UF_RLIST_err_path_not_found            ERROR_RLIST_base + 48
#define UF_RLIST_err_sdata_not_found           ERROR_RLIST_base + 49
#define UF_RLIST_err_unq_path_not_found        ERROR_RLIST_base + 50
#define UF_RLIST_err_invalid_stock_style       ERROR_RLIST_base + 51
#define UF_RLIST_err_auto_route_error          ERROR_RLIST_base + 52
#define UF_RLIST_err_unroute_error             ERROR_RLIST_base + 53
#define UF_RLIST_err_manual_route_error        ERROR_RLIST_base + 55
#define UF_RLIST_err_acomp_not_loaded          ERROR_RLIST_base + 56
#define UF_RLIST_err_bad_cfg_file              ERROR_RLIST_base + 57
#define UF_RLIST_err_broken_loop               ERROR_RLIST_base + 58
#define UF_RLIST_err_no_route_list_fmt         ERROR_RLIST_base + 59
#define UF_RLIST_err_load_xml_routelist        ERROR_RLIST_base + 60
#define UF_RLIST_err_write_xml_routelist       ERROR_RLIST_base + 61
#define UF_RLIST_err_write_xml_filters         ERROR_RLIST_base + 62
#define UF_RLIST_err_invalid_int_comps         ERROR_RLIST_base + 63
#define UF_RLIST_err_no_path_thru_int_comps    ERROR_RLIST_base + 64
#define UF_RLIST_err_cannot_create_list_record ERROR_RLIST_base + 65
#define UF_RLIST_err_dup_unique_ids            ERROR_RLIST_base + 66
#define UF_RLIST_err_dup_wire_ids              ERROR_RLIST_base + 67
#define UF_RLIST_err_fmbd_dup_unique_ids       ERROR_RLIST_base + 68
#define UF_RLIST_err_fmbd_dup_wire_ids         ERROR_RLIST_base + 69
#define UF_RLIST_err_from_comps_not_found      ERROR_RLIST_base + 70
#define UF_RLIST_err_to_comps_not_found        ERROR_RLIST_base + 71
#define UF_RLIST_err_from_ports_not_found      ERROR_RLIST_base + 72
#define UF_RLIST_err_to_ports_not_found        ERROR_RLIST_base + 73
#define UF_RLIST_err_from_port_has_connection  ERROR_RLIST_base + 74
#define UF_RLIST_err_to_port_has_connection    ERROR_RLIST_base + 75
#define UF_RLIST_err_path_seg_locked_fill_percen_reached ERROR_RLIST_base + 76
#define UF_RLIST_err_path_seg_invalid_fill_percen ERROR_RLIST_base + 77
#define UF_RLIST_err_max_error                 ERROR_RLIST_base + 77

/**************************
 ** Structures and Types **
 **************************/
/***************************************************************************
 * The following typedefs are pointers to internal structures.             *
 * The structures themselves are not accessible to the Open API programmer. *
 * Structure member access is provided by set and ask routines             *
 ***************************************************************************/
typedef struct
    RLIST_list_field_s  UF_RLIST_list_field_t, *UF_RLIST_list_field_p_t;
typedef struct
    RLIST_fld_map_s     UF_RLIST_fld_map_t,    *UF_RLIST_fld_map_p_t;
typedef struct
    RLIST_flt_map_s     UF_RLIST_flt_map_t,    *UF_RLIST_flt_map_p_t;
typedef struct
    RLIST_file_fmt_s    UF_RLIST_file_fmt_t,   *UF_RLIST_file_fmt_p_t;
typedef struct
    RLIST_config_s      UF_RLIST_config_t,     *UF_RLIST_config_p_t;
typedef struct
    RLIST_error_item_s  UF_RLIST_error_item_t, *UF_RLIST_error_item_p_t;
typedef struct
    RLIST_error_s       UF_RLIST_error_t,      *UF_RLIST_error_p_t;

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RLIST_H_INCLUDED */
