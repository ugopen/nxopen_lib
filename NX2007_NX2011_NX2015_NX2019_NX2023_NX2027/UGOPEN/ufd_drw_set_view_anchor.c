/*===========================================================================

        Copyright (c) 1998,1999 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_set_view_anchor().  It is placed
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
#include <uf_view.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
  int         ifail = 0;
  tag_t       point_tag = NULL_TAG;
  tag_t       curve_tag = NULL_TAG;
  tag_t       scalar_tag = NULL_TAG;
  tag_t       view_tag = NULL_TAG;
  tag_t       part_tag = NULL_TAG;
  char        *view_name = "TOP@1";
  char        *object_name = "CURVE";
  char        error_message[ MAX_LINE_BUFSIZE ];
  UF_SO_update_option_t update_option = UF_SO_update_within_modeling; 
  ifail = UF_initialize();
    
  if( !ifail )
      part_tag = UF_PART_ask_display_part();
      
  if( !ifail && part_tag != NULL_TAG )
      /* set drawing state to modeling view */
      ifail = UF_DRAW_set_display_state( UF_DRAW_MODELING_VIEW ); 
    
  if( !ifail && part_tag != NULL_TAG )
      ifail = UF_VIEW_ask_tag_of_view_name( view_name, 
                                           &view_tag );
    
  if( !ifail && part_tag != NULL_TAG && 
       view_tag != NULL_TAG )
        /* Retrieve tag of named object to define the */
        /* view anchor point.                         */
      ifail = UF_OBJ_cycle_by_name( object_name, 
                                   &curve_tag );
    
  if( !ifail && part_tag != NULL_TAG && 
      view_tag != NULL_TAG && 
      curve_tag != NULL_TAG)
        ifail = UF_SO_create_scalar_double( part_tag,
                                          update_option,
                                          0.0,
                                         &scalar_tag);
  
  if( !ifail && scalar_tag != NULL_TAG )                                    
      ifail = UF_SO_create_point_on_curve( part_tag,
                                           update_option,
                                           curve_tag,
                                           scalar_tag,
                                          &point_tag );
  if( !ifail && point_tag != NULL_TAG )
      /* set drawing state to drawing view */
      ifail = UF_DRAW_set_display_state( UF_DRAW_DRAWING_VIEW );
      
  if( !ifail && point_tag != NULL_TAG )
      ifail = UF_DRAW_set_view_anchor( view_tag, 
                                       point_tag );
  
  printf( "UF_DRAW_set_view_anchor " );
  if( ifail )
  {
      ifail = UF_get_fail_message( ifail, error_message );
      printf( "fails. \nError is:%s\n", error_message );
  }
  else if( part_tag == NULL_TAG )
      printf( "fails.\nError is: no active part.\n" );
  else if ( point_tag == NULL_TAG )
      printf( "fails.\nError is: no reference point.\n" );
  else if ( view_tag == NULL_TAG )
      printf( "fails.\nError is: view not found.\n" );
  else   
      printf( "is successful.\n" );
            
  ifail = UF_terminate();
}
