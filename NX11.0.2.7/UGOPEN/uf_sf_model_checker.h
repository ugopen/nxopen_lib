/*************************************************************************

                    Copyright (c) 2002 Unigraphics Solutions Inc.
                             Unpublished - All rights reserved

**************************************************************************



File description:

This is the Open C interface to the scenario model checker.


**************************************************************************/

#ifndef UF_SF_MODEL_CHECKER_H_INCLUDED
#define UF_SF_MODEL_CHECKER_H_INCLUDED


#include <uf_defs.h>

#include <libufun_cae_exports.h>  /* Keep this include always last */

#ifdef __cplusplus
extern "C" {
#endif

/*  */
#define UF_SF_MAX_NAME_LENGTH MAX_FSPEC_BUFSIZE 
/*  */

/**************************************************
         Element type enum for shape check
 **************************************************/
enum UF_SF_THRESHOLD_shape_e
{
      UF_SF_THRESHOLD_shape_tri3 = 0,
      UF_SF_THRESHOLD_shape_tri6,
      UF_SF_THRESHOLD_shape_quad4,
      UF_SF_THRESHOLD_shape_quad8,
      UF_SF_THRESHOLD_shape_tetra4,
      UF_SF_THRESHOLD_shape_tetra10,
      UF_SF_THRESHOLD_shape_hex8,
      UF_SF_THRESHOLD_shape_hex20,
      UF_SF_THRESHOLD_shape_wdg6,
      UF_SF_THRESHOLD_shape_wdg15,
      UF_SF_THRESHOLD_shape_pyr5,
      UF_SF_THRESHOLD_shape_pyr13,
      UF_SF_THRESHOLD_shape_all
};
typedef enum UF_SF_THRESHOLD_shape_e UF_SF_THRESHOLD_shape_t, *UF_SF_THRESHOLD_shape_p_t;

/**************************************************
      Structure for element shape threshold
 **************************************************/
struct UF_SF_THRESHOLD_data_s {
    int                            shape_option_data;
    int                            previous_shape_data;
    int                            aspect_toggle_data;
    double                         aspect_real_data;
    int                            warp_toggle_data;
    double                         warp_real_data;
    int                            skew_toggle_data;
    double                         skew_real_data;
    int                            taper_toggle_data;
    double                         taper_real_data;
    int                            jacobian_toggle_data;
    double                         jacobian_real_data;
    int                            jacobian_zero_toggle_data;
    double                         jacobian_zero_real_data;
    int                            minmax_angle_toggle_data;
    double                         minimum_angle_real_data;
    double                         maximum_angle_real_data;
    int                            tet_collapse_toggle_data;
    double                         tet_collapse_real_data;
    char                           solver_name[MAX_FSPEC_BUFSIZE];
                                        /* SFOM_LANG_MSC_NASTRAN_NAME   *
                                         * SFOM_LANG_NX_NASTRAN_NAME    *
                                         * SFOM_LANG_DES_NASTRAN_NAME   *
                                         * SFOM_LANG_ANSYS_NAME         *
                                         * SFOM_LANG_ABAQUS_NAME        *
                                         * SFOM_LANG_TMG_NAME           *
                                         * add when we have more        */
};
typedef struct UF_SF_THRESHOLD_data_s UF_SF_THRESHOLD_data_t, *UF_SF_THRESHOLD_data_p_t;

/***************************************************************************

    Definitions and Prototypes for the Open C API routines for
    Optimization in Scenario for Structures.

    Note on Error Handling: All High level Assembly Open C API functions return
        a failure code of non zero if an error is encountered.  A descriptive
        message associated with a failure code can be obtained by calling
        UF_get_fail_message with the failure code as the argument.

*****************************************************************************/


/*************************************************************************
 *  FUNCTION
 *     UF_SF_check_model_comprehensive
 *
 *  DESCRIPTION
 *     This function will run a comprehensive model check on the
 *     current scenario model.
 *
 *  INPUT
 *     detailed_message         TRUE for a more detailed output written
 *                              to output_file_with_path.
 *     output_file_with_path    Full path including filename of file
 *                              where results of model check should be
 *                              written.  Caller is responsible for
 *                              allocating and deallocating this array.
 *
 *  OUTPUT:
 *     none
 *
 *  RETURN
 *    error == 0.
 *            >0 for error
 *************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_check_model_comprehensive
(
   logical detailed_message,         /*<I>*/
   const char *ouput_file_with_path  /*<I>*/
);


/*************************************************************************
 *
 *  FUNCTION
 *      UF_SF_check_model_duplicate_nodes
 *
 *  DESCRIPTION
 *      This function will run a duplicate node model check on the
 *      current scenario model.
 *
 *  INPUT
 *     num_meshes            number of meshes to check.  0 if all
 *                           existing meshes should be checked.
 *     mesh_tags             Array of mesh tags to check.  NULL if
 *                           all existing meshes should be checked.
 *     merge_duplicates      TRUE if duplicates should be merged.
 *                           Otherwise FALSE
 *     tolerance             tolerance to decide if nodes are duplicate.
 *
 *  OUTPUT:
 *    num_duplicates         number of duplicates found and/or merged.
 *
 *  RETURN
 *    error == 0.
 *            >0 for error
 *************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_check_model_duplicate_nodes
(
   int num_meshes,              /*<I>*/
   tag_p_t mesh_tags,           /*<I>*/
   logical merge_duplicates,    /*<I>*/
   double tolerance,            /*<I>*/
   int *num_duplicates          /*<O>*/
);



#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_SF_MODEL_CHECKER_H_INCLUDED */
