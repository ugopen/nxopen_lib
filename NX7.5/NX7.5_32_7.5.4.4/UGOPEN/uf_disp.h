/*****************************************************************************

        Copyright 1993 Siemens Product Lifecycle Management Software Inc. 
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

#ifndef UF_DISP_INCLUDED
#define UF_DISP_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_obj_types.h>
#include <uf_disp_types.h>
#include <uf_retiring.h>
#include <uf_disp_ugopenint.h>
#include <uf_cfi.h>
#include <libufun_exports.h>  /* Must be last */


#ifdef __cplusplus
extern "C" {
#endif

/*
     Function prototypes
*/

/*****************************************************************
 * Creates polygon and vector data for the geometry of a part file.
 * The output polygon data is triangle strips for polygon data and
 * vectors for curves.
 *
 * wireframe - a boolean value where if the value is 1, then solids
 *             and sheets will be returned as wireframe vector data
 *             for the edges of the body.  If the value is 0, then
 *             solids and sheets will be returned as triangle strip
 *             polygon data.
 * num_entities - returns the number of elements in the entity_list
 * entitiy_list - An array of display data structures
 *
 * Environment: Internal  and  External
 * See Also: None
 * History: None
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_j3d_geometry( int                     wireframe, /* <I> */
                                            int                    *num_entities, /* <O> */
                                            UF_DISP_j3d_entity_p_t *entity_list /* <OF, len:num_entities> */ );

/*****************************************************************
 * Cleans up the data returned from UF_DISP_j3d_geometry
 * Environment: Internal  and  External
 * See Also: None
 * History: None
 ****************************************************************/
extern UFUNEXPORT int UF_DISP_j3d_free_geometry( int num_entities, /* <I> */
                                                 UF_DISP_j3d_entity_p_t entity_list /* <I, len:num_entities> */ );

/*****************************************************************
 * Creates a shaded image using the capabilities of NX Photo and saves
 * that image as a TIFF, GIF, or JPEG file. You specify the image type
 * by including the appropriate file extension in the save_filename
 * parameter. Use any one of the following file extensions:
 * .tif - TIFF
 * .gif - GIF
 * .jpg - JPEG
 * For example, specifying "test.jpg" for the filename parameter
 * creates a JPEG file.
 * The batch shade function shades the active view using the light
 * sources, backgrounds, foregrounds, materials and textures that were
 * setup using interactive NX. If the current layout is a drawing then
 * this function will return without creating an output file.
 *
 * If using a shade method of UF_DISP_high_quality, UF_DISP_preview,
 * UF_DISP_photo_real or UF_DISP_raytrace then a Studio Render license
 * is required.  If this license is not available then the method will
 * default back to UF_DISP_phong.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History: This function was modified in V14.0 to also produce GIF
 * and JPEG files
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_batch_shade(
    char* filename ,            /* <I>
                                Name of output TIFF, GIF, or JPEG file
                                */
    int x_size ,                /* <I>
                                X size of output in pixels
                                */
    int y_size ,                /* <I>
                                Y size of output in pixels
                                */
    UF_DISP_shade_method_t method  /* <I>
                                   Type of shade to produce.  Either:
                                    UF_DISP_flat, UF_DISP_gouraud,
                                    UF_DISP_phong, UF_DISP_high_quality,
                                    UF_DISP_preview,
                                    UF_DISP_photo_real, or
                                    UF_DISP_raytrace
                                    */
);

/*****************************************************************
 * Creates a shaded image using the capabilities of NX Photo and saves
 * that image as a TIFF, GIF, or JPEG file. You specify the image type
 * by including the appropriate file extension in the save_filename
 * parameter. Use any one of the following file extensions:
 * .tif - TIFF
 * .gif - GIF
 * .jpg - JPEG
 * For example, specifying "test.jpg" for the filename parameter
 * creates a JPEG file.
 * The batch shade function shades the active view using the light
 * sources, backgrounds, foregrounds, materials and textures that were
 * setup using interactive NX. If the current layout is a drawing then
 * this function will return without creating an output file.
 * This function allows setting of some options for the shading process.
 *
 * If using a shade method of UF_DISP_high_quality, UF_DISP_preview,
 * UF_DISP_photo_real or UF_DISP_raytrace then a Studio Render license
 * is required.  If this license is not available then the method will
 * default back to UF_DISP_phong.
 *
 * Environment: Internal  and  External
 * See Also:
 * History: This function was first released in NX3.0.3
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_batch_shade_options(
    char* filename ,            /* <I>
                                Name of output TIFF, GIF, or JPEG file
                                */
    int x_size ,                /* <I>
                                X size of output in pixels
                                */
    int y_size ,                /* <I>
                                Y size of output in pixels
                                */
    UF_DISP_shade_method_t method, /* <I>
                                   Type of shade to produce.  Either:
                                    UF_DISP_flat, UF_DISP_gouraud,
                                    UF_DISP_phong, UF_DISP_high_quality,
                                    UF_DISP_preview,
                                    UF_DISP_photo_real, or
                                    UF_DISP_raytrace
                                    */
    UF_DISP_shade_options_p_t options /* <I>
                                      Options to control the shading
                                      process.
                                      */
);

/*****************************************************************
 * Allows the batch creation of an MPEG movie based on an existing
 * animation saved in the opened part.  An Animation can be created 
 * using the Create Animation Dialog.  See the NX Gateway Online 
 * help for details on creating an animation name and frames.
 *
 * Note that only animations of "Define Key Frames" type are supported.
 * The Default animation is "Define Trajectory Curves" type.  To create
 * a "Define Key Frames" type animation, the user needs to select
 * "Define Key Frames" prior to selecting Add/Copy when creating a new 
 * animation.
 *
 * Returns:   0 = Success
 *           -1 = Unable to find data for "animation_name"
 *           -2 = General error creating MPEG data
 * not -1,-2, 0 = Error code
 *            Standard UF Error Codes
 * Environment: Internal  and  External
 * See Also:
 * History: Original release was in V13.0.
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_create_animation(
       char * filename ,             /* <I>
                                     Name of output file for MPEG data
                                     */
       char * animation_name ,       /* <I>
                                     Name of a Key Frame camera pan in the part
                                     */
       int first_frame ,             /* <I>
                                     Initial frame to generate (usually 0)
                                     */
       int last_frame                /* <I>
                                     Final frame to generate
                                     */
);

/*****************************************************************************
 * Performs an entire display refresh.
 * Return: void
 * Environment: Internal
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT void UF_DISP_refresh(void); /*<NEC>*/

/*****************************************************************************
 * Ensures that previously invoked display operations are complete.
 *
 * Function UF_DISP_make_display_up_to_date should be called only by
 * NX Open API programs that directly invoke Windows, MFC, or Motif
 * functions to display dialogs. This function is unneeded when
 * NX Open dialogs are used.
 *
 * When NX Open functions perform display operations, the display
 * operations can be buffered. NX Open dialog logic ensures that
 * the buffered operations are completed at appropriate times. If
 * a NX Open API program bypasses NX Open dialog logic, the program
 * might need to explicitly invoke UF_DISP_make_display_up_to_date
 * to complete buffered operations. The function should be called
 * immediately before invoking Windows, MFC, or Motif functions to
 * display dialogs.
 *
 * Return:
 *     Zero is returned upon successful execution.
 *     Any other return code indicates an error.
 * Environment: Internal
 * See Also:
 * History: Originally released in V17.0.2
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_make_display_up_to_date(void);

/*****************************************************************************
 * Returns the current name display setting.
 * Return:
 *
 * Environment: Internal  and  External
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_name_display_status (
                     int * current_status    /* <O>
                                             Name Display Status:
                                             UF_DISP_NAME_DISPLAY_OFF
                                             UF_DISP_NAME_DISPLAY_ON
                                             */
);

