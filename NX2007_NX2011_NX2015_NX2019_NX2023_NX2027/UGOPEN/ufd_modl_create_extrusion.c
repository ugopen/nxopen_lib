/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_extrusion                                           *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part. The code creates a unit     *
 *   block and a 4-sided polygon which is extruded and unioned to the bottom  *
 *   of the block.                                                            *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/


#include <stdlib.h>
#include <stdio.h>

#include <uf_curve.h>
#include <math.h>
#include <uf_modl.h>
#include <uf.h>

#define EPSILON (double)1.0e-7
#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static int report( char *file, int line, char *call, int irc)
{
  if (irc)
  {
     char    messg[133];
     printf("%s, line %d:  %s\n", file, line, call);
     (UF_get_fail_message(irc, messg)) ?
       printf("    returned a %d\n", irc) :
       printf("    returned error %d:  %s\n", irc, messg);
  }
  return(irc);
}

static void do_ugopen_api(void)
{

  int obj_cnt;
  char *offsets[2] = {"0.0", "0.0"};
  UF_FEATURE_SIGN mode_sign = UF_POSITIVE;
     
  UF_MODL_SWEEP_TRIM_object_t trim_object;
    
  int i, num;
  uf_list_p_t  face_list;
  double corner_pt[3] = { 0.0, 0.0, 2.0 };
  char *edges_len[3] = { "1", "1", "1" };
  char *limits[2]={ "0", "0" };
  char *taper_angle="0.0";
  tag_t blk_eid, face;
  tag_t trim_objects[1],line1, line2, line3, line4;
  tag_t *objects, generators[4]; 
  double pt1[3],face_dir[3],dir[3];
  UF_CURVE_line_t sline1, sline2, sline3, sline4;


  pt1[0]=0.0;
  pt1[1]=0.0;
  pt1[2]=0.0;

/* line#1 */
  sline1.start_point[0] = 0.0; 
  sline1.start_point[1] = 0.0;
  sline1.start_point[2] = 0.0;
  sline1.end_point[0] = 0.0;
  sline1.end_point[1] = 1.0;
  sline1.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&sline1,&line1));

/* line#2 */
  sline2.start_point[0] = 0.0;
  sline2.start_point[1] = 1.0;
  sline2.start_point[2] = 0.0;
  sline2.end_point[0] = 2.5;
  sline2.end_point[1] = 3.5;
  sline2.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&sline2,&line2));
 
/* line#3 */
  sline3.start_point[0] = 2.5;
  sline3.start_point[1] = 3.5;
  sline3.start_point[2] = 0.0;
  sline3.end_point[0] = 1.0;
  sline3.end_point[1] = 0.0;
  sline3.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&sline3,&line3));

/* line#4 */
  sline4.start_point[0] = 1.0;
  sline4.start_point[1] = 0.0;
  sline4.start_point[2] = 0.0;
  sline4.end_point[0] = 0.0;
  sline4.end_point[1] = 0.0;
  sline4.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&sline4,&line4));


/* line 4 */

  generators[0] = line1;
  generators[1] = line2;
  generators[2] = line3;
  generators[3] = line4;

  dir[0]=0.0; dir[1]=0.0; dir[2]=1.0;

/* create block 1x1x1 */

  UF_CALL(UF_MODL_create_block1( UF_NULLSIGN, corner_pt,
                                 edges_len, &blk_eid ));
  UF_CALL(UF_MODL_create_list( &face_list)); 

  UF_CALL(UF_MODL_ask_feat_faces( blk_eid, &face_list));
  UF_CALL(UF_MODL_ask_list_count( face_list,&num)); 

  trim_object.trim_count = 0;
    
  for ( i = 0; i < num; i ++ )
  {  
    int type, sense; 
    double point[3], box[6], radius, rad_data;
        
    UF_CALL(UF_MODL_ask_list_item(face_list, i, &face));
    UF_CALL(UF_MODL_ask_face_data(face, &type, point, face_dir,
                             box, &radius, &rad_data, &sense));
        
    if (type == 22 && fabs(face_dir[2] + 1) < EPSILON && (fabs(2.0 -               point[2]) < EPSILON ) )
    {
      trim_objects[0] = face;
      trim_object.trim_count = 1;
      trim_object.trim_objects = trim_objects;
      break;
    }
        
  }

  UF_CALL(UF_MODL_delete_list(&face_list));
  trim_object.sign =  UF_MODL_SWEEP_TRIM_TO_FACE;
    
      
  UF_CALL(UF_MODL_create_extrusion(generators, 4, &trim_object,
                                   taper_angle,limits,offsets,
                                   pt1, false, true, dir,
                                   mode_sign,&objects,&obj_cnt));

  UF_free(objects);
 
}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
{
  if (!UF_CALL(UF_initialize()))
  {
    do_ugopen_api();
    UF_CALL(UF_terminate());
  }
}

int ufusr_ask_unload(void)
{
  return (UF_UNLOAD_IMMEDIATELY);
}
