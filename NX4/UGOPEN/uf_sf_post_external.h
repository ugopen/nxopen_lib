/*****************************************************************************
             Copyright (c) 1998-2003 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       


  
File Description:

 Open C API interface to the Post Processor for Scenario product

Overview:
---------

Concepts:
---------

See the Scenario for FEA User Manual for details on
post processing

Requirements:
------------
As with any user function, you must first call UF_SF_initialize_post_processor()
before calling any user function defined in this header.

 End User Functions equivalent to Scenario dialogs:
 
   Scenario Post:
     UF_SF_POST_display_results
     UF_SF_POST_select_results
     UF_SF_POST_initialise_result_parms
     UF_SF_POST_get_result_params
     UF_SF_POST_get_unit_tag
     UF_SF_POST_set_fringe_params
     UF_SF_POST_initialise_fringe_params
     UF_SF_POST_export_vrml
     UF_SF_POST_export_display_to_text
     UF_SF_POST_set_def_disp_params
     UF_SF_POST_set_undef_disp_params
     UF_SF_POST_initialise_def_disp_params
     UF_SF_POST_initialise_def_scale_params
     UF_SF_POST_initialise_undef_disp_params
     UF_SF_POST_initialise_clip_params
     UF_SF_POST_initialise_ident_params
     UF_SF_POST_write_ident_data
     UF_SF_POST_initialise_deformed_result_params
     UF_SF_POST_select_deformed_results
     UF_SF_POST_set_clipping
     UF_SF_POST_create_combined_lcase
     UF_SF_POST_delete_combined_lcase
     UF_SF_POST_get_component_unit_tag
     UF_SF_POST_overlay
     UF_SF_POST_remove_overlay
     UF_SF_POST_exit_overlay

******************************************************************************/

#ifndef  UF_SF_POST_EXTERNAL__H_INCLUDED
#define  UF_SF_POST_EXTERNAL__H_INCLUDED

#include <uf_sf_post_datatypes.h>
#include <libufun_exports.h>  /* Keep this include always last */


/****************************************************************************

 **************************************************************************/
#define ERROR_UF_SFEM_base     1765000 

#define   UF_SF_POST_INVALID_MODEL                (ERROR_UF_SFEM_base + 125)
#define   UF_SF_POST_RESULTS_NOT_FOUND            (ERROR_UF_SFEM_base + 126)
#define   UF_SF_POST_INVALID_RESULTS_TYPES        (ERROR_UF_SFEM_base + 127)

#define   UF_SF_FAILED                             1

