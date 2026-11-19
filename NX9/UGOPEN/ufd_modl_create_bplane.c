/*===================================================================

        Copyright (c) 1998,2000  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_bplane                                              *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates a new part called "bplane.prt". The code   *
 *   creates a bounded plane with three interior hole loops. Thus there are a *
 *   total of four curve string loops.                                        *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_curve.h>
#include <uf_part.h>
#include <uf_csys.h>
#include <uf_cfi.h>

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
 /* bounded plane edge tolerance */
  double tol[3];
 /* data points for objects in loops */
  static double points[45] = { 4.,-2.,0.,4.,4.,0.,-4.,4.,0.,-4.,
    -4.,0.,0.,-2.,0.,-2.,3.,0.,-3.,3.,0.,-3.,2.,0.,
    -2.,2.,0.,-2.,-1.,0.,2.,3.,0.,3.,3.,0.,3.,2.,0.,
    2.,2.,0.,2.,3.,0.};
  static double startang = 0.0;
  static double endang = 6.28318530717958648;
  static double arcrad = 1.0;
  char prtnam[ UF_CFI_MAX_FILE_NAME_BUFSIZE ];
  int loops[4];
  int numlps = 4;
  int units =2;
  int arc = 1;
  int k, total;
  tag_t bpobj;
  tag_t part;
  tag_t objarray1[4];
  tag_t objarray2[3];
  tag_t objarray3, wcs_tag;
  tag_t objarray4[4];
  UF_STRING_t generator;
  UF_STRING_p_t ge = &generator;

  UF_CURVE_line_t line1;
  UF_CURVE_line_t line2;
  UF_CURVE_line_t line3;
  UF_CURVE_line_t line4;
  UF_CURVE_line_t line5;
  UF_CURVE_line_t line6;
  UF_CURVE_line_t line7;
  UF_CURVE_line_t line8;
  UF_CURVE_line_t line9;
  UF_CURVE_arc_t arc1;


  line1.start_point[0] = points[3];
  line1.start_point[1] = points[4];
  line1.start_point[2] = points[5];
  line1.end_point[0] = points[0];
  line1.end_point[1] = points[1];
  line1.end_point[2] = points[2];

  line2.start_point[0] = points[6];
  line2.start_point[1] = points[7];
  line2.start_point[2] = points[8];
  line2.end_point[0] = points[3];
  line2.end_point[1] = points[4];
  line2.end_point[2] = points[5];

  line3.start_point[0] = points[9];
  line3.start_point[1] = points[10];
  line3.start_point[2] = points[11];
  line3.end_point[0] = points[6];
  line3.end_point[1] = points[7];
  line3.end_point[2] = points[8];

  line4.start_point[0] = points[15];
  line4.start_point[1] = points[16];
  line4.start_point[2] = points[17];
  line4.end_point[0] = points[18];
  line4.end_point[1] = points[19];
  line4.end_point[2] = points[20];

  line5.start_point[0] = points[18];
  line5.start_point[1] = points[19];
  line5.start_point[2] = points[20];
  line5.end_point[0] = points[21];
  line5.end_point[1] = points[22];
  line5.end_point[2] = points[23];

  line6.start_point[0] = points[30];
  line6.start_point[1] = points[31];
  line6.start_point[2] = points[32];
  line6.end_point[0] = points[33];
  line6.end_point[1] = points[34];
  line6.end_point[2] = points[35];

  line7.start_point[0] = points[33];
  line7.start_point[1] = points[34];
  line7.start_point[2] = points[35];
  line7.end_point[0] = points[36];
  line7.end_point[1] = points[37];
  line7.end_point[2] = points[38];

  line8.start_point[0] = points[36];
  line8.start_point[1] = points[37];
  line8.start_point[2] = points[38];
  line8.end_point[0] = points[39];
  line8.end_point[1] = points[40];
  line8.end_point[2] = points[41];

  line9.start_point[0] = points[39];
  line9.start_point[1] = points[40];
  line9.start_point[2] = points[41];
  line9.end_point[0] = points[42];
  line9.end_point[1] = points[43];
  line9.end_point[2] = points[44];

  arc1.start_angle = startang;
  arc1.end_angle = endang;
  arc1.arc_center[0] = points[27];
  arc1.arc_center[1] = points[28];
  arc1.arc_center[2] = points[29];
  arc1.radius = arcrad;

  strcpy(prtnam,"bplane");
   
  UF_CALL(UF_PART_new(prtnam,units,&part));
  UF_CALL(UF_CSYS_ask_wcs(&wcs_tag));
  UF_CALL(UF_CSYS_ask_matrix_of_object(wcs_tag, &arc1.matrix_tag));

/* Create geometry for a bounded plane */
/* 1 peripheral loop and 3 hole loops */
/* Set up loop 1 - peripheral boundary - 3 lines and an arc */
  loops[0] = 4;
  UF_CALL(UF_CURVE_create_line(&line1, &objarray1[0]));
  UF_CALL(UF_CURVE_create_line(&line2, &objarray1[1]));
  UF_CALL(UF_CURVE_create_line(&line3, &objarray1[2]));
  FTN(uf5063)(&arc, points, &points[12], &points[9],
              &objarray1[3]);

/* Set up loop 2 - hole - 2 lines and an arc */
  loops[1] = 3;
  UF_CALL(UF_CURVE_create_line(&line4, &objarray2[0]));
  UF_CALL(UF_CURVE_create_line(&line5, &objarray2[1]));
  FTN(uf5063)(&arc, &points[21], &points[24], &points[15],
              &objarray2[2]);

/* Set up loop 3 - hole - single arc */
  loops[2] = 1;
  UF_CALL(UF_CURVE_create_arc(&arc1, &objarray3));

/* Set up loop 4 - hole - 4 lines */
  loops[3] = 4;
  UF_CALL(UF_CURVE_create_line(&line6, &objarray4[0]));
  UF_CALL(UF_CURVE_create_line(&line7, &objarray4[1]));
  UF_CALL(UF_CURVE_create_line(&line8, &objarray4[2]));
  UF_CALL(UF_CURVE_create_line(&line9, &objarray4[3]));
  UF_MODL_init_string_list(ge);
  UF_MODL_create_string_list(numlps,12,ge);

/* Store section loop data into string list structure. */
  total = 0;
  ge->string[0] = loops[0];
  ge->dir[0] = 1;
  for (k = 0; k < loops[0]; k++) ge->id[total++] = objarray1[k];
  ge->string[1] = loops[1];
  ge->dir[1] = -1;
  for (k = 0; k < loops[1]; k++) ge->id[total++] = objarray2[k];
  ge->string[2] = loops[2];
  ge->dir[2] = 1;
  ge->id[total++] = objarray3;
  ge->string[3] = loops[3];
  ge->dir[3] = -1;
  for (k = 0; k < loops[3]; k++) ge->id[total++] = objarray4[k];
  if (total != 12) printf("Error in total value!\n");
  tol[0] = .001;
  tol[1] = .5 * (PI/180);
  tol[2] = .02;
 
/* Create a bounded plane */
  UF_CALL(UF_MODL_create_bplane(ge,tol,&bpobj));
  UF_MODL_free_string_list(ge);

}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
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
