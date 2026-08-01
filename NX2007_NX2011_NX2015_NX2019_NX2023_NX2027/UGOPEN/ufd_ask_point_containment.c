
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support ask point containment:
 *
 *      UF_MODL_ask_point_containment
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
  char    *prtnam = "ask_point_containment"; 

  double  pt_coord[3];
  double  origin[3] = {0.0, 0.0, 0.0};

  int     pt_status;
        
  tag_t   body_tag;
  tag_t   feat_tag;
  tag_t   part_tag;

  UF_FEATURE_SIGN create = UF_NULLSIGN;
  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /* Create a block of dimensions 5, 5, 5 */
  UF_CALL(UF_MODL_create_block1(create, origin, edge_length, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &body_tag));

  /* test a point inside the body */
  pt_coord[0] = 2.0;
  pt_coord[1] = 2.0;
  pt_coord[2] = 2.0;
    
  UF_CALL(UF_MODL_ask_point_containment(pt_coord, body_tag, &pt_status )); 
  
  if ( pt_status != 1 )
    printf("*** ERROR from UF_MODL_ask_point_containment ***\n");
  
  /* test a point outside the body */
  pt_coord[0] = 10.0;
  pt_coord[1] = 10.0;
  pt_coord[2] = 10.0;
    
  UF_CALL(UF_MODL_ask_point_containment(pt_coord, body_tag, &pt_status )); 
  
  if ( pt_status != 2 )
    printf("*** ERROR from UF_MODL_ask_point_containment ***\n");

  /* test a point on the body */
  pt_coord[0] = 5.0;
  pt_coord[1] = 5.0;
  pt_coord[2] = 5.0;
    
  UF_CALL(UF_MODL_ask_point_containment(pt_coord, body_tag, &pt_status )); 
  
  if ( pt_status != 3 )
    printf("*** ERROR from UF_MODL_ask_point_containment ***\n");
    
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