#ifdef __cplusplus
extern "C" {
#endif


/*************************************************************************
*  displays the model with the current values of result.
*
* Environment:  Internal and External
*
* History: Originally released in NX3
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_display_results(void);


/***************************************************************************
* sets the result structure with the obtained data from the user
*
* Environment:  Internal and External
*
* History: Originally released in NX3
***************************************************************************/ 
extern UFUNEXPORT int UF_SF_POST_select_results(
      UF_SF_POST_result_parms_t_p result_params/* <I> Parameters for selecting results 
                                              Use function UF_SF_initialise_result_parms 
                                              to set this structure */ 
                                               );

/***************************************************************************
*  initialises the UF_SF_POST_result_parms_t_p structure with
*  user given values. To be called before a call to UF_SF_POST_select_results
*
* Environment:  Internal and External
*
* History: Originally released in NX3
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_result_parms
(
   UF_SF_POST_result_parms_t_p*    res_params,/* <OF> Parameters for selecting results */
   int                             abs_sw,    /* <I> 1 if results are requested in absolute,
                                                 0 otherwise */
   int                             avg_sw,    /*<I> 1 if results are requested in absolute, 0 otherwise */ 
   int                             lcase,     /*<I> Load Case number. Index starts from 0 */ 
   int                             iter,      /*<I> Valid for optimization,0 in othercases */
   double                          scale,     /*<I> Scale to display results*/
   UF_SF_POST_coord_sys_type_t     coords,    /*<I> Type of coordinate system
                                                    UF_SF_POST_ABS_RECTANGULAR, 
                                                    UF_SF_POST_ABS_CYLINDRICAL, 
                                                    UF_SF_POST_ABS_SPHERICAL, 
                                                    UF_SF_POST_WRK_RECTANGULAR, 
                                                    UF_SF_POST_WRK_CYLINDRICAL, 
                                                    UF_SF_POST_WRK_SPHERICAL, 
                                                    UF_SF_POST_LOCAL*/ 
   UF_SF_POST_result_type_quan_t   quan,  /*<I> Type of results to set
                                                    UF_SF_POST_DISPLACEMENT, 
                                                    UF_SF_POST_ROTATION, 
                                                    UF_SF_POST_CONTACT_DISP, 
                                                    UF_SF_POST_VELOCITY, 
                                                    UF_SF_POST_ACCELERATION, 
                                                    UF_SF_POST_STRESS, 
                                                    UF_SF_POST_STRAIN, 
                                                    UF_SF_POST_STRAIN_E, 
                                                    UF_SF_POST_STRAIN_ED, 
                                                    UF_SF_POST_STRAIN_EE, 
                                                    UF_SF_POST_THICKNESS, 
                                                    UF_SF_POST_TEMPERATURE, 
                                                    UF_SF_POST_TEMP_GRAD, 
                                                    UF_SF_POST_HEAT_FLUX, 
                                                    UF_SF_POST_THERMAL_ENERGY, 
                                                    UF_SF_POST_REACTION_HEAT_FLOW, 
                                                    UF_SF_POST_APPLIED_FORCE, 
                                                    UF_SF_POST_REACTION_FORCE, 
                                                    UF_SF_POST_ELEMENT_FORCE, 
                                                    UF_SF_POST_ELEMENT_PRESSURE, 
                                                    UF_SF_POST_FATIGUE_LIFE, 
                                                    UF_SF_POST_FATIGUE_DAMAGE, 
                                                    UF_SF_POST_FATIGUE_SAFETY, 
                                                    UF_SF_POST_STRENGTH_SAFETY, 
                                                    UF_SF_POST_ELEMENT_ERROR    */ 
   UF_SF_POST_result_type_lay_t    lay,      /*<I> Layer to be set for result
                                                   UF_SF_POST_AT_MID
                                                    (Result at mid section 
                                                     default, applicable for all kinds of elements)
                                                   UF_SF_POST_AT_TOP
                                                    (Result at top section
                                                     applicable only for shell elements)
                                                   UF_SF_POST_AT_BOT
                                                    (Result at bottom section
                                                     applicable only for shell elements)
                                                   UF_SF_POST_AT_MIN
                                                    (Minimum value
                                                     applicable only for shell elements)
                                                   UF_SF_POST_AT_MAX
                                                    (Maximum value
                                                     applicable only for shell elements)
                                                   UF_SF_POST_AT_SRP_C
                                                    (Stress Recovery Point at section-1
                                                     applicable only for truss elements)
                                                   UF_SF_POST_AT_SRP_D
                                                    (Stress Recovery Point at section-2
                                                     applicable only for truss elements)
                                                   UF_SF_POST_AT_SRP_E
                                                    (Stress Recovery Point at section-3
                                                     applicable only for truss elements)
                                                   UF_SF_POST_AT_SRP_F
                                                    (Stress Recovery Point at section-4
                                                     applicable only for truss elements)*/
   UF_SF_POST_result_comp_t        comp,    /*<I> Component to the result type to set
                                                    UF_SF_POST_COMP_SCALAR, 
                                                    UF_SF_POST_COMP_X, 
                                                    UF_SF_POST_COMP_Y, 
                                                    UF_SF_POST_COMP_Z, 
                                                    UF_SF_POST_COMP_MAG, 
                                                    UF_SF_POST_COMP_XX, 
                                                    UF_SF_POST_COMP_YY, 
                                                    UF_SF_POST_COMP_ZZ, 
                                                    UF_SF_POST_COMP_XY, 
                                                    UF_SF_POST_COMP_YZ, 
                                                    UF_SF_POST_COMP_ZX, 
                                                    UF_SF_POST_COMP_DETERMINANT, 
                                                    UF_SF_POST_COMP_MEAN, 
                                                    UF_SF_POST_COMP_MAX_SHEAR, 
                                                    UF_SF_POST_COMP_MIN_PRNCPL, 
                                                    UF_SF_POST_COMP_MID_PRNCPL, 
                                                    UF_SF_POST_COMP_MAX_PRNCPL, 
                                                    UF_SF_POST_COMP_OCTAHEDRAL 
                                                    UF_SF_POST_COMP_VON_MISES    */ 
   tag_t                          units_tag /*<I> To be obtained using function
                                                    UF_SF_get_unit_tag*/
);
/***************************************************************************
*  Get the currently set result param
*  Fill result_params structure with
*  current result settings. This function can be called anytime after post is initialized
*
* Environment:  Internal and External
*
* History: Originally released in NX4
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_get_result_params
(
    UF_SF_POST_result_parms_t_p result_params  /* <OF> Parameters for selecting results */
);

