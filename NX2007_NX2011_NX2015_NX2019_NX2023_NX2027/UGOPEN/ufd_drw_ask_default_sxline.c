/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_sxline_default_prfs.  It is placed
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

void ufusr(char *param, int *retcod, int param_len)
{

    int                         ifail = 0;
    char                        error_message[133];
    UF_DRAW_arrow_parms_t       arrow_parms;
    UF_DRAW_sxline_display_t    sxline_display;


    ifail = UF_initialize();
    if( !ifail )
    {

        /* Retrieve the global section line preferences. */
        ifail = UF_DRAW_ask_sxline_default_prfs( &arrow_parms,
            &sxline_display );
    }

    printf( "UF_DRAW_ask_sxline_default_prfs sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();

}
