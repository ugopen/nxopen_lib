/*******************************************************************************
             Copyright (c) 1995-2003 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File description:
 The public Open C API interface for the Sheet Metal Design module.

 The Sheet Metal Design functions operate on a flat pattern and enable you to:
  . Initialize the SMD environment and verifies that an SMD license exists.
  . Check if the SMD environment has been successfully initialized.
  . Terminate the SMD environment.
  . Execute to the UNFORMED process in the Part in Process table.
  . Execute to the FORMED process in the Part in Process table.
  . Get a list of nodes from Part in Process.
  . Create a new node in the Part in Process table.
  . Get data for a node in the in the Part in Process table.
  . Get the children of a node in the Part in Process table.
  . Edit a node in the Part in Process table.
  . Execute a node in the Part in Process table.
  . Delete a node in the Part in Process table.
  . Get a list of all formable features of the specified solid body.
  . Define the general SMD preferences.
  . Get the current settings of the general SMD preferences.
  . Each sheet metal design function either returns a zero (no error) or an
    error code. Use UF_get_fail_message to obtain the error message string.

 Flat Patterns:

 This section describes the Sheet Metal Design Flat Pattern API
 routines. The functions included in this section allow you to:

  . Acquire an array of object tags of additional curves which were mapped to
    the given flat pattern.
  . Acquire an array of bend line object tags from a given flat pattern.
  . Acquire an array of bend tangent line object tags from the given flat
    pattern.
  . Acquire an array of contour line object tags from the given flat pattern.
  . Acquire the tag of a current flat pattern group entity given the object
    identifier of a solid body.
  . Acquires an array of object tags of the faces which were used to generate
    the flat pattern.
  . Inquires the flat pattern preferences currently available for Sheet Metal
    Design.
  . Acquire an array of form block line object tags from the given flat pattern.
  . Create a flat pattern grouped object (collection of wire frame entities)
    for the solid body associated with the root face.
  . Delete the flat pattern grouped object along with the associated wire frame
    geometric entities.
  . Define the flat pattern preferences currently available for Sheet Metal
    Design.
  . Determine if any modification to the solid body has been performed and then
    updates the flat pattern accordingly.

*****************************************************************************/

#ifndef UF_SMD_H_INCLUDED
#define UF_SMD_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_retiring.h>
#include <libufun_exports.h> /* This should be put last */

