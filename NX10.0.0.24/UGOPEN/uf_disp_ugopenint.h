/*****************************************************************************

        Copyright 2000 Siemens Product Lifecycle Management Software Inc. 
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
routine once from an Open API program.  You can control which operation the 
routine participates in by selectively registering an Open API program using 
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

#ifndef UF_DISP_UGOPENINT_INCLUDED 
#define UF_DISP_UGOPENINT_INCLUDED 

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_disp_types.h>
#include <libugopenint_exports.h>

#ifdef __cplusplus
extern "C" {
#endif
    
/* 
     Function prototypes 
*/

/*****************************************************************
 * Export a PNG/JPEG/TIFF/GIF/XWD/BMP full window area image
 * Creates an image file with the file type you specify using the image
 * currently displayed in the graphics window.
 *
 * Return:
 *  Return code:
 *        = 0 No error
 *        = not 0 Error code, including:
 *                UF_DISP_err_failed_to_create_image_file
 *                Standard UF error codes
 *                
 * Environment: Internal
 * See Also: 
 * History: Original release was in V13.0.
 *****************************************************************/
extern UGOPENINTEXPORT int UF_DISP_create_image(
 char* filename ,                  /* <I>
                                   Name of output image file
                                   */
 UF_DISP_image_format_t format ,   /* <I>
                                   Image type to produce:
                                   UF_DISP_PNG
                                   UF_DISP_JPEG
                                   UF_DISP_TIFF
                                   UF_DISP_COMPRESSED_TIFF
                                   UF_DISP_GIF
                                   UF_DISP_XWD (Only on UNIX workstations)
                                   UF_DISP_BMP (Only on Windows workstations)
                                   */
 UF_DISP_background_color_t color  /* <I>
                                   Back ground color:
                                   UF_DISP_ORIGINAL
                                   UF_DISP_WHITE
                                   */
);

/*****************************************************************
 * Creates an image file with the file type and rectangular frame you
 * specify using the image currently displayed in the graphics window.
 * Export a PNG/JPEG/TIFF/GIF/XWD/BMP full window or rectangular area image
 * Full window image: set width and height to zero
 * Rectangular area image: set width, height greater than zero and set
 * upper left point window coordinate
 *
 * Return:
 *  Return code:
 *        = 0 No error
 *        = not 0 Error code, including:
 *                UF_DISP_err_failed_to_create_image_file
 *                Standard UF error codes
 *                
 * Environment: Internal
 * See Also:
 * History: Original release was in V15.0.
 *****************************************************************/
extern UGOPENINTEXPORT int UF_DISP_create_framed_image(
    char* filename ,                    /* <I>
                                        Name of output image file
                                        */
    UF_DISP_image_format_t format ,     /* <I>
                                        Image type to produce:
                                        UF_DISP_PNG
                                        UF_DISP_JPEG
                                        UF_DISP_TIFF
                                        UF_DISP_COMPRESSED_TIFF
                                        UF_DISP_GIF
                                        UF_DISP_XWD (Only on UNIX workstations)
                                        UF_DISP_BMP (Only on Windows workstations)
                                        */
    UF_DISP_background_color_t color ,  /* <I>
                                        Back ground color:
                                        UF_DISP_ORIGINAL - original background
                                                           color
                                        UF_DISP_WHITE - white background color.
                                        */
    int upper_left_corner[2] ,          /* <I>
                                        The Image's upper left corner in the 
                                        window. Set both x and y to 0 (zero) 
                                        for a full screen image.
                                        upper_left_corner[0] = x position
                                        upper_left_corner[1] = y position
                                        */
    int width ,                         /* <I>
                                        Image width in pixels. Set to 0 (zero)
                                        for full screen image.
                                        */
    int height                          /* <I>
                                        Image height in pixels. Set to 0 
                                        (zero) for full screen image.
                                        */
);

