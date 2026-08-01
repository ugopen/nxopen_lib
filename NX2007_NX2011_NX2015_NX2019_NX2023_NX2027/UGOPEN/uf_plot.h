/****************************************************************************

             Copyright (c) 1998-2003 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved


 

File description:

NX Plotting

  --------
  Overview
  --------

    NX provides a modern plotting system based on commercial printing software
    from System Development Inc. (SDI). The NX plotting system generates a plot
    file in CGM or TIFF format and delivers the file to SDI software for
    printing or for conversion to another format. Details of the plotting
    functionality and the administration of printers and plotters is available
    in the NX Gateway Help collection. Please review the online documentation
    available under File -> Plotting for a detailed description of the concepts
    for using the plotting system.

  ----------------------
  Major functional areas
  ----------------------

    Provided in the UF_PLOT module are routines for

    Using printer groups and obtaining information about available printers
    and profiles.

    Specifying the job options associated with a print operation.

        You can control how colors and widths of the geometry should be rendered
        in the output and what tolerance should be used in rendering curves. You
        can ask for the default job options and ask and set the session job
        options. If the program is executed as an internal user function, the
        session job options are "shared" with the interactive Plotting dialogs.

    Specifying the banner message string and whether or not a banner should
    be added to the plot.

        You can ask for the default banner options and ask and set the session
        banner options. Again, the session options are shared with the
        interactive dialogs.

    Defining the colors for the rendering of the plot.

        You can ask the default custom colors and ask and set the session custom
        colors. You can save a particular custom color palette with a drawing
        sheet, query whether a sheet has a custom color palette, retrieve the
        custom colors for a sheet, and delete the custom colors for a sheet. You
        can read and write custom color information to an external Color
        Definition File (CDF).

    Defining the widths for the rendering of the plot.

        You can ask the default custom widths and ask and set the session custom
        widths. You can save a particular custom width palette with a drawing
        sheet, query whether a sheet has a custom width palette, retrieve the
        custom widths for a sheet, and delete the custom widths for a sheet. You
        can read and write custom width information to an external Width
        Definition File (WDF).

    Printing, Saving, and Converting the display or a drawing sheet

        You can print the current display or a drawing sheet, print a CGM or
        TIFF file previously created, and convert an existing CGM or TIFF file
        to another output format, such as JPEG, PNG, or EMF. You can save the
        current display or drawing sheet to a CGM file.

    Adding the display or drawing sheet to the current Plot Layout

        You can add the current display or a drawing sheet to the Plot Layout
        which is a mechanism for gathering several plots together in a single
        output file.  You can then send the Plot Layout to a printer / plotter
        or save the output to a CGM file.

  ---------------
  Usage scenarios
  ---------------

    Listed below are the names of sample NX Open programs that demonstrate
    various usages of the NX Plotting system along with a high level
    description of what the programs do.

    ufd_plot_drawings.c (Internal)

      Print all drawing sheets using the default settings to a known printer /
      profile. This example assumes that the default Printer Group has a printer
      named "Printer One" and it uses the SDI "system" profile.

    ufd_plot_drawings_hpgl.c (External)

      Cycle the drawing sheets of a part and print each to a queue which is
      defined to generate an HPGL-2 output file.

    ufd_plot_many_widths.c (Internal)

       Demonstrates a strategy for performing a plotting operation that 
       uses more than three different line widths.

*******************************************************************************/

#ifndef UF_PLOT_H_INCLUDE
#define UF_PLOT_H_INCLUDE


/***************************************************************************

  ***************************************************************************/

#define ERROR_UF_PLOT_base     1130000

#include <uf_defs.h>
#include <uf_plot_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

enum UF_PLOT_cmp_color_width_e
{
    UF_PLOT_CMP_COLOR_WIDTH = 1,
    UF_PLOT_CMP_NO_COLOR_WIDTH
};

typedef enum UF_PLOT_cmp_color_width_e UF_PLOT_cmp_color_width_t;


enum UF_PLOT_diff_cmp_status_e
{
    UF_PLOT_CMP_NO_DIFF_FOUND = 0,
    UF_PLOT_CMP_DIFF_FOUND
};

typedef enum UF_PLOT_diff_cmp_status_e UF_PLOT_diff_cmp_status_t;

/*
   This enum is used as an option for when to create a results plot
   when calling UF_PLOT_compare_ughpgl_files.  The results plot will
   always contain the entire image, regardless of which option is selected.
*/
enum UF_PLOT_create_cmp_result_plot_e
{
    UF_PLOT_CREATE_CMP_PLOT = 1,        /* Always create a results plot */
    UF_PLOT_CREATE_CMP_PLOT_DIFF_ONLY,  /* Create a results plot only when the
                                           two original files differ.
                                        */
    UF_PLOT_CREATE_CMP_NO_PLOT          /* Never create a results plot */
};

