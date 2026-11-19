/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_isocline_curves                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open, blank part. The code creates     *
 *   surface and isocline curves. The angle is incremented in 5 degree        *
 *   increments from 30 - 90 degrees.                                         *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_modl.h>
#include <uf.h>
#include <uf_ui.h>

#define TOL 0.001

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
/* B-surface parameters */
  double pole1[272] = {-3.033042,-9.000000,0.641636,1.000000,
                       -2.819874,-9.000000,0.919637,1.000000,
                       -2.435243,-9.000000,1.275825,1.000000,
                       -1.807612,-9.000000,1.395713,1.000000,
                       -1.354613,-9.000000,0.937392,1.000000,
                       -1.044966,-9.000000,0.571565,1.000000,
                       -0.883241,-9.000000,0.452738,1.000000,
                       -0.651919,-9.000000,0.385723,1.000000,
                       -0.340421,-9.000000,0.596172,1.000000,
                       -0.036815,-9.000000,0.757535,1.000000,
                        0.182856,-9.000000,0.617462,1.000000,
                        0.334729,-9.000000,0.437994,1.000000,
                        0.629579,-9.000000,-0.040704,1.000000,
                        1.123166,-9.000000,-0.482252,1.000000,
                        1.950353,-9.000000,0.115269,1.000000,
                        2.504707,-9.000000,0.916548,1.000000,
                        2.824460,-9.000000,1.481816,1.000000,
                       -2.986289,-5.925315,-5.782342,1.000000,
                       -2.987650,-5.925315,-5.206033,1.000000,
                       -2.954141,-5.925315,-4.065211,1.000000,
                       -2.759453,-5.925315,-1.921877,1.000000,
                       -2.399153,-5.925315,-0.123032,1.000000,
                       -1.984206,-5.925315,0.911653,1.000000,
                       -1.725177,-5.925315,1.312445,1.000000,
                       -1.317304,-5.925315,1.720948,1.000000,
                       -0.635971,-5.925315,1.757500,1.000000,
                        0.132939,-5.925315,1.697968,1.000000,
                        0.672025,-5.925315,1.961864,1.000000,
                        1.038267,-5.925315,2.245758,1.000000,
                        1.686029,-5.925315,3.001513,1.000000,
                        2.372259,-5.925315,4.176731,1.000000,
                        2.867826,-5.925315,5.127934,1.000000,
                        3.029237,-5.925315,5.439132,1.000000,
                        3.082648,-5.925315,5.531233,1.000000,
                       -2.919238,-3.081835,7.699265,1.000000,
                       -2.711035,-3.081835,6.978883,1.000000,
                       -2.325208,-3.081835,5.657372,1.000000,
                       -1.661236,-3.081835,3.472273,1.000000,
                       -1.136837,-3.081835,1.945551,1.000000,
                       -0.761729,-3.081835,1.135099,1.000000,
                       -0.565783,-3.081835,0.815819,1.000000,
                       -0.287779,-3.081835,0.471250,1.000000,
                        0.076189,-3.081835,0.361157,1.000000,
                        0.399688,-3.081835,0.324798,1.000000,
                        0.617050,-3.081835,0.091020,1.000000,
                        0.763465,-3.081835,-0.138356,1.000000,
                        1.030631,-3.081835,-0.741188,1.000000,
                        1.400327,-3.081835,-1.862081,1.000000,
                        1.911997,-3.081835,-3.368024,1.000000,
                        2.228114,-3.081835,-4.241339,1.000000,
                        2.404480,-3.081835,-4.706095,1.000000,
                       -2.898459,0.000000,-0.016719,1.000000,
                       -2.820424,0.000000,-0.004876,1.000000,
                       -2.653031,0.000000,0.011669,1.000000,
                       -2.277420,0.000000,0.020703,1.000000,
                       -1.847267,0.000000,0.000414,1.000000,
                       -1.434876,0.000000,-0.031169,1.000000,
                       -1.190609,0.000000,-0.051477,1.000000,
                       -0.816433,0.000000,-0.083356,1.000000,
                       -0.229142,0.000000,-0.133318,1.000000,
                        0.379704,0.000000,-0.166430,1.000000,
                        0.786214,0.000000,-0.173034,1.000000,
                        1.056826,0.000000,-0.172748,1.000000,
                        1.527896,0.000000,-0.158462,1.000000,
                        2.053852,0.000000,-0.103863,1.000000,
                        2.554006,0.000000,0.002525,1.000000,
                        2.793251,0.000000,0.075236,1.000000,
                        2.909607,0.000000,0.117034,1.000000};
  double u_knot[21] = {0.000000,0.000000,0.000000,
                      0.000000,0.062500,0.125000,
                      0.250000,0.312500,0.343750,
                      0.375000,0.500000,0.625000,
                      0.656250,0.687500,0.750000,
                      0.875000,0.937500,1.000000,
                      1.000000,1.000000,1.000000};
  double v_knot[8] = {0.000000,0.000000,0.000000,0.000000,
                      1.000000,1.000000,1.000000,1.000000};

/* Isocline parameters */
  double direction[3] = {0.0,0.0,1.0};
  double angle = 30.0;
  double dist_tol = TOL;

/* Text buffers for error messages */
  char message[133], buffer[133];
 
/* B-surface parameters */
  int num_pole_u = 17;
  int num_pole_v = 4;
  int u_ord = 4;
  int v_ord = 4;
  int knot1_fix;
  int pole1_fix;
  int total_iso_curves;

/* Error parameter */
  int err;

/* Count of isocline curves created */
  int isocurve_cnt;
  tag_t bsurf;
  tag_t *isocurve;

/* Open Motif Window for messages */
  UF_UI_open_listing_window();

/* Create B-surface */
  UF_CALL(UF_MODL_create_bsurf(num_pole_u,num_pole_v,u_ord,
        v_ord,u_knot,v_knot,pole1,&bsurf,&knot1_fix,&pole1_fix));
  
/* Create isocline curves */
  total_iso_curves = 0;
  while(angle <= 90.0) {
  err = UF_MODL_create_isocline_curves(bsurf,direction,angle,
                          dist_tol,&isocurve,&isocurve_cnt);
  if(err){
    UF_get_fail_message(err,message);
    sprintf(buffer,
            "\nError num %d in UF_MODL_create_isocline_curves:\n",err);
    UF_UI_write_listing_window(buffer);
    UF_UI_write_listing_window(message);
  }
  else {
    total_iso_curves += isocurve_cnt;
  }
  angle += 5.0;
  }

/* Write the number of created curves to the window */
  sprintf(buffer,"\nThe number of curves is: %d",total_iso_curves);
  UF_UI_write_listing_window(buffer);
/* Deallocate memory */
  UF_free(isocurve);

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
