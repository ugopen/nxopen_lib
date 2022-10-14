/*==============================================================================

             Copyright (c) 1998,1999 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================
File description:

    This function is a small sample program that demonstrates the
    invocation of UF_DRAW_ask_display_state.  It is placed directly
    in our UFUN documentation starting with the include statements.

 
==============================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_draw.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int ifail = 0;
    int view_type = 0;
    char error_message[MAX_LINE_BUFSIZE];

    ifail = UF_initialize();

    /* Get the current drawing display state. */
    if( !ifail )
        ifail = UF_DRAW_ask_display_state( &view_type );

    printf( "UF_DRAW_ask_display_state sample ");

    if ( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
    {
        printf( "is successful.\n" );

        if ( view_type == UF_DRAW_MODELING_VIEW )
            printf( "The display state is the modeling view.\n" );

        if ( view_type == UF_DRAW_DRAWING_VIEW )
            printf( "The display state is the drawing view.\n" );
    }

    ifail = UF_terminate();
}
