
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support ask face grid count:
 *
 *      UF_MODL_ask_face_grid_count
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
  char    *prtnam = "face_grid"; 

  double  origin[3] = {0.0, 0.0, 0.0};

  int     u_count;
  int     v_count;
        
  tag_t   body_tag;
  tag_t   feat_tag;
  tag_t   part_tag;

  UF_FEATURE_SIGN create = UF_NULLSIGN;
  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /* Create a block of dimensions 5, 5, 5 */
  UF_CALL(UF_MODL_create_block1(create, origin, edge_length, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &body_tag));

  /* fetch the U and V grid counts of the body. They both should be zero */
  UF_CALL(UF_MODL_ask_face_grid_count(body_tag, &u_count, &v_count));
  
  if ( u_count != 0 || v_count != 0 )
     printf("*** ERROR from UF_MODL_ask_face_grid_count ***\n");
     
  /* change the grid counts of the body to 10 and 5 respectively */
  u_count = 10;
  v_count = 5;
  UF_CALL(UF_MODL_edit_face_grid_count(body_tag, u_count, v_count));
  
  /* verify grid count by fetching them again */
  UF_CALL(UF_MODL_ask_face_grid_count(body_tag, &u_count, &v_count));
  
  if ( u_count != 10 || v_count != 5 )
     printf("*** ERROR from UF_MODL_ask_face_grid_count ***\n");  

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



