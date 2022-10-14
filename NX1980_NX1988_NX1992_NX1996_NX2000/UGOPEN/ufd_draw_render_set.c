/*===========================================================================

        Copyright (c) 1999-2000,2004 Unigraphics Solutions Inc
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_create_render_set().  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/
#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_draw_types.h>
#include <uf_draw.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_view.h>

void ufusr(char *param, int *retcod, int param_len)
{
  int ifail = 0;
  int number_objects = 1;
  int number_sets_in_view = 0;
  int number_sets_in_part = 0;
  int number_render_sets = 0;
  int num_top_objects = 0;
  int number_bottom_objects = 2;
  int color_blue = 0;
  int color_red = 0;
  tag_t top_object = NULL_TAG;
  tag_t part_tag = NULL_TAG;
  tag_t top_render_set = NULL_TAG;
  tag_t bottom_render_set = NULL_TAG;
  tag_t member_view = NULL_TAG;
  tag_t drawing_tag = NULL_TAG;
  tag_t render_sets[2] = {NULL_TAG, NULL_TAG};
  tag_t bottom_objects[2] = {NULL_TAG, NULL_TAG};
  tag_t *render_sets_in_view = NULL;
  tag_t *top_objects = NULL;
  tag_t *render_sets_in_part = NULL;
  char *top_object_name = "TOPBOX";
  char *bottom_object_name = "BOTTOMBOX";
  char *mid_object_name = "MIDBOX";
  char *view_name = "TFR-ISO@6";
  char *top_render_set_name = "TOP_BOX";
  char *bottom_render_set_name = "BOTTOM_BOX";
  char error_message[133];
  UF_DRAW_render_prefs_t render_parms;
  
  ifail = UF_initialize();
  
  if( ifail == 0 )
      part_tag = UF_PART_ask_display_part();
  
  if( ifail == 0 && part_tag != NULL_TAG )
      ifail = UF_OBJ_cycle_by_name( top_object_name, &top_object );
  
  if( ifail == 0 && part_tag != NULL_TAG )
      ifail = UF_OBJ_cycle_by_name( bottom_object_name, &bottom_objects[0] );
  
  if( ifail == 0 && part_tag != NULL_TAG )
      ifail = UF_OBJ_cycle_by_name( mid_object_name, &bottom_objects[1] );
  
  if( ifail == 0 && part_tag != NULL_TAG )
      ifail = UF_DRAW_ask_render_set_parms( NULL_TAG, &render_parms );
  
  /* 1-22-04 Jason Bell NX3210 : map hardcoded colors to new color wheel */
  if( ifail == 0 && part_tag != NULL_TAG )
      ifail = UF_DISP_ask_closest_color_in_displayed_part(UF_DISP_MEDIUM_AZURE_BLUE_NAME,
                                                          &color_blue); /* blue */
  if( ifail == 0 && part_tag != NULL_TAG )
      ifail = UF_DISP_ask_closest_color_in_displayed_part(UF_DISP_MEDIUM_FADED_RED_NAME,
                                                          &color_red); /* red */

  /* Change some of the render set display parameters */
  render_parms.hidden_line  = UF_DRAW_hidden_line_removal_on;
  render_parms.hidden_line_color  = color_blue;
  render_parms.hidden_line_width  = UF_OBJ_WIDTH_THIN;
  render_parms.hidden_line_font  = UF_OBJ_FONT_DASHED;
  render_parms.visible_line_color  = color_red;
      
  render_parms.visible_line_font  = UF_OBJ_FONT_LONG_DASHED; 

  /* Show all hidden lines */ 
  render_parms.referenced_edges_only  = FALSE; 
  render_parms.edges_hidden_by_own_solid = TRUE; 
  
  if( ifail == 0 && part_tag != NULL_TAG )
      ifail = UF_DRAW_ask_current_drawing( &drawing_tag );
  
  if ( ifail == 0 )
      ifail = UF_VIEW_ask_tag_of_view_name(view_name, &member_view);
      
  if( ifail == 0 )
      ifail = UF_DRAW_create_render_set( top_render_set_name, 
                                        &render_parms, 
                                        &top_render_set );
      
  if( ifail == 0 && top_render_set != NULL_TAG )
  {
       number_render_sets++;
       render_sets[0] = top_render_set;
       ifail = UF_DRAW_set_render_set_objects( top_render_set,
                                               number_objects,
                                              &top_object );
  }
  if ( ifail == 0 )
       ifail = UF_DRAW_create_render_set( bottom_render_set_name, 
                                         &render_parms, 
                                         &bottom_render_set );
                                        
  if (ifail == 0 && bottom_render_set != NULL_TAG)
  {
      number_render_sets++;
      render_sets[1] = bottom_render_set;
      ifail = UF_DRAW_set_render_set_objects( bottom_render_set,
                                              number_bottom_objects,
                                              bottom_objects );
                                             
      /* Switch the colors for the bottom render set */
      render_parms.visible_line_color = color_blue;
      render_parms.hidden_line_color  = color_red;
      
      /* Change the line widths. */
      render_parms.visible_line_width = UF_OBJ_WIDTH_THICK;
      render_parms.hidden_line_width = UF_OBJ_WIDTH_ORIGINAL;
  }
  if ( ifail == 0 && bottom_render_set != NULL_TAG )
      ifail = UF_DRAW_set_render_set_parms( bottom_render_set, 
                                           &render_parms );
     
  if ( ifail == 0 && member_view != NULL_TAG )                                         
      ifail =  UF_DRAW_set_render_sets_for_view( member_view,
                                                 number_render_sets,
                                                 render_sets );                                          
  /* Determine Render Sets in View */
  if ( ifail == 0  && member_view != NULL_TAG )
      ifail = UF_DRAW_ask_render_sets_of_view( member_view,
                                              &number_sets_in_view,
                                              &render_sets_in_view);
   
  /* Ask display parameters of bottom render set */
  if ( bottom_render_set != NULL_TAG )
      ifail = UF_DRAW_ask_render_set_parms( bottom_render_set,
                                           &render_parms);
                 
                                              
  UF_free(render_sets_in_view);   
   
  /* Determine the objects in the top render set */
  if ( top_render_set != NULL_TAG )
      ifail = UF_DRAW_ask_render_set_objects( top_render_set,
                                             &num_top_objects,
                                             &top_objects);
  UF_free(top_objects);
  
  /* Force the view to update. */
  if ( drawing_tag != NULL_TAG )
      ifail = UF_DRAW_update_one_view( drawing_tag, member_view );
      
  /* Determine render sets in current part */
  if ( ifail == 0 && part_tag != NULL_TAG )
      ifail = UF_DRAW_ask_render_sets( &number_sets_in_part,
                                       &render_sets_in_part );
                                       
  UF_free(render_sets_in_part);                        

  printf( "UF_DRAW_create_render_set() sample " );
  if( ifail )
  {
      ifail = UF_get_fail_message( ifail, error_message );
      printf( "fails.\nError is: %s\n", error_message );
  }
  else if ( part_tag == NULL_TAG )
      printf( "fails.\nError is: no active part.\n" );
  else if ( top_object == NULL_TAG || bottom_objects[0] == NULL_TAG ||
            bottom_objects[1] == NULL_TAG )
      printf( "fails.\nError is: named object not found.\n" );
  else if ( member_view == NULL_TAG )
      printf( "fails.\nError is: view not found.\n" );
  else if ( drawing_tag == NULL_TAG )
      printf( "fails.\nError is: no current drawing.\n" );
  else    
      printf( "is successful.\n" );


  UF_terminate();

}
