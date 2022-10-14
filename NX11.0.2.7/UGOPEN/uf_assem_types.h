/*******************************************************************************

               Copyright (c) 2000-2004 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved


 *

 ****************************************************************************/


#ifndef UF_ASSEM_TYPES_INCLUDED
#define UF_ASSEM_TYPES_INCLUDED

/***************************************************************************

  ***************************************************************************/


#include <uf_defs.h>
#include <uf_fam_types.h>

#ifdef __cplusplus
extern "C" {
#endif


#define UF_ASSEM_load_from_directory    0
#define UF_ASSEM_load_from_search_dirs  1
#define UF_ASSEM_load_as_saved          2

#define UF_ASSEM_managed_load_by_revision_rule    1
#define UF_ASSEM_managed_load_as_saved            2

#define UF_ASSEM_do_not_add_components  0
#define UF_ASSEM_add_single_level       1
#define UF_ASSEM_add_all_levels         2

#define UF_ASSEM_no_update_report       1
#define UF_ASSEM_update_report          2

#define UF_ASSEM_do_not_emphasize_wp    1
#define UF_ASSEM_emphasize_wp           2

#define UF_ASSEM_do_abort_on_failure    0
#define UF_ASSEM_dont_abort_on_failure  1

#define UF_ASSEM_dont_maintain_work_part 0
#define UF_ASSEM_do_maintain_work_part  1

#define UF_ASSEM_load_exact_version     0
#define UF_ASSEM_load_latest_version    1

#define UF_ASSEM_dont_load_components   0
#define UF_ASSEM_do_load_components     1
#define UF_ASSEM_use_last_component_set 2
#define UF_ASSEM_specify_filter         4 /*This option is only valid for internal programs. */

/*
    New options for v10.4. For earlier versions, the default behaviour
    was 0 (load components partially)
*/

#define UF_ASSEM_load_components_partially 0
#define UF_ASSEM_load_components_fully     1

/* 
    New options for NX7.5 to determine whether lightweight representations is on or off.
    The default behavior is 0 i.e. don't allow lightweight representations
*/
#define UF_ASSEM_do_allow_lightweight_representations    1
#define UF_ASSEM_dont_allow_lightweight_representations  0

/*
    New option for auto regenerating missing part family members during
    the load of the assembly. The default behaviour is 1  i.e. to auto
    regenerate the missing part family members
*/
#define UF_ASSEM_dont_auto_generate_pfm    0
#define UF_ASSEM_auto_generate_pfm         1

#define UF_ASSEM_dont_allow_substitution   0
#define UF_ASSEM_do_allow_substitution     1

#define UF_ASSEM_dont_apply_to_all_levels  0
#define UF_ASSEM_do_apply_to_all_levels    1

/*
    New option for V14.0, load WAVE data, comes into effect if partial loading
    is enabled.

    UF_ASSEM_default_load_behaviour        - No special processing of Wave data
                                             or parents
    UF_ASSEM_load_wave_data                - Load weave data and parents as
                                             controlled by load_wave_parents
    UF_ASSEM_none                          - Don't load unlaoded parents, but
                                             ensure partially loaded parents
                                             are fully loaded
    UF_ASSEM_immediate                     - Load immediate parents of any WAVE
                                             data
    UF_ASSEM_all                           - Load parents of WAVE data, and
                                             parents of that, until no parents
                                             can be found
*/

#define UF_ASSEM_default_load_behaviour    0
#define UF_ASSEM_load_wave_data            1

#define UF_ASSEM_none                      0
#define UF_ASSEM_immediate                 1
#define UF_ASSEM_all                       2

/***************************************************************
 *  History:
 *     NX2: parts_list is no longer used.
 *     NX8.5: managed_mode_load_options introduced.
 ***************************************************************/
struct UF_ASSEM_options_s
{
    int load_options;          /* Load Options - for native mode only
                                     UF_ASSEM_load_from_directory
                                     UF_ASSEM_load_from_search_dirs
                                     UF_ASSEM_load_as_saved
                               */

    int parts_list;            /* NOTE: parts_list is no longer used */

    int update;                /*Update report setting -
                                    UF_ASSEM_no_update_report
                                    UF_ASSEM_update_report
                               */
    int emphasize;             /*Emphasize setting -
                                    UF_ASSEM_do_not_emphasize_wp
                                    UF_ASSEM_emphasize_wp
                               */
    int emphasize_color;       /* NOTE: emphasize_color is no longer used */

    int failure_action;        /* failure Option value -  
                                    UF_ASSEM_do_abort_on_failure
                                    UF_ASSEM_dont_abort_on_failure
                               */
    int maintain_work_part;    /* Option to apply to the work part when 
                                  changing the displayed part interactively:
                                    UF_ASSEM_dont_maintain_work_part 
                                       Work part set to be displayed part after
                                       a Change Displayed Part operation.
                                    UF_ASSEM_do_maintain_work_part 
                                       Work part unchanged after a Change 
                                       Displayed Part operation, provided that
                                       the work part is under the new displayed
                                       part, and has the same units as the new
                                       displayed part.
                               */

    int load_latest;           /* Load latest version switch  
                                    UF_ASSEM_load_exact_version
                                    UF_ASSEM_load_latest_version
                               */
    int load_components;       /* Load components option     
                                    UF_ASSEM_dont_load_components
                                    UF_ASSEM_do_load_components
                                    UF_ASSEM_use_last_component_set
                                    UF_ASSEM_use_last_filter
                                    UF_ASSEM_specify_filter
                               */
    int load_fully;            /* Full load switch
                                    UF_ASSEM_load_components_partially
                                    UF_ASSEM_load_components_fully
                               */
    int use_lightweight_representations; /* Lightweight Representations option
                                    UF_ASSEM_do_allow_lightweight_representations
                                    UF_ASSEM_dont_allow_lightweight_representations
                                 */
    int load_substitution;     /* Allow Substitution switch
                                    UF_ASSEM_dont_allow_substitution
                                    UF_ASSEM_do_allow_substitution
                               */
    int apply_to_all_levels;   /* Apply reference set defaults to all levels
                                    UF_ASSEM_dont_apply_to_all_levels
                                    UF_ASSEM_do_apply_to_all_levels
                                  prior to V13, the behavior was
                                  UF_ASSEM_dont_apply_to_all_levels.
                               */
    int load_wave_data;        /* New option for V14, if load_fully is set to
                                  UF_ASSEM_load_components_partially then
                                  this allows for components with WAVE data
                                  in them to be fully loaded. Other components
                                  will still be partially loaded.
                                    UF_ASSEM_default_load_behaviour
                                    UF_ASSEM_load_wave_data
                               */
    int load_wave_parents;     /* Load Unloaded Wave Parents option.  This
                                  field is only used if load_wave_data is set
                                  to UF_ASSEM_load_wave_data.  When it is, this
                                  value controls the way in which parents of
                                  wave geometry are loaded:
                                    UF_ASSEM_none - Don't load unloaded parents,
                                                    but ensure partially loaded
                                                    parents are fully loaded.
                                    UF_ASSEM_immediate - Load immediate parents
                                                         of any WAVE data.
                                    UF_ASSEM_all - Load parents of WAVE data,
                                                   and their parents, until no
                                                   parents can be found.

                                  A parent part is one which contains geometry
                                  that is linked to another part.  If part A
                                  has a LINKED_BODY which references geometry
                                  in part B, then set the load options as
                                  follows:
                                    load_wave_data = UF_ASSEM_load_wave_data
                                    load_wave_parents = UF_ASSEM_immediate
                                  If you load part A, then part B is loaded.
                               */

    int auto_regen_pfm_option; /* Auto regenerate missing part family children
                                  option. If this option is set to
                                  UF_ASSEM_auto_generate_pfm then while loading
                                  assemblies, any missing part family members
                                  will be automatically regenerated.
                                  The valid options are:
                                  UF_ASSEM_auto_generate_pfm
                                  UF_ASSEM_dont_auto_generate_pfm
                               */
    int managed_mode_load_options;  /* Load Options - for managed mode only
                                          UF_ASSEM_managed_load_by_revision_rule
                                          UF_ASSEM_managed_load_as_saved 
                                    */
};

typedef struct UF_ASSEM_options_s UF_ASSEM_options_t, *UF_ASSEM_options_p_t;

/*
  Assembly Upgrade status structure
*/

struct UF_ASSEM_upgrade_status_s
{
    logical failed;          /* true if any components could not be upgraded */
    int     n_components;    /* length of the following two arrays */
    char  **component_names; /* <len:n_components> array of component names that failed to upgrade.
                                This array must be freed using
                                UF_free_string_array.
                             */
    int    *statuses;        /* <len:n_components> associated statuses with each file name.  This
                                array must be freed using UF_free. */
};

typedef struct UF_ASSEM_upgrade_status_s UF_ASSEM_upgrade_status_t,
*UF_ASSEM_upgrade_status_p_t;


/******************************************************************************
   Component array functions.

   There are two types of component arrays - those which are based on feature
   instance sets (iset arrays) and those which are based on a master component
   (mc arrays).

   Each type of array has a data structure which defines the contents of the
   array. These structures are used as arguments to the various array functions.

******************************************************************************/


/* These constants are used for the array_subtype field.
*/

#define UF_ASSEM_iset_array        1
#define UF_ASSEM_linear_array      2
#define UF_ASSEM_circular_array    3

/* This defines the maximum number of dimensions for a component array.
   This is currently 2 (X and Y)
*/

#define UF_ASSEM_max_dim_count     2

/*
   Component array based on a master component.  Also referred to as an
   mc array.
*/
struct UF_ASSEM_mc_array_data_s
{
    int     array_subtype;     /* A flag indicating which type of array this is.
                                  It will either be UF_ASSEM_linear_array or
                                  UF_ASSEM_circular_array . */
    tag_t   master_component;  /* The tag of the master component for this
                                  array*/
    tag_t   template_component; /* The tag of the template component for this
                                   array. */
    tag_t   dimensions[UF_ASSEM_max_dim_count]; /* An array of expression tags
                                   which determine the size of the array.  For
                                   linear arrays, the first element is the
                                   number of components in the X direction, and
                                   the second element is the number of
                                   components in the Y direction. For one
                                   dimensional linear arrays, the second
                                   element will be NULL.  For circular arrays,
                                   the second element will be NULL. */
    tag_t   axis_definitions[UF_ASSEM_max_dim_count]; /* The solid entities
                                   (faces, datums, etc) which determine the
                                   direction of the array.  For linear arrays,
                                   the first element defines the X direction,
                                   and the second the Y direction.  For one
                                   dimensional linear arrays, the second element
                                   will be NULL.  For circular arrays, the first
                                   element is the central axis, and the second
                                   is NULL.  If these solid objects are in
                                   component part files, you should pass in
                                   their occurrences in the assembly that
                                   contains the array.*/

    tag_t   offsets[UF_ASSEM_max_dim_count]; /* An array of expression tags
                                   which determine the spacing between array
                                   elements. For linear arrays, the first
                                   element is the X offset, and the second is
                                   the Y offset.  For one dimensional linear
                                   arrays, the second element will be NULL.
                                   For circular arrays, the first element is
                                   the angle between components, and the
                                   second is NULL. */

    char *array_name;           /* The name of the array object. When this value
                                   is returned from an enquiry function, it is
                                   dynamically allocated, and must be freed with
                                   UF_free. */

};

typedef struct UF_ASSEM_mc_array_data_s UF_ASSEM_mc_array_data_t,
*UF_ASSEM_mc_array_data_p_t;

/*
   Component array based on a feature instance-set component.  Also referred
   to as an iset array.
*/
struct UF_ASSEM_iset_array_data_s
{
    tag_t     feature_iset;       /* The tag of the feature iset that the array
                                     is based upon. Information about the iset
                                     may be obtained by calling
                                     UF_MODL_ask_linear_iset_parms or
                                     UF_MODL_ask_circular_iset_parms as
                                     appropriate. */

    tag_t     template_component; /* The tag of the template component for this
                                     array. */
    int       dimensions[UF_ASSEM_max_dim_count]; /* An array of integers which
                                     indicates the size of the array.  A referenced iset can
                                     be Linear or Circular.  For a linear iset, the first
                                     array element is the number of components in the X direction
                                     and the second element is the number of components
                                     in the Y direction.  For a one dimensional linear iset, the 
                                     second element will be NULL.  For circular arrays, the second
                                     element will be NULL.  The dimensions array can be left 
                                     unpopulated (or not required) during creation. */
    char *array_name;             /* The name of the array object. When this
                                     value is returned from an enquiry function,
                                     it is dynamically allocated, and must be
                                     freed by calling UF_free. */

} ;

typedef struct UF_ASSEM_iset_array_data_s UF_ASSEM_iset_array_data_t,
*UF_ASSEM_iset_array_data_p_t;

/******************************************************************************
   Instance intent data types.
 ******************************************************************************/

struct UF_ASSEM_instance_intent_s
{
    UF_FAM_intent_data_p_t          fam_intent; /* Part family intent.  NULL
                                                   if no intent exists. */
} ;

typedef struct UF_ASSEM_instance_intent_s UF_ASSEM_instance_intent_t,
*UF_ASSEM_instance_intent_p_t;

struct UF_ASSEM_instance_status_s
{
    logical                         child_changed; /* A flag indicating whether
                                                      the child of the instance
                                                      has changed. */
    tag_t                           current_child; /* Current child of the
                                                      instance. */

    tag_t                           previous_child; /* Previous child of the
                                                       instance. */

    char                           *info;           /* Additional information.
                                                       This can be NULL. */
};

typedef struct UF_ASSEM_instance_status_s UF_ASSEM_instance_status_t,
*UF_ASSEM_instance_status_p_t;


/********************************************************************
*  UF_ASSEM_level_option_t is used to control the results of an operation
*  to modify a part occurrence, when the part occurrence chosen
*  cannot be modified directly for some reason.  It is currently
*  used for reposition.
*
********************************************************************/
enum UF_ASSEM_level_option_e
{
    UF_ASSEM_use_strict_level,   /* If the given part occurrence can't be
                                    modified, the operation will fail and return
                                    UF_ASSEM_err_operation_requires_override */
    UF_ASSEM_use_existing_level, /* If the given part occurrence can't be
                                    modified, the operation will instead transform
                                    the corresponding part occurrence at the
                                    nearest level down in the assembly where an
                                    appropriate override exists. If none exists
                                    then the instance will be modified. */
    UF_ASSEM_establish_override  /* If the given part occurrence can't be
                                    modified, the operation will create an override
                                    in the part of the given part occurrence and
                                    then perform the transform. */
};

typedef enum UF_ASSEM_level_option_e UF_ASSEM_level_option_t;

/********************************************************************
*  UF_ASSEM_prev16_align_t describes a PreV16 Align constraint which needs to
*  be converted to a Distance constraint because its offset direction is
*  not interpreted correctly.
*
*  This type is used as arguments by the following functions:
*     UF_ASSEM_find_prev16_aligns_to_check
*     UF_ASSEM_convert_prev16_aligns
*     UF_ASSEM_free_prev16_aligns
* 
********************************************************************/
typedef struct UF_ASSEM_prev16_align_s
{
    tag_t part;             /* The part in which the constraint resides */
    tag_t condition_tag;    /* The mating condition in which the constraint resides */
    char *condition_name;   /* The name of the mating condition */
    int constraint_index;   /* The index of the constraint within the mating condition */
    char *constraint_name;  /* The name of the constraint */
    tag_t offset;           /* The offset distance expression */
    char *offset_name;      /* The name of the offset distance expression of the constraint */
    double offset_value;    /* The value of the offset distance expression of the constraint */
    char *message;          /* A message indicating any problems related to the conversion of the constraint (might be NULL) */
    char *reason;           /* A reason explaining the above message (might be NULL) */
} UF_ASSEM_prev16_align_t, *UF_ASSEM_prev16_align_p_t;


/*  
    Return value of user registered animation callback function.
*/
#define UF_ASSEM_anim_continue        (0) /*If user want to continue to play next frame.*/
#define UF_ASSEM_anim_stop            (1) /*If user want to stop current sequence playback.*/

/* 
   Definition of a callback function mechanism for animation playback. 
   This callback function will called each frame when user use synchronous play.
*/
typedef int (*UF_ASSEM_animation_callback_f_t)(
    void* user_data          /* <I> This is a user supplied pointer. */
    );


/*********************************************************************/
/* Data returned by 
     UF_ASSEM_set_work_part_context_quietly
*/
typedef struct UF_ASSEM_work_part_context_s *UF_ASSEM_work_part_context_p_t;


/*********************************************************************/

#ifdef __cplusplus
}
#endif

#endif /* UF_ASSEM_TYPES_INCLUDED */
