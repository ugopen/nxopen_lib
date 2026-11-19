/*===========================================================================

        Copyright (c) 1998-2000,2004  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_set_view_display.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
  
 *
 ****************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_disp.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_obj.h>
#include <uf_view.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    char                error_message[ MAX_LINE_BUFSIZE ] = "";
    tag_p_t             view_list = NULL;
    tag_t               drawing_tag = NULL_TAG;
    int                 ifail = 0;
    int                 num_views = 0;
    int                 color_blue = 0;
    int                 color_cyan = 0;
    UF_DRAW_view_prfs_t view_display_parms;

    ifail = UF_initialize();

    if (!ifail)
    {
        /* Get the tag of drawing. */
        ifail = UF_DRAW_ask_current_drawing (&drawing_tag);
    }

    /* Obtain the list of view tags for the drawing */
    if (!ifail)
    {
        ifail = UF_DRAW_ask_views( drawing_tag, &num_views, &view_list );
    }

    if (ifail == 0)
    {
        /* ALWAYS retrieve the view's current display parameter
           settings before changing them
        */
        ifail = UF_DRAW_ask_view_display (view_list[0], &view_display_parms);
    }

    /* 1-22-04 Jason Bell NX3210 : map hardcoded colors to new color wheel */
    if (ifail == 0)
        ifail = UF_DISP_ask_closest_color_in_displayed_part(UF_DISP_MEDIUM_AZURE_BLUE_NAME,
                                                            &color_blue); /* blue */
    if (ifail == 0)
        ifail = UF_DISP_ask_closest_color_in_displayed_part(UF_DISP_MEDIUM_AZURE_CYAN_NAME,
                                                            &color_cyan); /* cyan */


    if (ifail == 0)
    {
        /* Change the view's display parameters. */
        view_display_parms.hidden_line = UF_DRAW_hidden_line_removal_on;
        view_display_parms.hidden_line_color = color_blue;
        view_display_parms.hidden_line_font = UF_OBJ_FONT_DOTTED;
        view_display_parms.hidden_line_width = UF_OBJ_WIDTH_NORMAL;
        view_display_parms.edge_hiding_edge = UF_DRAW_edge_hiding_edge_off;
        view_display_parms.silhouettes = UF_DRAW_silhouettes_off;
        view_display_parms.uvhatch = UF_DRAW_uvhatch_on;
        view_display_parms.smooth = UF_DRAW_smooth_on;
        view_display_parms.smooth_edge_color = color_blue;
        view_display_parms.smooth_edge_font = UF_OBJ_FONT_DASHED;
        view_display_parms.smooth_edge_width = UF_OBJ_WIDTH_NORMAL;
        view_display_parms.smooth_edge_gap = UF_DRAW_gap_on;
        /* For simplicity, we assume the drawing units are English */
        view_display_parms.smooth_edge_gap_size = 0.1;
        view_display_parms.virtual_intersect = UF_DRAW_virtual_intersect_on;
        view_display_parms.virtual_intersect_color = color_cyan;
        view_display_parms.virtual_intersect_font = UF_OBJ_FONT_DASHED;
        view_display_parms.virtual_intersect_width = UF_OBJ_WIDTH_NORMAL;
        view_display_parms.virtual_intersect_gap = UF_DRAW_gap_on;
        view_display_parms.virtual_intersect_gap_size = 0.15;
        view_display_parms.tolerance = 0.0001;

        /* Only render the hidden lines referenced by annotation. */ 
        view_display_parms.referenced_edges_only = TRUE; 

        /* Render the hidden lines correctly for an interfering solid condition. */ 
        view_display_parms.interfering_solids = TRUE; 

        /* Don't render self-hidden edges. */ 
        view_display_parms.edges_hidden_by_own_solid = FALSE; 

        /* Don't render small feature hidden lines in features 
           smaller than 3% of model box size. 
        */ 
        view_display_parms.simplify_small_features = 1; 
        view_display_parms.small_feature_tolerance = 3.0; 
         
        ifail = UF_DRAW_set_view_display (view_list[0], &view_display_parms);
    }

    UF_free( view_list );

    printf ("UF_DRAW_set_view_display sample ");

    if (ifail != 0)
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
    {
        if ( num_views > 0 )
            printf( "is successful.\n" );
        else
            printf( "did not find views in the drawing \n" );
    }

    UF_terminate();
}
