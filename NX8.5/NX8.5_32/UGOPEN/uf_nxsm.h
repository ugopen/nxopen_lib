/*****************************************************************************
             Copyright (c) 2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about NX Sheet Metal features.
*****************************************************************************/

#ifndef UF_NXSM_H_INCLUDED
#define UF_NXSM_H_INCLUDED


/*==========================================================================

  ==========================================================================*/

#include <uf_defs.h>
#include <libufun_exports.h>
#include <uf_nxsm_types.h>


#ifdef __cplusplus
extern "C" {
#endif

/*
 *NXSM - TAB FEATURE
 */

/****************************************************************************
This is to initialize the data structure for base tab feature with the
following default values and options. 

    sketch_obj                 NULL_TAG
    sweep_dist                 0.1/3.0 [in/mm]
    sweep_direction[3]         {0.0,0.0,0.0} 
    is_global_thickness        1
    
    
Environment: Internal  and  External
See Also:  UF_NXSM_create_tab
           UF_NXSM_edit_tab
           UF_NXSM_ask_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_tab_data(
UF_NXSM_tab_data_p_t tab_data /* <OF>
                               * The tab data structure to be initialized.
                               */
);

/****************************************************************************
This is to create a NXSM Tab feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_tab
          UF_NXSM_ask_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_tab(
UF_NXSM_tab_data_p_t   tab_data, /* <I>
                                  * Input data to be used to create a tab feature.
                                  */
tag_t  **features       /* <OF>
                         * List of feature identifiers created.  This 
                         * must be freed by caller.
                         */
);

/****************************************************************************
This is to inquire the data for a tab feature.
If a sketch_tag was used to create or edit the base tab, a sketch_tag will be returned from this method.
If a section_tag was used to create or edit the base tab, a section_tag will be returned from this method.

Environment: Internal  and  External
See Also:  UF_NXSM_create_tab
          UF_NXSM_edit_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_tab(
tag_t feature,          /* <I> 
                         * Tab feature to be asked
                         */
UF_NXSM_tab_data_p_t tab_data /* <OF>
                               * Data for the Tab feature.
                               */
);
/****************************************************************************
This is to edit a tab feature with given data.

Environment: Internal  and  External
See Also: UF_NXSM_ask_tab
          UF_NXSM_create_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_tab(
tag_t feature,          /* <I> 
                         * Tab feature to be edited
                         */
UF_NXSM_tab_data_p_t tab_data /* <I>
                               * Data for the Tab feature.
                               */
);

/*
 *NXSM - SECONDARY TAB FEATURE
 */

/****************************************************************************
This is to initialize the data structure for secondary tab feature with the
following default values and options. 

    sketch_profile             NULL_TAG
    placement_face             NULL_TAG
    material_side              IG_LEFT
    
   
Environment: Internal  and  External
See Also:  UF_NXSM_create_sec_tab
           UF_NXSM_edit_sec_tab
           UF_NXSM_ask_sec_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_sec_tab_data(
UF_NXSM_sec_tab_data_p_t tab_data
                        /* <OF>
                        The secondary tab data structure to be initialized.
                        */
);

/****************************************************************************
This is to create a NXSM Secondary Tab feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_sec_tab,
           UF_NXSM_ask_sec_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_sec_tab(
UF_NXSM_sec_tab_data_p_t   sec_tab_data, 
                        /* <I>
                        Input data to be used to create a secondary tab feature.
                        */
tag_t  **features       /* <OF>
                        List of feature identifiers created.  This 
                        must be freed by caller.
                        */
);

/****************************************************************************
This is to inquire the data for a secondary tab feature.
If a sketch_tag to create or edit the secondary tab, a sketch_tag will be returned from this method.
If a section_tag to create or edit the secondary tab, a section_tag will be returned from this method.

Environment: Internal  and  External
See Also:  UF_NXSM_create_sec_tab
           UF_NXSM_edit_sec_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_sec_tab(
tag_t feature,          /* <I> 
                        Tab feature to be asked */
