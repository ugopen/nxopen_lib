/*****************************************************************************

                   Copyright (c) 2003 UGS PLM Solutions Inc.
                      Unpublished - All Rights Reserved

******************************************************************************



File description:

The functions in this and other uf_cgm_*.h files allow you to perform
CGM-related operations, including functions for:

exporting CGMs from parts
importing CGMs to parts
inquiring information about CGM import and export options

*****************************************************************************/

#ifndef UF_CGM_TYPES_H_INCLUDED
#define UF_CGM_TYPES_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_disp_types.h>
#include <uf_obj_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************

                                  CGM Import Types

*****************************************************************************/

/*
    The fields of structure UF_CGM_import_options_t specify options for
    CGM import operations.
        allow_new_drawing - Set to FALSE if geometry is not to be imported
                            onto a new drawing sheet. If set to TRUE, the
                            system determines whether or not to create a new
                            drawing sheet for imported geometry. (TRUE by
                            default.)
*/
struct UF_CGM_import_options_s
{
    logical                     allow_new_drawing; /* TRUE, if geometry can
                                                      be imported onto a new
                                                      drawing sheet. */
};

typedef struct UF_CGM_import_options_s UF_CGM_import_options_t,
*UF_CGM_import_options_p_t;





/*****************************************************************************

                                  CGM Export Types

*****************************************************************************/


/*
    Enumerated data type UF_CGM_colors_t defines symbols to specify the
    colors applied to geometry recorded in exported CGM files. The colors
    field of the UF_CGM_export_options_t structure is set to one of these
    symbols.
*/
enum UF_CGM_colors_e
{
    UF_CGM_AS_DISPLAYED_COLORS,   /* Apply the colors displayed on screen. */
    UF_CGM_PART_COLORS,           /* Apply the colors of the part color table. */
    UF_CGM_CUSTOM_PALETTE_COLORS, /* Apply the session custom colors. */
    UF_CGM_BLACK_ON_WHITE,        /* Apply black to all geometry. */
    UF_CGM_LEGACY_COLORS,         /* Apply 15 fixed colors supported by
                                     NX releases before NX 3. */
    UF_CGM_COLOR_BY_WIDTH         /* Apply the first twelve entries(representing
                                     thin, normal & thick and 9 new widths) of the session
                                     custom colors. In otherwords the color is
                                     determined by the density index.  All thin
                                     objects will plot using the first color
                                     entry, all normal objects will plot with
                                     the second color entry, and all thick
                                     objects will plot in the third color entry, etc. 
                                   */
};

typedef enum UF_CGM_colors_e UF_CGM_colors_t  ;

/*
    Enumerated data type UF_CGM_widths_t defines symbols to specify the
    line widths applied to geometry recorded in exported CGM files. The
    widths field of the UF_CGM_export_options_t structure is set to one
    of these symbols.
*/
enum UF_CGM_widths_e
{
    UF_CGM_STANDARD_WIDTHS,       /* Apply the fixed line widths. */
    UF_CGM_SINGLE_WIDTH,          /* Apply the single line width defined
                                     in the session custom widths. */
    UF_CGM_CUSTOM_3_WIDTHS,       /* Apply custom widths per-width index,
                                     as defined in the session custom widths. */
    UF_CGM_CUSTOM_PALETTE_WIDTHS, /* Apply custom widths per-color index,
                                     as defined in the session custom widths. */
    UF_CGM_DEFAULT_FILE_WIDTHS    /* Apply line width settings specified in
                                     the CGM Defaults File (cgmdef.txt). */
};

typedef enum UF_CGM_widths_e UF_CGM_widths_t  ;

/*
    Enumerated data type UF_CGM_vdc_mode_t defines symbols to specify how
    coordinates are represented in the CGM file. The vdc_mode field of
    the UF_CGM_export_options_t structure is set to one of these symbols.
*/
enum UF_CGM_vdc_mode_e
{
    UF_CGM_INTEGER_VDC, /* Use 16-bit integer coordinates. */
    UF_CGM_REAL_VDC     /* Use 32-bit real coordinates. */
};

typedef enum UF_CGM_vdc_mode_e UF_CGM_vdc_mode_t  ;