#ifdef __cplusplus
extern "C" {
#endif


/* Enumerations for Tcl output types                                        */
enum UF_SMD_standard_values_e
{
    UF_SMD_single_value = 0, /* A single value                              */
    UF_SMD_value_list,       /* A list of values                            */
    UF_SMD_parm_value,       /* A parameter value list                      */
    UF_SMD_variable_list,    /* A variable list                             */
    UF_SMD_stds_error        /* An error in the Tcl standards file          */
} ;

typedef enum UF_SMD_standard_values_e UF_SMD_standard_values_t;

typedef enum
{
    UF_SMD_BAF_INVALID_OPTION = -1,
    UF_SMD_BAF_USE_EXPRESSION,
    UF_SMD_BAF_USE_TCL,
    UF_SMD_BAF_USE_SPRDSHEET,
    UF_SMD_BAF_NUM_ITEMS
} UF_SMD_baf_options_e_t;

typedef enum
{
    UF_SMD_ANGLE_INVALID_OPTION = -1,
    UF_SMD_ANGLE_BEND,
    UF_SMD_ANGLE_INCLUDED,
    UF_SMD_ANGLE_NUM_ITEMS
} UF_SMD_angle_type_e_t;

typedef enum
{
    UF_SMD_RADIUS_INVALID_OPTION = -1,
    UF_SMD_RADIUS_INSIDE,
    UF_SMD_RADIUS_OUTSIDE,
    UF_SMD_RADIUS_NUM_ITEMS
} UF_SMD_radius_type_e_t;

typedef enum
{
    UF_SMD_BAT_ANGLE_INVALID_OPTION = -1,
    UF_SMD_BAT_ANGLE_BEND,
    UF_SMD_BAT_ANGLE_INCLUDED,
    UF_SMD_BAT_ANGLE_NUM_ITEMS 
} UF_SMD_bat_angle_type_e_t;

typedef enum
{
    UF_SMD_BAT_RADIUS_INVALID_OPTION = -1,
    UF_SMD_BAT_RADIUS_INSIDE,
    UF_SMD_BAT_RADIUS_OUTSIDE,
    UF_SMD_BAT_RADIUS_NUM_ITEMS
} UF_SMD_bat_radius_type_e_t;

typedef enum
{
    UF_SMD_FORMING_METHOD_INVALID_OPTION = -1,
    UF_SMD_USE_SELF_FORMING_FEATURES,
    UF_SMD_USE_FORMING_OPERATIONS,
    UF_SMD_FORMING_METHOD_NUM_ITEMS
} UF_SMD_forming_method_e_t;

typedef enum
{
    UF_SMD_SEQUENTIAL_PROC_INVALID_OPTION = -1,
    UF_SMD_NON_SEQUENTIAL_PROCESS,
    UF_SMD_SEQUENTIAL_PROCESS,
    UF_SMD_SEQUENTIAL_PROC_NUM_ITEMS
} UF_SMD_pip_sequential_e_t;


/* Data structure used to define the General Preferences for the SMD module. */
struct  UF_SMD_gen_prefs_s
{
    int     seq_labels;     /* Display sequence labels on body
                            0 = Do not display the labels.
                            1 = Display the labels. */
    int     use_feat_stds;  /* Use feature standards on dialogs (1/0) */
    int     chk_stds;       /* Check standards on create (1/0) */
    char    *default_baf;   /* Bend Allowance formula for the creation
                            of flat patterns & unformed bodies. */
    char    *material;      /* Material type of the body. */
    char    *thickness;     /* Material thickness of the body */
    int     line_color;     /* Reference line color */
    int     enforce_cre_state; /* Enforce Creation State Editing*/
    char    *mat_margin;    /* Percentage by which bracket is made larger */
    int     use_bat;    /* OBSOLETE. Use the TCL Bend Allowance Table procedure
                               found in ugsmd_def.std?                    */
    logical  use_global_thickness;  /* Use Global thickness for feature
                                     creation (True/ False)   */
    int     thickness_type;     /* Thickness type 0 - Infer the thickness
                                                  1 - Use Expression  */
    logical  use_global_radius;     /* Use global radius for feature
                                       creation (True / False )  */
    char     *global_radius;        /* Global radius  */
    UF_SMD_radius_type_e_t  radius_type;     /* Radius type
                                              UF_SMD_RADIUS_INSIDE
                                              UF_SMD_RADIUS_OUTSIDE   */
    logical  use_global_angle;     /* Use global angle value for feature
                                      creation (True / False)   */
    char     *global_angle;        /* Global angle value */
    UF_SMD_angle_type_e_t  angle_type;      /* Angle type
                                              UF_SMD_ANGLE_INCLUDED
                                              UF_SMD_ANGLE_BEND  */
    UF_SMD_baf_options_e_t  baf_option;    /* Options for BAF
                                              UF_SMD_BAF_USE_EXPRESSION
                                              UF_SMD_BAF_USE_TCL
                                              UF_SMD_BAF_USE_SPRDSHEET */
    logical  use_global_baf;             /* Use global BAF for feature
                                           creation (True / False )  */
    UF_SMD_forming_method_e_t forming_method; /* Forming method
                                              UF_SMD_USE_SELF_FORMING_FEATURES,
                                              UF_SMD_USE_FORMING_OPERATIONS */
    UF_SMD_bat_radius_type_e_t  bat_radius_type;     /* Radius type
                                              UF_SMD_BAT_RADIUS_INSIDE
                                              UF_SMD_BAT_RADIUS_OUTSIDE   */
    UF_SMD_bat_angle_type_e_t  bat_angle_type;      /* Angle type
                                              UF_SMD_BAT_ANGLE_INCLUDED
                                              UF_SMD_BAT_ANGLE_BEND  */
    UF_SMD_pip_sequential_e_t pip_sequential; /* PIP sequential Processing
                                              UF_SMD_NON_SEQUENTIAL_PROCESS,
                                              UF_SMD_SEQUENTIAL_PROCESS */
};


typedef struct  UF_SMD_gen_prefs_s UF_SMD_gen_prefs_t,
                                  *UF_SMD_gen_prefs_p_t;
/* Data structures used to define the Flat Pattern Preferences for SMD Module */

/* Enumeration for flat pattern orientation */
enum UF_SMD_fp_orientation_e
{
    UF_SMD_start_position = 0,       /* Align with start face */
    UF_SMD_working_coordinate_system /* Aligh with WCS */
} ;

typedef enum UF_SMD_fp_orientation_e UF_SMD_fp_orientation_t;

/* Enumeration to specify curve types created in the flat pattern */
enum UF_SMD_fp_curves_e
{
    UF_SMD_lines = 0,           /* Flat Pattern comprised of only lines */
    UF_SMD_lines_arcs,          /* Flat Pattern comprised of lines and
                                arcs/circles */
    UF_SMD_lines_arcs_splines   /* Flat Pattern comprised of lines,
                                arcs/circles and splines */
} ;

typedef enum UF_SMD_fp_curves_e UF_SMD_fp_curves_t;

/* Enumeration for distortion constraint, laying out distortion faces */
enum UF_SMD_fp_distortion_e
{
    UF_SMD_shortest_edge = 0,   /* Use the shortest edge */
    UF_SMD_longest_edge         /* Use the longest edge */
} ;

typedef enum UF_SMD_fp_distortion_e UF_SMD_fp_distortion_t;

/* Data structure for Flat Pattern Preferences */
struct UF_SMD_fp_prefs_s
{
    double     angle_tol;                  /* The angle tolerance to use in
                                           laying out the surfaces*/
    double     chord_tol;                  /* The chordal tolerance to use in
                                           mapping curves to the flat pattern */
    double     grid_size;                  /* Grid size */
    int        layer;                      /* Layer to place flat pattern on */
    int        distortion_constraint;      /* Controls distortion face
                                            mapping (Longest edge /
                                            Shortest edge)*/
    int        fp_orientation;             /* Enumerated type defining where to
                                           create the flat pattern */
    int        curve_set;                  /* Enumerated type defining which
                                           curves are  used to generate a Flat
                                           Pattern. */
    logical    tangent_lines;              /*  Bend Tangent lines created on
                                           theFlat Pattern (TRUE/FALSE). */
    logical    center_lines;               /* Bend Center lines created on the
                                           Flat Pattern (TRUE/FALSE).*/
    logical    form_block_curves;          /* Form Block curves created on the
                                            Flat Pattern (TRUE/FALSE).*/
    logical    contour_curves;             /* Contour curves created on the
                                            Flat Pattern (TRUE/FALSE). */
    logical    multiple_fp;                /* Allow multiple flat patterns
                                           (TRUE/FALSE).*/
    logical    auto_update;                /* Enable auto flat pattern update */
    logical    use_baf;                    /* Use BAF when creating flat
                                           pattern */
    char       *name;                      /* Default flat pattern name */
    int        fp_algorithm;               /* Flat Pattern Creation algorithm */
} ;

typedef struct UF_SMD_fp_prefs_s UF_SMD_fp_prefs_t,
                                *UF_SMD_fp_prefs_p_t;
/*
** Data structure for UF_SMD_single_value and UF_SMD_error return types

*/
struct UF_SMD_single_value_s
{
    char *value;        /* Text string containing a single value            */
} ;

typedef struct UF_SMD_single_value_s UF_SMD_single_value_t,
                                    *UF_SMD_single_value_p_t;
/*
** Data structure for UF_SMD_value_list and UF_SMD_variable_list

*/
struct UF_SMD_value_list_s
{
    int  num_strings;   /* Number of strings                                */
    char **value_list;  /* <len:num_strings>
                           String Array of values                           */
} ;

typedef struct UF_SMD_value_list_s UF_SMD_value_list_t,
                                *UF_SMD_value_list_p_t;
/*
** Data structure for UF_SMD_parm_value

*/

struct UF_SMD_parm_value_s
{
    int  num_pairs;     /* Number of parameter-value pairs                  */
    char **parm_names;  /* <len:num_pairs>
                           Array of parameter names                         */
    char **parm_values; /* <len:num_pairs>
                           Array of parameter values                        */
} ;

typedef struct UF_SMD_parm_value_s UF_SMD_parm_value_t,
                                 *UF_SMD_parm_value_p_t;
/* Union of all three structures                                            */
union UF_SMD_results_union_u
{
    UF_SMD_single_value_t  single_value;
    UF_SMD_value_list_t    value_list;
    UF_SMD_parm_value_t    parm_values;
} ;

typedef union UF_SMD_results_union_u UF_SMD_results_union_t;
/* Results structure                                                        */
struct UF_SMD_results_s
{
    int result_type;                /* Return type                          */
    char *note;                     /* "note:" if present, otherwise ""     */
    UF_SMD_results_union_t results; /* Output from Tcl standards file       */
} ;

typedef struct UF_SMD_results_s UF_SMD_results_t,
                            *UF_SMD_results_p_t;
/* Output from chk_std                                                      */
struct UF_SMD_chk_std_results_s
{
    int  num_objects;
    char **results;     /* <len:num_objects>
                           Array of results strings                         */
} ;

typedef struct UF_SMD_chk_std_results_s UF_SMD_chk_std_results_t,
                                     *UF_SMD_chk_std_results_p_t;
/****************************************************************************

 **************************************************************************/

#define ERROR_UF_SMD_base      1465000

/* Error Code(s) for UF_SMD Interface. */
#define UF_SMD_ERR_NOT_INITIALIZED      (ERROR_UF_SMD_base + 1)
#define UF_SMD_ERR_TCL_EVAL             (ERROR_UF_SMD_base + 2)
#define UF_SMD_ERR_NO_STDS_FILE_FOUND   (ERROR_UF_SMD_base + 3)

/* Function prototypes for Initialization and Termination of the module.
 * The module must be initialized prior to calling any UF_SMD routines.
 * These routines are available for both Internal and External usage.
 */


/***************************************************************************
Initializes the SMD environment and verifies that an SMD license
exists.  If you do not call UF_SMD_initialize, then subsequent calls to
SMD Open API routines fail with an error code of
UF_err_program_not_initialized.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_initialize( void );

/**************************************************************************
Checks if the SMD environment has been successfully initialized.

Return:
     Return Code
     0 = SMD is not initialized
     1 = SMD has been properly initialized

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_is_initialized( void ); /*<NEC>*/

/**************************************************************************
Terminates the SMD environment. Once UF_SMD_terminate is called
from an external Open API program, the program should exit. It
is recommended that you do not attempt to call UF_SMD_initialize
again and continue operation.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_terminate( void );

/* Function prototypes for the Forming table operations of the
 * UF_SMD module.  This routines are available for both Internal
 * and External usage.
 */

/* Function prototypes for the Part in Process operations of the
 * UF_SMD module.
 */

/**************************************************************************
Execute to the UNFORMED sequence in the forming table.  This
results in the body being placed in its fully unformed state (flattened
representation).

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_exec_unformed(
tag_t body  /* <I>
            Object ID of current form table.
            */
);

