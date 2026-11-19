/*==============================================================================

             Copyright (c) 1998-2001 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================
File description:

    This function is a small sample program that demonstrates the
    invocation of UF_DRAW_ask_num_views.  It is placed directly in
    our UFUN documentation starting with the include statements.

 
==============================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_draw.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int ifail = 0;
    int num_views1 = 0, num_views2 = 0;
    tag_t drawing_tag = NULL_TAG, drawing_view = NULL_TAG;
    char error_message[MAX_LINE_BUFSIZE];

    ifail = UF_initialize();

    if( !ifail )
        ifail = UF_DRAW_ask_current_drawing( &drawing_tag );

    /* Get the number of views in the current drawing. */
    if( !ifail )
        ifail = UF_DRAW_ask_num_views( drawing_tag, &num_views1 );

    /* Check to see if the number of views is valid. */
    if( !ifail )
        ifail = UF_DRAW_ask_views( drawing_tag, &num_views2, NULL );
        
    /* Retrieve the view of the drawing */
    if ( !ifail )
        ifail = UF_DRAW_ask_view_of_drawing(drawing_tag, &drawing_view);

    printf( "UF_DRAW_ask_num_views sample ");

    if ( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }

    /* Test fails.  Two different values for the number of views. */
    else if ( num_views1 != num_views2 )
        printf( "fails.\nInconsistent number of views in the part.\n" );

    else
    {
        printf( "is successful.\n" );
        printf( "The number of views in the drawing is %i.\n", num_views1 );
        printf( "The tag of the drawing view is %d.\n", drawing_view );
    }

    ifail = UF_terminate();
}
