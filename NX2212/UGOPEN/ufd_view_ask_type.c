/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_VIEW_ask_type.  It is placed directly in our UFUN 
 *    documentation starting with the include statements.
 *
 
 *
 ****************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_view.h>

void ufusr(char *param, int *retcod, int param_len)
{
  int         ifail = 0;
  char        error_message[MAX_LINE_BUFSIZE] = "";
  tag_t       model_view = NULL_TAG, dwg_sheet = NULL_TAG, dwg_member_view = NULL_TAG, unknown_view = NULL_TAG;
  UF_VIEW_type_t view_type;
  UF_VIEW_subtype_t view_subtype;
    
  ifail = UF_initialize();
   
   /* Retrieve view type for a modeling view. */                                        
  if ( !ifail )
    ifail = UF_VIEW_ask_tag_of_view_name("TOP", &model_view);
  
  if ( !ifail && model_view != NULL_TAG )
    ifail = UF_VIEW_ask_type(model_view, &view_type, &view_subtype);
    
  /* Retriev view type for a drawing sheet. */   
  if( !ifail )
    ifail = UF_VIEW_ask_tag_of_view_name("SH1@0", &dwg_sheet);
    
  if( !ifail && dwg_sheet != NULL_TAG )
    ifail = UF_VIEW_ask_type(dwg_sheet, &view_type, &view_subtype);
    
  /* Retrieve view type for a drawing member view. */
  if ( !ifail  )
    ifail = UF_VIEW_ask_tag_of_view_name("TOP@1", &dwg_member_view);
  
  if ( !ifail && dwg_member_view != NULL_TAG )
    ifail = UF_VIEW_ask_type(dwg_member_view, &view_type, &view_subtype);
    
  /* Retrieve view type for an unknown view type. */
  if ( !ifail  )
    ifail = UF_VIEW_ask_tag_of_view_name("NEWNAME", &unknown_view);
    
  if ( !ifail && unknown_view != NULL_TAG )
    ifail = UF_VIEW_ask_type(unknown_view, &view_type, &view_subtype);
    
  printf( "UF_VIEW_ask_type " );
  if( ifail )
  {
    ifail = UF_get_fail_message( ifail, error_message );
    printf( "fails.\nError is: %s\n", error_message );
  }
  else    
    printf( "is successful.\n" );
    
  ifail = UF_terminate();
}

