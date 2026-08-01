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

*******************************************************************************/


#ifndef UF_SF_LEGEND_H_INCLUDED
#define UF_SF_LEGEND_H_INCLUDED

#include <uf_defs.h>
#include <uf_sf_types.h>

#ifdef __cplusplus
extern "C" {
#endif




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
    int     font_color;        /* font color */
    UF_SF_LEGEND_title_t      header;
                               /* The header text of the legend area
                                  default: none defined. */
    UF_SF_LEGEND_index_attr_t index_attr;
                               /* The index area's attributes if defined.
                                  default: none defined. */
    UF_SF_LEGEND_title_t      footer;
                               /* The footer text of the legend area
                                  default: none defined. */
    int        layout_type;    /* IViewManager::LayoutType */
    int        view_port_id;   /* viewport */
};
typedef struct UF_SF_LEGEND_attr_s UF_SF_LEGEND_attr_t, *UF_SF_LEGEND_attr_p_t;



#ifdef __cplusplus
}
#endif

#endif  /* UF_SF_LEGEND_H_INCLUDED  */
