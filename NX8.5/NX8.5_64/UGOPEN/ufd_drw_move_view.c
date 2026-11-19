/*===========================================================================

        Copyright (c) 1998 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_move_view().  It is placed
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
#include <uf_view.h>

void ufusr(char *param, int *retcod, int param_len)
{
  int         ifail = 0;
  tag_t       view_tag = NULL_TAG;
  tag_t       part_tag = NULL_TAG;
  tag_t       drawing_tag = NULL_TAG;
  char        view_name[31] = "TOP@1";
  char        error_message[133];
  double      dwg_reference_pt[2] = {15.0, 24.5};
    
  ifail = UF_initialize();
    
  if( !ifail )
      part_tag = UF_PART_ask_display_part();
  
  if( !ifail && part_tag != NULL_TAG )
      ifail = UF_DRAW_ask_current_drawing( &drawing_tag );
  
  if( !ifail && part_tag != NULL_TAG && drawing_tag != NULL_TAG )
      ifail = UF_VIEW_ask_tag_of_view_name( view_name, 
                                           &view_tag );
		  
  if( !ifail && part_tag != NULL_TAG && 
       drawing_tag != NULL_TAG && view_tag != NULL_TAG )
      ifail = UF_DRAW_move_view( view_tag,
			                     dwg_reference_pt );
			                               
  printf( "UF_DRAW_move_view " );
  if( ifail )
  {
      ifail = UF_get_fail_message( ifail, error_message );
      printf( "fails. \nError is:%s\n", error_message );
  }
  else if( part_tag == NULL_TAG )
      printf( "fails.\nError is: no active part.\n" );
  else if ( drawing_tag == NULL_TAG )
      printf( "fails.\nError is: drawing not found.\n" );
  else if ( view_tag == NULL_TAG )
      printf( "fails.\nError is: view not found.\n" );
  else   
      printf( "is successful.\n" );

  ifail = UF_terminate();
}

