/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_sxline_of_sxview.  It is placed
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

void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    tag_t                       sxview_tag = NULL_TAG;
    tag_t                       sxline_tag;
    char                        error_message[133];
    char *                      sxview = "sx@2";
    logical                     is_sxview;

    ifail = UF_initialize();

    if( ifail == 0 )
        /* Find the tag of the section line from its name. */
        ifail = UF_OBJ_cycle_by_name( sxview, &sxview_tag );

    if( ifail == 0 )
    {
        /* Verify that the view is a section view. */
        ifail = UF_DRAW_is_sxview( sxview_tag, &is_sxview );
    }

    if( ifail == 0 && is_sxview )
    {
        /* Get the sxline from the sxview tag. */
        ifail = UF_DRAW_ask_sxline_of_sxview( sxview_tag,
            &sxline_tag );
    }
    else if( !is_sxview )
        printf( "Input view is not a section view.\n" );

    printf( "UF_DRAW_ask_sxline_of_sxview sample " );
    if( ifail != 0 )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    ifail = UF_terminate();

}
