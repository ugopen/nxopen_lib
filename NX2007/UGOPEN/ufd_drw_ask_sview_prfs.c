
/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_sxview_display.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_obj.h>


void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    int                         numchrs;
    tag_t                       sxview_tag = NULL_TAG;
    char                        error_message[133];
    char *                      sxview_name = "sx@13";
    UF_DRAW_sxview_prfs_t       sxview_parms;

    ifail = UF_initialize();

    if (!ifail)
    {
        /* Get the tag of the section view. */
        numchrs = strlen (sxview_name);
        ifail = uc5028 (sxview_name, numchrs, &sxview_tag);
    }
    
    if (!ifail)
    {
        /* Query the section view background and crosshatch parameters */
        ifail = UF_DRAW_ask_sxview_display (sxview_tag,
                                            &sxview_parms);
    }

    printf ("UF_DRAW_ask_sxview_display sample ");

    if (ifail)
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();

}
