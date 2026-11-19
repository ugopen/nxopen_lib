/*===========================================================================

        Copyright (c) 1998,1999  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_VIEW_expand_view, UF_VIEW_unexpand_work_view, 
 *    and UF_VIEW_is_expanded.  It is placed directly in our UFUN 
 *    documentation starting with the include statements.
 *
 
 *
 ****************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_layout.h>
#include <uf_view.h>

/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
  int         ifail = 0;
  tag_t       view_tag = NULL_TAG;
  char        error_message[ MAX_LINE_BUFSIZE ] = "";
  char *      view_name = "TOP@1";
  char        layout_name[ UF_OBJ_NAME_BUFSIZE ] = "";
  char        work_view_name[ UF_OBJ_NAME_BUFSIZE ] = "";
  logical     is_expanded = FALSE;
    
  ifail = UF_initialize();
  
  if ( !ifail )
  /* Set the display state to drawing view */
      ifail = UF_DRAW_set_display_state( UF_DRAW_DRAWING_VIEW );
              
  if( !ifail )
    ifail = UF_VIEW_ask_tag_of_view_name( view_name, &view_tag );
   
   /* Test and validate expansion of a drawing member view. */                                        
  if ( !ifail && view_tag )
    ifail = UF_VIEW_expand_view( view_tag );
    
  /* Ensure that the view is in the expanded state. */   
  if( !ifail )
    ifail = UF_VIEW_is_expanded( &is_expanded );
    
  /* Unexpand the currently expanded view. */
  if ( ! ifail && is_expanded )
    ifail = UF_VIEW_unexpand_work_view();
        
  /* Set the display state to modeling view */
      ifail = UF_DRAW_set_display_state( UF_DRAW_MODELING_VIEW );
  
  /* Ask the names of the current layout and work view. */  
  if ( !ifail )
    ifail = uc6466( layout_name, work_view_name );
        
  if ( !ifail )
    ifail = UF_VIEW_ask_tag_of_view_name( work_view_name, &view_tag );
                                             
   /* Test and validate the expansion of the modeling work view. */
   if ( !ifail )
    ifail = UF_VIEW_expand_view( view_tag );
    
  printf( "UF_VIEW_expand_view for %s ", work_view_name );
  if( ifail )
  {
    ifail = UF_get_fail_message( ifail, error_message );
    printf( "fails.\nError is: %s\n", error_message );
  }
  else    
    printf( "is successful.\n" );
    
  ifail = UF_terminate();
}

