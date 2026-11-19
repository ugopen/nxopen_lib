/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_face_type                                              *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The example creates   *
 *   a feature (cylinder), extracts the faces, and inputs a face tag into     *
 *   UF_MODL_ask_face_type.                                                   *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_ui.h>

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

  double cyl_origin[3] = {0.0, 0.0, 0.0};
  double cyl_dir_vect[3] = {0.0, 0.0, 1.0};
  char *cyl_height = "1.5";
  char *cyl_diam = "2.0";
  char message[133];
  char buffer[133];
  UF_FEATURE_SIGN sign = UF_NULLSIGN;
  uf_list_p_t face_list;
  int list_count, err = 0,idx = 0, obj_type;
  tag_t cylinder = NULL_TAG;
  tag_t face = NULL_TAG;
  
  UF_CALL(UF_UI_open_listing_window());
  UF_CALL(UF_MODL_create_cyl1(sign,cyl_origin,cyl_height,cyl_diam,
                      cyl_dir_vect,&cylinder));
/* Get list of faces for cylinder. */
  UF_CALL(UF_MODL_ask_feat_faces(cylinder,&face_list));
  UF_CALL(UF_MODL_ask_list_count(face_list, &list_count));
/* Check that we have at least one face. */
  if(list_count)
  {
    UF_CALL(UF_MODL_ask_list_item(face_list,idx,&face));
  }
  else 
  {
    UF_UI_write_listing_window("No face was available!");
    return;
  }
/* Get the object type of the face. */
  err = UF_MODL_ask_face_type(face,&obj_type);
    
  if(err)
  {
    UF_UI_write_listing_window("Error in UF_MODL_ask_face_type:");
    UF_get_fail_message(err,message);
  }
  else
  {
    sprintf(buffer,"The object type value is: %d.\n",obj_type);
    UF_UI_write_listing_window(buffer);
  }
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
