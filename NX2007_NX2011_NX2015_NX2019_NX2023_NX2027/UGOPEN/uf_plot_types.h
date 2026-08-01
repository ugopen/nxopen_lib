/*============================================================================


   Copyright (c) 2004 Unigraphics Solutions, Inc.
        Unpublished - All rights reserved

============================================================================




File Description:

This file provides data types for use in the UF_PLOT module. Most of the
time this file does not need to be included directly, because it is included
by uf_plot.h.

============================================================================*/

/***************************************************************************

***************************************************************************/


#ifndef UF_PLOT_TYPES_H_INCLUDED
#define UF_PLOT_TYPES_H_INCLUDED

#include <uf_cgm_types.h>
#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
This enumerated type provides the units selection where needed. It is
initialized to be cognate to the values of UF_PART_METRIC and UF_PART_ENGLISH.
****************************************************************************/
enum UF_PLOT_units_e
{
    UF_PLOT_MILLIMETERS = 1,
    UF_PLOT_INCHES
};
typedef enum UF_PLOT_units_e
             UF_PLOT_units_t, *UF_PLOT_units_p_t;

/****************************************************************************
This enumerated type provides the selection of what colors are to be used
to render the display, drawing sheets without custom colors, and drawing
sheets when use_drawing_sheet_colors is FALSE.
****************************************************************************/
enum UF_PLOT_colors_e
{
    UF_PLOT_AS_DISPLAYED_COLORS,   /* Use the colors displayed on screen. */
    UF_PLOT_PART_COLORS,           /* Use the colors of the part color table. */
    UF_PLOT_CUSTOM_PALETTE_COLORS, /* Use the session custom colors. */
    UF_PLOT_BLACK_ON_WHITE,        /* Use black for all geometry. */
    UF_PLOT_LEGACY_COLORS,         /* Use 15 fixed colors supported by
                                      NX releases before NX 3. */
    UF_PLOT_COLOR_BY_WIDTH         /* Use the first twelve entries(representing
                                      thin, normal & thick and the new 9 
                                      standard widths) of the session
                                      custom colors. In otherwords the color is
                                      determined by the density index.  All thin
                                      objects will plot using the first color
                                      entry, all normal objects will plot with
                                      the second color entry, and all thick
                                      objects will plot in the third color entry, etc. */
};
typedef enum UF_PLOT_colors_e
             UF_PLOT_colors_t, *UF_PLOT_colors_p_t;

/****************************************************************************
This enumerated type provides the selection of what line widths are to be used
to render the display, drawing sheets without custom widths, and drawing sheets
when use_drawing_sheet_widths is FALSE.
****************************************************************************/
enum UF_PLOT_widths_e
{
    UF_PLOT_STANDARD_WIDTHS,      /* Use fixed line widths. */
    UF_PLOT_SINGLE_WIDTH,         /* Use the single line width defined
                                     in the session custom widths. */
    UF_PLOT_CUSTOM_3_WIDTHS,      /* Use custom widths per-width index,
                                     as defined in the session custom widths. */
    UF_PLOT_CUSTOM_PALETTE_WIDTHS /* Use custom widths per-color index,
                                     as defined in the session custom widths. */
};
typedef enum UF_PLOT_widths_e
             UF_PLOT_widths_t, *UF_PLOT_widths_p_t;

/********************* Custom Colors and Widths ******************************/

#define UF_PLOT_MAX_COLORS            UF_CGM_MAX_COLORS

#define UF_PLOT_NO_FAVORITE           UF_CGM_NO_FAVORITE

typedef UF_CGM_custom_colors_t        UF_PLOT_custom_colors_t,
                                      *UF_PLOT_custom_colors_p_t;

#define UF_PLOT_MAX_WIDTHS            UF_CGM_MAX_WIDTHS

#define UF_PLOT_MAX_NAME_SIZE         UF_CGM_MAX_NAME_SIZE

#define UF_PLOT_WIDTH_NORMAL          UF_CGM_WIDTH_NORMAL
#define UF_PLOT_WIDTH_THICK           UF_CGM_WIDTH_THICK
#define UF_PLOT_WIDTH_THIN            UF_CGM_WIDTH_THIN
#define UF_PLOT_WIDTH_1               UF_CGM_WIDTH_1       
#define UF_PLOT_WIDTH_2               UF_CGM_WIDTH_2       
#define UF_PLOT_WIDTH_3               UF_CGM_WIDTH_3       
#define UF_PLOT_WIDTH_4               UF_CGM_WIDTH_4    
#define UF_PLOT_WIDTH_5               UF_CGM_WIDTH_5      
#define UF_PLOT_WIDTH_6               UF_CGM_WIDTH_6    
#define UF_PLOT_WIDTH_7               UF_CGM_WIDTH_7     
#define UF_PLOT_WIDTH_8               UF_CGM_WIDTH_8     
#define UF_PLOT_WIDTH_9               UF_CGM_WIDTH_9      

#define UF_PLOT_width_use_t           UF_CGM_width_use_t
#define UF_PLOT_width_single          UF_CGM_width_single
#define UF_PLOT_width_by_width        UF_CGM_width_by_width
#define UF_PLOT_width_by_color        UF_CGM_width_by_color