/*************************************************************************
*   gets the units_tag corresponding to the type of
*         results
*   Environment:  Internal and External
*
*  History: Originally released in NX3
**************************************************************************/
extern UFUNEXPORT tag_t UF_SF_POST_get_unit_tag
(
    UF_SF_POST_result_type_quan_t result_type, /*<I> Type of results results to be set 
                                                     UF_SF_POST_DISPLACEMENT
                                                     UF_SF_POST_ROTATION
                                                     UF_SF_POST_CONTACT_DISP
                                                     UF_SF_POST_VELOCITY
                                                     UF_SF_POST_ACCELERATION
                                                     UF_SF_POST_STRESS
                                                     UF_SF_POST_STRAIN
                                                     UF_SF_POST_STRAIN_E
                                                     UF_SF_POST_STRAIN_ED
                                                     UF_SF_POST_STRAIN_EE
                                                     UF_SF_POST_THICKNESS
                                                     UF_SF_POST_TEMPERATURE
                                                     UF_SF_POST_TEMP_GRAD
                                                     UF_SF_POST_HEAT_FLUX
                                                     UF_SF_POST_THERMAL_ENERGY
                                                     UF_SF_POST_REACTION_HEAT_FLOW
                                                     UF_SF_POST_APPLIED_FORCE
                                                     UF_SF_POST_REACTION_FORCE
                                                     UF_SF_POST_ELEMENT_FORCE
                                                     UF_SF_POST_ELEMENT_PRESSURE
                                                     UF_SF_POST_FATIGUE_LIFE
                                                     UF_SF_POST_FATIGUE_DAMAGE
                                                     UF_SF_POST_FATIGUE_SAFETY
                                                     UF_SF_POST_STRENGTH_SAFETY
                                                     UF_SF_POST_ELEMENT_ERROR
                                               */
const char *unit_type_selected                 /*<I> Units string. 
                                                     See uf_unit_types.h for valid units */
);


/***************************************************************************
*   feeds the data relating to fringe parameters into NX specific structures
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_set_fringe_params
( 
                   UF_SF_POST_fringe_t_p fringe_params  /* <I> Structure containing 
                                                               fringe parameter variables
                                                        */
);

/***************************************************************************
*  Initializes the structure containing fringe parameters
*  from the variables entered as input
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_fringe_params
(
UF_SF_POST_fringe_t_p* fringe_params,        /* <O> Structure containing fringe parameters */
UF_SF_POST_fringe_style_t style,             /* <I> Type of fringe style 
                                               UF_SF_POST_FRINGE_NONE,
                                               UF_SF_POST_FRINGE_CONTOUR_LINES,
                                               UF_SF_POST_FRINGE_ISOSURFACES,
                                               UF_SF_POST_FRINGE_CONTOUR_BANDS,
                                               UF_SF_POST_FRINGE_SMOOTH_TONE,
                                               UF_SF_POST_FRINGE_ELEM_VALUES */
UF_SF_POST_fringe_color_spec_t spec,          /* <I> Type of color spectrum 
                                                UF_SF_POST_FRINGE_COLOR_STRUCT,
                                                UF_SF_POST_FRINGE_COLOR_TEMP,
                                                UF_SF_POST_FRINGE_COLOR_GRAY */
UF_SF_POST_fringe_scale_spec_t fringe_scale,  /* <I> Type of scale spectrum 
                                                     UF_SF_POST_FRINGE_SCALE_AUTOMATIC,
                                                     UF_SF_POST_FRINGE_SCALE_LINEAR,
                                                     UF_SF_POST_FRINGE_SCALE_LOG */