UF_NXSM_sec_tab_data_p_t sec_tab_data 
                        /* <OF>
                        Data for the secondary tab feature.
                        */
);
/****************************************************************************
This is to edit a secondary tab feature with given data.  

Environment: Internal  and  External
See Also:  UF_NXSM_ask_sec_tab
           UF_NXSM_create_sec_tab

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_sec_tab(
tag_t feature,          /* <I> 
                        Tab feature to be edited*/
UF_NXSM_sec_tab_data_p_t sec_tab_data 
                        /* <I>
                        Data for the Tab feature.
                        */
);

/*
 *NXSM - BEND FEATURE
 */

/****************************************************************************
This is to initialize the data structure for bend feature with the following 
default values and options. 

    sketch_section                         NULL_TAG  
    bend_angle                             90 degrees.
    bend_dir                               IG_NORMAL_SIDEDUMMY
    fixed_side                             IG_LEFT
    material_side                          IG_RIGHT
    extend_option                          IG_EXTEND

    bend_options.bend_radius                3.0 / 0.1 [mm/in]
    bend_options.is_bend_radius_global      TRUE
    bend_options.bend_relief                FALSE
    bend_options.extend_bend_relief         FALSE
    bend_options.bend_relief_type           IG_RECTANGULAR_BEND_RELIEF
    bend_options.bend_relief_depth          3.0 / 0.1 [mm/in]
    bend_options.bend_relief_depth_global   TRUE
    bend_options.bend_relief_width          3.0 / 0.1 [mm/in]
    bend_options.bend_relief_width_global   TRUE
    bend_options.corner_relief              FALSE
    bend_options.corner_relief_type         IG_RIP_CORNER_RELIEF
    bend_options.neutral_factor             TRUE
    bend_options.neutral_factor_global      0.3333333
         
  
Environment: Internal  and  External
See Also:  UF_NXSM_create_sec_cflange,
           UF_NXSM_edit_sec_cflange
           UF_NXSM_ask_sec_cflange
        
History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_bend_data(
UF_NXSM_bend_data_p_t bend_data
                        /* <OF>
                        bend data structure to be initialized.
                        */
);

/****************************************************************************
This is to create a NXSM bend feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_bend
           UF_NXSM_ask_bend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_bend(
    UF_NXSM_bend_data_p_t  bend_data, 
                        /* <I>
                        Input data to be used to create a bend feature.
                        */
   
    tag_t  **features   /* <OF>
                           List of feature identifiers created.  This 
                           must be freed by caller.
                        */
   
);

/****************************************************************************
This is to inquire the data for NXSM Bend feature.
If a sketch_tag was used to create or edit the bend, a sketch_tag will be returned from this method.
If a section_tag was used to create or edit the bend, a section_tag will be returned from this method.


Environment: Internal  and  External
See Also:  UF_NXSM_create_bend
           UF_NXSM_edit_bend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_bend(
tag_t feature,          /* <I> 
                         * bend feature to be asked
                         */
UF_NXSM_bend_data_p_t bend_data /* <OF>
                               * Data for the bend feature.
                               */
);

/****************************************************************************
This is to edit a NXSM bend feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_bend
           UF_NXSM_create_bend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_bend(
tag_t feature,          /* <I> 
                         * Bend feature to be asked
                         */
UF_NXSM_bend_data_p_t bend_data /* <I>
                               * Data for the bend feature.
                               */
);


/*
 *NX - CLOSED CORNER FEATURE
 */

/****************************************************************************
This is to initialize the data structure for closed corner feature with the
following default values and options. 

    n_edges = 0;            
    parent_edges = NULL;    
    treatment_type = IG_TREATMENT_OFF;
    closure_type = IG_CLOSE_CORNER_NONE;
    treatment_dia = 0.0;
    overlap_ratio = 0.0;
    corner_gap = 0.0;       

Environment: Internal  and  External
See Also:  UF_NXSM_create_closed_corner
           UF_NXSM_edit_closed_corner
           UF_NXSM_ask_closed_corner

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_closed_corner_data(
UF_NXSM_closed_corner_data_p_t clcorner_data /* <OF>
                                     *   The clcorner data structure to be initialized.
                                     */
);

