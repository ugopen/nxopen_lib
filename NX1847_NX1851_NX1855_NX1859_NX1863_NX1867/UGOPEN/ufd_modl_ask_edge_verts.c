/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_edge_verts                                             *
 *         UF_MODL_ask_object                                                 *
 *         UF_MODL_ask_body_edges                                             *
 *         UF_MODL_ask_list_count                                             *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part with a solid body. The code  *
 *   gets the number of vertices for each edge in the solid.                  *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_object_types.h>

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

  tag_t obj_id = 0;
  tag_t edge_id = 0;
  tag_t view;

  uf_list_p_t edge_list;
  uf_list_p_t face_list;

  UF_UI_selection_options_t opts;
  UF_UI_mask_t mask = {UF_solid_type,0,UF_UI_SEL_FEATURE_BODY};


  int edge_count = 0;
  int face_count = 0;
  int index, vertex, response;

  double p1[3]={0.0, 0.0, 0.0}, p2[3]={0.0, 0.0, 0.0}, cursor[3];
  opts.num_mask_triples = 1;
  opts.mask_triples = &mask;
  opts.scope = UF_UI_SEL_SCOPE_WORK_PART;

  response = 4;
  do
  {
    UF_CALL(UF_UI_select_single("Select a solid body", &opts,
                              &response, &obj_id,
                              cursor, &view));

    if((response == 4) || (response == 5))
    {
   
      UF_MODL_ask_body_edges(obj_id, &edge_list);
      UF_MODL_ask_list_count(edge_list, &edge_count);
      UF_MODL_ask_body_faces(obj_id, &face_list);
      UF_MODL_ask_list_count(face_list, &face_count);
  
      for(index = 0; index < edge_count; index++) 
      {
        printf("\nInfo for edge number: %d\n", index);
        UF_MODL_ask_list_item(edge_list, index, &edge_id);
        UF_MODL_ask_edge_verts(edge_id, p1, p2, &vertex);
        printf("The number of vertices is: %d\n", vertex);
        switch(vertex)
        {
          case 0:
            printf("There are no vertices on this edge.\n");
            break;
          case 1:
            printf("The X value of P1 is: %f\n", p1[0]);
            printf("The Y value of P1 is: %f\n", p1[1]);
            printf("The Z value of P1 is: %f\n", p1[2]);
            break;
          case 2:
            printf("The X value of P1 is: %f\n", p1[0]);
            printf("The Y value of P1 is: %f\n", p1[1]);
            printf("The Z value of P1 is: %f\n", p1[2]);
            printf("The X value of P2 is: %f\n", p2[0]);
            printf("The Y value of P2 is: %f\n", p2[1]);
            printf("The Z value of P2 is: %f\n", p2[2]);
            break;
          default:
            break;
        }
      }
    }
    printf("Total number of faces: %d\n", face_count);
  }while((response == 4) || (response ==5));

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
