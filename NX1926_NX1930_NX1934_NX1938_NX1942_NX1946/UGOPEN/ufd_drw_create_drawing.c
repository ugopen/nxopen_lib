/*==============================================================================

             Copyright (c) 1998,1999 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================
File description:

    This function is a small sample program that demonstrates the
    invocation of UF_DRAW_create_drawing along with UF_DRAW_open_drawing.
    It is placed directly in our UFUN documentation starting with
    the include statements.

 
==============================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_draw.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int ifail = 0;
    tag_t drawing_tag = NULL_TAG, new_drawing_tag = NULL_TAG;
    char error_message[MAX_LINE_BUFSIZE];
    char drawing_name[ UF_OBJ_NAME_BUFSIZE ] = "SUCCESS";
    UF_DRAW_info_t drawing_info;

    ifail = UF_initialize();

    if( !ifail )
        ifail = UF_DRAW_ask_current_drawing( &drawing_tag );

    /* Get the drawing information from the current drawing. */
    if( !ifail )
        ifail = UF_DRAW_ask_drawing_info( drawing_tag, &drawing_info );

    /* Create a new drawing named "SUCCESS" with the same setting as 
       the current drawing. */
    if( !ifail )
        ifail = UF_DRAW_create_drawing( drawing_name, &drawing_info,
                                        &new_drawing_tag);

    /* Open the new drawing. */
    if( !ifail )
        ifail = UF_DRAW_open_drawing( new_drawing_tag );

    printf( "UF_DRAW_create_drawing sample ");

    if ( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    ifail = UF_terminate();
}