/****************************************************************************
This is to create a NXSM closed corner feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_closed_corner
           UF_NXSM_ask_closed_corner

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_closed_corner(
UF_NXSM_closed_corner_data_p_t   clcorner_data,  /* <I>
                                         *   Input data to be used to create a clcorner feature.
                                         */
tag_t  **features       /* <OF>
                         * List of feature identifiers created.  This 
                         * must be freed by caller.
                         */
);

/****************************************************************************
This is to inquire the data for a closed corner feature.

Environment: Internal  and  External
See Also:  UF_NXSM_create_closed_corner
           UF_NXSM_edit_closed_corner

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_closed_corner(
tag_t feature,          /* <I> 
                         * clcorner feature to be asked 
                         */
UF_NXSM_closed_corner_data_p_t clcorner_data 
                        /* <OF>
                         * Data for the clcorner feature.
                         */
);

/****************************************************************************
This is to edit a closed corner feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_closed_corner 
           UF_NXSM_create_closed_corner

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_closed_corner(
tag_t feature,          /* <I> 
                         * clcorner feature to be edited
                         */
UF_NXSM_closed_corner_data_p_t clcorner_data 
                        /* <I>
                         * Data for the clcorner feature.
                         */
);

/****************************************************************************
This is to free the data structure for closed corner feature. 

Environment: Internal  and  External
See Also:  UF_NXSM_create_closed_corner
           UF_NXSM_edit_closed_corner
           UF_NXSM_ask_closed_corner

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_free_closed_corner_data(
UF_NXSM_closed_corner_data_p_t clcorner_data /* <I>
                                     *   The clcorner data structure to be freed.
                                     */
);

/*
 *NX - UNBEND FEATURE
 */

/****************************************************************************
This is to initialize the data structure for base unbend feature with the
following default values and options. 

    tag_t face_collector    = NULL_TAG;
    tag_t ref_entity    = NULL_TAG;
    int   nbend         = 0;
    tag_t *bend_list    = NULL;
    tag_t body = NULL_TAG;


Environment: Internal  and  External
See Also:  UF_NXSM_create_unbend
           UF_NXSM_edit_unbend
           UF_NXSM_ask_unbend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_unbend_data(
UF_NXSM_unbend_data_p_t unbend_data /* <OF>
                                     *   The unbend data structure to be initialized.
                                     */
);

/****************************************************************************
This is to create a NXSM unbend feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_unbend
           UF_NXSM_ask_unbend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_unbend(
UF_NXSM_unbend_data_p_t   unbend_data,  /* <I>
                                         *   Input data to be used to create a unbend feature.
                                         */
tag_t  **features       /* <OF>
                         * List of feature identifiers created.  This 
                         * must be freed by caller.
                         */
);

/****************************************************************************
This is to inquire the data for a unbend feature.

Environment: Internal  and  External
See Also:  UF_NXSM_create_unbend
           UF_NXSM_edit_unbend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_unbend(
tag_t feature,          /* <I> 
                         * unbend feature to be asked 
                         */
UF_NXSM_unbend_data_p_t unbend_data 
                        /* <OF>
                         * Data for the unbend feature.
                         */
);

/****************************************************************************
This is to edit a unbend feature with given data.

Environment: Internal  and  External
See Also: UF_NXSM_ask_unbend
          UF_NXSM_create_unbend


History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_unbend(
tag_t feature,          /* <I> 
                         * unbend feature to be edited
                         */
UF_NXSM_unbend_data_p_t unbend_data 
                        /* <I>
                         * Data for the unbend feature.
                         */
);

/****************************************************************************
This is to free the data structure for unbend feature. 

Environment: Internal  and  External
See Also:  UF_NXSM_create_unbend
           UF_NXSM_edit_unbend
           UF_NXSM_ask_unbend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_free_unbend_data(
UF_NXSM_unbend_data_p_t unbend_data /* <I>
                                     *   The unbend data structure to be freed.
                                     */
);

