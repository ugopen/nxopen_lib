/*****************************************************************************
 *
 *            Copyright (c) 2002 Unigraphics Solutions Corporation
 *                       Unpublished - All rights reserved
 *
 * 
 *
 *File description:
 *
 *   Datatypes for the UF_SF (Scenario User Function ) Post Processor module.
 *******************************************************************************/
 
#ifndef UF_SF_POST_DATATYPES_H_INCLUDED
#define UF_SF_POST_DATATYPES_H_INCLUDED

#include <uf_defs.h>
#include <uf_cfi.h>

/* The following must be the last include file */
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


/******************************************************************/

/* Constants for Post Processor */

/*
 * UF_SF_POST_NO_RESULT_NUM -This is prompted when there is no result
                             number

 * UF_SF_POST_DESC_SZ -      Maximum size of description

 * UF_SF_POST_FILE_NM_SZ     Maximum size of file name

 * UF_SF_POST_LIBRARY_NM_SZ  Maximum size of library name

 * UF_SF_POST_STATE_NM_SZ    Maximum size of state name
*/

#define UF_SF_POST_NO_RESULT_NUM            -777
#define UF_SF_POST_DESC_SZ                  64
#define UF_SF_POST_FILE_NM_SZ               1024
#define UF_SF_POST_LIBRARY_NM_SZ            9
#define UF_SF_POST_STATE_NM_SZ              16
#define UF_SF_POST_DSN_NM_SZ                64
#define UF_SF_POST_MAX_STRING_LEN           256


/******************************************************************/

/*****type def's for POST PROCESSOR********/

typedef enum
{
    UF_SF_POST_OUTPUT2 = 0,      /*Nastran output file*/
    UF_SF_POST_ANSYS = 2,        /*Ansys output file*/
    UF_SF_POST_FOCUS = 4,        /*FOCUS Database file*/
    UF_SF_POST_ABAQUS = 5,       /*Abaqus results file*/
    UF_SF_POST_MODEL_SOL = 6,     /*Model Solution results file*/
    UF_SF_POST_OUTPUT2_FATIGUE = 7, /* Nastran fatigue file */
    UF_SF_POST_ANSYS_FATIGUE = 8,   /* Ansys fatigue file */
    UF_SF_POST_ABAQUS_FATIGUE = 9,  /* Abaqus fatigue file */
    UF_SF_POST_FOCUS_FATIGUE = 10  /* Focus fatigue file */
}
UF_SF_POST_result_file_type_t;
typedef UF_SF_POST_result_file_type_t *UF_SF_POST_result_file_type_p_t ;


/********************************************************/
/**********************Result parameters************/
/*
 * UF_SF_POST_DISPLACEMENT      Displacement values in the result

 * UF_SF_POST_ROTATION          Rotational values

 * UF_SF_POST_CONTACT_DISP      Displacement for contact elements

 * UF_SF_POST_VELOCITY          Velocity for centrifugal loads

 * UF_SF_POST_ACCELERATION      Acceleration for centrifugal loads

 * UF_SF_POST_STRESS            Stress values

 * UF_SF_POST_STRAIN            Strain values

 * UF_SF_POST_STRAIN_E          Strain Energy values

 * UF_SF_POST_STRAIN_ED         Strain Energy density

 * UF_SF_POST_STRAIN_EE         Strain Energy Error

 * UF_SF_POST_THICKNESS         Thickness value

 * UF_SF_POST_TEMPERATURE       Temperature value

 * UF_SF_POST_TEMP_GRAD         Temperature Gradient value

 * UF_SF_POST_HEAT_FLUX         Heat flux value

 * UF_SF_POST_THERMAL_ENERGY    Thermal energy value

 * UF_SF_POST_REACTION_HEAT_FLOW Reaction heat flow value

 * UF_SF_POST_APPLIED_FORCE     Applied load

 * UF_SF_POST_REACTION_FORCE    Reaction force

 * UF_SF_POST_ELEMENT_FORCE     Element force

 * UF_SF_POST_ELEMENT_PRESSURE  Element Pressure (Contact Elements)

 * UF_SF_POST_FATIGUE_LIFE      Fatigue life

 * UF_SF_POST_FATIGUE_DAMAGE    Fatigue damage

 * UF_SF_POST_FATIGUE_SAFETY    Fatigue safety factor

 * UF_SF_POST_STRENGTH_SAFETY   Strength safety factor

 * UF_SF_POST_ELEMENT_ERROR     Element Error
*/


