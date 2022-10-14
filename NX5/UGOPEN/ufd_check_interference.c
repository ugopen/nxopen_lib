
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-1999 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support check interference:
 *
 *      UF_MODL_check_interference
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
  char    *prtnam = "check_interference"; 
  char    *dia = "3.0";
  char    *height = "10.0";
  
  double  cyl_dir[3] = {0.0, 0.0, 1.0};

  double  origin[3] = {0.0, 0.0, 0.0};

  int     num_tools;
  int     results[2];
        
  tag_t   target;
  tag_t   tools[2];
  tag_t   feat_tag;
  tag_t   part_tag;

  UF_FEATURE_SIGN create = UF_NULLSIGN;
  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /* Create a block of dimensions 5, 5, 5 */
  UF_CALL(UF_MODL_create_block1(create, origin, edge_length, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &target))   ;

  /* Create a cylinder */
  UF_CALL(UF_MODL_create_cyl1(create, origin, height, dia, cyl_dir, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &tools[0]));
  
  /* Create another cylinder not intersecting block */
  origin[0] = 10.0;
  origin[1] = 0.0;
  origin[2] = 0.0;
  UF_CALL(UF_MODL_create_cyl1(create, origin, height, dia, cyl_dir, &feat_tag));
  UF_CALL(UF_MODL_ask_feat_body(feat_tag, &tools[1]));
  
  /* check interference of the tool bodies against the target */
  num_tools = 2;
  UF_CALL(UF_MODL_check_interference( target, num_tools, tools, results )); 
  
  if (results[0] != 1 || results[1] != 2)
     printf("*** ERROR from UF_MODL_check_interference ***\n");
  

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



