/*===========================================================================

        Copyright (c) 1998,1999  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_set_view_angle.  It is placed
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
#include <uf_obj.h>
#include <uf_view.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    char                error_message[ MAX_LINE_BUFSIZE ] = "";
    tag_p_t             view_list = NULL;
    tag_t               drawing_tag = NULL_TAG;
    int                 ifail = 0;
    int                 num_views = 0;

    ifail = UF_initialize();

    if (!ifail)
    {
        /* Get the tag of drawing. */
        ifail = UF_DRAW_ask_current_drawing (&drawing_tag);
    }

    /* Obtain the list of view tags for the drawing */
    if (!ifail)
    {
        ifail = UF_DRAW_ask_views( drawing_tag, &num_views, &view_list );
    }

    if (!ifail)
    {
         /* Set the view angle. */
        if ( num_views > 0 )
            ifail = UF_DRAW_set_view_angle (view_list[0], 45.0);
    }

    UF_free( view_list );

    printf ("UF_DRAW_set_view_angle sample ");

    if (ifail)
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
    {
        if ( num_views > 0 )
            printf( "is successful.\n" );
        else
            printf( "did not find views in the drawing \n" );
    }

    UF_terminate();
}
