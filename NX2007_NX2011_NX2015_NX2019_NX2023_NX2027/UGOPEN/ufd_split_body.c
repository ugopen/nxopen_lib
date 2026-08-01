
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-1999 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support split of a body:
 *
 *      UF_MODL_split_body
 *
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

  char    *edge_length[3] = {"5.0", "5.0", "5.0"};
  char    *prtnam = "split_body"; 

  double  plane_dir[3] = {0.0, 0.0, 1.0};
  double  plane_pt[3] = {2.5, 2.5, 2.5};
  double  origin[3] = {0.0, 0.0, 0.0};

  int     num_splits;
        
  tag_t   body_tag;
  tag_t   feat_tag;
  tag_t   part_tag;
  tag_t   dplane_tag;
  tag_t   *split_bodies;

  UF_FEATURE_SIGN create = UF_NULLSIGN;
  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /* Create a block of dimensions 5, 5, 5 */
  UF_CALL(UF_MODL_create_block1(create, origin, edge_length, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &body_tag))   ;

  /* Create a datum plane at the center of block */
  UF_CALL(UF_MODL_create_fixed_dplane(plane_pt, plane_dir, &dplane_tag));
  
  /* split the body with the datum plane */
  UF_CALL(UF_MODL_split_body( 1, &body_tag, dplane_tag, &num_splits, 
                              &split_bodies )); 
  
  UF_free(split_bodies);
  

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



