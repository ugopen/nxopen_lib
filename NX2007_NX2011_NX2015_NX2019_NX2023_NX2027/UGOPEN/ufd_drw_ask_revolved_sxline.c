/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_revolved_sxline.  It is placed
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
#include <uf_drf_types.h>
#include <uf_obj.h>

void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    int                         numchrs;
    int                         num_sxviews;
    int                         num_sxsegs;
    int                         num_leg1_sxsegs;
    tag_t                       sxline1_tag;
    tag_t                       pview_tag;
    tag_t *                     sxview_tags = NULL;
    tag_t *                     sxseg_tags = NULL;
    double                      step_dir[3];
    double                      arrow_dir[3];
    char                        error_message[133];
    char *                      sxline1 = "rev_sxline1";
    UF_DRAW_sxline_status_t     sxline_status;
    UF_DRAW_sxline_leg_t        cut_plane_leg;
    UF_DRF_object_t             rotpt_object;


    ifail = UF_initialize();

    if( !ifail )
    {
        /* Find the tag of the section line from its name. */
        numchrs = strlen( sxline1 );
        ifail = uc5028( sxline1, numchrs, &sxline1_tag );
    }

    if( !ifail )
    {
        /* Retrieve revolved section line information. */
        ifail = UF_DRAW_ask_revolved_sxline( sxline1_tag,
            step_dir, arrow_dir, &pview_tag,
            &rotpt_object, &num_sxviews, &sxview_tags,
            &num_sxsegs, &num_leg1_sxsegs, &cut_plane_leg,
            &sxseg_tags, &sxline_status );

        UF_free( sxview_tags );
        UF_free( sxseg_tags );

    }

    printf( "UF_DRAW_ask_revolved_sxline sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();

}