typedef enum UF_PLOT_create_cmp_result_plot_e UF_PLOT_create_cmp_result_plot_t;


struct UF_PLOT_ughpgl_cmp_options_s
{
    UF_PLOT_cmp_color_width_t         color_width_option;
    UF_PLOT_create_cmp_result_plot_t  resulting_plot_option;
    double                            plot_tolerance;
};

typedef struct UF_PLOT_ughpgl_cmp_options_s UF_PLOT_ughpgl_cmp_options_t,
                                           *UF_PLOT_ughpgl_cmp_options_p_t;


#define UF_PLOT_ERR_PLOT       (ERROR_UF_PLOT_base + 0) /* plot error */
#define UF_PLOT_ERR_MODE       (ERROR_UF_PLOT_base + 1) /* invalid ufun mode */
/*  */
#define UF_PLOT_ERR_QNOTFOUND  (ERROR_UF_PLOT_base + 3) /* queue not found */
#define UF_PLOT_ERR_DRAWING    (ERROR_UF_PLOT_base + 4) /* bad drawing name */
#define UF_PLOT_ERR_NOQUEUES   (ERROR_UF_PLOT_base + 5) /* no plot queues */
#define UF_PLOT_ERR_PDAEMON    (ERROR_UF_PLOT_base + 6) /* plot server error */
#define UF_PLOT_ERR_NOFILE     (ERROR_UF_PLOT_base + 7) /* no file found */
#define UF_PLOT_ERR_JOBNAME    (ERROR_UF_PLOT_base + 8) /* jobname too long */
#define UF_PLOT_ERR_PAUSEMSG   (ERROR_UF_PLOT_base + 9) /* pause msg too long */
#define UF_PLOT_ERR_PLOTTER    (ERROR_UF_PLOT_base + 10) /* invalid plotter id*/
#define UF_PLOT_ERR_NODE       (ERROR_UF_PLOT_base + 11) /* node too long */
#define UF_PLOT_ERR_BANNERMSG  (ERROR_UF_PLOT_base + 12) /* banner too long */
#define UF_PLOT_ERR_OPTION     (ERROR_UF_PLOT_base + 13) /* invalid option */
#define UF_PLOT_ERR_ROT        (ERROR_UF_PLOT_base + 14) /* invalid rotation */
#define UF_PLOT_ERR_SCALE      (ERROR_UF_PLOT_base + 15) /* invalid scale */
#define UF_PLOT_ERR_PENTYPE    (ERROR_UF_PLOT_base + 16) /* invalid pen type */
#define UF_PLOT_ERR_NOTACTV    (ERROR_UF_PLOT_base + 17) /* inactive server */
#define UF_PLOT_ERR_CREATE     (ERROR_UF_PLOT_base + 18) /* inactive server */
#define UF_PLOT_ERR_OPEN       (ERROR_UF_PLOT_base + 19) /* file open fail  */
#define UF_PLOT_ERR_TOLER      (ERROR_UF_PLOT_base + 20) /* invalid tolerance */
/*  */
#define UF_PLOT_ERR_NO_DRAWING_SHEET_COLORS   (ERROR_UF_PLOT_base + 22) /* Drawing sheet does not have assigned colors */
#define UF_PLOT_ERR_NO_DRAWING_SHEET_WIDTHS   (ERROR_UF_PLOT_base + 23) /* Drawing sheed does not have assigned widths */
#define UF_PLOT_ERR_READING_WDF (ERROR_UF_PLOT_base + 24) /* Can not read a WDF*/
#define UF_PLOT_ERR_WRITE_WDF   (ERROR_UF_PLOT_base + 25) /* Can not write a WDF*/
#define UF_PLOT_ERR_READING_CDF (ERROR_UF_PLOT_base + 26) /* Can not read a CDF*/
#define UF_PLOT_ERR_WRITE_CDF   (ERROR_UF_PLOT_base + 27) /* Can not write a CDF*/
#define UF_PLOT_ERR_EMPTY_LAYOUT (ERROR_UF_PLOT_base + 28) /* Can not plot empty layout*/

