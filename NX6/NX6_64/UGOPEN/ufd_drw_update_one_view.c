/*===========================================================================

        Copyright (c) 1998,1999  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_update_one_view.  It is placed
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
    int           num_views = 0;
    char          error_message[MAX_LINE_SIZE + 1];
    tag_p_t       view_list = NULL;
    tag_t         drawing_tag = NULL_TAG;
    logical       out_of_date;

    ifail = UF_initialize();
    
    if (ifail == 0)
    {
        ifail = UF_DRAW_ask_current_drawing(&drawing_tag);
    }

    /* Obtain the list of view tags for the drawing */
    if (!ifail)
    {
        ifail = UF_DRAW_ask_views( drawing_tag, &num_views, &view_list );
    }

    if (ifail == 0)
    {
        /* Query the drawing's out of date status. */
        ifail = UF_DRAW_is_object_out_of_date(drawing_tag, &out_of_date);
    }

    if (ifail == 0 && out_of_date && num_views > 0 && view_list[0] != NULL_TAG)
    {
       /* Update the view. */
        ifail = UF_DRAW_update_one_view(drawing_tag, view_list[0]);
    }

    UF_free( view_list );

    printf ("UF_DRAW_update_one_view sample ");
  
    if (ifail != 0)
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}
