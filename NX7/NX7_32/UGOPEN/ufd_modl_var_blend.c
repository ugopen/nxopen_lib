/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_var_blend                                                  *
 *         UF_MODL_create_blend                                               *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank open part. The code creates a     *
 *   block and blends the verticle edges of the block using a variable radii. *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_modl.h>
#include <math.h>

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

static int vrb_routine(tag_t eid, double points[100][3], char radii[100][256],
                       int smooth_overflow, int cliff_overflow,
                       int notch_overflow, double vrb_tol,
                       int *number_of_points)
{
    int
        v_count;

    double edge_pt1[3],
           edge_pt2[3];
    
    /* Get the end points of the edge. */
    UF_CALL(UF_MODL_ask_edge_verts(eid, edge_pt1,edge_pt2,&v_count));
    *number_of_points = v_count;

    /* Use a variable blend radius. */
    if(edge_pt1[2] > edge_pt2[2])
    {
       strcpy(radii[0], "0.3");
       strcpy(radii[1],"0.1");
    }
    else
    {
       strcpy(radii[0], "0.1");
       strcpy(radii[1], "0.3");
    }

       points[0][0] = edge_pt1[0];
       points[0][1] = edge_pt1[1];
       points[0][2] = edge_pt1[2];
       points[1][0] = edge_pt2[0];
       points[1][1] = edge_pt2[1];
       points[1][2] = edge_pt2[2];
    
    return(0);
}

static void do_ugopen_api(void)
{
  UF_FEATURE_SIGN sign  = UF_NULLSIGN;
  double block_orig[3] = {0.0,0.0,0.0},
         pt1[3],
         pt2[3],
         vrb_tol = 0.00001;
  char *block_len[3] = {"1.0","2.0","3.0"};
  tag_t blk_obj,
        edge,
        feat_id;
  uf_list_p_t edge_list1,
              edge_list2;

  int
      index,
      num_edges,
      smooth_overflow = UF_MODL_BLEND_SMOOTH_OVERFLOW,
      cliff_overflow  = UF_MODL_BLEND_CLIFF_OVERFLOW,
      notch_overflow  = UF_MODL_BLEND_NOTCH_OVERFLOW,
      vcount;


  /* Create a block feature. */
  UF_CALL(UF_MODL_create_block1(sign, block_orig, block_len, &blk_obj));

  /* Create list */
  UF_CALL(UF_MODL_create_list(&edge_list1));

  /* Get blocks edges. */
  UF_CALL(UF_MODL_ask_feat_edges(blk_obj, &edge_list1));

  UF_CALL(UF_MODL_create_list(&edge_list2));

  /* Get count of edges. */
  UF_CALL(UF_MODL_ask_list_count(edge_list1, &num_edges));

  /* Get edges of length 3.0 and put the edges in a list. */
  for(index = 0; index < num_edges; index++)
  {
     UF_CALL(UF_MODL_ask_list_item(edge_list1, index, &edge));
     UF_CALL(UF_MODL_ask_edge_verts(edge,pt1,pt2,&vcount));

     if(fabs(fabs(pt1[2] - pt2[2]) - 3.0) < 0.001)
     {
        UF_CALL(UF_MODL_put_list_item(edge_list2,edge));
     }
  }
  /* Free the list. */
  UF_CALL(UF_MODL_delete_list(&edge_list1));

  /* Register the variable blend routine. */
  UF_CALL(UF_MODL_register_var_blend(vrb_routine));

  /* Create the variable blend. */
  UF_CALL(UF_MODL_create_blend("0.009246", edge_list2, smooth_overflow,
                          cliff_overflow, notch_overflow, vrb_tol, &feat_id));

  /* Unregister the variable blend routine. */
  UF_CALL(UF_MODL_unregister_var_blend());

  /* Free second edge list. */
  UF_CALL(UF_MODL_delete_list(&edge_list2));

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