/******************************************************************************
Compares the lines created by plotter pen movements in two HPGL
plot files created in NX, and returns a resulting plot file. The resulting
plot file shows the lines which are the same and those which are
different between the plot files compared.

Environment: Internal  and  External

See Also:

History: This function was originally released in V14.0.

******************************************************************************/
extern UFUNEXPORT int UF_PLOT_compare_ughpgl_files(
char * first_plot ,/* <I>
                   Name of the first plot file (256 char max)
                   */
char * second_plot ,/* <I>
                    Name of the second plot file (256 char max)
                    */
UF_PLOT_ughpgl_cmp_options_p_t compare_options ,/* <I>
                                                Indicates options considered
                                                during comparison of plots.
                                                */
char * result_plot ,/* <I>
                    Name of resulting plot file.  If created, this resulting
                    plot file will contain the overlay of both plots.  Lines
                    that are the same in both plots will be in one color,
                    lines that are in the first plot only will be in a second
                    color, and lines that are in the second plot only will be
                    in a third color.
                    */
UF_PLOT_diff_cmp_status_t * comparison_result  /* <O>
                                               Comparison results:
                                               UF_PLOT_CMP_NO_DIFF_FOUND
                                               UF_PLOT_CMP_DIFF_FOUND
                                               */
);


/******************************************************************************
  Sets the tolerance which is used when comparing non-overlapping vectors
  between the first and second plot file. When the vectors compared are a
  distance apart of less than or equal to the shift tolerance, they are
  checked off as common vectors and not as unique vectors.

See Also :

Environment: Internal  and  External

History :
******************************************************************************/
extern UFUNEXPORT int UF_PLOT_set_ughpgl_tol(
                            double shift_tolerance,
                                   /* <I>  The amount of shift which will be
                                   allowed between two non-overlapping pair of
                                   vectors from the first and second plot file.
                                   If the vectors are within the shift amount,
                                   they are then considered one and the same.
                                   */
                            int    units
                                   /* <I>  Metric of English units.*/
 );


/******************************************************************************
  Sets the tolerance which is used when determining if a vector is ignorable.
  If a vector is less than or equal to the given length, then the line may
  be ignored if it is not matched.

See Also :

Environment: Internal  and  External
History :
******************************************************************************/
extern UFUNEXPORT int UF_PLOT_set_ughpgl_small_tol(
                            double small_tolerance,
                                   /* <I>  The maximum length of a vector that
                                    * may be ignored.
                                    */
                            int    units
                                   /* <I>  Metric of English units.*/
 );



/****************************************************************************
*                                                                           *
*           FUNCTIONS PERTAINING TO PLOT JOB OPTIONS                        *
*                                                                           *
****************************************************************************/


/****************************************************************************
Returns the default job name.  The name might include the part name, the user
name, or a descriptive string, according to job name preferences specified in
the customer defaults file.  If the specified drawing sheet tag is not NULL_TAG,
the drawing sheet name is appended to the end of the job name.  The returned
job name can be used for constructing file names and other purposes.

The name is returned (such as can be constructed) even if there are errors.
However, no name will be returned if the drawing sheet is not in the 
displayed part.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_default_job_name(
    tag_t drawing_sheet,  /* <I> If not NULL_TAG, the name of this drawing
                                 sheet is appended to the end of the job name */
    char **job_name     /* <OF> String with job name. User must free with
                           UF_free()*/
 );


/****************************************************************************
Returns the default plot job option settings.

Environment: Internal  and  External

See Also:  UF_PLOT_job_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_default_job_options(
    UF_PLOT_job_options_p_t job_options /* <O> Non-null pointer to a
                                           job options data structure. */
 );


/****************************************************************************
Returns the current plot job option settings for the session.

Environment: Internal  and  External

See Also:  UF_PLOT_job_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_session_job_options(
    UF_PLOT_job_options_p_t job_options    /* <O> Non-null pointer to a
                                           job options data structure. */
 );


/****************************************************************************
Modifies the current plot job option settings for the session. Call
UF_PLOT_ask_default_job_options or UF_PLOT_ask_session_job_options 
to initialize the UF_PLOT_job_options_t structure before setting 
structure fields.

Environment: Internal  and  External

See Also:  UF_PLOT_job_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_set_session_job_options(
    UF_PLOT_job_options_p_t job_options    /* <I> Pointer to the job options
                                              you wish to set. */
 );



/****************************************************************************
*                                                                           *
*           FUNCTIONS PERTAINING TO BANNER OPTIONS                          *
*                                                                           *
****************************************************************************/


/****************************************************************************
Returns the default banner option settings.

Environment: Internal  and  External

See Also:  UF_PLOT_banner_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_default_banner_options(
    UF_PLOT_banner_options_p_t banner_options /* <O> Non-null pointer to a
                                                 banner options data structure. */
 );


/****************************************************************************
Returns the current banner option settings for the session.

Environment: Internal  and  External

See Also:  UF_PLOT_banner_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_session_banner_options(
    UF_PLOT_banner_options_p_t banner_options /* <O> Non-null pointer to a
                                                 banner options data structure. */
 );


/****************************************************************************
Modifies the current banner option settings for the session. Call
UF_PLOT_ask_default_banner_options or UF_PLOT_ask_session_banner_options 
to initialize the UF_PLOT_banner_options_t structure before setting 
structure fields.

Environment: Internal  and  External

See Also:  UF_PLOT_banner_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_set_session_banner_options(
    const UF_PLOT_banner_options_p_t banner_options      /* <I> banner options
                                                            data structure */
 );



/****************************************************************************
*                                                                           *
*           FUNCTIONS PERTAINING TO CUSTOM COLORS                           *
*                                                                           *
****************************************************************************/


/****************************************************************************
Returns the default plotting custom colors.

Environment: Internal  and  External

See Also:  UF_CGM_custom_colors_t AKA UF_PLOT_custom_colors_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_default_custom_colors(
    UF_PLOT_custom_colors_p_t custom_colors        /* <O> Pointer to the custom
                                                      colors data structure. */
 );


/****************************************************************************
Returns the current plotting custom colors for the session.

Environment: Internal  and  External

See Also:  UF_CGM_custom_colors_t AKA UF_PLOT_custom_colors_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_session_custom_colors(
    UF_PLOT_custom_colors_p_t custom_colors    /* <O> Pointer to the custom
                                                      colors used in the session. */
 );


/****************************************************************************
Modifies the current plotting custom colors for the session. Call
one of the following functions to initialize the UF_PLOT_custom_colors_t 
structure before setting structure fields.

    UF_PLOT_ask_default_custom_colors
    UF_PLOT_ask_session_custom_colors 
    UF_PLOT_ask_drawing_sheet_colors
    UF_PLOT_read_custom_colors_from_cdf

Environment: Internal  and  External

See Also:  UF_CGM_custom_colors_t AKA UF_PLOT_custom_colors_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_set_session_custom_colors(
    UF_PLOT_custom_colors_p_t custom_colors    /* <I> Custom colors data
                                                  structure to be used for
                                                  the current session */
 );


/****************************************************************************
Returns whether or not custom colors are saved for the specified 
drawing sheet.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_has_drawing_sheet_colors(
    tag_t    drawing_sheet,             /* <I> tag of sheet to check */
    logical *drawing_sheet_has_colors /* <O> TRUE - drawing sheet colors are
                                         saved for this drawing sheet.
                                         FALSE - drawing sheet colors are not
                                         saved for this drawing sheet. */);


/****************************************************************************
Returns the current custom colors for the drawing sheet. If no
custom colors are saved for the specified drawing sheet an error is returned.

Environment: Internal  and  External

See Also:  UF_CGM_custom_colors_t AKA UF_PLOT_custom_colors_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_drawing_sheet_colors(
    tag_t                     drawing_sheet,  /* <I> tag of the sheet in question */
    UF_PLOT_custom_colors_p_t custom_colors /* <O> Pointer to the custom colors
                                               used in the drawing sheet. */ );


/****************************************************************************
Saves the specified custom colors for the indicated drawing sheet. Call 
one of the following functions to initialize the UF_PLOT_custom_colors_t 
structure before setting structure fields.

    UF_PLOT_ask_default_custom_colors
    UF_PLOT_ask_session_custom_colors 
    UF_PLOT_ask_drawing_sheet_colors
    UF_PLOT_read_custom_colors_from_cdf

Environment: Internal  and  External

See Also:  UF_CGM_custom_colors_t AKA UF_PLOT_custom_colors_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_set_drawing_sheet_colors(
    tag_t                 drawing_sheet,   /* <I> The colors will be stored with
                                            this drawing sheet */
    UF_PLOT_custom_colors_p_t custom_colors /* <I> Colors to store with the
                                               drawing sheet */);


/****************************************************************************
Deletes custom colors saved for the specified drawing sheet.  An error
code is returned if the drawing sheet has no custom colors.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_delete_drawing_sheet_colors(
    tag_t    drawing_sheet /* <I> Colors will be deleted from this drawing */ );


/****************************************************************************
Initializes a UF_PLOT_custom_colors_t structure according to color data stored
in the specified CDF.

Environment: Internal  and  External

See Also:  UF_CGM_custom_colors_t AKA UF_PLOT_custom_colors_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_read_custom_colors_from_cdf(
    const char *                cdf_name,       /* <I> Name of CDF to use */
    UF_PLOT_custom_colors_p_t   custom_colors   /* <O> Color data found in the CDF */);


/****************************************************************************
Saves the custom colors in a CDF with the specified name.
Note that the suffix .cdf is appended to the name if not present.
If a CDF of the same name already exists it is overwritten.

Call one of the following functions to initialize the UF_PLOT_custom_colors_t 
structure before setting structure fields.

    UF_PLOT_ask_default_custom_colors
    UF_PLOT_ask_session_custom_colors 
    UF_PLOT_ask_drawing_sheet_colors
    UF_PLOT_read_custom_colors_from_cdf

Environment: Internal  and  External

See Also:  UF_CGM_custom_colors_t AKA UF_PLOT_custom_colors_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_write_custom_colors_to_cdf(
    const char *                cdf_name,       /* <I> Name of CDF to use */
    UF_PLOT_custom_colors_p_t   custom_colors   /* <I> Color data to write in the CDF */

    );


/****************************************************************************
*                                                                           *
*           FUNCTIONS PERTAINING TO CUSTOM WIDTHS                           *
*                                                                           *
****************************************************************************/



/****************************************************************************
Converts numeric values stored in the UF_PLOT_custom_widths_t structure to the
specified units, and then updates the units field of the structure.  This
function can be called to ensure custom widths are expressed in appropriate
units after obtaining the widths from a drawing sheet or WDF.

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t AKA UF_PLOT_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_convert_custom_widths(
    UF_PLOT_units_t           units,   /* <I> UF_PLOT_MILLIMETERS - the custom
                                         width data is converted to millimeters.
                                         UF_PLOT_INCHES - the custom width is
                                         converted to inches */
    UF_PLOT_custom_widths_p_t custom_widths   /* <I/O> custom widths data
                                                      structure to convert */
 );


/****************************************************************************
Returns the default plotting custom widths.

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t AKA UF_PLOT_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_default_custom_widths(
    UF_PLOT_custom_widths_p_t custom_widths        /* <O> default custom widths */
 );


/****************************************************************************
Returns the current plotting custom widths for the session.

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t AKA UF_PLOT_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_session_custom_widths(
    UF_PLOT_custom_widths_p_t custom_widths        /* <O> current session widths */
 );


/****************************************************************************
Modifies the current plotting custom widths for the session. Call one 
of the following functions to initialize the UF_PLOT_custom_widths_t 
structure before setting structure fields.

    UF_PLOT_ask_default_custom_widths
    UF_PLOT_ask_session_custom_widths 
    UF_PLOT_ask_drawing_sheet_widths
    UF_PLOT_read_custom_widths_from_wdf

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t AKA UF_PLOT_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_set_session_custom_widths(
    UF_PLOT_custom_widths_p_t custom_widths        /* <I> custom widths to set
                                                      for the current session*/
 );


/****************************************************************************
Returns whether or not custom widths are saved for the specified drawing sheet.

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t AKA UF_PLOT_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_has_drawing_sheet_widths(
    tag_t    drawing_sheet,             /* <I> tag of sheet to check */
    logical *drawing_sheet_has_widths /* <O> TRUE - drawing sheet widths are
                                         saved for this drawing sheet.
                                         FALSE - drawing sheet widths are not
                                         saved for this drawing sheet. */);


/****************************************************************************
Returns the current custom widths for the drawing sheet.  If no custom
widths are saved for the specified drawing sheet an error is returned.

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t AKA UF_PLOT_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_drawing_sheet_widths(
    tag_t                     drawing_sheet, /* <I> tag of the sheet in question */
    UF_PLOT_custom_widths_p_t    custom_widths /* <O> Pointer to the custom widths
                                                  used in the drawing sheet. */);

/****************************************************************************
Saves the specified widths for the indicated drawing sheet. Call one 
of the following functions to initialize the UF_PLOT_custom_widths_t 
structure before setting structure fields.

    UF_PLOT_ask_default_custom_widths
    UF_PLOT_ask_session_custom_widths 
    UF_PLOT_ask_drawing_sheet_widths
    UF_PLOT_read_custom_widths_from_wdf

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t AKA UF_PLOT_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_set_drawing_sheet_widths(
    tag_t                     drawing_sheet,  /* <I> The widths will be stored with
                                               this drawing sheet */
    UF_PLOT_custom_widths_p_t    custom_widths /* <I> Width to store with the
                                               drawing sheet */);

/****************************************************************************
Deletes drawing sheet widths saved for the specified drawing sheet.  An error
code is returned if the drawing sheet has no widths.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_delete_drawing_sheet_widths(
    tag_t    drawing_sheet /* <I> Widths will be deleted from this drawing */);


/****************************************************************************
Initializes a UF_PLOT_custom_widths_t structure according to width data stored
in the specified WDF.

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t AKA UF_PLOT_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_read_custom_widths_from_wdf(
    const char *                wdf_name,       /* <I> Name of WDF to use */
    UF_PLOT_custom_widths_p_t   custom_widths   /* <O> Width data found in the WDF */);


/****************************************************************************
Saves the custom width data in a WDF with the specified name.
Note that the suffix .wdf is appended to the name if not present.
If a WDF of the same name already exists it is overwritten.

Call one of the following functions to initialize the UF_PLOT_custom_widths_t 
structure before setting structure fields.

    UF_PLOT_ask_default_custom_widths
    UF_PLOT_ask_session_custom_widths 
    UF_PLOT_ask_drawing_sheet_widths
    UF_PLOT_read_custom_widths_from_wdf

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t AKA UF_PLOT_custom_widths_t


History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_write_custom_widths_to_wdf(
    const char *                wdf_name,       /* <I> Name of WDF to use */
    UF_PLOT_custom_widths_p_t   custom_widths   /* <I> Width data to write in the WDF */
);

/****************************************************************************
*                                                                           *
*           FUNCTIONS PERTAINING TO PRINTERS                                *
*                                                                           *
****************************************************************************/

/****************************************************************************
Returns the printer groups if the printer group list file exists.
Otherwise, returns zero printer groups.

More information about the Printer Group List File is available under
the Printer Administration section in the Gateway Help documentation.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_printer_groups(
    int                  *num_printer_groups, /* <O> Number of printer groups */

    UF_PLOT_printer_group_p_t *printer_groups /* <OF,len:num_printer_groups> Printer groups array.
                                                 Must be freed with UF_free() */
 );

/****************************************************************************
Sets the current printer group

The jobs_dir and home_dir parameters can be NULL, in which case the default 
jobs and home directories are used. If group_dir specifies a printer group
in the printer group list file, however, then jobs_dir and home_dir should
be set to the values returned by UF_PLOT_ask_printer_groups for group_dir.

If the jobs and home directories exist, they must be writable. If they do 
not exist, it must be possible to create them.

If the jobs_dir is passed a string with a trailing backslash, the directory
will not be created.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_set_printer_group(
    const char    *group_dir,                       /* <I> Group directory */
    const char    *jobs_dir,                        /* <I> Jobs directory */
    const char    *home_dir                         /* <I> Home directory */
 );

/****************************************************************************
Returns the names of the printers for the current printer group.
Each printer name in the array must be freed with UF_free, and the array of
printer names must also be freed with UF_free. NULL is returned if
there are no printers.

Environment: Internal and External

History: Originally released in NX3.0.

****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_printer_names(
    int                           *num_printers, /* <O> Number of printers in
                                                    the current printer group. */
    char                          ***printers /* <OF,len:num_printers> Names of the printers in
                                                 the current printer group.
                                                 Each name and the array
                                                 of names must be freed with
                                                 UF_free() */ );

/****************************************************************************
Returns the name of the default printer and default profile for the current
printer group.  Both arrays must be freed with UF_free.

Environment: Internal and External

History: Originally released in NX3.0.

****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_default_printer_and_profile(
    char                          **printer, /* <OF> The default printer in the
                                                current printer group. Must be
                                                freed with UF_free() */
    char                          **profile /* <OF> The default profile in the
                                               current printer group.  Must be
                                               freed with UF_free() */ );

/****************************************************************************
Returns an allocated array of the profile names associated with the
given printer in the current printer group. Each profile name in the array
must be freed with UF_free, and the array of profile names must also be freed
with UF_free.

Environment: Internal and External

History: Originally released in NX3.0.

****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_profile_names(
    const char                    *printer, /* <I> The name of a printer in
                                               the current printer group */
    int                           *num_profiles, /* <O> The number of profiles
                                                    associated with the given printer.*/
    char                          ***profiles /* <OF,len:num_profiles> The profile names associated with the
                                                 given printer in the current group.
                                                 Each name and the array
                                                 of names must be freed with
                                                 UF_free() */ );


/****************************************************************************
*                                                                           *
*           FUNCTIONS FOR MANAGING THE PLOT LAYOUT                          *
*                                                                           *
****************************************************************************/


/****************************************************************************
Adds a plot job to the plot layout, and outputs the rectangular bounds of the
plot in the specified units coordinates.
NOTE - If an error occurs during execution, the plot layout will be cleared.

Environment: Internal  and  External

See Also:  UF_PLOT_job_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_add_job_to_plot_layout(
    tag_t                       drawing_sheet,  /* <I> Tag of drawing sheet.  If this
                                                    is NULL_TAG, the current display
                                                    is being plotted. */
    UF_PLOT_job_options_p_t     job_options,    /* <I> Specifies plot job options.
                                                    If NULL, current session job 
                                                    options are used instead. If 
                                                    non-NULL, call 
                                                    UF_PLOT_ask_default_job_options 
                                                    or 
                                                    UF_PLOT_ask_session_job_options 
                                                    to initialize the structure before
                                                    setting structure fields. Current 
                                                    session job options are not 
                                                    modified by structure values. */
    const char *                job_name,       /* <I> Name of the job */
    UF_PLOT_units_t             units,          /* <I> Units used to define the plot origin
                                                    and extents. */
    double                      origin[2],      /* <I> The location of the plot origin
                                                    expressed in the specified units. */
    UF_PLOT_rotation_t          rotation,       /* <I> Defines the orientation of the
                                                    plot in the plot layout. */
    double                      scale,          /* <I> Defines the scale of the plot in
                                                    the plot layout. */
    UF_PLOT_extents_p_t         extents         /* <O> If non-NULL the rectangular bounds of
                                                    the plot in the layout (the coordinates of
                                                    the lower-left and the upper-right corners
                                                    of the plot in millimeters or inches as
                                                    indicated by the units parameter) are
                                                    returned. */
 );


/****************************************************************************
Saves the plot layout in a CGM file with the specified name.  Note that the
suffix .cgm is appended to the name if not present.  If a CGM file of the
same name already exists, it is overwritten.
Environment: Internal  and  External

See Also:  UF_PLOT_banner_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_save_cgm_for_plot_layout(
    const char *                job_name,       /* <I> Name for the plot job */
    UF_PLOT_banner_options_p_t  banner_options, /* <I> Specifies banner options.
                                                    If NULL, current session 
                                                    banner options are used 
                                                    instead. If non-NULL, call 
                                                    UF_PLOT_ask_default_banner_options 
                                                    or 
                                                    UF_PLOT_ask_session_banner_options 
                                                    to initialize the structure 
                                                    before setting structure 
                                                    fields. Current session banner
                                                    options are not modified by 
                                                    structure values. */
    const char *                cgm_file_name   /* <I> CGM file name */
 );


/****************************************************************************
Prints the plot layout.

Environment: Internal  and  External

See Also:  UF_PLOT_banner_options_t

Returns: UF_PLOT_ERR_EMPTY_LAYOUT if the plot layout is empty.

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_print_plot_layout(
    const char *                job_name,       /* <I> Name for the plot job */
    UF_PLOT_banner_options_p_t  banner_options, /* <I> Specifies banner options.
                                                    If NULL, current session 
                                                    banner options are used 
                                                    instead. If non-NULL, call 
                                                    UF_PLOT_ask_default_banner_options 
                                                    or 
                                                    UF_PLOT_ask_session_banner_options 
                                                    to initialize the structure 
                                                    before setting structure 
                                                    fields. Current session banner
                                                    options are not modified by 
                                                    structure values. */
    const char *                printer,        /* <I> Specifies the name of the printer on
                                                    which the job is to be printed.  If NULL, the
                                                    default printer is used. */
    const char *                profile,        /* <I> Specifies the name of the desired profile for the
                                                    printer.  If NULL, the default profile is used. */
    int                         num_copies      /* <I> Number of copies to print. */
);


/****************************************************************************
Returns the total bounds of the plot layout, the lower-left and upper-right
corners of the smallest rectangle that encloses all plots, in millimeters or
inches as indicated by the units parameter.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_ask_plot_layout_extents(
    UF_PLOT_units_t units, /* <I> UF_PLOT_MILLIMETERS - the extents are
                              returned in millimeters.
                              UF_PLOT_INCHES - the extents are returned in
                              inches */
    UF_PLOT_extents_p_t extents /* <O> The rectangular bounds of the plot in
                                   the layout. */
);


