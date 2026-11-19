/*===========================================================================

        Copyright (c) 1998 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_boundary_type.  It is placed
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
  tag_t       part_tag = NULL_TAG;
  tag_t       view_tag = NULL_TAG;
  char        error_message[133];
  char        *view_name = "TOP@1";
  UF_DRAW_boundary_type_t boundary_type;
    
  ifail = UF_initialize();
    
  if( !ifail )
      part_tag = UF_PART_ask_display_part();
    
  if( !ifail && part_tag != NULL_TAG  )
      ifail = UF_VIEW_ask_tag_of_view_name( view_name, 
  	                                       &view_tag );
  if( !ifail && view_tag != NULL_TAG && 
       view_tag != NULL_TAG )
      ifail = UF_DRAW_ask_boundary_type( view_tag, 
  			                            &boundary_type );
  if( !ifail )
      switch( boundary_type )
      {
      	case UF_DRAW_BREAK_DETAIL_TYPE:
        	printf( "Break line detail type. \n" );
            break;
        case UF_DRAW_MANUAL_RECTANGLE_TYPE:
        	printf( "Manual rectangle type. \n" );
            break;
        case UF_DRAW_AUTOMATIC_RECTANGLE_TYPE:
        	printf( "Automatic rectangle type. \n" );
            break;
        case UF_DRAW_BOUND_BY_OBJECTS_TYPE:
        	printf( "Bound by objects type. \n" );
            break;
        default:
        	break;
    	}
  
  printf( "UF_DRAW_ask_boundary_type " );
  if( ifail )
  {
      ifail = UF_get_fail_message( ifail, error_message );
      printf( "fails. \nError is:%s\n", error_message );
  }
  else if( part_tag == NULL_TAG )
      printf( "fails.\nError is: no active part.\n" );
  else if ( view_tag == NULL_TAG )
      printf( "fails.\nError is: view not found.\n" );
  else   
      printf( "is successful.\n" );	    
  ifail = UF_terminate();
}

