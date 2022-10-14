/*===========================================================================

        Copyright (c) 1998 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_import_view().  It is placed
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
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>

void ufusr(char *param, int *retcod, int param_len)
{
  int         ifail = 0;
  double      reference_point[2] = {10.0, 12.0};
  tag_t       drawing_tag = NULL_TAG;
  tag_t       part_tag = NULL_TAG;
  tag_t       view_tag = NULL_TAG;
  tag_t       draw_view_tag = NULL_TAG;
  char        error_message[133];
  char        *view_name = "BOTTOM";
  
    
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
                                            false,     /* skip occurrences */
                                            &view_tag );

      if( !ifail && view_tag != NULL_TAG )
      {  
          UF_DRAW_view_info_t view_info;

          UF_DRAW_initialize_view_info( &view_info );
          view_info.inherit_boundary = TRUE;

          ifail = UF_DRAW_import_view( drawing_tag,
                                       view_tag,
                                       reference_point,
                                       &view_info,
                                       &draw_view_tag );
      }
  }
  printf( "UF_DRAW_import_view " );
  if( ifail )
  {
      ifail = UF_get_fail_message( ifail, error_message );
      printf( "fails. \nError is:%s\n", error_message );
  }
  else if( part_tag == NULL_TAG )
      printf( "fails.\nError is: no active part.\n" );
  else if ( drawing_tag == NULL_TAG )
      printf( "fails.\nError is: no current drawing.\n" );
  else if ( view_tag == NULL_TAG )
      printf( "fails.\nError is: invalid view tag.\n" );
  else   
      printf( "is successful.\n" );
    
  ifail = UF_terminate();
}

