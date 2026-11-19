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
#include <uf_retiring.h>

#ifdef __cplusplus
extern "C" {
#endif


#define UF_ASSEM_load_from_directory    0
#define UF_ASSEM_load_from_search_dirs  1
#define UF_ASSEM_load_as_saved          2

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
#define UF_ASSEM_specify_filter         4

/*
    New options for v10.4. For earlier versions, the default behaviour
    was 0 (load components partially)
*/

#define UF_ASSEM_load_components_partially 0
#define UF_ASSEM_load_components_fully     1

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
 ***************************************************************/
struct UF_ASSEM_options_s
{
    int load_options;          /*Load Options -
                                    UF_ASSEM_load_from_directory,
                                    UF_ASSEM_load_from_search_dirs,
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
    int emphasize_color;       /* Emphasize color value see uf_obj.h, value
                                  can be from 1-216.
                               */
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

/******************************************************************************/
/*
    Mating condition structures. A mating condition consists of one or
    more constraints. Each constraint consists of a pair of mated geometric
    entities, and information on the type of mating of those entities
*/

/******************************************************************************/

enum UF_ASSEM_load_status_e
{
    UF_ASSEM_ok,
    UF_ASSEM_suppressed,         /* The object referenced by the mating
                                    condition is suppressed. */
    UF_ASSEM_not_loaded,         /* The object referenced by the mating
                                    condition is not loaded. */
    UF_ASSEM_instance_suppressed /* One of the instances along the path
                                    to the referenced object has been marked
                                    as suppressed. */
};

typedef enum UF_ASSEM_load_status_e UF_ASSEM_load_status_t;

/* Possible values for the 'from_type' field

    <SP> 9-Sep-2002
    ASM2004: Add UF_ASSEM_parametric_face. NOTE: The order here must match
    that in occ.sch
*/

#define UF_ASSEM_planar_face        0
#define UF_ASSEM_cylindrical_face   1
#define UF_ASSEM_conical_face       2
#define UF_ASSEM_toroidal_face      3
#define UF_ASSEM_spherical_face     4
#define UF_ASSEM_axi_sym_face       5
#define UF_ASSEM_straight_edge      6
#define UF_ASSEM_datum_plane        7
#define UF_ASSEM_datum_axis         8
#define UF_ASSEM_csys               9
#define UF_ASSEM_component         10
#define UF_ASSEM_point             11
#define UF_ASSEM_line              12
#define UF_ASSEM_circle_edge       13
#define UF_ASSEM_circle            14
#define UF_ASSEM_spline            15
#define UF_ASSEM_port              16
#define UF_ASSEM_parametric_face   17

/* Possible values for the 'mate_type' field */

#define UF_ASSEM_mate       0
#define UF_ASSEM_align      1
#define UF_ASSEM_orient     2
#define UF_ASSEM_v16_mate   3
#define UF_ASSEM_v16_align  4
#define UF_ASSEM_angle      5
#define UF_ASSEM_distance   6
#define UF_ASSEM_parallel   7
#define UF_ASSEM_perpendicular    8
#define UF_ASSEM_center           9
#define UF_ASSEM_tangent          10

#define UF_ASSEM_planar_angle    0
#define UF_ASSEM_3d_angle        1

#define UF_ASSEM_center_1_to_1   0
#define UF_ASSEM_center_1_to_2   1
#define UF_ASSEM_center_2_to_1   2
#define UF_ASSEM_center_2_to_2   3

#define UF_ASSEM_has_no_help_point      0
#define UF_ASSEM_has_help_point_on_from 1
#define UF_ASSEM_has_help_point_on_to   2
#define UF_ASSEM_has_help_point_on_both 3


/* Structure to define the Degree of Freedom (DOF) */
struct UF_ASSEM_dof_s
{
    double  base_point[3];       /* where the DOF's should be originated */
    int     num_trans_dof;       /* number of translational dof's        */
    double  trans_dof[3][3];     /* An array of vectors that define the
                                    translational degrees of freedom.  These are
                                    unitized, with their origin at the
                                    base_point.  Note that the vectors beyond
                                    "num_trans_dof" in this array are undefined.
                                 */
    int     num_rot_dof;         /* number of rotational dof's           */
    double  rot_dof[3][3];       /* An array of vectors that define the
                                    rotational degrees of freedom.  These are
                                    unitized, with their origin at the
                                    base_point.  Note that the vectors beyond
                                    "num_rot_dof" in this array are undefined.
                                 */
};

typedef struct UF_ASSEM_dof_s UF_ASSEM_dof_t, *UF_ASSEM_dof_p_t;

/*
    Constraint:
*/

struct UF_ASSEM_constraint_s
{
    UF_ASSEM_load_status_t from_status;  /* Load status of the object mated
                                            from.  This can be UF_ASSEM_ok,
                                            UF_ASSEM_suppressed or
                                            UF_ASSEM_not_loaded.  */
    UF_ASSEM_load_status_t to_status;    /* Load status of the object mated
                                            to */
    byte    mate_type;       /* Type of this constraint, one of the values:
                                UF_ASSEM_mate - Planar faces are mated
                                                together - i.e. surface normals
                                                point in opposite directions.
                                                Cylindrical faces touch.
                                UF_ASSEM_align - Planar faces are aligned, i.e.
                                                 surface normals point in the
                                                 same direction.  Cylindrical
                                                 faces are aligned along their
                                                 central axes.
                                UF_ASSEM_orient - Objects are at an angle.  In
                                                  this case, the "offset" field
                                                  is used to specify an angle.
                                Since V16, should use the following mating type :
                                    UF_ASSEM_v16_mate
                                    UF_ASSEM_v16_align
                                    UF_ASSEM_angle
                                    UF_ASSEM_distance
                                    UF_ASSEM_parallel
                                    UF_ASSEM_perpendicular
                                    UF_ASSEM_center
                                    UF_ASSEM_tangent */
    byte    from_type;       /* Type of the object mated from, value can be
                                UF_ASSEM_planar_face, UF_ASSEM_cylindrical_face,
                                UF_ASSEM_conical_face, UF_ASSEM_toroidal_face,
                                UF_ASSEM_spherical_face, UF_ASSEM_axi_sym_face,
                                UF_ASSEM_straight_edge, UF_ASSEM_datum_plane,
                                UF_ASSEM_datum_axis, UF_ASSEM_csys or
                                UF_ASSEM_component

                                Since V16, the following object types added :
                                    UF_ASSEM_point
                                    UF_ASSEM_line
                                    UF_ASSEM_circle_edge
                                    UF_ASSEM_circle
                                    UF_ASSEM_spline
                             */
    byte    to_type;         /* Type of the object mated from this can have
                                the same values as from_type. */

    tag_t   from;            /* prototype tag of object mated from */
    tag_t   from_part_occ;   /* part occurrence of object mated from */
    tag_t   to;              /* prototype tag of object mated to */
    tag_t   to_part_occ;     /* part occurrence of object mated to */

    tag_t   offset;          /* expression tag to be used as the offset
                                between the two objects (or the angle if
                                they are oriented.)  This is expresion can
                                be evaluated using UF_MODL_ask_exp_tag_value.
                                A NULL_TAG value can be used to represent an
                                offset of 0. */

    const char *name;        /* The name of this constraint */

    logical user_name;       /* TRUE if the name was defined by the user.  If
                                FALSE, then the name was derived from the names
                                of the mated objects. */
    logical suppressed;      /* TRUE if the constraint is suppressed */
    logical inherited;       /* TRUE if the constraint is an original constraint
                                of an override mating condition */
    byte    sub_type;        /* subtype for angle or center constraints :

                                UF_ASSEM_planar_angle : angle is measured
                                anti-clockwise from TO to FROM about an angle
                                AXIS;

                                UF_ASSEM_3d_angle : angle is measured between
                                TO and FROM.

                                UF_ASSEM_center_1_to_1 : align one object into
                                the center of the other;

                                UF_ASSEM_center_1_to_2 : align one FROM object
                                with the center of two TO objects;

                                UF_ASSEM_center_2_to_1 : align the center of
                                two FROM objects with one TO object;

                                UF_ASSEM_center_2_to_2 : align the center of
                                two FROM objects with the center of two TO
                                objects */

    byte    second_from_type; /* Type of the second FROM object for center
                                 constraint : 2-1 and 2-2 */
    tag_t   second_from;      /* prototype tag of the second FROM object */
    tag_t   second_from_part_occ; /* part occurrence of the second FROM object */

    byte    second_to_type; /* Type of the second TO object for center
                               constraint : 1-2 and 2-2 OR type of the angle
                               axis object for the planar constraint */
    tag_t   second_to;      /* prototype tag of the second TO object or angle
                               axis */
    tag_t   second_to_part_occ; /* part occurrence of the second TO object or
                                   angle axis */

    byte    has_help_point; /* indicate on which geom a help point is defined :
                               UF_ASSEM_has_no_help_point : no help point is
                               defined

                               UF_ASSEM_has_help_point_on_from : help point is
                               defined for FROM object, and is stored in
                               help_points[0,1,2]

                               UF_ASSEM_has_help_point_on_to : help point is
                               defined for TO object, and is stored in
                               help_points[3,4,5]

                               UF_ASSEM_has_help_point_on_both : help points
                               are defined for both FROM object and TO object,
                               and are stored in help_points[0,1,2] and
                               help_points[3,4,5] */
    double  help_points[6]; /* help points defined in part occ space. used for
                               specifying where the tangent position should be
                               located. Currently, help points are needed for
                               tangent constraint and any spline-related
                               constraints. If no help points are defined, the
                               constraint solver will find the closest solution
                            */
} ;

typedef struct UF_ASSEM_constraint_s UF_ASSEM_constraint_t,
*UF_ASSEM_constraint_p_t;

#define UF_ASSEM_MAX_CONSTRAINTS 30

/*
    Mating condition
*/
struct UF_ASSEM_mating_condition_s
{

    tag_t                   mated_object;     /* The instance tag of the
                                                 component that is positioned
                                                 with this mating condition. */
    tag_t                   part_occurrence;  /* The tag of the part occurrence
                                                 in which the mating condition
                                                 exists. This field can vary if
                                                 override is TRUE */
    const char              *name;            /* The name of this mating
                                                 condition. */
    logical                 user_name;        /* TRUE if the name was
                                                 defined by the user. FALSE, if
                                                 the user did not specify a
                                                 name, and the name has instead
                                                 been derived from the names of
                                                 the components involved. */
    short                  init_check;        /* This is set by UF_ASSEM_init_mc
                                                 which should be used when
                                                 allocating mating conditions
                                              */
    UF_ASSEM_constraint_t  constraints[UF_ASSEM_MAX_CONSTRAINTS]; /*
                                                 The array of constraints
                                                 that define this mating
                                                 condition. */
    int                     num_constraints;  /* The number of constraints
                                                 in this mating condition. */
    logical                 suppressed;       /* TRUE if the mating condition
                                                 is suppressed.  A suppressed
                                                 mating conditions is not
                                                 updated in response to any
                                                 changes in the mated geometry.
                                              */
    logical                 override;         /* TRUE if this is an override
                                                 mating condition */
    logical                 implicit;         /* TRUE if the override mating
                                                 condition is implicit. This
                                                 field is meaningless unless
                                                 override is TRUE */
};

typedef struct UF_ASSEM_mating_condition_s UF_ASSEM_mating_condition_t,
*UF_ASSEM_mating_condition_p_t;


/* Values used in UF_ASSEM_solve_mc  */
enum UF_ASSEM_mc_status_e
{
    UF_ASSEM_mc_solved,
    UF_ASSEM_mc_not_solved,
    UF_ASSEM_mc_no_mating_specified,
    UF_ASSEM_mc_suppressed,           /* This could apply either to the mating
                                         condition or to all its constraints */
    UF_ASSEM_mc_data_unloaded,        /* This means that a to or from geometry
                                         used in the mating condition is not
                                         available, either because the part is
                                         not loaded or because a feature is
                                         suppressed */
    UF_ASSEM_mc_ignored               /* This means that the arrangement the
                                         condition was solved in is set to
                                         ignore constraints */
};


typedef enum UF_ASSEM_mc_status_e UF_ASSEM_mc_status_t;

/* Values used in UF_ASSEM_check_mc_structure */
enum UF_ASSEM_mc_structure_state_e
{
    UF_ASSEM_structure_ok,        /* The mating condition structure is valid.*/
    UF_ASSEM_no_component,        /* No component was specified */
    UF_ASSEM_invalid_entity_type, /* An invalid type of object was given in a
                                     constraint or an occurrence was given */
    UF_ASSEM_invalid_occ,         /* There was no occurrence of the given object
                                     in the given part occurrence. */
    UF_ASSEM_invalid_from_part,   /* The from_part_occ does not exist in the
                                     component to be mated. */
    UF_ASSEM_invalid_to_part,     /* The to_part_occ does exist in the
                                     component to be mated (i.e. trying to
                                     mate a component to itself. */
    UF_ASSEM_circular_mating,     /* The mating condition would cause a
                                     circular chain of dependencies within
                                     the mating conditions in this part.*/
    UF_ASSEM_promoted_object,     /* An attempt was made to mate a component
                                     using promoted geometry. This is not
                                     allowed. */
    UF_ASSEM_invalid_offset,      /* Implies that the expression stored in a
                                     mating conditions constraint is invalid.
                                     For example, if the expression is in a
                                     different part than the mating condition
                                     itself. */
    UF_ASSEM_invalid_from_ipath,  /* Indicates a problem in the instance path
                                     generated from the from_part_occ field
                                     specified in the mating condition data
                                     structure. */
    UF_ASSEM_invalid_to_ipath,    /* Indicates a problem in the instance path
                                     generated from the to_part_occ field
                                     specified in the mating condition data
                                     structure. */
    UF_ASSEM_invalid_override,    /* Indicates one or more override instances
                                     in a constraint that does not belong to an
                                     override mating condition. */
    UF_ASSEM_not_initialized      /* Indicates the structure was not initialized
                                     using UF_ASSEM_init_mc. */
};

typedef enum UF_ASSEM_mc_structure_state_e UF_ASSEM_mc_structure_state_t;

/******************************************************************************/
/* Component array functions.

   There are two types of component arrays - those which are based on feature
   instance sets (iset arrays) and those which are based on a master component
   (mc arrays).

   Each type of array has a data structure which defines the contents of the
   array. These structures are used as arguments to the various array functions.
*/

/******************************************************************************/


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
                                     determine the size of the array. For linear
                                     arrays, the first element is the number of
                                     components in the X direction, and the
                                     second element is the number of components
                                     in the Y direction. For one dimensional
                                     linear arrays, the second element will be
                                     NULL.  For circular arrays, the second
                                     element will be NULL. */

    char *array_name;             /* The name of the array object. When this
                                     value is returned from an enquiry function,
                                     it is dynamically allocated, and must be
                                     freed by calling UF_free. */

} ;

typedef struct UF_ASSEM_iset_array_data_s UF_ASSEM_iset_array_data_t,
*UF_ASSEM_iset_array_data_p_t;

/******************************************************************************/
/* Instance intent data types.
*/
/******************************************************************************/

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



#ifdef __cplusplus
}
#endif

#endif /* UF_ASSEM_TYPES_INCLUDED */
