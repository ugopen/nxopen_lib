/*===========================================================================

        Copyright (c) 1998,1999 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_add_circ_detail_view().  It is placed
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
#include <uf_part.h>
#include <uf_so.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
  double      reference_point[2] = {10.0, 12.0};
  double      detail_view_scale = 2.5;
  int         ifail = 0;
  tag_t       drawing_tag = NULL_TAG;
  tag_t       part_tag = NULL_TAG;
  tag_t       parent_view_tag = NULL_TAG;
  tag_t       curve_tag = NULL_TAG;
  tag_t       circle_center_tag = NULL_TAG;
  tag_t       circle_point_tag = NULL_TAG;
  tag_t       scalar_tag = NULL_TAG;
  tag_t       detail_view_tag = NULL_TAG;
  char        error_message[MAX_LINE_SIZE + 1];
  char        *view_name = "TOP@1";
  char        *object_name = "CURVE";
  UF_SO_update_option_t update_option = UF_SO_update_within_modeling; 
    
  ifail = UF_initialize();
    
  if( !ifail )
      part_tag = UF_PART_ask_display_part();
            
  if( !ifail && part_tag != NULL_TAG )
      ifail = UF_DRAW_ask_current_drawing( &drawing_tag );
                                             
  if( !ifail && drawing_tag != NULL_TAG )
      ifail = UF_OBJ_cycle_by_name( view_name,
                                   &parent_view_tag );
                                 
  if( !ifail && parent_view_tag != NULL_TAG )
  	  /* Retrieve tag of named object to define the */
  	  /* circle points.                         */
      ifail = UF_OBJ_cycle_by_name( object_name, 
                                   &curve_tag );
    
  if( !ifail && curve_tag != NULL_TAG )
      /* set drawing state to modeling */
      ifail = UF_DRAW_set_display_state( UF_DRAW_MODELING_VIEW );
    
  if( !ifail && curve_tag != NULL_TAG)
      ifail = UF_SO_create_scalar_double( part_tag,
                                          update_option,
                                          0.0,
                                         &scalar_tag);
  
  if( !ifail && scalar_tag != NULL_TAG )                                    
      ifail = UF_SO_create_point_on_curve( part_tag,
                                           update_option,
                                           curve_tag,
                                           scalar_tag,
                                          &circle_center_tag );

  if( !ifail && circle_center_tag != NULL_TAG)
      ifail = UF_SO_create_scalar_double( part_tag,
                                          update_option,
                                          0.5,
                                         &scalar_tag);
  
  if( !ifail && scalar_tag != NULL_TAG )                                    
      ifail = UF_SO_create_point_on_curve( part_tag,
                                           update_option,
                                           curve_tag,
                                           scalar_tag,
                                          &circle_point_tag );

  if( !ifail && circle_point_tag != NULL_TAG )
      /* Set to drawing view */
      ifail = UF_DRAW_set_display_state( UF_DRAW_DRAWING_VIEW );
      
      
  if( !ifail && circle_point_tag != NULL_TAG )
        ifail = UF_DRAW_add_circ_detail_view( drawing_tag,
                                         parent_view_tag,
                                         circle_center_tag,
                                         circle_point_tag,
                                         detail_view_scale,
                                         reference_point,
                                        &detail_view_tag );

  printf( "UF_DRAW_add_circ_detail_view " );
  if( ifail )
  {
      ifail = UF_get_fail_message( ifail, error_message );
      printf( "fails. \nError is:%s\n", error_message );
  }
  else if( part_tag == NULL_TAG )
      printf( "fails.\nError is: no active part.\n" );
  else if ( drawing_tag == NULL_TAG )
      printf( "fails.\nError is: no current drawing.\n" );
  else if ( parent_view_tag == NULL_TAG )
      printf( "fails.\nError is: no parent view.\n" );
  else if ( curve_tag == NULL_TAG )
      printf( "fails.\nError is: no curve.\n" );
  else if ( scalar_tag == NULL_TAG )
      printf( "fails.\nError is: no scalar.\n" );
  else if ( circle_center_tag == NULL_TAG )
      printf( "fails.\nError is: no circle center.\n" );
  else if ( circle_point_tag == NULL_TAG )
      printf( "fails.\nError is: no circle point.\n" );
  else   
      printf( "is successful.\n" );
    
  ifail = UF_terminate();
}