/****************************************************************************
Removes all plots from the plot layout, leaving it empty.
NOTE - This routine is unnecessary after a successful call to
UF_PLOT_save_cgm_for_plot_layout or UF_PLOT_print_plot_layout as they
automatically clear the plot layout upon successful execution.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_clear_plot_layout( void );


/****************************************************************************
Saves a plot job in a CGM file with the specified name.  The Suffix .cgm is
appended to the name if it is not present.  If a CGM file of the same name
already exists, it is overwritten.  The drawing sheet provided must be in 
the displayed part.

Environment: Internal  and  External

See Also:  UF_PLOT_job_options_t
 UF_PLOT_banner_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_save_cgm(
    tag_t                       drawing_sheet,  /* <I> The plot job represents this
                                                    drawing sheet.  If NULL_TAG, the
                                                    plot job represents the current
                                                    display image.*/
    UF_PLOT_job_options_p_t     job_options,    /* <I> Specifies plot job options.
                                                    If NULL, current session job 
                                                    options are used instead. If 
                                                    non-NULL, call 
                                                    UF_PLOT_ask_default_job_options 
                                                    or 
                                                    UF_PLOT_ask_session_job_options 
                                                    to initialize the structure before
                                                    setting structure fields. Current 
                                                    session job options are not 
                                                    modified by structure values. */
    const char *                job_name,       /* <I> Name for the plot job */
    UF_PLOT_banner_options_p_t  banner_options, /* <I> Specifies banner options.
                                                    If NULL, current session 
                                                    banner options are used 
                                                    instead. If non-NULL, call 
                                                    UF_PLOT_ask_default_banner_options 
                                                    or 
                                                    UF_PLOT_ask_session_banner_options 
                                                    to initialize the structure 
                                                    before setting structure 
                                                    fields. Current session banner
                                                    options are not modified by 
                                                    structure values. */
    const char *                cgm_file_name   /* <I> CGM file name */
 );

/****************************************************************************
Prints a plot job.  The drawing sheet provided must be in the displayed part.
Environment: Internal  and  External

See Also:  UF_PLOT_job_options_t
 UF_PLOT_banner_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_print(
    tag_t                       drawing_sheet,  /* <I> The plot job represents this drawing sheet.
                                                    If NULL_TAG, the plot job represents the current
                                                    display image.*/
    UF_PLOT_job_options_p_t     job_options,    /* <I> Specifies plot job options.
                                                    If NULL, current session job 
                                                    options are used instead. If 
                                                    non-NULL, call 
                                                    UF_PLOT_ask_default_job_options 
                                                    or 
                                                    UF_PLOT_ask_session_job_options 
                                                    to initialize the structure before
                                                    setting structure fields. Current 
                                                    session job options are not 
                                                    modified by structure values. */
    const char *                job_name,       /* <I> Name of job to print. */
    UF_PLOT_banner_options_p_t  banner_options, /* <I> Specifies banner options.
                                                    If NULL, current session 
                                                    banner options are used 
                                                    instead. If non-NULL, call 
                                                    UF_PLOT_ask_default_banner_options 
                                                    or 
                                                    UF_PLOT_ask_session_banner_options 
                                                    to initialize the structure 
                                                    before setting structure 
                                                    fields. Current session banner
                                                    options are not modified by 
                                                    structure values. */
    const char *                printer,        /* <I> Specifies the name of the printer on
                                                    which the job is to be printed.  If NULL, the
                                                    default printer is used. */
    const char *                profile,        /* <I> Specifies the name of the desired profile for the
                                                    printer.  If NULL, the default profile is used. */
    int                         num_copies      /* <I> Number of copies to print. */
 );

/****************************************************************************
Prints the CGM or TIFF file with the specified name.
Environment: Internal  and  External

See Also:

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_print_file(
    const char *    filename,   /* <I> Name of CGM or TIFF file to print */
    const char *    printer,    /* <I> Specifies the name of the printer on which the
                                    job is to be printed.  If NULL, the default printer
                                    is used. */
    const char *    profile,    /* <I> Specifies the name of the desired profile for the
                                    printer.  If NULL, the default profile is used. */
    int             num_copies  /* <I> Number of copies to print. */
    );



/****************************************************************************
Parses the indicated CGM or TIFF file, converts the CGM or TIFF data to the
graphics format indicated by the output_format parameter, and saves the
converted data in a file with the specified name, appending an appropriate
suffix if necessary.  If a file of the same name already exists, it is
overwritten.  Note that this call uses the plotting system to do the conversion
so the plotting system must be configured correctly.  In particular the 
graphics format that you choose needs to have proper defaults in the NX Print
Print Setup page.  In particular the Pixel Dimensions must be non-zero.

Starting in NX 5.0.2, the TIFF conversion is done by calling the cgm2tiff 
program released in the NXPLOT kit.  The resolution for this conversion is
forced to 72 DPI.  You can force the old behavior (which uses the plotting
system) by setting the environment variable UGII_PLOT_CONVERT_OLD_BEHAVIOR.

By far the best way to do a TIFF conversion will be to bypass this call 
completely, and directly call the cgm2tiff program to do the conversion
once you have created a CGM file.  The cgm2tiff program has options so that
you can control the resolution, scale and rotation of the TIFF file.

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_PLOT_convert_file(
    const char *        cgm_or_tiff_file_name,  /* <I> Name of CGM or TIFF file to convert */
    UF_PLOT_format_t    output_format,          /* <I> Format used to create the output file */
    const char *        output_file_name        /* <I> Name of converted file */
);





#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif
