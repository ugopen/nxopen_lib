/*******************************************************************************

   Copyright (c) 1998-2001 Unigraphics Solutions Inc.
                 Unpublished - All rights reserved

*******************************************************************************





File description:

   Internal type definitions for UF_SF_LEGEND (Scenario Legend) module.

   The LEGEND module uses an attribute structure in order to define what
   is displayed in the legend.  The attribute structure should be built
   by the application using the functions provided in the LEGEND API.  The
   functions assist in allocating and freeing the attribute structure and
   in adding text strings in order to display. Assigning simple values to
   the attribute structure is left to the application.

   It is not necessary for applications to define each and every attribute
   for the legend if the default is what is wanted.  This is the reason for
   attribute masks for each structure in the attribute structure.
   Application code sets the desired attributes to define and then sets the
   corresponding value in the attribute structure.  For adding text strings,
   convenience functions are provided.

   The best way to learn how to use this API is some example code which is
   provided below.  The examples both show the use of the LEGEND API as
   well as the CGP_PART API since the latter is an integral part of
   display scalar fringes and such.

*******************************************************************************/


#ifndef UF_SF_LEGEND_H_INCLUDED
#define UF_SF_LEGEND_H_INCLUDED

#include <uf_defs.h>
#include <uf_sf_types.h>

#ifdef __cplusplus
extern "C" {
#endif


#ifdef LEGEND_COMPILE_EXAMPLE_CODE
  /************************************************************************
   * Example - Generate a 3 color fringe legend using user defined        *
   * color index labeling. The labeling is wanted in the middle of the    *
   * discreate color index band instead of at the threshold point of each *
   * color range. This index is for a safety factor so the color range    *
   * values are predefined.  Negative values are used so that a top to    *
   * bottom "red", "yellow", "green" can be used with "red" values close  *
   * to zero. This is a cgp_part restriction.                             *
   ************************************************************************/

    int    num_colors = 3;

    tag_t legend_view = NULL_TAG;

    char  displ_str[256];
    char  real_str[MAX_LINE_BUFSIZE];
    char  *displ_title_1 = "Structural";
    char  *displ_title_2 = "Performance";
    char  *safe_title = "Safety Factor =";
    char  *index_title_1 = "Safe";
    char  *index_title_2_1 = "Exceeds";
    char  *index_title_2_2 = "Safety";
    char  *index_title_2_3 = "Factor";
    char  *index_title_3 = "Failure";

    double max_res, min_res;
    UF_SF_COLOR_attr_t    color_attr;
    UF_SF_LEGEND_attr_p_t legend_attr_p = NULL;
    UF_SF_LEGEND_title_p_t title_p;

    /* Get extreme result values */
    UF_SF_get_extreme_mesh_results (&max_res, &min_res);

    /***************************************
     * fill the color attribute structure  *
     ***************************************/
    color_attr.num_ranges = num_colors;

    color_attr.ranges = UF_allocate_memory( sizeof(double) * (num_colors+1), &error) ;
    if (error ) UF_get_fail_message(error, fail_message ) ;
    color_attr.ranges[0] = -100.0;
    color_attr.ranges[1] = -2.0;
    color_attr.ranges[2] = -1.0;
    color_attr.ranges[3] = 0.0;

    color_attr.rgb_values = UF_allocate_memory( sizeof(double) * num_colors * 3, &error) ;
    if (error ) UF_get_fail_message(error, fail_message ) ;

    color_attr.rgb_values[0] = 0.0;       /*green*/
    color_attr.rgb_values[1] = 1.0;
    color_attr.rgb_values[2] = 0.0;

    color_attr.rgb_values[3] = 1.0;       /*yellow*/
    color_attr.rgb_values[4] = 1.0;
    color_attr.rgb_values[5] = 0.0;

    color_attr.rgb_values[6] = 1.0;       /*red*/
    color_attr.rgb_values[7] = 0.0;
    color_attr.rgb_values[8] = 0.0;

    /***************************************
     * setup the color fringing attributes *
     ***************************************/

    error = UF_SF_LEGEND_set_colors(&color_attr);
    if (error) UF_get_fail_message(error, fail_message );

    /*******************************
     * setup the legend attributes *
     *******************************/
    UF_SF_LEGEND_new_attr(&legend_attr_p);
    legend_attr_p->attr_mask = UF_LEGEND_WIDTH_ATTR | UF_LEGEND_HEADER_ATTR | UF_LEGEND_INDEX_ATTR;
    legend_attr_p->width_percent = 15;

    /* header */
    UF_SF_LEGEND_add_title_line (&legend_attr_p->header, displ_title_1);
    UF_SF_LEGEND_add_title_line (&legend_attr_p->header, displ_title_2);
    UF_SF_LEGEND_add_title_line (&legend_attr_p->header," ");
    UF_SF_LEGEND_add_title_line (&legend_attr_p->header, safe_title);
    UF_SF_LEGEND_format_real_to_str (-min_res, real_str);
    sprintf(displ_str, "    %s+", real_str);
    UF_SF_LEGEND_add_title_line (&legend_attr_p->header, displ_str);

    /* overall index */
    legend_attr_p->index_attr.attr_mask = UF_LEGEND_INDEX_HEIGHT_ATTR |
                                          UF_LEGEND_INDEX_COLOR_ATTR  |
                                          UF_LEGEND_INDEX_TEXT_ATTR;

    legend_attr_p->index_attr.height_percent = 60;

    /* color index */
    legend_attr_p->index_attr.color_attr.attr_mask = UF_LEGEND_INDEX_COLOR_WIDTH_ATTR |
                                                     UF_LEGEND_INDEX_COLOR_SMOOTH_ATTR;
    legend_attr_p->index_attr.color_attr.width_percent = 30;
    legend_attr_p->index_attr.color_attr.smooth_sw = FALSE;
    legend_attr_p->index_attr.color_attr.num_values = num_colors;
    legend_attr_p->index_attr.color_attr.values = color_attr.ranges;

    /* text index */
    legend_attr_p->index_attr.text_attr.attr_mask = UF_LEGEND_INDEX_TEXT_JUSTIFY_ATTR;
    legend_attr_p->index_attr.text_attr.justify = UF_LEGEND_CENTER_JUSTIFIED_TEXT;

    /* since the legend titles are wanted in the middle of the color index
       there are 3 color indicies so specify 7 index titles with the
       2nd, 4th and 6th titles with text */

    UF_SF_LEGEND_add_index_text_title (legend_attr_p, &title_p); /*one*/

    UF_SF_LEGEND_add_index_text_title (legend_attr_p, &title_p); /*two*/
    UF_SF_LEGEND_add_title_line (title_p, index_title_1);

    UF_SF_LEGEND_add_index_text_title (legend_attr_p, &title_p); /*three*/

    UF_SF_LEGEND_add_index_text_title (legend_attr_p, &title_p); /*four*/
    UF_SF_LEGEND_add_title_line (title_p, index_title_2_1);
    UF_SF_LEGEND_add_title_line (title_p, index_title_2_2);
    UF_SF_LEGEND_add_title_line (title_p, index_title_2_3);

    UF_SF_LEGEND_add_index_text_title (legend_attr_p, &title_p); /*five*/

    UF_SF_LEGEND_add_index_text_title (legend_attr_p, &title_p); /*six*/
    UF_SF_LEGEND_add_title_line (title_p, index_title_3);

    UF_SF_LEGEND_add_index_text_title (legend_attr_p, &title_p); /*seven*/

    /* do the deed */
    error = UF_SF_LEGEND_create_legend(legend_attr_p,&legend_view);

    .
    .
    UF_SF_LEGEND_free_attr (legend_attr_p);

#endif /* LEGEND_COMPILE_EXAMPLE_CODE */


/***************************************************************************
  UF_SF_LEGEND_REAL_STR_SZ is being deprecated.  It was
  used to define the string length of a character string in the
  LEGEND_format_real_to_str function. Use MAX_LINE_BUFSIZE declared in
  uf_defs.h instead
  
***************************************************************************/
/*  */
#define UF_SF_LEGEND_REAL_STR_SZ   (MAX_LINE_BUFSIZE-1)
/*  */

/***************************************************************************
  Text justification for titles in the user defined color index text.
***************************************************************************/
enum UF_SF_LEGEND_text_justification_e
{
    UF_LEGEND_LEFT_JUSTIFIED_TEXT   = 1,
    UF_LEGEND_CENTER_JUSTIFIED_TEXT = 2,
    UF_LEGEND_RIGHT_JUSTIFIED_TEXT  = 3
};
typedef enum UF_SF_LEGEND_text_justification_e UF_SF_LEGEND_text_justification_t;

/***************************************************************************
  Title structures are used for text so that multiple lines of text
  can be defined for headers, footers, and user defined index text.
***************************************************************************/
struct UF_SF_LEGEND_title_s
{
    int num_strs;   /* Number of strings in the title */
    char **strs;    /* <len:num_strs>
                        Array of strings               */
};
typedef struct UF_SF_LEGEND_title_s UF_SF_LEGEND_title_t, *UF_SF_LEGEND_title_p_t;

/***************************************************************************
  The following are the definitions used to define user defined color
  index text.  The application can directly set the text justification
  value but should use the functions: UF_SF_LEGEND_add_index_text_title,
  UF_SF_LEGEND_add_title_line, in order to build the index text.
***************************************************************************/

#define UF_LEGEND_INDEX_TEXT_JUSTIFY_ATTR     0x0001

struct UF_SF_LEGEND_index_text_attr_s
{
    unsigned int attr_mask;     /* This field is set to one or more of the following
                                   symbols OR'd together to indicate which of the
                                   remaining fields of the structure are set.
                                       UF_LEGEND_INDEX_TEXT_JUSTIFY_ATTR      */
    UF_SF_LEGEND_text_justification_t justify;
                               /* Justification of text in the legend
                                default: UF_LEGEND_RIGHT_JUSTIFIED_TEXT */
    int                    num_titles;
                               /* Number of title structures */
    UF_SF_LEGEND_title_p_t *titles;
                               /* <len:num_titles>
                Pointer to instances of title structures */

};
typedef struct UF_SF_LEGEND_index_text_attr_s UF_SF_LEGEND_index_text_attr_t, *UF_SF_LEGEND_index_text_attr_p_t;

/***************************************************************************
  The following are the definitions used to define the color index of
  the legend.  This is main part of most legend areas.
***************************************************************************/

#define UF_LEGEND_INDEX_COLOR_WIDTH_ATTR     0x0001
#define UF_LEGEND_INDEX_COLOR_SMOOTH_ATTR    0x0002

struct UF_SF_LEGEND_index_color_attr_s
{
    unsigned int attr_mask;     /* This field is set to one or more of the following
                                   symbols OR'd together to indicate which of the
                                   remaining fields of the structure are set.
                                       UF_LEGEND_INDEX_COLOR_WIDTH_ATTR
                                       UF_LEGEND_INDEX_COLOR_SMOOTH_ATTR      */
    int        width_percent;  /* The percentage of the legend area which the color
                                  index fills. The index is always on the right side
                                  default value: 30% */
    logical    smooth_sw;      /* Switch indicating whether or not the color index
                                  represents smooth continuous colors or
                                  discrete color bands as follows:
                                  = TRUE  -> smooth color index (default)
                                  = FALSE -> discrete color index. */
    int        num_values;     /* Number of colors in index.  Must be >= 2.
                                  Mandatory if color index is specified */
    double     *values;        /* <len:num_values>
                                  Array[num_values] in size. Scalar value associated
                                  as the starting value of each color in the index.
                                  Memory should not be freed until legend is deleted.
                                  Mandatory if color index is specified. */
};
typedef struct UF_SF_LEGEND_index_color_attr_s UF_SF_LEGEND_index_color_attr_t, *UF_SF_LEGEND_index_color_attr_p_t;

/***************************************************************************
   The following are the definitions used to define the overall
   attributes of the index area.
***************************************************************************/

#define UF_LEGEND_INDEX_HEIGHT_ATTR     0x0001
#define UF_LEGEND_INDEX_COLOR_ATTR      0x0002
#define UF_LEGEND_INDEX_TEXT_ATTR       0x0004

struct UF_SF_LEGEND_index_attr_s
{
    unsigned int attr_mask;       /* This field is set to one or more of the following
                                     symbols OR'd together to indicate which of the
                                     remaining fields of the structure are set.
                                         UF_LEGEND_INDEX_HEIGHT_ATTR
                                         UF_LEGEND_INDEX_COLOR_ATTR
                                         UF_LEGEND_INDEX_TEXT_ATTR      */
    int          height_percent;  /* The percentage of the legend area which the
                                     index fills. The index is placed in the
                                     middle of the legend unless there is a long
                                     header in which case the index follows
                                     directly after. default: 50% */
    UF_SF_LEGEND_index_color_attr_t color_attr;
                                 /* The attributes of the color index
                                    default: none specified */
    UF_SF_LEGEND_index_text_attr_t  text_attr;
                                 /* The attributes of the text index
                                    If not specified, default labeling will be used
                                    for the color index.  default: none specified */
};
typedef struct UF_SF_LEGEND_index_attr_s UF_SF_LEGEND_index_attr_t, *UF_SF_LEGEND_index_attr_p_t;

/***************************************************************************
  The following are the definitions used to define parameters of the
  scalar-to-color mapping that is used in rendering fringe displays.
****************************************************************************/
struct UF_SF_COLOR_attr_s
{

    int         num_ranges;   /* Number of of discrete ranges of scalar
                                 values in the scalar-to-color mapping. */
    double      *ranges;      /* <len:num_ranges>
                                 Array of size num_ranges defining
                                 ranges of scalar values, each of which
                                 maps to a different color.
                                 It is an array of (num_ranges + 1) double
                                 scalar values, where the minimum and
                                 maximum scalar value for the ith range
                                 are given by ranges[i] and
                                 and ranges[i + 1], respectively.
                                 The scalar ranges map to the colors in the
                                 rgb_values field, if specified, or to linear
                                 increments of the HSV blue-to-red model,
                                 otherwise. */
    double     *rgb_values;      /* <len:num_ranges*3>
                                 Array of RGB triples where each triple
                                 consists of red, green, and blue
                                 double-precision numbers.
                                 Scalar values in the ith range map to the
                                 ith RGB triple, given by:
                                 {  rgb_values[(i],       <-- RED
                                    rgb_values[(i + 1],   <-- GREEN
                                    rgb_values[(i + 2] }  <-- BLUE

                                 The size of the array of triples is num_ranges*3 */

};
typedef struct UF_SF_COLOR_attr_s UF_SF_COLOR_attr_t, *UF_SF_COLOR_attr_p_t;

/***************************************************************************
  The following are the definitions used to define the overall legend
  attributes.
****************************************************************************/

#define UF_LEGEND_WIDTH_ATTR            0x0001
#define UF_LEGEND_BORDER_ATTR           0x0002
#define UF_LEGEND_FONT_SIZE_ATTR        0x0004
#define UF_LEGEND_HEADER_ATTR           0x0008
#define UF_LEGEND_INDEX_ATTR            0x0010
#define UF_LEGEND_FOOTER_ATTR           0x0020

struct UF_SF_LEGEND_attr_s
{
    unsigned int attr_mask;    /* This field is set to one or more of the following
                                  symbols OR'd together to indicate which of the
                                  remaining fields of the structure are set.
                                      UF_LEGEND_WIDTH_ATTR
                                      UF_LEGEND_BORDER_ATTR
                                      UF_LEGEND_FONT_SIZE_ATTR
                                      UF_LEGEND_HEADER_ATTR
                                      UF_LEGEND_INDEX_ATTR
                                      UF_LEGEND_FOOTER_ATTR      */
    int        width_percent;  /* The percentage of the display which the
                                  legend occupies. The legend takes up the full
                                  height of the display. default: 20% */
    logical    border_sw;      /* Switch indicating whether or not the border
                                  of the legend gets displayed.
                                  = TRUE  -> display border
                                  = FALSE -> do not display border. (default) */
    double     font_size;      /* The size in inches of an individual character.
                                  If not specified, the font is automatically
                                  calculated so that 15 characters can be
                                  displayed in the full width of the legend.
                                  The auto size also is constrained by a maximum
                                  size of .12"  and a minimum size of .04".
                                  default: automatic */
    UF_SF_LEGEND_title_t      header;
                               /* The header text of the legend area
                                  default: none defined. */
    UF_SF_LEGEND_index_attr_t index_attr;
                               /* The index area's attributes if defined.
                                  default: none defined. */
    UF_SF_LEGEND_title_t      footer;
                               /* The footer text of the legend area
                                  default: none defined. */
};
typedef struct UF_SF_LEGEND_attr_s UF_SF_LEGEND_attr_t, *UF_SF_LEGEND_attr_p_t;



#ifdef __cplusplus
}
#endif

#endif  /* UF_SF_LEGEND_H_INCLUDED  */
