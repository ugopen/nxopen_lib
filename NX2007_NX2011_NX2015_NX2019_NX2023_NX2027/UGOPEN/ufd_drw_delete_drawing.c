/*==============================================================================

             Copyright (c) 1998,1999 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================
File description:

    This function is a small sample program that demonstrates the
    invocation of UF_DRAW_delete_drawing.  It is placed directly
    in our UFUN documentation starting with the include statements.

 
==============================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_draw.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int           ifail = 0;
    int           num_drawings = 0;
    tag_t         curr_dwg_tag = NULL_TAG;
    tag_p_t       drawing_list = NULL;
    char          error_message[ MAX_LINE_BUFSIZE ] = "";

    ifail = UF_initialize();

    if ( !ifail )
        ifail = UF_DRAW_ask_current_drawing( &curr_dwg_tag );

    /* Get the list of drawing tags in the part. */
    if ( !ifail )
        ifail = UF_DRAW_ask_drawings( &num_drawings, &drawing_list );

    if ( !ifail )
    {
        /* To do the test, we need at least 2 drawings in the part. */
        if ( num_drawings >= 2 )
        {
            /* If the first drawing is the current drawing, then open the
               next drawing. */
            if ( drawing_list[0] == curr_dwg_tag )
                ifail = UF_DRAW_open_drawing( drawing_list[1] );

            /* Delete the first drawing in the part. */
            if ( !ifail )
                ifail = UF_DRAW_delete_drawing( drawing_list[0] );
        }
    }

    UF_free( drawing_list );

    printf ("UF_DRAW_delete_drawing sample ");

    if ( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
    {
        if ( num_drawings >= 2 )
            printf( "is successful.\n" );
        else
            printf( "needs at least 2 drawings in the part \n" );
    }

    UF_terminate();
}
