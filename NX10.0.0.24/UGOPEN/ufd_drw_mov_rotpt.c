/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_move_sxline_rotpt.  It is placed  
 *    directly in our UFUN documentation starting with the 
 *    include statements.
 *
 
 *
 ****************************************************************************/


#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_drf.h>
#include <uf_drf_types.h>
#include <uf_obj.h>

void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    int                         numchrs;
    int                         num_sxviews;
    int                         num_sxsegs;
    int                         num_leg1_sxsegs;
    tag_p_t                     sxview_tags = NULL;
    tag_p_t                     sxseg_tags = NULL;
    tag_t                       sxline_tag;
    tag_t                       pview_tag;
    char                        error_message[133];
    char *                      sxline = "rev_sxline1";
    double                      step_dir[3];
    double                      arrow_dir[3];
    UF_DRAW_sxline_leg_t        cut_plane_leg;
    UF_DRAW_sxline_status_t     sxline_status;
    UF_DRF_object_t             old_rotpt_object;
    UF_DRF_object_t             rotpt_object;


    ifail = UF_initialize();

    if( !ifail )
    {
        /* Get the tag of a section line named rev_sxline1. */
        numchrs = strlen( sxline );
        ifail = uc5028( sxline, numchrs, &sxline_tag );
    }

    if( !ifail )
    {
        ifail = UF_DRAW_ask_revolved_sxline( sxline_tag, 
            step_dir, arrow_dir, &pview_tag, &old_rotpt_object,
            &num_sxviews, &sxview_tags, &num_sxsegs, 
            &num_leg1_sxsegs, &cut_plane_leg, &sxseg_tags, 
            &sxline_status );
    }

    if( !ifail )
    {
        ifail = UF_DRF_init_object_structure( &rotpt_object );
    }

    if( !ifail )
    {
        /* Change the rotpt_object. */
        rotpt_object.object_assoc_type = UF_DRF_dwg_pos;
        rotpt_object.assoc_dwg_pos[0] = 
            old_rotpt_object.assoc_dwg_pos[0] + .05;
        rotpt_object.assoc_dwg_pos[1] = 
            old_rotpt_object.assoc_dwg_pos[1] + .05;
        ifail = UF_DRAW_move_sxline_rotpt( sxline_tag,
            &rotpt_object );
    }

    UF_free( sxview_tags );
    UF_free( sxseg_tags );

    printf( "UF_DRAW_move_sxline_rotpt sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}
