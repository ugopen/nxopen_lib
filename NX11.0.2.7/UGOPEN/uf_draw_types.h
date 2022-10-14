/*******************************************************************************
             Copyright (c) 1998-2006 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       



File description:

Contains Open C API typedefs and macros that are specific to the DRAW module.

*****************************************************************************/

#ifndef UF_DRAW_TYPES_INCLUDED
#define UF_DRAW_TYPES_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_drf_types.h>
#include <uf_object_types.h>

#ifdef __cplusplus
extern "C" {
#endif

#define UF_DRAW_NUM_VIEW_PARMS 9
#define UF_DRAW_MAX_NUM_SXSEGS 99
#define UF_DRAW_MAX_NUM_STEP_SXSEGS 49
#define UF_DRAW_MAX_LABEL_LEN  (132)

/*************************************************************************
 Section through components attribute name:                             
    This is the user-defined string attribute title.                    
    A string value of yes is the default.  Components are sectioned.    
    A string value of no indicates that the component is not sectioned. 
    For more information, reference the Drafting User's Manual.          
**************************************************************************/
#define UF_DRAW_SECTION_ATTR     "section-component" 
/*************************************************************************
 Curve for Hidden Line Removal attribute name:                             
    This is the user-defined string attribute title.                    
    A string value of yes is to allow the curve to join the process of 
    Hidden Line Removal.
    A string value of no indicates that the curve is not to join the process
    of Hidden Line Removal.
    For more information, reference the Drafting User's Manual.          
**************************************************************************/
#define UF_DRAW_CURVE_HLR_ATTR "DMV_HLR"
/*******************************************************************************
Attribute name for the curve for Hidden Line Processing:                             
This is the user-defined attribute of Null type.                
If this attribute is assigned to a curve, The curve will be ignored during 
Hidden Line Processing.
The curves without this attribute will participate during Hidden Line Processing.
********************************************************************************/
#define UF_DRAW_CURVE_HLP_ATTR "DMV_HLP_IGNORE"
/*************************************************************************
 Arrow head types                                                      
*************************************************************************/
enum UF_DRAW_arw_head_type_e 
{
        UF_DRAW_ansi_arrow = 1,
        UF_DRAW_iso_arrow,
        UF_DRAW_iso128,       
        UF_DRAW_jis,         
        UF_DRAW_gb          
};

typedef enum UF_DRAW_arw_head_type_e UF_DRAW_arw_head_type_t;

/*************************************************************************
 Arrow head control (style)
 
*************************************************************************/
enum UF_DRAW_arw_head_cntl_e 
{
        UF_DRAW_closed_arrowhead = 1,
        UF_DRAW_open_arrowhead,
        UF_DRAW_filled_arrowhead
};

typedef enum UF_DRAW_arw_head_cntl_e UF_DRAW_arw_head_cntl_t;

/*************************************************************************
 Section line segment type                                              
*************************************************************************/
enum UF_DRAW_sxseg_type_e 
{
        UF_DRAW_sxseg_arrow = UF_arrow_segment_subtype,
        UF_DRAW_sxseg_cut = UF_cut_segment_subtype,
        UF_DRAW_sxseg_bend = UF_bend_segment_subtype
};
typedef enum UF_DRAW_sxseg_type_e UF_DRAW_sxseg_type_t;

/*************************************************************************
 Revolved section line leg                                              
*************************************************************************/
enum UF_DRAW_sxline_leg_e 
{
        UF_DRAW_sxline_leg1 = 1,
        UF_DRAW_sxline_leg2
};
typedef enum UF_DRAW_sxline_leg_e UF_DRAW_sxline_leg_t;

/*************************************************************************
 Section line status                                                    
**************************************************************************/
enum UF_DRAW_sxline_status_e 
{
        UF_DRAW_invalid_sxline = 0, /* 
                                    status may require that a segment be 
                                    added with UF_DRAW_add_sxline_sxseg
                                    */
        UF_DRAW_valid_sxline, /* section line is valid */
        UF_DRAW_sxline_sxseg_lost_assoc, /* warning, at least one segment
                                         of section line lost associativity
                                         */
        UF_DRAW_sxline_rotpt_lost_assoc, /* warning, section line rotation
                                         point lost associativity 
                                         */
        UF_DRAW_sxline_rotpt_or_sxseg_lost_assoc /* 
                                                 warning, section line rotation
                                                 point lost associativity and at
                                                 least one segment of section
                                                 line lost associativity
                                                 */
};
typedef enum UF_DRAW_sxline_status_e UF_DRAW_sxline_status_t;

/************************************************************************
 Section line display                                                   
*************************************************************************/
enum UF_DRAW_sxline_display_e 
{
        UF_DRAW_no_display_sxline = 1,
        UF_DRAW_display_sxline
};
typedef enum UF_DRAW_sxline_display_e UF_DRAW_sxline_display_t;

/**************************************************************************
 Section line segment mode                                              
**************************************************************************/
enum UF_DRAW_sxseg_mode_e 
{
        UF_DRAW_user_defined_sxseg = 1,
        UF_DRAW_system_defined_sxseg
};
typedef enum UF_DRAW_sxseg_mode_e UF_DRAW_sxseg_mode_t;

/*************************************************************************
 Section line type                                                      
*************************************************************************/
enum UF_DRAW_sxline_type_e 
{
        UF_DRAW_simple_sxline = 1,
        UF_DRAW_stepped_sxline,
        UF_DRAW_revolved_sxline,
        UF_DRAW_half_sxline,
        UF_DRAW_unfolded_sxline,
        UF_DRAW_breakline,
        UF_DRAW_folded_sxline
};
typedef enum UF_DRAW_sxline_type_e UF_DRAW_sxline_type_t;

/*************************************************************************
 Section segment highlight status                                       
**************************************************************************/
enum UF_DRAW_sxseg_highlight_e 
{
        UF_DRAW_unhighlighted = 0,
        UF_DRAW_highlighted
};
typedef enum UF_DRAW_sxseg_highlight_e UF_DRAW_sxseg_highlight_t;

/************************************************************************
 Arrow parameters structure for section line display                    
*************************************************************************/
typedef struct UF_DRAW_arrow_parms_s *UF_DRAW_arrow_parms_p_t;
struct UF_DRAW_arrow_parms_s {
        double                  size; /* Arrow size must be greater than 0.
                                       
                                      */
        double                  total_length; /* Arrow total length (must be 
                                                 greater than 0)  
                                              */ 
        double                  incl_angle; /* Arrow included angle
                                            (must be greater than 0)  
                                             */
        double                  past_part_dist; /* Arrow past part
                                                (must be greater than 0) 
                                      
                                                */
        double                  stub_len; /* Arrow stub length
                                          (must be greater than 0)
                                      
                                          */
        UF_DRAW_arw_head_type_t head_type; /* Arrow head type 
                                           UF_DRAW_ansi_arrow = ansi arrow
                                           UF_DRAW_iso_arrow = iso arrow
                                      
                                           */
        UF_DRAW_arw_head_cntl_t head_control; /* Arrow head control (style)
                                               (must be greater than 0)
                                              UF_DRAW_open_arrowhead 
                                              UF_DRAW_closed_arrowhead 
                                              UF_DRAW_filled_arrowhead
                                      
                                              */
} ;
typedef struct UF_DRAW_arrow_parms_s UF_DRAW_arrow_parms_t;

/**************************************************************************
 Half section line segment object structure                             
**************************************************************************/
typedef struct UF_DRAW_half_sxsegs_s *UF_DRAW_half_sxsegs_p_t;
struct UF_DRAW_half_sxsegs_s {
        UF_DRF_object_p_t    bend_object; /* Object associated to bend segment*/
        UF_DRF_object_p_t    cut_object; /* Object associated to cut segment */
        UF_DRF_object_p_t    arrow_object; /* Object associated to arrow 
                                              segment */
} ;
typedef struct UF_DRAW_half_sxsegs_s UF_DRAW_half_sxsegs_t;

/*************************************************************************
 Section line segment object structure used for revolved, stepped       
 and unfolded section line types.                                      
*************************************************************************/
typedef struct UF_DRAW_sxline_sxsegs_s *UF_DRAW_sxline_sxsegs_p_t;
struct UF_DRAW_sxline_sxsegs_s {
UF_DRAW_sxseg_type_t sxseg_type; /* UF_DRAW_sxseg_arrow = arrow segment
                                    UF_DRAW_sxseg_cut  = cut segment
                                    UF_DRAW_sxseg_bend = bend segment
                                 */
UF_DRF_object_p_t sxseg_object; /* Object associated to section line segment */
double sxseg_angle;             /* Angle of section segment in degrees from 
                                   -180 to 180 (for unfolded section line 
                                   segments only)
                                */
} ;
typedef struct UF_DRAW_sxline_sxsegs_s UF_DRAW_sxline_sxsegs_t;

/*************************************************************************
 Section line segment structure                                         
**************************************************************************/
struct UF_DRAW_sxseg_info_s
{
  UF_DRAW_sxseg_type_t    sxseg_type; /* Segment type:
                                           UF_DRAW_sxseg_arrow = arrow segment
                                           UF_DRAW_sxseg_cut  = cut segment 
                                           UF_DRAW_sxseg_bend = bend segment 
                                      */
  UF_DRAW_sxline_leg_t    leg_num; /* Segment leg number: 
                                      If REVOLVED Section Line, then leg_num 
                                      can be UF_DRAW_sxline_leg1 or 
                                      UF_DRAW_sxline_leg2.  In all other cases
                                      it will be UF_DRAW_sxline_leg1.
                                   */               
  UF_DRAW_sxseg_mode_t    sxseg_mode; /* Creation mode of segment:
                                         UF_DRAW_system_defined_sxseg 
                                         UF_DRAW_user_defined_sxseg
                                      */
  UF_DRAW_sxseg_highlight_t highlight_status; /* Segment highlight state
                                                 (due to lost associativity)
                                                 UF_DRAW_unhighlighted
                                                 UF_DRAW_highlighted
                                              */
  double sxseg_angle;                 /* Angle of segment (for unfolded section
                                         line segments only).  In degrees from
                                         -180 to 180.
                                      */
} ;

typedef struct UF_DRAW_sxseg_info_s UF_DRAW_sxseg_info_t;
typedef struct UF_DRAW_sxseg_info_s *UF_DRAW_sxseg_info_p_t;

/*************************************************************************
 Section view Section Sheet Bodies status                                         
**************************************************************************/
enum UF_DRAW_sx_section_sheet_body_e 
{
        UF_DRAW_sx_section_sheet_body_off = 0,
        UF_DRAW_sx_section_sheet_body_on
} ;
typedef enum UF_DRAW_sx_section_sheet_body_e UF_DRAW_sx_section_sheet_body_t;
/*************************************************************************
 Section view background status                                         
**************************************************************************/
enum UF_DRAW_sx_background_e 
{
        UF_DRAW_sx_background_off = 0,
        UF_DRAW_sx_background_on
} ;
typedef enum UF_DRAW_sx_background_e UF_DRAW_sx_background_t;
/**************************************************************************
 Section view crosshatch status                                         
**************************************************************************/
enum UF_DRAW_sx_crosshatch_e 
{
        UF_DRAW_sx_crosshatch_off = 0,
        UF_DRAW_sx_crosshatch_on
} ;
typedef enum UF_DRAW_sx_crosshatch_e UF_DRAW_sx_crosshatch_t;
/*************************************************************************
 Section view assembly crosshatching status                             
**************************************************************************/
enum UF_DRAW_sx_assy_xhatch_e 
{
        UF_DRAW_sx_assy_xhatch_off = 0,
        UF_DRAW_sx_assy_xhatch_on
} ;
typedef enum UF_DRAW_sx_assy_xhatch_e UF_DRAW_sx_assy_xhatch_t;
/**************************************************************************
 Hidden line removal status                                             
**************************************************************************/
enum UF_DRAW_hidden_line_e 
{
        UF_DRAW_hidden_line_removal_off = 0,
        UF_DRAW_hidden_line_removal_on
} ;
typedef enum UF_DRAW_hidden_line_e UF_DRAW_hidden_line_t;
/*************************************************************************
 Hidden edge status                                                     
**************************************************************************/
enum UF_DRAW_edge_hiding_edge_e 
{
        UF_DRAW_edge_hiding_edge_off = 0,
        UF_DRAW_edge_hiding_edge_on
} ;
typedef enum UF_DRAW_edge_hiding_edge_e UF_DRAW_edge_hiding_edge_t;
/**************************************************************************
 Edge smooth status                                                     
**************************************************************************/
enum UF_DRAW_smooth_e 
{
        UF_DRAW_smooth_off = 0,
        UF_DRAW_smooth_on
} ;
typedef enum UF_DRAW_smooth_e UF_DRAW_smooth_t;
/*************************************************************************
 Silhouette status                                                      
**************************************************************************/
enum UF_DRAW_silhouette_e 
{
        UF_DRAW_silhouettes_off = 0,
        UF_DRAW_silhouettes_on
} ;
typedef enum UF_DRAW_silhouette_e UF_DRAW_silhouette_t;
/*************************************************************************
 UV Hatch status                                                     
**************************************************************************/
enum UF_DRAW_uvhatch_e 
{
        UF_DRAW_uvhatch_off = 0,
        UF_DRAW_uvhatch_on
} ;
typedef enum UF_DRAW_uvhatch_e UF_DRAW_uvhatch_t;
/*************************************************************************
 Smooth Edge Gap status                                                 
**************************************************************************/
enum UF_DRAW_gap_e 
{
        UF_DRAW_gap_off = 0,
        UF_DRAW_gap_on
} ;
typedef enum UF_DRAW_gap_e UF_DRAW_gap_t;
/**************************************************************************
 Virtual Intersection Curve status                                      
**************************************************************************/
enum UF_DRAW_virtual_intersect_e 
{
        UF_DRAW_virtual_intersect_off = 0,
        UF_DRAW_virtual_intersect_on
} ;
typedef enum UF_DRAW_virtual_intersect_e UF_DRAW_virtual_intersect_t;    
/**************************************************************************
 Extracted edge status - should edges be extracted for the view?        
**************************************************************************/
enum UF_DRAW_extracted_edges_e 
{
        UF_DRAW_extracted_edges_off = 0,
        UF_DRAW_extracted_edges_on
} ;
typedef enum UF_DRAW_extracted_edges_e UF_DRAW_extracted_edges_t;
/**************************************************************************
 drafting curve type                                              
**************************************************************************/
enum UF_DRAW_drafting_curve_type_e 
{
        UF_DRAW_unknown_type = -1,
        UF_DRAW_extracted_edge_type = 1,
        UF_DRAW_silhouette_curve_type,
        UF_DRAW_thread_silhouette_curve_type,
        UF_DRAW_section_edge_type,
        UF_DRAW_thread_section_edge_type,
        UF_DRAW_vi_curve_type,
        UF_DRAW_uvhatch_curve_type,
        UF_DRAW_trace_line_type,
        UF_DRAW_simplified_curve_type,
        UF_DRAW_interference_curve_type,
        UF_DRAW_extracted_model_curve_type
};
typedef enum UF_DRAW_drafting_curve_type_e UF_DRAW_drafting_curve_type_t;
/**************************************************************************
 Section view structure                                                 
**************************************************************************/
typedef struct UF_DRAW_sxview_prfs_s *UF_DRAW_sxview_prfs_p_t;
struct UF_DRAW_sxview_prfs_s
{
        UF_DRAW_sx_section_sheet_body_t sx_section_sheet_body; 
                                                      /* Section view
                                                         Section Sheet Body
                                                         UF_DRAW_sx_section_sheet_body_off
                                                         UF_DRAW_sx_section_sheet_body_on
                                                      */

        UF_DRAW_sx_background_t        sx_background; /* Section view background
                                                      UF_DRAW_sx_background_on
                                                      UF_DRAW_sx_background_off
                                                      */
        UF_DRAW_sx_crosshatch_t        sx_crosshatch; /* Section view crosshatch
                                                      UF_DRAW_sx_crosshatch_off
                                                      UF_DRAW_sx_crosshatch_on
                                                      */
        UF_DRAW_sx_assy_xhatch_t       sx_assy_xhatch;
        double                         xhatch_adj_toler;
};
typedef struct UF_DRAW_sxview_prfs_s UF_DRAW_sxview_prfs_t;

/*****************************************************************************
 View display preferences structure                                         
******************************************************************************/
typedef struct UF_DRAW_view_prfs_s *UF_DRAW_view_prfs_p_t;
struct UF_DRAW_view_prfs_s
{
   UF_DRAW_hidden_line_t         hidden_line; /* Hidden line removal, use
                                              UF_DRAW_hidden_line_removal_off or
                                              UF_DRAW_hidden_line_removal_on
                                                   */
   int                           hidden_line_color; /* Hidden line color
                                                    */
   int                           hidden_line_font; /* Hidden line font
                                                  */
   int                           hidden_line_width; /* Hidden line width, 
                                                    please use 
                                                    UF_OBJ_WIDTH_NORMAL,
                                                    UF_OBJ_WIDTH_THIN,
                                                    UF_OBJ_WIDTH_THICK, or
                                                    UF_OBJ_WIDTH_ORIGINAL
                                                    */
   UF_DRAW_edge_hiding_edge_t    edge_hiding_edge; /* 
                                               UF_DRAW_edge_hiding_edge_off or
                                               UF_DRAW_edge_hiding_edge_on
                                                   */
   UF_DRAW_smooth_t              smooth; /* Smooth Edges UF_DRAW_smooth_off or
                                         UF_DRAW_smooth_on
                                         */
   double                        tolerance; /* Chord height tolerance for
                                            silhouettes and hidden line
                                            display; must be >= 0.0 
                                            */
   UF_DRAW_silhouette_t          silhouettes; /* UF_DRAW_silhouettes_off or
                                                 UF_DRAW_silhouettes_on
                                              */
   UF_DRAW_uvhatch_t             uvhatch; /* UF_DRAW_uvhatch_off or
                                             UF_DRAW_uvhatch_on
                                          */
   int                           smooth_edge_color; /* Smooth edge color
                                                       (0=original)
                                                    */  
   int                           smooth_edge_font; /* Smooth edge font
                                                      (0=original)
                                                   */
   int                           smooth_edge_width; /* Smooth edge width 
                                                    (see hidden_line_width)
                                                    */
   UF_DRAW_gap_t                 smooth_edge_gap; /* Smooth edge gap
                                                     (0=off, 1 = on)
                                                  */
   double                        smooth_edge_gap_size; /* Smooth edge gap 
                                                       size (in part units)
                                                       */
   UF_DRAW_virtual_intersect_t   virtual_intersect; /* Virtual intersection
                                                    curves (0=off, 1 = on)
                                                    */
   int                           virtual_intersect_color;/* Virtual 
                                                         intersection color
                                                         (0=original)
                                                         */
   int                           virtual_intersect_font; /* Virtual 
                                                         intersection font 
                                                         (0=original)
                                                         */
   int                           virtual_intersect_width;/* Virtual 
                                                         intersection width
                                                          (0=original)
                                                          */
   UF_DRAW_gap_t                 virtual_intersect_gap; 
   double                        virtual_intersect_gap_size;
   UF_DRAW_extracted_edges_t     extracted_edges; /* Associative Extracted 
                                                  Edge use (0=off, 1=on)
                                                  */
   int                           visible_line_color; /* (0 = original) */
   int                           visible_line_font;  /* (0=original)    */
   int                           visible_line_width; /* Please use either
                                                     UF_OBJ_WIDTH_NORMAL,
                                                     UF_OBJ_WIDTH_THIN,
                                                     UF_OBJ_WIDTH_THICK, or
                                                     UF_OBJ_WIDTH_ORIGINAL
                                                     */
   int         interfering_solids; /* 0 = no interfering solids
                                      1 = yes without Interference Curves
                                      2 = yes and render InterferenceCurves
                                   */ 
   logical     referenced_edges_only; /* When TRUE, renders only hidden lines 
                                      referencing annotation with hidden line 
                                      settings above.  When FALSE, all hidden 
                                      lines are rendered with hidden line 
                                      settings above. 
                                      */ 
   logical     edges_hidden_by_own_solid; /* When TRUE, renders self-hidden 
                                          edges according to hidden line 
                                          settings above.  When FALSE, only 
                                          edges hidden by other solids are 
                                          rendered according to hidden line 
                                          settings above. 
                                          */  
   int         simplify_small_features;  /* 0 =  don't simplify
                                            1 =  simplify features 
                                                 smaller than small_feature_tolerance 
                                                  when rendering hidden lines.
                                            2 = hide features small than the
                                                small_feature_tolerance when 
                                                rendering hidden lines. 
                                          */ 
   double       small_feature_tolerance;  /* Small feature tolerance percentage
                                          (from 0.0 to 5.00).  Features 
                                          smaller than this percentage of the 
                                          model will be simplified when 
                                          simplify_small_features is true. 
                                          */ 
   int           traceline_visible_color; /* Traceline visible color
                                             (0=original)
                                          */  
   int           traceline_visible_font; /* Traceline visible font
                                            (0=original)
                                         */
   int           traceline_visible_width; /* Traceline visible width 
                                             (see hidden_line_width)
                                          */
   int           traceline_hidden_color; /* Traceline hidden color
                                            (0=original)
                                         */  
   int           traceline_hidden_font; /* Traceline hidden font
                                           (0=invisible)
                                        */
   int           traceline_hidden_width; /* Traceline hidden width 
                                            (see hidden_line_width)
                                         */
   UF_DRAW_gap_t traceline_gap; /* Traceline gap
                                   (0=off, 1 = on)
                                */
   double        traceline_gap_size; /* Traceline gap 
                                        size (in part units)
                                     */
} ;
typedef struct UF_DRAW_view_prfs_s UF_DRAW_view_prfs_t;
/****************************************************************************
 * The following enum defines the rendering methods for all of the threads
 * in a given view.
 *****************************************************************************/
enum UF_DRAW_thd_meth_e 
{
    UF_DRAW_THD_METH_NONE=0,          /* No method specified (default for pre-v12 parts)
                                       */
    UF_DRAW_THD_METH_ANSI_SIMPLIFIED, /* Render threads using the ANSI 
                                       * standard simplified method
                                       */
    UF_DRAW_THD_METH_ANSI_SCHEMATIC,  /* Render threads using the ANSI 
                                       * standard schematic method
                                       */
    UF_DRAW_THD_METH_ANSI_DETAILED,   /* Render threads using the ANSI 
                                       * standard detailed method
                                       */
    UF_DRAW_THD_METH_ISO_SIMPLIFIED,  /* Render threads using the ISO 
                                       *standard simplified method
                                       */
    UF_DRAW_THD_METH_ISO_DETAILED,     /* Render thread using the ISO 
                                       * standard detailed method
                                       */
    UF_DRAW_THD_METH_ESKD_SIMPLIFIED  /* Render thread using the  
                                       * ESKD standard.
                                       */
};
typedef enum UF_DRAW_thd_meth_e UF_DRAW_thd_meth_t;
/*************************************************************************
 View Boundary structure - used for asking boundary curves and          
 making a view boundary associative to the model.                      
**************************************************************************/

struct UF_DRAW_view_boundary_s {
    tag_t   curve_tag;    /* Tag of boundary curve. */    
    logical const_status; /* Construction status of a curve.
                                FALSE = not a construction line
                                TRUE  = curve is a construction line
                             This parameter is unused when defining a 
                             view boundary (you cannot define a view
                             boundary with a construction curve with
                             NX Open API).
                          */
    int     point_count;  /* Number of defining points for the curve.*/
    tag_p_t defining_points; /* <len:point_count> Array of defining points for the curve */
    tag_t   hatch_tag;       /* Tag of hatch object */
};
typedef struct UF_DRAW_view_boundary_s UF_DRAW_view_boundary_t, 
               *UF_DRAW_view_boundary_p_t;
/**************************************************************************
 Define View Boundary structure - setting a break line detail type      
 view boundary.                                                         
*************************************************************************/
  
struct UF_DRAW_define_boundary_s {
        tag_t                   curve_tag; /* Tag of curve defining the
                                              view boundary. */
};
typedef struct UF_DRAW_define_boundary_s UF_DRAW_define_boundary_t, 
               *UF_DRAW_define_boundary_p_t;
/**************************************************************************
 Drawing Sizes                                                          
**************************************************************************/
enum UF_DRAW_metric_size_e 
{
    UF_DRAW_A0 = 1,    /* 841 x 1189 */
    UF_DRAW_A1,        /* 594 X  841 */
    UF_DRAW_A2,        /* 420 X  594 */
    UF_DRAW_A3,        /* 297 X  420 */
    UF_DRAW_A4         /* 210 X  297 */
};
typedef enum UF_DRAW_metric_size_e UF_DRAW_metric_size_t;

enum UF_DRAW_english_size_e 
{
    UF_DRAW_A = 1,    /* 8.5 x 11 */
    UF_DRAW_B,        /* 11 X  17 */
    UF_DRAW_C,        /* 17 X  22 */
    UF_DRAW_D,        /* 22 X  34 */
    UF_DRAW_E,        /* 34 X  44 */
    UF_DRAW_F,        /* 28 X  40 */
    UF_DRAW_H,        /* 28 X  44 */
    UF_DRAW_J         /* 34 X  55 */
};
typedef enum UF_DRAW_english_size_e UF_DRAW_english_size_t;

union UF_DRAW_size_union_u
{
    UF_DRAW_metric_size_t  metric_size_code;
    UF_DRAW_english_size_t english_size_code;
    double                 custom_size[2];
};
typedef union UF_DRAW_size_union_u UF_DRAW_size_union_t;

enum UF_DRAW_size_state_e 
{ 
    UF_DRAW_METRIC_SIZE = 0,
    UF_DRAW_ENGLISH_SIZE,
    UF_DRAW_CUSTOM_SIZE
};
typedef enum UF_DRAW_size_state_e UF_DRAW_size_state_t;
/*************************************************************************
 Projection Angles                                                      
**************************************************************************/
enum UF_DRAW_projection_angle_e 
{
    UF_DRAW_NO_ANGLE_DATA = 0,
    UF_DRAW_THIRD_ANGLE_PROJECTION,
    UF_DRAW_FIRST_ANGLE_PROJECTION
};
typedef enum UF_DRAW_projection_angle_e UF_DRAW_projection_angle_t;

/**************************************************************************
 View Status for Adding Views                                           
**************************************************************************/
enum UF_DRAW_view_status_e 
{
    UF_DRAW_ACTIVE_VIEW = 1,
    UF_DRAW_REFERENCE_VIEW
};
typedef enum UF_DRAW_view_status_e UF_DRAW_view_status_t;
/*************************************************************************
 Boundary types                                                         
**************************************************************************/
enum UF_DRAW_boundary_type_e 
{
    UF_DRAW_BREAK_DETAIL_TYPE = 1,
    UF_DRAW_MANUAL_RECTANGLE_TYPE,
    UF_DRAW_AUTOMATIC_RECTANGLE_TYPE,
    UF_DRAW_BOUND_BY_OBJECTS_TYPE
};
typedef enum UF_DRAW_boundary_type_e UF_DRAW_boundary_type_t;
/**************************************************************************
 Orthographic Projection Direction                                      
**************************************************************************/
enum UF_DRAW_proj_dir_e 
{
        UF_DRAW_project_infer = 0,
        UF_DRAW_project_above,
        UF_DRAW_project_right,
        UF_DRAW_project_below,
        UF_DRAW_project_left
};
typedef enum UF_DRAW_proj_dir_e UF_DRAW_proj_dir_t;

/**************************************************************************
 Drawing Info Structure                                                 
**************************************************************************/
typedef struct UF_DRAW_info_s *UF_DRAW_info_p_t;

struct UF_DRAW_info_s{
    UF_DRAW_size_state_t       size_state; /* Flag specifying the type used in
                                              size, UF_DRAW_METRIC_SIZE,
                                              UF_DRAW_ENGLISH_SIZE or 
                                              UF_DRAW_CUSTOM_SIZE. */
    UF_DRAW_size_union_t       size;       /* The drawing size, as specified in
                                              size_state.  If using metric, 
                                              then use a UF_DRAW_metric_size_t
                                              variable.  If using english, use
                                              a UF_DRAW_english_size_t
                                              variable.  If using a custom size,
                                              specify the size in a double array
                                              where size[0] is the height and
                                              size[1] is the length.
                                            */
    double                     drawing_scale; /* The drawing scale. */
    int                        units; /* The drawing units, either 
                                         UF_PART_METRIC or UF_PART_ENGLISH. */
    UF_DRAW_projection_angle_t projection_angle; /* The projection angle, either
                                               UF_DRAW_THIRD_ANGLE_PROJECTION or
                                               UF_DRAW_FIRST_ANGLE_PROJECTION.
                                               */
};
typedef struct UF_DRAW_info_s UF_DRAW_info_t;

/**************************************************************************
 Drawing Member View Structure                                          
**************************************************************************/
typedef struct UF_DRAW_view_info_s *UF_DRAW_view_info_p_t;
struct UF_DRAW_view_info_s{
    UF_DRAW_view_status_t  view_status; /* Active = UF_DRAW_ACTIVE_VIEW,
                                           reference = UF_DRAW_REFERENCE_VIEW.
                                        */
    tag_t                  anchor_point; /* The anchor point of the view.  Must
                                            be a smart point (see uf_so.h). 
                                            When adding a view, if no anchor 
                                            point is desired, use NULL_TAG.  If
                                            you wish to set the view reference
                                            point with a "dumb" point, use 
                                            uc6484.
                                          */
    double                 view_scale;    /* The view scale. */
    logical                use_ref_pt;    /* If true, then used the saved
                                             reference point. */
    logical                clean_model_view; /* v15.0 No longer used, model
                                                views can no longer be cleaned 
                                                when imported onto a drawing  */
    logical                inherit_boundary; /* If TRUE, then the drawing view
                                                will inherit the model view's
                                                boundary. */
    logical                transfer_annotation;  /* If TRUE, annotations are
                                                  moved from model view to 
                                                 imported drawing view */
    logical                inherit_pmi;      /* If TRUE, then PMI are copied
                                                from the model view to the
                                                imported drawing view */
   char model_name[UF_DRAW_MAX_LABEL_LEN];   /* Part name for the view, filespec with path, must not be NULL or empty.
                                               Used only when importing views
                                               or asking the settings of a view */
   char arrangement_name[UF_DRAW_MAX_LABEL_LEN];  /* Name of arrangement, may be '\0'.
                                                   Used only when importing views, or 
                                                   asking the settings of a view. */
};
typedef struct UF_DRAW_view_info_s UF_DRAW_view_info_t;

/******************************************************************************
 * Render Set display preferences structure                                   
 *                                                                           
 ******************************************************************************/
typedef struct UF_DRAW_render_prefs_s *UF_DRAW_render_prefs_p_t;
struct UF_DRAW_render_prefs_s
{
  UF_DRAW_hidden_line_t         hidden_line; /* Hidden line rendering */
  int                           hidden_line_color; /* Hidden line color 
                                                      (0=original)  */
  int                           hidden_line_font; /* Hidden line font 
                                                     (0=original)  */
  int                           hidden_line_width; /* Hidden line width, use  
                                                      UF_OBJ_WIDTH_NORMAL
                                                      UF_OBJ_WIDTH_THIN
                                                      UF_OBJ_WIDTH_THICK
                                                      UF_OBJ_WIDTH_ORIGINAL */
  UF_DRAW_edge_hiding_edge_t   edge_hiding_edge; /* UF_DRAW_edge_hiding_edge_off
                                                    UF_DRAW_edge_hiding_edge_on
                                                 */
  int                           visible_line_color; /* Visible line color
                                                       (0=original) */
  int                           visible_line_font; /* Visible line font  
                                                      (0=original) */
  int                           visible_line_width; /* Visible line width, use 
                                                       UF_OBJ_WIDTH_NORMAL
                                                       UF_OBJ_WIDTH_THIN
                                                       UF_OBJ_WIDTH_THICK
                                                       UF_OBJ_WIDTH_ORIGINAL */
  logical       referenced_edges_only;  /* When TRUE, renders only hidden lines
                                           referencing annotation with hidden 
                                           line settings above. When FALSE, all 
                                           hidden lines are rendered with 
                                           hidden line settings above. 
                                        */ 
  logical       edges_hidden_by_own_solid; /* When TRUE, renders self-hidden 
                                              edges according to hidden line 
                                              settings above. When FALSE, only 
                                              edges hidden by other solids 
                                              are rendered according to hidden 
                                              line settings above. 
                                           */ 
};
typedef struct UF_DRAW_render_prefs_s UF_DRAW_render_prefs_t;

/* Pen assignment for plot data. */
enum UF_DRAW_pen_assignment_e
{
    UF_DRAW_USE_CURRENT_VALUE = 0,
    UF_DRAW_DENSITY,
    UF_DRAW_COLOR
};
typedef enum UF_DRAW_pen_assignment_e UF_DRAW_pen_assignment_t;

/* Data source for plot data. */
enum UF_DRAW_data_source_e
{
    UF_DRAW_DRAWING_DATA = 0,
    UF_DRAW_DEFAULT_DATA
};
typedef enum UF_DRAW_data_source_e UF_DRAW_data_source_t;

/**************************************************************************
* Drawing Plotter Data Structure                                         
**************************************************************************/
typedef struct UF_DRAW_plotter_data_s *UF_DRAW_plotter_data_p_t;
struct UF_DRAW_plotter_data_s
{
    char        plotter_name[17]; /* Plotter name (16 characters max). */
    double      plot_scale;       /* Plot scale. */
    double      rotation;         /* Rotation angle (in degrees).*/
    int         media_ref_num;    /* Media reference number. */
    int         copies;           /* Number of copies. */
    double      plot_origin[2];   /* Plot origin (XY coordinates).
                                     [0] - X coordinate 
                                     [1] - Y coordinate  */
    double      plot_offset[2];   /* Plot offset (XY coordinates).
                                     [0] - X offset
                                     [1] - Y offset  */
    UF_DRAW_pen_assignment_t   pen_assignment;   /* Pen assignment.
                                                      UF_DRAW_DENSITY 
                                                      UF_DRAW_COLOR  */
    int                        pen_list[16];     /* Pen list. */
    UF_DRAW_data_source_t      data_source;      /* Data source.
                                                      UF_DRAW_DRAWING_DATA
                                                      UF_DRAW_DEFAULT_DATA */
} ;

typedef struct UF_DRAW_plotter_data_s UF_DRAW_plotter_data_t;

/* Sectioning component in view settings. */
enum UF_DRAW_comp_section_in_view_e
{
    UF_DRAW_NON_SECTIONED = 0,
    UF_DRAW_SECTIONED,
    UF_DRAW_NOT_VIEW_SPECIFIED
};
typedef enum UF_DRAW_comp_section_in_view_e UF_DRAW_comp_section_in_view_t;

/* Breakout section data structure. */
struct UF_DRAW_breakout_data_s
{ 
    tag_t     base_point;            /* Base point on the floor of breakout */
    tag_t     extrusion_vector;      /* If NULL_TAG, the extrusion vector is  
                                        perpendicular to the xy plane of the
                                        view and points toward the viewer.  
                                        Otherwise, the vector is perpendicular
                                        to the floor of the breakout section
                                        and points toward the side of the floor
                                        on which the material of the part is
                                        removed. */
    int       num_curves;            /* Number of breakout curves */
    tag_p_t   curves;                /* <len:num_curves> Breakout curves */
    logical  *const_status;          /* <len:num_curves> Construction status of each
                                        breakout curve */
    logical   cut_thru_model;        /* Cut through the model */
    logical   hidden_line_hatching;  /* Hidden line hatching */
}; 
typedef struct UF_DRAW_breakout_data_s
               UF_DRAW_breakout_data_t, *UF_DRAW_breakout_data_p_t; 

/* break region positioning mehods */
enum UF_DRAW_break_position_type_e
{
    UF_DRAW_BREAK_POSITION_INFERRED = 0,
    UF_DRAW_BREAK_POSITION_DISTANCE,
    UF_DRAW_BREAK_POSITION_TWO_REGIONS,
    UF_DRAW_BREAK_POSITION_DEFAULT
};
typedef enum UF_DRAW_break_position_type_e UF_DRAW_break_position_type_t;

/* Breakout section data structure. */
struct UF_DRAW_break_region_data_s
{ 
    tag_t  view_tag;                /* Tag of broken view */
    UF_DRAW_break_position_type_t position_type;
                                    /* Positioning method */
    double distance;                /* Distance (gap) between aligned XY boxes
                                       of break region and reference region in
                                       drawing units; for inferred and
                                       distance position types only */
    tag_t  reference_regions[2];    /* Break region(s) to be used as reference 
                                       for alignment */
    tag_t  alignment_vectors[2];    /* Direction(s) of alignment in drawing 
                                       coordinates */
}; 
typedef struct UF_DRAW_break_region_data_s
               UF_DRAW_break_region_data_t, *UF_DRAW_break_region_data_p_t; 

/* Break Region boundary structure */
struct UF_DRAW_break_region_boundary_s {
    tag_t   curve_tag;              /* Tag of curve defining the break region 
                                       boundary */
    logical construction_curve;     /* TRUE if hidden; FALSE if visible */
    logical hatch_curve;            /* TRUE if curve is to be hatched; FALSE 
                                       if not */
};
typedef struct UF_DRAW_break_region_boundary_s
               UF_DRAW_break_region_boundary_t, *UF_DRAW_break_region_boundary_p_t;

/* view label parameter type */ 
typedef enum
{
        UF_DRAW_view_label_other_view = 1, 
        UF_DRAW_view_label_detail_view , 
        UF_DRAW_view_label_section_view,
        UF_DRAW_view_label_projected_view
} UF_DRAW_view_label_parm_type_t; 

/* view label view label type - use view name or prefix and letter */ 
typedef enum
{
        UF_DRAW_view_label_view_name = 1, 
        UF_DRAW_view_label_prefix_and_letter 
} UF_DRAW_view_label_view_text_type_t; 

/* view label letter format */ 
typedef enum
{
        UF_DRAW_view_label_single_letter = 1, 
        UF_DRAW_view_label_dashed_letter 
} UF_DRAW_view_label_letter_format_t; 

/* view label scale position relative to view label */
typedef enum
{
        UF_DRAW_view_label_below = 1,   /* scale label is below view label  */
        UF_DRAW_view_label_above,       /* scale label is above view label  */
        UF_DRAW_view_label_before,      /* scale label is before view label */
        UF_DRAW_view_label_after        /* scale label is after view label  */
} UF_DRAW_view_label_scale_position_t; 

/* view label position relative to view boundary */ 
typedef enum
{
        UF_DRAW_view_label_below_boundary = 1, 
        UF_DRAW_view_label_above_boundary 
} UF_DRAW_view_label_position_t; 

/* view label scale format */ 
typedef enum
{
        UF_DRAW_view_label_ratio = 1, 
        UF_DRAW_view_label_vertical_fraction, 
        UF_DRAW_view_label_horizontal_fraction,
        UF_DRAW_view_label_Nx
} UF_DRAW_view_label_scale_format_t; 


/* view label on parent type - used for detail views */ 
typedef enum
{
        UF_DRAW_parent_view_label_no_display = 0,  /* no circle */
        UF_DRAW_parent_view_label_boundary,        /* circle    */
        UF_DRAW_parent_view_label_circle = UF_DRAW_parent_view_label_boundary, /* alternate name for circle    */
        UF_DRAW_parent_view_label_note,            /* circle with note */
        UF_DRAW_parent_view_label_label,           /* circle with label */
        UF_DRAW_parent_view_label_embedded,        /* embedded note in circle */
        UF_DRAW_parent_view_label_true_boundary    /* true boundary */
} UF_DRAW_label_on_parent_type_t;

/* view label text to stub format option - used for detail views */
typedef enum
{
        UF_DRAW_parent_view_label_text_before_stub = 0,
        UF_DRAW_parent_view_label_text_above_stub
} UF_DRF_view_label_text_to_stub_format_t;

/* Secondary indexing alignment */
typedef enum
{
    UF_DRAW_secondary_indexing_inline = 0,
    UF_DRAW_secondary_indexing_subscript
} UF_DRAW_secondary_indexing_align_t;


#define UF_DRAW_MAX_LETTER_NCHARS 30
#define UF_DRAW_MAX_LETTER_BUFSIZE NX_BUFSIZE(UF_DRAW_MAX_LETTER_NCHARS) 

/*  */ 
#define UF_DRAW_MAX_LETTER_LEN (UF_DRAW_MAX_LETTER_BUFSIZE-1) 
/*  */ 


/* view label preferences */ 
struct UF_DRAW_view_label_parms_s { 
    UF_DRAW_view_label_parm_type_t       view_label_parm_type; 
                                             /* Parameter type - Detail view, 
                                                Section View, or other. */ 
    UF_DRAW_view_label_view_text_type_t  view_label_type;           
                                            /* View label type - view name or 
                                               view letter */ 
    UF_DRAW_view_label_letter_format_t   letter_format;             
                                           /* Letter format - single letter or 
                                              letter separated by dash */ 
    UF_DRAW_view_label_position_t  view_label_position;       
                                          /* View Label position relative to 
                                             view boundary */ 
    UF_DRAW_view_label_scale_position_t  view_scale_position;       
                                          /* View Scale position relative to 
                                             view label */ 
    UF_DRAW_view_label_scale_format_t    view_scale_value_format;   
                                          /* View Scale value format - ratio, 
                                             vertical fraction, horizontal 
                                             fraction, or Nx */ 
    UF_DRF_view_label_text_to_stub_format_t view_label_text_to_stub_format;
                                          /* View lable text to stub format -
                                             controls the location of the text
                                             on the parent view label relative
                                             to the stub. */
    double     letter_size_factor;        /* Character size of letter relative 
                                             to the current font */ 
    double     view_scale_prefix_factor;  /* Character size of scale label 
                                             relative to the current font */ 
    double     view_scale_text_factor;    /* Character size of scale value 
                                             relative to the current font */ 
    logical    view_label;                /* TRUE - include view label; 
                                             FALSE - do not include view label 
                                          */ 
    logical    scale_label;               /* TRUE - include scale label; 
                                             FALSE - do not include scale label
                                          */
    logical    view_label_customize;       /* TRUE - turn on customized toggle
                                              FALSE - turn off customized toggle
                                           */ 
    logical    scale_parentheses;         /* TRUE - include parentheses around scale; 
                                             FALSE - do not include parentheses around scale;
                                          */ 
    char       view_label_prefix[UF_DRAW_MAX_LABEL_LEN];     
                                         /* View label prefix string */ 
    char       scale_label_prefix[UF_DRAW_MAX_LABEL_LEN];    
                                         /* Scale label prefix string */ 
    char       view_letter[UF_DRAW_MAX_LETTER_BUFSIZE];          
                                         /* View letter string */ 
    UF_DRAW_label_on_parent_type_t        parent_label_type;
                                         /* label on parent of detail view type */
    double     text_to_gap_factor;       /* Defines how big the gap will be for embedded
                                            label on parent types */
    char       parent_vw_lbl_prefix[UF_DRAW_MAX_LABEL_LEN];
                                         /* Parent view label prefix string */

    logical show_rotation_symbol;       /* Show rotation symbol */
    logical show_rotation_angle;        /* Show rotation angle */

    UF_DRAW_secondary_indexing_align_t secondary_indexing_align;    /* Secondary indexing alignment */
    double subscript_size_factor;        /* Subscript size factor */
};
typedef struct UF_DRAW_view_label_parms_s 
               UF_DRAW_view_label_parms_t, *UF_DRAW_view_label_parms_p_t;

#ifdef __cplusplus
}
#endif

#endif /* UF_DRAW_TYPES_INCLUDED */
