/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_set_suppress_view_updat.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_draw.h>
#include <uf_draw_types.h>


void ufusr(char *param, int *retcod, int param_len)
{
    int                 ifail = 0;
    char                error_message[133];

    ifail = UF_initialize();
    
    if (!ifail)
    {
        /* Set the suppress view update flag off. */
        ifail =  UF_DRAW_set_suppress_view_updat(false);
    }

    printf ("UF_DRAW_set_suppress_view_updat sample ");

    if (ifail)
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}
