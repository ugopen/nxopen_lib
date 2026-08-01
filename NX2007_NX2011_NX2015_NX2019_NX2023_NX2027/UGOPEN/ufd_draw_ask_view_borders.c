/*===========================================================================

        Copyright (c) 1998,1999 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_view_borders.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *  
 *
 ****************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_view.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int       ifail = 0;
    double    view_borders[4];
    char      error_message[ MAX_LINE_BUFSIZE ];
    char *    view_name = "TOP@1";
    tag_t     view_tag = NULL_TAG;

    ifail = UF_initialize();

    if( !ifail )
        ifail = UF_VIEW_ask_tag_of_view_name( view_name, &view_tag );

    if( !ifail )
    {
        /* Find the view bounds of a view named "TOP@1". */
        ifail = UF_DRAW_ask_view_borders( view_tag, view_borders );
    }

    printf( "UF_DRAW_ask_view_borders sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    ifail = UF_terminate();

}