/*****************************************************************************
 * Displays all or some rpo dimensions which belong to the specified
 * feature. The dimensions are specified indirectly by an array of
 * expression tags. If the count of the array is -1 then the array is
 * ignored and all rpo dimensions of the feature are displayed. If the
 * count is 0 then nothing is displayed. The display is temporary and can
 * be removed by a display refresh operation. The background color can
 * also be used to erase the dimensions but it may leave gaps on the
 * display. There must be a part loaded when this function is called. Any
 * specified expression which does not tie directly to a dimension of the
 * specified feature is considered invalid.
 *
 * Environment: Internal
 * See Also:
 * History:
 ***************************************************************************/
extern UGOPENINTEXPORT int UF_DISP_display_rpo_dimensions(
                 tag_t feature_tag ,       /* <I>
                                           Tag of the feature to which the 
                                           dimensions belong
                                           */
                 int exp_count ,           /* <I>
                                           >=0 = Number of expression tags 
                                                 in exp_tags array
                                            -1 = all rpo dimensions of the 
                                            feature
                                            */
                 tag_t* exp_tags ,          /* <I,len:exp_count> exp_count
                                            Array of expression tags of which 
                                            the dimensions need to be 
                                            displayed.(is ignored if count <=0)
                                            */
                 int view_option ,          /* <I>
                                            Option for the view, the constants
                                            are in uf_disp.h:
                                            UF_DISP_ALL_VIEWS_BUT_DRAWING
                                            UF_DISP_VIEW_OF_LAST_CURSOR
                                            UF_DISP_ALL_ACTIVE_VIEWS
                                            UF_DISP_WORK_VIEW_ONLY
                                            */
                 int color_option ,         /* <I>
                                            Option for the color, the constants
                                             are in uf_disp.h:
                                            UF_DISP_USE_SYSTEM_COLOR
                                            UF_DISP_USE_BACKGROUND_COLOR
                                            UF_DISP_USE_ORIGINAL_COLOR
                                            UF_DISP_USE_SPECIFIED_COLOR
                                            */
                 int color                  /* <I>
                                            Color used to display the 
                                            dimensions if color_option=
                                             UF_DISP_USE_SPECIFIED_COLOR.
                                            Use the color constants listed
                                            in uf_obj.h.
                                            */
);

/*****************************************************************************
 * Displays all or some sketch dimensions which belong to a specified
 * sketch. The dimensions are specified indirectly by an array of
 * expression tags. If the count of the array is -1 then the array is
 * ignored and all dimensions of the sketch are displayed. If the count is
 * 0 then nothing is displayed. The display is temporary and can be
 * removed by a display refresh operation. The background color can
 * also be used to erase the dimensions but it may leave gaps on the
 * display. There must be a part loaded when this function is called. Any
 * specified expression which does not tie directly to a dimension of the
 * specified feature is considered invalid.
 *
 * Environment: Internal
 * See Also:
 * History:
*****************************************************************************/
extern UGOPENINTEXPORT int UF_DISP_display_sket_dimensions(
              tag_t sketch_tag ,            /* <I>
                                            Tag of the sketch to which the 
                                            dimensions belong
                                            */
              int exp_count ,               /* <I>
                                            >= 0 = Number of expression tags in 
                                            exp_tags array
                                            -1 = all dimensions of the sketch
                                            */
              tag_t* exp_tags ,             /* <I,len:exp_count> exp_count
                                            Array of expression tags of which 
                                            the dimensions need to be displayed.
                                            (is ignored if count <= 0)
                                            */
              int view_option ,             /* <I>
                                            Option for the view, the constants 
                                            are in uf_disp.h:
                                            UF_DISP_ALL_VIEWS_BUT_DRAWING
                                            UF_DISP_VIEW_OF_LAST_CURSOR
                                            UF_DISP_ALL_ACTIVE_VIEWS
                                            UF_DISP_WORK_VIEW_ONLY
                                            */
              int color_option ,            /* <I>
                                            Option for the color, the constants
                                             are in uf_disp.h:
                                            UF_DISP_USE_SYSTEM_COLOR
                                            UF_DISP_USE_BACKGROUND_COLOR
                                            UF_DISP_USE_ORIGINAL_COLOR
                                            UF_DISP_USE_SPECIFIED_COLOR
                                            */
              int color                     /* <I>
                                            Color used to display the
                                            dimensions if color_option=
                                            UF_DISP_USE_SPECIFIED_COLOR.
                                            Use the color constants listed in 
                                            uf_obj.h.
                                            */
);