logical whole_sw,                             /* <I> Whole model threshold switch */
double threshold_max,                         /* <I> Threshold value maximum limit */
double threshold_min,                         /* <I> Threshold value minimum limit */
int    colors_used,                           /* <I> No of colors used */
logical trans_sw,                             /* <I> Translucency switch */
UF_SF_POST_fringe_legend_opt_t legend,        /* <I> Type of legend option 
                                                UF_SF_POST_FRINGE_LEGEND_NONE,
                                                UF_SF_POST_FRINGE_LEGEND_COLOR,
                                                UF_SF_POST_FRINGE_LEGEND_DETAILED 
                                              */
logical thresh_sw                             /* <I> Threshold switch */
);

/***************************************************************************
*  exports the current display to a vrml file
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_export_vrml
(
    const char *file_name                           /* <I> VRML file name */
);

/***************************************************************************
*   exports the current display to a file
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_export_display_to_text
( 
    const char *file_name_with_extn,              /*<I> Name of file with relevant extension*/
    UF_SF_POST_file_type_t file_form              /*<I> Desired format of the file:
                                                           UF_SF_POST_FILE_ASCII
                                                           UF_SF_POST_FILE_VRML */
);

/***************************************************************************
*   feeds the data relating to deformed display parameters into NX specific structures
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_set_def_disp_params
(
 UF_SF_POST_def_disp_t_p def_disp       /*<I> Structure containing deformed display parameters
                                              obtained from UF_SF_POST_initialise_def_disp_params()
                                        */
);

/***************************************************************************
*   feeds the data relating to undeformed parameters into NX specific structures
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 ***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_set_undef_disp_params
(
 UF_SF_POST_undef_disp_t_p undef_disp   /*<I> Structure containing undeformed display parameters
                                              obtained from UF_SF_POST_initialise_undef_disp_params()
                                        */
 );

/****************************************************************************
*    Initialises the structure containing deformed display parameters
*    from the variables entered as input
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 ****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_def_disp_params
(
UF_SF_POST_def_disp_t_p *def_disp,              /*<OF>
                                                  Structure Containing deformed display
                                                  parameters
                                                */
UF_SF_POST_elem_edge_style_t edge_style,        /*<I>
                                                  Display type of element edges
                                                  UF_SF_POST_ELEM_EDGE_NONE,
                                                  UF_SF_POST_ELEM_EDGE_FREE,
                                                  UF_SF_POST_ELEM_EDGE_EXTERNAL,
                                                  UF_SF_POST_ELEM_EDGE_WIRE
                                                */
UF_SF_POST_hue_colors_t edge_color,             /*<I>
                                                  Color for displaying the element edges
                                                  UF_SF_POST_BLACK,
                                                  UF_SF_POST_MAGENTA_RED,
                                                  UF_SF_POST_MAGENTA,
                                                  UF_SF_POST_BLUE_MAGENTA,
                                                  UF_SF_POST_BLUE,
                                                  UF_SF_POST_CYAN_BLUE,
                                                  UF_SF_POST_CYAN,
                                                  UF_SF_POST_GREEN_CYAN,
                                                  UF_SF_POST_GREEN,
                                                  UF_SF_POST_YELLOW_GREEN,
                                                  UF_SF_POST_YELLOW,
                                                  UF_SF_POST_ORANGE,
                                                  UF_SF_POST_RED,
                                                  UF_SF_POST_DARK_GRAY,
                                                  UF_SF_POST_LIGHT_GRAY,
                                                  UF_SF_POST_WHITE
                                                */
UF_SF_POST_elem_face_style_t face_style,        /*<I>
                                                  Type of element face display
                                                  UF_SF_POST_ELEM_FACE_NONE,
                                                  UF_SF_POST_ELEM_FACE_FILLED,
                                                  UF_SF_POST_ELEM_FACE_FILLED_TRANS,
                                                  UF_SF_POST_ELEM_FACE_AUTO  
                                                */
