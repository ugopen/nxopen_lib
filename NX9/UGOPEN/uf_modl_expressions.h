/*******************************************************************************

                     Copyright 2007 UGS Corp.
                       All Rights Reserved.



File description:
    Open API modeling routines to create, edit and inquire about expressions.

*****************************************************************************/

#ifndef UF_MODL_EXPRESSIONS_H_INCLUDED
#define UF_MODL_EXPRESSIONS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <uf_curve.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
The user inputs a pointer to a character string that contains three
pieces of information.  The first item is a unique name for the
expression and is followed by an "=" sign. The value of the expression
completes the requirements for a valid input string. The pieces on
either side of the equal sign are also referred to as the lhs (left hand
side) and rhs (right hand side).

If the tag of the created expression is required, then UF_MODL_create_exp_tag
should be used instead.

Environment: Internal  and  External
See Also:  UF_MODL_create_exp_tag

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_exp(
char * expr_str  /* <I>
                 New expression. The maximum number of characters for an 
                 expression name (lhs or left hand side) is 100. The maximum 
                 length for the entire expression is UF_MAX_EXP_NCHARS characters. 
                 This includes all three pieces: lhs, equal sign, and rhs.
                 */
);

/****************************************************************************
The user inputs a pointer to a character string that matches the
expression that is to be deleted.  Only the name should be included, the
'=' and value are to be left out of the character string.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_delete_exp(
char * exp_name  /* <I>
                 Name of expression to delete
                 */
);

/****************************************************************************
The input to UF_MODL_edit_exp is similar to UF_MODL_create_exp, except for
the fact that the expression name must already exist. The user needs to have
the name of the expression, an '=' sign, and a new value contained within the
input character string. This routine does not automatically update the database.

After you use this routine, call UF_MODL_update to update the database.

Environment: Internal  and  External
See Also: UF_MODL_update
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_exp(
char * expr_str  /* <I>
                 Replacement expression.
                 */
);

/****************************************************************************
The input to UF_MODL_eval_exp is a character string containing the
name of the expression. What is returned to the user is the numeric
value of the expression.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_eval_exp(
char * exp_name ,/* <I>
                 Name of expression to be evaluated.
                 */
double * exp_value  /* <O>
                    Result of evaluation.
                    */
);

/****************************************************************************
Exports expressions to a file. You input a file specification (path and
filename).

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_export_exp(
char * file_spec  /* <I>
                  File name specification to export expressions into.
                  NOTE: if the file already exists, an error code is
                  returned and the file is not overwritten.
                  */
);

/****************************************************************************
The input to UF_MODL_ask_exp is a character string containing the
name of the expression. What is returned to the user is the entire
expression string.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_exp(
char * exp_name ,/* <I>
                 Name of expression.
                 */
char exp_defn[ UF_MAX_EXP_BUFSIZE ]  /* <O>
                    Complete expression string. This includes the left
                    hand side, equal sign, and right hand side.
                    */
);

/****************************************************************************
Imports expressions from a file. Input a file specification.  This
routine does not automatically update the database. After you use this
routine, call UF_MODL_update to update the database.

Environment: Internal  and  External
See Also: UF_MODL_update 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_import_exp(
char * file_spec ,/* <I>
                  File name specification to import expressions from.
                  */
int new_def  /* <I>
             Flag designating action to be taken if a name read
             from the file is already used for an expression.
              0 = ok to replace existing definition
              1 = must not exist. If it does, quit reading and give an error.
              2 = delete all imports that are not used.
             */
);

/****************************************************************************
Renames an existing expression. You input the old and new expression names.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_rename_exp(
char * old_exp_name ,/* <I>
                     Name of expression to be renamed.
                     */
char * new_exp_name  /* <I>
                     New name for expression.
                     */
);

/****************************************************************************
Creates a parameter expression, based upon the input string. This
string can be either a numerical value or another expression. The
expression can be named explicitly, by passing in a full expression,
including the name, an = and the expression value, or named automatically,
using the same scheme as is used for feature parameters.

The following call produces an expression tag which evaluates to 42,
and will be named my_exp:
UF_MODL_create_exp_tag( "my_exp=42", &tag1 );

The following call produces an expression tag which evaluates to 42:
UF_MODL_create_exp_tag( "42", &tag1 );

The expression might automatically be named p5 (for example: p5=42).

The next example produces an expression tag which evaluates to 21:
UF_MODL_create_exp_tag( "p5/2", &tag1 );

This expression might be automatically named P6 (for example: p6=p5/2).

Environment: Internal  and  External
See Also:  UF_MODL_create_exp

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_exp_tag(
const char * string ,/* <I>
                     The string for the expression
                     */
tag_t * new_exp  /* <O>
                 The tag of the new expression.
                 */
);

/****************************************************************************
Deletes an expression tag.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_delete_exp_tag(
tag_t old_exp  /* <I>
               Tag to delete.
               */
);

