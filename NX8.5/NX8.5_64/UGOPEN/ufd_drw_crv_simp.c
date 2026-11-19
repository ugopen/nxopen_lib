/*===========================================================================

        Copyright (c) 1998 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_simplified_curve and
 *    UF_DRAW_create_simplified_curve.  It is placed
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
    int                         num_sxsolids = 0;
    int                         num_sxedges = 0;
    int                         num_segments = 0;
    logical                     flat_arc_to_line = TRUE;
    double                      tolerance;
    tag_t                       sxview_tag = NULL_TAG;
    tag_p_t                     sxsolid_tags = NULL;
    tag_p_t                     sxedge_tags = NULL;
    tag_p_t                     segments = NULL;
    char                        error_message[133];
    char *                      sxview = "sx@1";
    UF_DRAW_sxline_leg_t        sxline_leg = UF_DRAW_sxline_leg1;

    ifail = UF_initialize();

    if( ifail == 0 )
    {
        int numchrs = 0;            
        /* Find the tag of the section view from its name. */
        numchrs = strlen( sxview );
        ifail = uc5028( sxview, numchrs, &sxview_tag );
    }

    /* Find the section solids of the section view. */
    if( ifail == 0 )
        ifail = UF_DRAW_ask_sxsolids_of_sxview( sxview_tag, 
                                                sxline_leg,
                                                &num_sxsolids,
                                                &sxsolid_tags );

    /* Find the section edges of the first section 
       solid of the view. */
    if( ifail == 0 )
    {
        ifail = UF_DRAW_ask_sxedges_of_sxsolid( sxsolid_tags[0],
                                                &num_sxedges,
                                                &sxedge_tags );
        UF_free( sxsolid_tags );
    }

    /* Simplify the first section edge of that section solid. 
       Note that only section edges that are splines or conics
       will be simplified. */
    if( ifail == 0 )
    {
        ifail = UF_DRAW_create_simplified_curve( 
            sxedge_tags[0],
            sxview_tag,
            flat_arc_to_line,
            &num_segments,
            &segments );
        UF_free( segments );
        segments = NULL;
    }

    /* After a simplification has been created, it may be
       queried. */
    if( ifail == 0 && num_segments > 0 )
    {
        ifail = UF_DRAW_ask_simplified_curve( sxedge_tags[0],
                                              &sxview_tag,
                                              &flat_arc_to_line,
                                              &tolerance,
                                              &num_segments,
                                              &segments );
        UF_free( sxedge_tags );
    }

    /* To delete a simplification, delete just one of the simple
       curves. */
    if( ifail == 0 && num_segments > 0 )
    {
        ifail = UF_OBJ_delete_object( segments[0] ); 
        UF_free( segments );
    }

    printf( "UF_DRAW_crv_simp sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    ifail = UF_terminate();
}