UF_SF_POST_hue_colors_t face_color,             /*<I>
                                                  Color for the displaying the element faces
                                                  UF_SF_POST_BLACK,
                                                  UF_SF_POST_MAGENTA_RED,
                                                  UF_SF_POST_MAGENTA,
                                                  UF_SF_POST_BLUE_MAGENTA,
                                                  UF_SF_POST_BLUE,
                                                  UF_SF_POST_CYAN_BLUE,
                                                  UF_SF_POST_CYAN,
                                                  UF_SF_POST_GREEN_CYAN,
                                                  UF_SF_POST_GREEN,
                                                  UF_SF_POST_YELLOW_GREEN,
                                                  UF_SF_POST_YELLOW,
                                                  UF_SF_POST_ORANGE,
                                                  UF_SF_POST_RED,
                                                  UF_SF_POST_DARK_GRAY,
                                                  UF_SF_POST_LIGHT_GRAY,
                                                  UF_SF_POST_WHITE
                                                */
UF_SF_POST_display_marker_t display_marker,     /*<I>
                                                  Marker to display the minimum and/or
                                                  maximum values
                                                  UF_SF_POST_DISPLAY_MARKER_MIN_MAX,
                                                  UF_SF_POST_DISPLAY_MARKER_MAXIMUM,
                                                  UF_SF_POST_DISPLAY_MARKER_MINIMUM,
                                                  UF_SF_POST_DISPLAY_MARKER_NONE    
                                                */
logical def_sw,                                 /*<I>
                                                  Switch to decide whether to display the deformed
                                                  model or not
                                                */
logical undef_sw                                /*<I>
                                                  Switch to decide whether to display the undeformed
                                                  model or not
                                                */
);

/**************************************************************************
*  Initialise the structure containing deformation scaling parameters
*  from the variables entered as input
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_def_scale_params
(
UF_SF_POST_def_t_p *def_scale,                  /*<OF>
                                                  Structure Containing deformation scaling
                                                  parameters
                                                */
logical true_scale,                             /*<I>
                                                  Switch that sets the deformation of model 
                                                  to be displayed in true scale
                                                */
double true_multiplier,                         /*<I>
                                                  Multiplier value for true_Scale
                                                */
logical rel_scale,                              /*<I>
                                                  Switch that sets the deformation of model 
                                                  to be displayed in relative scale
                                                */
int rel_percentage                              /*<I>
                                                  Value of %, the deformation should be
                                                  relative to the undeformed model
                                                */
);

/*****************************************************************************
*  Initialise the structure containing deformation scaling parameters
*  from the variables entered as input
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 *****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_undef_disp_params
(
UF_SF_POST_undef_disp_t_p *undef_disp,          /*<OF>
                                                  Structure Containing undeformed display
                                                  parameters
                                                */
UF_SF_POST_elem_edge_style_t edge_style,        /*<I>
                                                  Display type of element edges
                                                  UF_SF_POST_ELEM_EDGE_NONE,
                                                  UF_SF_POST_ELEM_EDGE_FREE,
                                                  UF_SF_POST_ELEM_EDGE_EXTERNAL,
                                                  UF_SF_POST_ELEM_EDGE_WIRE
                                                */
UF_SF_POST_hue_colors_t edge_color,             /*<I>
                                                  Color for displaying the element edges
                                                  UF_SF_POST_BLACK,
                                                  UF_SF_POST_MAGENTA_RED,
                                                  UF_SF_POST_MAGENTA,
                                                  UF_SF_POST_BLUE_MAGENTA,
                                                  UF_SF_POST_BLUE,
                                                  UF_SF_POST_CYAN_BLUE,
                                                  UF_SF_POST_CYAN,
                                                  UF_SF_POST_GREEN_CYAN,
                                                  UF_SF_POST_GREEN,
                                                  UF_SF_POST_YELLOW_GREEN,
                                                  UF_SF_POST_YELLOW,
                                                  UF_SF_POST_ORANGE,
                                                  UF_SF_POST_RED,
                                                  UF_SF_POST_DARK_GRAY,
                                                  UF_SF_POST_LIGHT_GRAY,
                                                  UF_SF_POST_WHITE
                                                */
UF_SF_POST_elem_face_style_t face_style,        /*<I>
                                                  Type of element face display
                                                  UF_SF_POST_ELEM_FACE_NONE,
                                                  UF_SF_POST_ELEM_FACE_FILLED,
                                                  UF_SF_POST_ELEM_FACE_FILLED_TRANS,
                                                */
