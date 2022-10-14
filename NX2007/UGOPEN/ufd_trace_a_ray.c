
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support ray tracing:
 *
 *      UF_MODL_trace_a _ray
 **
 * ========================================================================== */


#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_defs.h>
#include <uf_modl.h>


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

  char    *edge_length[3] = {"5.0", "3.0", "10.0"};
  char    *prtnam = "trace_a_ray"; 
  char    *dia = "3.0";
  char    *height = "10.0";
  char    *cone_ht = "7.0";
  char    *cone_dias[2] = { "2.5","1.0" };
    
  double  cyl_dir[3] = {0.0, 0.0, 1.0};
  double  origin[3] = {0.0, 0.0, -5.0};
  double  cone_axis[3] = { 0.0,0.0,1.0};
  double transform[16] = { 1.0,0.0,0.0,0.0,
                           0.0,1.0,0.0,0.0,
                           0.0,0.0,1.0,0.0,
                           0.0,0.0,0.0,1.0 };
                           
  double point[3]  = { 2.0,-1.0,0.0 };
  double raydir[3] = { 8.0,5.0,0.0 };
    
  int     hits_found;
        
  tag_t   bodies[3];
  tag_t   feat_tag;
  tag_t   part_tag;

  UF_FEATURE_SIGN create = UF_NULLSIGN;
  UF_MODL_ray_hit_point_info_p_t  hit_list;
  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /* Create a block */
  UF_CALL(UF_MODL_create_block1(create, origin, edge_length, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &bodies[0]));

  /* Create a cylinder */
  origin[0] = 10.0;
  origin[1] = 0.0;
  origin[2] = 0.0;
  UF_CALL(UF_MODL_create_cyl1(create, origin, height, dia, cyl_dir, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &bodies[1]));

  /* Create a cone */
  origin[0] = 10.0;
  origin[1] = 4.0;
  origin[2] = -3.0;
  UF_CALL(UF_MODL_create_cone1(create, origin, cone_ht, cone_dias, cone_axis,
                               &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &bodies[2]))   ;
  
  /* fire the ray on the bodies */
  UF_CALL(UF_MODL_trace_a_ray( 3, bodies, point, raydir,
                               transform, 6, &hits_found, &hit_list )); 

  if ( hits_found != 4 )
     printf("*** ERROR from UF_MODL_trace_a_ray ***\n");
             
  if ( hit_list[0].hit_body != bodies[0] && hit_list[2].hit_body != bodies[2] )
     printf("*** ERROR from UF_MODL_trace_a_ray ***\n");

  UF_free(hit_list);

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



