
/******************************************************************************
 *                                                                            *
 * FILE DESCRIPTION -                                                         *
 *   This program shows how to use the following User Function programs:      *
 *                                                                            *
 *                        UF_DRF_ask_sbf_file                                 *
 *                        UF_DRF_set_customer_sbf_file                        *
 *                        UF_DRF_create_symbol_font                           *
 *                        UF_DRF_place_symbol                                 *
 *                        UF_DRF_add_symbol_to_object                         *
 *                        UF_DRF_ask_symbol_data                              *
 *                        UF_DRF_ask_symbols_used                             *
 *                                                                            *
 
 ******************************************************************************/

#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_drf.h>
#include <uf_obj.h>
#include <uf_curve.h>
#include <uf_csys.h>

void ufusr (char *param, int *retcod, int param_len)
{
    int     status = 0;
    int     num_symbol_fonts = 2;
    logical is_inverted = TRUE;
    logical is_mirrored = TRUE;
    double  symbol_factor = 0.0;
    double  symbol_anchor[3] = {-1.5, 0.0, 0.0};
    double  symbol_orient[3] = { 1.5, 0.0, 0.0};
    double  symbol_angle  = 30.0;
    double  symbol_length = 2.0;
    double  symbol_height = 1.0;
    double  point1[3];
    tag_t   point1_tag, point2_tag, point3_tag;
    tag_t   line1_tag, line2_tag;
    tag_t   symbol_tag, symbol_font_tags[9];
    tag_t   dimension_tag;
    char    dimtxt[15 + 1] = "DIMENSION TEXT ";
    char    symbol_file_name[UF_CFI_MAX_FILE_NAME_BUFSIZE];
    char    symbol_name[UF_CFI_MAX_FILE_NAME_BUFSIZE] = "SYMBOLx ";

    UF_CURVE_line_t             line_coords;
    UF_DRF_symbol_create_data_t symbol_data;
    UF_DRF_symbol_data_t        symbol_info;
    UF_DRF_object_t             object1, object2;
    UF_DRF_text_t               drf_text;

    status = UF_initialize ();

    if (!status)
    {
        /* create some points and lines */
        point1[0] =  2.0;
        point1[1] = 11.0;
        point1[2] =  0.0;
        UF_CURVE_create_point (point1, &point1_tag);

        point1[0] = 3.0;
        point1[1] = 0.5;
        UF_CURVE_create_point (point1, &point2_tag);

        point1[0] = -0.7;
        point1[1] =  2.5;
        UF_CURVE_create_point (point1, &point3_tag);

        line_coords.start_point[0] = -1.0;
        line_coords.start_point[1] = -1.0;
        line_coords.start_point[2] =  0.0;
        line_coords.end_point[0]   =  1.0;
        line_coords.end_point[1]   =  1.0;
        line_coords.end_point[2]   =  0.0;
        UF_CURVE_create_line (&line_coords, &line1_tag);

        line_coords.start_point[0] =  1.0;
        line_coords.start_point[1] = -1.0;
        line_coords.start_point[2] =  0.0;
        line_coords.end_point[0]   = -1.0;
        line_coords.end_point[1]   =  1.0;
        line_coords.end_point[2]   =  0.0;
        UF_CURVE_create_line (&line_coords, &line2_tag);

        UF_DRF_init_symbol_create_data (&symbol_data);
        /* initialize the object structures */
        UF_DRF_init_object_structure (&object1);
        UF_DRF_init_object_structure (&object2);
        /* load drf_text specification */
        drf_text.user_dim_text  = dimtxt;
        drf_text.lines_app_text = 0;
        drf_text.appended_text  = NULL;

        /* create a parallel dimension */
        point1[0] = 5.0;
        point1[1] = 3.0;
        object1.object_tag = line1_tag;
        object1.object_view_tag = NULL_TAG;
        object1.object_assoc_type = UF_DRF_end_point;
        object1.object_assoc_modifier = UF_DRF_last_end_point;
        object2.object_tag = point1_tag;
        object2.object_view_tag = NULL_TAG;
        object2.object_assoc_type = UF_DRF_end_point;
        object2.object_assoc_modifier = UF_DRF_first_end_point;
        UF_DRF_create_parallel_dim
            (&object1, &object2, &drf_text, point1, &dimension_tag);

        UF_DRF_set_customer_sbf_file ();

        UF_DRF_ask_sbf_file (symbol_file_name);

        /* create symbol font entity */
        symbol_font_tags[0] = line1_tag;
        symbol_font_tags[1] = line2_tag;
        UF_DRF_create_symbol_font
            (symbol_name, symbol_factor, symbol_anchor, symbol_orient,
             num_symbol_fonts, symbol_font_tags);

        /* create standalone symbol */
        strcpy (symbol_data.symbol_name, symbol_name);
        symbol_data.angle      = symbol_angle;
        symbol_data.length     = symbol_length;
        symbol_data.height     = symbol_height;
        symbol_data.anchor_tag = point1_tag;
        UF_DRF_place_symbol
            (&symbol_data, is_inverted, is_mirrored, &symbol_tag);

        symbol_data.length     *= 0.15;
        symbol_data.height     *= 0.15;
        symbol_data.anchor_tag  = point2_tag;
        UF_DRF_add_symbol_to_object
            (&symbol_data, dimension_tag);

        symbol_data.anchor_tag = point3_tag;
        UF_DRF_add_symbol_to_object
            (&symbol_data, dimension_tag);

        UF_DRF_ask_symbols_used
            (dimension_tag, &num_symbol_fonts, symbol_font_tags);

        status = UF_DRF_ask_symbol_data (symbol_tag, &symbol_info);
        if (status == UF_DRF_NO_ERRORS)
        {
            symbol_font_tags[0] = symbol_info.symbol_font_tag;
            /* absolute anchor point coordinates */
            symbol_anchor[0] = symbol_info.anchor_point[0];
            symbol_anchor[1] = symbol_info.anchor_point[1];
            symbol_anchor[2] = symbol_info.anchor_point[2];
            /* absolute orientation point coordinates */
            symbol_orient[0] = symbol_info.orient_point[0];
            symbol_orient[1] = symbol_info.orient_point[1];
            symbol_orient[2] = symbol_info.orient_point[2];
            /* angle, length, height */
            symbol_angle  = symbol_info.angle;
            symbol_length = symbol_info.length;
            symbol_height = symbol_info.height;
        }
    }

    UF_terminate ();
}
