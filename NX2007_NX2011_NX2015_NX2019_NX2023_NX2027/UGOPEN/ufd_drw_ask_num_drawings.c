/*==============================================================================

             Copyright (c) 1998,1999 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================
File description:

    This function is a small sample program that demonstrates the
    invocation of UF_DRAW_ask_num_drawings.  It is placed directly 
    in our UFUN documentation starting with the include statements.

 
==============================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_draw.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int ifail = 0;
    int num_drawings1 = 0, num_drawings2 = 0;
    char error_message[MAX_LINE_BUFSIZE];

    ifail = UF_initialize();

    /* Get the number of drawings in the part. */
    if( !ifail )
        ifail = UF_DRAW_ask_num_drawings( &num_drawings1 );

    /* Check to see if the number of drawings is valid. */
    if( !ifail )
        ifail = UF_DRAW_ask_drawings( &num_drawings2, NULL );

    printf( "UF_DRAW_ask_num_drawings sample ");

    if ( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }

    /* Test fails.  Two different values for the number of drawings. */
    else if ( num_drawings1 != num_drawings2 )
        printf( "fails.\nInconsistent number of drawings in the part.\n" );

    else
    {
        printf( "is successful.\n" );
        printf( "The number of drawings in the part is %i.\n", num_drawings1 );
    }

    ifail = UF_terminate();
}
