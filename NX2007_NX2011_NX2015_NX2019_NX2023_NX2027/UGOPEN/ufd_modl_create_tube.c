/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_tube                                                *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code generates a  *
 *   tube from a quarter arc and line.                                        *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_defs.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_curve.h>
#include <uf_csys.h>


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

    char *diams[2] = {"1.0","0.75"};
    tag_t objarc, objline;
    tag_t wcs_tag;
    uf_list_p_t tubelist, tubefeats;
    UF_CURVE_line_t line_coords;
    UF_CURVE_arc_t arc_coords;
    UF_FEATURE_SIGN sign = UF_NULLSIGN;

    UF_CALL(UF_CSYS_ask_wcs(&wcs_tag));
    UF_CALL(UF_CSYS_ask_matrix_of_object(wcs_tag, &arc_coords.matrix_tag));
    arc_coords.start_angle = 0.0;
    arc_coords.end_angle = PI/2;
    arc_coords.arc_center[0] = 0.0;
    arc_coords.arc_center[1] = 0.0;
    arc_coords.arc_center[2] = 0.0;
    arc_coords.radius = 1.0;

    UF_CALL(UF_CURVE_create_arc(&arc_coords,&objarc));

    line_coords.start_point[0] = 1.0;
    line_coords.start_point[1] = 0.0;
    line_coords.start_point[2] = 0.0;
    line_coords.end_point[0] = 1.0;
    line_coords.end_point[1] = -1.0;
    line_coords.end_point[2] = 0.0;

    UF_CALL(UF_CURVE_create_line(&line_coords,&objline));
    UF_CALL(UF_MODL_create_list(&tubelist));
    UF_CALL(UF_MODL_put_list_item(tubelist, objarc));
    UF_CALL(UF_MODL_put_list_item(tubelist, objline));
    UF_CALL(UF_MODL_create_tube(tubelist, diams, sign, &tubefeats));
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
