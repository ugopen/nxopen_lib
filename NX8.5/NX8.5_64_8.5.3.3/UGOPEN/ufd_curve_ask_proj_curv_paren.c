/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_CURVE_create_proj_curves                                        *
 *         UF_CURVE_ask_proj_curves                                           *
 *         UF_CURVE_ask_proj_curve_parents                                    *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates proj_curve.prt. The code creates a block   *
 *   and a line and projects the line onto the blocks faces.                  *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <uf.h>
#include <uf_curve.h>
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

  int num_faces,i,num_proj_curves;

  double origin[3]={0.0,0.0,0.0};

  tag_t part_tag,block_tag,curves_to_proj[1];
  tag_t *faces,proj_curve_feature,*proj_curves;
  tag_t defining_feature,defining_target,defining_curve;

  char *part_name = "proj_curve";
  char *edge_lens[3]={"300.0","25.0","150.0"};

  UF_CURVE_line_t line_data;
  UF_CURVE_proj_t proj_data;
  uf_list_p_t face_list;


  UF_CALL(UF_PART_new(part_name,ENGLISH,&part_tag));

  UF_CALL(UF_MODL_create_block1(UF_NULLSIGN,
                                origin,
                                edge_lens,
                                &block_tag));

  line_data.start_point[0] =  25.0;
  line_data.start_point[1] =  50.0;
  line_data.start_point[2] =  25.0;
  line_data.end_point[0]   = 275.0;
  line_data.end_point[1]   =  50.0;
  line_data.end_point[2]   = 125.0;

  UF_CALL(UF_CURVE_create_line(&line_data,&curves_to_proj[0]));

  printf("curves to project tag = %d\n",curves_to_proj[0]);


  UF_CALL(UF_MODL_ask_feat_faces(block_tag,&face_list));

  UF_CALL(UF_MODL_ask_list_count(face_list,&num_faces));

  faces = (tag_t *)malloc(num_faces * sizeof(tag_t));
  for (i = 0;i < num_faces;i++)
  {
    UF_CALL(UF_MODL_ask_list_item(face_list,
  				  i,
  				  &faces[i]));
    printf("face %d of block tag = %d\n",i,faces[i]);
  }

  UF_CALL(UF_MODL_delete_list(&face_list));

  proj_data.proj_type = 3;
  proj_data.proj_vec[0] = 0.0;
  proj_data.proj_vec[1] = 1.0;
  proj_data.proj_vec[2] = 0.0;
  proj_data.multiplicity = 2;

  UF_CALL(UF_CURVE_create_proj_curves(1,
                                      curves_to_proj,
                                      num_faces,
                                      faces,
                                      3,
                                      &proj_data,
                                      &proj_curve_feature));

  printf("proj curve feature tag = %d\n",proj_curve_feature);

  UF_CALL(UF_CURVE_ask_proj_curves(proj_curve_feature,
                                   &num_proj_curves,
                                   &proj_curves));

  for (i = 0;i < num_proj_curves;i++)
  {
    UF_CALL(UF_CURVE_ask_proj_curve_parents(proj_curves[i],
                                            &defining_feature,
                                            &defining_target,
                                            &defining_curve));

    printf("proj_curves[%d]\n",i);
    printf("  belongs to feature tag = %d\n",defining_feature);
    printf("  was projected onto tag = %d\n",defining_target);
    printf("  was generated by curve tag = %d\n",
              defining_curve);
  }

  
  UF_free(proj_curves);
  free(faces);

}
/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
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