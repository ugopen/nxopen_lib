/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_define_view_boundary.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_drf_types.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_view.h>

void ufusr(char *param, int *retcod, int param_len)
{
    int         ifail = 0;
    const int   num_objects = 1;
    tag_t       object_tag = NULL_TAG;
    tag_t       view_tag = NULL_TAG;
    tag_t       part_tag = NULL_TAG;
    char        error_message[133];
    char *      view_name = "TOP@1";
    char *      object_name = "CIRCLE_BOUNDARY";
    UF_DRAW_define_boundary_t * boundary_curves = NULL;
    
    ifail = UF_initialize();
    
    if( !ifail )
        part_tag = UF_PART_ask_display_part();
            
    if( !ifail && part_tag != NULL_TAG )
        ifail = UF_VIEW_ask_tag_of_view_name( view_name, 
                                             &view_tag );
    
    if( !ifail && part_tag != NULL_TAG )
                                
        /* retrieve tag of circle to define view boundary */
        /* this example uses a part with a named object   */
        
        ifail = UF_OBJ_cycle_by_name( object_name, 
                                     &object_tag );
        
    if( !ifail && part_tag != NULL_TAG && object_tag )
    {   
        boundary_curves = (UF_DRAW_define_boundary_t *)malloc
              (num_objects * sizeof(UF_DRAW_define_boundary_t));
        boundary_curves[0].curve_tag = object_tag;
    
        
        ifail = UF_DRAW_define_view_boundary( view_tag,
                                              num_objects,
                                             &boundary_curves );
    }
    printf( "UF_DRAW_define_view_boundary " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else if ( part_tag == NULL_TAG )
        printf( "fails.\nError is: no active part.\n" );
    else    
        printf( "is successful.\n" );

    free( boundary_curves );
    ifail = UF_terminate();
}