/*****************************************************************************
 * Displays a temporary conehead vector with either the base of the staff,
 * the arrow tip or the base of the arrow head at the reference point
 * in the specified view.
 * Return: void
 * Environment: Internal
 * See Also: 
 * History:
*****************************************************************************/
extern UGOPENINTEXPORT void UF_DISP_conehead(
       int display_flag ,     /* <I>
                              Display views to draw the conehead vector in.
                              UF_DISP_ALL_VIEWS_BUT_DRAWING
                              UF_DISP_VIEW_OF_LAST_CURSOR
                              UF_DISP_ALL_ACTIVE_VIEWS
                              UF_DISP_WORK_VIEW_ONLY
                              >0 = View sequence number
                  */
       double coord[3] ,       /* <I>
                              3D absolute coordinates of anchor.
                              */
       double vector[3] ,      /* <I>
                              3D vector which gives conehead direction
                              */
       int anchor_flag        /* <I>
                              Denotes the anchor point
                               0 = Anchor point at base of staff
                               1 = Anchor point at tip of arrowhead
                               2 = Anchor point at base of arrowhead
                               */
);/*<NEC>*/

/*****************************************************************************
 * Displays a temporary, labeled conehead vector with either the base of
 * the staff, the arrow tip or the base of the arrowhead at the reference
 * point in the specified view(s).  A label will be placed at the cone's tip.
 * Environment: Internal
 * Return: void
 * See Also:
 * History:
*****************************************************************************/
extern UGOPENINTEXPORT void UF_DISP_labeled_conehead(
            int display_flag ,        /* <I>
                                      Display views to draw the conehead 
                                      vector in.
                                      UF_DISP_ALL_VIEWS_BUT_DRAWING
                                      UF_DISP_VIEW_OF_LAST_CURSOR
                                      UF_DISP_ALL_ACTIVE_VIEWS
                                      UF_DISP_WORK_VIEW_ONLY
                                      >0 = View sequence number
                                      */
             double coord[3] ,         /* <I>
                                      3D absolute coordinates of anchor or 
                                      reference point in absolute space.
                                      */
             double vector[3] ,        /* <I>
                                      3D vector which gives conehead direction 
                                      in absolute space.
                                      */
             int anchor_flag ,        /* <I>
                                      Denotes the anchor point's location:
                                       0 = Anchor point at base of staff
                                       1 = Anchor point at tip of arrowhead
                                       2 = Anchor point at base of arrowhead
                                      */
             char * label             /* <I>
                                      Labels the conehead at its tip.
                                      */
);

/*****************************************************************************
 * Gets the current attribute settings with which the conehead vector
 * displays by a call to UF_DISP_conehead. You can then obtain the
 * values of the fields of the UF_DISP_conehead_attrb_s structure (see
 * the example below).
 * Return:void
 * Environment: Internal
 * See Also: 
 * History:
*****************************************************************************/
extern UGOPENINTEXPORT void UF_DISP_get_conehead_attrb(
    UF_DISP_conehead_attrb_s * attributes  /* <O>
                                           Pointer to the attributes structure. 
                                           */
);

/*****************************************************************************
 * Allows changes to the current attribute settings with which the
 * conehead vector displays by a call to UF_DISP_conehead.
 * Note that it is best to get the current attribute settings and then 
 * adjust the ones you need, as shown in the example.
 * Return:void
 * Environment: Internal
 * See Also: 
 * History:
*****************************************************************************/
extern UGOPENINTEXPORT void UF_DISP_set_conehead_attrb(
    UF_DISP_conehead_attrb_s * attributes  /* <I>
                                           Pointer to attributes structure. 
                                           */
);/*<NEC>*/

/*****************************************************************************
 * Resets the conehead attributes to the default values.
 * Return: void
 * Environment: Internal
 * See Also:
 * History:
*****************************************************************************/
extern UGOPENINTEXPORT void UF_DISP_reset_conehead_attrb(void);/*<NEC>*/

