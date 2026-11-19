/*=============================================================================
                          Copyright (c) 2004 UGS Corp.
                       Unpublished - All Rights Reserved
===============================================================================


    This NX Open example illustrates one strategy for performing a plotting
    operation that uses more than three different line widths. The example
    operation saves a CGM file to disk for each drawing sheet in the display
    part, but the same width strategy can be used when plotting jobs to a
    printer, adding plots to the plot layout, etc.

    You can use more than three different line widths in plotted output by
    associating line widths with object color indices. A displayable object
    has a color index in the range [ 1 through 216 ], so you can assign up
    to 216 different line widths. In most cases, however, your plot output
    will require only 10 or fewer line widths.

    A key step in this strategy is to decide how many different widths and
    colors you require for plotting. You must choose the number of widths
    and the number of colors so that...

        (number of different widths) * (number of different colors) <= 216

    For example, if you require 6 different widths, then you can use
    (216 / 6) = 36 different colors.

    This example uses 9 different widths and 24 different colors, so the
    example defines custom colors for plotting that specify the 24 colors
    repeated 9 times...

    + indices  1 through 24 specify the 24 colors for width #1
    + indices 25 through 48 specify the 24 colors for width #2
    + indices 49 through 72 specify the 24 colors for width #3

    ...and so forth. Also, the example defines custom widths for plotting
    that specify the 9 width values 24 times each...

    + indices  1 through 24 specify the numeric width value for width #1
    + indices 25 through 48 specify the numeric width value for width #2
    + indices 49 through 72 specify the numeric width value for width #3

    ...and so forth.

    Before performing a plotting operation, the example temporarily
    changes the color index of each object to be plotted to a value that
    will produce the desired plot width and color. After the plotting
    operation is complete, the example restores (via undo) the original
    object color indices.

    A second key step in the strategy is to specify the widths for the
    objects to be plotted. This example uses an integer attribute with
    title PLOT_WIDTH to indicate widths. That is, the example assumes that
    for the display part, some user (or some NX Open program) previously
    assigned PLOT_WIDTH integer attribute values in the range [ 1 through
    6 ] to objects of interest. The examples uses 6 custom plot widths for
    objects that have these attribute values. For any objects that do not
    have these attribute values, the example uses the 3 default custom
    widths, assigning the width according to the object width index (thin,
    normal, thick).

    A third key step in the strategy is to define plot colors. This example
    defines 24 arbitrary plot colors, and in place of each object color in
    the display part, the example simply uses the most similar of the 24 plot
    colors.

    The example performs these steps.

    1.  Define custom colors for plotting to specify the set of
        24 colors repeated 9 times.

    2.  Define custom widths for plotting to specify the 9 widths
        24 times each.

    3.  For each displayable object in the display part, if the object
        has a PLOT_WIDTH value, use the value and the object color to
        compute a new object color index for plotting. If the object
        has no PLOT_WIDTH value, use the object width index value and
        the object color to compute the new object color index.

    4.  For each drawing sheet in the display part, save a CGM file for
        the drawing sheet using the custom colors and widths applied
        according to modified object color indices.

    5.  Invoke undo to restore original object color indices.

    6.  Restore original custom colors and widths.

    This example assumes that the custom colors might already be specified
    in a color definition file (CDF) that resides in a directory created
    to store CDFs. You can set environment variable CDF_DIRECTORY to
    identify this directory, but if the variable is unset, the example
    uses a hard-coded default directory.

    This example assumes that the custom widths might already be specified
    in a width definition file (WDF) that resides in a directory created
    to store WDFs. You can set environment variable WDF_DIRECTORY to
    identify this directory, but if the variable is unset, the example
    uses a hard-coded default directory.

    This example assumes that all CGM files should be saved in a direc-
    tory created to store CGM files. You can set environment variable
    CGM_DIRECTORY to identify this directory, but if the variable is
    unset, the example uses a hard-coded default directory.

=============================================================================*/

#include <stdio.h>
#include <stdlib.h>
#include <uf.h>
#include <uf_attr.h>
#include <uf_disp.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_plot.h>
#include <uf_ui.h>
#include <uf_undo.h>
#include <string.h>

/*  The following symbols define the number of widths and colors used
    in plot output.  */