/*****************************************************************************
 * Sets the name display status for objects.  Names are created with
 * UF_OBJ_set_name, and the location where they are displayed is set with
 * UF_OBJ_set_name_origin.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 *  UF_OBJ_set_name
 *  UF_OBJ_set_name_origin
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_set_name_display_status (
                   const int new_status      /* <I>
                                             Name display status:
                                             UF_DISP_NAME_DISPLAY_OFF
                                             UF_DISP_NAME_DISPLAY_ON
                                             */
);

/*****************************************************************************
 * Returns the current name display view setting. The constant
 * UF_DISP_NAMES_IN_VIEW_OF_DEFN is the view which was the
 * work view when the object was defined.
 *
 * Environment: Internal  and  External
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_name_view_status (
           int * current_status           /* <O>
                                          View Status
                                          0 = UF_DISP_NAMES_IN_WORK_VIEW
                                          1 = UF_DISP_NAMES_IN_VIEW_OF_DEFN
                                          */
);

/*****************************************************************************
 * Sets the name display view status. The constant
 * UF_DISP_NAMES_IN_VIEW_OF_DEFN is the view which is the work
 * view when the object is defined.
 * Environment: Internal  and  External
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_set_name_view_status (
              const int new_status        /* <I>
                                          Name display view status:
                                          UF_DISP_NAMES_IN_WORK_VIEW
                                          UF_DISP_NAMES_IN_VIEW_OF_DEFN
                                          */
);

/*****************************************************************************
 * Turns object/feature highlight on or off.
 * Environment: Internal
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_set_highlight(
          tag_t object_id ,       /* <I>
                                  Object/Feature identifier
                                  */
          int action_switch       /* <I>
                                  Action Switch
                                  0 = Turn Highlight Off
                                  1 = Turn Highlight On
                                  */
);

/*****************************************************************************
 * Queries the display status. You can use UF_DISP_ask_display to find out
 * the current state of the graphics display.
 * Environment: Internal
 * See Also:
 * History: Released in V16.0
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_display(
          int *display_code     /* <O>
                                display code:
                                UF_DISP_SUPPRESS_DISPLAY- set display off
                                UF_DISP_UNSUPPRESS_DISPLAY- set display on
                                */
);

/*****************************************************************************
 * Sets the display status. You can use UF_DISP_set_display to turn
 * off the graphics display before executing a long series of graphics
 * intensive operations such as manipulations of views, layouts, or
 * drawings. You must call UF_DISP_regenerate_display to update the
 * display after turning it back on.
 * Note that there are limitations to this function in conjunction with
 * layout and drawing changes. If you open a layout or drawing, the
 * display will change to show the outlines of the views in the layout
 * or drawing, even though the suppress state is enabled; the contents
 * of the views will not be shown however.
 * Environment: Internal
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_set_display(
          int display_code      /* <I>
                                display code:
                                UF_DISP_SUPPRESS_DISPLAY- set display off
                                UF_DISP_UNSUPPRESS_DISPLAY- set display on
                                */
);

/****************************************************************************
 * Regenerates the display of a single view . The view must  be currently
 * displayed. If you specify an inactive view (i.e. a view on a layout or a
 * drawing which is not displayed), an error occurs. Use
 * UF_VIEW_ask_tag_of_view_name to find the view_tag.
 *
 * Environment: Internal
 * See Also:
 *  UF_VIEW_ask_tag_of_view_name
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DISP_regenerate_view(
             tag_t view_tag         /* <I>
                                    The tag of the view to regenerate
                                    */
);

/****************************************************************************
 * Reads system display parameters. This routine uses a pointer to the
 * structure UF_DISP_system_params_s.
 *
 * To access parameters related to shaded face edges, please use
 *  UF_VIEW_ask_shaded_edge_options
 * instead.
 *
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_system_params_p_t
 * History:  V12.0 light_source_angles field removed from the structure
 *           V13.0 Added show_shaded_face_edges and hidden_shaded_face_edges
 *           to the structure
 *           V19.0 Added fields use_face_edges_color
 *                              face_edges_color
 *                              hidden_geometry_color
 *                              random_color_displayed
 *                              random_color_object_type
 ****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_system_parameters(
  UF_DISP_system_params_p_t system_parameters  /* <O>
                                               System display parameters
                                               */
);

/****************************************************************************
 * Sets new system display parameters. This routine uses a pointer to the
 * structure.
 *  UF_DISP_system_params_p_t
 *
 * To access parameters related to shaded face edges, please use
 *  UF_VIEW_set_shaded_edge_options
 * instead.
 *
 * Environment: Internal  and  External
 * See Also:
 * History:  V12.0 light_source_angles field removed from the structure
 *           V13.0 Added show_shaded_face_edges and hidden_shaded_face_edges
 *           to the structure
 *           V19.0 Added fields use_face_edges_color
 *                              face_edges_color
 *                              hidden_geometry_color
 *                              random_color_displayed
 *                              random_color_object_type
 ****************************************************************************/
extern UFUNEXPORT int UF_DISP_set_system_parameters(
  UF_DISP_system_params_p_t system_parameters  /* <I>
                                               New system display parameters
                                               */
);

/****************************************************************************
 *     Color Access routines
 *****************************************************************************/

/****************************************************************************
 * Returns the actual number of records currently in the Color Table
 * object of the Display part, including the record for the background
 * color. There must be a part loaded when this function is called.
 *
 * Environment: Internal  and  External
 * See Also:
 * 
 * History:
 *****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_color_count(
           int *count              /* <O>
                                   number of records in the color table object
                                   (includes background color)
                                   */
);

/****************************************************************************
 * Obtains the name and values of the specified color from the Color
 * Table object (CTO) of the Display part. The color values are given
 * using the specified color model.
 * Note that the maximum value permitted for clr_num is the number of
 * records presently in the CTO, minus 1. The number of CTO records
 * may be obtained by calling UF_DISP_ask_color_count. There must be
 * a part loaded when this function is called.
 *
 * Environment: Internal  and  External
 * See Also:
 * 
 * History:
 *****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_color(
         int clr_num ,         /* <I>
                               The number of the color whose name and value
                               are to be returned;
                               Range:  0 .. (# color records in CTO) - 1
                               Note:   0 is for the background color
                               */
         int clr_model ,       /* <I>
                               The color model of the values in clr_values:
                               UF_DISP_rgb_model
                               UF_DISP_hsv_model
                               UF_DISP_hls_model
                               */
         char ** clr_name ,    /* <OF>
                               A pointer to the name of the color.
                               This must be freed by the caller using UF_free
                               */
         double clr_values[3]   /* <O>
                               Three doubles representing the color, where
                               the meaning and range of each value depends on
                                the color model specified:
                rgb:           clr_values[0]:  0.0 <= red <= 1.0
                               clr_values[1]:  0.0 <=green <= 1.0
                               clr_values[2]:  0.0 <= blue <= 1.0
                hsv:           clr_values[0]:  0.0 <= hue <=  360.0
                               clr_values[1]:  0.0 <= saturation <= 1.0
                               clr_values[2]:  0.0 <= value <= 1.0
                hls:           clr_values[0]:  0.0 <= hue <=  360.0
                               clr_values[2]:  0.0 <= light <= 1.0
                               clr_values[1]:  0.0 <= saturation <= 1.0
                               */
);

/****************************************************************************
 * Modifies the name and values of the specified color in the Color Table
 * object (CTO) of the Display part.  The color values are given using
 * the specified color model.
 * Note that the maximum value permitted for clr_num is the number of
 * records presently in the CTO, minus 1.  The number of CTO records
 * may be obtained by calling UF_DISP_ask_color_count. There must be
 * a part loaded when this function is called.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_set_color(
        int clr_num ,         /* <I>
                              The number of the color whose name and value
                               are to be returned;
                              Range:  0 .. (# color records in CTO) - 1
                              Note:   0 is for the background color
                              */
        int clr_model ,       /* <I>
                              The color model of the values in clr_values:
                              UF_DISP_rgb_model
                              UF_DISP_hsv_model
                              UF_DISP_hls_model
                              */
        char * clr_name ,     /* <I>
                              The name of the color;  the character array must
                               be null terminated. The length must not exceed
                              UF_DISP_MAX_NAME_SIZE, as defined in uf_disp.h
                              ignored if clr_num == 0
                              */
        double clr_values[3]  /* <I>
                              Three doubles representing the color, where the
                              meaning and range of each value depends on the
                              color model specified:
              rgb:            clr_values[0]:  0.0 <= red <= 1.0
                              clr_values[1]:  0.0 <=green <= 1.0
                              clr_values[2]:  0.0 <= blue <= 1.0
              hsv:            clr_values[0]:  0.0 <= hue <=  360.0
                              clr_values[1]:  0.0 <= saturation <= 1.0
                              clr_values[2]:  0.0 <= value <= 1.0
              hls:            clr_values[0]:  0.0 <= hue <=  360.0
                              clr_values[2]:  0.0 <= light <= 1.0
                              clr_values[1]:  0.0 <= saturation <= 1.0
                              */
);

/****************************************************************************
 * Determines the color in the Color Table Object (CTO) "closest" to
 * the given color values, based on the specified Color Comparison
 * Method. The index of the closest color is returned.
 * UF_DISP_CCM_EUCLIDEAN_DISTANCE - this method returns the
 * color which is the least Euclidean distance away from the given color
 * in the RGB color cube.
 * Note that the background color is not considered as a candidate.
 * There must be a part loaded when this function is called.
 *
 * Environment: Internal
 * See Also: 
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_closest_color(
           int clr_model ,            /* <I>
                                      The color model of the values in
                                      clr_values;  the following constants are
                                      defined in uf_disp.h:
                                      UF_DISP_rgb_model
                                      UF_DISP_hsv_model
                                      UF_DISP_hls_model
                                      */
           double clr_values[3] ,      /* <I>
                                      Three doubles representing the color,
                                       where the meaning and range of each
                                      value depends on the color model
                                      specified:
                     rgb:             clr_values[0]:  0.0 <= red <= 1.0
                                      clr_values[1]:  0.0 <=green <= 1.0
                                      clr_values[2]:  0.0 <= blue <= 1.0
                     hsv:             clr_values[0]:  0.0 <= hue <=  360.0
                                      clr_values[1]:  0.0 <= saturation <= 1.0
                                      clr_values[2]:  0.0 <= value <= 1.0
                     hls:             clr_values[0]:  0.0 <= hue <=  360.0
                                      clr_values[2]:  0.0 <= light <= 1.0
                                      clr_values[1]:  0.0 <= saturation <= 1.0
                                      */
           int clr_cmp_mtd ,          /* <I>
                                      The Color Comparison Method currently
                                      only UF_DISP_CCM_EUCLIDEAN_DISTANCE
                                      is defined.
                                      */
           int * clr_num              /* <O>
                                      The number of the closest color.
                                      Range:  1 .. (# color records in CTO) - 1
                                      Note:   the background color is not
                                      considered as a candidate.
                                      */
);


/****************************************************************************
 * Returns the index of the color in the color table of the currently
 * displayed part that is most similar to the color indicated by the
 * given color name symbol.
 *
 * If the specified part cannot be found, then the closest color in
 * the default color definition file (CDF) specified by the customer
 * defaults file is returned. If no such file exists, then the closest
 * color in the system color table is returned.
 *
 * Return:
 *     Zero is returned upon successful execution.
 *     Any other return code indicates an error.
 *
 * Environment: Internal and External
 * See Also:
 *  UF_DISP_color_name_t
 *  UF_DISP_ask_closest_color
 *  UF_DISP_ask_closest_color_in_part
 * History: Originally released in NX3.
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_closest_color_in_displayed_part(
    UF_DISP_color_name_t    color_name,   /* <I> symbol for color name */
    int                     *color_index  /* <O> color index of most
                                             similar color             */
);
/****************************************************************************
 * Returns the index of the color in the color table of the specified
 * part that is most similar to the color indicated by the given color
 * name symbol. Parameter object_in_part identifies the part; the
 * parameter can be set to the part tag or the tag of an object in the
 * part.
 *
 * If the specified part cannot be found, then the closest color in
 * the default color definition file (CDF) specified by the customer
 * defaults file is returned. If no such file exists, then the closest
 * color in the system color table is returned.
 *
 * Return:
 *     Zero is returned upon successful execution.
 *     Any other return code indicates an error.
 *
 * Environment: Internal and External
 * See Also:
 *  UF_DISP_color_name_t
 *  UF_DISP_ask_closest_color
 *  UF_DISP_ask_closest_color_in_displayed_part
 * History: Originally released in NX3.
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_closest_color_in_part(
    tag_t                   object_in_part, /* <I> object in part of interest */
    UF_DISP_color_name_t    color_name,     /* <I> symbol for color name      */
    int                     *color_index    /* <O> color index of most
                                               similar color                  */
);



/****************************************************************************
 * Displays a temporary marker. A display refresh erases temporary
 * geometry.
 * Environment: Internal
 * See Also:

 *  UF_OBJ_disp_props_t
 *  UF_DISP_poly_marker_t
 *  UF_DISP_view_type_t
 * History:
****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_temporary_point(
        tag_t view_tag ,                    /* <I>
                                            The tag of the view in which to
                                            display the temporary maker.
                                            */
        UF_DISP_view_type_t which_views ,   /* <I>
                                            The view mode to use.
                                            */
        double markerpos[3] ,               /* <I>
                                            The marker position in absolute
                                            coordinates of the work part
                                            */
        UF_OBJ_disp_props_t * color ,       /* <I>
                                            The color element of the structure.
                                             All other elements of the
                                            structure are ignored.
                                            If color->color = 0, then the
                                             system default color is used.
                                            */
        UF_DISP_poly_marker_t marker_type   /* <I>
                                            The marker type
                                            */
);



/****************************************************************************
 * Displays a temporary line.  A display refresh erases temporary geometry.
 * Environment: Internal
 * See Also:
 *  UF_OBJ_disp_props_t
 *  UF_DISP_view_type_t
 * History:
****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_temporary_line(
     tag_t view_tag ,                      /* <I>
                                           The tag of the view in which the
                                           temporary line is to display.
                                           */
     UF_DISP_view_type_t which_views ,     /* <I>
                                           The view mode to use
                                           */
     double start_line[3] ,                /* <I>
                                           The absolute coordinates of the
                                           start point of the line.
                                           */
     double end_line[3] ,                  /* <I>
                                           The absolute coordinates of the work
                                           part of the end point of the line.
                                           */
     UF_OBJ_disp_props_t * attrib          /* <I>
                                           The color, font, and width elements
                                           of the structure should be set to:
                                           attrib->color = color index
                                           attrib->font = 1 for solid
                                                          2-7, user defined
                                                          0 use system default
                                           attrib->line_width = line width
                                           values in uf_obj.h
                                                      -1 use the default width
                                           */
);

