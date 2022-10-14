
/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support create arc through three points:
 *
 *      UF_MODL_create_arc_thru_3pts
 *
 * ========================================================================== */


#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_defs.h>
#include <uf_eval.h>
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

  char    *prtnam = "curve_thru_3_pts"; 

  double  limits[2];
  double  pt1[3] = { 1.0, 0.0, 1.0};
  double  pt2[3] = { 0.0, 0.0, 2.0};
  double  pt3[3] = { -1.0, 0.0, 1.0};

  tag_t   part_tag;
  tag_t   arc_tag;
  
  int     flag;
  
  UF_EVAL_p_t    arc_evaluator;
  UF_EVAL_arc_t  arc_data;  

  

  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  /* create an arc thru 3 pts whose limits should be 0 and pi */
  flag = 1;
  UF_CALL(UF_CURVE_create_arc_thru_3pts(flag, pt1, pt2, pt3, &arc_tag));

  /* Fetch the parameters of the arc */
  UF_CALL(UF_EVAL_initialize( arc_tag,  &arc_evaluator ));
  UF_CALL(UF_EVAL_ask_arc( arc_evaluator, &arc_data ));
  UF_CALL(UF_EVAL_ask_limits( arc_evaluator, limits ));
  UF_CALL(UF_EVAL_free( arc_evaluator ));  
  
  if ( (limits[0] != 0.0) || (limits[1] != PI) )
  {
     printf("*** ERROR creating arc thru 3 pts ***\n");  
  }    

  /* now, create a circle thru 3 pts whose limits should be 0 and twopi */
  flag = 2;
  UF_CALL(UF_CURVE_create_arc_thru_3pts(flag, pt1, pt2, pt3, &arc_tag));

  /* Fetch the parameters of both the planes */
  UF_CALL(UF_EVAL_initialize( arc_tag,  &arc_evaluator ));
  UF_CALL(UF_EVAL_ask_arc( arc_evaluator, &arc_data ));
  UF_CALL(UF_EVAL_ask_limits( arc_evaluator, limits ));
  UF_CALL(UF_EVAL_free( arc_evaluator ));  
  
  if ( (limits[0] != 0.0) || (limits[1] != TWOPI) )
  {
     printf("*** ERROR creating arc thru 3 pts ***\n");  
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