typedef enum UF_SF_POST_result_type_quan_e
{
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
    UF_SF_POST_STRAIN_PLAST_EQ,
    UF_SF_POST_STRAIN_CREEP_EQ,
    UF_SF_POST_THICKNESS,
    UF_SF_POST_TEMPERATURE,
    UF_SF_POST_TEMP_GRAD,
    UF_SF_POST_HEAT_FLUX,
    UF_SF_POST_THERMAL_ENERGY,
    UF_SF_POST_REACTION_HEAT_FLOW,
    UF_SF_POST_APPLIED_FORCE,
    UF_SF_POST_APPLIED_MOMENT,
    UF_SF_POST_REACTION_FORCE,
    UF_SF_POST_REACTION_MOMENT ,
    UF_SF_POST_CONTACT_TRACTION ,
    UF_SF_POST_CONTACT_FORCE ,
    UF_SF_POST_ELEMENT_FORCE,
    UF_SF_POST_ELEMENT_PRESSURE,
    UF_SF_POST_FATIGUE_LIFE,
    UF_SF_POST_FATIGUE_DAMAGE,
    UF_SF_POST_FATIGUE_SAFETY,
    UF_SF_POST_STRENGTH_SAFETY,
    UF_SF_POST_ELEMENT_ERROR,
    UF_SF_POST_ELEMENTRESULT, 
    UF_SF_POST_MAX_TEMPERATURE_TRANSIENT, 
    UF_SF_POST_MIN_TEMPERATURE_TRANSIENT, 
    UF_SF_POST_TIME_OF_MAX_TEMPERATURE_TRANSIENT, 
    UF_SF_POST_TIME_OF_MIN_TEMPERATURE_TRANSIENT,
    UF_SF_POST_CONDUCTIVE_FLUX, 
    UF_SF_POST_TOTAL_HEAT_LOAD, 
    UF_SF_POST_TOTAL_HEAT_FLUX, 
    UF_SF_POST_HEAT_RESIDUAL,
    UF_SF_POST_FILM_COEF, 
    UF_SF_POST_VIEW_FACTORS_SUM,
    UF_SF_POST_VELOCITIES_ADJUSTED, 
    UF_SF_POST_PRESSURE_POSITIVE_SIDE,
    UF_SF_POST_PRESSURE_NEGATIVE_SIDE, 
    UF_SF_POST_STATIC_PRESSURE, 
    UF_SF_POST_TOTAL_PRESSURE, 
    UF_SF_POST_TURBULENCE_ENERGY, 
    UF_SF_POST_TURBULENCE_DISSIPATION, 
    UF_SF_POST_FLUID_DENSITIES,
    UF_SF_POST_SHEAR_STRESS_POSITIVE_SIDE, 
    UF_SF_POST_SHEAR_STRESS_NEGATIVE_SIDE, 
    UF_SF_POST_ROUGHNESS_POSITIVE_SIDE, 
    UF_SF_POST_ROUGHNESS_NEGATIVE_SIDE,
    UF_SF_POST_YPLUS_POSITIVE_SIDE, 
    UF_SF_POST_YPLUS_NEGATIVE_SIDE, 
    UF_SF_POST_MASS_FLUX,
    UF_SF_POST_FLUID_TEMPERATURES,
    UF_SF_POST_HEAT_FLUX_CONVECTIVE, 
    UF_SF_POST_CONVECTION_COEF_LOCAL, 
    UF_SF_POST_CONVECTION_COEF_BULK,
    UF_SF_POST_PRESSURE,
    UF_SF_POST_VELOCITY_COMPONENT,
    UF_SF_POST_MASS_FLOW,
    UF_SF_POST_ELEM_HEAT_LOAD

}
UF_SF_POST_result_type_quan_t;

/*************************************************************/
/************* Results at layers*******************/
/*
 * UF_SF_POST_AT_MID        Result at mid section

 * UF_SF_POST_AT_TOP        Result at top section

 * UF_SF_POST_AT_BOT        Result at bottom section

 * UF_SF_POST_AT_MIN        Minimum value

 * UF_SF_POST_AT_MAX        Maximum value

 * UF_SF_POST_AT_SRP_C      Stress Recovery Point at section-1

 * UF_SF_POST_AT_SRP_D      Stress Recovery Point at section-2

 * UF_SF_POST_AT_SRP_E      Stress Recovery Point at section-3

 * UF_SF_POST_AT_SRP_F      Stress Recovery Point at section-4
*/


typedef enum UF_SF_POST_result_type_lay_e
{
    UF_SF_POST_AT_MID,
    UF_SF_POST_AT_TOP,
    UF_SF_POST_AT_BOT,
    UF_SF_POST_AT_MIN,
    UF_SF_POST_AT_MAX,
    UF_SF_POST_AT_SRP_C,
    UF_SF_POST_AT_SRP_D,
    UF_SF_POST_AT_SRP_E,
    UF_SF_POST_AT_SRP_F
}
UF_SF_POST_result_type_lay_t;