/*
    Enumerated data type UF_CGM_size_mode_t defines symbols to indicate
    how the size of CGM geometry is specified. The mode field of the
    UF_CGM_size_t structure is set to one of these symbols.
*/
enum UF_CGM_size_mode_e
{
    UF_CGM_SIZE_BY_SCALE,     /* Specify size as a scale factor. */
    UF_CGM_SIZE_BY_DIMENSIONS /* Specify size as dimensions. */
};

typedef enum UF_CGM_size_mode_e UF_CGM_size_mode_t  ;

/*
    Enumerated data type UF_CGM_units_t defines symbols to indicate 
    the units of dimensions that specify the size of CGM geometry. The
    units field of the UF_CGM_dimensions_t structure is set to one of
    these symbols.
*/
enum UF_CGM_units_e
{
    UF_CGM_MILLIMETERS,
    UF_CGM_INCHES
};

typedef enum UF_CGM_units_e UF_CGM_units_t  ;

/*
    Structure UF_CGM_dimensions_t specifies the dimensions of CGM
    geometry recorded in the CGM file. The dimensions field of the
    UF_CGM_size_t structure is a structure of type UF_CGM_dimensions_t.

    The dimensions field of the UF_CGM_dimensions_t structure specifies
    the width and height of CGM geometry, expressed in the units indicated 
    by the units field.
*/
struct UF_CGM_dimensions_s
{
    UF_CGM_units_t              units;
    double                      dimensions[2];
};

typedef struct UF_CGM_dimensions_s UF_CGM_dimensions_t,
*UF_CGM_dimensions_p_t;

/*
    Structure UF_CGM_size_t specifies the size of geometry recorded
    in the CGM file. The size field of the UF_CGM_export_options_t
    structure is a structure of type UF_CGM_size_t.

    If the mode field of the UF_CGM_size_t structure is set to
    UF_CGM_SIZE_BY_SCALE, then geometry is sized according to the
    scale factor specified by the scale field. If the mode field is
    set to UF_CGM_SIZE_BY_DIMENSIONS, then geometry is sized to fit
    the dimensions specified by the dimensions field.
*/
struct UF_CGM_size_s
{
    UF_CGM_size_mode_t          mode;
    double                      scale;
    UF_CGM_dimensions_t         dimensions;
};

typedef struct UF_CGM_size_s UF_CGM_size_t, *UF_CGM_size_p_t;

/*
    Enumerated data type UF_CGM_text_mode_t defines symbols to specify
    how text is represented in the CGM file. The text_mode field of the
    UF_CGM_export_options_t structure is set to one of these symbols.
*/
enum UF_CGM_text_mode_e
{
    UF_CGM_TEXT_AS_POLYLINES,  /* Record text as CGM polyline elements. */
    UF_CGM_TEXT_AS_CHARACTERS, /* Record text as as CGM text elements. */
    UF_CGM_TEXT_BEST_FIT,      /* Record standard fonts as CGM text elements, 
                                  record NX fonts as CGM polyline elements */
    UF_CGM_TEXT_RESERVED1,     /* RESERVED - internal use only */
    UF_CGM_TEXT_RESERVED2      /* RESERVED - internal use only */

};

typedef enum UF_CGM_text_mode_e UF_CGM_text_mode_t  ;

/*
    Enumerated data type UF_CGM_fonts_t defines symbols to specify how
    text fonts are recorded in the CGM file. The fonts field of the
    UF_CGM_export_options_t structure is set to one of these symbols.
*/
enum UF_CGM_fonts_e
{
    UF_CGM_1_CALS_FONT,       /* Map all NX fonts to CALS font Hershey
                                 Simplex Roman. */
    UF_CGM_4_CALS_FONTS,      /* Map NX fonts 1 through 4 to CALS fonts
                                 as follows:
                                     1: Hershey Simplex Roman
                                     2: Hershey Cartographic Roman
                                     3: Hershey Simplex Script
                                     4: Hershey Complex Italic
                                 Map all other NX fonts to CALS font
                                 Hershey Simplex Roman. */
    UF_CGM_NX_FONTS,          /* Record the names of NX fonts in the CGM. */
    UF_CGM_DEFAULT_FILE_FONTS /* Record fonts according to text font mapping
                                 keywords specified in the CGM Defaults File
                                 (cgmdef.txt). */
};

