/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_extruded                                            *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates and saves "arm.prt". The code extrudes     *
 *   lines and arcs along the z-axis. Three lines and two arcs are drawn.     *
 *   The center line is a reference line only, and is not included in the     *
 *   objects to be extruded.                                                  *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_curve.h>
#include <uf_csys.h>
#include <uf_modl.h>
#include <uf_disp.h>
#include <uf_part.h>


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
  double l1_endpt1[3] = {-1.4476606170268,2.3788333712953,0.0};
  double l1_endpt2[3] = { 1.5471310496399,2.2539419253757,0.0};
  double l2_endpt1[3] = {-1.4476606170268,1.2548103580189,0.0};
  double l2_endpt2[3] = { 1.5471310496399,1.3797018039385,0.0};
  double l3_endpt1[3] = {-1.4710981170268,1.8168218646571,0.0};
  double l3_endpt2[3] = { 1.5289018829732,1.8168218646571,0.0};
  double direction[3] = {0.0,0.0,1.0};
  double ref_pt[3];
  double arc1_start_ang = (PI/180)*87.611984536731;
  double arc1_end_ang   = (PI/180)*272.38801546327;
  double arc1_rad       = 0.5625;   
  double arc2_start_ang = (PI/180)*272.38801546327;
  double arc2_end_ang   = (PI/180)*447.61198453673;
  double arc2_rad       = 0.4375;

  char *part_name = "arm";
  char *taper_angle = "0.0";
  char *limit1[2] = {"1.0", "1.25"};

  int english_units = 2, i, count = 4;
  tag_t objarray[5], part, wcs_tag, matrix_tag;

  uf_list_p_t loop_list, features;
  UF_FEATURE_SIGN create = UF_NULLSIGN;

  UF_CURVE_line_t line1, line2, line3;
  UF_CURVE_arc_t arc1, arc2;

  line1.start_point[0] = l1_endpt1[0];
  line1.start_point[1] = l1_endpt1[1];
  line1.start_point[2] = l1_endpt1[2];
  line1.end_point[0]   = l1_endpt2[0];
  line1.end_point[1]   = l1_endpt2[1];
  line1.end_point[2]   = l1_endpt2[2];

  line2.start_point[0] = l2_endpt1[0];
  line2.start_point[1] = l2_endpt1[1];
  line2.start_point[2] = l2_endpt1[2];
  line2.end_point[0]   = l2_endpt2[0];
  line2.end_point[1]   = l2_endpt2[1];
  line2.end_point[2]   = l2_endpt2[2];

  line3.start_point[0] = l3_endpt1[0];
  line3.start_point[1] = l3_endpt1[1];
  line3.start_point[2] = l3_endpt1[2];
  line3.end_point[0]   = l3_endpt2[0];
  line3.end_point[1]   = l3_endpt2[1];
  line3.end_point[2]   = l3_endpt2[2];

  arc1.start_angle   = arc1_start_ang;
  arc1.end_angle     = arc1_end_ang;
  arc1.arc_center[0] = l3_endpt1[0];
  arc1.arc_center[1] = l3_endpt1[1];
  arc1.arc_center[2] = l3_endpt1[2];
  arc1.radius        = arc1_rad;

  arc2.start_angle   = arc2_start_ang;
  arc2.end_angle     = arc2_end_ang;
  arc2.arc_center[0] = l3_endpt2[0];
  arc2.arc_center[1] = l3_endpt2[1];
  arc2.arc_center[2] = l3_endpt2[2];
  arc2.radius        = arc2_rad;


  
  UF_CALL(UF_PART_new(part_name, english_units, &part));

  UF_CALL(UF_CURVE_create_line(&line1,&objarray[0]));
  UF_CALL(UF_CURVE_create_line(&line2,&objarray[1]));
  UF_CALL(UF_CURVE_create_line(&line3,&objarray[4]));

  UF_CALL(UF_CSYS_ask_wcs(&wcs_tag));
  UF_CALL(UF_CSYS_ask_matrix_of_object(wcs_tag, &matrix_tag));

  arc1.matrix_tag = matrix_tag;
  arc2.matrix_tag = matrix_tag;

  UF_CALL(UF_CURVE_create_arc(&arc1, &objarray[2]));
  UF_CALL(UF_CURVE_create_arc(&arc2, &objarray[3]));

  UF_CALL(UF_MODL_create_list(&loop_list));
  for(i = 0; i < count; i++) {
    UF_CALL(UF_MODL_put_list_item(loop_list, objarray[i]));
  }
  UF_CALL(UF_MODL_create_extruded(loop_list, taper_angle, limit1,
                          ref_pt, direction, create, &features));
  
  UF_PART_save();

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