/*****************************************************************************
 * Adds an object to the display. You can use this routine to update the
 * display of a new or modified object, if UF_DISP_set_display has been
 * used to turn off the display update.
 * Environment: Internal
 * See Also:
 * History:
*****************************************************************************/
extern UGOPENINTEXPORT int UF_DISP_add_item_to_display(
                      tag_t object_id    /* <I>
                                         Object identifier of the object to 
                                         be added to display
                                         */
);

/****************************************************************************
 * Downloads the color table to the graphics display, so that all geometry
 * displayed in the graphics window will now use the current contents of
 * the Color Table object (of the Display part); this is equivalent to
 * selecting Apply from the color palette dialog in interactive
 * NX. There must be a part loaded before calling this function.
 * Environment: Internal
 * See Also: 
 * History:
*****************************************************************************/
extern UGOPENINTEXPORT int  UF_DISP_load_color_table(
   void
);

/*****************************************************************************
 *
 *              Overlay Graphics related prototypes follow
 *
 *****************************************************************************/

/***************************************************************************
 * This function defines a simple line to be rendered in the specified
 * view.  The "ogp" in the name indicates that the line is drawn as an
 * Overlay Graphics primitive (please see the Overview to this section);  as
 * such, it neither creates, nor is directly associated with, an NX
 * object.  UF_DISP_display_ogp_* functions are intended to be used
 * exclusively from motion callback functions.  Please see the discussion
 * and example provided with UF_UI_specify_screen_position.
 * Environment: Internal Only
 * See Also: 
 * History:
 ****************************************************************************/
extern UGOPENINTEXPORT int UF_DISP_display_ogp_line(
             tag_t view_tag ,       /* <I>
                                    Tag of the view in which the line is to 
                                    be rendered
                                    */
             double pos1[3] ,       /* <I>
                                    1st endpoint (Work Part Abs Coords)
                                    */
             double pos2[3]         /* <I>
                                    2nd endpoint (Work Part Abs Coords)
                                    */
);

/***************************************************************************
 * This function defines a polyline to be rendered in the specified view.
 * The "ogp" in the name indicates that the polyline will be drawn as an
 * Overlay Graphics primitive (please see the Overview to this section);  as
 * such, it neither creates, nor is directly associated with, an NX
 * object.  * UF_DISP_display_ogp_* functions are intended to be used
 * exclusively from motion callback functions.  Please see the discussion
 * and example provided with UF_UI_specify_screen_position.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ****************************************************************************/
extern UGOPENINTEXPORT int UF_DISP_display_ogp_polyline(
               tag_t view_tag ,          /* <I>
                                         Tag of the view in which the polyline 
                                         is to be rendered
                                         */
               double pos_array[][3] ,  /* <I,len:pos_count>
                                         Array of positions [pos_count][3]
                                         each position is an (x,y,z) triplet in
                                         Work Part Absolute Coordinates.
                                         */
               int pos_count             /* <I>
                                         count of positions in pos_array
                                         */
);

/***************************************************************************
 * This function defines a circle to be rendered in the specified view.
 * The "ogp" in the name indicates that the arc will be drawn as an
 * Overlay Graphics primitive (please see the Overview to this section);  as
 * such, it neither creates, nor is directly associated with, an NX
 * object. The orientation matrix must be ortho-normal.  (If necessary, use
 * UF_MTX3_initialize to create the matrix from X and Y vectors.)
 * UF_DISP_display_ogp_* functions are intended to be used
 * exclusively from motion callback functions.  Please see the discussion
 * and example provided with UF_UI_specify_screen_position.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ****************************************************************************/
