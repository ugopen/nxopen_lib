/*==============================================================================

             Copyright (c) 1998,1999 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================
File description:

    This function is a small sample program that demonstrates the 
    invocation of UF_DRAW_set_drawing_ref_pt.  It is placed directly
    in our UFUN documentation starting with the include statements.

 
==============================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_draw.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int        ifail = 0;
    int        num_views = 0;
    tag_t      drawing_tag = NULL_TAG;
    tag_p_t    view_list = NULL;
    double     reference_pt[2] = {15.0, 18.0};
    char       error_message[ MAX_LINE_BUFSIZE ] = "";

    ifail = UF_initialize();

    if ( !ifail )
        ifail = UF_DRAW_ask_current_drawing( &drawing_tag );

    /* Get the list of view tags for the current drawing. */
    if ( !ifail )
        ifail = UF_DRAW_ask_views( drawing_tag, &num_views, &view_list );

    if ( !ifail )
    {
        if ( num_views > 0 )
        {
            /* Set the drawing reference point on the first view. */
            ifail = UF_DRAW_set_drawing_ref_pt( drawing_tag, view_list[0],
                                                reference_pt );

            /* Check if the drawing reference point is properly set. */
            if ( !ifail )
                ifail = UF_DRAW_ask_drawing_ref_pt( view_list[0],
                                                    reference_pt );
        }
    }

    UF_free( view_list );

    printf ("UF_DRAW_set_drawing_reference_pt sample ");

    if ( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
    {
        if ( num_views > 0 )
        {
            printf( "is successful.\n" );
            printf( "The drawing reference point of the view is (%f, %f)\n", 
                    reference_pt[0], reference_pt[1] );
        }
        else
            printf( "did not find views in the drawing \n" );
    }

    UF_terminate();
}
