/*===========================================================================

        Copyright (c) 1998 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_VIEW_ask_vde_data().  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/
#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_view.h>

void ufusr(char *param, int *retcod, int param_len)
{
  int ifail = 0;
  int number_edits = 0;
  int inx = 0;
  tag_t object = NULL_TAG;
  tag_t part_tag = NULL_TAG;
  char *object_name = "NMDOBJ";
  char error_message[133];
  UF_VIEW_vde_data_p_t vde_data;
  
  ifail = UF_initialize();
  
  if( ifail == 0 )
      part_tag = UF_PART_ask_display_part();
  
  if( ifail == 0 && part_tag != NULL_TAG )
      ifail = UF_OBJ_cycle_by_name( object_name, &object );
  
  if( ifail == 0 && object != NULL_TAG )
      ifail = UF_VIEW_ask_vde_data( object, 
                                   &number_edits, 
                                   &vde_data );
      
  if (ifail == 0 && object != NULL_TAG )
      for (inx = 0; inx < number_edits; inx++ )
      {
      	  printf( "\nFor inx = %d, view_tag = %d\n",
      	           inx, vde_data[inx].view_tag );
      	  printf( "Parameter range = %f to %f\n",
      	           vde_data[inx].start_parameter, 
      	           vde_data[inx].end_parameter );
      	  printf( "color = %d, font = %d, width = %d\n",
      	           vde_data[inx].color, 
      	           vde_data[inx].font, 
      	           vde_data[inx].width );
      	           
          /* Code to manage the edits can go here */
      }
  
  UF_free(vde_data);

  printf( "UF_VIEW_ask_vde_data() sample " );
  if( ifail )
  {
      ifail = UF_get_fail_message( ifail, error_message );
      printf( "fails.\nError is: %s\n", error_message );
  }
  else if ( part_tag == NULL_TAG )
      printf( "fails.\nError is: no active part.\n" );
  else if ( object == NULL_TAG )
      printf( "fails.\nError is: named object not found.\n" );
  else    
      printf( "is successful.\n" );


  UF_terminate();

}
