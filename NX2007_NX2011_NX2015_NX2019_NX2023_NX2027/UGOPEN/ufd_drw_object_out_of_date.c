/*===========================================================================

        Copyright (c) 1998,1999  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_is_object_out_of_date.  It is placed
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
    int           ifail = 0;
    int           num_drawings = 0;
    int           num_views = 0;
    char          error_message[MAX_LINE_BUFSIZE];
    tag_p_t       drawing_list = NULL;
    tag_p_t       view_list = NULL;
    logical       out_of_date = false;

    ifail = UF_initialize();

    if (!ifail)
    {
        /* Get the tag of the current drawing. */
    ifail = UF_DRAW_ask_drawings( &num_drawings, &drawing_list );
    }

    if (!ifail)
    {
        /* Query the drawing's out of date status. */
        ifail = UF_DRAW_is_object_out_of_date(drawing_list[0], &out_of_date);
    }

    if (!ifail && out_of_date)
    {
        /* Obtain the list of view tags for the first drawing */
        if (!ifail)
        {
            ifail = UF_DRAW_ask_views( drawing_list[0], &num_views, &view_list );
        }

        /* Update the first view. */
        ifail = UF_DRAW_update_one_view(drawing_list[0], view_list[0]);
    }

    UF_free( drawing_list );
    UF_free( view_list );

    printf ("UF_DRAW_is_object_out_of_date sample ");

    if (ifail)
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}