typedef enum UF_CGM_fonts_e UF_CGM_fonts_t  ;

/****************************************************************************
                             CGM EXPORT REASONS

    Applications can implement callback functions to monitor 
    CGM export operations in order to control whether/how application-
    specific geometry is recorded in the CGM file.

    To support this monitoring, a "reason" is specified for each CGM 
    export operation, so an application can evaluate the reason in 
    deciding whether/how to respond to the operation. For example, an 
    application might generate application geometry differently during 
    plotting than during CGM export operations for non-plotting reasons 
    (File->Export->CGM, File->Print, export operations invoked 
    programmatically by applications, etc.).

    Enumerated type UF_CGM_export_reason_t enumerates symbols/codes that 
    represent the possible reasons for a CGM export operation. 

    Code UF_CGM_plot_reason is specified for CGM export operations invoked 
    by plotting functionality, including File->Plot and corresponding 
    NX Open and GRIP functionality.

    Code UF_CGM_export_reason is specified for CGM export operations
    invoked by File->Export->CGM and can be used by UF_CGM_export_cgm.

    Code UF_CGM_print_reason is specified for CGM export operations
    invoked by File->Print and can be used by UF_CGM_export_cgm.

    Code UF_CGM_copy_display_reason is specified for CGM export operations
    invoked by Edit->Copy Display can be used by UF_CGM_export_cgm.

    Code UF_CGM_pdf_reason can be used by UF_CGM_export_cgm when the CGM
    is to be used to create a PDF.

    Code UF_CGM_pdf_hidden_text_reason is specified for File->Export PDF 
    and can be used by UF_CGM_export_cgm.  Note that using this reason 
    will generate a non-standard CGM file if you also request Text as Text. 
    The CGM file will only be properly interpreted by the cgm2pdf executable. 
    The NX text will be both stroked and added as hidden text for the PDF. 
    The visible stroked text will render the text as seen in NX, and the 
    hidden text will give searchable text in the PDF file.  

    Code UF_CGM_misc_appl_reason is specified for CGM export operations
    invoked programmatically by an application unless an application-
    specific reason code is defined.

 ****************************************************************************/
typedef enum UF_CGM_export_reason_e
{
    UF_CGM_plot_reason = 0,  /* Plotting either interactive, NXOpen or Grip */
    UF_CGM_export_reason,    /* CGM Export either interactive or NXOpen */
    UF_CGM_print_reason,     /* File->Print either interactive or NX Open */
    UF_CGM_copy_display_reason, /* Edit->Copy Display */
    UF_CGM_pdf_reason,          /* CGM is for a PDF */
    UF_CGM_misc_appl_reason,    /* All other CGM Export operations */
    UF_CGM_pdf_hidden_text_reason,   /* File->Export PDF */
    UF_CGM_vised_hidden_text_reason,   /* Visual Editor */
    UF_CGM_max_reasons

} UF_CGM_export_reason_t, *UF_CGM_export_reason_p_t;



/*
    The fields of structure UF_CGM_export_options_t specify options for
    CGM export operations.
*/
struct UF_CGM_export_options_s
{
    UF_CGM_colors_t             colors;    /* Specifies how colors are applied
                                              to exported geometry. */
    UF_CGM_widths_t             widths;    /* Specifies how lines widths are
                                              applied to exported geometry. */
    UF_CGM_vdc_mode_t           vdc_mode;  /* Specifies how coordinates are
                                              represented in the CGM file. */
    UF_CGM_size_t               size;      /* Specifies the size or scale of
                                              exported geometry. */
    UF_CGM_text_mode_t          text_mode; /* Specifies how text geometry is
                                              represented in the CGM file. */
    UF_CGM_fonts_t              fonts;     /* Specifies how fonts are recorded
                                              in the CGM file. */
    UF_CGM_export_reason_t      reason;    /* Specifies the reason the CGM 
                                              file is being exported. This
                                              can have an effect on how the 
                                              CGM is produced. The default
                                              is UF_CGM_export_reason. */
    double                      tolerance; /* A unitless value that controls
                                              the accuracy or smoothness of
                                              exported curve geometry. Values
                                              must be greater than or equal to
                                              1.0e-10 (.0000000001). Smaller 
                                              values produce smoother curves. */
};

typedef struct UF_CGM_export_options_s UF_CGM_export_options_t,
*UF_CGM_export_options_p_t;


/************************** Custom Colors and Widths ************************/

#define UF_CGM_MAX_NAME_SIZE    UF_DISP_MAX_NAME_SIZE

/* Maximum number of colors
 */
#define UF_CGM_MAX_COLORS     UF_OBJ_MAX_COLOR+1

/****************************************************************************
 *
 *  STRUCTURE:   UF_CGM_color_t
 *
 *  DESCRIPTION: This structure contains the parameters for one color.
 *
 ****************************************************************************/

#define UF_CGM_NO_FAVORITE    -1

struct UF_CGM_color_s
{
    int    clr_index;                        /* Color index in the range
                                                [ 0 to UF_OBJ_MAX_COLOR ]  */
    char   clr_name[UF_CGM_MAX_NAME_SIZE+1]; /* Color name, specified as a
                                                NULL-terminated ASCII string */
    double clr_vals[3];                      /* An RGB definition of the
                                                color, consisting of red,
                                                green, and blue values in
                                                the range [ 0.0 to 1.0 ]. */
    int    favorite_index;                   /* If the color is a favorite
                                                color, an favorite index in
                                                the range [ 1 to 30 ].
                                                Otherwise, UF_CGM_NO_FAVORITE. */
};

typedef struct UF_CGM_color_s UF_CGM_color_t, *UF_CGM_color_p_t;

/****************************************************************************
 *
 *  STRUCTURE:   UF_CGM_custom_colors_t
 *
 *  DESCRIPTION: This structure contains the parameters for a color palette.
 *               It can be used to map the colors of a display image when
 *               creating a CGM.
 *
 ****************************************************************************/
struct UF_CGM_custom_colors_s
{
    UF_CGM_color_t colors[UF_CGM_MAX_COLORS];
};

typedef struct UF_CGM_custom_colors_s UF_CGM_custom_colors_t,
*UF_CGM_custom_colors_p_t;


/* Maximum number of widths
 */
#define UF_CGM_MAX_WIDTHS     14

/* Display widths
 */
#define UF_CGM_WIDTH_NORMAL   UF_OBJ_WIDTH_NORMAL
#define UF_CGM_WIDTH_THICK    UF_OBJ_WIDTH_THICK
#define UF_CGM_WIDTH_THIN     UF_OBJ_WIDTH_THIN
#define UF_CGM_WIDTH_1        UF_OBJ_WIDTH_1
#define UF_CGM_WIDTH_2        UF_OBJ_WIDTH_2
#define UF_CGM_WIDTH_3        UF_OBJ_WIDTH_3
#define UF_CGM_WIDTH_4        UF_OBJ_WIDTH_4
#define UF_CGM_WIDTH_5        UF_OBJ_WIDTH_5
#define UF_CGM_WIDTH_6        UF_OBJ_WIDTH_6
#define UF_CGM_WIDTH_7        UF_OBJ_WIDTH_7
#define UF_CGM_WIDTH_8        UF_OBJ_WIDTH_8
#define UF_CGM_WIDTH_9        UF_OBJ_WIDTH_9

/****************************************************************************
 *
 *  ENUMERATED:  UF_CGM_width_use_t
 *
 *  DESCRIPTION:  This enumerated type specifies the primary selection of
 *  width assignment, a single width, the custom widths, or by color.
 *
 ****************************************************************************/
enum UF_CGM_width_use_e
{
    UF_CGM_width_single,          /* single width */
    UF_CGM_width_by_width,        /* custom widths by width index */
    UF_CGM_width_by_color         /* custom widths by color index */
};

typedef enum UF_CGM_width_use_e UF_CGM_width_use_t;


/****************************************************************************
 *
 *  ENUMERATED:  UF_CGM_width_single_t
 *
 *  DESCRIPTION:  This enumerated type specifies the source of a single width
 *  is, one of the standard widths, one of custom widths, or a user-defined
 *  width.
 *
 ****************************************************************************/
enum UF_CGM_width_single_e
{
    UF_CGM_width_std,             /* single width, standard */
    UF_CGM_width_custom,          /* single width, custom */
    UF_CGM_width_user             /* single width, user-defined */
};

typedef enum UF_CGM_width_single_e UF_CGM_width_single_t;

/****************************************************************************
 *
 *  STRUCTURE:   UF_CGM_width_custom_t
 *
 *  DESCRIPTION: This structure describes a custom width by width index.
 *               There are 3 legacy widths (thin, normal, thick) and the
 *               new 9 standard widths that can also be customized.
 *
 ****************************************************************************/
struct UF_CGM_width_custom_s
{
    double width;                      /* Width of lines for the custom width */
    char name[UF_CGM_MAX_NAME_SIZE+1]; /* Width name, specified as a
                                          NULL-terminated ASCII string */
};

typedef struct UF_CGM_width_custom_s UF_CGM_width_custom_t,
*UF_CGM_width_custom_p_t;

#define UF_CGM_NOT_CUSTOM_WIDTH     (-1)

/****************************************************************************
 *
 *  STRUCTURE:   UF_CGM_width_color_t
 *
 *  DESCRIPTION: This structure describes a custom width by color index.
 *               The width_source member has the following values:
 *
 *                   -1  not a custom width (UF_CGM_NOT_CUSTOM_WIDTH)
 *                  >=0  custom width index - value is the index into the
 *                       custom member of the main structure below.
 *
 *               Note that the index is an internal one.
 *
 *               Note that the width member of this structure contains the
 *               actual width to use with its color index, regardless of the
 *               source.
 *
 ****************************************************************************/
struct UF_CGM_width_color_s
{
    double width;         /* Width associated with the color */
    int    width_source;  /* Width entry source */
};

typedef struct UF_CGM_width_color_s UF_CGM_width_color_t,
*UF_CGM_width_color_p_t;

/****************************************************************************
 *
 *  STRUCTURE:   UF_CGM_custom_widths_t
 *
 *  DESCRIPTION: This structure describes a width palette.  It can be used to
 *               map the line widths of a display image when creating a CGM.
 *
 *               It gives the units in which all the widths are stored, single width information,
 *               the custom width definitions, and an entry for each color.
 *
 *               The 'use' member specifies the primary selection of which
 *               type of width assignment to use.
 *
 *               The 'single_width' member contains the last-typed value for
 *               the user-defined width to use when UF_CGM_width_user is
 *               selected for member 'single'.  It is always defined, even when
 *               'single' is not set to UF_CGM_width_user.
 *
 *               The 'single_source' member contains a value when the 'single'
 *               member is UF_CGM_width_std or UF_CGM_width_custom. The value
 *               is the index in the 'custom' width array or the standard width
 *               index value. Both are assumed to be in internal order, normal,
 *               thick, and thin for 0, 1, and 2, respectively.
 *
 *               Note that 'single_source' is undefined when 'single' is
 *               UF_CGM_width_single.
 *
 *               The 'widths' array is indexed by the color index straight
 *               out of the database, or 1-216.  Therefore the array is one
 *               longer than the actual number of colors, or 217.
 *
 *               Note: the structure has been devised to be amenable to
 *               increasing the number of width indices.
 *
 ****************************************************************************/
struct UF_CGM_custom_widths_s
{
    int             units;              /* Units of data in this structure:
                                             UF_PART_METRIC
                                             UF_PART_ENGLISH */
    UF_CGM_width_use_t
                    use;                /* type of width assignment to use */
    UF_CGM_width_single_t
                    single;             /* single width type selection */
    double          single_width;       /* user-defined width value */
    int             single_source;      /* source index for single width when
                                           single is _std or _custom */
    UF_CGM_width_custom_t
                    custom[UF_CGM_MAX_WIDTHS];
                                        /* per-width custom width definitions */
    UF_CGM_width_color_t
                    color[UF_CGM_MAX_COLORS];
                                        /* per-color custom width definitions */
};

typedef struct UF_CGM_custom_widths_s UF_CGM_custom_widths_t,
*UF_CGM_custom_widths_p_t;

/****************************************************************************
   The values of enumerated type UF_CGM_export_source_t identify the
   content or source for a CGM export operation, so applications can
   determine whether the source is relevant. The following values
   can be specified.

   UF_CGM_drawing_sheet: specified when exporting a drawing sheet by
   tag (e.g. non-NULL drawing tag).

   UF_CGM_current_display_is_drawing_sheet: specified when exporting
   the current display/layout, but the current layout represents a
   drawing sheet. Also specified when exporting an expanded member
   view of a drawing sheet.

   UF_CGM_current_display_is_modeling_layout: specified when exporting
   the current display/layout, but the current layout represents a
   modeling layout.
 ****************************************************************************/
typedef enum UF_CGM_export_source_e
{
    UF_CGM_drawing_sheet,
    UF_CGM_current_display_is_drawing_sheet,
    UF_CGM_current_display_is_modeling_layout

} UF_CGM_export_source_t, *UF_CGM_export_source_p_t;


/****************************************************************************
    UF_CGM_pre_export_f_t

    A pre_export callback of type UF_CGM_pre_export_f_t is invoked before
    geometry is recorded in a CGM file during a CGM export operation.
    In this function, the application might enable or disable display
    of application objects, as appropriate.

    If the application decides to take some action in response to the
    export operation, then the application can return a (void *) pointer
    to arbitrary application data in the appl_data parameter. This pointer
    will later be passed as the appl_data parameter to the post_export
    and export_error callback functions.

    The application returns TRUE from the pre_export callback if the
    operation is of interest, and FALSE otherwise. The post_export and
    export_error callback functions are not invoked unless the pre_export
    callback returns TRUE.
 ****************************************************************************/

typedef logical (*UF_CGM_pre_export_f_t)(
    UF_CGM_export_reason_t reason, /*<I> The reason that CGM export is in progress */
    UF_CGM_export_source_t source, /*<I> The source for the CGM export */
    tag_t drawing_sheet,           /*<I> The tag of the drawing sheet being exported,
                                      or NULL_TAG if the export is the current display.
                                   */
    void **appl_data               /*<I> The application data passed to the registration
                                      of the function. 
                                   */
);

/****************************************************************************
   UF_CGM_post_export_f_t

   A post_export callback of type UF_CGM_post_export_f_t is invoked after
   geometry is successfully recorded in a CGM file. In this callback,
   the application can restore the state of application objects/geometry
   and can free resources allocated for the operation.

   The post_export callback is invoked only if the pre_export callback
   returned TRUE for the same export operation.

   The post_export callback is not invoked if an error occurs during the
   export operation. The export_error callback is invoked instead.
 ****************************************************************************/

typedef void (*UF_CGM_post_export_f_t)(
    UF_CGM_export_reason_t reason, /*<I> The reason that CGM export is in progress */
    UF_CGM_export_source_t source, /*<I> The source for the CGM export */
    tag_t drawing_sheet,           /*<I> The tag of the drawing sheet being exported,
                                      or NULL_TAG if the export is the current display.
                                   */
    void *appl_data               /*<I> The application data passed to the registration
                                      of the function. This is always NULL.
                                   */
);

/****************************************************************************
    UF_CGM_export_error_f_t

    An export_error callback of type UF_CGM_export_error_f_t is invoked if
    some error occurs while generating the CGM file. In this callback,
    the application can restore the state of application objects/geometry
    and can free resources allocated for the operation. 

    The export_error callback is invoked only if the pre_export callback
    returned TRUE for the same export operation.

    If the export_error callback is invoked, then the post_export callback
    is not invoked for the same export operation.

 ****************************************************************************/
typedef void (*UF_CGM_export_error_f_t)(
    UF_CGM_export_reason_t reason, /*<I> The reason that CGM export is in progress */
    UF_CGM_export_source_t source, /*<I> The source for the CGM export */
    tag_t drawing_sheet,           /*<I> The tag of the drawing sheet being exported,
                                      or NULL_TAG if the export is the current display.
                                   */
    void *appl_data               /*<I> The application data passed to the registration
                                      of the function. This is always NULL.
                                   */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_CGM_TYPES_H_INCLUDED */
