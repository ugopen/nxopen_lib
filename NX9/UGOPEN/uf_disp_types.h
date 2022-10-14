/*****************************************************************************

        Copyright 2004 Siemens Product Lifecycle Management Software Inc. 
                       Unpublished - All Rights Reserved

****************************************************************************




File Description :

This include file contains the prototypes and descriptions of the display
functions.  The functions include temporary display, color table access and
model bounds access.

In addition, this file contains the prototypes for the public functions in the
UF_DISP module.  This module is to be used to display UDO geometry. These
functions should be called from the user program.  The user program can be
registered with the display, selection, fit and attention point callbacks.

This provides routines for:

Coneheads -  describes the functions that enable you to display coneheads and
             objects. The coneheads section describes the C include files, data
             structures, and C functions available to you which enable you to
             temporarily display coneheads, and get and set conehead attributes.

Features and Dimensions - describes the functions that enable you to display
                          sketch and rpo dimensions.

Batch Shade - describes the batch shade function.

Color Table Access - describes the functions that enable you to read and modify
                     colors or the value of any color.

Model Bounds - are functions that enable you to query model bounds.

Name Display - are functions that enable you to set/query the name view status
               or the name display status.

Object Display - are routines that enable you to display temporary graphics
                 objects, regenerate the display, and display objects.

Overlay Graphics Primitives - are routines to render geometry using Overlay
                              Graphics Primitives (OGP).  These functions are
                              intended to be used exclusively from motion
                              callbacks. Please see the discussion and example
                              provided with UF_UI_specify_screen_position. Note
                              that these functions do not create NX
                              objects, and the geometry they define is not
                              associated with any existing objects.

Overlay Graphics primitives give the appearance of being drawn on a transparent
 overlay. That is, they are displayed on top of any previously displayed
geometry, and when they are erased, the display of the underlying geometry is
not affected.  Overlay Graphics primitives are drawn in the same color as the
crosshair:  either white or black, whichever will contrast better with
the current background color.

Because of the method used internally to render Overlay Graphics primitives,
on most workstation configurations, when a portion of one primitive overlaps
another primitive, the overlapping portion will not display at all. Visually,
it is as if they cancel each other out.  Therefore, in the course of defining
the primitives, care should be taken to avoid overlapping geometry.

User Defined Object Display - are routines that display, fit, and perform
attention point/selection computations.  Each routine is overloaded with these
operations.  The overloading of multiple functions allows you to call the
routine once from a NX Open API program.  You can control which operation the
routine participates in by selectively registering a NX Open API program using
the registration methods in uf_udobj.h.

Work Plane Emphasis is a mode where all objects that are not on the work plane
are dimmed through a color change.  These de-emphasized objects are filtered
out of selection operations.

The work plane emphasis set consists of points, lines, arcs, conics splines,
planes datum planes, datum axes, coordinate systems (except the WCS and GFEM
coordinate systems), and edges.  This option also employs an exclusion object
set, which consists of those objects not affected by work plane emphasis.  The
exclusion object set consists of sketcher datums and degree of freedom
indicators, the WCS, and the Grid.

***************************************************************************/

#ifndef UF_DISP_TYPES_INCLUDED
#define UF_DISP_TYPES_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_cfi_types.h>