/****************************************************************************
 * Displays a temporary arc. A display refresh erases temporary
 * geometry. The start angle must be less than the end angle and the
 * absolute value of the difference must be less than two pi.
 * Environment: Internal
 * See Also:
 *  UF_OBJ_disp_props_t
 *  UF_DISP_view_type_t
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_temporary_arc(
    tag_t view_tag ,                     /* <I>
                                         The tag of the view in which to
                                         display the temporary arc.
                                         */
    UF_DISP_view_type_t which_views ,    /* <I>
                                         The view mode to use.
                                         */
    double matrix[9] ,                   /* <I>
                                         A matrix for the CSYS in which the
                                         arc exists. Use UF_MTX3_initialize
                                         to create a matrix from X and
                                         Y vectors.
                                         */
    double start_angle ,                 /* <I>
                                         Start angle in radians
                                         */
    double end_angle ,                  /* <I>
                                        End angle in radians.
                                         */
    double arc_center[3] ,              /* <I>
                                        Coordinates are with respect to the
                                        CSYS of the matrix in the work part.
                                        */
    double radius ,                     /* <I>
                                        Radius from the arc center.
                                        */
    UF_OBJ_disp_props_t * attrib        /* <I>
                                        The color, font, and width elements of
                                         the structure should be set to:
                                        attrib->color = color index
                                        attrib->font = 1 for solid
                                                       2-7, user defined
                                                       0 use system default
                                        attrib->line_width = line width values
                                                             in uf_obj.h
                                                             -1 use the default
                                                             width
                                        */
);

/****************************************************************************
 * Displays temporary text. A display refresh erases temporary text. The
 * text is entered in an array and each newline is specified by entering
 * the '\n' character in the text. The text must be null terminated.
 * The text is displayed parallel to the screen.  The size of the text
 * is in the given size (or the system default size) on the screen, and
 * remains at the same size regardless of the view scale.
 * Environment: Internal
 * See Also:
 *  UF_OBJ_disp_props_t
 * 
 *  UF_DISP_view_type_t
 *
 *  UF_DISP_text_ref_t
 * History:  V18.0 Add comments.
****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_temporary_text(
       tag_t view_tag ,                   /* <I>
                                          The tag of the view in which to
                                          display the temporary text.
                                          */
       UF_DISP_view_type_t which_views ,  /* <I>
                                          The view mode to use.
                                          */
       char text[] ,                      /* <I>
                                          Lines of text
                                          */
       double text_coord[3] ,             /* <I>
                                          Position of text box reference point
                                          in absolute coordinates of the displayed
                                          part.
                                          */
       UF_DISP_text_ref_t ref_point ,     /* <I>
                                          Reference point of text box
                                          */
       UF_OBJ_disp_props_t * color ,      /* <I>
                                          The color element of the structure.
                                          All other elements of the structure
                                          are ignored. If color->color = 0,
                                          then the system default color is used.
                                          */
       double char_size ,                 /* <I>
                                          The character size in part units
                                          (Metric or inches).
                                          Used only if software text is used.
                                          If <= 0, then uses system default.
                                          */
       int hardware                       /* <I>
                                          hardware/software flag:
                                            0 = Use hardware font
                                            1 = Use software font
                                          */
);

/*******************************************************************************
 *                       Model Bounds access routines
 *****************************************************************************/

/*******************************************************************************
 * Returns the model bounds of the work part. Each part should contain
 * exactly one "model bounds object" which ideally contains a 3D box in
 * absolute space inside of which is all of the geometry of the work part.
 * NOTE: In general, the model bounds returned by this function are
 * NOT accurate, as NX does not usually update the model bounds as
 * objects are created, modified, and deleted. This function is intended
 * for use by certain NX applications such as translators which know that
 * their application has earlier computed model bounds which are still
 * known to be valid.
 * Environment: Internal  and  External
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_model_bounds(
   const tag_t model_bounds_obj ,    /* <I>
                                     The tag of the Model Bounds object of the
                                     work part. Use
                                     UF_DISP_ask_model_bounds_tag to find this
                                     tag.
                                     */
   double model_bounds[6]            /* <O>
                                     The model bounds of the work part.  The
                                     six values are
                                     (Minimum_X, Maximum_X, Minimum_Y,
                                      Maximum_Y, Minimum_Z, Maximum_Z)
                                      */
);

/*******************************************************************************
 * Returns the model bounds tag of the work part. Each part should
 * contain exactly one "model bounds object" which ideally contains a
 * 3D box in absolute space inside of which is all of the geometry of the
 * work part.
 * Environment: Internal  and  External
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_model_bounds_tag(
            tag_t * model_bounds_object  /* <O>
                                         The tag of the Model Bounds object of
                                         the work part. If the work part has
                                         no model bounds object (which is an
                                         abnormal condition), NULL_TAG is
                                         returned.
                                         */
);

/*******************************************************************************
 * Computes the model bounds for the work part. The model bounds
 * defines a box in Absolute coordinates which contains all of the
 * potentially displayable geometry of the part. The sides of the box are
 * parallel to the axes of the absolute coordinate system. Objects which
 * are not currently displayable, because they are blanked or on an
 * invisible layer, are still included within the model bounds.
 * If there are no displayable objects in the part, bounds_computed will
 * be FALSE, and model_bounds will contain default bounds, which are
 * the size of the current graphics in X and Y, with Z the same as the
 * smaller of X and Y.
 * NOTE: This function is of limited value for most NX Open API
 * application developers. It is intended to be used by certain NX
 * applications such as translators.
 * Environment: Internal  and  External
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_compute_model_bounds (
    logical  *bounds_computed, /* <O> TRUE if there are some displayable
                                objects in the work part, so that normal
                                model bounds were computed.  FALSE if the
                                work part has no displayable objects        */
    double   model_bounds[6]   /* <O>
                                  The model bounds for the work part.
                                  This is a box in absolute space, whose sides
                                  are parallel to the axes of the absolute
                                  coordinate system.  The six values of the
                                  array are the Minimum_X, Maximum_X,
                                  Minimum_Y, Maximum_Y, Minimum_Z and
                                  Maximum_Z of the box.  If bounds_computed
                                  is FALSE, default bounds are returned.
                                  The default bounds are roughly the size
                                  of the current graphics window. */
);

/*******************************************************************************
 * Stores the given model bounds into the one and only model bounds
 * object for the work part. The given tag must be that of the model
 * bounds object.
 * NOTE: This function is of limited value for most NX Open API
 * application developers. It is intended to be used by certain NX
 * applications such as translators.
 * Environment: Internal  and  External
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_set_model_bounds(
   const tag_t model_bounds_object ,   /* <I>
                                       The tag of the Model Bounds object of
                                       the work part.   You will have received
                                       this from a prior call to
                                       UF_DISP_ask_model_bounds_tag
                                       */
   const double model_bounds[6]        /* <I>
                                       The model bounds of the current work
                                       part.  The six values are
                                       (Minimum_X, Maximum_X, Minimum_Y,
                                        Maximum_Y, Minimum_Z, Maximum_Z).
                                       You probably have determined these
                                       bounds in a prior call to
                                       UF_DISP_compute_model_bounds.
                                       */
);

/******************************************************************************
 *     Surface Analysis routines
 *****************************************************************************/

/******************************************************************************
 * Reads the face analysis display parameters into the supplied
 * UF_DISP_srfanl_data_t structure. This routine uses a pointer to the
 * structure UF_DISP_srfanl_data_s.
 * Environment: Internal
 * See Also:
 * History:
*****************************************************************************/
extern UFUNEXPORT int  UF_DISP_ask_srfanl_params(
      UF_DISP_srfanl_data_t * params  /* <O>
                                      Face analysis display parameters
                                      */
);

/******************************************************************************
 * Sets the face analysis display parameters. This routine uses a pointer
 * to the structure UF_DISP_srfanl_data_s.
 *
 * Environment: Internal
 * See Also:
 *  UF_DISP_srfanl_data_t
 * History:
*****************************************************************************/
extern UFUNEXPORT int UF_DISP_set_srfanl_params(
     UF_DISP_srfanl_data_t * params  /* <O>
                                     New system display parameters
                                     */
);



