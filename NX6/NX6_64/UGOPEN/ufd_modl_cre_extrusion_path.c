/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_extrusion_path                                      *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part. The code creates a 4-sided  *
 *   polygon which is extruded along a guide path.                            *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_curve.h>
#include <uf.h>
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

  int obj_cnt;
  char *offsets[2] = {"0.0", "0.0"};
  UF_FEATURE_SIGN mode_sign = UF_NULLSIGN;
  tag_t line1, line2, line3, line4, guide, *objects;
  tag_t generators[4]; 
  double pt1[3] = {2.5, 3.5, 0.0};
  UF_CURVE_line_t mline1, mline2, mline3, mline4, mguide;

/* line 1 */   
  mline1.start_point[0] = 0.0;
  mline1.start_point[1] = 0.0;
  mline1.start_point[2] = 0.0;
  mline1.end_point[0] = 0.0;
  mline1.end_point[1] = 1.0;
  mline1.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&mline1, &line1));

/* line 2 */
  mline2.start_point[0] = 0.0;
  mline2.start_point[1] = 1.0;
  mline2.start_point[2] = 0.0;
  mline2.end_point[0] = 2.5;
  mline2.end_point[1] = 3.5;
  mline2.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&mline2, &line2));

/* line 3 */
  mline3.start_point[0] = 2.5;
  mline3.start_point[1] = 3.5;
  mline3.start_point[2] = 0.0;
  mline3.end_point[0] = 1.0;
  mline3.end_point[1] = 0.0;
  mline3.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&mline3, &line3));

/* line 4 */
  mline4.start_point[0] = 1.0;
  mline4.start_point[1] = 0.0;
  mline4.start_point[2] = 0.0;
  mline4.end_point[0] = 0.0;
  mline4.end_point[1] = 0.0;
  mline4.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&mline4, &line4));

  generators[0] = line1;
  generators[1] = line2;
  generators[2] = line3;
  generators[3] = line4;

/* Guide Line */
  mguide.start_point[0] = 2.5;
  mguide.start_point[1] = 3.5;
  mguide.start_point[2] = 0.0;
  mguide.end_point[0] = 2.5;
  mguide.end_point[1] = 3.5;
  mguide.end_point[2] = 1.0;
  UF_CALL(UF_CURVE_create_line(&mguide, &guide));

  
  UF_CALL(UF_MODL_create_extrusion_path(generators, 4, &guide, 1, NULL,
                                offsets, pt1, false, true,
                                mode_sign, &objects, &obj_cnt ));
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
