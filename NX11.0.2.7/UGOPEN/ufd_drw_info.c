/*===========================================================================

        Copyright (c) 1998, 2001 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_drawing_info() and 
 *    UF_DRAW_set_drawing_info().  It is placed
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
#include <uf_part.h>

static void determine_drawing_size(UF_DRAW_info_t *drawing_info, double size[2]);

static void determine_drawing_size(UF_DRAW_info_t *drawing_info, double size[2])
{                
  if ( drawing_info->size_state == UF_DRAW_CUSTOM_SIZE )
  {
      size[0] = drawing_info->size.custom_size[0];
      size[1] = drawing_info->size.custom_size[1];
  }
  else if ( drawing_info->size_state == UF_DRAW_ENGLISH_SIZE )
  {
      double english_sizes[8][2] = {{8.5, 11},      /* UF_DRAW_A */
                                     {11, 17},      /* UF_DRAW_B */
                                     {17, 22},      /* UF_DRAW_C */
                                     {22, 34},      /* UF_DRAW_D */
                                     {34, 44},      /* UF_DRAW_E */
                                     {28, 40},      /* UF_DRAW_F */
                                     {28, 44},      /* UF_DRAW_H*/
                                     {34, 55} };    /* UF_DRAW_J */
                                       
      /* subtract 1 because typedefs start at one. */
      size[0] = english_sizes[drawing_info->size.english_size_code - 1][0];
      size[1] = english_sizes[drawing_info->size.english_size_code - 1][1];
  }
  else
  {

      double metric_sizes[5][2] = {{841, 1189},     /* UF_DRAW_A0 */
                                   {594, 841},      /* UF_DRAW_A1 */
                                   {420, 594},      /* UF_DRAW_A2 */
                                   {297, 420},      /* UF_DRAW_A3 */
                                   {210, 297} };    /* UF_DRAW_A4 */

      /* subtract 1 because typedefs start at one. */
      size[0] = metric_sizes[drawing_info->size.metric_size_code - 1][0];
      size[1] = metric_sizes[drawing_info->size.metric_size_code - 1][1];
  }
}

void ufusr(char *param, int *retcod, int param_len)
{
  int         ifail = 0;
  tag_t       drawing_tag = NULL_TAG;
  tag_t       part_tag = NULL_TAG;
  UF_DRAW_info_t drawing_info;
  char        error_message[133];
  char		*draw_name = "SH1";
    
  ifail = UF_initialize();
    
  if( !ifail )
      part_tag = UF_PART_ask_display_part();
            
  if( !ifail && part_tag != NULL_TAG )
      ifail = UF_OBJ_cycle_by_name( draw_name, &drawing_tag );
                                             
  if( !ifail && part_tag != NULL_TAG && drawing_tag != NULL_TAG )
  {   
      ifail = UF_DRAW_ask_drawing_info( drawing_tag,
                                       &drawing_info );
  }
  printf( "UF_DRAW_ask_drawing_info() " );
  if( ifail )
  {
    ifail = UF_get_fail_message( ifail, error_message );
    printf( "fails.\nError is: %s\n", error_message );
  }
  else if ( part_tag == NULL_TAG )
    printf( "fails.\nError is: no active part.\n" );
  else if ( drawing_tag == NULL_TAG )
    printf( "fails.\nError is: no current drawing.\n" );
  else   
  {
    double size[2];
     
    printf( "is successful.\n" );
    printf( "The value of the drawing info structure is.\n" );
    printf( "size_state:  %d\n", drawing_info.size_state );
    if(drawing_info.size_state == UF_DRAW_METRIC_SIZE )
        printf( "standard metric size %d\n", drawing_info.size.metric_size_code );
    else if(drawing_info.size_state == UF_DRAW_ENGLISH_SIZE )
        printf( "standard english size %d\n", drawing_info.size.english_size_code );
    else
        printf("custom size = %f,  %f\n", drawing_info.size.custom_size[0], 
  		                                  drawing_info.size.custom_size[1] );
    printf( "scale:  %f\n", drawing_info.drawing_scale );
    if(drawing_info.projection_angle == UF_DRAW_THIRD_ANGLE_PROJECTION )
        printf(" projection angle : third \n" );
    else
        printf(" projection angle : first \n" );
  		
    determine_drawing_size(&drawing_info, size);
    printf("Size of drawing is %f x %f\n", size[0], size[1]);
  			                                  
   }
   
   /* Now change the values */
   
   if( !ifail && part_tag != NULL_TAG && drawing_tag != NULL_TAG )
   {
       drawing_info.size_state = UF_DRAW_CUSTOM_SIZE;
       drawing_info.size.custom_size[0] = 30.0;
       drawing_info.size.custom_size[1] = 45.0;
       drawing_info.drawing_scale = 1.5;
       drawing_info.units = UF_PART_ENGLISH;
       /* leave the projection angle the same, for simplicity */
       
       ifail = UF_DRAW_set_drawing_info( drawing_tag, &drawing_info );
  }     
  printf( "UF_DRAW_set_drawing_info() " );
  if( ifail )
  {
      ifail = UF_get_fail_message( ifail, error_message );
      printf( "fails.\nError is: %s\n", error_message );
  }
  else if ( part_tag == NULL_TAG )
      printf( "fails.\nError is: no active part.\n" );
  else if ( drawing_tag == NULL_TAG )
      printf( "fails.\nError is: no current drawing.\n" );
  else   
  {  
  	  printf( "is successful.\n" );
  }
  
    
  ifail = UF_terminate();
}