/****************************************************************/
/************Results at locations**************/
/*
 * UF_SF_POST_AT_NODES                Nodal results

 * UF_SF_POST_AT_ELEMS                Element results

 * UF_SF_POST_AT_ELNDS                Element Nodal results

*/


typedef enum UF_SF_POST_result_type_loc_e
{
    UF_SF_POST_AT_NODES,
    UF_SF_POST_AT_ELEMS,
    UF_SF_POST_AT_ELNDS
}
UF_SF_POST_result_type_loc_t;


struct UF_SF_POST_result_type_s
{
    UF_SF_POST_result_type_quan_t quan;
    UF_SF_POST_result_type_lay_t  lay;
    UF_SF_POST_result_type_loc_t  loc;
};
typedef struct UF_SF_POST_result_type_s UF_SF_POST_result_type_t;
typedef struct UF_SF_POST_result_type_s *UF_SF_POST_result_type_p_t;


/*********************************************************/
/************Stress Components**********************/
/*
 * UF_SF_POST_COMP_SCALAR         Scalar value of the result

 * UF_SF_POST_COMP_X              X-component result

 * UF_SF_POST_COMP_Y              Y-component result

 * UF_SF_POST_COMP_Z              Z-component result

 * UF_SF_POST_COMP_MAG            Magnitude

 * UF_SF_POST_COMP_XX             XX-component

 * UF_SF_POST_COMP_YY             yy-component

 * UF_SF_POST_COMP_ZZ             zz-component

 * UF_SF_POST_COMP_XY             XY-component

 * UF_SF_POST_COMP_YZ             YZ-component

 * UF_SF_POST_COMP_ZX             ZX-component

 * UF_SF_POST_COMP_DETERMINANT    Determinant values

 * UF_SF_POST_COMP_MEAN           Mean stress values

 * UF_SF_POST_COMP_MAX_SHEAR      Maximum shear values

 * UF_SF_POST_COMP_MIN_PRNCPL     Minimum Principal stress

 * UF_SF_POST_COMP_MID_PRNCPL     Mid Principal stress

 * UF_SF_POST_COMP_MAX_PRNCPL     Maximum Principal stress

 * UF_SF_POST_COMP_OCTAHEDRAL     Octahedral values

 * UF_SF_POST_COMP_VON_MISES      Von-mises stresses
*/


typedef enum UF_SF_POST_result_comp_e
{
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
    UF_SF_POST_COMP_OCTAHEDRAL,
    UF_SF_POST_COMP_VON_MISES,
    UF_SF_POST_COMP_MEMBRANE_XX,
    UF_SF_POST_COMP_MEMBRANE_YY,
    UF_SF_POST_COMP_MEMBRANE_XY,
    UF_SF_POST_COMP_BENDING_XX,
    UF_SF_POST_COMP_BENDING_YY,
    UF_SF_POST_COMP_BENDING_XY,
    UF_SF_POST_COMP_SHEAR_YZ,
    UF_SF_POST_COMP_SHEAR_XZ,
    UF_SF_POST_COMP_AXIAL,
    UF_SF_POST_COMP_BENDING_S,
    UF_SF_POST_COMP_BENDING_T,
    UF_SF_POST_COMP_TORSION,
    UF_SF_POST_COMP_SHEAR_S,
    UF_SF_POST_COMP_SHEAR_T
}
UF_SF_POST_result_comp_t;
typedef UF_SF_POST_result_comp_t *UF_SF_POST_result_comp_p_t;

typedef enum
{
    UF_SF_POST_NODE,
    UF_SF_POST_ELEM
}
UF_SF_POST_object_type_t;
typedef UF_SF_POST_object_type_t *UF_SF_POST_object_type_p_t;

typedef enum UF_SF_POST_id_type_e
{
    UF_SF_POST_USERID,
    UF_SF_POST_VKIID
}
UF_SF_POST_id_type_t;
typedef UF_SF_POST_id_type_t *UF_SF_POST_id_type_p_t;

typedef enum UF_SF_POST_minmax_e
{
    UF_SF_POST_MINIMUM,
    UF_SF_POST_MAXIMUM
}
UF_SF_POST_minmax_t;
typedef UF_SF_POST_minmax_t *UF_SF_POST_minmax_p_t;




