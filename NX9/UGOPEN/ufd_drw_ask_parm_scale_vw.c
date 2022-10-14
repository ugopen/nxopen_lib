/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_view_parm_scale.  It is placed
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


void ufusr(char *param, int *retcod, int param_len)
{
    char                drawing_name [ UF_OBJ_NAME_BUFSIZE ] = "";
    char                view_name [ UF_OBJ_NAME_BUFSIZE ] = "";
    char                error_message[MAX_LINE_BUFSIZE] = "";
    tag_t               view_tag = NULL_TAG;
    tag_t               drawing_tag = NULL_TAG;
    tag_t               exp_tag = NULL_TAG;
    double              scale = 0.0;
    int                 ifail = 0, len;

    ifail = UF_initialize();

    if (!ifail)
    {
        /* Get the tag of drawing. */
    ifail = UF_DRAW_ask_current_drawing(&drawing_tag);
    }

    if (!ifail)
    {
        /* Get the name of first drawing. */
        ifail = uc5027(drawing_tag, drawing_name, &len);
    }

    if (!ifail)
    {
        /* Get the name of the drawing's first view. */
        ifail = uc6499 (drawing_name, view_name);
    }

    if (!ifail)
    {
        /* Get the view's tag. */
        ifail = UF_VIEW_ask_tag_of_view_name (view_name, &view_tag);
    }

    if (!ifail)
    {
        /* Get the parametric view scale. */
        ifail = UF_DRAW_ask_view_parm_scale (view_tag, &exp_tag, &scale);
    }

    printf ("UF_DRAW_ask_view_parm_scale sample ");

    if (ifail)
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
    {
        printf( "is successful.\n" );
        printf( "The scale value is %g \n", scale );
    }

    UF_terminate();
}
