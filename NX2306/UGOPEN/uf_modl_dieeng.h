/*****************************************************************************
             Copyright (c) 2001-2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to inquire about die engineering features.
*****************************************************************************/

#ifndef UF_MODL_DIEENG_H_INCLUDED
#define UF_MODL_DIEENG_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libufun_die_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/* 
   Following is a structure definition for die tip feature inquiry data. 
   It contains all the information needed to define the product orientation
   in the die.
*/

struct UF_MODL_die_tip_info_s
{
   tag_t product;                    /* Tag of product body being tipped */
   double origin[3];                 /* origin on product body that is
                                        mapped to center of operation box */
   double center[3];                 /* center of operation box */
   tag_t defining_tip_feature;       /* tag of feature that actually 
                                        defined the product orientation, 
                                        NULL_TAG if this feature defined 
                                        the product orientation */
   double trans[3];                  /* translation from center of die */
   int num_trans_reasons;            /* number of strings in following array,
                                        will be 0 if no reasons supplied */  
   char **trans_reasons;             /* <len:num_trans_reasons> 
                                        reasons supplied for translation,
                                        will be NULL if no reason,
                                        the memory for these strings should
                                        be freed by calling UF_free */
   int num_steps;                    /* number of steps in the product 
                                        orientation definition, also the 
                                        size of the following arrays */
   int *rot_axis;                    /* <len:num_steps> 
                                        for each step, the axis the
                                        rotation is performed about
                                        =0 -> X
                                        =1 -> Y
                                        =2 -> Z
                                        =3 -> -X
                                        =4 -> -Y
                                        =5 -> -Z,
                                        the memory for this array should
                                        be freed by calling UF_free */
   double *rot_angle;                /* <len:num_steps> 
                                        for each step, the angle of
                                        rotation in degrees, the memory 
                                        for this array should be freed 
                                        by calling UF_free */
   int *num_rot_reasons;             /* <len:num_steps> 
                                        number of reasons for each step,
                                        will be 0 if no reasons supplied 
                                        for a step, the memory for this
                                        array should be freed by 
                                        calling UF_free */
   char ***rot_reasons;              /* <len:num_rot_reasons> 
                                        for each step, the reasons supplied
                                        for the rotation, an entry will
                                        be NULL if no reasons, the memory
                                        for each string should be freed
                                        by calling UF_free, the string array
                                        should be freed by calling UF_free,
                                        and the complete array should also be
                                        freed by calling UF_free
                                        (e.g., UF_free(rot_reasons[0..n][0..n]);,
                                        UF_free(rot_reasons[0..n]);
                                        and UF_free(rot_reasons);) */
};
typedef struct UF_MODL_die_tip_info_s UF_MODL_die_tip_info_t, 
*UF_MODL_die_tip_info_p_t;

/****************************************************************************
Outputs the product orientation information for the input die tip feature.

Return: error code

Environment: Internal  and  External

History: Original release was in V19.0
 ***************************************************************************/
extern UFUN_DIEEXPORT int UF_MODL_ask_die_tip(
    tag_t die_tip_feature, /* <I>
                              die tip feature to inquire
                           */
    UF_MODL_die_tip_info_p_t die_tip_info/* <OF>
                                die tip information
                             */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_DIEENG_H_INCLUDED */