/*********************************************************************/
/*************Co-ordinate systems*********/
/*
 * UF_SF_POST_ABS_RECTANGULAR       Absolute rectangular co-ord system

 * UF_SF_POST_ABS_CYLINDRICAL       Cylindrical co-ordinate system

 * UF_SF_POST_ABS_SPHERICAL         Absolute Spherical co-ord system

 * UF_SF_POST_WRK_RECTANGULAR       WCS rectangular co-ord system

 * UF_SF_POST_WRK_CYLINDRICAL       WCS  Cylindrical co-ord system

 * UF_SF_POST_WRK_SPHERICAL         WCS Spherical co-ord system

 * UF_SF_POST_LOCAL                 Local co-ordinate system
*/


typedef enum UF_SF_POST_coord_sys_type_e
{
    UF_SF_POST_ABS_RECTANGULAR,
    UF_SF_POST_ABS_CYLINDRICAL,
    UF_SF_POST_ABS_SPHERICAL,
    UF_SF_POST_WRK_RECTANGULAR,
    UF_SF_POST_WRK_CYLINDRICAL,
    UF_SF_POST_WRK_SPHERICAL,
    UF_SF_POST_LOCAL
}
UF_SF_POST_coord_sys_type_t;
typedef UF_SF_POST_coord_sys_type_t *UF_SF_POST_coord_sys_type_p_t;

/*********************************************************************/
/*************Fringe Style Components*********/
/*
 * UF_SF_POST_FRINGE_NONE               No Style

 * UF_SF_POST_FRINGE_CONTOUR_LINES       Contour lines display format

 * UF_SF_POST_FRINGE_ISOSURFACES         Isosurface display format

 * UF_SF_POST_FRINGE_CONTOUR_BANDS       Contour band display format

 * UF_SF_POST_FRINGE_SMOOTH_TONE         Smooth tone display format

 * UF_SF_POST_FRINGE_ELEM_VALUES         Element value display format

 */
typedef enum UF_SF_POST_fringe_style_e
{
    UF_SF_POST_FRINGE_NONE,
    UF_SF_POST_FRINGE_CONTOUR_LINES,
    UF_SF_POST_FRINGE_ISOSURFACES,
    UF_SF_POST_FRINGE_CONTOUR_BANDS, 
    UF_SF_POST_FRINGE_SMOOTH_TONE,
    UF_SF_POST_FRINGE_ELEM_VALUES,
    UF_SF_POST_FRINGE_ARROW, 
    UF_SF_POST_FRINGE_CUBE, 
    UF_SF_POST_FRINGE_SPHERE,
    UF_SF_POST_FRINGE_TENSOR
}
UF_SF_POST_fringe_style_t;
typedef UF_SF_POST_fringe_style_t *UF_SF_POST_fringe_style_t_p;


/*********************************************************************/
/*************Fringe Color Spectrum Components*********/
/*
 * UF_SF_POST_FRINGE_COLOR_STRUCT      Structural scale color display

 * UF_SF_POST_FRINGE_COLOR_TEMP        Temperature scale color display

 * UF_SF_POST_FRINGE_COLOR_GRAY        Grey scale color display

 */
typedef enum UF_SF_POST_fringe_color_spec_e
{
    UF_SF_POST_FRINGE_COLOR_STRUCT,
    UF_SF_POST_FRINGE_COLOR_TEMP,
    UF_SF_POST_FRINGE_COLOR_GRAY
}
UF_SF_POST_fringe_color_spec_t;
typedef UF_SF_POST_fringe_color_spec_t *UF_SF_POST_fringe_color_spec_t_p;


/*********************************************************************/
/*************Fringe Scale Spectrum Components*********/
/*
 * UF_SF_POST_FRINGE_SCALE_AUTOMATIC      Automatic query for linear scale or log scale

 * UF_SF_POST_FRINGE_SCALE_LINEAR         Linear scale spectrum

 * UF_SF_POST_FRINGE_SCALE_LOG            Log scale spectrum

 */
typedef enum UF_SF_POST_fringe_scale_spec_e
{
    UF_SF_POST_FRINGE_SCALE_AUTOMATIC,
    UF_SF_POST_FRINGE_SCALE_LINEAR,
    UF_SF_POST_FRINGE_SCALE_LOG
}
UF_SF_POST_fringe_scale_spec_t;
typedef UF_SF_POST_fringe_scale_spec_t *UF_SF_POST_fringe_scale_spec_t_p;


/*********************************************************************/
/*************Fringe Legend Components*********/
/*
 * UF_SF_POST_FRINGE_LEGEND_NONE         No Legend color bar

 * UF_SF_POST_FRINGE_LEGEND_COLOR        Legend color bar with color index only

 * UF_SF_POST_FRINGE_LEGEND_DETAILED     Legend color bar with color index and detailed specification

 */
