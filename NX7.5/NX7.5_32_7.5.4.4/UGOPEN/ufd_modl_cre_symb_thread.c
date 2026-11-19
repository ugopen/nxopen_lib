/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_symb_thread                                         *
 *         UF_MODL_ask_symb_thread_parms                                      *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates symbolic_thread.prt. The code creates a    *
 *   a box and a symbolic thread.                                             *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/
#include <stdio.h>
#include <math.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_part.h>



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

  tag_t part_tag;
  tag_t blk_id, feature_eid, boss_id;
  tag_t face, s_face, c_face;
  char *part_name = "symbolic_thread";
  char *edge_len[3];
  double point[3], dir[3], box[6], radius, rad;
  int i, num, type, sen; 
  uf_list_p_t list;
  UF_MODL_symb_thread_data_t thread; 

  UF_CALL(UF_PART_new(part_name,ENGLISH,&part_tag));

/*
  Create block(10x10x10) at (0,0,0)
*/
  edge_len[0] = "10.0";
  edge_len[1] = "10.0";
  edge_len[2] = "10.0";
  point[0] = 0.0, point[1] = 0.0, point[2] = 0.0;
  UF_CALL(UF_MODL_create_block1(UF_NULLSIGN,point,edge_len,&blk_id));
/*
  Get faces of the block
*/
  UF_CALL(UF_MODL_ask_feat_faces(blk_id,&list));
  UF_CALL(UF_MODL_ask_list_count(list,&num));
/*
  Get face data
*/
  for (i=0; i<num; i++)
  {
    UF_CALL(UF_MODL_ask_list_item(list,i,&face));

    UF_CALL(UF_MODL_ask_face_data(face,&type,point,
                                  dir,box,&radius,&rad,&sen));
    if (fabs(dir[2]-1.0)< 10e-7)
    {
      point[0] = box[0] + 2.0;
      point[1] = box[1] + 2.0;
      UF_CALL(UF_MODL_create_boss(point,dir,
                                  "0.85","0.6","0.0",face,&boss_id));
      break;
    }
  } 
  UF_MODL_delete_list(&list);

/*
  Get boss feature faces
*/
  UF_MODL_ask_feat_faces(boss_id,&list);
  UF_MODL_ask_list_count(list,&num);
  for (i=0;i<num;i++)
  {
    UF_CALL(UF_MODL_ask_list_item(list,i,&face));
 
    UF_CALL(UF_MODL_ask_face_data(face,&type,point,dir,box,
				&radius,&rad,&sen));
    if (type == 22) /* Planar face */
      s_face = face;
    if (type == 16) /* Cylindrical face */
      c_face = face;
  }
  UF_MODL_delete_list(&list);
/*
  Create symbolic thread
*/
  thread.cyl_face = c_face;
  thread.start_face = s_face;
  thread.axis_direction[0]=0;
  thread.axis_direction[1]=0;
  thread.axis_direction[2]=-1;
  thread.include_instances = UF_MODL_INCL_INSTANCES;
  thread.rotation=UF_MODL_RIGHT_HAND;
  thread.length_flag=UF_MODL_FIXED_LENGTH;
  thread.tapered = UF_MODL_NON_TAPERED;
  thread.num_starts = 1;
  thread.length="1.0";
  thread.form = "Unified";
  thread.method = "CUT";
  thread.callout = "1-8_UNC";
  thread.major_dia = "1.0";
  thread.minor_dia = "0.8512";
  thread.tapped_dia = "0.8985";
  thread.pitch = "0.125";
  thread.angle = "60";
  UF_CALL(UF_MODL_create_symb_thread(&thread, &feature_eid));

/*
  Retrieve data
*/
  if(!UF_CALL(UF_MODL_ask_symb_thread_parms(feature_eid, &thread)))
  {
/*
  Print data
*/
    printf("Cylindrical face tag = %d\n", thread.cyl_face);
    printf("Start face tag = %d\n", thread.start_face);
    printf("Thread axis direction = (%f,%f,%f)\n",
      thread.axis_direction[0],thread.axis_direction[1],
      thread.axis_direction[2]);
    printf("Number of starts = %d\n", thread.num_starts);
    if (thread.include_instances == UF_MODL_INCL_INSTANCES)
      printf("Include instances = Yes\n");
    else
      printf("Include instances = No\n");
    if (thread.rotation == UF_MODL_RIGHT_HAND)
      printf("Rotation = Right_hand\n");
    else
      printf("Rotation = Left_hand\n");
    if (thread.length_flag == UF_MODL_FIXED_LENGTH)
      printf("Thread length flag = Fixed length\n");
    else
      printf("Thread length flag = Full thread\n");
    if (thread.tapered == UF_MODL_TAPERED)
      printf("Thread tapered = Yes\n");
    else
      printf("Thread tapered = No\n");

    printf("Length expression %s\n", thread.length);
    printf("Form = %s\n", thread.form);
    printf("Callout = %s\n", thread.callout);
    printf("Method = %s\n", thread.method);
    printf("Major diameter expression %s\n", thread.major_dia);
    printf("Minor diameter expression %s\n", thread.minor_dia);
    printf("Tapped diameter expression %s\n", thread.tapped_dia);
    printf("Pitch expression %s\n", thread.pitch);
    printf("Angle expression %s\n", thread.angle);
  }

  UF_free(thread.length);
  UF_free(thread.form);
  UF_free(thread.method);
  UF_free(thread.callout);
  UF_free(thread.major_dia);
  UF_free(thread.minor_dia);
  UF_free(thread.tapped_dia);
  UF_free(thread.pitch);
  UF_free(thread.angle);

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
