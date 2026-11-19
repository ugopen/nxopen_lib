/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_sxsolids_of_sxview,
 *    UF_DRAW_ask_sxedges_of_sxsolid, UF_DRAW_ask_xhatch_of_sxsolid,
 *    and UF_DRAW_ask_curve_of_sxedge.  
 *    It is placed directly in our UFUN documentation starting with
 *    the include statements.
 *
 
 *
 ****************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_drf_types.h>
#include <uf_view.h>

void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    int                         num_sxedges;
    int                         num_sxsolids;
    tag_t                       curve_tag;
    tag_t                       sxview_tag;
    tag_t                       xhatch_tag;
    tag_t *                     sxsolid_tags = NULL;
    tag_t *                     sxedge_tags = NULL;
    char                        error_message[133];
    char *                      sxview1 = "SX@2";


    ifail = UF_initialize();
    if( !ifail )
    {
        /* Find the tag of the section view from its name. */
        ifail = UF_VIEW_ask_tag_of_view_name( sxview1, 
                                              &sxview_tag );
    }

    if( !ifail )
    {
        /* Retrieve the section solids associated to the first 
           leg of the section view. */
        ifail = UF_DRAW_ask_sxsolids_of_sxview( 
                    sxview_tag, 
                    UF_DRAW_sxline_leg1, 
                    &num_sxsolids, 
                    &sxsolid_tags );
    }

    if( !ifail )
    {
        /* Retrieve the crosshatch associated to the 
           first section solid. */
        ifail = UF_DRAW_ask_xhatch_of_sxsolid( sxsolid_tags[0],
                                               &xhatch_tag );
    }

    if( !ifail )
    {
        /* Retrieve the section edges of the first section 
           solid. */
        ifail = UF_DRAW_ask_sxedges_of_sxsolid( sxsolid_tags[0],
                                                &num_sxedges, 
                                                &sxedge_tags );
    }

    if( !ifail )
    {
        /* Retrieve the curve of the first section edge in the 
           array. */
        ifail = UF_DRAW_ask_curve_of_sxedge( sxedge_tags[0], 
                                             &curve_tag );
    }

    UF_free( sxedge_tags );
    UF_free( sxsolid_tags );

    printf( "UF_DRAW_ask_sxsolids_of_sxview sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    ifail = UF_terminate();

}