typedef enum UF_SF_POST_fringe_legend_opt_e
{
    UF_SF_POST_FRINGE_LEGEND_NONE,
    UF_SF_POST_FRINGE_LEGEND_COLOR,
    UF_SF_POST_FRINGE_LEGEND_DETAILED
}
UF_SF_POST_fringe_legend_opt_t;
typedef UF_SF_POST_fringe_legend_opt_t *UF_SF_POST_fringe_legend_opt_t_p;

typedef enum
{
    UF_SF_POST_RES_TYPE_SCALAR = 0,
    UF_SF_POST_RES_TYPE_VECTOR,
    UF_SF_POST_RES_TYPE_TENSOR,
    UF_SF_POST_TYPE_SIX_DOF_VECTOR,
    UF_SF_POST_TYPE_ELEMENTRESULT,
    UF_SF_POST_TYPE_GENERALTENSOR
} UF_SF_POST_res_type_dimension_t;
typedef UF_SF_POST_res_type_dimension_t *UF_SF_POST_res_type_dimension_t_p;

/*********************************************************************/
/*************Element Edge Display Styles*********/
/*
 * UF_SF_POST_ELEM_EDGE_NONE       No element edges are displayed

 * UF_SF_POST_ELEM_EDGE_FREE       Only free element edges are displayed

 * UF_SF_POST_ELEM_EDGE_EXTERNAL   All external element edges are displayed

 * UF_SF_POST_ELEM_EDGE_WIRE       Element edges are displayed as wireframe
*/

typedef enum UF_SF_POST_elem_edge_style_e
{
    UF_SF_POST_ELEM_EDGE_NONE,
    UF_SF_POST_ELEM_EDGE_FREE,
    UF_SF_POST_ELEM_EDGE_EXTERNAL,
    UF_SF_POST_ELEM_EDGE_WIRE
}
UF_SF_POST_elem_edge_style_t;
typedef UF_SF_POST_elem_edge_style_t *UF_SF_POST_elem_edge_style_t_p;

/*********************************************************************/
/*************Element Face Display Styles*********/
/*
 * UF_SF_POST_ELEM_FACE_NONE          Element faces are not displayed

 * UF_SF_POST_ELEM_FACE_FILLED        Faces displayed in a fill color

 * UF_SF_POST_ELEM_FACE_FILLED_TRANS  Translucency applied over fill color

 * UF_SF_POST_ELEM_FACE_AUTO          Automatic style selection enabled
*/
typedef enum UF_SF_POST_elem_face_style_e
{
    UF_SF_POST_ELEM_FACE_NONE,
    UF_SF_POST_ELEM_FACE_FILLED,
    UF_SF_POST_ELEM_FACE_FILLED_TRANS,
    UF_SF_POST_ELEM_FACE_AUTO
}
UF_SF_POST_elem_face_style_t;
typedef UF_SF_POST_elem_face_style_t *UF_SF_POST_elem_face_style_t_p;

/*********************************************************************/
/*************Element Display Styles*********/
/* NOTE : This choice does NOT seem to be exposed via UI at present */
/*
 * UF_SF_POST_ELEM_DISP_ALL             All elements are displayed

 * UF_SF_POST_ELEM_DISP_FOLLOW_SCENARIO Use Scenario settings

 * UF_SF_POST_ELEM_DISP_1D              Display 1D elements only

 * UF_SF_POST_ELEM_DISP_2D              Display 2D elements only

 * UF_SF_POST_ELEM_DISP_3D              Display 3D elements only
*/
typedef enum UF_SF_POST_elem_display_e
{
    UF_SF_POST_ELEM_DISP_ALL= 0,
    UF_SF_POST_ELEM_DISP_FOLLOW_SCENARIO,
    UF_SF_POST_ELEM_DISP_1D,
    UF_SF_POST_ELEM_DISP_2D,
    UF_SF_POST_ELEM_DISP_3D
}
UF_SF_POST_elem_display_t;
typedef UF_SF_POST_elem_display_t *UF_SF_POST_elem_display_t_p;

/*********************************************************************/
/*************Display Marker Styles*********/
/*
 * UF_SF_POST_DISPLAY_MARKER_MIN_MAX    Display both Max and Min markers

 * UF_SF_POST_DISPLAY_MARKER_MAXIMUM    Display only the Max marker

 * UF_SF_POST_DISPLAY_MARKER_MINIMUM    Display only the Min marker

 * UF_SF_POST_DISPLAY_MARKER_NONE       Do not display any markers
*/
typedef enum UF_SF_POST_display_marker_e
{
    UF_SF_POST_DISPLAY_MARKER_MIN_MAX = 0,
    UF_SF_POST_DISPLAY_MARKER_MAXIMUM,
    UF_SF_POST_DISPLAY_MARKER_MINIMUM,
    UF_SF_POST_DISPLAY_MARKER_NONE
}
UF_SF_POST_display_marker_t;
typedef UF_SF_POST_display_marker_t *UF_SF_POST_display_marker_t_p;