/****************************************************************************
 * Displays a User Defined Object arc. The arc is drawn from the  start
 * angle to the end angle in a counter clockwise manner.  This routine
 * may only be called from a UDO registered callback routine.  The
 * context argument passed into this routine will be passed from NX
 * to the UDO callback routine.
 *
 * Environment: Internal  and  External
 * See Also:
 *  UF_UDOBJ_register_display_cb
 *  UF_UDOBJ_register_fit_cb
 *  UF_UDOBJ_register_attn_pt_cb
 *  UF_UDOBJ_register_select_cb
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_arc(
    double matrix[9],          /* <I> A matrix for the CSYS in which the arc
                               exists. Use UF_MTX3_initialize to create a matrix
                               from X and Y vectors */
    double start_angle,        /* <I> Start angle expressed in radians */
    double end_angle,          /* <I> End angle expressed in radians. The start
                                angle must be less than the end angle and the
                               difference between the two must be less than
                               2 PI
                               */
    double arc_center[3],      /* <I> Coordinates in arc coordinates system
                               CSYS
                               */
    double radius,             /* <I>
                               Radius from the arc_center
                               */
    void *context              /* <I/O> A private context pointer obtained
                               from the callback
                               */
);

/****************************************************************************
 * Displays a User Defined Object circle which can be solid filled. This
 * routine may only be called from a UDO registered callback routine.  The
 * context argument passed into this routine will be passed from NX
 * to the UDO callback routine.
 *
 * Environment: Internal  and  External
 * See Also:
 *  UF_UDOBJ_register_display_cb
 *  UF_UDOBJ_register_fit_cb
 *  UF_UDOBJ_register_attn_pt_cb
 *  UF_UDOBJ_register_select_cb
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_circle(
    double matrix[9] ,            /* <I>
                                  A matrix for the CSYS in which the circle
                                  exists.  Use UF_MTX3_initialize to create a
                                  matrix from X and Y vectors.
                                  */
     double circle_center[3] ,    /* <I>
                                  Circle's center coordinates (x, y, and z)
                                  from the CSYS in which the circle exists
                                  (see the matrix[9] argument).
                                  */
     double radius ,              /* <I>
                                  Radius from the circle_center
                                  */
     logical filled ,             /* <I>
                                  TRUE = Solid fill the circle's interior
                                  FALSE =  Circle's interior not filled
                                  */
     void * context               /* <I/O>
                                  A private context pointer obtained from the
                                  callback.
                                  */
);


/****************************************************************************
 * Displays a User Defined Object polyline which is a connected set of
 * line segments.  This routine may only be called from a UDO registered
 * callback routine.  The context argument passed into this routine will be
 * passed from NX to the UDO callback routine.
 *
 * Environment: Internal  and  External
 * See Also:
 *  UF_UDOBJ_register_display_cb
 *  UF_UDOBJ_register_fit_cb
 *  UF_UDOBJ_register_attn_pt_cb
 *  UF_UDOBJ_register_select_cb
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_polyline(
       double * poly_points ,       /* <I,len:num_points>
                                    An array of absolute coordinates which
                                    represent a connected set of line segments.
                                    */
       int num_points ,             /* <I>
                                    The number of points in the poly_points
                                    array.
                                    */
       void * context               /* <I/O>
                                    A private context pointer obtained from
                                    the callback.
                                    */
);

/****************************************************************************
 * Displays User Defined Object points. This routine may only be called from
 * a UDO registered callback routine.  The context argument passed into this
 * routine will be passed from NX to the UDO callback routine.
 *
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_poly_marker_t
 *  UF_UDOBJ_register_display_cb
 *  UF_UDOBJ_register_fit_cb
 *  UF_UDOBJ_register_attn_pt_cb
 *  UF_UDOBJ_register_select_cb
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_points(
 double * points ,                 /* <I,len:num_points> num_points
                                    An array of point coordinates.
                                    */
 int num_points ,                   /* <I>
                                    The number of points in the points array.
                                    */
 UF_DISP_poly_marker_t marker_type ,/* <I>
                                    The type of marker to be displayed.
                                    */
 void * context                     /* <I/O>
                                    A private context pointer obtained from the
                                    callback.
                                    */
);

/****************************************************************************
 * Displays a closed User Defined Object polygon and may be solid
 * filled. The polygon must be planar and convex when using the filled option.
 * This routine may only be called from a UDO registered callback routine.
 * The context argument passed into this routine will be passed from
 * NX to the UDO callback routine.
 * NOTE: A polygon is convex if a line joining any two interior
 * points of the polygon lies completely inside the polygon
 * Environment: Internal  and  External
 * See Also:
 *  UF_UDOBJ_register_display_cb
 *  UF_UDOBJ_register_fit_cb
 *  UF_UDOBJ_register_attn_pt_cb
 *  UF_UDOBJ_register_select_cb
 * History:
****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_polygon(
            double * points ,       /* <I,len:num_points> num_points
                                    An array of coordinates resulting in a
                                    closed polygon.
                                    */
            int num_points ,        /* <I>
                                    The number of points in the points array.
                                    */
            logical filled ,        /* <I>
                                    TRUE = Solid fill polygon's interior.
                                    FALSE = Do not fill polygon's interior
                                    */
            void * context          /* <I/O>
                                    A private context pointer obtained from
                                    the callback.
                                    */
);


/****************************************************************************
 * Displays User Defined Object text which rotates with the view. The
 * text is entered in an array and each newline is specified by entering
 * the '\n' character in the text.  The text must be null terminated.  For
 * example, "Hello \n World!".  This routine may only be called from a
 * UDO registered callback routine.  The context argument passed into this
 * routine will be passed from NX to the UDO callback routine.
 * The text is drawn using the character size found in the Annotations
 * Preference dialog, under Lettering, General.  This size may be changed
 * by UF_DRF_set_preferences, setting mpr[4] to the desired size.
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_text_ref_t
 *  UF_UDOBJ_register_display_cb
 *  UF_UDOBJ_register_fit_cb
 *  UF_UDOBJ_register_attn_pt_cb
 *  UF_UDOBJ_register_select_cb
 * History:
****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_text(
      char text[] ,             /* <I>
                                Lines of text
                                */
      double text_coord[3] ,    /* <I>
                                Position of text box reference point in
                                absolute coordinates.
                                */
UF_DISP_text_ref_t ref_point ,  /* <I>
                                Reference point of text box
                                */
      void * context            /* <I/O>
                                A private context pointer obtained from
                                the callback.
                                */
);

/****************************************************************************
 * Displays User Defined Object facets. This routine may only be called from a
 * UDO registered callback routine.  The context argument passed into this
 * routine will be passed from NX to the UDO callback routine.
 *
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_facet_p_t
 *  UF_DISP_facet_type_t
 *  UF_UDOBJ_register_display_cb
 *  UF_UDOBJ_register_fit_cb
 *  UF_UDOBJ_register_attn_pt_cb
 *  UF_UDOBJ_register_select_cb
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_DISP_display_facets(
    UF_DISP_facet_p_t facets ,      /* <I,len:num_facets>
                                    An array of facets.
                                    */
    int num_vertices ,              /* <I>
                                    The number of vertices in one facet.
                                    */
    int num_facets ,                /* <I>
                                    The number of facets in the facet array.
                                    */
UF_DISP_facet_type_t type_of_facet ,/* <I>
                                    The format of the facet in the facet array.
                                    */
    void * context                  /* <I/O>
                                    A private context pointer obtained from the
                                    callback.
                                    */
);

