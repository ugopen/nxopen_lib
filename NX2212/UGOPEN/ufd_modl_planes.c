
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support creating and editing a plane:
 *
 *      UF_MODL_ask_plane
 *      UF_MODL_create_plane
 *      UF_MODL_edit_plane
 *
 * ========================================================================== */


#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_vec.h>


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

  char    *edge_length[3] = {"5.0", "5.0", "5.0"};
  char    *prtnam = "planes"; 

  double  dot_value;
  double  magnitude;
  double  origin[3] = {0.0, 0.0, 0.0};
  double  origin_point[3];
  double  pl1_normal[3];
  double  pl2_normal[3];
  double  unit_pl2_normal[3];
  
  tag_t   block_feat_tag;
  tag_t   part_tag;
  tag_t   plane1_tag;
  tag_t   plane2_tag;

  UF_FEATURE_SIGN create = UF_NULLSIGN;
  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /* Create a block of dimensions 5, 5, 5 */
  UF_CALL(UF_MODL_create_block1(create, origin, edge_length, &block_feat_tag));
  
  /* Create the first plane on a face of the block */
  origin_point[0] = 0.0;
  origin_point[1] = 0.0;
  origin_point[2] = 5.0;
  
  pl1_normal[0] = 0.0;
  pl1_normal[1] = 0.0;
  pl1_normal[2] = 1.0;
  
  UF_CALL(UF_MODL_create_plane(origin_point, pl1_normal, &plane1_tag));

  /* Create the second plane on the diagonally opposite face of the block */
  origin_point[0] = 5.0;
  origin_point[1] = 5.0;
  origin_point[2] = 0.0;
  
  pl2_normal[0] = 0.0;
  pl2_normal[1] = 0.0;
  pl2_normal[2] = 1.0;
  
  UF_CALL(UF_MODL_create_plane(origin_point, pl2_normal, &plane2_tag));

  /* Fetch the parameters of both the planes */
  UF_CALL(UF_MODL_ask_plane(plane1_tag, origin_point, pl1_normal));
  UF_CALL(UF_MODL_ask_plane(plane2_tag, origin_point, pl2_normal));

  /* Compute the dot product of plane normals and verify it to be 1 */
  /* normals should be identical */
  UF_VEC3_dot(pl1_normal, pl2_normal, &dot_value);

  if ( dot_value != 1.0 )
  {
     printf("***ERROR creating planes***\n");
  }
  
  /* Edit the second plane by changing it's normal by 90 degrees */
  pl2_normal[0] = 0.0;
  pl2_normal[1] = 1.0;
  pl2_normal[2] = 0.0;

  UF_CALL(UF_VEC3_unitize(pl2_normal, 0.0000002, &magnitude, unit_pl2_normal));
  UF_CALL(UF_MODL_edit_plane(plane2_tag, origin_point, unit_pl2_normal));

  /* Fetch the parameter again of the second plane */
  UF_CALL(UF_MODL_ask_plane(plane2_tag, origin_point, pl2_normal));
  
  /* Compute the dot product of plane normals and verify it to be 0 */
  UF_VEC3_dot(pl1_normal, pl2_normal, &dot_value);
  
  if ( dot_value != 0.0 )
  {
     printf("***ERROR editing planes***\n");
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