/**************************************************************************
Execute to the FORMED sequence in the forming table. This results
in the body being placed in its fully formed state (folded
representation).

Environment: Internal  and  External
See Also:
History:
*************************************************************************/
extern UFUNEXPORT int UF_SMD_exec_formed(
tag_t body  /* <I>
            Object ID of current form table.
            */
);

/* Function prototypes for the Preferences used by the UF_SMD module
 * ( General and Flat Pattern).
 */


/**************************************************************************
Inquires the current settings of general SMD preferences.  These
preferences currently consist of the default bend allowance formula
for the creation of a flat pattern grouped object, the specified
material, and whether or not to display the bend sequence labels.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_general_prefs(
UF_SMD_gen_prefs_p_t * general_prefs  /* <OF>
                                      The address of a pointer to typed data.
                                      */
);
/**************************************************************************
Defines the general SMD preferences.  These preferences currently
consist of the default bend allowance formula for the creation of a flat
pattern grouped object, the specified material, and whether or not to
display the bend sequence labels.

(Radius + (Thickness * 0.44))*rad(Angle)

The default bend formula must be a valid RHS (right hand side) for a NX
Expression.

Radius, Thickness, and Angle when used, must be represented exactly as shown
with the first letter capitalized.  They are not actually expression variables
in the usual sense, but are substituted variables for each flange when the
expression is evaluated.

Radius is the inside bend radius; Thickness is the material thickness;
Angle is the bend angle; and rad is a built-in NX Expression
function. The value .44 represents the Neutral Axis Factor, an
empirical value which may be adjusted for the material type and
thickness to correctly calculate the developed length of the bend
portion of a flange feature due to folding.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_set_general_prefs (
UF_SMD_gen_prefs_p_t general_prefs  /* <I>
                                    A pointer to typed data.
                                    */
);
/**************************************************************************
Inquires the flat pattern preferences currently available for Sheet
Metal Design. The routine returns a data structure and individual
elements that must be freed by a call to UF_free.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_fp_prefs (
UF_SMD_fp_prefs_p_t *fp_options  /* <OF>
                                Structure that contains the SMD flat pattern
                                preferences.
                                */
);
/**************************************************************************
Defines the flat pattern preferences currently available for Sheet
Metal Design. The routine requires that the data structure and
individual elements be allocated by the calling routine.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_set_fp_prefs (
UF_SMD_fp_prefs_p_t fp_options  /* <I>
                                Structure that contains the SMD flat pattern
                                preferences.
                                */
);