UF_SF_POST_hue_colors_t face_color              /*<I>
                                                  Color for the displaying the element faces
                                                  UF_SF_POST_BLACK,
                                                  UF_SF_POST_MAGENTA_RED,
                                                  UF_SF_POST_MAGENTA,
                                                  UF_SF_POST_BLUE_MAGENTA,
                                                  UF_SF_POST_BLUE,
                                                  UF_SF_POST_CYAN_BLUE,
                                                  UF_SF_POST_CYAN,
                                                  UF_SF_POST_GREEN_CYAN,
                                                  UF_SF_POST_GREEN,
                                                  UF_SF_POST_YELLOW_GREEN,
                                                  UF_SF_POST_YELLOW,
                                                  UF_SF_POST_ORANGE,
                                                  UF_SF_POST_RED,
                                                  UF_SF_POST_DARK_GRAY,
                                                  UF_SF_POST_LIGHT_GRAY,
                                                  UF_SF_POST_WHITE
                                                */
);

/**************************************************************************
*  sets the "clip" structure with the obtained data from the user  
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
***************************************************************************/
extern UFUNEXPORT int UF_SF_POST_set_clipping
(
UF_SF_post_clipping_data_t_p clip_params             /* <I> Structure containing clip 
                                                            parameters
                                                     */
);

/***************************************************************************
*  initialises the sturcture for clip parameters with user given values  
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
*****************************************************************************/
extern  UFUNEXPORT int UF_SF_POST_initialise_clip_params
(
UF_SF_post_clipping_data_t_p *clip_params,             /* <OF> Structure containing clip
                                                             parameters to be initialized
                                                       */
int                           clip_tgl_data,           /* <I> Clip toggle 
                                                              default value = 1
                                                       */
int                           ghost_tgl_data,          /* <I> Ghost model toggle 
                                                              value = 0 or 1 
                                                       */
int                           outline_tgl_data,        /* <I> Outline model toggle
                                                              value = 0 or 1
                                                       */
int                           auto_update_tgl_data,    /* <I> Auto update toggle
                                                              default value = 1
                                                       */
int                           plane_type_data,         /* <I> Type of clip plane 
                                                              UF_SF_CLIP_ABS_XY
                                                              UF_SF_CLIP_ABS_YZ
                                                              UF_SF_CLIP_ABS_ZX
                                                              UF_SF_CLIP_WCS_XY
                                                              UF_SF_CLIP_WCS_YZ
                                                              UF_SF_CLIP_WCS_ZX
                                                              UF_SF_CLIP_WCS_CYL_RT
                                                              UF_SF_CLIP_WCS_CYL_TZ
                                                              UF_SF_CLIP_WCS_SPH_TP
                                                       */
int                           clip_side_data,          /* <I> Clip side data
                                                              UF_SF_CLIP_POSITIVE
                                                              UF_SF_CLIP_NEGATIVE
                                                              UF_SF_CLIP_BOTH
                                                        */
double                        clip_value_data,          /* <I> Distance along the axis */
int                           clip_scale_data,          /* <I> Clip scale toggle 
                                                               Default value = 1
                                                        */
double                        clip_scale_curr_min,      /* <I> Scaling minimum
                                                               default value = 0.0
                                                        */
double                        clip_scale_curr_max,      /* <I> Scaling maximum
                                                               default value = 0.0
                                                        */
double                        scale_min,                /* default value = 0 */
double                        scale_max                 /* default value = 0 */
);

/**************************************************************************
*  Initializes the structure ident_params from the variables entered as input
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_SF_POST_initialise_ident_params
(
UF_SF_POST_ident_parms_t_p* ident_params,    /* <OF> Structure containing Identify parameters to
                                                    be initialized*/
UF_SF_POST_ident_action_t   action,          /* <I> Entities for action to be performed
                                                    UF_SF_POST_IDENT_N_HIGH_NODES
                                                    UF_SF_POST_IDENT_N_LOW_NODES
                                                    UF_SF_POST_IDENT_NODE_IDS
                                                    UF_SF_POST_IDENT_NODE_BY_ELEM_IDS
                                                    UF_SF_POST_IDENT_N_HIGH_ELEMS
                                                    UF_SF_POST_IDENT_N_LOW_ELEMS
                                                    UF_SF_POST_IDENT_ELEM_IDS
                                              */
int                         number,           /* <I> Node or Element ID whose value needs 
                                                     to be printed in the file
                                              */
char*                       data_string,      /* <I> String containing data about 
                                                     elements or nodes
                                                     ex: "1-25" or "1,3,5" etc
                                              */