/****************************************************************************
 * Inquires the context pointer and returns information about display,
 * selection, fit, and attention point information in the output structure.
 * This function can be called prior to displaying geometry, after
 * geometry is displayed, or both.  This routine may only be called from a
 * UDO registered callback routine.  The context argument passed into this
 * routine will be passed from NX to the UDO callback routine.
 *
 * NOTE: All values in the inquiry structure are set to NULL or FALSE by this function
 *     except for the following:
 *     If this routine is being called from the attention point callback the
 *     is_attn_pt_valid field is set to TRUE.
 *     If this routine is being called from the fit callback only the view_tag is set.
 *     If this routine is being called from the display callback,
 *     the view_tag, is_draw_open_disp, is_view_mode_valid, and view_mode fields
 *     are set.
 *
 *
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_inquire_p_t
 *  UF_UDOBJ_register_display_cb
 *  UF_UDOBJ_register_fit_cb
 *  UF_UDOBJ_register_attn_pt_cb
 *  UF_UDOBJ_register_select_cb
 * History: Modified in V17 to return the view tag
 ****************************************************************************/
extern UFUNEXPORT int  UF_DISP_ask_display_context(
            void * context ,             /* <I>
                                         The private context pointer obtained
                                         from the callback.
                                         */
            UF_DISP_inquire_p_t inquiry  /* <O>
                                         The inquiry structure.
                                         */
);

/*****************************************************************************
 *
 *                 Work Plane Emphasis prototypes follow
 *
 *****************************************************************************/

/*******************************************************************************
 * Queries the current work plane emphasis setting. When work plane emphasis
 * is on, objects that do not lie on the work plane appear de-emphasized, in
 * which the object color is blended with the De-emphasis Blend Color according
 * to the De-emphasis Blend Percentage. A de-emphasized object is unselectable
 * unless the work plane emphasis selection filter is overridden. Work plane
 * emphasis is a session dependent value; it is not saved with any part.
 *
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_set_work_plane_emphasis
 *  UF_DISP_ask_work_plane_sel
 * UF_DISP_set_work_plane_sel
 * 
 * History: Original release was in V13.0.

 ******************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_work_plane_emphasis(
                    int * emphasis         /* <O>
                                           Emphasis setting. Must be one of:
                                           UF_DISP_WORK_PLANE_EMPHASIS_ON, or
                                           UF_DISP_WORK_PLANE_EMPHASIS_OFF
                                           */
);

/*******************************************************************************
 * Sets work plane emphasis on or off. When work plane emphasis is on,
 * objects that do not lie on the work plane appear de-emphasized, in
 * which the object color is blended with the De-emphasis Blend Color 
 * according to the De-emphasis Blend Percentage. A de-emphasized object 
 * is unselectable unless the work plane emphasis selection filter is 
 * overridden. Work plane emphasis is a session dependent value; it is 
 * not saved with any part.
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_ask_work_plane_emphasis
 *  UF_DISP_ask_work_plane_sel
 * UF_DISP_set_work_plane_sel
 * History: Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_DISP_set_work_plane_emphasis(
                   int emphasis            /* <I>
                                           Emphasis setting. Must be either:
                                           UF_DISP_WORK_PLANE_EMPHASIS_ON, or
                                           UF_DISP_WORK_PLANE_EMPHASIS_OFF
                                           */
);

/******************************************************************************
 * Queries the value of the selection override for work plane emphasis.
 * When work plane emphasis is enabled and the selection override is
 * equal to UF_DISP_SELECT_WORK_DIMMED, no objects are
 * filtered out of selection because they are off the work plane.
 * When work plane emphasis is enabled and the selection override is
 * equal to UF_DISP_NO_SELECT_WORK_DIMMED, no objects
 * dimmed for work plane emphasis are selectable.
 * When work plane emphasis is disabled, the selection override setting
 * has no affect although it can be changed. The selection override
 * setting takes effect once work plane emphasis is enabled.
 * The work plane emphasis selection override is a session dependent
 * value; it is not saved with any part.
 *
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_set_work_plane_emphasis
 *  UF_DISP_ask_work_plane_emphasis
 * UF_DISP_set_work_plane_sel
 * History: Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_work_plane_sel(
                  int * override       /* <O>
                                       Emphasis selection override setting.
                                       Must be either:
                                       UF_DISP_SELECT_WORK_DIMMED, or
                                       UF_DISP_NO_SELECT_WORK_DIMMED
                                       */
);

/*******************************************************************************
 * Sets (or unsets) the work plane emphasis selection override.
 * When work plane emphasis is enabled and the selection override is
 * set to UF_DISP_SELECT_WORK_DIMMED, no objects are filtered
 * out of selection because they are off the work plane.
 * When work plane emphasis is enabled and the selection override is
 * set to UF_DISP_NO_SELECT_WORK_DIMMED, no objects
 * dimmed for work plane emphasis are selectable.
 * When work plane emphasis is disabled, the selection override setting
 * has no affect although it can be changed. The selection override
 * setting takes effect once work plane emphasis is enabled.
 * The work plane emphasis selection override is a session dependent
 * value; it is not saved with any part.
 *
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_ask_work_plane_emphasis
 * UF_DISP_set_work_plane_emphasis
 *  UF_DISP_ask_work_plane_sel
 * History: Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_DISP_set_work_plane_sel(
              int override            /* <I>
                                      Emphasis selection override setting.
                                      Must be either:
                                      UF_DISP_SELECT_WORK_DIMMED, or
                                      UF_DISP_NO_SELECT_WORK_DIMMED
                                      */
);

/*******************************************************************************
 * Queries the work plane emphasis dim color attribute, which is obsolete
 * in NX 6.0. The function accesses the De-emphasis Blend Color instead.
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_ask_work_plane_emphasis
 *  UF_DISP_set_work_plane_emphasis
 *  UF_DISP_ask_work_plane_sel
 * UF_DISP_set_work_plane_sel
 * UF_DISP_set_work_plane_dim_clr
 *  
 * History: Original release was in V13.0. 
 *          Modified in NX 6.0 to access the De-emphasis Blend Color.
 ******************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_work_plane_dim_clr(
                       int * color        /* <O> Emphasis dim color. */
);

/*******************************************************************************
 * Sets the work plane emphasis dim color attribute, which is obsolete
 * in NX 6.0. The function accesses the De-emphasis Blend Color instead.
 * Environment: Internal  and  External
 * See Also:
 *  UF_DISP_ask_work_plane_emphasis
 *  UF_DISP_set_work_plane_emphasis
 *  UF_DISP_ask_work_plane_sel
 * UF_DISP_set_work_plane_sel
 * UF_DISP_ask_work_plane_dim_clr
 * 
 * History: Original release was in V13.0.
 *          Modified in NX 6.0 to access the De-emphasis Blend Color.
 ******************************************************************************/
extern UFUNEXPORT int UF_DISP_set_work_plane_dim_clr(
                        int dim_color     /* <I> Emphasis dim color.  */
);

/******************************************************************************
 * Creates a Windows Enhanced Metafile of the image in the
 * NX graphics window.  This function is available only
 * on Windows NT.  Calling it on any other platform will result
 * in an error being returned.   There are options to export the
 * Enhanced Metafile to the clipboard or to a device context. This is
 * similar to exporting a plot file or a CGM file of the current display.
 * Any views which are in Shaded, Partially Shaded, or in Face Analysis
 * mode are treated as if they were in Wireframe mode.
 * The Enhanced Metafile will be created using part colors and a single
 * (standard thin) line width value.
 * The size of the image in the generated Enhanced Metafile is the same
 * as that of the current graphics window. Therefore, you may wish to
 * resize the graphics window to the desired size prior to invoking this
 * function. When in External mode, the size of the graphics window is
 * the size the last time the part was saved.
 * The output Enhanced Metafile does not include the Work Coordinate
 * System, the grid, nor any temporary display.
 * You can only use the UF_DISP_WMF_TO_CLIPBOARD option
 * when in Internal mode. If you use this option in External mode, this
 * function returns an error code.
 * Environment: Internal  and  External
 * See Also:
 * History: Original release was in V14.0.
******************************************************************************/
extern UFUNEXPORT int UF_DISP_export_windows_metafile(
     UF_DISP_wmf_output_t output_type ,    /* <I>
                                           Specifies where the output Enhanced
                                           Metafile should be written:
                                           UF_DISP_WMF_TO_CLIPBOARD writes
                                           directly to the Windows clipboard.
                                           This is not available in external
                                           NX Open programs.
                                           UF_DISP_WMF_TO_FILE uses the
                                           following file_spec to output the
                                           metafile data to.
                                           */
     char * file_spec                      /* <I>
                                           The file specification of the file
                                           to create. This parameter is used
                                           only when the output_type is
                                           UF_DISP_WMF_TO_FILE.
                                           This file specification must be at
                                           most MAX_FSPEC_SIZE characters.
                                           */
);