/* Function prototypes for the Utility routines of the UF_SMD module.
 */


/**************************************************************************
Returns a linked list of all formable features used in the composition
of the specified solid body. An example of a formable feature would
be a flange. The handling of the linked list can be done by using the
UF_MODL_*_list_* routines.

Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_formable_feats(
tag_t body ,/* <I>
            Object ID of a solid body.
            */
uf_list_p_t * feat_list  /* <OF,free:UF_MODL_delete_list>
                         A linked list of formable features which take part in
                         the composition of the specified solid body.  Use
                         UF_MODL_delete_list to free the space allocated
                         for the linked list.
                         */
);
/**************************************************************************
Returns the bend allowance formula (BAF), bend angle, inside radius,
thickness of the solid body, computed bend allowance distance, and
inside/outside indicator for the bend line associated of a flat pattern
object.



Environment: Internal  and  External

See Also:

History:
 *************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_bend_line_data(
tag_t bend_line ,/* <I>
                 Object ID of a bend line (curve).
                 */
char ** bend_formula ,/* <OF>
                      Pointer to a character string defining the Bend
                      Allowance Formula.  This must be freed by calling UF_free.
                      */
double * angle ,/* <O>
                Bend angle (in Radians).
                */
double * inside_radius ,/* <O>
                        Radius of the bend area.
                        */