/*
 *NX - REBEND FEATURE
 */

/****************************************************************************
This is to initialize the data structure for base rebend feature with the
following default values and options. 

    tag_t face_collector    = NUL_TAG;
    int   nbend         = 0;
    tag_t *unbend_list    = NULL;

Environment: Internal  and  External
See Also:  UF_NXSM_create_rebend
           UF_NXSM_edit_rebend
           UF_NXSM_ask_rebend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_rebend_data(
UF_NXSM_rebend_data_p_t rebend_data /* <OF>
                                     *   The rebend data structure to be initialized.
                                     */
);

/****************************************************************************
This is to create a NXSM rebend feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_rebend  
           UF_NXSM_ask_rebend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_rebend(
UF_NXSM_rebend_data_p_t   rebend_data,  /* <I>
                                         *   Input data to be used to create a rebend feature.
                                         */
tag_t  **features       /* <OF>
                         * List of feature identifiers created.  This 
                         * must be freed by caller.
                         */
);

/****************************************************************************
This is to inquire the data for a rebend feature.

Environment: Internal  and  External
See Also:  UF_NXSM_create_rebend
          UF_NXSM_edit_rebend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_rebend(
tag_t feature,          /* <I> 
                         * rebend feature to be asked 
                         */
UF_NXSM_rebend_data_p_t rebend_data 
                        /* <OF>
                         * Data for the rebend feature.
                         */
);
/****************************************************************************
This is to edit a rebend feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_rebend
           UF_NXSM_create_rebend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_rebend(
tag_t feature,          /* <I> 
                         * rebend feature to be edited
                         */
UF_NXSM_rebend_data_p_t rebend_data 
                        /* <I>
                         * Data for the rebend feature.
                         */
);

/****************************************************************************
This is to free the data structure for rebend feature. 

Environment: Internal  and  External
See Also:  UF_NXSM_create_unbend
           UF_NXSM_edit_unbend
           UF_NXSM_ask_unbend

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_free_rebend_data(
UF_NXSM_rebend_data_p_t rebend_data /* <I>
                                     *   The rebend data structure to be freed.
                                     */
);

/*
 *NXSM - FLANGE FEATURE
 */

/****************************************************************************
This is to initialize the data structure for flange feature with the
following default values and options. 

    parent_edge = NULL_TAG;
    sketch_tag = NULL_TAG;    
    br_type = IG_RECTANGULAR_BEND_RELIEF;
    cr_type = IG_RIP_CORNER_RELIEF;
    off_type = IG_NONE;
    material_side = IG_LEFT;

    bend_rad = "0.1";
    br_width = "0.1";
    br_length = "0.1";
    off_val = "0.01";       
    n_factor = "0.33";
    angle = "0.0";
    extend_bend_relief = false;

    use_global_radius_value = false;
    use_global_br_width_value = false;
    use_global_br_length_value = false;
    use_global_nfactor_value = false;    

Environment: Internal  and  External
See Also:  UF_NXSM_create_flange
           UF_NXSM_edit_flange
           UF_NXSM_ask_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_flange_data(
UF_NXSM_flange_data_p_t flange_data /* <OF> 
                                     *   The flange data structure to be initialized.
                                     */
);

/****************************************************************************
This is to initialize the data structure for the sketch to be used for flange feature with the
following default values and options. 

    at_start_point = false;
    dim_option = IG_OUTSIDE_DIMENSION;
    width_option = FULL_WIDTH_TYPE;
    prev_width_option = OPTION_NOT_SET;

    length = "0.0";
    width = "0.0";
    dist_from_end = "0.0";
    dist_from_left_end = "0.0";       
    dist_from_right_end = "0.0";       

Environment: Internal  and  External
See Also:  UF_NXSM_create_flange
           UF_NXSM_edit_flange
           UF_NXSM_ask_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_flange_sketch_data(
UF_NXSM_flange_sketch_data_p_t sketch_data /* <OF>
                                            *   The data structure for flange sketchto be initialized.
                                            */
);

