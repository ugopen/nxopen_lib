/*===========================================================================

        Copyright (c) 1998,1999  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_create_stepped_sxview.  It is placed
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
    int                         num_sxviews;
    int                         num_sxsegs = 0;
    int                         num_user_defined_sxsegs = 0;
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
    char *                      sxline1 = "step_sxline1";
    UF_DRAW_sxline_status_t     sxline_status;
    UF_DRAW_sxseg_info_t        sxseg_info;
    UF_DRF_object_p_t           object;
    UF_DRAW_sxline_sxsegs_t     stepped_sxsegs[99] = {UF_DRAW_sxseg_arrow, 0, 0};


    ifail = UF_initialize();

    if( !ifail )
    {
        /* Find the tag of the section line from its name. */
        ifail = UF_OBJ_cycle_by_name(sxline1, &sxline1_tag );
    }

    if( !ifail )
    {
        /* Retrieve information about a stepped section line. */
        ifail = UF_DRAW_ask_stepped_sxline( sxline1_tag, step_dir,
                                            arrow_dir, &pview_tag, 
                                            &num_sxviews, &sxview_tags,
                                            &num_sxsegs, &sxseg_tags, 
                                            &sxline_status );
    }

    if (!ifail)
    {
        /* Get the tag of drawing. */
    ifail = UF_DRAW_ask_current_drawing(&dwg_tag);
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
       
            /* Save only user defined sxsegs. */
            if( sxseg_info.sxseg_mode == UF_DRAW_user_defined_sxseg )
            {
                stepped_sxsegs[num_user_defined_sxsegs].sxseg_type =
                    sxseg_info.sxseg_type;
                stepped_sxsegs[num_user_defined_sxsegs].sxseg_object =
                    object;
                num_user_defined_sxsegs++;
            }
            else
                UF_free( object );
        }
    }

    /* Create a similar stepped section line. */
    if( !ifail )
    {
        ifail = UF_DRAW_create_stepped_sxview( dwg_tag, sxview_scale, 
                                               step_dir, arrow_dir, 
                                               pview_tag,
                                               num_user_defined_sxsegs, 
                                               stepped_sxsegs,
                                               view_placement_pt, 
                                               &new_sxview_tag );
    }

    if( num_user_defined_sxsegs > 0 )
    {
        for( seg_ndx = 0; seg_ndx<num_user_defined_sxsegs; 
            seg_ndx++ )
        {
            /* Free each of the object structures. */
            UF_free( (stepped_sxsegs[seg_ndx].sxseg_object) );
        }
    }

    UF_free( sxview_tags );
    UF_free( sxseg_tags );

    printf( "UF_DRAW_create_stepped_sxview sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