/****************************************************************************
  Returns the data that affects drawing monochrome display.
  This routine MUST be called to populate the data structure, before
  UF_DISP_set_drawing_display is called.

  Please reference ufd_disp.c to review a sample execution of this function.

  Return: UF_err_program_not_initialized
  Environment: Internal  and  External
  See Also:
   UF_DISP_drawing_display_data_t
  History: None
****************************************************************************/
extern UFUNEXPORT int  UF_DISP_ask_drawing_display(
            UF_DISP_drawing_display_data_p_t drawing_display  /* <O>
                                         The drawing monochrome display structure.
                                         */
);

/****************************************************************************
  Update the data that affects drawing monochrome display.
  The routine UF_DISP_ask_drawing_display MUST be called to
  populate the data structure, before this routine is called.

  Please reference ufd_disp.c to review a sample execution of this function.

  Return: UF_err_program_not_initialized, UF_err_bad_parameter_number_1
  Environment: Internal  and  External
  See Also:
   UF_DISP_drawing_display_data_t
  History: None
****************************************************************************/
extern UFUNEXPORT int  UF_DISP_set_drawing_display(
            UF_DISP_drawing_display_data_p_t drawing_display  /* <I>
                                         The drawing monochrome display structure.
                                         */
);


/******************************************************************************
 * Queries the information about the grid in the designated application
 * context. The 'product_context' variable must be set.
 *
 * product_context - either  UF_DISP_SKETCH_GRID for sketcher application,
 *                   or      UF_DISP_DRAWING_GRID for drawing,
 *                   or      UF_DISP_SHED_GRID for True Shading display,
 *                   or      UF_DISP_MODEL_GRID for others (or default).
 *
 * Environment:  Internal and External
 *
 * See Also:
 *   UF_DISP_set_grid_parameters
 *   UF_DISP_activate_grid
 *   UF_DISP_deactivate_grid
 *   UF_DISP_ask_current_grid_context
 *
 * History: Originally released in V19.0
 *
 ******************************************************************************/
extern UFUNEXPORT void UF_DISP_ask_grid_parameters (
    UF_DISP_grid_context_t   product_context, /* <I> either
                                                 UF_DISP_SKETCH_GRID or
                                                 UF_DISP_DRAWING_GRID or
                                                 UF_DISP_MODEL_GRID or
                                                 UF_DISP_SHED_GRID
                                               */
    UF_DISP_grid_p_t         output_grid      /* <O> a grid structure */
);/*<NEC>*/

/******************************************************************************
 * Sets up the information for the grid in the designated application
 * context. Any field not set will have a default value provided.
 *
 * product_context - either  UF_DISP_SKETCH_GRID for sketcher application,
 *                   or      UF_DISP_DRAWING_GRID for drawing,
 *                   or      UF_DISP_SHED_GRID for True Shading display,
 *                   or      UF_DISP_MODEL_GRID for others (or default).
 *
 * Environment:  Internal and External
 *
 * See Also:
 *   UF_DISP_ask_grid_parameters
 *   UF_DISP_activate_grid
 *   UF_DISP_deactivate_grid
 *   UF_DISP_ask_current_grid_context
 *
 * History: Originally released in V19.0
 *
 ******************************************************************************/
extern UFUNEXPORT void UF_DISP_set_grid_parameters (
    UF_DISP_grid_context_t   product_context, /* <I> either
                                                 UF_DISP_SKETCH_GRID or
                                                 UF_DISP_DRAWING_GRID or
                                                 UF_DISP_MODEL_GRID or
                                                 UF_DISP_SHED_GRID
                                               */
    UF_DISP_grid_p_t         input_grid       /* <I> a polulated grid structure */
);/*<NEC>*/

/******************************************************************************
 *
 * This causes the grid to be display immediately instead of waiting for a
 * system determined regeneration (at more opportune time). However, trying
 * to activate a grid in the wrong context will not work. For example, a drawing
 * grid cannot be displayed in the Modeling application context.
 *
 * product_context - either  UF_DISP_SKETCH_GRID for sketcher application,
 *                   or      UF_DISP_DRAWING_GRID for drawing,
 *                   or      UF_DISP_SHED_GRID for True Shading display,
 *                   or      UF_DISP_MODEL_GRID for others (or default).
 *
 * Environment:  Internal and External
 *
 * See Also:
 *   UF_DISP_ask_grid_parameters
 *   UF_DISP_set_grid_parameters
 *   UF_DISP_deactivate_grid
 *   UF_DISP_ask_current_grid_context
 *
 * History: Originally released in V19.0
 *
 ******************************************************************************/
extern UFUNEXPORT void UF_DISP_activate_grid (
    UF_DISP_grid_context_t   product_context  /* <I> either
                                                 UF_DISP_SKETCH_GRID or
                                                 UF_DISP_DRAWING_GRID or
                                                 UF_DISP_MODEL_GRID or
                                                 UF_DISP_SHED_GRID
                                               */
);/*<NEC>*/

/******************************************************************************
 *
 * This is mainly called when existing from a 'task' environment (eg. Sketcher)
 * This causes the grid to be removed from display. In general, if switching
 * from one application to another this call is not necessary because the DSS
 * subsystem manages all this. However, in a task environment, existing the
 * environment doesn't always cause display regeneration. Therefore, it is a
 * good 'house keeping' practice to call this when another grid is expected to
 * be restored when existing from the current task environment.
 *
 * product_context - either  UF_DISP_SKETCH_GRID for sketcher application,
 *                   or      UF_DISP_DRAWING_GRID for drawing,
 *                   or      UF_DISP_SHED_GRID for True Shading display,
 *                   or      UF_DISP_MODEL_GRID for others (or default).
 * restore_prev_context_grid - TRUE  to assure a proper display regeneration
 *                             FALSE, if you don't care
 *
 * Environment:  Internal and External
 *
 * See Also:
 *   UF_DISP_ask_grid_parameters
 *   UF_DISP_set_grid_parameters
 *   UF_DISP_activate_grid
 *   UF_DISP_ask_current_grid_context
 *
 * History: Originally released in V19.0
 *
 ******************************************************************************/
extern UFUNEXPORT void UF_DISP_deactivate_grid (
    UF_DISP_grid_context_t   product_context, /* <I> either
                                                 UF_DISP_SKETCH_GRID or
                                                 UF_DISP_DRAWING_GRID or
                                                 UF_DISP_MODEL_GRID or
                                                 UF_DISP_SHED_GRID
                                               */
    logical                  restore_prev_context_grid /* <I> either
                                                          TRUE or
                                                          FALSE
                                                        */
);/*<NEC>*/