#ifdef __cplusplus
extern "C" {
#endif

#define ERROR_UF_DISP_base     1390000

/* Color models supported by the UF_DISP color functions */
/* Use zero based numbers to match "C" enums */

#define UF_DISP_rgb_model  0
#define UF_DISP_hsv_model  1
#define UF_DISP_hls_model  2

/* Color Comparison Methods (CCMs), for determining the "closest" color to a
 * given color.
 */
#define UF_DISP_CCM_EUCLIDEAN_DISTANCE  1

/* Index of the background color in the Color Table Object
 */
#define UF_DISP_BACKGROUND_COLOR  0

/* Maximum length for color names
 */
#define UF_DISP_MAX_NAME_SIZE     32   /* Excluding terminator ('\0') */

/***************************************************************************
 * Constants for view options. Some options may not be available
 * for some functions.
  ***************************************************************************/
#define  UF_DISP_ALL_ACTIVE_MEMBER_VIEWS   (-4)
#define  UF_DISP_ALL_VIEWS_BUT_DRAWING     (-3)
#define  UF_DISP_VIEW_OF_LAST_CURSOR       (-2)
#define  UF_DISP_ALL_ACTIVE_VIEWS          (-1)
#define  UF_DISP_WORK_VIEW_ONLY              0

/***************************************************************************
 * Constants for UF_DISP_set_display
  ***************************************************************************/

#define UF_DISP_SUPPRESS_DISPLAY   (0)
#define UF_DISP_UNSUPPRESS_DISPLAY (1)

/***************************************************************************
 * Constants for color options. Some options may not be available
 * for some functions.
  ***************************************************************************/
#define  UF_DISP_USE_SPECIFIED_COLOR   (-3)
#define  UF_DISP_USE_ORIGINAL_COLOR    (-2)
#define  UF_DISP_USE_BACKGROUND_COLOR  (-1)
#define  UF_DISP_USE_SYSTEM_COLOR        0

/***************************************************************************
 * Constants for name display options.
  ***************************************************************************/
#define  UF_DISP_NAME_DISPLAY_OFF        0
#define  UF_DISP_NAME_DISPLAY_ON         1
#define  UF_DISP_NAMES_IN_WORK_VIEW      0
#define  UF_DISP_NAMES_IN_VIEW_OF_DEFN   1
#define  UF_DISP_NAMES_IN_ALL_VIEWS      2     /*all views except drawing member views*/

/***************************************************************************
* Symbolic constants used by surface analysis functions
* The four types of analysis display (with range constants)
  ***************************************************************************/
#define UF_DISP_SRFANL_DISPLAY_TYPE_MIN 0
#define UF_DISP_FRINGE                  0
#define UF_DISP_HEDGEHOG                1
#define UF_DISP_REFL_LINES              2
#define UF_DISP_CONTOUR_LINES           3
#define UF_DISP_SRFANL_DISPLAY_TYPE_MAX 3

/* The ten scalar functions that can be displayed (with range constants) */
#define UF_DISP_SRFANL_SCALAR_FUNC_MIN 0
#define UF_DISP_GAUSSIAN_CURVATURE     0
#define UF_DISP_MEAN_CURVATURE         1
#define UF_DISP_MINIMUM_CURVATURE      2
#define UF_DISP_MAXIMUM_CURVATURE      3
#define UF_DISP_NORMAL_CURVATURE       4
#define UF_DISP_SECTIONAL_CURVATURE    5
#define UF_DISP_SLOPE                  6
#define UF_DISP_DISTANCE               7
#define UF_DISP_U_CURVATURE            8
#define UF_DISP_V_CURVATURE            9
#define UF_DISP_REFLECTION             10
#define UF_DISP_FACET_COLORMAP         11    
#define UF_DISP_SRFANL_SCALAR_FUNC_MAX 11

/* The four different values of 'fineness' (with range constants) */
#define UF_DISP_SRFANL_FINENESS_MIN 0
#define UF_DISP_STANDARD            0
#define UF_DISP_FINE                1
#define UF_DISP_EXTRA_FINE          2
#define UF_DISP_ULTRA_FINE          3
#define UF_DISP_SRFANL_FINENESS_MAX 3

/* The display option BLEND/SHARP */
#define UF_DISP_SRFANL_DISTYPE_OPTION_MIN  0
#define UF_DISP_SRFANL_BLEND               0
#define UF_DISP_SRFANL_SHARP               1
#define UF_DISP_SRFANL_DISTYPE_OPTION_MAX  1

/* The number of color options(3,5,7) */
#define UF_DISP_SRFANL_DISCOLOR_OPTION_MIN  0
#define UF_DISP_SRFANL_DISCOLOR_3           0
#define UF_DISP_SRFANL_DISCOLOR_5           1
#define UF_DISP_SRFANL_DISCOLOR_7           2
#define UF_DISP_SRFANL_DISCOLOR_OPTION_MAX  2

/* the new shaded tolerance fineness */
#define UF_DISP_SHADED_FINENESS_MIN 0
#define UF_DISP_SHADED_COARSE              0
#define UF_DISP_SHADED_STANDARD            1
#define UF_DISP_SHADED_FINE                2
#define UF_DISP_SHADED_EXTRA_FINE          3
#define UF_DISP_SHADED_ULTRA_FINE          4
#define UF_DISP_SHADED_CUSTOMIZE_TOL       5
#define UF_DISP_SHADED_FINENESS_MAX        5

/* Surface reflection types */
#define UF_DISP_REFL_TYPE_BLACKLINES          0
#define UF_DISP_REFL_TYPE_BLKWHTLINES         1
#define UF_DISP_REFL_TYPE_COLOREDLINES        2
#define UF_DISP_REFL_TYPE_SIMHORIZON          3
#define UF_DISP_REFL_TYPE_PHOTOHORIZON        4
#define UF_DISP_REFL_TYPE_SPHEREROOM          5
#define UF_DISP_REFL_TYPE_SCENE1              6
#define UF_DISP_REFL_TYPE_SCENE2              7
#define UF_DISP_REFL_TYPE_SCENE3              8
#define UF_DISP_REFL_TYPE_SCENE4              9
#define UF_DISP_REFL_TYPE_SCENE5             10
#define UF_DISP_REFL_TYPE_SCENE6             11
#define UF_DISP_REFL_TYPE_SCENE7             12
#define UF_DISP_REFL_TYPE_SCENE8             13
#define UF_DISP_REFL_TYPE_SCENE9             14
#define UF_DISP_REFL_TYPE_USERIMAGE          15

/* The three thicknesses of reflection lines */
#define UF_DISP_REFL_THIN               0
#define UF_DISP_REFL_MEDIUM             1
#define UF_DISP_REFL_THICK              2

/* Whether to display horizontal, vertical, or all reflection lines
 * (includes range constants) */
#define UF_DISP_REFL_LINE_STYLE_MIN 0
#define UF_DISP_REFL_HORIZ          0
#define UF_DISP_REFL_VERT           1
#define UF_DISP_REFL_HORIZ_AND_VERT 2
#define UF_DISP_REFL_LINE_STYLE_MAX 2

/* Surface reflectivity (or blending) factor limits */
#define UF_DISP_REFL_REFLECTIVITY_MAX 100
#define UF_DISP_REFL_REFLECTIVITY_MIN   0

/* Reflection movement types */
#define UF_DISP_REFL_TRANSLATE_HORIZ 0
#define UF_DISP_REFL_TRANSLATE_VERT  1
#define UF_DISP_REFL_ROTATE          2

/* Reflection movement limits */
#define UF_DISP_REFL_TRANSLATE_MAX     128
#define UF_DISP_REFL_TRANSLATE_MIN   (-128)
#define UF_DISP_REFL_ROTATE_ANGLE_MAX   90
#define UF_DISP_REFL_ROTATE_ANGLE_MIN (-90)

/* maximum number of contour and reflection lines */
#define UF_DISP_MAX_CONTOUR_LINES 32
#define UF_DISP_MAX_REFLECTION_LINES 256

/***************************************************************************
* First argument to UF_DISP_export_windows_metafile
  ***************************************************************************/
enum UF_DISP_wmf_output_e
{
    UF_DISP_WMF_TO_CLIPBOARD,
    UF_DISP_WMF_TO_FILE
};

typedef enum UF_DISP_wmf_output_e UF_DISP_wmf_output_t;

/***************************************************************************
 * Constants for work plane emphasis options.
  ***************************************************************************/
#define UF_DISP_WORK_PLANE_EMPHASIS_ON  (1)
#define UF_DISP_WORK_PLANE_EMPHASIS_OFF (0)
#define UF_DISP_SELECT_WORK_DIMMED      (1)
#define UF_DISP_NO_SELECT_WORK_DIMMED   (0)

/***************************************************************************
 * Constants for error codes
  ***************************************************************************/

/* A specified tag on the expression list does not relate to a dimension */
#define UF_DISP_err_invalid_expression            (ERROR_UF_DISP_base + 0)

/* The specified object tag is not in work part */
#define UF_DISP_err_object_not_in_work_part       (ERROR_UF_DISP_base + 1)

/* The arc or circle has a radius less than the system tolerance */
#define UF_DISP_err_radius_less_than_systol       (ERROR_UF_DISP_base + 2)

/* The arc's end angle is less than or equal to the start angle */
#define UF_DISP_err_end_ang_lt_start_ang          (ERROR_UF_DISP_base + 3)

/* The arc's start and end angles differ by more than TWOPI */
#define UF_DISP_err_angle_delta_gt_2pi            (ERROR_UF_DISP_base + 4)

/* The hardware configuration does not support the requested analysis mode */
#define UF_DISP_err_reflection_lines_unsupported  (ERROR_UF_DISP_base + 5)
#define UF_DISP_err_contour_lines_unsupported     (ERROR_UF_DISP_base + 6)

#define UF_DISP_err_failed_to_create_image_file   (ERROR_UF_DISP_base + 7)

/* An attention point could not be computed for an object */
#define UF_DISP_err_could_not_compute_attention_point (ERROR_UF_DISP_base + 8)

/***************************************************************************
    Structure definition for system display parameters

    With V12, light settings become view attributes and are no longer
    specified in the UF_DISP_system_params_t structure.  Light settings
    can now be accessed through functions UF_VIEW_ask_view_light and
    UF_VIEW_set_view_light declared in uf_view.h.

  ***************************************************************************/

/***************************************************************************
    The hidden_shaded_face_edges field of the UF_DISP_system_params_t
    structure can be set to a color index or to one of the following
    symbols.
  ***************************************************************************/

#define UF_DISP_INVISIBLE_HIDDEN_FACE_EDGES    -2
#define UF_DISP_DASHED_HIDDEN_FACE_EDGES       -1

/* System display parameters.

Structure fields show_shaded_face_edges, use_face_edges_color,
face_edges_color, and hidden_shaded_face_edges are now represented
by view options. See
 UF_VIEW_ask_shaded_edge_options
and
 UF_VIEW_set_shaded_edge_options
.
*/
struct UF_DISP_system_params_s
{
    double  tolerance;                 /* Curve and surface tolerance         */
    double  dash_size;                 /*  Dash size if font = 1              */
    double  space_size;                /* Space size if font = 1              */
    double  symbol_size;               /* symbol size in line font            */
    double  facet_edge_tol;            /* This is the facet edge tolerance for
                                          shaded display.  This is an upper
                                          bound on the distance from each
                                          chord to the curve it is approximating
                                          The recommend value is .005.  Smaller
                                          values result in finer display but
                                          causes degraded performance.  A
                                          value of .01 would give a coarse
                                          display, .0005 would give an extra
                                          fine display.

                                       */
    double  facet_chord_tol;           /* This is the facet chord distance
                                          for shaded display.  This is an upper
                                          bound on the distance from a
                                          positions on a facet to the surface.
                                          The recommended value is .005.  A
                                          smaller value results in a finer
                                          display but causes degraded
                                          performance. A value of .01 would
                                          give a coarse display, .0025 would
                                          give a fine display, .001 an extra
                                          fine display and .0005 an ultra
                                          fine display.

                                       */

    double  facet_angle_tol;           /* This is the facet angle tolerance
                                          for shaded display.  This is an
                                          upper bound on the angular
                                          deviation between the surface normals
                                          at any two positions under the facet.
                                          The recommended value is 15 degrees.
                                          A smaller value results in a finer
                                          display, but causes slower
                                          performance. A coarse display would
                                          use a tolerance of 0.0, 15.0 gives
                                          the standard angle, a value of 6.0
                                          would give an extra fine display,
                                          and a value of 3.0 an ultra fine
                                          display.

                                          */
    int     color;                     /* system display color */
    int     preselection_color;        /* Preselection color.  Note that this is the general
                                          preselection color, and should not be confused with
                                          the one use for monochrome drawings (see
                                          UF_DISP_ask_drawing_display().*/

    int     handle_color;              /* Handle color */

    int     font;                      /* system font mode
                                            1 = software line fonts
                                            2 = hardware line fonts  */
    int     view_display;              /* view names and borders display
                                            1 = ON, 2 = OFF   */
    int     line_width_display;        /* line width display mode
                                            1 = yes, 2 = no        */

    logical show_shaded_face_edges;    /* Specifies whether or not edges are
                                          displayed for shaded and analysis
                                          faces of solid and sheet bodies. If
                                          TRUE, shaded face edges are displayed
                                          as specified by the use_face_edges_-
                                          color field and the face_edges_color
                                          field. If FALSE, shaded face edges
                                          are not displayed. */

    logical use_face_edges_color;      /* Significant only if the show_shaded_-
                                          face_edges field is TRUE. If TRUE,
                                          shaded face edges are displayed in
                                          the color specified by the face_-
                                          edges_color field. If FALSE, face
                                          edges are displayed in the body
                                          color. */

    int     face_edges_color;          /* Significant only if both the show_-
                                          shaded_face_edges field and the
                                          use_face_edges_color field are TRUE.
                                          Specifies the non-negative index of
                                          the color used to display shaded
                                          face edges. */

    int     hidden_shaded_face_edges;  /* Controls the appearance of hidden
                                          edges for shaded and analysis faces
                                          of solid and sheet bodies. If set to
                                          UF_DISP_INVISIBLE_HIDDEN_FACE_EDGES,
                                          hidden shaded face edges are not
                                          displayed. If set to UF_DISP_DASHED_-
                                          HIDDEN_FACE_EDGES, hidden shaded face
                                          edges are displayed like visible
                                          shaded face edges but with dashed
                                          line font. If set to a non-negative
                                          color index, hidden shaded face edges
                                          are displayed in this color, and the
                                          color is also used to display other
                                          hidden geometry where the geometry
                                          shows through shaded or analysis
                                          geometry. */

    int     hidden_geometry_color;     /* Significant only if the hidden_-
                                          shaded_face_edges field is not set
                                          to a color index. Specifies the non-
                                          negative index of the color used to
                                          display hidden geometry where the
                                          geometry shows through shaded or
                                          analysis geometry. */

    logical random_color_displayed;    /* Are random colors displayed for the
                                          part?  If TRUE, random colors are
                                          displayed on the random color object
                                          type in the displayed part.  If
                                          FALSE, normal object colors are used.
                                                                             */
    int     random_color_object_type;  /* Set to the type of objects on which
                                          random colors will be displayed.
                                          Valid values are found in
                                          UF_DISP_random_color_object_e      */
};

typedef         struct UF_DISP_system_params_s  UF_DISP_system_params_t,
                                               *UF_DISP_system_params_p_t;
typedef const   struct UF_DISP_system_params_s  UF_DISP_system_params_c_t;

/* This is used to determine the type of shade to produce.  The first three
   methods (UF_DISP_flat, UF_DISP_gouraud, and UF_DISP_phong) only need a
   gateway license to work correctly.  If UF_DISP_high_quality, UF_DISP_preview,
   UF_DISP_photo_real or UF_DISP_raytrace are used than a Studio Render license
   is needed.  If this license is not available then the shade method will
   default back to UF_DISP_phong.
*/
enum UF_DISP_shade_method_e
{
    UF_DISP_flat,
    UF_DISP_gouraud,
    UF_DISP_phong,
    UF_DISP_high_quality,
    UF_DISP_preview,
    UF_DISP_photo_real,
    UF_DISP_raytrace
};

typedef enum UF_DISP_shade_method_e UF_DISP_shade_method_t;

enum UF_DISP_random_color_object_e
{
    UF_DISP_RANDOM_FACE_COLOR,
    UF_DISP_RANDOM_BODY_COLOR
};

/*
    Parameters that control the monochrome display of drawings.
    The color settings are in effect only when monochrome display is TRUE.
*/
struct UF_DISP_drawing_display_data_s {
    logical monochrome_display;  /* monochrome or full color display of drawings */
    int system_color;            /* system color for monochrome display of drawings */
    int preselection_color;      /* preselection color for monochrome display of drawings */
    int foreground_color;        /* foreground color for monochrome display of drawings */
    int background_color;        /* background color for monochrome display of drawings */
    logical show_widths;         /* line width display for monochrome display of drawings */
};

typedef struct UF_DISP_drawing_display_data_s UF_DISP_drawing_display_data_t,
                                              *UF_DISP_drawing_display_data_p_t;

/*
    Structure definition for face analysis display parameters. These
    parameters affect the display of all faces whose "face analysis"
    attribute is TRUE, in all "face analysis" views. Each of
    these parameters, is settable by the NX user using the
    "face analysis" dialog. The data_range for different analysis type
    is automatically calculated.
*/
struct UF_DISP_srfanl_data_s {
    double spike_length;   /* spike length for a hedgehog display */
    double ref_plane[6];   /* reference plane, point on a plane & normal. Used
                              for 'sectional radius' and 'distance' display. */
    double ref_vector[3];  /* reference vector, used for 'normal radius' and 'slope' display */
    double mid_value;      /* mid value of the scalar function data range for GAUSSIAN type */
    double scale_factor;   /* scale factor applied to the data range
                              The range of the scalar function in all
                              'face analysis' faces in the NX part is called
                              the 'data-range'.  Some portion of this range
                              is mapped to displayed colors (from red through
                              green to blue). This mapped range is centered
                              at 'mid_value' and has size equal to the size of
                              the data_range times the 'scale_factor'. The
                              'mid_value' and 'scale_factor' are directly
                              controllable by the NX user, using sliders on
                              the 'face analysis' dialog.
                              This is only for  GAUSSIAN type */
    double anal_facet_edge_tol;     /* This is the facet edge tolerance for
                                       shaded display.  This value is ignored
                                       unless the surf_anal_fineness member
                                       is set to UF_DISP_SHADED_CUSTOMIZE_TOL.
                                       This is an upper
                                       bound on the distance from each
                                       chord to the curve it is approximating
                                       The recommend value is .005 inch.Smaller
                                       values result in finer display but
                                       causes degraded performance.  A
                                       value of .01 would give a coarse
                                       display, .0005 would give an extra
                                       fine display but also causes slower
                                       performance.

                                    */
    double anal_facet_chord_tol;    /* This is the facet chord distance
                                       for shaded display. This value is ignored
                                       unless the surf_anal_fineness member
                                       is set to UF_DISP_SHADED_CUSTOMIZE_TOL.
                                       This is an upper
                                       bound on the distance from a
                                       positions on a facet to the surface.
                                       The recommended value is .005 inch.  A
                                       smaller value results in a finer
                                       display but causes degraded
                                       performance. A value of .01 would
                                       give a coarse display, .0025 would
                                       give a fine display, .001 an extra
                                       fine display and .0005 an ultra
                                       fine display.

                                    */
    double anal_facet_angle_tol;    /* This is the facet angle tolerance
                                       for shaded display. This value is ignored
                                       unless the surf_anal_fineness member
                                       is set to UF_DISP_SHADED_CUSTOMIZE_TOL.
                                       This is an upper bound on the angular
                                       deviation between the surface normals
                                       at any two positions under the facet.
                                       The recommended value is 15 degrees.
                                       A smaller value results in a finer
                                       display, but causes slower
                                       performance. A coarse display would
                                       use a tolerance of 0.0, 15.0 gives
                                       the standard angle, a value of 6.0
                                       would give an extra fine display,
                                       and a value of 3.0 an ultra fine
                                       display.

                                    */
    double anal_facet_width_tol; /* Facet width tolerance for analysis
                                    display. This value is ignored
                                    unless the surf_anal_fineness member
                                    is set to UF_DISP_SHADED_CUSTOMIZE_TOL.
                                    This value specifies the
                                    maximum width of a facet.  The
                                    recommended value is .3.  A smaller
                                    tolerance value causes a finer display
                                    but also causes slower performance. A
                                    value of .075 would give a fine display,
                                    .02 an extra fine display, and .005
                                    an ultra fine display.

                                 */
    int surf_anal_data;     /* one of the 11 scalar functions to display
                               UF_DISP_GAUSSIAN_CURVATURE
                               UF_DISP_MEAN_CURVATURE
                               UF_DISP_MINIMUM_CURVATURE
                               UF_DISP_MAXIMUM_CURVATURE
                               UF_DISP_NORMAL_CURVATURE
                               UF_DISP_SECTIONAL_CURVATURE
                               UF_DISP_SLOPE
                               UF_DISP_DISTANCE
                               UF_DISP_U_CURVATURE
                               UF_DISP_V_CURVATURE
                               UF_DISP_REFLECTION */
    int surf_anal_fineness; /* one of the 6 values of 'fineness'
                               UF_DISP_SHADED_COARSE
                               UF_DISP_SHADED_STANDARD
                               UF_DISP_SHADED_FINE
                               UF_DISP_SHADED_EXTRA_FINE
                               UF_DISP_SHADED_ULTRA_FINE
                               UF_DISP_SHADED_CUSTOMIZE_TOL
 
                               */
    int refl_type;          /* reflection type values are:
                               UF_DISP_REFL_TYPE_BLACKLINES
                               UF_DISP_REFL_TYPE_BLKWHTLINES
                               UF_DISP_REFL_TYPE_COLOREDLINES
                               UF_DISP_REFL_TYPE_SIMHORIZON
                               UF_DISP_REFL_TYPE_PHOTOHORIZON
                               UF_DISP_REFL_TYPE_USERIMAGE */
    int num_refl_lines;     /* The number of reflection lines. Must be a
                               power of 2 between 2 and
                               UF_DISP_MAX_REFLECTION_LINES */
    int refl_horiz_vert;    /* Determines whether to display horizontal,
                               vertical, or all reflection lines values are:
                               UF_DISP_REFL_HORIZ
                               UF_DISP_REFL_VERT
                               UF_DISP_REFL_HORIZ_AND_VERT */
    int thick_refl_lines;   /* One of 3 thicknesses of reflection lines
                               UF_DISP_REFL_THIN
                               UF_DISP_REFL_MEDIUM
                               UF_DISP_REFL_THICK */
    int reflectivity;       /* surface reflectivity (blending) factor.
                               Must be a value between
                               UF_DISP_REFL_REFLECTIVITY_MIN which results
                               in no reflection and
                               UF_DISP_REFL_REFLECTIVITY_MAX, which is the
                               default, where the surface is absolutely
                               reflective. */
    int refl_move_type;     /* reflection movement type.  To use, set it to
                               one of the following types:
                               UF_DISP_REFL_TRANSLATE_HORIZ
                               UF_DISP_REFL_TRANSLATE_VERT
                               UF_DISP_REFL_ROTATE  */
    int refl_move_position; /* reflection translation or rotation factor.
                               This is used when the reflection movement
                               type has been set.  Must be a value between
                               UF_DISP_REFL_TRANSLATE_MIN and
                               UF_DISP_REFL_TRANSLATE_MAX when refl_move_type
                               is set to translate or between
                               UF_DISP_REFL_ROTATE_ANGLE_MIN and
                               UF_DISP_REFL_ROTATE_ANGLE_MAX when refl_move_type
                               is set to rotate. */
    int refl_smooth_lines;  /* Determines whether reflection lines should be
                               anti-aliased.  Must be set to TRUE, the
                               default or FALSE.  Effects both
                               UF_DISP_REFL_TYPE_BLACKLINES,
                               UF_DISP_REFL_TYPE_BLKWHTLINES and
                               UF_DISP_REFL_TYPE_COLOREDLINES */

    char refl_user_image_filename[ MAX_FSPEC_BUFSIZE ];
                           /* Stores user specified reflection image file name.
                              Effects UF_DISP_REFL_TYPE_USERIMAGE */

    int num_contours;       /* Determines the number of displayed contour
                               lines, between 2 and UF_DISP_MAX_CONTOUR_LINES*/
    int surf_anal_display;  /* The type of face analysis display for GAUSSIAN:
                                UF_DISP_FRINGE
                                UF_DISP_HEDGEHOG
                                UF_DISP_CONTOUR_LINES */

    int    legend_color_type_gaussian; /* This is blend/sharp type for GAUSSIAN type */
    int    legend_color_num_gaussian;  /* This is number of color option for GAUSSIAN type */

    int    surf_anal_display_mean; /* The type of face analysis display for MEAN:
                                      UF_DISP_FRINGE
                                      UF_DISP_HEDGEHOG
                                      UF_DISP_CONTOUR_LINES */
    double mid_value_mean;         /* mid value of the scalar function data range for MEAN type */
    double scale_factor_mean;      /* scale factor applied to the data range for MEAN */
    int    legend_color_type_mean; /* This is blend/sharp type for MEAN type */
    int    legend_color_num_mean;  /* This is number of color option for MEAN type */

    int    surf_anal_display_max;  /* The type of face analysis display for MAX:
                                      UF_DISP_FRINGE
                                      UF_DISP_HEDGEHOG
                                      UF_DISP_CONTOUR_LINES */
    double mid_value_max;          /* mid value of the scalar function data range for MAX type */
    double scale_factor_max;       /* scale factor applied to the data range for MAX type */
    int    legend_color_type_max;  /* This is blend/sharp type for MAX type */
    int    legend_color_num_max;   /* This is number of color option for MAX type */

    int    surf_anal_display_min;  /* The type of face analysis display for MIN:
                                      UF_DISP_FRINGE
                                      UF_DISP_HEDGEHOG
                                      UF_DISP_CONTOUR_LINES */
    double mid_value_min;          /* mid value of the scalar function data range for MIN type */
    double scale_factor_min;       /* scale factor applied to the data range for MIN type */
    int    legend_color_type_min;  /* This is blend/sharp type for MIN type */
    int    legend_color_num_min;   /* This is number of color option for MIN type */


    int    surf_anal_display_normal;/* The type of face analysis display for NORMAL:
                                       UF_DISP_FRINGE
                                       UF_DISP_HEDGEHOG
                                       UF_DISP_CONTOUR_LINES */
    double mid_value_normal;        /* mid value of the scalar function data range for NORMAL type */
    double scale_factor_normal;     /* scale factor applied to the data range for NORMAL type */
    int    legend_color_type_normal;/* This is blend/sharp type for NORMAL type */
    int    legend_color_num_normal; /* This is number of color option for NORMAL type */

    int    surf_anal_display_sec;   /* The type of face analysis display for SECTIONAL:
                                       UF_DISP_FRINGE
                                       UF_DISP_HEDGEHOG
                                       UF_DISP_CONTOUR_LINES */
    double mid_value_sec;           /* mid value of the scalar function data range for SECTIONAL type */
    double scale_factor_sec;        /* scale factor applied to the data range for SECTIONAL type */
    int    legend_color_type_sec;   /* This is blend/sharp type for SECTIONAL type */
    int    legend_color_num_sec;    /* This is number of color option for SECTIONAL type */

    int    surf_anal_display_u;     /* The type of face analysis display for U:
                                       UF_DISP_FRINGE
                                       UF_DISP_HEDGEHOG
                                       UF_DISP_CONTOUR_LINES */
    double mid_value_u;             /* mid value of the scalar function data range for U type */
    double scale_factor_u;          /* scale factor applied to the data range for U */
    int    legend_color_type_u;     /* This is blend/sharp type for U type */
    int    legend_color_num_u;      /* This is number of color option for U type */

    int    surf_anal_display_v;     /* The type of face analysis display for V:
                                       UF_DISP_FRINGE
                                       UF_DISP_HEDGEHOG
                                       UF_DISP_CONTOUR_LINES */
    double mid_value_v;             /* mid value of the scalar function data range for V type */
    double scale_factor_v;          /* scale factor applied to the data range for V type */
    int    legend_color_type_v;     /* This is blend/sharp type for V type */
    int    legend_color_num_v;      /* This is number of color option for V type */

    int    surf_anal_display_slope; /* The type of face analysis display for SLOPE:
                                       UF_DISP_FRINGE
                                       UF_DISP_HEDGEHOG
                                       UF_DISP_CONTOUR_LINES */
    double mid_value_slope;         /* mid value of the scalar function data range for SLOPE type */
    double scale_factor_slope;      /* scale factor applied to the data range for SLOPE */
    int    legend_color_type_slope; /* This is blend/sharp type for SLOPE type */
    int    legend_color_num_slope;  /* This is number of color option for SLOPE type */

    int    surf_anal_display_distance;/* The type of face analysis display for DISTANCE:
                                         UF_DISP_FRINGE
                                         UF_DISP_HEDGEHOG
                                         UF_DISP_CONTOUR_LINES */
    double mid_value_distance;        /* mid value of the scalar function data range for DISTANCE type */
    double scale_factor_distance;     /* scale factor applied to the data range for DISTANCE */
    int    legend_color_type_distance;/* This is blend/sharp type for DISTANCE type */
    int    legend_color_num_distance; /* This is number of color option for DISTANCE type */

    int    surf_anal_display_refl;    /* This is the reflection display UF_DISP_REFL_LINES */

};

typedef struct UF_DISP_srfanl_data_s UF_DISP_srfanl_data_t;

struct UF_DISP_j3d_entity_s {
  tag_t             eid; /* NX identifier for this shape */
  int               vectors; /* flag for vector data - if true then vectors else triangles */
  int               has_transform; /* true if an assembly transform is used */
  double            transform[4][4]; /* assembly transform */
  double           *point_list; /* list of points in groups of 3 for x,y,z */
  double           *normal_list; /* list of normals in groups of 3 for each point ( triangles
only ) */
  int              *points_per_strip; /* number of points in each tri strip */
  int               num_strips; /* number of triangle strips */
  int               total_points; /* total number of points in the point_list */
  int               sheet; /* true if this is a sheet body ( need bi-directional normals ) */
  double            color[3]; /* RGB color from 0.0 to 1.0 for red, green, blue */
  char             *name; /* entity name (if one is found) */
};
typedef struct UF_DISP_j3d_entity_s
               UF_DISP_j3d_entity_t, *UF_DISP_j3d_entity_p_t;


/****************************************************************************
 *
 *  ENUMERATED:  UF_DISP_color_name_t
 *
 *  DESCRIPTION: Symbols of type UF_DISP_color_name_t represent color
 *               names that can be specified ONLY to function
 *               UF_DISP_ask_closest_color_in_part or function
 *               UF_DISP_ask_closest_color_in_displayed_part. The
 *               functions return the index of the color in the color
 *               table of the specified part that is most similar to
 *               the color indicated by the color name symbol.
 *
 *               These symbols DO NOT represent color indices. Do not
 *               pass these symbols to any function besides
 *               UF_DISP_ask_closest_color_in_part or
 *               UF_DISP_ask_closest_color_in_displayed_part.
 *
 ****************************************************************************/

enum UF_DISP_color_name_e
{
    UF_DISP_PALE_WEAK_YELLOW_NAME,        /* RGB (1.0, 1.0, 0.8) */
    UF_DISP_PALE_DULL_YELLOW_NAME,        /* RGB (1.0, 1.0, 0.6) */
    UF_DISP_LIGHT_FADED_YELLOW_NAME,      /* RGB (1.0, 1.0, 0.4) */
    UF_DISP_LIGHT_HARD_YELLOW_NAME,       /* RGB (1.0, 1.0, 0.2) */
    UF_DISP_PALE_WEAK_CYAN_NAME,          /* RGB (0.8, 1.0, 1.0) */
    UF_DISP_PALE_WEAK_GREEN_NAME,         /* RGB (0.8, 1.0, 0.8) */
    UF_DISP_PALE_DULL_SPRING_NAME,        /* RGB (0.8, 1.0, 0.6) */
    UF_DISP_LIGHT_SPRING_YELLOW_NAME,     /* RGB (0.8, 1.0, 0.4) */
    UF_DISP_LIGHT_YELLOW_SPRING_NAME,     /* RGB (0.8, 1.0, 0.2) */
    UF_DISP_YELLOW_YELLOW_SPRING_NAME,    /* RGB (0.8, 1.0, 0.0) */
    UF_DISP_PALE_DULL_CYAN_NAME,          /* RGB (0.6, 1.0, 1.0) */
    UF_DISP_PALE_DULL_TEAL_NAME,          /* RGB (0.6, 1.0, 0.8) */
    UF_DISP_PALE_DULL_GREEN_NAME,         /* RGB (0.6, 1.0, 0.6) */
    UF_DISP_LIGHT_SPRING_GREEN_NAME,      /* RGB (0.6, 1.0, 0.4) */
    UF_DISP_LIGHT_HARD_SPRING_NAME,       /* RGB (0.6, 1.0, 0.2) */
    UF_DISP_SPRING_SPRING_YELLOW_NAME,    /* RGB (0.6, 1.0, 0.0) */
    UF_DISP_LIGHT_FADED_CYAN_NAME,        /* RGB (0.4, 1.0, 1.0) */
    UF_DISP_LIGHT_TEAL_CYAN_NAME,         /* RGB (0.4, 1.0, 0.8) */
    UF_DISP_LIGHT_TEAL_GREEN_NAME,        /* RGB (0.4, 1.0, 0.6) */
    UF_DISP_LIGHT_FADED_GREEN_NAME,       /* RGB (0.4, 1.0, 0.4) */
    UF_DISP_LIGHT_GREEN_SPRING_NAME,      /* RGB (0.4, 1.0, 0.2) */
    UF_DISP_SPRING_SPRING_GREEN_NAME,     /* RGB (0.4, 1.0, 0.0) */
    UF_DISP_LIGHT_HARD_CYAN_NAME,         /* RGB (0.2, 1.0, 1.0) */
    UF_DISP_LIGHT_CYAN_TEAL_NAME,         /* RGB (0.2, 1.0, 0.8) */
    UF_DISP_LIGHT_HARD_TEAL_NAME,         /* RGB (0.2, 1.0, 0.6) */
    UF_DISP_LIGHT_GREEN_TEAL_NAME,        /* RGB (0.2, 1.0, 0.4) */
    UF_DISP_LIGHT_HARD_GREEN_NAME,        /* RGB (0.2, 1.0, 0.2) */
    UF_DISP_GREEN_GREEN_SPRING_NAME,      /* RGB (0.2, 1.0, 0.0) */
    UF_DISP_CYAN_CYAN_TEAL_NAME,          /* RGB (0.0, 1.0, 0.8) */
    UF_DISP_TEAL_TEAL_CYAN_NAME,          /* RGB (0.0, 1.0, 0.6) */
    UF_DISP_TEAL_TEAL_GREEN_NAME,         /* RGB (0.0, 1.0, 0.4) */
    UF_DISP_GREEN_GREEN_TEAL_NAME,        /* RGB (0.0, 1.0, 0.2) */
    UF_DISP_PALE_WEAK_MAGENTA_NAME,       /* RGB (1.0, 0.8, 1.0) */
    UF_DISP_PALE_WEAK_RED_NAME,           /* RGB (1.0, 0.8, 0.8) */
    UF_DISP_PALE_DULL_ORANGE_NAME,        /* RGB (1.0, 0.8, 0.6) */
    UF_DISP_LIGHT_ORANGE_YELLOW_NAME,     /* RGB (1.0, 0.8, 0.4) */
    UF_DISP_LIGHT_YELLOW_ORANGE_NAME,     /* RGB (1.0, 0.8, 0.2) */
    UF_DISP_YELLOW_YELLOW_ORANGE_NAME,    /* RGB (1.0, 0.8, 0.0) */
    UF_DISP_PALE_WEAK_BLUE_NAME,          /* RGB (0.8, 0.8, 1.0) */
    UF_DISP_PALE_GRAY_NAME,               /* RGB (0.8, 0.8, 0.8) */
    UF_DISP_LIGHT_WEAK_YELLOW_NAME,       /* RGB (0.8, 0.8, 0.6) */
    UF_DISP_LIGHT_DULL_YELLOW_NAME,       /* RGB (0.8, 0.8, 0.4) */
    UF_DISP_MEDIUM_FADED_YELLOW_NAME,     /* RGB (0.8, 0.8, 0.2) */
    UF_DISP_DARK_HARD_YELLOW_NAME,        /* RGB (0.8, 0.8, 0.0) */
    UF_DISP_PALE_DULL_AZURE_NAME,         /* RGB (0.6, 0.8, 1.0) */
    UF_DISP_LIGHT_WEAK_CYAN_NAME,         /* RGB (0.6, 0.8, 0.8) */
    UF_DISP_LIGHT_WEAK_GREEN_NAME,        /* RGB (0.6, 0.8, 0.6) */
    UF_DISP_LIGHT_DULL_SPRING_NAME,       /* RGB (0.6, 0.8, 0.4) */
    UF_DISP_MEDIUM_SPRING_YELLOW_NAME,    /* RGB (0.6, 0.8, 0.2) */
    UF_DISP_DARK_YELLOW_SPRING_NAME,      /* RGB (0.6, 0.8, 0.0) */
    UF_DISP_LIGHT_AZURE_CYAN_NAME,        /* RGB (0.4, 0.8, 1.0) */
    UF_DISP_LIGHT_DULL_CYAN_NAME,         /* RGB (0.4, 0.8, 0.8) */
    UF_DISP_LIGHT_DULL_TEAL_NAME,         /* RGB (0.4, 0.8, 0.6) */
    UF_DISP_LIGHT_DULL_GREEN_NAME,        /* RGB (0.4, 0.8, 0.4) */
    UF_DISP_MEDIUM_SPRING_GREEN_NAME,     /* RGB (0.4, 0.8, 0.2) */
    UF_DISP_DARK_HARD_SPRING_NAME,        /* RGB (0.4, 0.8, 0.0) */
    UF_DISP_LIGHT_CYAN_AZURE_NAME,        /* RGB (0.2, 0.8, 1.0) */
    UF_DISP_MEDIUM_FADED_CYAN_NAME,       /* RGB (0.2, 0.8, 0.8) */
    UF_DISP_MEDIUM_TEAL_CYAN_NAME,        /* RGB (0.2, 0.8, 0.6) */
    UF_DISP_MEDIUM_TEAL_GREEN_NAME,       /* RGB (0.2, 0.8, 0.4) */
    UF_DISP_MEDIUM_FADED_GREEN_NAME,      /* RGB (0.2, 0.8, 0.2) */
    UF_DISP_DARK_GREEN_SPRING_NAME,       /* RGB (0.2, 0.8, 0.0) */
    UF_DISP_CYAN_CYAN_AZURE_NAME,         /* RGB (0.0, 0.8, 1.0) */
    UF_DISP_DARK_HARD_CYAN_NAME,          /* RGB (0.0, 0.8, 0.8) */
    UF_DISP_DARK_CYAN_TEAL_NAME,          /* RGB (0.0, 0.8, 0.6) */
    UF_DISP_DARK_HARD_TEAL_NAME,          /* RGB (0.0, 0.8, 0.4) */
    UF_DISP_DARK_GREEN_TEAL_NAME,         /* RGB (0.0, 0.8, 0.2) */
    UF_DISP_DARK_HARD_GREEN_NAME,         /* RGB (0.0, 0.8, 0.0) */
    UF_DISP_PALE_DULL_MAGENTA_NAME,       /* RGB (1.0, 0.6, 1.0) */
    UF_DISP_PALE_DULL_PINK_NAME,          /* RGB (1.0, 0.6, 0.8) */
    UF_DISP_PALE_DULL_RED_NAME,           /* RGB (1.0, 0.6, 0.6) */
    UF_DISP_LIGHT_ORANGE_RED_NAME,        /* RGB (1.0, 0.6, 0.4) */
    UF_DISP_LIGHT_HARD_ORANGE_NAME,       /* RGB (1.0, 0.6, 0.2) */
    UF_DISP_ORANGE_ORANGE_YELLOW_NAME,    /* RGB (1.0, 0.6, 0.0) */
    UF_DISP_PALE_DULL_VIOLET_NAME,        /* RGB (0.8, 0.6, 1.0) */
    UF_DISP_LIGHT_WEAK_MAGENTA_NAME,      /* RGB (0.8, 0.6, 0.8) */
    UF_DISP_LIGHT_WEAK_RED_NAME,          /* RGB (0.8, 0.6, 0.6) */
    UF_DISP_LIGHT_DULL_ORANGE_NAME,       /* RGB (0.8, 0.6, 0.4) */
    UF_DISP_MEDIUM_ORANGE_YELLOW_NAME,    /* RGB (0.8, 0.6, 0.2) */
    UF_DISP_DARK_YELLOW_ORANGE_NAME,      /* RGB (0.8, 0.6, 0.0) */
    UF_DISP_PALE_DULL_BLUE_NAME,          /* RGB (0.6, 0.6, 1.0) */
    UF_DISP_LIGHT_WEAK_BLUE_NAME,         /* RGB (0.6, 0.6, 0.8) */
    UF_DISP_MEDIUM_WEAK_YELLOW_NAME,      /* RGB (0.6, 0.6, 0.4) */
    UF_DISP_DARK_DULL_YELLOW_NAME,        /* RGB (0.6, 0.6, 0.2) */
    UF_DISP_DARK_FADED_YELLOW_NAME,       /* RGB (0.6, 0.6, 0.0) */
    UF_DISP_LIGHT_AZURE_BLUE_NAME,        /* RGB (0.4, 0.6, 1.0) */
    UF_DISP_LIGHT_DULL_AZURE_NAME,        /* RGB (0.4, 0.6, 0.8) */
    UF_DISP_MEDIUM_WEAK_CYAN_NAME,        /* RGB (0.4, 0.6, 0.6) */
    UF_DISP_MEDIUM_WEAK_GREEN_NAME,       /* RGB (0.4, 0.6, 0.4) */
    UF_DISP_DARK_DULL_SPRING_NAME,        /* RGB (0.4, 0.6, 0.2) */
    UF_DISP_DARK_SPRING_YELLOW_NAME,      /* RGB (0.4, 0.6, 0.0) */
    UF_DISP_LIGHT_HARD_AZURE_NAME,        /* RGB (0.2, 0.6, 1.0) */
    UF_DISP_MEDIUM_AZURE_CYAN_NAME,       /* RGB (0.2, 0.6, 0.8) */
    UF_DISP_DARK_DULL_CYAN_NAME,          /* RGB (0.2, 0.6, 0.6) */
    UF_DISP_DARK_DULL_TEAL_NAME,          /* RGB (0.2, 0.6, 0.4) */
    UF_DISP_DARK_DULL_GREEN_NAME,         /* RGB (0.2, 0.6, 0.2) */
    UF_DISP_DARK_SPRING_GREEN_NAME,       /* RGB (0.2, 0.6, 0.0) */
    UF_DISP_AZURE_AZURE_CYAN_NAME,        /* RGB (0.0, 0.6, 1.0) */
    UF_DISP_DARK_CYAN_AZURE_NAME,         /* RGB (0.0, 0.6, 0.8) */
    UF_DISP_DARK_FADED_CYAN_NAME,         /* RGB (0.0, 0.6, 0.6) */
    UF_DISP_DARK_TEAL_CYAN_NAME,          /* RGB (0.0, 0.6, 0.4) */
    UF_DISP_DARK_TEAL_GREEN_NAME,         /* RGB (0.0, 0.6, 0.2) */
    UF_DISP_DARK_FADED_GREEN_NAME,        /* RGB (0.0, 0.6, 0.0) */
    UF_DISP_LIGHT_FADED_MAGENTA_NAME,     /* RGB (1.0, 0.4, 1.0) */
    UF_DISP_LIGHT_PINK_MAGENTA_NAME,      /* RGB (1.0, 0.4, 0.8) */
    UF_DISP_LIGHT_PINK_RED_NAME,          /* RGB (1.0, 0.4, 0.6) */
    UF_DISP_LIGHT_FADED_RED_NAME,         /* RGB (1.0, 0.4, 0.4) */
    UF_DISP_LIGHT_RED_ORANGE_NAME,        /* RGB (1.0, 0.4, 0.2) */
    UF_DISP_ORANGE_ORANGE_RED_NAME,       /* RGB (1.0, 0.4, 0.0) */
    UF_DISP_LIGHT_VIOLET_MAGENTA_NAME,    /* RGB (0.8, 0.4, 1.0) */
    UF_DISP_LIGHT_DULL_MAGENTA_NAME,      /* RGB (0.8, 0.4, 0.8) */
    UF_DISP_LIGHT_DULL_PINK_NAME,         /* RGB (0.8, 0.4, 0.6) */
    UF_DISP_LIGHT_DULL_RED_NAME,          /* RGB (0.8, 0.4, 0.4) */
    UF_DISP_MEDIUM_ORANGE_RED_NAME,       /* RGB (0.8, 0.4, 0.2) */
    UF_DISP_DARK_HARD_ORANGE_NAME,        /* RGB (0.8, 0.4, 0.0) */
    UF_DISP_LIGHT_VIOLET_BLUE_NAME,       /* RGB (0.6, 0.4, 1.0) */
    UF_DISP_LIGHT_DULL_VIOLET_NAME,       /* RGB (0.6, 0.4, 0.8) */
    UF_DISP_MEDIUM_WEAK_MAGENTA_NAME,     /* RGB (0.6, 0.4, 0.6) */
    UF_DISP_MEDIUM_WEAK_RED_NAME,         /* RGB (0.6, 0.4, 0.4) */
    UF_DISP_DARK_DULL_ORANGE_NAME,        /* RGB (0.6, 0.4, 0.2) */
    UF_DISP_DARK_ORANGE_YELLOW_NAME,      /* RGB (0.6, 0.4, 0.0) */
    UF_DISP_LIGHT_FADED_BLUE_NAME,        /* RGB (0.4, 0.4, 1.0) */
    UF_DISP_LIGHT_DULL_BLUE_NAME,         /* RGB (0.4, 0.4, 0.8) */
    UF_DISP_MEDIUM_WEAK_BLUE_NAME,        /* RGB (0.4, 0.4, 0.6) */
    UF_DISP_DARK_WEAK_YELLOW_NAME,        /* RGB (0.4, 0.4, 0.2) */
    UF_DISP_OBSCURE_DULL_YELLOW_NAME,     /* RGB (0.4, 0.4, 0.0) */
    UF_DISP_LIGHT_BLUE_AZURE_NAME,        /* RGB (0.2, 0.4, 1.0) */
    UF_DISP_MEDIUM_AZURE_BLUE_NAME,       /* RGB (0.2, 0.4, 0.8) */
    UF_DISP_DARK_DULL_AZURE_NAME,         /* RGB (0.2, 0.4, 0.6) */
    UF_DISP_DARK_WEAK_CYAN_NAME,          /* RGB (0.2, 0.4, 0.4) */
    UF_DISP_DARK_WEAK_GREEN_NAME,         /* RGB (0.2, 0.4, 0.2) */
    UF_DISP_OBSCURE_DULL_SPRING_NAME,     /* RGB (0.2, 0.4, 0.0) */
    UF_DISP_AZURE_AZURE_BLUE_NAME,        /* RGB (0.0, 0.4, 1.0) */
    UF_DISP_DARK_HARD_AZURE_NAME,         /* RGB (0.0, 0.4, 0.8) */
    UF_DISP_DARK_AZURE_CYAN_NAME,         /* RGB (0.0, 0.4, 0.6) */
    UF_DISP_OBSCURE_DULL_CYAN_NAME,       /* RGB (0.0, 0.4, 0.4) */
    UF_DISP_OBSCURE_DULL_TEAL_NAME,       /* RGB (0.0, 0.4, 0.2) */
    UF_DISP_OBSCURE_DULL_GREEN_NAME,      /* RGB (0.0, 0.4, 0.0) */
    UF_DISP_LIGHT_HARD_MAGENTA_NAME,      /* RGB (1.0, 0.2, 1.0) */
    UF_DISP_LIGHT_MAGENTA_PINK_NAME,      /* RGB (1.0, 0.2, 0.8) */
    UF_DISP_LIGHT_HARD_PINK_NAME,         /* RGB (1.0, 0.2, 0.6) */
    UF_DISP_LIGHT_RED_PINK_NAME,          /* RGB (1.0, 0.2, 0.4) */
    UF_DISP_LIGHT_HARD_RED_NAME,          /* RGB (1.0, 0.2, 0.2) */
    UF_DISP_RED_RED_ORANGE_NAME,          /* RGB (1.0, 0.2, 0.0) */
    UF_DISP_LIGHT_MAGENTA_VIOLET_NAME,    /* RGB (0.8, 0.2, 1.0) */
    UF_DISP_MEDIUM_FADED_MAGENTA_NAME,    /* RGB (0.8, 0.2, 0.8) */
    UF_DISP_MEDIUM_PINK_MAGENTA_NAME,     /* RGB (0.8, 0.2, 0.6) */
    UF_DISP_MEDIUM_PINK_RED_NAME,         /* RGB (0.8, 0.2, 0.4) */
    UF_DISP_MEDIUM_FADED_RED_NAME,        /* RGB (0.8, 0.2, 0.2) */
    UF_DISP_DARK_RED_ORANGE_NAME,         /* RGB (0.8, 0.2, 0.0) */
    UF_DISP_LIGHT_HARD_VIOLET_NAME,       /* RGB (0.6, 0.2, 1.0) */
    UF_DISP_MEDIUM_VIOLET_MAGENTA_NAME,   /* RGB (0.6, 0.2, 0.8) */
    UF_DISP_DARK_DULL_MAGENTA_NAME,       /* RGB (0.6, 0.2, 0.6) */
    UF_DISP_DARK_DULL_PINK_NAME,          /* RGB (0.6, 0.2, 0.4) */
    UF_DISP_DARK_DULL_RED_NAME,           /* RGB (0.6, 0.2, 0.2) */
    UF_DISP_DARK_ORANGE_RED_NAME,         /* RGB (0.6, 0.2, 0.0) */
    UF_DISP_LIGHT_BLUE_VIOLET_NAME,       /* RGB (0.4, 0.2, 1.0) */
    UF_DISP_MEDIUM_VIOLET_BLUE_NAME,      /* RGB (0.4, 0.2, 0.8) */
    UF_DISP_DARK_DULL_VIOLET_NAME,        /* RGB (0.4, 0.2, 0.6) */
    UF_DISP_DARK_WEAK_MAGENTA_NAME,       /* RGB (0.4, 0.2, 0.4) */
    UF_DISP_DARK_WEAK_RED_NAME,           /* RGB (0.4, 0.2, 0.2) */
    UF_DISP_OBSCURE_DULL_ORANGE_NAME,     /* RGB (0.4, 0.2, 0.0) */
    UF_DISP_LIGHT_HARD_BLUE_NAME,         /* RGB (0.2, 0.2, 1.0) */
    UF_DISP_MEDIUM_FADED_BLUE_NAME,       /* RGB (0.2, 0.2, 0.8) */
    UF_DISP_DARK_DULL_BLUE_NAME,          /* RGB (0.2, 0.2, 0.6) */
    UF_DISP_DARK_WEAK_BLUE_NAME,          /* RGB (0.2, 0.2, 0.4) */
    UF_DISP_OBSCURE_GRAY_NAME,            /* RGB (0.2, 0.2, 0.2) */
    UF_DISP_OBSCURE_WEAK_YELLOW_NAME,     /* RGB (0.2, 0.2, 0.0) */
    UF_DISP_BLUE_BLUE_AZURE_NAME,         /* RGB (0.0, 0.2, 1.0) */
    UF_DISP_DARK_BLUE_AZURE_NAME,         /* RGB (0.0, 0.2, 0.8) */
    UF_DISP_DARK_AZURE_BLUE_NAME,         /* RGB (0.0, 0.2, 0.6) */
    UF_DISP_OBSCURE_DULL_AZURE_NAME,      /* RGB (0.0, 0.2, 0.4) */
    UF_DISP_OBSCURE_WEAK_CYAN_NAME,       /* RGB (0.0, 0.2, 0.2) */
    UF_DISP_OBSCURE_WEAK_GREEN_NAME,      /* RGB (0.0, 0.2, 0.0) */
    UF_DISP_MAGENTA_MAGENTA_PINK_NAME,    /* RGB (1.0, 0.0, 0.8) */
    UF_DISP_PINK_PINK_MAGENTA_NAME,       /* RGB (1.0, 0.0, 0.6) */
    UF_DISP_PINK_PINK_RED_NAME,           /* RGB (1.0, 0.0, 0.4) */
    UF_DISP_RED_RED_PINK_NAME,            /* RGB (1.0, 0.0, 0.2) */
    UF_DISP_MAGENTA_MAGENTA_VIOLET_NAME,  /* RGB (0.8, 0.0, 1.0) */
    UF_DISP_DARK_HARD_MAGENTA_NAME,       /* RGB (0.8, 0.0, 0.8) */
    UF_DISP_DARK_MAGENTA_PINK_NAME,       /* RGB (0.8, 0.0, 0.6) */
    UF_DISP_DARK_HARD_PINK_NAME,          /* RGB (0.8, 0.0, 0.4) */
    UF_DISP_DARK_RED_PINK_NAME,           /* RGB (0.8, 0.0, 0.2) */
    UF_DISP_DARK_HARD_RED_NAME,           /* RGB (0.8, 0.0, 0.0) */
    UF_DISP_VIOLET_VIOLET_MAGENTA_NAME,   /* RGB (0.6, 0.0, 1.0) */
    UF_DISP_DARK_MAGENTA_VIOLET_NAME,     /* RGB (0.6, 0.0, 0.8) */
    UF_DISP_DARK_FADED_MAGENTA_NAME,      /* RGB (0.6, 0.0, 0.6) */
    UF_DISP_DARK_PINK_MAGENTA_NAME,       /* RGB (0.6, 0.0, 0.4) */
    UF_DISP_DARK_PINK_RED_NAME,           /* RGB (0.6, 0.0, 0.2) */
    UF_DISP_DARK_FADED_RED_NAME,          /* RGB (0.6, 0.0, 0.0) */
    UF_DISP_VIOLET_VIOLET_BLUE_NAME,      /* RGB (0.4, 0.0, 1.0) */
    UF_DISP_DARK_HARD_VIOLET_NAME,        /* RGB (0.4, 0.0, 0.8) */
    UF_DISP_DARK_VIOLET_MAGENTA_NAME,     /* RGB (0.4, 0.0, 0.6) */
    UF_DISP_OBSCURE_DULL_MAGENTA_NAME,    /* RGB (0.4, 0.0, 0.4) */
    UF_DISP_OBSCURE_DULL_PINK_NAME,       /* RGB (0.4, 0.0, 0.2) */
    UF_DISP_OBSCURE_DULL_RED_NAME,        /* RGB (0.4, 0.0, 0.0) */
    UF_DISP_BLUE_BLUE_VIOLET_NAME,        /* RGB (0.2, 0.0, 1.0) */
    UF_DISP_DARK_BLUE_VIOLET_NAME,        /* RGB (0.2, 0.0, 0.8) */
    UF_DISP_DARK_VIOLET_BLUE_NAME,        /* RGB (0.2, 0.0, 0.6) */
    UF_DISP_OBSCURE_DULL_VIOLET_NAME,     /* RGB (0.2, 0.0, 0.4) */
    UF_DISP_OBSCURE_WEAK_MAGENTA_NAME,    /* RGB (0.2, 0.0, 0.2) */
    UF_DISP_OBSCURE_WEAK_RED_NAME,        /* RGB (0.2, 0.0, 0.0) */
    UF_DISP_DARK_HARD_BLUE_NAME,          /* RGB (0.0, 0.0, 0.8) */
    UF_DISP_DARK_FADED_BLUE_NAME,         /* RGB (0.0, 0.0, 0.6) */
    UF_DISP_OBSCURE_DULL_BLUE_NAME,       /* RGB (0.0, 0.0, 0.4) */
    UF_DISP_OBSCURE_WEAK_BLUE_NAME,       /* RGB (0.0, 0.0, 0.2) */
    UF_DISP_BLACK_NAME,             /* RGB (0.0000000, 0.0000000, 0.0000000) */
    UF_DISP_CHARCOAL_GRAY_NAME,     /* RGB (0.0470588, 0.0470588, 0.0470588) */
    UF_DISP_DARK_GRAY_NAME,         /* RGB (0.2000000, 0.2000000, 0.2000000) */
    UF_DISP_IRON_GRAY_NAME,         /* RGB (0.2980392, 0.2980392, 0.2980392) */
    UF_DISP_GRANITE_GRAY_NAME,      /* RGB (0.4000000, 0.4000000, 0.4000000) */
    UF_DISP_MEDIUM_GRAY_NAME,       /* RGB (0.4901961, 0.4901961, 0.4901961) */
    UF_DISP_SILVER_GRAY_NAME,       /* RGB (0.6000000, 0.6000000, 0.6000000) */
    UF_DISP_SMOKE_GRAY_NAME,        /* RGB (0.6941176, 0.6941176, 0.6941176) */
    UF_DISP_LIGHT_GRAY_NAME,        /* RGB (0.8000000, 0.8000000, 0.8000000) */
    UF_DISP_ASH_GRAY_NAME,          /* RGB (0.8745098, 0.8745098, 0.8745098) */
    UF_DISP_POWDER_GRAY_NAME,       /* RGB (0.9490196, 0.9490196, 0.9490196) */
    UF_DISP_WHITE_NAME,             /* RGB (1.0000000, 1.0000000, 1.0000000) */
    UF_DISP_MAGENTA_NAME,           /* RGB (1.0000000, 0.0000000, 1.0000000) */
    UF_DISP_DEEP_MAGENTA_NAME,      /* RGB (0.8000000, 0.2000000, 0.8000000) */
    UF_DISP_STRONG_MAGENTA_NAME,    /* RGB (1.0000000, 0.2274510, 0.8823529) */
    UF_DISP_MEDIUM_MAGENTA_NAME,    /* RGB (1.0000000, 0.4274510, 1.0000000) */
    UF_DISP_PALE_MAGENTA_NAME,      /* RGB (1.0000000, 0.6627451, 1.0000000) */
    UF_DISP_RED_NAME,               /* RGB (1.0000000, 0.0000000, 0.0000000) */
    UF_DISP_DEEP_RED_NAME,          /* RGB (1.0000000, 0.1882353, 0.1882353) */
    UF_DISP_STRONG_RED_NAME,        /* RGB (1.0000000, 0.3176471, 0.3176471) */
    UF_DISP_MEDIUM_RED_NAME,        /* RGB (1.0000000, 0.4000000, 0.4000000) */
    UF_DISP_PALE_RED_NAME,          /* RGB (1.0000000, 0.5647059, 0.5647059) */
    UF_DISP_ORANGE_NAME,            /* RGB (1.0000000, 0.6000000, 0.0000000) */
    UF_DISP_DEEP_ORANGE_NAME,       /* RGB (1.0000000, 0.4000000, 0.0000000) */
    UF_DISP_STRONG_ORANGE_NAME,     /* RGB (1.0000000, 0.6000000, 0.2000000) */
    UF_DISP_MEDIUM_ORANGE_NAME,     /* RGB (1.0000000, 0.7529412, 0.2980392) */
    UF_DISP_PALE_ORANGE_NAME,       /* RGB (1.0000000, 0.8000000, 0.6000000) */
    UF_DISP_YELLOW_NAME,            /* RGB (1.0000000, 1.0000000, 0.0000000) */
    UF_DISP_DEEP_YELLOW_NAME,       /* RGB (1.0000000, 0.7921569, 0.0000000) */
    UF_DISP_STRONG_YELLOW_NAME,     /* RGB (1.0000000, 0.8627451, 0.2274510) */
    UF_DISP_MEDIUM_YELLOW_NAME,     /* RGB (1.0000000, 0.9411765, 0.4941176) */
    UF_DISP_PALE_YELLOW_NAME,       /* RGB (1.0000000, 0.9411765, 0.6627451) */
    UF_DISP_LIME_NAME,              /* RGB (0.8000000, 1.0000000, 0.2000000) */
    UF_DISP_DEEP_LIME_NAME,         /* RGB (0.6627451, 0.8901961, 0.0000000) */
    UF_DISP_STRONG_LIME_NAME,       /* RGB (0.7372549, 0.9294118, 0.2039216) */
    UF_DISP_MEDIUM_LIME_NAME,       /* RGB (0.8000000, 1.0000000, 0.4000000) */
    UF_DISP_PALE_LIME_NAME,         /* RGB (0.8000000, 1.0000000, 0.6000000) */
    UF_DISP_GREEN_NAME,             /* RGB (0.0000000, 1.0000000, 0.0000000) */
    UF_DISP_DEEP_GREEN_NAME,        /* RGB (0.4000000, 0.8000000, 0.0000000) */
    UF_DISP_STRONG_GREEN_NAME,      /* RGB (0.2000000, 1.0000000, 0.2000000) */
    UF_DISP_MEDIUM_GREEN_NAME,      /* RGB (0.6000000, 1.0000000, 0.4000000) */
    UF_DISP_PALE_GREEN_NAME,        /* RGB (0.8431373, 1.0000000, 0.7803922) */
    UF_DISP_EMERALD_NAME,           /* RGB (0.0000000, 0.6000000, 0.0000000) */
    UF_DISP_DEEP_EMERALD_NAME,      /* RGB (0.0000000, 0.6745098, 0.3960784) */
    UF_DISP_STRONG_EMERALD_NAME,    /* RGB (0.0000000, 0.8039216, 0.5254902) */
    UF_DISP_MEDIUM_EMERALD_NAME,    /* RGB (0.4470588, 1.0000000, 0.8039216) */
    UF_DISP_PALE_EMERALD_NAME,      /* RGB (0.6000000, 1.0000000, 0.7921569) */
    UF_DISP_CYAN_NAME,              /* RGB (0.0000000, 1.0000000, 1.0000000) */
    UF_DISP_DEEP_CYAN_NAME,         /* RGB (0.0000000, 0.8117647, 0.8117647) */
    UF_DISP_STRONG_CYAN_NAME,       /* RGB (0.3058824, 1.0000000, 1.0000000) */
    UF_DISP_MEDIUM_CYAN_NAME,       /* RGB (0.6000000, 1.0000000, 1.0000000) */
    UF_DISP_PALE_CYAN_NAME,         /* RGB (0.7411765, 1.0000000, 1.0000000) */
    UF_DISP_CORNFLOWER_NAME,        /* RGB (0.0000000, 0.6000000, 1.0000000) */
    UF_DISP_DEEP_CORNFLOWER_NAME,   /* RGB (0.0000000, 0.2666667, 1.0000000) */
    UF_DISP_STRONG_CORNFLOWER_NAME, /* RGB (0.2000000, 0.6000000, 1.0000000) */
    UF_DISP_MEDIUM_CORNFLOWER_NAME, /* RGB (0.4000000, 0.8000000, 1.0000000) */
    UF_DISP_PALE_CORNFLOWER_NAME,   /* RGB (0.6000000, 0.8000000, 1.0000000) */
    UF_DISP_BLUE_NAME,              /* RGB (0.0000000, 0.0000000, 1.0000000) */
    UF_DISP_DEEP_BLUE_NAME,         /* RGB (0.0000000, 0.0000000, 0.7529412) */
    UF_DISP_STRONG_BLUE_NAME,       /* RGB (0.2000000, 0.2000000, 1.0000000) */
    UF_DISP_MEDIUM_BLUE_NAME,       /* RGB (0.2549020, 0.3764706, 1.0000000) */
    UF_DISP_PALE_BLUE_NAME,         /* RGB (0.5372549, 0.7137255, 1.0000000) */
    UF_DISP_COBALT_NAME,            /* RGB (0.0000000, 0.0000000, 1.0000000) */
    UF_DISP_DEEP_COBALT_NAME,       /* RGB (0.0000000, 0.0000000, 0.7529412) */
    UF_DISP_STRONG_COBALT_NAME,     /* RGB (0.2000000, 0.2000000, 1.0000000) */
    UF_DISP_MEDIUM_COBALT_NAME,     /* RGB (0.2549020, 0.3764706, 1.0000000) */
    UF_DISP_PALE_COBALT_NAME,       /* RGB (0.5372549, 0.7137255, 1.0000000) */
    UF_DISP_PURPLE_NAME,            /* RGB (0.4000000, 0.2000000, 0.8000000) */
    UF_DISP_DEEP_PURPLE_NAME,       /* RGB (0.4000000, 0.0000000, 0.8000000) */
    UF_DISP_STRONG_PURPLE_NAME,     /* RGB (0.4000000, 0.0000000, 1.0000000) */
    UF_DISP_MEDIUM_PURPLE_NAME,     /* RGB (0.4470588, 0.4156863, 1.0000000) */
    UF_DISP_PALE_PURPLE_NAME,       /* RGB (0.7098039, 0.7098039, 1.0000000) */
    UF_DISP_BROWN_NAME,             /* RGB (0.6000000, 0.4000000, 0.2000000) */
    UF_DISP_DEEP_BROWN_NAME,        /* RGB (0.4000000, 0.2000000, 0.0000000) */
    UF_DISP_STRONG_BROWN_NAME,      /* RGB (0.6431373, 0.4000000, 0.0000000) */
    UF_DISP_MEDIUM_BROWN_NAME,      /* RGB (0.8000000, 0.6000000, 0.2000000) */
    UF_DISP_PALE_BROWN_NAME,        /* RGB (0.9411765, 0.8000000, 0.5254902) */
    UF_DISP_DEEP_FUCHSIA_NAME,      /* RGB (0.2588235, 0.0980392, 0.2588235) */
    UF_DISP_STRONG_FUSHCIA_NAME,    /* RGB (0.5647059, 0.1960784, 0.4156863) */
    UF_DISP_MEDIUM_FUCHSIA_NAME,    /* RGB (0.6941176, 0.4588235, 0.5764706) */
    UF_DISP_PALE_FUCHSIA_NAME,      /* RGB (0.8274510, 0.6235294, 0.7843137) */
    UF_DISP_DEEP_MAROON_NAME,       /* RGB (0.4000000, 0.0000000, 0.0000000) */
    UF_DISP_STRONG_MAROON_NAME,     /* RGB (0.6000000, 0.2000000, 0.2000000) */
    UF_DISP_MEDIUM_MAROON_NAME,     /* RGB (0.6000000, 0.4000000, 0.4000000) */
    UF_DISP_PALE_MAROON_NAME,       /* RGB (0.8117647, 0.6039216, 0.6117647) */
    UF_DISP_DEEP_CORAL_NAME,        /* RGB (0.6745098, 0.2156863, 0.0745098) */
    UF_DISP_STRONG_CORAL_NAME,      /* RGB (0.8235294, 0.4196078, 0.2156863) */
    UF_DISP_MEDIUM_CORAL_NAME,      /* RGB (0.7882353, 0.5921569, 0.3960784) */
    UF_DISP_PALE_CORAL_NAME,        /* RGB (0.8196078, 0.7019608, 0.6196078) */
    UF_DISP_DEEP_GOLD_NAME,         /* RGB (0.6117647, 0.4549020, 0.1607843) */
    UF_DISP_STRONG_GOLD_NAME,       /* RGB (0.6705882, 0.5960784, 0.3215686) */
    UF_DISP_MEDIUM_GOLD_NAME,       /* RGB (0.8823529, 0.7607843, 0.2823529) */
    UF_DISP_PALE_GOLD_NAME,         /* RGB (0.8901961, 0.8274510, 0.6156863) */
    UF_DISP_DEEP_KHAKI_NAME,        /* RGB (0.4000000, 0.4000000, 0.2000000) */
    UF_DISP_STRONG_KHAKI_NAME,      /* RGB (0.5529412, 0.5803922, 0.2039216) */
    UF_DISP_MEDIUM_KHAKI_NAME,      /* RGB (0.6980392, 0.6941176, 0.4039216) */
    UF_DISP_PALE_KHAKI_NAME,        /* RGB (0.7568627, 0.7568627, 0.5647059) */
    UF_DISP_DEEP_PINE_NAME,         /* RGB (0.3686275, 0.5215686, 0.2470588) */
    UF_DISP_STRONG_PINE_NAME,       /* RGB (0.5333333, 0.7333333, 0.4392157) */
    UF_DISP_MEDIUM_PINE_NAME,       /* RGB (0.6274510, 0.8313725, 0.6588235) */
    UF_DISP_PALE_PINE_NAME,         /* RGB (0.7647059, 0.8823529, 0.7450980) */
    UF_DISP_DEEP_SEA_NAME,          /* RGB (0.2000000, 0.4000000, 0.2000000) */
    UF_DISP_STRONG_SEA_NAME,        /* RGB (0.2823529, 0.5647059, 0.4156863) */
    UF_DISP_MEDIUM_SEA_NAME,        /* RGB (0.5176471, 0.6784314, 0.6078431) */
    UF_DISP_PALE_SEA_NAME,          /* RGB (0.7176471, 0.8117647, 0.7647059) */
    UF_DISP_DEEP_TURQUOISE_NAME,    /* RGB (0.1254902, 0.3450980, 0.4039216) */
    UF_DISP_STRONG_TURQUOISE_NAME,  /* RGB (0.1921569, 0.5215686, 0.6078431) */
    UF_DISP_MEDIUM_TURQUOISE_NAME,  /* RGB (0.5098039, 0.7137255, 0.7686275) */
    UF_DISP_PALE_TORQUOISE_NAME,    /* RGB (0.6862745, 0.8588235, 0.8588235) */
    UF_DISP_DEEP_STEEL_NAME,        /* RGB (0.1411765, 0.2509804, 0.3803922) */
    UF_DISP_STRONG_STEEL_NAME,      /* RGB (0.2117647, 0.3764706, 0.5725490) */
    UF_DISP_MEDIUM_STEEL_NAME,      /* RGB (0.5960784, 0.6666667, 0.6862745) */
    UF_DISP_PALE_STEEL_NAME,        /* RGB (0.7529412, 0.8235294, 0.8823529) */
    UF_DISP_DEEP_MIDNIGHT_NAME,     /* RGB (0.0588235, 0.1411765, 0.2431373) */
    UF_DISP_STRONG_MIDNIGHT_NAME,   /* RGB (0.1647059, 0.2862745, 0.4470588) */
    UF_DISP_MEDIUM_MIDNIGHT_NAME,   /* RGB (0.5019608, 0.6352941, 0.7058824) */
    UF_DISP_PALE_MIDNIGHT_NAME,     /* RGB (0.6039216, 0.7294118, 0.8392157) */
    UF_DISP_DEEP_INDIGO_NAME,       /* RGB (0.2431373, 0.2000000, 0.3294118) */
    UF_DISP_STRONG_INDIGO_NAME,     /* RGB (0.3607843, 0.2862745, 0.5019608) */
    UF_DISP_MEDIUM_INDIGO_NAME,     /* RGB (0.4627451, 0.4156863, 0.5882353) */
    UF_DISP_PALE_INDIGO_NAME,       /* RGB (0.6509804, 0.6392157, 0.7686275) */
    UF_DISP_DEEP_STONE_NAME,        /* RGB (0.2862745, 0.2705882, 0.1803922) */
    UF_DISP_STRONG_STONE_NAME,      /* RGB (0.5764706, 0.5450980, 0.3921569) */
    UF_DISP_MEDIUM_STONE_NAME,      /* RGB (0.7686275, 0.7490196, 0.6470588) */
    UF_DISP_PALE_STONE_NAME,        /* RGB (0.8666667, 0.8549020, 0.7882353) */
    UF_DISP_DEEP_PLUM_NAME,         /* RGB (0.3960784, 0.0000000, 0.2666667) */
    UF_DISP_STRONG_PLUM_NAME,       /* RGB (0.6000000, 0.2000000, 0.4000000) */
    UF_DISP_MEDIUM_PLUM_NAME,       /* RGB (0.7529412, 0.1882353, 0.6431373) */
    UF_DISP_PALE_PLUM_NAME,         /* RGB (0.8000000, 0.4000000, 0.6000000) */
    UF_DISP_DEEP_CRIMSON_NAME,      /* RGB (0.4941176, 0.0000000, 0.0000000) */
    UF_DISP_STRONG_CRIMSON_NAME,    /* RGB (0.6000000, 0.0000000, 0.0000000) */
    UF_DISP_MEDIUM_CRIMSON_NAME,    /* RGB (0.8000000, 0.2000000, 0.2000000) */
    UF_DISP_PALE_CRIMSON_NAME,      /* RGB (0.8509804, 0.3372549, 0.2980392) */
    UF_DISP_DEEP_CARROT_NAME,       /* RGB (0.4274510, 0.1764706, 0.0392157) */
    UF_DISP_STRONG_CARROT_NAME,     /* RGB (0.5647059, 0.3137255, 0.0274510) */
    UF_DISP_MEDIUM_CARROT_NAME,     /* RGB (0.9019608, 0.4823529, 0.0705882) */
    UF_DISP_PALE_CARROT_NAME,       /* RGB (0.9647059, 0.6274510, 0.2862745) */
    UF_DISP_DEEP_OLIVE_NAME,        /* RGB (0.4352941, 0.4078431, 0.0000000) */
    UF_DISP_STRONG_OLIVE_NAME,      /* RGB (0.6078431, 0.5647059, 0.0000000) */
    UF_DISP_MEDIUM_OLIVE_NAME,      /* RGB (0.8000000, 0.8000000, 0.2000000) */
    UF_DISP_PALE_OLIVE_NAME,        /* RGB (0.9019608, 0.8588235, 0.2862745) */
    UF_DISP_DEEP_LEAF_NAME,         /* RGB (0.3058824, 0.3803922, 0.0000000) */
    UF_DISP_STRONG_LEAF_NAME,       /* RGB (0.2901961, 0.4509804, 0.1058824) */
    UF_DISP_MEDIUM_LEAF_NAME,       /* RGB (0.4627451, 0.6235294, 0.1647059) */
    UF_DISP_PALE_LEAF_NAME,         /* RGB (0.6196078, 0.7921569, 0.2392157) */
    UF_DISP_DEEP_FOREST_NAME,       /* RGB (0.1098039, 0.2862745, 0.0117647) */
    UF_DISP_STRONG_FOREST_NAME,     /* RGB (0.0000000, 0.4000000, 0.0000000) */
    UF_DISP_MEDIUM_FOREST_NAME,     /* RGB (0.2000000, 0.6000000, 0.2000000) */
    UF_DISP_PALE_FOREST_NAME,       /* RGB (0.4313725, 0.7019608, 0.3803922) */
    UF_DISP_DEEP_MOSS_NAME,         /* RGB (0.0000000, 0.2274510, 0.0000000) */
    UF_DISP_STRONG_MOSS_NAME,       /* RGB (0.0000000, 0.3450980, 0.1568627) */
    UF_DISP_MEDIUM_MOSS_NAME,       /* RGB (0.0000000, 0.5882353, 0.4352941) */
    UF_DISP_PALE_MOSS_NAME,         /* RGB (0.2156863, 0.6666667, 0.5333333) */
    UF_DISP_DEEP_TEAL_NAME,         /* RGB (0.0000000, 0.2784314, 0.2509804) */
    UF_DISP_STRONG_TEAL_NAME,       /* RGB (0.0000000, 0.4000000, 0.4000000) */
    UF_DISP_MEDIUM_TEAL_NAME,       /* RGB (0.0000000, 0.6000000, 0.6000000) */
    UF_DISP_PALE_TEAL_NAME,         /* RGB (0.1450980, 0.6235294, 0.6470588) */
    UF_DISP_DEEP_AZURE_NAME,        /* RGB (0.0000000, 0.2470588, 0.3686275) */
    UF_DISP_STRONG_AZURE_NAME,      /* RGB (0.0000000, 0.4000000, 0.6000000) */
    UF_DISP_MEDIUM_AZURE_NAME,      /* RGB (0.0000000, 0.6156863, 0.8509804) */
    UF_DISP_PALE_AZURE_NAME,        /* RGB (0.0000000, 0.6901961, 0.9411765) */
    UF_DISP_DEEP_ROYAL_NAME,        /* RGB (0.0705882, 0.1568627, 0.4274510) */
    UF_DISP_STRONG_ROYAL_NAME,      /* RGB (0.0000000, 0.2235294, 0.6039216) */
    UF_DISP_MEDIUM_ROYAL_NAME,      /* RGB (0.2000000, 0.4000000, 0.8000000) */
    UF_DISP_PALE_ROYAL_NAME,        /* RGB (0.2196078, 0.4705882, 0.7529412) */
    UF_DISP_DEEP_VIOLET_NAME,       /* RGB (0.1411765, 0.0000000, 0.1411765) */
    UF_DISP_STRONG_VIOLET_NAME,     /* RGB (0.2235294, 0.0666667, 0.3333333) */
    UF_DISP_MEDIUM_VIOLET_NAME,     /* RGB (0.3176471, 0.1215686, 0.4980392) */
    UF_DISP_PALE_VIOLET_NAME,       /* RGB (0.4000000, 0.4000000, 0.8000000) */
    UF_DISP_DEEP_UMBER_NAME,        /* RGB (0.1607843, 0.1411765, 0.1333333) */
    UF_DISP_STRONG_UMBER_NAME,      /* RGB (0.2549020, 0.2156863, 0.1960784) */
    UF_DISP_MEDIUM_UMBER_NAME,      /* RGB (0.3725490, 0.3137255, 0.2705882) */
    UF_DISP_PALE_UMBER_NAME,        /* RGB (0.5254902, 0.4509804, 0.3803922) */
    UF_DISP_DEEP_PINK_NAME,         /* RGB (0.9176471, 0.4313725, 0.6470588) */
    UF_DISP_STRONG_PINK_NAME,       /* RGB (0.9333333, 0.5843137, 0.7411765) */
    UF_DISP_MEDIUM_PINK_NAME,       /* RGB (0.9607843, 0.7490196, 0.8470588) */
    UF_DISP_PALE_PINK_NAME,         /* RGB (0.9764706, 0.8431373, 0.9058824) */
    UF_DISP_DEEP_SALMON_NAME,       /* RGB (1.0000000, 0.5450980, 0.5450980) */
    UF_DISP_STRONG_SALMON_NAME,     /* RGB (1.0000000, 0.6000000, 0.6000000) */
    UF_DISP_MEDIUM_SALMON_NAME,     /* RGB (1.0000000, 0.7019608, 0.7058824) */
    UF_DISP_PALE_SALMON_NAME,       /* RGB (1.0000000, 0.8431373, 0.8235294) */
    UF_DISP_DEEP_PEACH_NAME,        /* RGB (0.9647059, 0.6274510, 0.4078431) */
    UF_DISP_STRONG_PEACH_NAME,      /* RGB (0.9686275, 0.6862745, 0.5176471) */
    UF_DISP_MEDIUM_PEACH_NAME,      /* RGB (0.9843137, 0.7803922, 0.6274510) */
    UF_DISP_PALE_PEACH_NAME,        /* RGB (0.9607843, 0.8313725, 0.7254902) */
    UF_DISP_DEEP_LEMON_NAME,        /* RGB (1.0000000, 0.9098039, 0.3843137) */
    UF_DISP_STRONG_LEMON_NAME,      /* RGB (1.0000000, 0.9490196, 0.5137255) */
    UF_DISP_MEDIUM_LEMON_NAME,      /* RGB (1.0000000, 0.9607843, 0.6549020) */
    UF_DISP_PALE_LEMON_NAME,        /* RGB (1.0000000, 0.9803922, 0.7490196) */
    UF_DISP_DEEP_PISTACHIO_NAME,    /* RGB (0.8117647, 0.8705882, 0.4196078) */
    UF_DISP_STRONG_PISTACHIO_NAME,  /* RGB (0.8627451, 0.8901961, 0.6039216) */
    UF_DISP_MEDIUM_PISTACHIO_NAME,  /* RGB (0.8901961, 0.9098039, 0.5254902) */
    UF_DISP_PALE_PISTACHIO_NAME,    /* RGB (0.9098039, 0.9254902, 0.8470588) */
    UF_DISP_DEEP_SPRING_NAME,       /* RGB (0.6117647, 0.8156863, 0.4941176) */
    UF_DISP_STRONG_SPRING_NAME,     /* RGB (0.6705882, 0.8392157, 0.6274510) */
    UF_DISP_MEDIUM_SPRING_NAME,     /* RGB (0.7960784, 0.9019608, 0.7843137) */
    UF_DISP_PALE_SPRING_NAME,       /* RGB (0.8666667, 0.9215686, 0.8392157) */
    UF_DISP_DEEP_MINT_NAME,         /* RGB (0.4705882, 0.7529412, 0.5490196) */
    UF_DISP_STRONG_MINT_NAME,       /* RGB (0.6039216, 0.8117647, 0.6588235) */
    UF_DISP_MEDIUM_MINT_NAME,       /* RGB (0.7058824, 0.8588235, 0.7450980) */
    UF_DISP_PALE_MINT_NAME,         /* RGB (0.8156863, 0.9098039, 0.8352941) */
    UF_DISP_DEEP_AQUA_NAME,         /* RGB (0.3764706, 0.8039216, 0.8235294) */
    UF_DISP_STRONG_AQUA_NAME,       /* RGB (0.6235294, 0.8352941, 0.8235294) */
    UF_DISP_MEDIUM_AQUA_NAME,       /* RGB (0.7529412, 0.8901961, 0.8745098) */
    UF_DISP_PALE_AQUA_NAME,         /* RGB (0.8627451, 0.9372549, 0.9294118) */
    UF_DISP_DEEP_SKY_NAME,          /* RGB (0.3372549, 0.6941176, 1.0000000) */
    UF_DISP_STRONG_SKY_NAME,        /* RGB (0.5960784, 0.7882353, 0.9215686) */
    UF_DISP_MEDIUM_SKY_NAME,        /* RGB (0.7647059, 0.8784314, 0.9450980) */
    UF_DISP_PALE_SKY_NAME,          /* RGB (0.8823529, 0.9607843, 1.0000000) */
    UF_DISP_DEEP_ICE_NAME,          /* RGB (0.4000000, 0.6000000, 0.8000000) */
    UF_DISP_STRONG_ICE_NAME,        /* RGB (0.5960784, 0.6901961, 0.8470588) */
    UF_DISP_MEDIUM_ICE_NAME,        /* RGB (0.7019608, 0.7647059, 0.8784314) */
    UF_DISP_PALE_ICE_NAME,          /* RGB (0.8117647, 0.8431373, 0.9098039) */
    UF_DISP_DEEP_LAVENDER_NAME,     /* RGB (0.4784314, 0.4509804, 0.7098039) */
    UF_DISP_STRONG_LAVENDER_NAME,   /* RGB (0.5921569, 0.5843137, 0.7725490) */
    UF_DISP_MEDIUM_LAVENDER_NAME,   /* RGB (0.6784314, 0.6588235, 0.8313725) */
    UF_DISP_PALE_LAVENDER_NAME,     /* RGB (0.7921569, 0.7803922, 0.8941176) */
    UF_DISP_DEEP_TAN_NAME,          /* RGB (0.7019608, 0.5058824, 0.3647059) */
    UF_DISP_STRONG_TAN_NAME,        /* RGB (0.7137255, 0.5725490, 0.4313725) */
    UF_DISP_MEDIUM_TAN_NAME,        /* RGB (0.7764706, 0.6588235, 0.5529412) */
    UF_DISP_PALE_TAN_NAME,          /* RGB (0.8274510, 0.7411765, 0.6705882) */
    UF_DISP_MAX_COLOR_NAME
};
/*==========================================================================

==========================================================================*/

typedef enum UF_DISP_color_name_e UF_DISP_color_name_t, *UF_DISP_color_name_p_t;


/****************************************************************************
 *
 *  ENUMERATED:  UF_DISP_poly_marker_t
 *
 *  DESCRIPTION: This enumerated type specifies the type of marker to
 *               be displayed
 *
 *
 ****************************************************************************/
enum UF_DISP_poly_marker_e
{
    UF_DISP_NO_MARKER = 0,

    UF_DISP_POINT,
    UF_DISP_DOT,
    UF_DISP_ASTERISK,
    UF_DISP_CIRCLE,
    UF_DISP_POUNDSIGN,
    UF_DISP_X,
    UF_DISP_GRIDPOINT,
    UF_DISP_SQUARE,
    UF_DISP_TRIANGLE_MARKER,
    UF_DISP_DIAMOND,
    UF_DISP_CENTERLINE,
    UF_DISP_CONS_FIX,
    UF_DISP_CONS_HORIZONTAL,
    UF_DISP_CONS_VERTICAL,
    UF_DISP_CONS_PARALLEL,
    UF_DISP_CONS_PERPENDICULAR,
    UF_DISP_CONS_TANGENT,
    UF_DISP_CONS_CONCENTRIC,
    UF_DISP_CONS_COINCIDENT ,
    UF_DISP_CONS_COLLINEAR ,
    UF_DISP_CONS_POINT_ON_CURVE ,
    UF_DISP_CONS_MIDPOINT ,
    UF_DISP_CONS_EQUAL_LENGTH ,
    UF_DISP_CONS_EQUAL_RADIUS ,
    UF_DISP_CONS_CONSTANT_LENGTH ,
    UF_DISP_CONS_CONSTANT_ANGLE ,
    UF_DISP_CONS_MIRROR ,
    UF_DISP_DIM_RADIUS ,
    UF_DISP_DIM_DIAMETER ,
    UF_DISP_DIM_PARALLEL ,
    UF_DISP_DIM_PERPENDICULAR ,
    UF_DISP_CONS_SLOPE ,
    UF_DISP_CONS_STRING ,
    UF_DISP_CONS_UNIFORM_SCALED ,
    UF_DISP_CONS_NON_UNIFORM_SCALED ,
    UF_DISP_CONS_ASSOC_TRIM ,
    UF_DISP_CONS_ASSOC_OFFSET ,
    UF_DISP_2T_RES_SPOT_WELD ,
    UF_DISP_3T_RES_SPOT_WELD ,
    UF_DISP_4T_RES_SPOT_WELD ,
    UF_DISP_2T_DC_SPOT_WELD ,
    UF_DISP_3T_DC_SPOT_WELD ,
    UF_DISP_4T_DC_SPOT_WELD ,
    UF_DISP_2T_KPC_SPOT_WELD ,
    UF_DISP_3T_KPC_SPOT_WELD ,
    UF_DISP_4T_KPC_SPOT_WELD ,
    UF_DISP_2T_PROC_SPOT_WELD ,
    UF_DISP_3T_PROC_SPOT_WELD ,
    UF_DISP_4T_PROC_SPOT_WELD ,
    UF_DISP_ARC_SPOT_WELD ,
    UF_DISP_CLINCH_WELD ,
    UF_DISP_ANCHOR ,
    UF_DISP_LEFT_LEADER_CONNECTION ,
    UF_DISP_RIGHT_LEADER_CONNECTION ,
    UF_DISP_FILLED_CIRCLE ,
    UF_DISP_FILLED_SQUARE ,
    UF_DISP_LARGE_FILLED_SQUARE ,
    UF_DISP_DATUM_POINT ,
    UF_DISP_SNAPPING_DIAMOND,
    UF_DISP_CIRCLE_IN_CIRCLE,
    UF_DISP_CIRCLE_IN_SQUARE,
    UF_DISP_SQUARE_IN_SQUARE,
    UF_DISP_FILLED_LEFT_TRIANGLE,
    UF_DISP_FILLED_RIGHT_TRIANGLE,
    UF_DISP_FILLED_UP_TRIANGLE,
    UF_DISP_FILLED_DOWN_TRIANGLE,
    UF_DISP_FILLED_LEFT_TRIANGLE_IN_CIRCLE,
    UF_DISP_FILLED_RIGHT_TRIANGLE_IN_CIRCLE,
    UF_DISP_FILLED_UP_TRIANGLE_IN_CIRCLE,
    UF_DISP_FILLED_DOWN_TRIANGLE_IN_CIRCLE,
    UF_DISP_FILLED_LEFT_TRIANGLE_IN_SQUARE,
    UF_DISP_FILLED_RIGHT_TRIANGLE_IN_SQUARE,
    UF_DISP_FILLED_UP_TRIANGLE_IN_SQUARE,
    UF_DISP_FILLED_DOWN_TRIANGLEIN_SQUARE,
    UF_DISP_ROUNDED_CROSS,
    UF_DISP_FILLED_DIAMOND,
    UF_DISP_UP_DOWN_TRIANGLES,
    UF_DISP_LEFT_RIGHT_TRIANGLES,
    UF_DISP_SMALL_WHEEL,
    UF_DISP_LARGE_WHEEL,
    UF_DISP_HOLLOW_CIRCLE,
    UF_DISP_PREVIEW_PERPENDICULAR,
    UF_DISP_PREVIEW_HORIZONTAL,
    UF_DISP_PREVIEW_VERTICAL,
    UF_DISP_PREVIEW_TANGENT,
    UF_DISP_PREVIEW_PARALLEL,
    UF_DISP_PREVIEW_POINT_ON_CURVE,
    UF_DISP_PREVIEW_COLLINEAR,
    UF_DISP_RULER,
    UF_DISP_PROTRACTOR,
    UF_DISP_SKETCH_NOTEBOOK,
    UF_DISP_ARC_END_POINT,
    UF_DISP_2_PT_ARC_MARKER,
    UF_DISP_BIG_ASTERISK,
    UF_DISP_LINE_IN_CIRCLE,
    UF_DISP_PLUS_IN_CIRCLE,
    UF_DISP_CENTER_OF_ROTATION,
    UF_DISP_PREVIEW_X,
    UF_DISP_PREVIEW_Y,
    UF_DISP_PREVIEW_Z,
    UF_DISP_2T_GENERAL_SPOT_WELD,
    UF_DISP_3T_GENERAL_SPOT_WELD,
    UF_DISP_4T_GENERAL_SPOT_WELD,
    UF_DISP_2T_VITAL_SPOT_WELD,
    UF_DISP_3T_VITAL_SPOT_WELD,
    UF_DISP_4T_VITAL_SPOT_WELD,
    UF_DISP_2T_IMPORTANT_SPOT_WELD,
    UF_DISP_3T_IMPORTANT_SPOT_WELD,
    UF_DISP_4T_IMPORTANT_SPOT_WELD,
    UF_DISP_2T_SEMIPANEL_SPOT_WELD,
    UF_DISP_3T_SEMIPANEL_SPOT_WELD,
    UF_DISP_4T_SEMIPANEL_SPOT_WELD,
    UF_DISP_SPOT_WELD_NUT,
    UF_DISP_SPOT_WELD_STUD,

    UF_DISP_INVALID_MARKER
};
/***************************************************************************

  ***************************************************************************/

typedef enum UF_DISP_poly_marker_e UF_DISP_poly_marker_t,
                                  *UF_DISP_poly_marker_p_t;


/****************************************************************************
 *
 *  ENUMERATED:  UF_DISP_text_ref_e_t
 *
 *  DESCRIPTION: This enumerated type specifies the type of reference point
 *               used in the text box.
 *
 *
 ****************************************************************************/
enum UF_DISP_text_ref_e
{
   UF_DISP_TOPLEFT=1,  /* Display the text in the top left of the text box */
   UF_DISP_TOPCENTER=2,/* Display the text in the top center of the text box */
   UF_DISP_TOPRIGHT=3, /* Display the text in the top right of the text box */
   UF_DISP_MIDDLELEFT=4,/* Display the text in the middle left of the text box*/
   UF_DISP_MIDDLECENTER=5, /* Display the text in middle center of text box */

   UF_DISP_MIDDLERIGHT=6, /* Display the text in middle right of text box*/

   UF_DISP_BOTTOMLEFT=7,  /* Display the text in bottom left of text box */

   UF_DISP_BOTTOMCENTER=8,/* Display the text in bottom center of text box */

   UF_DISP_BOTTOMRIGHT=9,  /* Display the text in bottom right of text box */
   UF_DISP_SYSTEMDEFAULT=0 /* Display the text using the system default */
};

typedef enum UF_DISP_text_ref_e UF_DISP_text_ref_t, *UF_DISP_text_ref_p_t;

/****************************************************************************
 *
 *  ENUMERATED:  UF_DISP_view_type_t
 *
 *  DESCRIPTION: The enumerated type of the view mode to use
 *
 *
 ****************************************************************************/
enum UF_DISP_view_type_e
{
    UF_DISP_USE_VIEW_TAG=0,         /* Display in view specified by its tag */
    UF_DISP_USE_ACTIVE_PLUS=1,      /* Use the active view plus drawing views*/
    UF_DISP_USE_CURSOR=2,           /* Use the position of the last cursor */
    UF_DISP_USE_ACTIVE_MINUS=3,     /* Use only active views no drawing views*/
    UF_DISP_USE_WORK_VIEW=4         /* Use the work view */
};

typedef enum UF_DISP_view_type_e UF_DISP_view_type_t;




/****************************************************************************
 *
 *  The Following Section Contains the Definitions and Prototypes
 *  for User Defined Objects (UDO's)
 *
 ****************************************************************************/

/****************************************************************************
 *
 *  ENUMERATED:  UF_DISP_facet_type_t
 *
 *  DESCRIPTION: The enumerated type facet to be displayed
 *
 *
 ****************************************************************************/
enum UF_DISP_facet_type_e
{
    UF_DISP_TRIANGLE,     /* The facet topology is a triangle facet */
    UF_DISP_POLYGON,      /* The facet topology is a polygon facet */
    UF_DISP_TRISTRIP      /* The facet topology is a tristrip facet */
};

typedef enum UF_DISP_facet_type_e UF_DISP_facet_type_t,
                                 *UF_DISP_facet_type_p_t;

/****************************************************************************
 *
 *  ENUMERATED:  UF_DISP_context_t
 *
 *  DESCRIPTION:  This enumerated type contains definitions for
 *                each of the context values found in the inquiry
 *                structure
 *
 *
 *
 ****************************************************************************/
enum UF_DISP_context_e
{
    UF_DISP_DISPLAY,         /* The geometry is being displayed */
    UF_DISP_FIT,             /* The geometry is being fit */
    UF_DISP_SELECT_SING,     /* The geometry is being selected by a single pick */
    UF_DISP_SELECT_BOX,      /* The geometry is rectangle or polygon selected */
    UF_DISP_ATTEN,           /* The geometry attention point is being calculated */
    UF_DISP_SCREEN_SIZE_FIT  /* A fit for screen size geometry is being done */
};

typedef enum UF_DISP_context_e UF_DISP_context_t, *UF_DISP_context_p_t;
/****************************************************************************
 *
 *  STRUCTURE:  UF_DISP_inquire_t
 *
 *  DESCRIPTION:  This structure contains information about the context
 *                in which the geometry is displayed.  The user must
 *                check to make sure that the information is available
 *                before using the contents.  There are logicals in this
 *                structure to check to see if information has been returned.
 *
 *
 *
 ****************************************************************************/
struct UF_DISP_inquire_s
{
   UF_DISP_context_t context_running;
                                /* Describes the context which is being
                                   executed when the inquire is performed.
                                   The context may be display, selection,
                                   fit, or attention point. */

   logical is_view_mode_valid;   /* True if the view mode was returned and
                                    False if no information was available */

   int view_mode;                /* View mode describes the views shading
                                    and face analysis mode valid values
                                    are
                                        UF_VIEW_NOT_SHADED
                                        UF_VIEW_PARTIALLY_SHADED
                                        UF_VIEW_FULLY_SHADED
                                        UF_VIEW_ANALYSIS_SHADED
                                    See uf_view.h for definitions
                                  */
   logical is_atten_pt_valid;    /* True if the atten point was returned and
                                    False if no information was available */

   double atten_pt[3];           /* The attention point of the geometry
                                    just displayed */

   logical is_draw_open_disp;    /* Is the drawing view open for display?
                                    If true then geometry may be added to
                                    the drawing. If false another view
                                    which is not the drawing is open */

   tag_t view_tag;               /* View tag of the view being displayed */


};

typedef struct UF_DISP_inquire_s UF_DISP_inquire_t, *UF_DISP_inquire_p_t;
/****************************************************************************
 *
 *  STRUCTURE:  UF_DISP_facet_t
 *
 *  DESCRIPTION: This structure contains the vertices and normals
 *               for ONE facet.  The structure may be put into an
 *               array so that many facets may be displayed at one time.
 *
 *
 *
 ****************************************************************************/
struct UF_DISP_facet_s
{
    double *vertices;    /* The vertices are of the form
                                (X,           Y,            Z )
                            ((vertices[1], vertices[2], vertices[3]),
                             (vertices[4], vertices[5], vertices[6])
                             ...
                            in which each vertex point is represented by an
                            (x,y,z) coordinate */
    double *normals;     /* The normals are of the same form as the vertices
                            above.  The number of normals must equal the
                            number of vertices */
};

typedef struct UF_DISP_facet_s UF_DISP_facet_t, *UF_DISP_facet_p_t;


/****************************************************************************
 *
 *  ENUMERATED:  UF_DISP_grid_context_t
 *
 *  DESCRIPTION:  This enumerated type contains definitions for
 *                each of the context values found in the grid
 *                structure
 *
 *  UF_DISP_SKETCH_GRID    For the grid to be used when a sketch is displayed
 *  UF_DISP_DRAWING_GRID   For the grid to be used when a drawing is displayed
 *  UF_DISP_MODEL_GRID     For the grid to be used when neither a sketch nor
 *                         a drawing is displayed
 *  UF_DISP_SHED_GRID      For a grid to be used during True Shading display
 *  UF_DISP_NULL_GRID      When no grid is available (if no part exists)
 *
 ****************************************************************************/
enum UF_DISP_grid_context_e
{
    UF_DISP_SKETCH_GRID,    /* the grid for the sketcher */
    UF_DISP_DRAWING_GRID,   /* the grid for the drawing */
    UF_DISP_MODEL_GRID,     /* the default grid context */
    UF_DISP_SHED_GRID,      /* the grid for True Shading */
    UF_DISP_NULL_GRID       /* no grid is available (rarely) */
};
typedef enum UF_DISP_grid_context_e UF_DISP_grid_context_t;

/****************************************************************************
 *
 *  ENUMERATED:  UF_DISP_grid_type_t
 *
 *  DESCRIPTION:  This enumerated type contains definitions of the grid type
 *
 ****************************************************************************/
enum UF_DISP_grid_type_e
{
    UF_DISP_POLAR_GRID,        /* a circular grid using polar coordinates */
    UF_DISP_RECTANGULAR_GRID   /* the default retangular grid */
};
typedef enum UF_DISP_grid_type_e UF_DISP_grid_type_t;

/****************************************************************************
 *
 *  STRUCTURE:  UF_DISP_grid_s
 *
 *  DESCRIPTION: This is the definition of a grid structure. It is used to
 *               specifies the parameters to apply when a grid is used.
 *               There are 3 grid application contexts & 2 grid types. The
 *               grid behaviors and appearances are different among them.
 *               Grid "emphasis" lines and circles are drawn as solid lines,
 *               while other grid line and circles are drawn as a series of
 *               dots.
 *
 *  show_grid        - TRUE to make the grid visible, FALSE otherwise.
 *  snap_to_grid     - TRUE to enable snapping, FALSE otherwise.
 *  grid_color       - 1 to 216
 *  grid_type        - Either rectangular (default) or polar
 *  grid_non_uniform - TRUE allows X & Y units to be different,
 *                     FALSE (default) is otherwise.
 *  grid_on_top - TRUE to show grid on top of all displayed graphics
 *
 *
 *  rectangular_grid_emphasis - TRUE (default) to draw the emphasis lines,
 *                              FALSE otherwise.
 *  grid_unit_x       - Distance between dots along X in inches/mm.
 *  grid_unit_y       - Distance between dots along Y. If 'grid_non_uniform' is
 *                      FALSE, this field is ignored.
 *  grid_line_every_x - No. of dots between each grid line along X.
 *  grid_line_every_y - No. of dots between each grid line along Y. If
 *                      'grid_non_uniform' is FALSE, this field is ignored.
 *  grid_emphasis_every_x - This value must be a multiple of
 *                          'grid_line_every_x'.
 *  grid_emphasis_every_y - Like 'grid_emphasis_every_x' except it is ignored
 *                          when 'grid_non_uniform' is FALSE.
 *
 *
 *  polar_grid_emphasis - TRUE (default) to draw the emphasis lines,
 *                        FALSE otherwise.
 *  grid_angular_unit   - Angular distance between dots in degrees (at the
 *                        first ring when all dots are visible).
 *  grid_angular_line_every - No. of fully visible dots between each grid line.
 *  grid_angular_emphasis_every - This value must be a multiple of
 *                                'grid_angular_line_every'.
 *  grid_radial_unit - Distance between dots along angular lines in inche/mm.
 *  grid_radial_circle_every   - No. of dots between each concentric circles.
 *  grid_radial_emphasis_every - this value must be a multiple of
 *                               'grid_radial_circle_every'.
 *
 ****************************************************************************/
struct UF_DISP_grid_s
{
    logical                  show_grid;                  /* FALSE    */
    logical                  show_labels;                
    logical                  snap_to_grid;               /* FALSE    */
    int                      grid_color;
    UF_DISP_grid_type_t      grid_type;                  /* UF_DISP_RECTANGULAR_GRID */
    logical                  grid_non_uniform;           /* FALSE    */
    logical                  grid_on_top;                

    logical                  rectangular_grid_emphasis;  /* TRUE     */
    double                   grid_unit_x;                /* 0.125 in or 1 mm */
    double                   grid_unit_y;                /* " " " " " */
    int                      grid_line_every_x;          /* 4 (0.5 in) or 5 (5 mm) */
    int                      grid_line_every_y;          /* " " " " " */
    int                      grid_emphasis_every_x;      /* 2 (1 in) or 10 (10 mm) */
    int                      grid_emphasis_every_y;      /* " " " " " */

    logical                  polar_grid_emphasis;        /* TRUE      */
    double                   grid_angular_unit;          /* 15 Deg.   */
    int                      grid_angular_line_every;    /* 3 (45 Deg)*/
    int                      grid_angular_emphasis_every;/* 2 (90 Deg)*/
    double                   grid_radial_unit;           /* 0.125 in or 1 mm */
    int                      grid_radial_circle_every;   /* 4 (0.5 in) or 5 (5 mm) */
    int                      grid_radial_emphasis_every; /* 2 (1 in) or 10 (10 mm) */
};
typedef struct UF_DISP_grid_s UF_DISP_grid_t, *UF_DISP_grid_p_t;

/* **************************************************************************
    Structure definition for conehead attribute settings
 * **************************************************************************/
struct UF_DISP_conehead_attrb_s_tag
{
   double staff_length;    /* Length of conehead staff.  Default is 0.6 */
   double total_length;    /* Length of overall conehead = arrowhead+staff
                              Default is 1.0 */
   double cone_radius;     /* The radius of the arrowhead's base.  The
                              default is .075 */
   int    color;           /* The color to draw the vector in, or
                              -1 = Use background Color
                               0 = Use System Color
                           */

   int    font;            /* The display font setting:
                              1 = Solid
                              2 = Dashed
                              3 = Phantom
                              4 = Centerline
                              5-7 = User Defined */
   int    density;         /* The density settings
                              0 = Normal
                              1 = Heavy
                              2 = Thin  */
};

typedef struct UF_DISP_conehead_attrb_s_tag UF_DISP_conehead_attrb_s;

enum UF_DISP_image_format_e
{
    UF_DISP_PNG,
    UF_DISP_JPEG,
    UF_DISP_TIFF,
    UF_DISP_COMPRESSED_TIFF,
    UF_DISP_GIF,
    UF_DISP_XWD,  /*  Supported only on UNIX workstations     */
    UF_DISP_BMP   /*  Supported only on Windows workstations  */
};

typedef enum UF_DISP_image_format_e UF_DISP_image_format_t;

enum UF_DISP_background_color_e
{
    UF_DISP_ORIGINAL,
    UF_DISP_WHITE,
    UF_DISP_INVALID_COLOR
};

typedef enum UF_DISP_background_color_e UF_DISP_background_color_t;

enum UF_DISP_shade_format_e
{
    UF_DISP_FORMAT_RASTER,
    UF_DISP_FORMAT_QTVR_PANORAMA,
    UF_DISP_FORMAT_QTVR_OBJECT_LOW,
    UF_DISP_FORMAT_QTVR_OBJECT_HIGH
};

typedef enum UF_DISP_shade_format_e UF_DISP_shade_format_t;

enum UF_DISP_shade_display_e
{
    UF_DISP_DISPLAY_RGB_PLUS_NOISE,
    UF_DISP_DISPLAY_FS_RGB,
    UF_DISP_DISPLAY_FS_RGB_PLUS_NOISE,
    UF_DISP_DISPLAY_MONOCHROME,
    UF_DISP_DISPLAY_GRAY_SCALE,
    UF_DISP_DISPLAY_NEAREST_RGB,
    UF_DISP_DISPLAY_ORDERED_DITHER,
    UF_DISP_DISPLAY_TC_PLUS_NOISE
};

typedef enum UF_DISP_shade_display_e UF_DISP_shade_display_t;

enum UF_DISP_shade_plot_e
{
    UF_DISP_PLOT_FINE,
    UF_DISP_PLOT_MEDIUM,
    UF_DISP_PLOT_ROUGH,
    UF_DISP_PLOT_COARSE
};

typedef enum UF_DISP_shade_plot_e UF_DISP_shade_plot_t;

/* **************************************************************************
    Structure definition for shading processing options for batch shading.
 * **************************************************************************/
struct UF_DISP_shade_options_s
{
    UF_DISP_shade_format_t format;    /* Format */
    UF_DISP_shade_display_t display;  /* Display option */
    int resolution;                   /* Dots per inch of image,
                                         Draft -> 75
                                         Low -> 180
                                         Medium -> 300
                                         High -> 400
                                      */
    UF_DISP_shade_plot_t plot_quality;/* Plot quality */
    logical generate_shadows;         /* Generate shadows or not? */
    double facet_quality;             /* Quality of facets
                                         0.01 -> 2.0 */
    logical transparent_shadows;      /* Allow transparent shadows or not? */
    logical disable_raytracing;       /* Disable ray tracing or not? */
    logical fixed_camera_viewing;     /* Fixed camera viewing or not? */
    int super_sample;                 /* Super sample
                                         1 -> 5 */
    int subdivision_depth;            /* Subdivision depth
                                         0 -> 6 */
    int raytrace_memory;              /* Memory in Mb for ray tracing,
                                         4, 8, 16, 32, 64, 128 */
    int radiosity_quality;            /* Radiosity quality
                                         0 -> 15 */
    logical distribute_excess_light;  /* Distribute excess light or not? */
    logical use_midpoint_sampling;    /* Use midpoint sampling or not? */
};

typedef struct UF_DISP_shade_options_s UF_DISP_shade_options_t, *UF_DISP_shade_options_p_t;



/* **************************************************************************
    Structure definition for material texture space information
 * **************************************************************************/

enum UF_DISP_texture_space_type_e
{
   UF_DISP_arbitrary_plane_texture_space,
   UF_DISP_cylindrical_texture_space,
   UF_DISP_spherical_texture_space,
   UF_DISP_autoaxis_texture_space,
   UF_DISP_uv_texture_space,
   UF_DISP_use_camera_direction_plane_texture_space
};

typedef enum UF_DISP_texture_space_type_e UF_DISP_texture_space_type_t;


struct UF_DISP_texture_space_info_s
{
   UF_DISP_texture_space_type_t type;
   double ts_scale;
   double ts_scale1;
   double aspect_ratio;
   double origin[3];
   double normal_vector[3];
   double up_vector[3];
   double center_point[3];
   int camera_direction_plane_option;
};

typedef struct UF_DISP_texture_space_info_s UF_DISP_texture_space_info_t, * UF_DISP_texture_space_info_p_t;

/*------------------------------------------------------------------
UF_DISP_arbitrary_plane_texture_space

Arguments:
"scale"  Type: double Default: 1.0 [ts_scale]
"aspect ratio"  Type:  double  Default: 1.0 [aspect_ratio]
"origin"  Type:  double[3] Default: (0.0, 0.0, 0.0) [origin]
"normal vector"  double[3] Default: (0.0, 0.0, 1.0) [normal_vector]
"up"  Type:  double[3] Default: (0.0, 1.0, 0.0) [up_vector]
"camera_direction_plane_option": Type: int <0 - normal vector only ,1 -both normal and up vectors>
     This option determines how texture space vectors are updated upon "Update Texture to Camera Direction"
     Type: int :0 texture space normal vector alone is updated to camera direction 
                1 both texture space normal and up vectors are updated to camera direction.

Definition:
A texture space in which all points are mapped onto an arbitrary plane.
The plane is specified in terms of a point which lies in the plane as
argument "origin", a normal vector perpendicular to the plane as argument
"normal_vector", and an orientation expressed as an ``up'' vector passed
in argument "up_vecotr". The point passed as "origin" is used for the origin of
textures such that the texture origins appear at this point. An overall
scaling factor can be passed as argument "ts_scale". Increasing this value
will have the effect of increasing the scale of all wrapped textures which
use this texture space.
The aspect ratio of the texture space, defined as one unit of its height
divided by one unit of its width, may be set by the value passed to argument
"aspect ratio". This is interpreted such that the horizontal scale is equal
to the value passed as argument "scale", and the vertical scale is equal to
the product of this value and the value passed for argument "aspect ratio".
-------------------------------------------------------------------------*/


/*------------------------------------------------------------------
UF_DISP_cylindrical_texture_space

Arguments:
"scale around axis"  Type:  double Default: 1.0 [ts_scale]
"scale along axis"  Type:  double Default: 1.0 [ts_scale1]
"centre point"  Type:  double[3] Default: (0.0, 0.0, 0.0)    [center_point]
"axis direction"  Type:  double[3] Default: (0.0, 0.0, 1.0) [normal_vector]
"origin"  Type:  double[3] Default: (1.0, 0.0, 0.0)             [origin]

Definition:
A texture space in which all points in space are mapped onto a cylinder.
The cylinder is specified in terms of a point on its axis in argument "centre
point", and a direction vector along the axis in argument "normal_vector".
The origin of wrapped textures is specified by means of argument "origin".
Scaling factors are provided in the direction around the axis in argument
"ts_scale", and in the direction along the axis in argument "ts_scale1".
The "scale around axis or ts_scale" is applied such that decreasing its value
will cause a "wrapped" shader to repeat more over a corresponding cylindrical
surface.
-------------------------------------------------------------------------*/

/*------------------------------------------------------------------
UF_DISP_spherical_texture_space

Arguments:
"latitude scale"  Type:  double Default: 1.0   [ts_scale]
"longitude scale"  Type:  double Default: 1.0 [ts_scale1]
"centre point"  Type:  double [3] Default: (0.0, 0.0, 0.0) [center_point]
"origin"  Type:  double[3] Default: (1.0, 0.0, 0.0) [origin]
"axis direction"  Type:  double[3] Default: (0.0, 0.0, 1.0) [up_vector]

Definition:
A texture space in which all points in space are mapped onto a sphere. The
sphere is specified in terms of its centre point, passed as argument "centre
point", and a point which corresponds to the origin of wrapped textures, passed
as argument "origin". The orientation is specified by an ``up'' vector passed
as argument "axis direction", which corresponds to the upward pointing axis of
the sphere.
Scaling factors are provided, one in the latitudinal direction ( "ts_scale")
and one in the longitudinal direction ( "ts_scale1"). These
scales are applied such that decreasing their value will cause a "wrapped"
shader to repeat more over a corresponding spherical surface.
-------------------------------------------------------------------------*/

/*------------------------------------------------------------------
UF_DISP_autoaxis_tecture_space

Arguments:
"scale"  Type:  double Default: 1.0 [ts_scale]

Definition:
A texture space which selects one of the three coordinate axes
(x- y- and z-axes) whose plane is most closely aligned with the surface at
each point. The points in space are then mapped onto this plane. An overall
scaling factor is provided by argument "ts_scale". Increasing this value will
have the effect of increasing the scale of all wrapped textures which use
this mapping.
-------------------------------------------------------------------------*/

/*------------------------------------------------------------------
UF_DISP_uv_tecture_space

Arguments:
"u scale"  Type: double Default: 1.0 [ts_scale]
"v scale"  Type:  double Default: 1.0         [ts_scale1]

Definition:
A texture space type that assigns the parametric coordinate
system to the texture space. Independent scaling factors are provided for
the u- and v-coordinate directions in arguments "ts_scale" and "ts_scale1"
respectively. This texture space type may be used for geometry that has a natural
parametric coordinate system, such as all algebraic and patch primitives.
-------------------------------------------------------------------------*/

/*------------------------------------------------------------------
UF_DISP_use_camera_direction_plane_texture_space

Arguments:
"scale"  Type: double Default: 1.0 [ts_scale]
"aspect ratio"  Type:  double  Default: 1.0 [aspect_ratio]
"origin"  Type:  double[3] Default: (0.0, 0.0, 0.0) [origin]
"normal vector"  double[3] Default: (0.0, 0.0, 1.0) [normal_vector]
"up"  Type:  double[3] Default: (0.0, 1.0, 0.0) [up_vector]
"camera_direction_plane_option": Type: int <0 - normal vector only ,1 - both normal and up vectors>
     This option determines how texture space vectors are updated based on the camera direction. 
     Type: int :0 texture space normal vector alone is updated to camera direction 
                1 both texture space normal and up vectors are updated to camera direction.

Definition:
This texture space is the same as UF_DISP_arbitrary_plane_texture_space.
The only difference is that the normal vector and or up vector(determined by the camera_direction_plane_option argument) 
are automatically updated during viewing operation to the camera direction. 
-------------------------------------------------------------------------*/

/* **************************************************************************
    Structure definition for visualization material texture origin 

    This is used to determine the source of the currently selected material. 
    It is used in UF_DISP_ask_currently_selected_material.
*/
enum UF_DISP_material_source_e 
{
  UF_DISP_lw_material_in_Materials_Library,
  UF_DISP_lw_material_in_Materials_in_Part_Palette
};
typedef enum UF_DISP_material_source_e UF_DISP_material_source_t;

#ifdef __cplusplus
}
#endif

#endif    /*  END  UF_DISP_TYPES_INCLUDED  */
