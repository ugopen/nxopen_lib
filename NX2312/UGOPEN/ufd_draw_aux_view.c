/*===========================================================================

                               Copyright 1998 UGS Corp.
                                 All rights reserved.

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_add_auxiliary_view().  It is placed
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
#include <uf_so.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
  double      reference_point[2] = {10.0, 12.0};
  int         ifail = 0;
  tag_t       drawing_tag = NULL_TAG;
  tag_t       part_tag = NULL_TAG;
  tag_t       parent_view_tag = NULL_TAG;
  tag_t       aux_view_tag = NULL_TAG;
  tag_t       hinge_line_tag = NULL_TAG;
  tag_t       curve_tag = NULL_TAG;
  char        error_message[ MAX_LINE_BUFSIZE ];
  char        *view_name = "TOP@1";
  char        *object_name = "CURVE";
  UF_SO_update_option_t update_option = UF_SO_update_within_modeling; 
  logical     reverse_option = FALSE;
  
  ifail = UF_initialize();
    
  if( !ifail )
      part_tag = UF_PART_ask_display_part();
            
  if( !ifail && part_tag != NULL_TAG )
      ifail = UF_DRAW_ask_current_drawing( &drawing_tag );
                                             
  if( !ifail && drawing_tag != NULL_TAG )
        /* Retrieve tag of named object to define the */
        /* view anchor point.                         */
      ifail = UF_OBJ_cycle_by_name( object_name, 
                                   &curve_tag );
    
  if( !ifail && part_tag != NULL_TAG && curve_tag != NULL_TAG)
  {
      ifail = UF_OBJ_cycle_by_name_and_type(part_tag,
                                            view_name,
                                            UF_view_type,
                                            false,   /* no occurrences */
                                            &parent_view_tag);
  }
                                 
  if( !ifail && parent_view_tag != NULL_TAG )
      /* set drawing state to modeling */
      ifail = UF_DRAW_set_display_state( UF_DRAW_MODELING_VIEW );   
    
  if( !ifail && parent_view_tag != NULL_TAG )                                    
      ifail = UF_SO_create_dirr_line( part_tag,
                                      update_option,
                                      curve_tag,
                                      reverse_option,
                                     &hinge_line_tag );

  if( !ifail && hinge_line_tag != NULL_TAG )
      /* Set to drawing view */
      ifail = UF_DRAW_set_display_state( UF_DRAW_DRAWING_VIEW );
      
  if( !ifail && hinge_line_tag != NULL_TAG )
      ifail = UF_DRAW_add_auxiliary_view( drawing_tag,
                                         parent_view_tag,
                                         hinge_line_tag,
                                         reference_point,
                                        &aux_view_tag );

  printf( "UF_DRAW_add_auxiliary_view " );
  if( ifail )
  {
      ifail = UF_get_fail_message( ifail, error_message );
      printf( "fails. \nError is:%s\n", error_message );
  }
  else if( part_tag == NULL_TAG )
      printf( "fails.\nError is: no active part.\n" );
  else if ( drawing_tag == NULL_TAG )
      printf( "fails.\nError is: no current drawing.\n" );
  else if ( curve_tag == NULL_TAG )
      printf( "fails.\nError is: no curve.\n" );
  else if ( parent_view_tag == NULL_TAG )
      printf( "fails.\nError is: no parent view.\n" );
  else if ( hinge_line_tag == NULL_TAG )
      printf( "fails.\nError is: no hinge line.\n" );
  else   
      printf( "is successful.\n" );
    
  ifail = UF_terminate();
}