logical                     list_comp_sw      /* <I> Lists all components when the value is TRUE */
); 

/***********************************************************************
*   Set up the ident parameters in the Ident structure 
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
************************************************************************/
extern UFUNEXPORT int UF_SF_POST_write_ident_data
(
UF_SF_POST_ident_parms_t_p ident_params,    /*<I> Structure containing Identify parameters */
char*                      data_file        /*<I> File name to write Identify data */
);

/***********************************************************************
*    creates a combined load case from the input load components and scales.
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
*************************************************************************/
extern  UFUNEXPORT int UF_SF_POST_create_combined_lcase
(
char    *clc_name,                /* <I> Name of the combined load case */
int      num_lcases,              /* <I> Number of Load Case Components */
int     *lcase_list,              /* <I> List of Load Case Component Numbers */
double  *lcase_scales,            /* <I> List of Load Case Scale factors */
int     *new_clc_num              /* <O> New Combined Load Case Number */
);

/***************************************************************************  
* deletes a combined load case with the specified name.
*
* Environment: Internal  and  External
*
* History: Originally released in NX3.0
****************************************************************************/  
extern  UFUNEXPORT int UF_SF_POST_delete_combined_lcase
(
char   *clc_name                   /* <I>  Name of the combined load case */
);

/******************************************************************************
*   Initialises the the structure for deformed result parameters
*  from the variables entered as input
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
******************************************************************************/ 
extern UFUNEXPORT int UF_SF_POST_initialise_deformed_result_params
(
 UF_SF_post_deform_result_t_p   def_result_params,  /*<O> Deformed Result Parameter sturcture to be filled */ 
 int                            loadcase,           /*<I> Loadcase selected */
 int                            iteration,          /*<I> Iteration Selected */
 UF_SF_POST_result_type_quan_t  quan,               /*<I> 
                                                          Result Type Parameter
                                                            UF_SF_POST_DISPLACEMENT
                                                            UF_SF_POST_ROTATION
                                                            UF_SF_POST_CONTACT_DISP
                                                            UF_SF_POST_VELOCITY
                                                            UF_SF_POST_ACCELERATION
                                                            UF_SF_POST_STRESS
                                                            UF_SF_POST_STRAIN
                                                            UF_SF_POST_STRAIN_E
                                                            UF_SF_POST_STRAIN_ED
                                                            UF_SF_POST_STRAIN_EE
                                                            UF_SF_POST_THICKNESS
                                                            UF_SF_POST_TEMPERATURE
                                                            UF_SF_POST_TEMP_GRAD
                                                            UF_SF_POST_HEAT_FLUX
                                                            UF_SF_POST_THERMAL_ENERGY
                                                            UF_SF_POST_REACTION_HEAT_FLOW
                                                            UF_SF_POST_APPLIED_FORCE
                                                            UF_SF_POST_REACTION_FORCE
                                                            UF_SF_POST_ELEMENT_FORCE
                                                            UF_SF_POST_ELEMENT_PRESSURE
                                                            UF_SF_POST_FATIGUE_LIFE
                                                            UF_SF_POST_FATIGUE_DAMAGE
                                                            UF_SF_POST_FATIGUE_SAFETY
                                                            UF_SF_POST_STRENGTH_SAFETY
                                                            UF_SF_POST_ELEMENT_ERROR
                                                        */
 UF_SF_POST_result_type_lay_t   lay,                    /* <I> Result Type Parameter for Layer
                                                               UF_SF_POST_AT_MID
                                                               UF_SF_POST_AT_TOP
                                                               UF_SF_POST_AT_BOT
                                                               UF_SF_POST_AT_MIN
                                                               UF_SF_POST_AT_MAX
                                                               UF_SF_POST_AT_SRP_C
                                                               UF_SF_POST_AT_SRP_D
                                                               UF_SF_POST_AT_SRP_E
                                                               UF_SF_POST_AT_SRP_F
                                                         */
 double                         scale,                   /* <I> Deformation scaling value */
 int                            def_value_choice,        /* <I> Deformation value choice */
 int                            undef_choice             /* <I> Undefrmation choice */
 );


/*************************************************************************
* updates the corresponding data related to deformed  and undeformed options 
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_select_deformed_results
(
UF_SF_post_deform_result_t_p  def_result_params    /*<I> Deformed Result Parameter sturcture */
);

