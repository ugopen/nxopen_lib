/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_proj_curves                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open blank part. The code creates      *
 *   two planes and one arc. The arc is projected onto the planes.            *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_modl.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_curve.h>
#include <uf_csys.h>
#include <uf_disp.h>

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

  int along_face = 1;
  int not_along_face = 0;

  tag_t arctag;
  tag_t wcs_tag;
  tag_t wcs_planetag; 
  tag_t planetag;
  tag_t proj1tag;
  tag_t proj2tag;

  uf_list_p_t curve_refs;
  uf_list_p_t face1_refs;
  uf_list_p_t face2_refs;

  UF_CURVE_arc_t arc_coords;

  double plan1orig[3] = { 0.0, 0.0, 0.0 };
  double plan2orig[3] = { 0.0, 0.0, 3.0 };
  double x1axpt[3] = { 1.0, 0.0, 0.0 };
  double x2axpt[3] = { 1.0, 0.0, 3.0 };
  double plan1pt[3] = { 1.0, 1.0, 0.0 };
  double plan2pt[3] = { 0.0, .70710678118655, 3.70710678118655 };
  double proj_vector[3] = { 0.0, 0.0, 1.0 };
  
  /* Create planes and arc */
  FTN(uf5374)(plan1orig, x1axpt, plan1pt, &wcs_planetag);
  FTN(uf5374)(plan2orig, x2axpt, plan2pt, &planetag);

  UF_CALL(UF_CSYS_ask_wcs(&wcs_tag));
  UF_CALL(UF_CSYS_ask_matrix_of_object(wcs_tag, &arc_coords.matrix_tag));
  arc_coords.start_angle = 0.0;
  arc_coords.end_angle = 2 * PI;
  arc_coords.arc_center[0] = 1.0;
  arc_coords.arc_center[1] = 1.0;
  arc_coords.arc_center[2] = 6.0;
  arc_coords.radius = 0.5;
  UF_CALL(UF_CURVE_create_arc(&arc_coords, &arctag));

  UF_CALL(UF_MODL_create_list(&curve_refs));
  UF_MODL_create_list(&face1_refs);
  UF_MODL_create_list(&face2_refs);
  UF_MODL_put_list_item(curve_refs, arctag);
  UF_MODL_put_list_item(face1_refs, wcs_planetag);
  UF_MODL_put_list_item(face2_refs, planetag);
  UF_CALL(UF_MODL_create_proj_curves(curve_refs, face1_refs,
                              along_face,proj_vector, &proj1tag));
  UF_CALL(UF_MODL_create_proj_curves(curve_refs, face2_refs,
                          not_along_face,proj_vector, &proj2tag));
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