/****************************************************************************
This is to create a NXSM flange feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_flange
           UF_NXSM_ask_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_flange(
UF_NXSM_flange_data_p_t   flange_data,  /* <I>
                                         *   Input data to be used to create a flange feature.
                                         */
UF_NXSM_flange_sketch_data_p_t   sketch_data,  /* <I>
                                                *   Input data for a sketch to be used to create a flange feature.
                                                */
tag_t  **features       /* <OF>
                         * List of feature identifiers created.  This 
                         * must be freed by caller.
                         */
);

/****************************************************************************
This is to inquire the data for a flange feature.

Environment: Internal  and  External
See Also:  UF_NXSM_create_flange
           UF_NXSM_edit_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_flange(
tag_t feature,          /* <I> 
                         * flange feature to be asked 
                         */
UF_NXSM_flange_data_p_t flange_data, 
                        /* <O>
                         * Data for the flange feature.
                         */
UF_NXSM_flange_sketch_data_p_t sketch_data
                        /* <O>
                         * Data for sketch of the flange feature.
                         */
);

/****************************************************************************
This is to edit a flange feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_flange 
           UF_NXSM_create_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_flange(
tag_t feature,          /* <I> 
                         * flange feature to be edited
                         */
UF_NXSM_flange_data_p_t flange_data,
                        /* <I>
                         * Data for the flange feature.
                         */
UF_NXSM_flange_sketch_data_p_t sketch_data 
                        /* <I>
                         * Data for sketch of the flange feature.
                         */
);

/****************************************************************************
This is to initialize the data structure for flange feature returned by the query method. 

Environment: Internal  and  External
See Also:  UF_NXSM_create_flange
           UF_NXSM_edit_flange
           UF_NXSM_ask_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_free_flange_data(
UF_NXSM_flange_data_p_t flange_data /* <I>
                                     *   The flange data structure to be freed.
                                     */
);

/****************************************************************************
This is to free the data structure for the sketch returned by the query method. 

Environment: Internal  and  External
See Also:  UF_NXSM_create_flange
           UF_NXSM_edit_flange
           UF_NXSM_ask_flange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_free_flange_sketch_data(
UF_NXSM_flange_sketch_data_p_t sketch_data /* <I>
                                            *   The data structure for flange sketch to be freed.
                                            */
);

/*
 *NXSM - BASE CONTOUR FLANGE FEATURE
 */

/****************************************************************************
This is to initialize the data structure for base contour flange feature with the
following default values and options. 

    sketch_section                              NULL_TAG
    thickness                                   0.00
    thickness_side                              IG_LEFT
    projection_dist                             0.1/3.0 [in/mm]
    projection_side                             IG_LEFT
    extent_type                                 IG_FINITE
    bend_parm_type                              IG_NFTYPE
    mitre_data.mitre_position                   IG_NONE
    mitre_data.mitre_type_at_start              IG_MITRE_NORMAL_TO_THICKNESS
    mitre_data.mitre_type_at_end                IG_MITRE_NORMAL_TO_THICKNESS
    mitre_data.mitre_side_at_start              IG_INSIDE
    mitre_data.mitre_side_at_end                IG_INSIDE
    mitre_data.mitre_by_dist_or_angle_at_start  IG_MITRE_BY_ANGLE
    mitre_data.mitre_by_dist_or_angle_at_start  IG_MITRE_BY_ANGLE
    mitre_data.mitre_angle_at_start             -45.0
    mitre_data.mitre_angle_at_end               -45.0
    mitre_data.mitre_cut_type                   IG_MITRE_REGULAR_CUT
    mitre_data.close_corner_type                IG_CLOSE_CORNER_NONE 
    mitre_data.close_corner_dia                 0.00   
    bend_options.bend_radius                    3.0 / 0.1  [mm/in]
    bend_options.is_bend_radius_global          TRUE
    bend_options.bend_relief                    FALSE
    bend_options.extend_bend_relief             FALSE
    bend_options.bend_relief_type               IG_RECTANGULAR_BEND_RELIEF
    bend_options.bend_relief_depth              3.0 / 0.1 [mm/in]
    bend_options.bend_relief_depth_global       TRUE
    bend_options.bend_relief_width              3.0 / 0.1 [mm/in]
    bend_options.bend_relief_width_global       TRUE
    bend_options.corner_relief                  FALSE
    bend_options.corner_relief_type             IG_RIP_CORNER_RELIEF
    bend_options.neutral_factor                 0.33333    
    bend_options.neutral_factor_global          TRUE
    is_global_thickness                         1    

Environment: Internal  and  External
See Also:  UF_NXSM_create_base_cflange
           UF_NXSM_edit_base_cflange
           UF_NXSM_ask_base_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_base_cflange_data(
UF_NXSM_base_cflange_data_p_t base_cflange_data
                        /* <OF>
                        The base_cflange data structure to be initialized.
                        */
);


/****************************************************************************
This is to create a NXSM base contour flange feature based on the input data. 

Environment: Internal  and  External
See Also:
           UF_NXSM_edit_base_cflange
           UF_NXSM_ask_base_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_base_cflange(
UF_NXSM_base_cflange_data_p_t  base_cflange_data, 
                        /* <I>
                        Input data to be used to create a base contour flange feature.
                        */
tag_t  **features      /* <OF>
                        List of feature identifiers created.  This 
                        must be freed by caller.
                        */
);

/****************************************************************************
This is to edit a base contour flange feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_base_cflange
           UF_NXSM_create_base_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_base_cflange(
tag_t feature,          /* <I> 
                         * Base contour flange feature to be edited
                         */
UF_NXSM_base_cflange_data_p_t base_cflange_data /* <I>
                               * Data for the base contour flange feature.
                               */
);

/****************************************************************************
This is to inquire the data for a feature.


Environment: Internal  and  External
See Also:  UF_NXSM_create_base_cflange
           UF_NXSM_edit_base_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_base_cflange(
tag_t feature,          /* <I> 
                         * Base contour flange feature to be asked
                         */
UF_NXSM_base_cflange_data_p_t base_cflange_data /* <OF>
                               * Data for the base contour flange feature.
*/
);



/*
 *NXSM - SECONDARY CONTOUR FLANGE FEATURE
 */

/****************************************************************************
This is to initialize the data structure for secondary contour flange feature with the
following default values and options. 

    sketch_section                              NULL_TAG
    ref_edge                                    NULL_TAG     
    section_edges                               NULL
    profile_ref_end                             IG_INSIDE
    projection_dist                             25.4 / 1.0 [mm/in]
    projection_side                             IG_LEFT
    extent_type                                 IG_FINITE
    bend_parm_type                              IG_NFTYPE
    mitre_data.mitre_position                   IG_NONE
    mitre_data.mitre_type_at_start              IG_MITRE_NORMAL_TO_THICKNESS
    mitre_data.mitre_type_at_end                IG_MITRE_NORMAL_TO_THICKNESS
    mitre_data.mitre_side_at_start              IG_INSIDE
    mitre_data.mitre_side_at_end                IG_INSIDE
    mitre_data.mitre_by_dist_or_angle_at_start  IG_MITRE_BY_ANGLE
    mitre_data.mitre_by_dist_or_angle_at_start  IG_MITRE_BY_ANGLE
    mitre_data.mitre_angle_at_start             -45.0 degrees
    mitre_data.mitre_angle_at_end               -45.0 degrees 
    mitre_data.mitre_cut_type                   IG_MITRE_REGULAR_CUT
    mitre_data.close_corner_type                IG_CLOSE_CORNER_NONE 
    mitre_data.close_corner_dia                 0.00   [mm/in]
    bend_options.bend_radius                    3.0 / 0.1  [mm/in]
    bend_options.is_bend_radius_global          TRUE
    bend_options.bend_relief                    FALSE
    bend_options.extend_bend_relief             FALSE
    bend_options.bend_relief_type               IG_RECTANGULAR_BEND_RELIEF
    bend_options.bend_relief_depth              3.0 / 0.1 [mm/in]
    bend_options.bend_relief_depth_global       TRUE
    bend_options.bend_relief_width              3.0 / 0.1 [mm/in]
    bend_options.bend_relief_width_global       TRUE
    bend_options.corner_relief                  FALSE
    bend_options.corner_relief_type             IG_RIP_CORNER_RELIEF
    bend_options.neutral_factor                 0.33333    
    bend_options.neutral_factor_global          TRUE
    
        
    
Environment: Internal  and  External
See Also:  UF_NXSM_create_sec_cflange
           UF_NXSM_edit_sec_cflange
           UF_NXSM_ask_sec_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_init_sec_cflange_data(
UF_NXSM_sec_cflange_data_p_t sec_cflange_data
                        /* <OF>
                        The secondary cflange data structure to be initialized.
                        */
);