/*********************************************************************/
/*************Choice of colors for element edge/face display*********/
typedef enum UF_SF_POST_hue_colors_e
{
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
}
UF_SF_POST_hue_colors_t;
typedef UF_SF_POST_hue_colors_t *UF_SF_POST_hue_colors_t_p;

typedef enum UF_SF_POST_elem_value_e
{
    UF_SF_POST_ELEM_VALUE_CENT = 0,
    UF_SF_POST_ELEM_VALUE_AVE,
    UF_SF_POST_ELEM_VALUE_MIN,
    UF_SF_POST_ELEM_VALUE_MAX
}
UF_SF_POST_elem_value_t;
typedef UF_SF_POST_elem_value_t *UF_SF_POST_elem_value_t_p;

/*****************************************************************************
  Structure defining the parameters of a results request.
******************************************************************************/

struct UF_SF_POST_mark_vec_comp_s
{
    int x_sw;
    int y_sw;
    int z_sw;
    int mag_sw;
};
typedef struct UF_SF_POST_mark_vec_comp_s UF_SF_POST_mark_vec_comp_t;
typedef struct UF_SF_POST_mark_vec_comp_s *UF_SF_POST_mark_vec_comp_t_p;

struct UF_SF_POST_result_parms_s
{
    int                         abs_sw;
    int                         avg_sw;
    int                         lcase;
    int                         iter;
    double                      scale;
    UF_SF_POST_coord_sys_type_t coords;
    UF_SF_POST_result_type_t    res_type;
    UF_SF_POST_result_comp_t    comp;
    tag_t                       units_tag;
    UF_SF_POST_mark_vec_comp_t vcomp;
    int tensor_cube_sw;
    UF_SF_POST_elem_value_t elem_value;
    int eval_sw;
};
typedef struct UF_SF_POST_result_parms_s UF_SF_POST_result_parms_t;
typedef struct UF_SF_POST_result_parms_s *UF_SF_POST_result_parms_t_p;

 struct UF_SF_post_clipping_data_s 
  {
    int                  clip_tgl_data;
    int                  ghost_tgl_data;
    int                  outline_tgl_data;
    int                  auto_update_tgl_data;
    int                  plane_type_data;
    int                  clip_side_data;
    double               clip_value_data;
    int                  clip_scale_data;
    double               clip_scale_curr_min;
    double               clip_scale_curr_max;
    double               scale_min;
    double               scale_max;
};
typedef struct UF_SF_post_clipping_data_s UF_SF_post_clipping_data_t;
typedef struct UF_SF_post_clipping_data_s *UF_SF_post_clipping_data_t_p;

struct UF_SF_post_deform_result_s
{
    int loadcase;
    int iteration;
    UF_SF_POST_result_type_t res_type;
    int scaling_choice;
    int undef_toggle;
    double scaling_value;

};
typedef struct UF_SF_post_deform_result_s UF_SF_post_deform_result_t;
typedef struct UF_SF_post_deform_result_s *UF_SF_post_deform_result_t_p;


typedef enum
{
    UF_SF_CLIP_ABS_XY,
    UF_SF_CLIP_ABS_YZ,
    UF_SF_CLIP_ABS_ZX,
    UF_SF_CLIP_WCS_XY,
    UF_SF_CLIP_WCS_YZ,
    UF_SF_CLIP_WCS_ZX,
    UF_SF_CLIP_WCS_CYL_RT,
    UF_SF_CLIP_WCS_CYL_TZ,
    UF_SF_CLIP_WCS_SPH_TP
}
UF_SF_clip_plane_t;
typedef UF_SF_clip_plane_t *UF_SF_clip_plane_t_p;

typedef enum
{
    UF_SF_CLIP_POSITIVE,
    UF_SF_CLIP_NEGATIVE,
    UF_SF_CLIP_BOTH
}
UF_SF_clip_side_t;
typedef UF_SF_clip_side_t *UF_SF_clip_side_t_p;

typedef enum UF_SF_POST_file_type_e
{
    UF_SF_POST_FILE_NONE,
    UF_SF_POST_FILE_ASCII,
    UF_SF_POST_FILE_BINARY,
    UF_SF_POST_FILE_VRML,
    UF_SF_POST_FILE_JT
}
UF_SF_POST_file_type_t;
typedef UF_SF_POST_file_type_t *UF_SF_POST_file_type_t_p;


