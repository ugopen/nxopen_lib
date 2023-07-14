/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_delete_sxline_sxseg.  It is placed  
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
    tag_t                       sxline1_tag;
    tag_t                       pview_tag;
    tag_t *                     sxview_tags = NULL;
    tag_t *                     sxseg_tags = NULL;
    double                      step_dir[3];
    double                      arrow_dir[3];
    char                        error_message[133];
    char *                      sxline1 = "step_sxline1";
    UF_DRAW_sxline_status_t     sxline_status;


    ifail = UF_initialize();
    if( !ifail )
    {
        /* Find the tag of the section line from its name. */
        numchrs = strlen( sxline1 );
        ifail = uc5028( sxline1, numchrs, &sxline1_tag );
    }

    if( !ifail )
    {
        /* Retrieve information about a stepped section line. */
        ifail = UF_DRAW_ask_stepped_sxline( sxline1_tag, 
            step_dir, arrow_dir, &pview_tag, &num_sxviews,
            &sxview_tags, &num_sxsegs, &sxseg_tags, 
            &sxline_status );
    }

    if( !ifail )
    {

        /* Delete a cut segment of the stepped section line. */
        ifail = UF_DRAW_delete_sxline_sxseg( sxseg_tags[1] );
    }

    UF_free( sxview_tags );
    UF_free( sxseg_tags );

    printf( "UF_DRAW_delete_sxline_sxseg sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();

}