double * thickness ,/* <O>
                    Thickness of the material
                    */
double * bend_allowance ,/* <O>
                         The dimensional amount added to the part through
                         elongation during the bending process derived from
                         the bend allowance formula.
                         */
int * material_side  /* <O>
                     Indicator of the material side for the bend line.
                     0 = Inside
                     1 = Outside
                     */
);

/*
** Function prototypes for the Standards routines of the UF_SMD module.
*/


/***************************************************************************
Load the given standards file into memory.  If no file specification is
given, then it loads the file pointed to by $UGII_UGSMD_STDS_LIBRARY.
If the environment variable doesn't point to a specific file, the
routine will load the file ugsmd_def.std from one of the following
directories, searching them in order:
        current working directory
        $UGII_UGSMD_STDS_LIBRARY
        $UGII_BASE_DIR/ugii

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_load_standards (
char * fspec  /* <I>
              File specification of standards file, or
              "" to use default standards file.
              */
);
/***************************************************************************
Queries the standards file with the given query text string. This
routine returns a data structure and individual elements that must be
freed by a call to UF_SMD_free_std_results.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_standards(
char * query_string ,/* <I>
                     Query string
                     */
UF_SMD_results_p_t* results  /* <OF,free:UF_SMD_free_std_results>
                             Pointer to pointer to an array of results data
                             structures.  This must be freed by calling
                             UF_SMD_free_std_results.
                             */
);
/***************************************************************************
Checks the entire part against the sheet metal standards file.  This
routine returns a data structure and individual elements that must be
freed by a call to UF_SMD_free_std_chk_results.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_chk_entire_part_stds (
UF_SMD_chk_std_results_p_t * results  /* <OF,free:UF_SMD_free_std_chk_results>
                                      Pointer to pointer to results data
                                      structure.  This must be freed by
                                      calling UF_SMD_free_std_chk_results.
                                      */
);
/***************************************************************************
This routine will utilize the "chk_std" function in the stds file to
compare the feature's parameter values with the stds and return the
test string from the standards file.

Environment: Internal  and  External
See Also:
History:
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_chk_feature_stds (
    tag_t                      *features,    /* <I,len:num_features>
                                             Array of feature tags
                                             */
    int                        num_features, /* <I>
                                             Number of features
                                             */
    UF_SMD_chk_std_results_p_t *results      /* <OF,free:UF_SMD_free_std_chk_results>
                                             Ptr to results.  This must be
                                             freed by calling
                                             UF_SMD_free_std_chk_results
                                             */
);
/***************************************************************************
Frees all memory associated with the results of a standards query.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_free_std_results (
UF_SMD_results_t * results  /* <I>
                            Pointer to results structure
                            */
);/* <NON_NXOPEN> */


/***************************************************************************
Frees all memory associated with the results of a standards check.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_free_std_chk_results (
UF_SMD_chk_std_results_t * results  /* <I>
                                    Pointer to check standard results structure
                                    */
);/* <NON_NXOPEN> */

/*
 * Function prototypes for the Flat Pattern routines of the UF_SMD module.
 */


/***************************************************************************
Creates a flat pattern grouped object (collection of wireframe
entities) for the solid body associated with the root face. A
NULL_TAG is returned if a flat pattern is not generated from the
solid body. If a non-fatal error occurs during the creation of a flat
pattern grouped object, a valid tag is returned along with an error
code.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_create_flat_pattern (
char * name ,/* <I>
             Name of the flat pattern
             */
int layer ,/* <I>
           Layer on which to create the flat pattern grouped
           object.
           */
