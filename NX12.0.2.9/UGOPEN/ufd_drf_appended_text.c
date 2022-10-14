/*===================================================================

        Copyright (c) 2000 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the functions UF_DRF_ask_appended_text, UF_DRF_set_appended_text,
 *    and UF_DRF_free_appended_text.
 *    In this program UF_DRF_set_appended_text adds appended text 
 *    before and below a dimension.  
 *    It then uses UF_DRF_ask_append_appended_text and UF_DRF_set_appended_text
 *    to move the before appended text to after the dimension.
 *    
 *
 *  
 *
 ********************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_csys.h>
#include <uf_curve.h>
#include <uf_drf.h>
#include <uf_drf_types.h>

void ufusr(char *param, int *retcod, int param_len)
{
    int num_text, i, ifail = 0;
    double origin[3] = {2.0, 2.0, 0.0};
    tag_t wcs, arc_tag, dimension;
    UF_CURVE_arc_t  arc_coords;
    UF_DRF_object_t arc;
    UF_DRF_appended_text_t text[2];
    UF_DRF_appended_text_p_t appended_text;
    char *text1 = "text1";
    char *text2[3] =
    { 
      "text2 - line 1",
      "text2 - line 2",
      "text2 - line 3"
    };
    char error_message[133] = "";

    /* Initialize User Function. */
    ifail = UF_initialize();

    /* create an arc */
    UF_CSYS_ask_wcs(&wcs);
    UF_CSYS_ask_matrix_of_object(wcs, &arc_coords.matrix_tag);
    arc_coords.start_angle = 0.0;
    arc_coords.end_angle = TWOPI;
    arc_coords.arc_center[0] = 0.0;
    arc_coords.arc_center[1] = 0.0;
    arc_coords.arc_center[2] = 0.0;
    arc_coords.radius = 1.0;
    ifail = UF_CURVE_create_arc(&arc_coords, &arc_tag);

    /* create a radius dimension */
    if (!ifail)
    {
        UF_DRF_init_object_structure(&arc);
        arc.object_tag = arc_tag;
        arc.object_view_tag = NULL_TAG;
        arc.object_assoc_type = UF_DRF_arc_center;
        arc.object_assoc_modifier = 0;
        ifail = UF_DRF_create_radius_dim(&arc, NULL, origin, &dimension);
    }

    /* add appended text before and below the dimension */
    if (!ifail)
    {
        text[0].location = UF_DRF_APPENDED_TEXT_BEFORE;
        text[0].num_lines = 1;
        text[0].text = &text1;

        text[1].location = UF_DRF_APPENDED_TEXT_BELOW;
        text[1].num_lines = 3;
        text[1].text = text2;

        ifail = UF_DRF_set_appended_text(dimension, 2, text);
    }

    if (!ifail)
    {
        /* query the dimension's appended text */
        ifail = UF_DRF_ask_appended_text(dimension, &num_text, &appended_text);

        if (!ifail)
        {
            /* move text from before dimension to after dimension */

            /* find before text */
            for (i=0; i<num_text; i++)
            {
                if (appended_text[i].location == UF_DRF_APPENDED_TEXT_BEFORE)
                {
                    /* remove before text */
                    text[0].location = UF_DRF_APPENDED_TEXT_BEFORE;
                    text[0].num_lines = 0;
                    text[0].text = NULL;

                    /* set after text to before text */
                    text[1].location = UF_DRF_APPENDED_TEXT_AFTER;
                    text[1].num_lines = appended_text[i].num_lines;
                    text[1].text = appended_text[i].text;

                    ifail = UF_DRF_set_appended_text(dimension, 2, text);
                    break;
                 }
             }

             ifail = UF_DRF_free_appended_text(num_text, appended_text);
        }
    }

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