#define NUM_PLOT_COLORS          24
#define NUM_PLOT_WIDTHS           9
#define NUM_EXTRA_PLOT_WIDTHS     6


/*  Array plot_color_data defines the colors used in plot output. Each
    possible object color is mapped to the most similar of these colors.  */

typedef struct plot_color_data_s
{
    char      name[UF_PLOT_MAX_NAME_SIZE + 1];
    double    rgb_values[3];

} plot_color_data_t, *plot_color_data_p_t;

static plot_color_data_t    plot_color_data[NUM_PLOT_COLORS] =
{
    { "Pale Gray",             { 0.8,  0.8,  0.8 } },
    { "Light Gray",            { 0.6,  0.6,  0.6 } },
    { "Dark Gray",             { 0.4,  0.4,  0.4 } },
    { "Obscure Gray",          { 0.2,  0.2,  0.2 } },
    { "Black",                 { 0.0,  0.0,  0.0 } },
    { "Red",                   { 1.0,  0.0,  0.0 } },
    { "Green",                 { 0.0,  1.0,  0.0 } },
    { "Blue",                  { 0.0,  0.0,  1.0 } },
    { "Cyan",                  { 0.0,  1.0,  1.0 } },
    { "Yellow",                { 1.0,  1.0,  0.0 } },
    { "Magenta",               { 1.0,  0.0,  1.0 } },
    { "Dark Faded Red",        { 0.6,  0.0,  0.0 } },
    { "Dark Faded Green",      { 0.0,  0.6,  0.0 } },
    { "Dark Faded Blue",       { 0.0,  0.0,  0.6 } },
    { "Dark Faded Cyan",       { 0.0,  0.6,  0.6 } },
    { "Dark Faded Yellow",     { 0.6,  0.6,  0.0 } },
    { "Dark Faded Magenta",    { 0.6,  0.0,  0.6 } },
    { "Dark Weak Yellow",      { 0.4,  0.4,  0.2 } },
    { "Light Weak Red",        { 0.8,  0.6,  0.6 } },
    { "Dark Dull Orange",      { 0.6,  0.4,  0.2 } },
    { "Light Dull Orange",     { 0.8,  0.6,  0.4 } },
    { "Medium Violet Magenta", { 0.6,  0.2,  0.8 } },
    { "Dark Dull Red",         { 0.6,  0.2,  0.2 } },
    { "Dark Dull Cyan",        { 0.2,  0.6,  0.6 } }
};


/*  Array plot_width_data defines the line widths used in plot output
    (in millimeters).

    The first 3 entries in the array specify widths used for objects
    that _do not_ have PLOT_WIDTH attributes. The value of the 'width'
    field for these entries is initialized by function ask_custom_widths.

    The remaining NUM_EXTRA_PLOT_WIDTHS entries specify widths used
    for objects that have PLOT_WIDTH attributes.  */

static UF_PLOT_width_color_t    plot_width_data[NUM_PLOT_WIDTHS] =
{
    { 0.0,  UF_PLOT_WIDTH_NORMAL     },
    { 0.0,  UF_PLOT_WIDTH_THICK      },
    { 0.0,  UF_PLOT_WIDTH_THIN       },
    { 1.0,  UF_PLOT_NOT_CUSTOM_WIDTH },
    { 1.5,  UF_PLOT_NOT_CUSTOM_WIDTH },
    { 2.0,  UF_PLOT_NOT_CUSTOM_WIDTH },
    { 2.5,  UF_PLOT_NOT_CUSTOM_WIDTH },
    { 3.0,  UF_PLOT_NOT_CUSTOM_WIDTH },
    { 3.5,  UF_PLOT_NOT_CUSTOM_WIDTH }
};


/*  Macro UF_CALL invokes an NX Open function and calls check_status
    to evaluate the status/error code returned by the NX Open function.  */