tag_t start_face ,/* <I>
                  Object ID of the start face for traversing the part to
                  create the flat pattern.
                  */
tag_p_t flat_pattern  /* <O>
                      Object ID of the flat pattern grouped object.
                      */
);

/***************************************************************************
Deletes the flat pattern grouped object along with the associated
wireframe geometric entities.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_delete_flat_pattern (
tag_t flat_pattern  /* <I>
                    Body of the flat pattern to be deleted.
                    */
);
/***************************************************************************
Determines if any modification to the solid
body has been performed and then updates the flat pattern
accordingly. A pointer to a NULL_TAG is returned if a flat pattern is
not generated from the solid body.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_update_flat_pattern (
tag_t body ,/* <I>
            Object ID of the body that the flat pattern was
            created from.
            */
tag_p_t flat_pattern  /* <O>
                      Object ID of the flat pattern group object.
                      */
);

/***************************************************************************
Acquires the tag of current flat pattern group entity given the object
identifier of a solid body. Returns NULL_TAG if a flat pattern does
not exist for the associated body.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_flat_pattern (
tag_t body ,/* <I>
            Object ID of a solid body.
            */
tag_p_t flat_pattern  /* <O>
                      Object ID of the flat pattern group.
                      */
);

/***************************************************************************
Acquires an array of bend line object tags from the given flat pattern.
Returns NULL_TAG if the flat pattern does not contain bend lines.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_bend_lines (
tag_t flat_pattern ,/* <I>
                    Object ID of the flat pattern.
                    */
int *num_bend_lines , /* <O>
                      Number of bend line object IDs.
                      */
tag_p_t *bend_lines /* <OF,len:num_bend_lines>
                     Array of bend line object IDs.  This array must be freed
                     by calling UF_free.
                     */
);
/***************************************************************************
Acquires an array of bend tangent line object tags from the given flat
pattern. Returns NULL_TAG if the flat pattern does not contain bend
tangent lines.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_bend_tan_lines (
tag_t flat_pattern ,/* <I>
                    Object ID of the flat pattern.
                    */
int *num_bend_tan_lines , /* <O>
                          Number of bend tangent line object IDs.
                          */
tag_p_t *bend_tan_lines /* <OF,len:num_bend_tan_lines>
                         Array of bend tangent line object IDs.  This array
                         must be freed by calling UF_free.
                         */
);
/***************************************************************************
Acquires an array of contour line object tags from the given flat
pattern. Returns NULL_TAG if the flat pattern does not contain
contour lines.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_contour_lines (
tag_t flat_pattern ,/* <I>
                    Object ID of the flat pattern.
                    */
int *num_contour_lines , /* <O>
                         Number of contour line object IDs.
                         */
tag_p_t *contour_lines /* <OF,len:num_contour_lines>
                        Array of contour line object IDs.  This array must be
                        freed by calling UF_free.
                        */
);
/***************************************************************************
Acquires an array of form block line object tags from the given flat
pattern. Returns NULL_TAG if the flat pattern does not contain form
block lines.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_formblk_lines (
tag_t flat_pattern ,/* <I>
                    Object ID of the flat pattern.
                    */
int *num_formblk_lines , /* <O>
                         Number of form block line object IDs.
                         */
tag_p_t *formblk_lines /* <OF,len:num_formblk_lines>
                        Array of form block line object IDs.  This array must
                        be freed by calling UF_free.
                        */
);
/***************************************************************************
Acquires an array of object tags of the faces which were used to
generate the flat pattern.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_fp_faces (
tag_t body,         /* <I>
                    Object ID of the solid body.
                    */
int *num_faces , /* <O>
                 Number of flat pattern faces.
                 */
tag_p_t *faces /* <OF,len:num_faces>
                Array of flat pattern faces.  This array must be freed by
                calling UF_free.
                */
);
/***************************************************************************
Acquires an array of object tags of additional curves which were
mapped to the flat pattern associated with the given body. Returns NULL_TAG
if the flat pattern does not contain additional curves.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_fp_add_curves (
tag_t body,         /* <I>
                    Object ID of the solid body.
                    */
int *num_additional_curves , /* <O>
                             Number of additional curve object IDs.
                             */
