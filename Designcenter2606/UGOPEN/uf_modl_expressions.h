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

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_EXPRESSIONS_H_INCLUDED */

