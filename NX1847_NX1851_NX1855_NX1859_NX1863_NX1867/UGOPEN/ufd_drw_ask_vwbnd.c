/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_boundary_curves.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <uf_part.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_drf_types.h>
#include <uf_view.h>

void ufusr(char *param, int *retcod, int param_len)
{
    double                      tolerance = 0.0;
    int                         ifail = 0;
    int                         num_objects = 0;
    tag_t                       view_tag = NULL_TAG;
    tag_t                       part_tag = NULL_TAG;
    char                        error_message[133];
    char *                      view_name= "TOP@1";
    UF_DRAW_view_boundary_t *   boundary_curves = NULL;

    ifail = UF_initialize();
    if( !ifail )
        part_tag = UF_PART_ask_display_part();
             
    if( !ifail && part_tag != NULL_TAG  )
    
        /* get view tag of TOP view */
        ifail = UF_VIEW_ask_tag_of_view_name( view_name, 
                                             &view_tag );
                                             
    if( !ifail && part_tag != NULL_TAG )
        ifail = UF_DRAW_ask_boundary_curves( view_tag,
                                            &tolerance,
                                            &num_objects,
                                            &boundary_curves );

    printf( "UF_DRAW_ask_boundary_curves " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else if ( part_tag == NULL_TAG )
        printf( "fails.\nError is: no active part.\n" );
    else    
        printf( "is successful, %d curves in boundary array\n", num_objects );

    UF_DRAW_free_boundary( num_objects, boundary_curves );
    
    ifail = UF_terminate();
}