/****************************************************************************
This is to create a NXSM secondary contour flange feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_edit_sec_cflange
           UF_NXSM_ask_sec_cflange

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_create_sec_cflange(
    UF_NXSM_sec_cflange_data_p_t  sec_cflange_data, 
                        /* <I>
                        Input data to be used to create a secondary contour flange feature.
                        */
    tag_t  **features   /* <OF>
                           List of feature identifiers created.  This 
                           must be freed by caller.
                        */
);

/****************************************************************************
This is to edit a secondary contour flange feature with given data.

Environment: Internal  and  External
See Also:  UF_NXSM_ask_sec_cflange
           UF_NXSM_create_sec_cflange

History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_edit_sec_cflange(
tag_t feature,          /* <I> 
                         * Secondary contour flange feature to be asked
                         */
UF_NXSM_sec_cflange_data_p_t sec_cflange_data /* <I>
                               * Data for the Secondary contour flange feature.
                               */

);

/****************************************************************************
This is to inquire the data for a Secondary Contour Flange feature.

Environment: Internal  and  External
See Also:  UF_NXSM_create_sec_cflange
           UF_NXSM_edit_sec_cflange

History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_ask_sec_cflange(
tag_t feature,          /* <I> 
                         * secondary contour flange feature to be asked
                         */
UF_NXSM_sec_cflange_data_p_t sec_cflange_data /* <OF>
                               * Data for the secondary contour flange feature.
                               */
);


/*
 *NXSM - FLATTEN FEATURE
 */

/****************************************************************************
This is to initialize the data structure for flatten feature with the
following default values and options.

    face_tag          NULL_TAG
    edge_tag          NULL_TAG
    is_start_vertex   0

Environment: Internal  and  External
See Also: UF_NXSM_create_flat_solid
          
History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_init_flat_solid(
UF_NXSM_flat_solid_data_p_t flat_solid_data
                        /* <I/O>
                        The flatten data structure to be initialized.
                        */
);



/****************************************************************************
This is to create a SBSM flatten feature based on the input data. 

Environment: Internal  and  External
See Also:  UF_NXSM_init_flat_solid
       
History:New in NX3.0

 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_create_flat_solid(
    UF_NXSM_flat_solid_data_p_t  flat_solid_data, 
                        /* <I>
                        Input data to be used to create a flatten feature.
                        */
   
    tag_t  **features   /* <OF> 
                           List of feature identifiers created.  This 
                           must be freed by caller.
                           Use SM_free( ) to free the features
                        */
);


/****************************************************************************
This is to inquire the data for a flatten feature.

Environment: Internal  and  External
See Also: UF_NXSM_create_flat_solid
          UF_NXSM_edit_flat_solid
History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_flat_solid(
            tag_t feature, /* <I> 
                            * Flatten feature to be asked
                            */       
            UF_NXSM_flat_solid_data_p_t flat_solid_data     /* <OF>
                                                             * Data for the Flatten feature.
                                                             */
            );


