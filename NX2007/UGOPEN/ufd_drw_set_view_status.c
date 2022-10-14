/*==============================================================================

             Copyright (c) 1998,1999 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================
File description:

    This function is a small sample program that demonstrates the
    invocation of UF_DRAW_set_view_status along with UF_DRAW_ask_view_status.
    It is placed directly in our UFUN documentation starting with the
    include statements.

 
==============================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_draw.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int                      ifail = 0;
    int                      num_views = 0;
    tag_t                    drawing_tag = NULL_TAG;
    tag_p_t                  view_list = NULL;
    char                     error_message[ MAX_LINE_BUFSIZE ] = "";
    UF_DRAW_view_status_t    view_status;

    ifail = UF_initialize();

    if ( !ifail )
        ifail = UF_DRAW_ask_current_drawing( &drawing_tag );

    /* Get the list of view tags in the drawing. */
    if ( !ifail )
        ifail = UF_DRAW_ask_views( drawing_tag, &num_views, &view_list );

    if ( !ifail )
    {
        /* To do the test, we need at least 2 views in the drawing. */
        if ( num_views >= 2 )
        {
            /* Get the view status of the first view in the drawing. */
            ifail = UF_DRAW_ask_view_status( view_list[0], &view_status );

            /* Set the view status of the next view in the drawing to the
               same view status as the first view. */
            if ( !ifail )
            {
                ifail = UF_DRAW_set_view_status( view_list[1], view_status );
            }
        }
    }

    UF_free( view_list );

    printf ("UF_DRAW_set_view_status sample ");

    if ( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
    {
        if ( num_views >= 2 )
            printf( "is successful.\n" );
        else
            printf( "needs at least 2 views in the drawing \n" );
    }

    UF_terminate();
}
