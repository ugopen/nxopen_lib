/*==============================================================================

             Copyright (c) 1998,1999 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================
File description:

    This function is a small sample program that demonstrates the
    invocation of UF_VIEW_delete.  It is placed directly in our UFUN
    documentation starting with the include statements.

 
==============================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_draw.h>
#include <uf_view.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int         ifail = 0;
    int         num_views = 0;
    tag_t       drawing_tag = NULL_TAG;
    tag_p_t     view_list = NULL;
    char        error_message[ MAX_LINE_BUFSIZE ];

    ifail = UF_initialize();

    if( !ifail )
        ifail = UF_DRAW_ask_current_drawing( &drawing_tag );

    /* Get the list of view tags in the current drawing. */
    if( !ifail )
        ifail = UF_DRAW_ask_views( drawing_tag, &num_views, &view_list );

    /* Remove the first view in the list from the drawing. */
    if( !ifail )
    {
        if ( num_views > 0 )
            UF_VIEW_delete( view_list[0], &ifail );
    }

    UF_free( view_list );

    printf( "UF_DRAW_remove_member_view sample ");

    if ( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
    {
        if ( num_views > 0 )
            printf( "is successful.\n" );
        else
            printf( "did not find views in the drawing.\n" );
    }

    ifail = UF_terminate();
}
