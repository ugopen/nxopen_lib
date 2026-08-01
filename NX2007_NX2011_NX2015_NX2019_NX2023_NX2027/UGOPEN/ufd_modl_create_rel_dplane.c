/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_relative_dplane                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open, blank part. The code creates a   *
 *   block and then uses two edges of the block as constraints for creating a *
 *   relative dplane.                                                         *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <math.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_obj.h>

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
  int ecount,
      i,
      vcount,
      num_refs = 2,
      point_select[] = {UF_MODL_EDGE,
                        UF_MODL_EDGE,
                        0},
      which_plane=1,
      num_dplanes;

  char *edge_len[] = {"1.0", "2.0", "3.0"};

  double origin[] = {0.0, 0.0, 0.0},
         pt1[3],
         pt2[3];

  tag_t block_feat_tag,
        block_body_tag,
        edge,
        edge1,
        edge2,
        object_tags[3],
        dplane_tag[2];

  uf_list_p_t list1,  /* list of edges */
              list2;  /* list of top 2 edges */

  UF_FEATURE_SIGN create = UF_NULLSIGN;

  /* Create a block feature. */
  UF_CALL(UF_MODL_create_block1(create, origin, edge_len, &block_feat_tag));

  /* Get the body tag of the feature. */
  UF_CALL(UF_MODL_ask_feat_body(block_feat_tag, &block_body_tag));

  /* Get block edges. */
  UF_CALL(UF_MODL_ask_body_edges(block_body_tag, &list1));

  /* Get the edge count */
  UF_CALL(UF_MODL_ask_list_count(list1, &ecount));

  /* Create list2, a list of two parallel edges. */
  UF_CALL(UF_MODL_create_list(&list2));

  /* Loop through all object edges and get their vertices. */
  for(i=0; i < ecount; i++)
  {
     /* Get an edge from the list. */
     UF_CALL(UF_MODL_ask_list_item(list1,i,&edge));

     /* Get the edge vertices. */
     UF_CALL(UF_MODL_ask_edge_verts(edge,pt1,pt2,&vcount));

     if((fabs(fabs(pt1[0] - pt2[0]) - 1.0) < 0.001) &&
         (fabs(pt1[2] - 3.0) < 0.001) &&
         (fabs(pt2[2] - 3.0) < 0.001))
     {
       /* Put item on list2. */
       UF_CALL(UF_MODL_put_list_item(list2,edge));
     }
   }
   UF_CALL(UF_MODL_ask_list_count(list2, &ecount));

   UF_CALL(UF_MODL_ask_list_item(list2, 0, &edge1));
   UF_CALL(UF_MODL_ask_list_item(list2, 1, &edge2));
  
   object_tags[0] = edge1;
   object_tags[1] = edge2;
   object_tags[2] = NULL_TAG;

   /* Get and print the edge vertices. */
   UF_CALL(UF_MODL_ask_edge_verts(object_tags[0],pt1,pt2,&vcount));
   printf("\nedge1 vertices are: (%f,%f,%f), (%f,%f,%f)\n",
           pt1[0],pt1[1],pt1[2],pt2[0],pt2[1],pt2[2]);

   UF_CALL(UF_MODL_ask_edge_verts(object_tags[1],pt1,pt2,&vcount));
   printf("\nedge2 vertices are: (%f,%f,%f), (%f,%f,%f)\n",
           pt1[0],pt1[1],pt1[2],pt2[0],pt2[1],pt2[2]);

   /* Deallocate memory from lists. */
   UF_CALL(UF_MODL_delete_list(&list1));
   UF_CALL(UF_MODL_delete_list(&list2));

   /* Create a relative dplane on top of the block by using two
      "Through Edge" constraints. We are not using three of the
      parameters, so we set them to NULL.
   */
   UF_CALL(UF_MODL_create_relative_dplane(num_refs,
                                          object_tags,
                                          point_select,
                                          which_plane,
                                          NULL,
                                          NULL,
                                          NULL,
                                          &num_dplanes,
                                          dplane_tag));

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
