/*===========================================================================

                             Copyright 1998 UGS Corp.
                               All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_add_detail_view().  It is placed
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
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>

void ufusr(char *param, int *retcod, int param_len)
{
    double      corner1[2] = {1.0, 1.0};
    double      corner2[2] = {4.0, 4.0};
    double      reference_point[2] = {10.0, 12.0};
    double      detail_view_scale = 2.5;
    int         ifail = 0;
    tag_t       drawing_tag = NULL_TAG;
    tag_t       part_tag = NULL_TAG;
    tag_t       parent_view_tag = NULL_TAG;
    tag_t       detail_view_tag = NULL_TAG;
    char        error_message[133];
    char        *view_name = "TOP@1";
    
    ifail = UF_initialize();
     
    if( !ifail )
        part_tag = UF_PART_ask_display_part();
            
    if( !ifail && part_tag != NULL_TAG )
        ifail = UF_DRAW_ask_current_drawing( &drawing_tag );
                                             
    if( !ifail && part_tag != NULL_TAG && drawing_tag != NULL_TAG )
    {        
        ifail = UF_OBJ_cycle_by_name_and_type(part_tag,
                                              view_name,
                                              UF_view_type,
                                              false,   /* skip occurrences */
                                              &parent_view_tag );
                                 
        if( !ifail && parent_view_tag != NULL_TAG )
        {
            ifail = UF_DRAW_add_detail_view( drawing_tag,
                                             parent_view_tag,
                                             corner1,
                                             corner2,
                                             detail_view_scale,
                                             reference_point,
                                            &detail_view_tag );
        }
    }
    printf( "UF_DRAW_add_detail_view " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails. \nError is:%s\n", error_message );
    }
    else if( part_tag == NULL_TAG )
        printf( "fails.\nError is: no active part.\n" );
    else if ( drawing_tag == NULL_TAG )
        printf( "fails.\nError is: no current drawing.\n" );
    else   
        printf( "is successful.\n" );
    
    ifail = UF_terminate();
}
