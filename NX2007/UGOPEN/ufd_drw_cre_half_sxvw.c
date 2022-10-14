/*===========================================================================

        Copyright (c) 1998,1999  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_create_half_sxview.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_drf_types.h>
#include <uf_obj.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    int                         num_sxviews = 0;
    int                         num_sxsegs = 0;
    int                         seg_ndx;
    tag_t                       sxline1_tag = NULL_TAG;
    tag_t                       pview_tag = NULL_TAG;
    tag_t                       dwg_tag = NULL_TAG;
    tag_t                       curve_tag;
    tag_t                       new_sxview_tag;
    tag_t *                     sxview_tags = NULL;
    tag_t *                     sxseg_tags = NULL;
    double                      step_dir[3];
    double                      arrow_dir[3];
    double                      view_placement_pt[2];
    double                      sxview_scale = 1.0;
    char                        error_message[MAX_LINE_BUFSIZE];
    char *                      sxline1 = "half_sxline1";
    UF_DRAW_sxline_status_t     sxline_status;
    UF_DRAW_sxseg_info_t        sxseg_info;
    UF_DRF_object_p_t           object = NULL;
    UF_DRAW_half_sxsegs_t       half_sxseg_objects;

    half_sxseg_objects.bend_object = NULL;
    half_sxseg_objects.cut_object = NULL;

    ifail = UF_initialize();

    if( !ifail )
    {
        /* Find the tag of the section line from its name. */
        ifail = UF_OBJ_cycle_by_name(sxline1, &sxline1_tag );
    }

    if( !ifail )
    {
        /* Retrieve information about a half section line. */
        ifail = UF_DRAW_ask_half_sxline( sxline1_tag, step_dir, arrow_dir, 
                                         &pview_tag, &num_sxviews, 
                                         &sxview_tags, &num_sxsegs, 
                                         &sxseg_tags, &sxline_status );
    }

    if (!ifail)
    {
        /* Get the tag of the current drawing. */
    ifail = UF_DRAW_ask_current_drawing( &dwg_tag );
    }

   
    if ( !ifail )
    {
         /* find the drawing reference point */
        ifail = UF_DRAW_ask_drawing_ref_pt( sxview_tags[0], 
                                            view_placement_pt );
    }

    if( !ifail )
    {

        /* Get the section line segment information. */
        for( seg_ndx = 0; seg_ndx < num_sxsegs; seg_ndx++ )
        {
            ifail = UF_DRAW_ask_sxline_sxseg( sxseg_tags[seg_ndx],
                &sxseg_info, &curve_tag, &object );
            if( ifail ) break;
       
            if( sxseg_info.sxseg_type == UF_DRAW_sxseg_bend )
                half_sxseg_objects.bend_object = object;
            else if( sxseg_info.sxseg_type == UF_DRAW_sxseg_cut )
                half_sxseg_objects.cut_object = object;
            else
                UF_free( object );
        }
    }

    if( !ifail )
    {
        /* The system will generate the arrow. */
        half_sxseg_objects.arrow_object = NULL;
        num_sxsegs = 2;
    }

    /* Create a similar half section line. */
    if( !ifail )
    {
        ifail = UF_DRAW_create_half_sxview( dwg_tag, 
            sxview_scale,step_dir, arrow_dir, pview_tag,
            num_sxsegs, &half_sxseg_objects,
            view_placement_pt, &new_sxview_tag );
    }

    /* Free the object structures and arrays. */
    UF_free( half_sxseg_objects.bend_object ); 
    UF_free( half_sxseg_objects.cut_object ); 
    UF_free( sxview_tags );
    UF_free( sxseg_tags );

    printf( "UF_DRAW_create_half_sxview sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();

}