/******************************************************************************
 * This function returns the current application for task environment
 *
 * return - either      UF_DISP_SKETCH_GRID for sketcher application,
 *          or          UF_DISP_DRAWING_GRID for drawing,
 *          or          UF_DISP_SHED_GRID for True Shading display,
 *          or          UF_DISP_MODEL_GRID for others (or default).
 *          or          UF_DISP_NULL_GRID if no grid is setup yet
 *
 * Environment:  Internal and External
 *
 * See Also:
 *   UF_DISP_ask_grid_parameters
 *   UF_DISP_set_grid_parameters
 *   UF_DISP_activate_grid
 *   UF_DISP_deactivate_grid
 *
 * History: Originally released in V19.0
 *
 ******************************************************************************/
extern UFUNEXPORT UF_DISP_grid_context_t UF_DISP_ask_current_grid_context (
    void
);/*<NEC>*/

/******************************************************************************
 * This function returns the material tag and name of the material assigned to
 * the object defined by object_tag.
 * The object_tag is limited to these types: UF_solid_type, UF_solid_face_subtype
 * and UF_faceted_model_type.
 *
 * Environment: Internal and External
 * See Also: 
 * History: This function is created for NX3 QRM.
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_ask_material(
    const tag_t object_tag ,       /* <I> The tag of the object.              */
    tag_p_t material_tag,          /* <O> The tag of material that is assigned
                                          to the specified object.            */
    char * material_name           /* <O> The name of the material that is    */

);

/*******************************************************************************************
 * This function returns ERROR_OK or zero if either                                        
 *   a material in the Materials in Part Palette is selected or                           
 *   a material in the Materials Library is selected depending which was selected lastly. 
 * If material selected is from the Materials in Part palette, then both material_tag and 
 * material_full_archive_name will be returned.  If the material selected is from         
 * the Materials library, then only material_full_archive_name will be returned.         
 * The function also returns the material source of UF_DISP_material_source_t type.     
 * This can be used to determine which of UF_DISP_ask_work_part_material_lwa_user_area_data
 * or UF_DISP_ask_library_material_lwa_user_area_data to call to find the                 
 * LWA (LightWork Archive) user area data.                                                              
 * If no material is found selected, non-zero is returned.                              
 * Environment: Internal only                                                          
 * History: This function is created for NX604.                                       
 *******************************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_currently_selected_material(
    UF_DISP_material_source_t *material_source, /* <O> UF_DISP_lw_material_in_Materials_Library or UF_DISP_lw_material_in_Materials_in_Part_Palette*/
    tag_t * material_tag,                       /* <O> The tag of material that is currently selected in the Materials in Part Palette*/
    char  * material_full_archive_name          /* <O> The full_arachive_name of the material currently selected in the Materials in part 
                                                   palette or the Materials Library*/
);

/*******************************************************************************************
 * This function returns the LWA user area data based on the material tag and the  
 * specification_attribute_string_key.                                                    
 * If the specified data is found from the LWA user area data, ERROR_OK or 0 is returned. 
 * Environment: Internal only                                                            
 * History: This function is created for NX604.                                         
 *******************************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_work_part_material_lwa_user_area_data(
    tag_t material_tag,                 /* <I> the tag of the material to get the lwa user area data */
    const char * attribute_string_key,  /* <I> key to identify which data in the lwa user data area to get 
                                               NOTE max key length is 31 */
    const char ** attribute_data        /* <O> return the user area data specified by the attribute_string_key*/
);

/*******************************************************************************************
 *  This function returns the LWA user area data based on the material_full_archive_name and the
 *  specification_attribute_string_key.                                                    
 *  If the specified data is found in the LWA user area data, ERROR_OK or 0 is returned.   
 * Environment: Internal only                                                            
 * History: This function is created for NX604.                                         
 *******************************************************************************************/
extern UFUNEXPORT int UF_DISP_ask_library_material_lwa_user_area_data(
    char * material_full_archive_name,  /* <I> the full archive_name of the material to get lwa user area data*/ 
    const char * attribute_string_key,  /* <I> key to identify which data in the lwa user data area to get */
    const char ** attribute_data        /* <O> return the user area data specified by the attribute_string_key*/
);

/******************************************************************************
 * This function returns the texture space information required for the
 * specified material.
 * For certain material texture (e.g., logos), texture space information is
 * required to describe how to place the texture on a body so the texture image
 * or pattern will appear correctly on the model (orientation, position and
 * scale).  If texture space information is not found for the material
 * (e.g., for non-textured mateirals, such as metals), ts_info_defined will
 * be set to 0 and no texture space information will be returned.
 *
 * Environment: Internal and External
 * See Also: 
 * History: This function is created for NX3 QRM.
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_ask_texture_space_info(
    tag_t material_tag,           /* <I> tag of material to request texture
                                         space information for. */
    UF_DISP_texture_space_info_t * ts_info_ptr,  /* <O> texture space information */
    int *ts_info_defined /* <O> value of 1 is returned if texture space information is returned */
);

/*****************************************************************************
* This function creates a new material based on an existing material
* attributes defined by the given material tag.
* Environment: Internal and External
* See Also: 
* History: This function is created for NX3 QRM.
*****************************************************************/
extern UFUNEXPORT int UF_DISP_copy_material(
    const tag_t material_tag,      /* <I> The tag of material that the new
                                       material is copied from.               */
    tag_t * new_material_tag,      /* <O> new material tag                    */
    char * new_material_name       /* <O> The name of the newly copied material*/
);


/***********************************************************************************
 * This function allows user to set new texture space information of the material.
 *
 *
 * Environment: Internal and External
 * See Also: 
 * History: This function is created for NX3 QRM.
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_set_texture_space_info(
    const tag_t material_tag,           /* <I> tag of material                    */
    UF_DISP_texture_space_info_t * ts_info_ptr  /* <I> new texture space information  */
);



/******************************************************************************
 * This function assigns the material to object
 * NOTE object types accepted include: UF_solid_type, UF_solid_face_subtype
 * and UF_faceted_model_type.
 *
 * Environment: Internal and external
 * See Also: 
 * History: This function is created for NX3 QRM.
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_assign_material(
    const tag_t material_tag, /* <I> The tag of the material to assign to object */
    const tag_t object_tag    /* <I> The tag of object to assign the material to */
);

/******************************************************************************
*
* This function deletes the material specified by the material_tag
*
* Environment: Internal and external
* See Also: 
* History: This function is created for NX3 QRM.
 *****************************************************************/

extern UFUNEXPORT int UF_DISP_delete_material(
    const tag_t material_tag       /* <I> The tag of material to be deleted   */
);

/******************************************************************************
 * This function updates the display of the given geometry objects  
 * in Studio rendering style.
 *
 * The display of UF_solid_type, UF_solid_face_subtype and UF_faceted_model_type
 * are updated.  All other object types are ignored.
 *
 *
 * Environment: Internal
 * See Also: 
 * History: This function is created for NX7.5.2 QRM.
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_update_material_display_of_geometry(
    const int       object_count, /* <I> The number of objects in the object_list    */
    const tag_p_t   object_list   /* <I> The tags of objects with material applied to */
);

/******************************************************************************
 * This function returns a list of geometry object tags that are associated to  
 * the given material tag. 
 *
 * The object_tags are limited to these types: UF_solid_type, UF_solid_face_subtype
 * and UF_faceted_model_type.
 *
 * Environment: Internal
 * See Also: 
 * History: This function is created for NX7.5 QRM.
 *****************************************************************/
extern UFUNEXPORT int UF_DISP_ask_geometry_of_material(
    const tag_t material_tag,   /* <I>  The tag of material that is 
                                        assigned to the returned objects.  */
    int         *object_count,  /* <O>  Number of objects found            */
    tag_p_t     *object_tags    /* <OF> A pointer to a list of geometry object tags
                                        associated to the given material.  */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif    /*  END  UF_DISP_INCLUDED  */
