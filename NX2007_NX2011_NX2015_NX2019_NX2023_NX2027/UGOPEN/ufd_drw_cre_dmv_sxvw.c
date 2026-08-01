/*==============================================================================

             Copyright (c) 1999 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================
File description:

    This is a small sample program that demonstrates the invocation
    of UF_DRAW_create_sxview_from_dmv.  It is placed directly in our
    UFUN documentation starting with the include statements.

 
==============================================================================*/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_drf_types.h>
#include <uf_obj.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int       ifail = 0;
    int       num_user_def_sxsegs = 1;
    int       num_sxviews = 0;
    int       num_sxsegs = 0;
    int       seg_ndx = 0;
    tag_t     sxline_tag = NULL_TAG;
    tag_t     sxview_tag = NULL_TAG;
    tag_t     pview_tag = NULL_TAG;
    tag_t     drawing_tag = NULL_TAG;
    tag_t     curve_tag = NULL_TAG;
    tag_p_t   sxview_tags = NULL;
    tag_p_t   sxseg_tags = NULL;
    logical   pict_sxview = false;
    double    cut_dir[3] = {0.0, 0.0, 0.0};
    double    arrow_dir[3] = {0.0, 0.0, 0.0};
    double    view_placement_pt[2] = {0.0, 0.0};
    double    sxview_scale = 1.0;
    char      error_message[ MAX_LINE_BUFSIZE ];
    char *    sxline = "pict_simple_sxline";

    UF_DRF_object_p_t        object;
    UF_DRAW_sxseg_info_t     sxseg_info;
    UF_DRAW_sxline_type_t    sxline_type = UF_DRAW_simple_sxline;
    UF_DRAW_sxline_status_t  sxline_status;
    UF_DRAW_sxline_sxsegs_t  sxseg_data;

    memset( &sxseg_data, 0, sizeof(UF_DRAW_sxline_sxsegs_t) );

    ifail = UF_initialize();
    
    if ( !ifail )
        ifail = UF_DRAW_ask_current_drawing( &drawing_tag );

    /* Find the tag of the section line from its name.  In this sample test,
       it is named "pict_simple_sxline". */
    if ( !ifail )
        ifail = UF_OBJ_cycle_by_name( sxline, &sxline_tag );

    /* Get info from the pictorial simple section line. */
    if ( !ifail )
        ifail = UF_DRAW_ask_pictorial_sxline( sxline_tag, &sxline_type, 
                                              cut_dir, arrow_dir, &pview_tag,
                                              &num_sxviews, &sxview_tags, 
                                              &num_sxsegs, &sxseg_tags,
                                              &pict_sxview, &sxline_status );
        
    if ( !ifail )
        ifail = UF_DRAW_ask_drawing_ref_pt( sxview_tags[0],
                                            view_placement_pt );

    if ( !ifail )
    {
        /* Get the section line segment information. */
        for( seg_ndx = 0; seg_ndx < num_sxsegs; seg_ndx++ )
        {
            ifail = UF_DRAW_ask_sxline_sxseg( sxseg_tags[seg_ndx], &sxseg_info,
                                              &curve_tag, &object );

            if ( ifail ) break;
       
            /* Save only the cut segment of the pictorial simple 
               section line. */
            if( sxseg_info.sxseg_type == UF_DRAW_sxseg_cut )
            {
                sxseg_data.sxseg_type = sxseg_info.sxseg_type;
                sxseg_data.sxseg_object = object;
                break;
            }
            else
                UF_free( object );
        }
    }

    /* Create a pictorial section line and section view similar to the
       ones given in the drawing. */
    if ( !ifail )
        ifail = UF_DRAW_create_sxview_from_dmv( drawing_tag, pview_tag,
                                                sxline_type, sxview_scale,
                                                cut_dir, arrow_dir,
                                                num_user_def_sxsegs,
                                                &sxseg_data, view_placement_pt,
                                                pict_sxview, &sxview_tag );

    UF_free( sxview_tags );
    UF_free( sxseg_tags );

    if ( sxview_tag != NULL_TAG )
         UF_free( sxseg_data.sxseg_object );

    printf( "UF_DRAW_create_sxview_from_dmv sample " );

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    ifail = UF_terminate();
}
