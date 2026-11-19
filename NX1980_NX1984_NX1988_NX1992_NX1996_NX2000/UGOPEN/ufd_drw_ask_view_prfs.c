/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_view_display.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_obj.h>
#include <uf_view.h>

void ufusr(char *param, int *retcod, int param_len)
{

    char                drawing_name [30] = "";
    char                view_name [30] = "";
    char                error_message[133] = "";
    tag_t               view_tag = NULL_TAG;
    tag_t               drawing_tag = NULL_TAG;
    int                 ifail = 0;
    UF_DRAW_view_prfs_t hidden_line_parms;

    ifail = UF_initialize();

    if (!ifail)
    {
        /* Get the first drawing's name.*/
        ifail = uc6492 (drawing_name);
    }

    if (!ifail)
    {
        /* Get the drawing's tag. */
        ifail = UF_OBJ_cycle_by_name (drawing_name, &drawing_tag);
    }

    if (!ifail)
    {
        /* Get the view name. */
        ifail = uc6499 (drawing_name, view_name);
    }

    if (!ifail)
    {
        /* Get the tag of view. */
        ifail = UF_VIEW_ask_tag_of_view_name (view_name, &view_tag);
    }

    if (!ifail)
    {
        /* Retrieve the view's display parameter settings. */
        ifail = UF_DRAW_ask_view_display (view_tag, &hidden_line_parms);
    }

    printf ("UF_DRAW_ask_view_display sample ");

    if (ifail)
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}