#define UF_PLOT_width_single_t        UF_CGM_width_single_t
#define UF_PLOT_width_std             UF_CGM_width_std
#define UF_PLOT_width_custom          UF_CGM_width_custom
#define UF_PLOT_width_user            UF_CGM_width_user

typedef UF_CGM_width_custom_t         UF_PLOT_width_custom_t,
                                      *UF_PLOT_width_custom_p_t;

#define UF_PLOT_NOT_CUSTOM_WIDTH      UF_CGM_NOT_CUSTOM_WIDTH

typedef UF_CGM_width_color_t          UF_PLOT_width_color_t,
                                     *UF_PLOT_width_color_p_t;

typedef UF_CGM_custom_widths_t        UF_PLOT_custom_widths_t,
                                     *UF_PLOT_custom_widths_p_t;

/****************************************************************************
This structure provides the options for rendering plots.
****************************************************************************/
struct UF_PLOT_job_options_s
{
    UF_PLOT_colors_t    colors;      /* Specifies colors used in plotting. */
    logical             use_drawing_sheet_colors; /* TRUE if custom colors
                                        associated with the drawing sheet
                                        are used in plotting the sheet.
                                        If FALSE, or if custom colors are
                                        not associated with the sheet, then
                                        plotting colors are determined by
                                        the colors field. */
    UF_PLOT_widths_t    widths;      /* Specifies widths used in plotting. */
    logical             use_drawing_sheet_widths; /* TRUE if custom widths
                                        associated with the drawing sheet
                                        are used in plotting the sheet.
                                        If FALSE, or if custom widths are
                                        not associated with the sheet, then
                                        plotting widths are determined by
                                        the widths field. */
    double              tolerance;   /* A unitless value that controls the
                                        accuracy or smoothness of plotted
                                        curve geometry. Values must be
                                        greater than or equal to 0.0001;
                                        smaller values produce smoother
                                        curves. */

};
typedef struct UF_PLOT_job_options_s
               UF_PLOT_job_options_t, *UF_PLOT_job_options_p_t;

/****************************************************************************
This structure provides the banner options for rendering plots.
****************************************************************************/
struct UF_PLOT_banner_options_s
{
    logical             show_banner; /* TRUE if the banner appears on plot
                                        output. */
    char                *message;    /* If non-NULL, a NULL-terminated ASCII
                                        string that appears in the banner if
                                        a banner entry is defined to display
                                        the message. */
};
typedef struct UF_PLOT_banner_options_s
               UF_PLOT_banner_options_t, *UF_PLOT_banner_options_p_t;

/****************************************************************************
This enumerated type provides the selection of the rotation a plot is to
have when placed in the layout.
****************************************************************************/
enum UF_PLOT_rotation_e
{
    UF_PLOT_ROTATION_0,
    UF_PLOT_ROTATION_90,
    UF_PLOT_ROTATION_180,
    UF_PLOT_ROTATION_270
};
typedef enum UF_PLOT_rotation_e
             UF_PLOT_rotation_t, *UF_PLOT_rotation_p_t;

/****************************************************************************
This structure provides a means of returning data indicating the location
and borders of a plot placed in the layout, or the entire layout.
****************************************************************************/
struct UF_PLOT_extents_s
{
    double              left;
    double              right;
    double              bottom;
    double              top;
};
typedef struct UF_PLOT_extents_s
               UF_PLOT_extents_t, *UF_PLOT_extents_p_t;

#define UF_PLOT_MAX_STRING_NCHARS 1000
#define UF_PLOT_MAX_STRING_BUFSIZE NX_BUFSIZE(UF_PLOT_MAX_STRING_NCHARS)

/*  */
#define UF_PLOT_MAX_STRING_SIZE        (UF_PLOT_MAX_STRING_BUFSIZE)
/*  */

/****************************************************************************
This structure provides a means of returning data associated with a printer
group.
****************************************************************************/
struct UF_PLOT_printer_group_s
{
    char                group_dir[ MAX_FSPEC_BUFSIZE ];
    char                jobs_dir[ MAX_FSPEC_BUFSIZE ];
    char                home_dir[ MAX_FSPEC_BUFSIZE ];
    char                label[UF_PLOT_MAX_STRING_BUFSIZE];
};
typedef struct UF_PLOT_printer_group_s
               UF_PLOT_printer_group_t, *UF_PLOT_printer_group_p_t;

/****************************************************************************
This enumerated type provides the selection of the type of file to create
when converting files.
****************************************************************************/
enum UF_PLOT_format_e
{
    UF_PLOT_CGM_FORMAT,
    UF_PLOT_EMF_FORMAT,
    UF_PLOT_TIFF_FORMAT,
    UF_PLOT_JPEG_FORMAT,
    UF_PLOT_PNG_FORMAT
};
typedef enum UF_PLOT_format_e
             UF_PLOT_format_t, *UF_PLOT_format_p_t;

#ifdef __cplusplus
}
#endif

#endif /* UF_PLOT_TYPES_H_INCLUDED */