/****************************************************************************
Asks the value of an expression tag.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_exp_tag_value(
tag_t expression_tag ,/* <I>
                      Tag to evaluate.
                      */
double * value  /* <O>
                Value of expression
                */
);

/****************************************************************************
Returns the string that represents an expression. This is of the form:
<name>=<value>.

For example:
        p1=p2+5
        p10=3.1415926

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_exp_tag_string(
tag_t expression_tag ,/* <I>
                      Tag to evaluate.
                      */
char ** string  /* <OF>
                String that represents the expression.  The caller must
                free this by calling UF_free.
                */
);

/****************************************************************************
Dissects an expression character string of the form <left>=<right>
and return its expression tag, <left> character string, and <right>
character string.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_dissect_exp_string(
char * exp_str ,/* <I>
                Expression character string <left>=<right> .
                */
char ** lhs_str ,/* <OF>
                 <left> character string.  This must be freed by the caller
                 by calling UF_free.
                 */
char ** rhs_str ,/* <OF>
                 <right> character string.  This must be freed by the caller
                 by calling UF_free.
                 */
tag_t * exp_tag  /* <O>
                 Tag for the expression.
                 */
);

/****************************************************************************
Returns a parameter suppress expression, based upon the input
feature.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_suppress_exp_tag(
tag_t feature_tag ,/* <I>
                   Feature object id
                   */
tag_t * expression_tag  /* <O>
                        Suppress expression tag
                        */
);

/****************************************************************************
Links the parameter suppress expression to the feature.

The value of the specified expression tag must match the current
suppression state of the specified feature.  If the feature is unsuppressed
then the expression value must be 1.  If feature is suppressed then the
expression value must not be 1.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_set_suppress_exp_tag(
tag_t feature_tag ,/* <I>
                   Feature object id
                   */
tag_t expression_tag  /* <I>
                      Suppress expression tag
                      */
);

/****************************************************************************
Unsets suppress expression tag from the input feature.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_unset_suppress_exp_tag(
tag_t feature_tag  /* <I>
                   Feature object id
                   */
);

/******************************************************************************
Gets all expressions related to the supplied feature.

Environment: Internal  and  External
See Also: UF_MODL_ask_exps_of_part
          UF_MODL_ask_features_of_exp

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_exps_of_feature(
tag_t feature ,/* <I>
               Feature to query
               */
int * number_of_exps ,/* <O>
                      number of expressions returned
                      */
tag_t ** exps  /* <OF,len:number_of_exps>
               Array of expressions related to feature.  This array must
               be freed by calling UF_free.
               */
);

/******************************************************************************
Gets all the numeric expressions of a part.

Environment: Internal  and  External
See Also: UF_MODL_ask_exps_of_feature
          UF_MODL_ask_features_of_exp

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_exps_of_part(
tag_t part_tag ,/* <I>
                Tag of the part to be queried
                */
int * number_of_exps ,/* <O>
                      Number of expressions returned
                      */
tag_t ** exps  /* <OF,len:number_of_exps>
               All the expressions in the part. Use UF_free to
               deallocate memory.
               */
);

/******************************************************************************
Gets all the features that use the supplied expression.

Environment: Internal  and  External
See Also: UF_MODL_ask_exps_of_feature
          UF_MODL_ask_exps_of_part

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_features_of_exp(
tag_t exp ,/* <I>
           Expression to query
           */
int * number_of_features ,/* <O>
                          Number of feature tags returned
                          */
tag_t ** features  /* <OF,len:number_of_features>
                   Features related to given expression.  This array must be
                   freed by calling UF_free.
                   */
);

/******************************************************************************
Returns expressions and expression descriptions related to the
supplied feature.

Environment: Internal  and  External
See Also:
History:Original release was in V14.0. V15.0 change: This function was
   renamed from UF_MODL_ask_exp_desc_of_frec to UF_MODL_ask_exp_desc_of_feat.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_exp_desc_of_feat(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier of created rectangular
                       groove
                       */
int * number_of_exps ,/* <O>
                      Number of expressions returned
                      */
char *** descriptions ,/* <OF,len:number_of_exps> number_of_exps 
                       Array of expression descriptions related to feature.
                       Use UF_free_string_array to deallocate memory when done.
                       */
tag_t ** exps  /* <OF,len:number_of_exps> number_of_exps 
               Array of object identifiers to expressions related to
               feature. Use UF_free to deallocate memory when done.
               */
);

/******************************************************************************
Use UF_MODL_ask_desc_of_feat instead.
Returns expressions and expression descriptions related to the supplied feature.

Environment: Internal  and  External
See Also:
History:Original release was in V14.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_exp_desc_of_frec(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier of created rectangular
                       groove
                       */
int * number_of_exps ,/* <O>
                      Number of expressions returned
                      */