tag_p_t *additional_curves /* <OF,len:num_additional_curves>
                            Array of additional curve object IDs.  This array
                            must be freed by calling UF_free.
                            */
);
/***************************************************************************
This routine will return the total number of points created.  Associated
to each point is a point tag, curve tag, face tag and calculated trim angle.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_eval_trim_angles (
    tag_p_t        curves,              /* <I,len:num_curves>
                                        array of curves
                                        */
    int            num_curves,          /* <I>
                                        number of curves/edges
                                        */
    tag_p_t        faces,               /* <I,len:num_faces>
                                        array of faces
                                        */
    int            num_faces,           /* <I>
                                        number of faces
                                        */
    double         dir_vec[3],          /* <I>
                                        trimming direction
                                        */
    double         equal_arc_len,       /* <I>
                                        equal arc length
                                        */
    int            *num_of_pts,         /* <O>
                                        number of points
                                        */
    tag_t          **pts,               /* <OF,len:num_of_pts>
                                        Array of point tags.  This array must
                                        be freed by calling UF_free.
                                        */
    tag_t          **assoc_curves,      /* <OF,len:num_of_pts>
                                        Array of associated curves tags.  This
                                        array must be freed by calling UF_free.
                                        */
    tag_t          **assoc_faces,       /* <OF,len:num_of_pts>
                                        Array of associated faces tags .  This
                                        array must be freed by calling UF_free.
                                        */
    double         **trim_ang_array     /* <OF,len:num_of_pts>
                                        Array of trim angles at each point.
                                        This array must be freed by calling
                                        UF_free.
                                        */
);

/************************************************************************
This routine creates a Sheet Metal Representation of a Modeling feature.
It currently supports Modeling Hole and Slot features.

Environment : Internal  and  External

See Also:

History :
 ************************************************************************/
extern UFUNEXPORT int UF_SMD_create_representation(
             tag_t feature, /* <I>
                               the tag of Modeling feature
                            */
             int hint_flag, /* <I>
                               hint flag
                               CURRENTLY UNUSED
                            */
             tag_t *new_feature /* <O>
                               the tag of output SMD feature
                               CURRENTLY EQUALS MODELING FEATURE TAG
                            */
);

/************************************************************************
This routine deletes a Sheet Metal Representation of a Modeling feature.
It currently supports SMD Hole and Slot representations.

Environment : Internal  and  External

See Also:

History :
 ************************************************************************/
extern UFUNEXPORT int UF_SMD_delete_representation(
             tag_t feature, /* <I>
                               the tag of SMD feature
                            */
             tag_t *new_feature /* <O>
                               the tag of the output Modeling feature
                               CURRENTLY EQUALS SMD FEATURE TAG
                            */
);

/***************************************************************************
Return the parent (edge or additional curve) of a curve or point in a
flat pattern group.  The object must be in the Master Flat Pattern
which is the newest flat pattern for a given body. The returned parent
is the object that corresponds with the child object. If the object is
an additional curve (including Contour, Mold and Form Block curves) or
point of the flat pattern the parent will be a curve or point,
otherwise the parent will be an edge.

Returns:
SMDFLAT_ERR_NOT_FLAT_PATTERN
SMDFLAT_ERR_NOT_MASTER_FLAT_PATTERN
SMDFLAT_ERR_NOT_MASTER_FLAT_PATTERN_ELEMENT

Environment: Internal  and  External

See Also:

History: Original release was in V19.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_fp_parent (
tag_t child ,  /* <I>
                    Object ID of the child entity in the flat pattern.
                    */

tag_p_t parent  /* <O>
                     Parent entity of the input child.
                     (Or NULL_TAG if there is an error.)
                     */
);


/***************************************************************************
Return the children of an object mapped by a flat pattern.  The flat
pattern specified must be the Master Flat Pattern which is the newest
flat pattern for a given body. (This can be found using
UF_SMD_ask_flat_pattern().)  The parent specified may be an edge of
the body being flattened or an additional curve (including Contour,
Mold and Form Block curves).  The returned children will be those
members of the flat pattern group which correspond to the input
object.

Returns:
SMDFLAT_ERR_NOT_MASTER_FLAT_PATTERN

Environment: Internal  and  External

See Also:

History: Original release was in V19.0.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_fp_children (
tag_t flat_pattern ,/* <I>
                    Object ID of the flat pattern.
                    */
tag_t parent ,/* <I>
                    Object ID of the flat pattern.
                    */
int *num_children , /* <O>
                      Number of child object IDs in the flat pattern.
                     (Or 0 if there is an error.)
                      */
tag_t **children /* <OF,len:num_children>
                     Array of child object IDs.  This array must be freed
                     by calling UF_free.
                     (Or NULL if there is an error.)
                     */
);





typedef enum
{
    UF_SMD_invalid_pip_node_type = -1, /* invalid value                     */
    UF_SMD_pip_process           =  0, /* PIP Process node                  */
    UF_SMD_pip_unform_group,           /* not used                          */
    UF_SMD_pip_group,                  /* PIP Group node                    */
    UF_SMD_pip_form_group,             /* not used                          */
    UF_SMD_pip_step,                   /* PIP Step node                     */
    UF_SMD_pip_unform_process,         /* reserved                          */
    UF_SMD_pip_form_process,           /* reserved                          */
    UF_SMD_num_node_type               /* number of node types              */
} UF_SMD_pip_type_enum_e_t;

/* Data structure that stores data associated with a PIP node.
 */
struct  UF_SMD_pip_node_data_s
{
    UF_SMD_pip_type_enum_e_t  node_type;   /* Type of PIP node              */
    tag_t                     parent;      /* Parent node for current node  */
    char                      name[ MAX_LINE_BUFSIZE ];
                                           /* Name of PIP node              */
    tag_t                     feature_tag; /* Feature for this PIP node     */
    int                       state_index; /* State index (used by
                                              General Flange, SMBridge,
                                              and Solid Punch features)     */
    double                    proc_ang;    /* Process angle (used by
                                              Flange and Inset Flange.
                                              For Profile Flange, SMBend,
                                              and Multibend Bracket
                                              features, a value of zero
                                              indicates unformed.  A
                                              non-zero value indicates
                                              fully formed. )               */
};

typedef struct  UF_SMD_pip_node_data_s UF_SMD_pip_node_data_t,
                                       *UF_SMD_pip_node_data_p_t;

/***************************************************************************
Create a node (process, group, or step) on the Part In
Process Navigator tree.

Environment: Internal  and  External

See Also:

History: Original release was in NX 1.0.2.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_create_pip_node (
UF_SMD_pip_node_data_p_t node_data, /* <I>
                                    Data used to create node
                                    The parent of a UF_SMD_pip_process
                                    must be NULL_TAG.  The parent of a
                                    UF_SMD_pip_group must be a process.
                                    The parent of a UF_SMD_pip_step must
                                    be a group.  UF_SMD_pip_unform_process
                                    and UF_SMD_pip_form_process node are
                                    created automatically and cannot be
                                    created with this function.
                                    */
tag_t                    *node_tag  /* <O>
                                    Tag of the new PIP node
                                    */
);

/***************************************************************************
Ask for data associated with a node on the Part In Process Navigator tree.

Environment: Internal  and  External

See Also:

History: Original release was in NX 1.0.2.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_pip_node_data (
tag_t                    node,      /* <I>
                                    The tag of the PIP node for which
                                    data is needed.
                                    */
UF_SMD_pip_node_data_t   *node_data /* <O>
                                    Data associated with this node.
                                    */
);

/***************************************************************************
This routine returns the array of PIP nodes that are children of the
given parent node.  If you want all processes, pass in NULL_TAG as the
parent.  Pass in a process tag to get an array of groups.  Pass in a
group tag to get an array of steps.

Environment: Internal  and  External

See Also:

History: Original release was in NX 1.0.2.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_ask_child_pip_nodes (
tag_t                    parent,      /* <I>
                                      The parent PIP node
                                      */
int                      *n_pip_nodes,/* <O>
                                      The size of the array of node tags
                                      */
tag_t                    **pip_nodes  /* <OF,len:n_pip_nodes>
                                      The array of child PIP nodes
                                      */
);

/***************************************************************************
This routine edits the data associated with a PIP node.

Environment: Internal  and  External

See Also:

History: Original release was in NX 1.0.2.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_edit_pip_node (
tag_t                    node,      /* <I>
                                    The tag of the PIP node for which
                                    data is to be edited.
                                    */
UF_SMD_pip_node_data_t   *node_data /* <I>
                                    New data associated with this node.
                                    Note that you cannot change the
                                    node_type or the parent.  These
                                    fields will be ignored.
                                    */
);

/***************************************************************************
Execute the specified PIP node.  Note that PIP Processes cannot be
executed.  If you execute a Group, all Steps within the Group are
executed.

Environment: Internal  and  External

See Also:

History: Original release was in NX 1.0.2.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_execute_pip_node (
tag_t                    node       /* <I>
                                    The tag of the PIP node for which
                                    data is needed.
                                    */
);

/***************************************************************************
Delete the specified PIP node.  When you delete a Process, all children
Groups and Steps are deleted.  When you delete a Group, its Steps are
deleted.

Environment: Internal  and  External

See Also:

History: Original release was in NX 1.0.2.
 **************************************************************************/
extern UFUNEXPORT int UF_SMD_delete_pip_node (
tag_t                    node       /* <I>
                                    The tag of the PIP node to be
                                    deleted.
                                    */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_SMD_H_INCLUDED */
