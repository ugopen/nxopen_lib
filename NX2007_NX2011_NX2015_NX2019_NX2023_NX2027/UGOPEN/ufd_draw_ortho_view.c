/*===========================================================================

        Copyright (c) 1998 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_add_orthographic_view().  It is placed
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
  double      reference_point[2] = {10.0, 12.0};
  int         ifail = 0;
  tag_t       drawing_tag = NULL_TAG;
  tag_t       part_tag = NULL_TAG;
  tag_t       parent_view_tag = NULL_TAG;
  tag_t       ortho_view_tag = NULL_TAG;
  char        error_message[133];
  char        *view_name = "TOP@1";
  UF_DRAW_proj_dir_t projection_direction = UF_DRAW_project_infer;
  
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
                                            false,        /* no occurrences */
                                            &parent_view_tag);
  }
                                 
  if( !ifail && parent_view_tag != NULL_TAG )
      ifail = UF_DRAW_add_orthographic_view( drawing_tag,
                                         parent_view_tag,
                                         projection_direction,
                                         reference_point,
                                        &ortho_view_tag );

  printf( "UF_DRAW_add_orthographic_view " );
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
  else   
      printf( "is successful.\n" );
    
  ifail = UF_terminate();
}