/****************************************************************************
This is to edit a Flatten feature with given data.
On Success returns 0.

Environment: Internal  and  External
See Also: UF_NXSM_ask_flat_solid
          UF_NXSM_create_flat_solid
History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_edit_flat_solid(
        tag_t features, /* <I> 
                         * Flatten feature to be edited */

        UF_NXSM_flat_solid_data_p_t get_flat_solid_data  /* <I>
                               * Data for the Flatten feature. */
        );




/*
 *NXSM - JOG FEATURE
 */

/****************************************************************************
This is to initialize the data structure for jog feature with the following 
default values and options. 

    sketch_tag                                 NULL_TAG
    offset_dist                                25.4/1.00 [mm/in]
    offset_type                                IG_OFFSET
    fixed_side                                 IG_LEFT
    material_side                              IG_INSIDE
    extend_option                              IG_EXTEND 
    
    bend_options.bend_radius                   3.0 / 0.1 [mm/in]
    bend_options.is_bend_radius_global         TRUE
    bend_options.bend_relief                   FALSE
    bend_options.extend_bend_relief            FALSE
    bend_options.bend_relief_type              IG_RIP_BEND_RELIEF
    bend_options.bend_relief_depth             3.0 / 0.1 [mm/in]
    bend_options.bend_relief_depth_global      TRUE
    bend_options.bend_relief_width             3.0 / 0.1 [mm/in]
    bend_options.bend_relief_width_global      TRUE
    bend_options.corner_relief                 FALSE
    bend_options.corner_relief_type            IG_RIP_CORNER_RELIEF
    bend_options.neutral_factor                TRUE
    bend_options.neutral_factor_global         0.3333333
         
  
Environment: Internal  and  External
See Also: UF_NXSM_create_jog
          UF_NXSM_edit_jog
          UF_NXSM_ask_jog

History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_init_jog(
UF_NXSM_jog_data_p_t jog_data
                        /* <I/O>
                        The jog data structure to be initialized.
                        */
);


/****************************************************************************
This is to create a SBSM jog feature based on the input data. 


Environment: Internal  and  External
See Also: UF_NXSM_edit_jog
          UF_NXSM_ask_jog

History:New in NX3.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_create_jog(
    UF_NXSM_jog_data_p_t  jog_data, 
                        /* <I>
                        Input data to be used to create a jog feature.
                        */
   
    tag_t  **features   /* <OF> 
                           List of feature identifiers created.  This 
                           must be freed by caller.
                           Use SM_free( ) to free the features
                        */
);


/****************************************************************************
This is to inquire the data for a jog feature.
If a sketch_tag was used to create or edit the jog, a sketch_tag will be returned from this method.
If a section_tag was used to create or edit the jog, a section_tag will be returned from this method.

Environment: Internal  and  External
See Also: UF_NXSM_create_jog
          UF_NXSM_edit_jog

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_ask_jog(
tag_t feature,          /* <I> 
                         * Jog feature to be asked
                         */
UF_NXSM_jog_data_p_t jog_data /* <OF>
                               * Data for the Jog feature.
                               */
);
/****************************************************************************
This is to edit a jog feature with given data.

Environment: Internal  and  External
See Also: UF_NXSM_ask_jog
          UF_NXSM_create_jog

History:New in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_NXSM_edit_jog(
tag_t feature,          /* <I> 
                         * Jog feature to be edited */
                         
UF_NXSM_jog_data_p_t jog_data /* <I>
                               * Data for the jog feature. */
                               
);

/****************************************************************************
This is used to get a corner edge given its associated bend faces.

History:New in NX5.0
 ***************************************************************************/

extern UFUNEXPORT int UF_NXSM_get_qualified_corner_edge
(tag_t bend_face1,/*<I> 
                    * Bend face adjacent to a corner edge
                    */ 
 tag_t bend_face2, /*<I> 
                   * Another bend face adjacent to a corner edge
                   */
 logical is_3flange_feature,/* <I>
                            * True if the corner is of 3 bend   
                            */
 tag_t* corner_edge/*<O>
                   * Corner edge of the associated bend faces
                   */ );


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_NXSM_H_INCLUDED */