extern UFUNEXPORT tag_t UF_SF_POST_get_component_unit_tag(
    UF_SF_POST_result_comp_t comp_type,/*<I> Type of results results to be set <I>*/
    const char *unit_type_selected /*<I> Units string. 
                                         See uf_unit_types.h for valid units */);

/*************************************************************************
* overlays a specific post view
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_overlay
(
const char* post_view_name,    /*<I> Deformed Result Parameter sturcture */
logical set_work,/*<I>*/
logical apply_on_work /*<I>*/
);

/*************************************************************************
* remves a specific post view from overlay
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_remove_overlay
(
const char* post_view_name    /*<I> Deformed Result Parameter sturcture */
);

/*************************************************************************
* exit overlay mode
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_POST_exit_overlay
(
);

/*************************************************************************
* post mark setting
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_post_mark_setting( UF_SF_POST_mark_arrow_style_t arrowtype,/*<I>
                                                                                           UF_SF_POST_MARK_ARROW_STYLE_LINE,
                                                                                           UF_SF_POST_MARK_ARROW_STYLE_UMBRELLA,
                                                                                           UF_SF_POST_MARK_ARROW_STYLE_CYLINDER*/
                                               int markcomps,
                                               UF_SF_POST_mark_tensor_style_t tensortype,/*<I>    
                                                                                        UF_SF_POST_MARK_TENSOR_STYLE_ARROWS,
                                                                                        UF_SF_POST_MARK_TENSOR_STYLE_CROWSFEET,
                                                                                        UF_SF_POST_MARK_TENSOR_STYLE_BOX*/ 
                                               UF_SF_POST_mark_color_type_t markcolortype,/*<I>
                                                                                            UF_SF_POST_MARK_COLOR_RESULT,
                                                                                            UF_SF_POST_MARK_COLOR_ANNOTEXT,
                                                                                            UF_SF_POST_MARK_COLOR_SELECTED*/ 
                                               int markcolor,
                                               UF_SF_POST_mark_size_type_t marksizetype, /*<I>    
                                                                                         UF_SF_POST_MARK_SIZE_RESULT,
                                                                                        UF_SF_POST_MARK_SIZE_CONSTANT*/ 
                                               UF_SF_POST_mark_size_valtype_t marksizevaluetype, /*<I>
                                                                                                UF_SF_POST_MARK_SIZE_MODELPERCENT,
                                                                                                UF_SF_POST_MARK_SIZE_VALUE*/
                                               double marksizevalue, 
                                               UF_SF_POST_mark_loc_type_t arrowloc,  /*<I>
                                                                                        UF_SF_POST_MARK_AT_NODES,
                                                                                        UF_SF_POST_MARK_AT_ELEMCENTROID*/
                                               int hidemark, 
                                               UF_SF_POST_mark_hide_valtype_t hidetype, /*<I>
                                                                                            UF_SF_POST_MARK_HIDE_RESULTPERCENT,
                                                                                            UF_SF_POST_MARK_HIDE_VALUE*/
                                               double hidevalue, 
                                               UF_SF_POST_elem_value_t elementcriterion /*<I>
                                                                                        UF_SF_POST_ELEM_VALUE_CENTD,
                                                                                        UF_SF_POST_ELEM_VALUE_AVE,
                                                                                        UF_SF_POST_ELEM_VALUE_MIN,
                                                                                        UF_SF_POST_ELEM_VALUE_MAX*/);


/*************************************************************************
* post mark setting
*
*   Environment: Internal or External
*
*   See Also:
*
*   History: Released in NX3
*****************************************************************************/
extern UFUNEXPORT int UF_SF_marker_display(UF_SF_POST_display_marker_t marker /*<I>
                                                                              Marker to display the minimum and/or
                                                                              maximum values
                                                                              UF_SF_POST_DISPLAY_MARKER_MIN_MAX,
                                                                              UF_SF_POST_DISPLAY_MARKER_MAXIMUM,
                                                                              UF_SF_POST_DISPLAY_MARKER_MINIMUM,
                                                                              UF_SF_POST_DISPLAY_MARKER_NONE    
                                                                            */);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY
  
#endif  /*  UF_SF_POST_EXTERNAL__H_INCLUDED */