/*****************************************************************************
  Structure defining the parameters of a fringe request.
******************************************************************************/
struct UF_SF_POST_fringe_s
{
    UF_SF_POST_fringe_style_t style;                /* Selected fringe style.      */
    UF_SF_POST_fringe_color_spec_t spec;            /* Selected fringe color spec. */
    UF_SF_POST_fringe_scale_spec_t fringe_scale;    /* Scale method option 
                                                Auto/Linear/Log Scales      */
    logical whole_sw;                          /* TRUE - calculate fringe 
                                                thresholds using whole
                                                model, otherwise use only
                                                the displayed model       */
    double threshold_max;                      /* Maximum color index value   */
    double threshold_min;                      /* Minimum color index value   */
    int    colors_used;                        /* number of colors used       */
    logical trans_sw;                          /* Fringe translucency switch  */
    UF_SF_POST_fringe_legend_opt_t legend;          /* Selected fringe legend style
                                               structures items are        */
    logical thresh_sw;
};
typedef struct UF_SF_POST_fringe_s UF_SF_POST_fringe_t;
typedef struct UF_SF_POST_fringe_s *UF_SF_POST_fringe_t_p;

typedef enum UF_SF_POST_ident_action_e
{
    UF_SF_POST_IDENT_NODES,
    UF_SF_POST_IDENT_ELEMS,
    UF_SF_POST_IDENT_ELEM_NODES,
    UF_SF_POST_IDENT_MESH_NODES,
    UF_SF_POST_IDENT_MESH_ELEMS,
    UF_SF_POST_IDENT_MESH_ELEMS_1D,
    UF_SF_POST_IDENT_MESH_ELEMS_2D,
    UF_SF_POST_IDENT_MESH_ELEMS_3D,
    UF_SF_POST_IDENT_EDGE_NODES,
    UF_SF_POST_IDENT_FACE_NODES,
    UF_SF_POST_IDENT_BODY_NODES,
    UF_SF_POST_IDENT_N_HIGH_NODES,
    UF_SF_POST_IDENT_N_LOW_NODES,
    UF_SF_POST_IDENT_N_HIGH_ELEMS,
    UF_SF_POST_IDENT_N_LOW_ELEMS,
    UF_SF_POST_IDENT_NODE_IDS,                       
    UF_SF_POST_IDENT_ELEM_IDS,                    
    UF_SF_POST_IDENT_NODE_BY_ELEM_IDS,                    
    UF_SF_POST_IDENT_1D_ELMS
}
UF_SF_POST_ident_action_t;
typedef UF_SF_POST_ident_action_t *UF_SF_POST_ident_action_t_p;

/* Soma start */
typedef enum
{
    UF_SF_SINGLE_VIEW = 1,
    UF_SF_SIDE_BY_SIDE,
    UF_SF_TOP_BOTTOM,
    UF_SF_THREE_VIEWS,
    UF_SF_FOUR_VIEWS,
    UF_SF_SIX_VIEWS,
    UF_SF_NINE_VIEWS
}
UF_SF_POST_layout_type_t;
typedef UF_SF_POST_layout_type_t *UF_SF_POST_layout_type_t_p;
/* Soma end */

struct UF_SF_POST_ident_parms_s
{
    UF_SF_POST_ident_action_t action;
    int number;
    char *id_string;
    logical List_all_Comp_sw;
};
typedef struct UF_SF_POST_ident_parms_s UF_SF_POST_ident_parms_t;
typedef struct UF_SF_POST_ident_parms_s *UF_SF_POST_ident_parms_t_p;

/*****************************************************************************
  Structure defining the parameters for deformed model scaling
******************************************************************************/

struct UF_SF_POST_def_s
{
    char    dsn[UF_SF_POST_DSN_NM_SZ +1];      /* FOCUS result dataset name   */
    logical rel_sw;                            /* Show relative deformations  */
    double  rel_percentage;                    /* relative def model percent  */
    double  true_multiplier;                   /* true deformation scaling    */
};
typedef struct UF_SF_POST_def_s UF_SF_POST_def_t;
typedef struct UF_SF_POST_def_s *UF_SF_POST_def_t_p;

/*****************************************************************************
  Structure defining the parameters to display an undeformed model
******************************************************************************/

struct UF_SF_POST_undef_disp_s
{
    UF_SF_POST_elem_edge_style_t edge_style;        /* Element edge rendering      */
    UF_SF_POST_hue_colors_t edge_color;             /* Element edge color          */
    UF_SF_POST_elem_face_style_t face_style;        /* Element face rendering      */
    UF_SF_POST_hue_colors_t face_color;             /* Element edge color          */
};
typedef struct UF_SF_POST_undef_disp_s UF_SF_POST_undef_disp_t;
typedef struct UF_SF_POST_undef_disp_s *UF_SF_POST_undef_disp_t_p;