#define UF_CALL(function_call) \
    (check_status(__FILE__, __LINE__, #function_call, (function_call)))


/*------------------------------------+---------------------------------------
                       PROTOTYPES FOR STATIC FUNCTIONS
--------------------------------------+-------------------------------------*/

static void ask_color_index_mapping(
    int    color_index_mapping[UF_PLOT_MAX_COLORS]);

static void ask_custom_colors(
    UF_PLOT_custom_colors_p_t    custom_colors);

static void ask_custom_widths(
    UF_PLOT_custom_widths_p_t    custom_widths);

static char *ask_file_path(
    char    *environment_variable,
    char    *default_directory,
    char    *base_file_name);

static int check_status(
    char    *source_file_name,
    int     source_file_line_number,
    char    *function_call,
    int     status);

static int delete_trailing_spaces(
    char    *string);

static void do_example(void);

static void init_plotting_options(
    UF_PLOT_job_options_p_t       job_options,
    UF_PLOT_banner_options_p_t    banner_options,
    UF_PLOT_custom_colors_p_t     original_custom_colors,
    UF_PLOT_custom_widths_p_t     original_custom_widths);

static void restore_plotting_options(
    UF_PLOT_custom_colors_p_t     original_custom_colors,
    UF_PLOT_custom_widths_p_t     original_custom_widths);

static void set_object_colors_for_plotting(
    tag_t    display_part);



void ufusr(

char    *param,
int     *retcode,
int     paramLen)

{
    if (UF_CALL(UF_initialize()) == ERROR_OK)
    {
        do_example();
        UF_CALL(UF_terminate());
    }
}


int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}


static void do_example(void)

{
    UF_PLOT_banner_options_t    banner_options;
    tag_t                       display_part;
    tag_t                       drawing_sheet;
    UF_PLOT_job_options_t       job_options;
    UF_UNDO_mark_id_t           mark_id;
    UF_PLOT_custom_colors_t     original_custom_colors;
    UF_PLOT_custom_widths_t     original_custom_widths;

    /*  If no part is displayed, do nothing.  */

    display_part = UF_PART_ask_display_part();
    if (display_part == NULL_TAG)
    {
        return;
    }

    /*  Initialize plotting options. In particular, initialize custom
        colors and custom widths to support 24 different colors and 9
        different widths.  */

    init_plotting_options(&job_options,
                          &banner_options,
                          &original_custom_colors,
                          &original_custom_widths);

    /*  Set a mark, and then temporarily modify object color indices
        so that each object will be plotted with the desired color and
        width. When the plotting operation is complete, the original
        color indices can be restored by undoing to this mark.  */

    mark_id = 0;
    UF_CALL(UF_UNDO_set_mark(UF_UNDO_invisible, NULL, &mark_id));

    set_object_colors_for_plotting(display_part);

    /*  For each drawing sheet in the display part, save a CGM file for
        the drawing sheet using the custom colors and widths applied
        according to modified object color indices.  */

    drawing_sheet = NULL_TAG;
    while ((UF_CALL(UF_OBJ_cycle_objs_in_part(display_part,
                                              UF_drawing_type,
                                              &drawing_sheet)) == ERROR_OK) &&
           (drawing_sheet != NULL_TAG))
    {
        char    *cgm_path;
        char    *job_name;

        /*  Obtain the plot job name for use as the base name of the
            CGM file.  */

        job_name = NULL;
        if (UF_CALL(UF_PLOT_ask_default_job_name(drawing_sheet,
                                                 &job_name)) != ERROR_OK)
        {
            continue;
        }

        cgm_path = ask_file_path("CGM_DIRECTORY", "C:\\cgm_files", job_name);

        if (cgm_path != NULL)
        {
            UF_CALL(UF_PLOT_save_cgm(drawing_sheet,
                                     &job_options,
                                     job_name,
                                     &banner_options,
                                     cgm_path));
            free(cgm_path);
        }

        UF_free(job_name);
    }

    /*  Undo to the previously-set mark to restore original object
        color indices.  */

    UF_CALL(UF_UNDO_undo_to_mark(mark_id, NULL));

    /*  Restore original custom colors and widths for plotting.  */

    restore_plotting_options(&original_custom_colors,
                             &original_custom_widths);

}


static void init_plotting_options(

UF_PLOT_job_options_p_t       job_options,
UF_PLOT_banner_options_p_t    banner_options,
UF_PLOT_custom_colors_p_t     original_custom_colors,
UF_PLOT_custom_widths_p_t     original_custom_widths)

{
    UF_PLOT_custom_colors_t    custom_colors;
    UF_PLOT_custom_widths_t    custom_widths;

    UF_CALL(UF_PLOT_ask_default_job_options(job_options));

    job_options->colors                   = UF_PLOT_CUSTOM_PALETTE_COLORS;
    job_options->use_drawing_sheet_colors = FALSE;
    job_options->widths                   = UF_PLOT_CUSTOM_PALETTE_WIDTHS;
    job_options->use_drawing_sheet_widths = FALSE;

    UF_CALL(UF_PLOT_ask_default_banner_options(banner_options));

    UF_CALL(UF_PLOT_ask_session_custom_colors(original_custom_colors));
    ask_custom_colors(&custom_colors);
    UF_CALL(UF_PLOT_set_session_custom_colors(&custom_colors));

    UF_CALL(UF_PLOT_ask_session_custom_widths(original_custom_widths));
    ask_custom_widths(&custom_widths);
    UF_CALL(UF_PLOT_set_session_custom_widths(&custom_widths));
}


static void restore_plotting_options(

UF_PLOT_custom_colors_p_t     original_custom_colors,
UF_PLOT_custom_widths_p_t     original_custom_widths)

{
    UF_CALL(UF_PLOT_set_session_custom_colors(original_custom_colors));
    UF_CALL(UF_PLOT_set_session_custom_widths(original_custom_widths));
}


static void set_object_colors_for_plotting(

tag_t    display_part)

{
    int      color_index_mapping[UF_PLOT_MAX_COLORS];
    tag_t    object;

    /*  Compute a color index mapping that specifies, for each of the
        216 possible object color indices, which of the 24 plot colors
        is most similar.  */

    ask_color_index_mapping(color_index_mapping);

    /*  Cycle displayable objects in the part and assign a new color
        index to each object, so it will be plotted with the desired
        color and width.  */

    object = NULL_TAG;

    while ((object = UF_OBJ_cycle_all(display_part, object)) != NULL_TAG)
    {
        UF_ATTR_value_t        attr_value;
        UF_OBJ_disp_props_t    display_properties;
        logical                displayable;
        int                    plot_color;
        int                    plot_width;
        int                    subtype;
        int                    type;

        if (UF_OBJ_ask_status(object) != UF_OBJ_ALIVE)
        {
            continue;
        }

        if ((UF_CALL(UF_OBJ_is_displayable(object,
                                           &displayable)) != ERROR_OK) ||
            (displayable == FALSE))
        {
            continue;
        }

        if ((UF_CALL(UF_OBJ_ask_type_and_subtype(object,
                                                 &type,
                                                 &subtype)) != ERROR_OK) ||
            (type == UF_component_type)                                  ||
            (type == UF_group_type)                                      ||
            ((type == UF_solid_type) && (subtype != UF_solid_body_subtype)))
        {
            continue;
        }

        if (UF_CALL(UF_OBJ_ask_display_properties(
                        object,
                        &display_properties)) != ERROR_OK)
        {
            continue;
        }

        /*  In case the object does not have a valid PLOT_WIDTH 
            attribute, prepare to use the object width index to 
            determine the plot width.  */

        if ((display_properties.line_width >= 0) &&
            (display_properties.line_width <  UF_PLOT_MAX_WIDTHS))
        {
            plot_width = display_properties.line_width;
        }
        else
        {
            plot_width = UF_PLOT_WIDTH_NORMAL;
        }

        /*  If the object has a PLOT_WIDTH integer attribute value in
            the range [ 1 through 6 ], then use this value to determine
            the plot width.  */

        if ((UF_CALL(UF_ATTR_read_value(object,
                                        "PLOT_WIDTH",
                                        UF_ATTR_integer,
                                        &attr_value)) == ERROR_OK) &&
            (attr_value.type == UF_ATTR_integer))
        {
            if ((attr_value.value.integer >= 1) &&
                (attr_value.value.integer <= NUM_EXTRA_PLOT_WIDTHS))
            {
                plot_width =
                    (UF_PLOT_MAX_WIDTHS - 1) + attr_value.value.integer;
            }
        }

        /*  Use the determined width and the object color index to compute
            a color index for plotting. Temporarily apply this color index
            to the object.  */

        plot_color = (plot_width * NUM_PLOT_COLORS) +
                     color_index_mapping[display_properties.color] + 1;

        UF_CALL(UF_OBJ_set_color(object, plot_color));
    }
}


static void ask_color_index_mapping(

int    color_index_mapping[UF_PLOT_MAX_COLORS])

{
    int    the_index;

    /*  For each of the 216 object colors stored in the part color
        table, determine which of the 24 plot colors is most similar.
        Use a simple Euclidean distance calculation to identify the
        closest color.  */

    color_index_mapping[0] = 0;

    for (the_index = 1; the_index < UF_PLOT_MAX_COLORS; the_index++)
    {
        double    blue_difference;
        int       closest_color;
        double    distance_squared;
        double    green_difference;
        double    min_distance_squared;
        double    red_difference;
        double    rgb_values[3];
        int       the_color;
        char      *unused_color_name;

        color_index_mapping[the_index] = the_index;

        if (UF_CALL(UF_DISP_ask_color(the_index,
                                      UF_DISP_rgb_model,
                                      &unused_color_name,
                                      rgb_values)) != ERROR_OK)
        {
            continue;
        }
        UF_free(unused_color_name);

        min_distance_squared = 1.0E10;
        closest_color        = 0;

        for (the_color = 0; the_color < NUM_PLOT_COLORS; the_color++)
        {
            red_difference   =
                rgb_values[0] - plot_color_data[the_color].rgb_values[0];
            green_difference =
                rgb_values[1] - plot_color_data[the_color].rgb_values[1];
            blue_difference  =
                rgb_values[2] - plot_color_data[the_color].rgb_values[2];

            distance_squared = (red_difference   * red_difference)   +
                               (green_difference * green_difference) +
                               (blue_difference  * blue_difference);

            if (min_distance_squared > distance_squared)
            {
                min_distance_squared = distance_squared;
                closest_color        = the_color;
            }
        }

        color_index_mapping[the_index] = closest_color;
    }
}


static void ask_custom_colors(

UF_PLOT_custom_colors_p_t    custom_colors)

{
    char    *cdf_path;
    int     the_color;
    int     the_index;
    int     the_width;

    cdf_path = ask_file_path("CDF_DIRECTORY",
                             "C:\\custom_color_palettes",
                             "colors_24_widths_9");

    /*  First attempt to read custom colors from the CDF.  */

    if ((cdf_path != NULL) &&
        (UF_CALL(UF_PLOT_read_custom_colors_from_cdf(
                     cdf_path, custom_colors)) == ERROR_OK))
    {
        free(cdf_path);
        return;
    }
    else
    {
        UF_CALL(UF_PLOT_ask_default_custom_colors(custom_colors));
    }

    /*  If unable to read custom colors from the CDF, then define
        custom colors from static data.  */

    the_index = 1;

    for (the_width = 0; the_width < NUM_PLOT_WIDTHS; the_width++)
    {
        for (the_color = 0; the_color < NUM_PLOT_COLORS; the_color++)
        {
            strcpy(custom_colors->colors[the_index].clr_name,
                   plot_color_data[the_color].name);
            custom_colors->colors[the_index].clr_vals[0] =
                plot_color_data[the_color].rgb_values[0];
            custom_colors->colors[the_index].clr_vals[1] =
                plot_color_data[the_color].rgb_values[1];
            custom_colors->colors[the_index].clr_vals[2] =
                plot_color_data[the_color].rgb_values[2];

            the_index++;
        }
    }

    /*  Save the custom colors in the CDF for future use.  */

    if (cdf_path != NULL)
    {
        UF_CALL(UF_PLOT_write_custom_colors_to_cdf(cdf_path,
                                                   custom_colors));
        free(cdf_path);
    }
}


static void ask_custom_widths(

UF_PLOT_custom_widths_p_t    custom_widths)

{
    int     the_color;
    int     the_index;
    int     the_width;
    char    *wdf_path;

    wdf_path = ask_file_path("WDF_DIRECTORY",
                             "C:\\custom_width_palettes",
                             "colors_24_widths_9");

    /*  First attempt to read custom widths from the WDF.  */

    if ((wdf_path != NULL) &&
        (UF_CALL(UF_PLOT_read_custom_widths_from_wdf(
                     wdf_path, custom_widths)) == ERROR_OK))
    {
        free(wdf_path);
        return;
    }
    else
    {
        UF_CALL(UF_PLOT_ask_default_custom_widths(custom_widths));
    }

    /*  If unable to read custom widths from the WDF, then define
        custom widths from static data. First convert the default
        custom widths to millimeters to ensure compatibility with
        the static data, which is specified in millimeters.  */

    UF_CALL(UF_PLOT_convert_custom_widths(UF_PLOT_MILLIMETERS,
                                          custom_widths));


    /*  Initialize the value of the 'width' field for the entries
        that represent the default custom widths.  */

    for (the_width = 0; the_width < NUM_PLOT_WIDTHS; the_width++)
    {
        if (plot_width_data[the_width].width_source != UF_PLOT_NOT_CUSTOM_WIDTH)
        {
            int    width_index;

            width_index = plot_width_data[the_width].width_source;

            plot_width_data[the_width].width =
                custom_widths->custom[width_index].width;
        }
    }

    /*  Define custom widths for plotting to specify the 9 widths
        24 times each.  */

    custom_widths->use = UF_PLOT_width_by_color;

    the_index = 1;

    for (the_width = 0; the_width < NUM_PLOT_WIDTHS; the_width++)
    {
        for (the_color = 0; the_color < NUM_PLOT_COLORS; the_color++)
        {
            custom_widths->color[the_index++] = plot_width_data[the_width];
        }
    }

    /*  Save the custom widths in the WDF for future use.  */

    if (wdf_path != NULL)
    {
        UF_CALL(UF_PLOT_write_custom_widths_to_wdf(wdf_path,
                                                   custom_widths));
        free(wdf_path);
    }
}


static char *ask_file_path(

char    *environment_variable,
char    *default_directory,
char    *base_file_name)

{
#if defined(_WIN32)
#define DELIMITER '\\'
#else
#define DELIMITER '/'
#endif

    char    *directory;
    char    *path;
    int     path_length;

    /*  NOTE:  This function returns a (char *) character string
               allocated via malloc. Callers must call free to
               free character string memory when it is no longer
               needed.  */

    path = (char *)malloc( MAX_FSPEC_BUFSIZE);
    path[0] = '\0';

    /*  If the environment variable is set, then use the directory it
        specifies. Otherwise, use the default directory.  */

    directory = NULL;

    if ((environment_variable == NULL)                           ||
        (UF_CALL(UF_translate_variable(environment_variable,
                                       &directory)) != ERROR_OK) ||
        (directory == NULL))
    {
        directory = default_directory;
    }

    /*  Append a delimiter character to the directory if one is not
        already present.  */

    if (path != NULL && directory != NULL)
    {
        strcpy(path, directory);

        path_length = delete_trailing_spaces(path);

        if ((path_length > 0) &&
            (path[path_length - 1] != DELIMITER))
        {
            path[path_length]     = DELIMITER;
            path[path_length + 1] = '\0';
        }
    }

    /*  Add the base file name to the path.  */

    if (path != NULL && base_file_name != NULL)
    {
        strcat(path, base_file_name);
    }

    path_length = delete_trailing_spaces(path);

    if (path_length == 0)
    {
        free(path);
        path = NULL;
    }

    return(path);
}


static int delete_trailing_spaces(

char    *string)

{
    int    length;

    length = 0;

    if ((string != NULL) &&
        ((length = strlen(string)) > 0))
    {
        char    *last_char;

        last_char = string + length - 1;

        while ((length > 0) &&
               (*last_char == ' '))
        {
            *(last_char--) = '\0';
            length--;
        }
    }

    return(length);
}


static int check_status(

char    *source_file_name,
int     source_file_line_number,
char    *function_call,
int     status)

{
    /*  NOTE:  Use macro UF_CALL to invoke this function.  */

    if (status != ERROR_OK)
    {
        char    *buffer;
        char    fail_message[133];

        if (UF_get_fail_message(status, fail_message) != ERROR_OK)
        {
            sprintf(fail_message, "No message for error code %d", status);
        }

        buffer = (char *)malloc(strlen(source_file_name) +
                                strlen(fail_message)     +
                                strlen(function_call)    +
                                UF_UI_MAX_STRING_BUFSIZE);

        if (buffer != NULL)
        {
            sprintf(buffer, 
                "\n*** ERROR code %d at line %d of %s\n+++ %s\n%s;\n",
                status,
                source_file_line_number,
                source_file_name,
                fail_message,
                function_call);

            UF_print_syslog(buffer, FALSE);

            if (UF_UI_open_listing_window() == ERROR_OK)
            {
                UF_UI_write_listing_window(buffer);
            }

            free(buffer);
        }
    }

    return(status);
}
