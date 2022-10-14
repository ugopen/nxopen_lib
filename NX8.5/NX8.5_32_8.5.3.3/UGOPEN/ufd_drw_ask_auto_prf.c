/*===========================================================================

        Copyright (c) 1998,1999  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_auto_update.  It is placed
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
    char        error_message[MAX_LINE_SIZE + 1] = "";
    tag_t       drawing_tag = NULL_TAG;
    tag_p_t     view_list = NULL;
    int         ifail = 0;
    logical     auto_update;
    int         num_views = 0;

    ifail = UF_initialize();

    if (!ifail)
    {
        /* Get the tag of the current drawing. */
	ifail = UF_DRAW_ask_current_drawing( &drawing_tag );
    }

    /* Obtain the list of view tags for the drawing */
    if (!ifail)
    {
        ifail = UF_DRAW_ask_views( drawing_tag, &num_views, &view_list );
    }

    if (!ifail)
    {
        /* Query the auto update status of the first view in the drawing. */
        if ( num_views > 0 )
            ifail = UF_DRAW_ask_auto_update (view_list[0], &auto_update);
    }

    UF_free( view_list );

    printf ("UF_DRAW_ask_auto_update sample ");

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
