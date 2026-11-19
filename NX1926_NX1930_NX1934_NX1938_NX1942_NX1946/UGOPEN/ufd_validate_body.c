
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support validation of bodies:
 *
 *      UF_MODL_validate_body
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
  char    *dia = "3.0";
  char    *height = "10.0";
  
  double  cyl_dir[3] = {0.0, 0.0, 1.0};
  double  cyl_origin[3] = {10.0, 0.0, 0.0};

  double  origin[3] = {0.0, 0.0, 0.0};

  int     num_bodies;
  int     valid[2] = {0, 0};
        
  tag_t   bodies[2];
  tag_t   feat_tag;
  tag_t   part_tag;

  UF_FEATURE_SIGN create = UF_NULLSIGN;
  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /* Create a block of dimensions 5, 5, 5 */
  UF_CALL(UF_MODL_create_block1(create, origin, edge_length, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &bodies[0]))   ;

  /* Create a cylinder at different origin */
  UF_CALL(UF_MODL_create_cyl1(create, cyl_origin, height, dia, cyl_dir, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &bodies[1]))   ;
  
  /* validate the bodies */
  num_bodies = 2;
  UF_CALL(UF_MODL_validate_body( num_bodies, bodies, valid )); 
  
  if (valid[0] != 1 && valid[1] != 1)
     printf("*** ERROR from UF_MODL_validate_body ***\n");
  

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



