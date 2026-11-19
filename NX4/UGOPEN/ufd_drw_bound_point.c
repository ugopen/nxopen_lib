/*===========================================================================

        Copyright (c) 1998 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_set_boundary_assoc(), UF_DRAW_free_boundary(),
 *    and UF_DRAW_edit_boundary_point.  It is placed directly in our
 *    UFUN documentation starting with the include statements.
 *
 
 *
 ****************************************************************************/
 
#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_so.h>
#include <uf_view.h>

static void create_two_smart_points( tag_t part_tag, tag_t view_tag, tag_t point_tags[2] );

void ufusr(char *param, int *retcod, int param_len)
{
    int         ifail = 0;
    int         return_code = 0;
    int         curve_count = 0;
    tag_t       part_tag = NULL_TAG;
    tag_t       view_tag = NULL_TAG;
    tag_t       new_point_tags[2] = {NULL_TAG, NULL_TAG};
    tag_t       defining_point_tag = NULL_TAG;
    tag_t       drawing_tag = NULL_TAG;
    char        error_message[133];
    char *      view_name = "TOP@1";
    UF_DRAW_view_boundary_p_t    boundary_curves;     
    
    ifail = UF_initialize();
    
    if( ifail == 0 )
        part_tag = UF_PART_ask_display_part();
    
    if ( ifail == 0 && part_tag != NULL_TAG )
        ifail = UF_DRAW_ask_current_drawing( &drawing_tag );
            
    if( ifail == 0 && drawing_tag != NULL_TAG )
        ifail = UF_VIEW_ask_tag_of_view_name(view_name,
                                            &view_tag );
    
    if( ifail == 0 && view_tag != NULL_TAG )
        create_two_smart_points( part_tag, view_tag, new_point_tags );
                                                                
    if( ifail == 0 && new_point_tags[0] != NULL_TAG && 
        new_point_tags[1] != NULL_TAG)
    {       
        ifail = UF_DRAW_set_boundary_assoc( view_tag, 
                                           &curve_count,
                                           &boundary_curves ); 
        if( ifail == 0 &&  curve_count > 0 && boundary_curves[0].point_count > 0 )
        {
            /* The boundary point being edited is defined as the  
             * last defining point of the first boundary curve.     */                 
            defining_point_tag = boundary_curves[0].defining_points[boundary_curves[0].point_count-1];
            ifail = UF_DRAW_edit_boundary_point( defining_point_tag, 
                                                 new_point_tags[0],
                                                 view_tag );
            /* The boundary point being edited is defined as the  
             * first defining point of the first boundary curve.     */                 
            defining_point_tag = boundary_curves[0].defining_points[0];
            ifail = UF_DRAW_edit_boundary_point( defining_point_tag, 
                                                 new_point_tags[1],
                                                 view_tag );
            
            /* Update the view to correct the view boundary. */
            return_code = UF_DRAW_update_one_view( drawing_tag, view_tag );
        }
    }
                                                               
    printf("UF_DRAW_edit_boundary_point ");                        
    if( ifail != 0 )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else if ( part_tag == NULL_TAG )
        printf( "fails.\nError is: no active part.\n" );
    else if ( view_tag == NULL_TAG )
        printf( "fails.\nError is: no TOP@1 view.\n" );
    else if ( new_point_tags[0] == NULL_TAG || new_point_tags[1] == NULL_TAG )
        printf( "fails.\nA new point was not created.\n" );
    else if ( curve_count == 0 )
        printf( "fails.\nError is: no curves in boundary.\n" );
    else if ( boundary_curves[0].point_count <= 0 )
        printf( "fails.\nError is: no def. pts in 1st curve.\n"); 
    else							
        printf( "is successful.\n" );                                                                 
    
    UF_DRAW_free_boundary(curve_count, boundary_curves);          
    
    ifail = UF_terminate();
}

static void create_two_smart_points( tag_t part_tag, tag_t view_tag, tag_t point_tags[2])
{
    int   return_code = 0;
    tag_t line_tags[2]    = {NULL_TAG, NULL_TAG};
	tag_t scalar_tags[2]  = {NULL_TAG, NULL_TAG};
    char *line_name1   = "NAMEDLINE1";
    char *line_name2   = "NAMEDLINE2";
    
    return_code = UF_VIEW_expand_view( view_tag );

    if ( return_code == 0 )
        return_code = UF_OBJ_cycle_by_name( line_name1, &line_tags[0] );

    if ( return_code == 0 )
        return_code = UF_OBJ_cycle_by_name( line_name2, &line_tags[1] );
    
    if ( return_code == 0 && line_tags[0] != NULL_TAG && line_tags[1] != NULL_TAG )
    {
        /* Create two scalars. */
    	return_code = UF_SO_create_scalar_double( part_tag,
                                                  UF_SO_update_after_modeling,
                                                  .648,
                                                 &scalar_tags[0] );
                                                 
    	return_code = UF_SO_create_scalar_double( part_tag,
                                                  UF_SO_update_after_modeling,
                                                  .466,
                                                 &scalar_tags[1] );
    }
    if ( return_code == 0 && scalar_tags[0] != NULL_TAG && scalar_tags[1] != NULL_TAG )
    {
    	return_code = UF_SO_create_point_on_curve( part_tag, 
                                                   UF_SO_update_after_modeling,
                                                   line_tags[0],
                                                   scalar_tags[0],
                                                  &point_tags[0] );
                                                  
    	return_code = UF_SO_create_point_on_curve( part_tag, 
                                                   UF_SO_update_after_modeling,
                                                   line_tags[1],
                                                   scalar_tags[1],
                                                  &point_tags[1] );
    }
                                                  
    return_code = UF_VIEW_unexpand_work_view();
}

