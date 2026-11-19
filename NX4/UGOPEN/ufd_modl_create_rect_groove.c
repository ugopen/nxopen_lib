/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_rect_groove                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates a    *
 *   cylinder and a rectangular groove.                                       *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_modl.h>
#include <uf_object_types.h>
#include <uf_defs.h>
#include <uf.h>

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
  int count;
  int i;
  int type;
  int norm_dir;
  
  UF_FEATURE_SIGN sign = UF_NULLSIGN;
  tag_t cyl_obj_id;
  tag_t face;
  tag_t face_id;
  tag_t feature_id;
  tag_t body;
  uf_list_p_t face_list;
  double origin[3] = {0.0, 0.0, 0.0};
  double direction[3] = {0.0, 0.0, 1.0};
  double center[3];
  double dir[3];
  double box[6];
  double radius;
  double rad_data;
  double location[3] = {0.0,0.0,2.0};
  char *height = "4.0";
  char *diam   = "2.0";
  char *gr_diam = "1.0";
  char *width = "1.0";
  
  UF_CALL(UF_MODL_create_list(&face_list));
  UF_CALL(UF_MODL_create_cyl1(sign,origin,height,diam,direction,
                        &cyl_obj_id));
  UF_CALL(UF_MODL_ask_feat_body(cyl_obj_id, &body));
  UF_CALL(UF_MODL_ask_body_faces(body,&face_list));
  UF_CALL(UF_MODL_ask_list_count(face_list, &count));
  for(i = 0; i < count; i++) {
    UF_CALL(UF_MODL_ask_list_item(face_list,i,&face));
    UF_CALL(UF_MODL_ask_face_data(face, &type, center, dir, box, &radius,
                          &rad_data, &norm_dir));
    if(type == UF_cylinder_type) face_id = face;
  }
  UF_CALL(UF_MODL_create_rect_groove(location,direction,gr_diam,width,
                             face_id,&feature_id));
  UF_CALL(UF_MODL_delete_list(&face_list));

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