char *** descriptions ,/* <OF,len:number_of_exps> number_of_exps 
                       Array of expression descriptions related to feature.
                       Use UF_free_string_array to deallocate memory when done.
                       */
tag_t ** exps  /* <OF,len:number_of_exps> number_of_exps 
               Array of object identifiers to expressions related to
               feature. Use UF_free to deallocate memory when done.
               */
);

/******************************************************************************
Return the owning feature of the expression.

This is the feature that created it during feature creation.  For example,
the expression "p0 = x" is owned by feature "BLOCK(0)".

This works with both normal expressions and expressions created by the
geometric expression feature.

Environment: Internal and External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_owning_feat_of_exp
(
    tag_t  exp,    /* <I> Expression to query */
    tag_t *feature /* <O> Feature if found else NULL_TAG */
);

/******************************************************************************
Return descriptor of the expression else return NULL.  Currently, only feature
expressions have descriptors.

Environment: Internal and External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_descriptor_of_exp
(
    tag_t   exp,       /* <I> Expression to query */
    char  **descriptor /* <OF> Expression descriptor.  This must be freed
                       by calling UF_free.
                       */
);

/******************************************************************************
Queries whether the specified expression is a geometric expression.

Environment: Internal  and  External
See Also:UF_MODL_ask_owning_feat_of_exp
          
History: This function was originally released in V15.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_geometric_expression
(
    tag_t exp_tag,                /* <I>
                                  Tag of expression to query
                                  */
    logical *flag                 /* <O>
                                  TRUE if this expression is a geometric
                                  expression
                                  */
);

/******************************************************************************
Is the expression in the part?

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_exp_in_part
(
    tag_t       object_in_search_part, /* <I>
                                       determines which part to search in
                                       */
    const char *left_hand_side,        /* <I>
                                       left hand side of expression
                                       */
    logical    *is_exp_in_part         /* <O>
                                       TRUE if expression is in part
                                       */
);

/*****************************************************************************/

/* The structure UF_MODL_dimension_data_s stores the data to create drafting
   dimension data for feature expressions.  The structure is filled by the 
   function UF_MODL_get_dimension_data (see below ). */ 
struct UF_MODL_dimension_data_s {
    int type ;         /* Type of dimension  - 0 - Parallel 
                                               1 - Diameter 
                                               2- angular 
                                               3- Radial 
                                               4 - RPO 
                                               */
    tag_t feature_tag;        /* The tag of the feature associated with the 
                                 dimension */
    double value;             /* The value of the expression from which we 
                                 create the dimension. */    
    double first_point[3];    /* The absolute coordinates of objects used to 
                                 create the dimension.  For a parallel 
                                 dimension this is the first point necessary 
                                 to create the dimension.  For a diameter or
                                 radial dimension this is the center of the 
                                 arc from which we create the dimension. For
                                 an angular or RPO dimension????*/

    double second_point[3];   /* The second point necessary to create the 
                                 parallel dimension. This is unused for the
                                 other types of dimensions. */
    double origin[3];         /* Origin for the dimension placement in 
                                 absolute coordinates. */ 
    double start_angle;       /* Start angle for arc of radial dimensions in radians */
    double end_angle;         /* End angle for arc of radial dimensions in radians */
    tag_t csys_tag;           /* This is the coordinate system which defines 
                                 the XY plane on which the dimension is 
                                 created. */
    char *drf_txt;            /* Dimension text associated with the dimension.
                              */
    tag_t *top_array;         /* <len:num_top_array> Topological information associated with the 
                                 feature (such as faces or edges) which should 
                                 be used to customize the dimension creation by
                                 the user.  This array must be freed by the 
                                 user by calling UF_free. */
    int num_top_array;        /* Number of topological entities returned */
    UF_CURVE_line_t first_line; /* Used only when the dimension is angular,
                                   this is the first line to be created for 
                                   the angular dimension. */
    UF_CURVE_line_t second_line;  /* Used only when the dimension is angular,
                                     this is the Second line to be created for
                                     the angular dimension. */
};
typedef  struct UF_MODL_dimension_data_s UF_MODL_dimension_data_t; 
typedef struct UF_MODL_dimension_data_s *UF_MODL_dimension_data_p_t;


/******************************************************************************
This function is used to extract the data to create a drafting dimension for 
a parametric expression associated with the given feature. 

Note this function can not be used with Extruded Features.

Environment: Internal  and  External
See Also:
History: Originally released in V17.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_get_dimension_data( 
tag_t exp ,          /* <I>  
                       The expression tag for which we want to create the 
                       dimension */
tag_t feature_tag,  /* <I>  
                       The feature which owns the expression.
                    */
                                      
UF_MODL_dimension_data_p_t dim_data /* <OF>  
                                       The structure which contains the
                                       dimension data.  This structure must be
                                       allocated by the user.  The member
                                       array dim_data->top_array must be freed
                                       by calling UF_free. */
                                     );


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_EXPRESSIONS_H_INCLUDED */

