/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_revolution                                          *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates four *
 *   lines which are used as generator curves for creating a revolved feature.*
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_curve.h>
#include <uf_modl.h>
#include <uf.h>

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
  int  obj_count;
  UF_FEATURE_SIGN mode_sign = UF_NULLSIGN;
  tag_t generators[4], line1, line2, line3, line4, *objects;  
  char *body_limit[2] = {"0.0", "360.0"}; 
  char *offsets[2]= {"0.0", "0.0" };
  double origin[3] = {-2.0, 0.0, 0.0};
  double direction[3] = {0.0, 1.0, 0.0};
    
  UF_MODL_SWEEP_TRIM_object_p_t trim_data = NULL;   
    
  UF_CURVE_line_t sline1, sline2, sline3, sline4;

    /* line#1 */
  sline1.start_point[0] = 0.0; 
  sline1.start_point[1] = 0.0;
  sline1.start_point[2] = 0.0;
  sline1.end_point[0] = 0.0;
  sline1.end_point[1] = 1.0;
  sline1.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&sline1,&line1));

/* line#2 */
  sline2.start_point[0] = 0.0;
  sline2.start_point[1] = 1.0;
  sline2.start_point[2] = 0.0;
  sline2.end_point[0] = 2.5;
  sline2.end_point[1] = 3.5;
  sline2.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&sline2,&line2));
 
/* line#3 */
  sline3.start_point[0] = 2.5;
  sline3.start_point[1] = 3.5;
  sline3.start_point[2] = 0.0;
  sline3.end_point[0] = 1.0;
  sline3.end_point[1] = 0.0;
  sline3.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&sline3,&line3));

/* line#4 */
  sline4.start_point[0] = 1.0;
  sline4.start_point[1] = 0.0;
  sline4.start_point[2] = 0.0;
  sline4.end_point[0] = 0.0;
  sline4.end_point[1] = 0.0;
  sline4.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&sline4,&line4));

  generators[0] = line1;
  generators[1] = line2;
  generators[2] = line3;
  generators[3] = line4;

  UF_CALL(UF_MODL_create_revolution(generators, 4, trim_data,
                            body_limit, offsets, origin, false,
                            true, origin, direction, mode_sign,
                            &objects, &obj_count ));

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