extern UGOPENINTEXPORT int UF_DISP_display_ogp_circle(
            tag_t view_tag ,          /* <I>
                                      Tag of the view in which the circle is to
                                      be rendered
                                      */
            double orientation[9] ,   /* <I>
                                      The rotation matrix of the circle 
                                      (relative to the Work Part Absolute 
                                      Coordinate System). The matrix must be 
                                      ortho-normal. If necessary, use 
                                      UF_MTX3_initialize to create the matrix 
                                      from X and Y vectors.  
                                      */
            double center[3] ,        /* <I>
                                      The circle center in the coordinate 
                                      system of the arc (as defined by 
                                      "orientation" above).  
                                      */
            double radius             /* <I>
                                      The radius of the circle (Work Part 
                                      Absolute units)
                                      */
);


/***************************************************************************
 * This function defines an arc to be rendered in the specified view.  The
 * "ogp" in the name indicates that the arc will be drawn as an Overlay
 * Graphics primitive (please see the Overview to this section);  as such, it
 * neither creates, nor is directly associated with, an NX object.
 * The arc is drawn in a positive angular direction ("counterclockwise")
 * from the start angle to the end angle.
 * The orientation matrix must be ortho-normal.  (If necessary, use
 * UF_MTX3_initialize to create the matrix from X and Y vectors.)
 * This function returns an error if the absolute value of the difference
 * between the start and end angle is greater than two pi (plus the system
 * tolerance). An error is also returned if the start angle is greater than
 * the end angle.
 * UF_DISP_display_ogp_* functions are intended to be used
 * exclusively from motion callback functions.  Please see the discussion
 * and example provided with UF_UI_specify_screen_position.
 *
 * Environment: Internal  and  External
 * See Also: 
 * History:
 ****************************************************************************/
extern UGOPENINTEXPORT int UF_DISP_display_ogp_arc(
       tag_t view_tag ,            /* <I>
                                   Tag of the view in which the arc is to be 
                                   rendered
                                   */
       double orientation[9] ,     /* <I>
                                   The rotation matrix of the arc (relative to 
                                   the Work Part Absolute Coordinate System). 
                                   The matrix must be ortho-normal. If 
                                   necessary, use UF_MTX3_initialize to create 
                                   the matrix from X and Y vectors.
                                   */
       double start_angle ,        /* <I>
                                   Start angle in radians;  the zero degree 
                                   vector is the positive x-axis of the space 
                                   described by the orientation matrix.
                                   */
       double end_angle ,          /* <I>
                                   End angle in radians;  the zero degree 
                                   vector is the positive x-axis of the space 
                                   described by the orientation matrix.
                                   */
       double center[3],           /* <I>
                                   The arc center in the coordinate system of 
                                   the arc (as defined by "orientation" above).
                                   */
       double radius               /* <I>
                                   The radius of the arc (Work Part Absolute 
                                   units)
                                   */
);

/*****************************************************************************
 *
 * Prints the contents of the graphics window to the default printer. 
 * This function is available only on Windows workstations and returns
 * an error if called on a non-Windows workstation.
 *
 * Environment: Internal
 * See Also:
 * History: Originally released in V16.0.
 *          Second parameter redefined in V18.0.
 *****************************************************************************/
extern UGOPENINTEXPORT int UF_DISP_print_window_ug_image (
    int format,         /* <I> Specifies the format of the printed image.

                           0: A vector-format image is printed.
                           1: A raster-format (bitmap) image is printed.

                           If only wireframe views are displayed, then a 
                           vector-format image is printed even if the 
                           format parameter is set to 1. */

    int color_usage     /* <I> Specifies how color is used in the printed 
                           image.

                           0: If a vector image is printed, line color is
                           determined by the setting of the Black Lines Only 
                           option in the File->Print dialog. If a raster image 
                           is printed, the image background is the same as the 
                           background of the graphics window.

                           1: If a vector image is printed, line color is
                           determined by the setting of the Black Lines Only 
                           option in the File->Print dialog. If a raster image 
                           is printed, the image background is white.

                           2: If a vector image is printed, lines are printed
                           in color (or shades of gray on a monochrome printer).
                           If a raster image is printed, the image background 
                           is the same as the background of the graphics 
                           window. 

                           3: If a vector image is printed, all lines are
                           printed in black. If a raster image is printed, 
                           the image background is white. */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif    /*  END  UF_DISP_UGOPENINT_INCLUDED  */
