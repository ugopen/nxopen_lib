/*==============================================================================

        Copyright 1994 Siemens Product Lifecycle Management Software Inc.
                       Unpublished - All rights reserved

================================================================================

 * 


File Description:
  Open C API typedefs and defines for the UF_PART module
 ***************************************************************************/

#ifndef UF_PART_TYPES_INCLUDED
#define UF_PART_TYPES_INCLUDED


/***************************************************************************

  ***************************************************************************/


#include <uf_defs.h>


#ifdef __cplusplus
extern "C" {
#endif

/*
 * UF_PART error and warning codes.
 */
#define ERROR_PART_base     640000
#define UF_PART_ERROR_BASE                 (ERROR_PART_base)

#define UF_PART_warn_objects_not_copied  (UF_PART_ERROR_BASE + 1075)
#define UF_PART_err_read_only_modified  (UF_PART_ERROR_BASE + 1058)

/*
 * Data structure to return the part names and statuses of all parts retrieved
 * into the session by either
 *      UF_PART_open   or
 *      UF_ASSEM_add_part_to_assembly
 *
 * Starting NX3: The utility routine UF_PART_free_load_status has been provided
 * to free the allocated memory below. This may be used as an alternative to
 * calling UF_free_string_array and UF_free directly.
 */

struct UF_PART_load_status_s
  { logical failed;         /* Output: True if the load failed and was
                            rolled back
                            */
    logical user_abort;     /* Output: True if the only 'failure' was user abort
                            */
    int     n_parts;        /* Output: Length of the following two
                            allocated arrays. Number of parts that had
                            errors or warnings when loading. This is the
                            number (dimension) of entries in the file_names
                            and statuses arrays.
                            */
    char  **file_names;     /* <OF,len:n_parts,free:UF_free_string_array>
                            Allocated array of file names
                            */
    int    *statuses;       /* <OF,len:n_parts>
                            Allocated array of associated status codes
                            for each file name. Use UF_get_fail_message
                            on each status code in the array to get
                            the associated message string.
                            The allocated array must be freed.
                            */
  };

typedef struct UF_PART_load_status_s UF_PART_load_status_t,
                                    *UF_PART_load_status_p_t;
/*
 *  Data structure and constants used in part import
 *  History:
 *     NX2: plist_mode is no longer used.
 */
struct UF_import_part_modes_s
    {
    int      layer_mode;   /* 0 = Merge on work layer
                              1 = Merge on original layers
                           */
    int      group_mode;   /* 0 = Merge ungrouped
                              1 = Merge grouped
                           */
    int      csys_mode;    /* Not used by Open API applications */

    int      plist_mode;   /* NOTE: plist_mode is no longer used */

    int      view_mode;    /* 0 = do not retrieve views and layouts.
                              1 = retrieve views and layouts.
                           */
    logical  cam_mode;     /* If true, merge in tools and parameter
                              sets, if false do not.
                           */
    logical  use_search_dirs; /* This is not used by Open API applications. */
    };

typedef struct UF_import_part_modes_s UF_import_part_modes_t,
                                     *UF_import_part_modes_p_t;

/*
 *  Data structure used by the part history routines
 */

typedef struct UF_PART_history_list_s *UF_PART_history_list_p_t;

#define  IP_WORK        0
#define  IP_ORIG        1

#define  IP_NOGROUP     0
#define  IP_GROUP       1

#define  IP_USE_WCS     0
#define  IP_CSYS_MENU   1

#define  IP_NONE        0
#define  IP_FORMAT      1
#define  IP_ADD_TO      2
#define  IP_ALL         3

#define  IP_NO_VIEW     0
#define  IP_VIEW        1


#define  UF_PART_METRIC    1
#define  UF_PART_ENGLISH   2

#define  UF_PART_CDP_BEGIN_TEXT    0
#define  UF_PART_CDP_END_TEXT      1
#define  UF_PART_CDP_CONTAIN_TEXT  2
#define  UF_PART_CDP_EXACT_TEXT    3

/*****************************************************************************
 *
 * Type which describes how solid parameters should be processed during
 * an export operation,
 * NOTE: UF_PART_maintain_all_params is a newly introduced option in V15.0.
 *
 *       The behaviours of UF_PART_maintain_params and UF_PART_remove_params
 *       are the same in V15.0 as in earlier releases.
 *
 ******************************************************************************/
enum UF_PART_export_params_mode_e
{
    UF_PART_maintain_params, /* Solid parameters should be maintained
                             during the export operation.  Note that
                             with this option, solid parameters will
                             NOT be copied if they depend upon other
                             objects for their validity unless those
                             other objects are going to be copied
                             anyway.
                             */
    UF_PART_remove_params, /* Solid parameters will be removed during
                           the export operation.  Solids copied
                           into the destination part will have no
                           solid parameters.
                           */
    UF_PART_maintain_all_params /* All solid parameters should be
                                maintained during the export
                                operation.  All solid parameters in
                                the source objects will be copied into
                                the destination objects.  Note that
                                extra objects which are required to
                                maintain the validity of the
                                parameters will be copied too.
                                */
};

typedef enum UF_PART_export_params_mode_e UF_PART_export_params_mode_t,
                                         *UF_PART_export_params_mode_p_t;
/*****************************************************************************
 *
 * Type which describes how expressions should be processed during an
 * export operation:
 ******************************************************************************/
enum UF_PART_export_exp_mode_e
{
    UF_PART_copy_exp_deeply, /*Expressions will be copied deeply.
                               If an expression references another
                               expression in the same part, then
                               that referenced expression will also
                               be copied.  (However any referenced
                               expressions in a different part will
                               not be copied.)
                             */
    UF_PART_copy_exp_shallowly /*Expressions will be copied shallowly.
                                 If an expression references another
                                 expression, the copy of the
                                 referencing expression will reference
                                 the same referenced expression.  This
                                 happens for both inter-part and
                                 intra-part references to expressions.
                               */
} ;

typedef enum UF_PART_export_exp_mode_e UF_PART_export_exp_mode_t,
                                      *UF_PART_export_exp_mode_p_t;
/*****************************************************************************
 *
 * Type which describes the options provided to an export operation.
 ******************************************************************************/
struct UF_PART_export_options_s
{
    logical new_part; /* Determines whether the objects should be exported
                         into a new part.
                      */
    UF_PART_export_params_mode_t params_mode; /* Determines how solid
                                                 parameters will be copied.
                                              */
    UF_PART_export_exp_mode_t expression_mode; /* Determines how expressions
                                                  will be copied.
                                               */
};

typedef struct UF_PART_export_options_s UF_PART_export_options_t,
                                       *UF_PART_export_options_p_t;
/*****************************************************************************
 *
 * Type which describes the compression options available
 ******************************************************************************/
struct UF_PART_compress_flags_s
{
    logical standard; /* Specifies the standard compression option state
                      */
};

typedef struct UF_PART_compress_flags_s UF_PART_compress_flags_t,
                                       *UF_PART_compress_flags_p_t;


/*
    Search types for UF_PART_cdp_params_t
*/
#define UF_PART_CDP_BEGIN_TEXT      0
#define UF_PART_CDP_END_TEXT        1
#define UF_PART_CDP_CONTAIN_TEXT    2
#define UF_PART_CDP_EXACT_TEXT      3


#define UF_PART_cleanup_highlight          (1U <<  0)
#define UF_PART_cleanup_all_groups         (1U <<  1)
#define UF_PART_cleanup_unnamed_groups     (1U <<  2)
#define UF_PART_cleanup_unreferenced       (1U <<  3)
#define UF_PART_cleanup_feature            (1U <<  4)
#define UF_PART_cleanup_parts_all          (1U <<  5)
#define UF_PART_cleanup_parts_components   (1U <<  6)
#define UF_PART_cleanup_spreadsheet        (1U <<  7)
#define UF_PART_cleanup_mating             (1U <<  8)  /* Note: This operation may load parts */
#define UF_PART_cleanup_CAM_cleanup        (1U <<  9)
#define UF_PART_cleanup_fonts              (1U <<  10)
#define UF_PART_cleanup_unreferenced_exps  (1U <<  11)
#define UF_PART_cleanup_occurrences        (1U <<  12)
#define UF_PART_cleanup_visual_editor      (1U <<  13)
#define UF_PART_cleanup_hwo_force_demoting (1U <<  14) /* Beware that if both UF_PART_cleanup_hwo_force_demoting *
                                                        * and UF_PART_cleanup_occurrences are specified, then    *
                                                        * UF_PART_cleanup_occurrences takes precedence.          */
#define UF_PART_cleanup_drafting           (1U <<  15)
#define UF_PART_cleanup_sketch             (1U <<  16)

#define UF_PART_cleanup_delete_broken_interpart   (1U <<  17)
#define UF_PART_cleanup_delete_all_materials      (1U <<  18)
#define UF_PART_cleanup_assembly_constraints      (1U <<  19)
#define UF_PART_cleanup_delete_duplicate_lights   (1U <<  20)
#define UF_PART_cleanup_routing                   (1U <<  21)
#define UF_PART_cleanup_delete_invalid_attributes (1U <<  22)

#define UF_PART_cleanup_all                ((~0U) & (~UF_PART_cleanup_sketch))

#ifdef __cplusplus
}
#endif

#endif /* UF_PART_TYPES_INCLUDED */