/*****************************************************************************
  Structure defining the parameters to display a deformed model
******************************************************************************/

struct UF_SF_POST_def_disp_s
{
    UF_SF_POST_elem_edge_style_t edge_style;        /* Element edge rendering      */
    UF_SF_POST_hue_colors_t edge_color;             /* Element edge color          */
    UF_SF_POST_elem_face_style_t face_style;        /* Element face rendering      */
    UF_SF_POST_hue_colors_t face_color;             /* Element edge color          */
    UF_SF_POST_elem_display_t elem_disp;            /* Element display             */
    UF_SF_POST_display_marker_t display_marker;     /* Marker display              */
    logical def_sw;                                 /* whether to display as def   */
    logical undef_sw;                               /* whether to display undef fem*/
    int num_vgrid;                                  /* number of vgrid in p model  */
    UF_SF_POST_undef_disp_t undef_data;             /* undeformed data structure   */

    /* NOTE : The following members are NOT used during UFT testing. They are
     *        here as placeholders to maintain parallelism with SFPPM_fem_disp_t_p 
     */
    logical mesh_disp_flag;
    int     mesh_group_count;
    int     *mesh_count; /* <len:mesh_group_count> */
    tag_t   **mesh_tags; /* <len:mesh_count> */
    int     **mesh_disp; /* <len:mesh_count> */
    int     **mesh_post_id; /* <len:mesh_count */
    int     **mesh_geom_in_sync; /* <len:mesh_count */
};
typedef struct UF_SF_POST_def_disp_s UF_SF_POST_def_disp_t;
typedef struct UF_SF_POST_def_disp_s *UF_SF_POST_def_disp_t_p;

/************ target **************/

typedef enum
{
    UF_SF_POST_TARGET_FREEFACE = 0,
    UF_SF_POST_TARGET_VOLUME,
    UF_SF_POST_TARGET_CUTTINGPLANE
}
UF_SF_POST_target_t;
typedef UF_SF_POST_target_t *UF_SF_POST_target_t_p;

typedef struct { 
    int                  post_view_id;
    char                 filename_text_data[UF_CFI_MAX_PATH_NAME_SIZE];
    int                  icon_toggle;
    char                 name_text_data[UF_CFI_MAX_FILE_NAME_LEN];
    int                  is_default;
} UF_SF_POST_template_data_t, *UF_SF_POST_template_data_t_p;

typedef enum 
{
    UF_SF_POST_UNKNOWN_TEMPLATE_TYPE = -1,
    UF_SF_POST_TEMPLATE_TYPE_LAYOUT,
    UF_SF_POST_TEMPLATE_TYPE_POSTVIEW
} UF_SF_POST_template_type_t;
typedef UF_SF_POST_template_type_t *UF_SF_POST_template_type_t_p;

typedef enum {
    UF_SF_POST_MARK_ARROW_STYLE_LINE,
    UF_SF_POST_MARK_ARROW_STYLE_UMBRELLA,
    UF_SF_POST_MARK_ARROW_STYLE_CYLINDER
} UF_SF_POST_mark_arrow_style_t;

typedef enum {
    UF_SF_POST_MARK_TENSOR_STYLE_ARROWS,
    UF_SF_POST_MARK_TENSOR_STYLE_CROWSFEET,
    UF_SF_POST_MARK_TENSOR_STYLE_BOX
} UF_SF_POST_mark_tensor_style_t;

typedef enum {
    UF_SF_POST_MARK_COLOR_RESULT,
    UF_SF_POST_MARK_COLOR_ANNOTEXT,
    UF_SF_POST_MARK_COLOR_SELECTED
} UF_SF_POST_mark_color_type_t;

typedef enum {
    UF_SF_POST_MARK_SIZE_RESULT,
    UF_SF_POST_MARK_SIZE_CONSTANT
} UF_SF_POST_mark_size_type_t;

typedef enum {
    UF_SF_POST_MARK_SIZE_MODELPERCENT,
    UF_SF_POST_MARK_SIZE_VALUE
} UF_SF_POST_mark_size_valtype_t;

typedef enum {
    UF_SF_POST_MARK_AT_NODES,
    UF_SF_POST_MARK_AT_ELEMCENTROID
} UF_SF_POST_mark_loc_type_t;

typedef enum {
    UF_SF_POST_MARK_HIDE_RESULTPERCENT,
    UF_SF_POST_MARK_HIDE_VALUE
} UF_SF_POST_mark_hide_valtype_t;

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif

