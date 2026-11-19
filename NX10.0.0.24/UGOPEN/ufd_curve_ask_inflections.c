/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_CURVE_ask_curve_inflections                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates two  *
 *   planar B-curves and calculates their inflection points.                  *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <uf_modl.h>
#include <uf_defs.h>
#include <uf_curve.h>
#include <uf.h>
#include <uf_obj.h>
#include <stdio.h>
#include <string.h>

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
  int i, k, curve_cnt=0;
  tag_t curve_array[2];
  char newnam[ UF_OBJ_NAME_BUFSIZE ];
  int num_infpts;
  double range[]={0.0, 100.0}, *inf_pts;
  double proj_matrx[]={ 1.0, 0.0, 0.0, 0., 1.0, 0.0,0.0, 0.0, 1.0};
  int    knot1_fix, knot2_fix, pole1_fix, pole2_fix;
  
  double bc1_knots[] = {-3./8., -2./8., -1./8., 0.0, 1./8.,
                         2./8., 3./8., 4./8., 5./8., 6./8.,
                         7./8., 1.0, 9./8., 10./8., 11./8};
  double bc1_poles[] = { 2.0, 0.0, 0.0, 1.0,
                         4.0, 0.0, 0.0, 1.0,
                         3.5, 2.0, 0.0, 1.0,
                         6.0, 6.0, 0.0, 1.0,
                         2.0, 3.5, 0.0, 1.0,
                         0.0, 4.0, 0.0, 1.0,
                         0.0, 2.0, 0.0, 1.0,
                         0.0, 0.0, 0.0, 1.0,
                         2.0, 0.0, 0.0, 1.0,
                         4.0, 0.0, 0.0, 1.0,
                         3.5, 2.0, 0.0, 1.0  };
 
  double bc2_knots[] = {0.0, 0.0, 0.0, 1.0/3.0,
                        2.0/3.0, 1.0, 1.0, 1.0};
  double bc2_poles[] = {0.0, 0.0, 1.0, 1.0,
                        1.0, 2.0, 1.0, 1.0,
                        0.625, 0.0, 0.25, 0.25,
                        4.0, 2.0, 1.0, 1.0,
                        5.0, 0.0, 1.0, 1.0 };


  /*    create two B-curves   */
  UF_CALL(UF_MODL_create_spline(11,
                                4,
                                bc1_knots,
                                bc1_poles,
                                &curve_array[0],
                                &knot1_fix,
                                &pole1_fix));
    
  strcpy(newnam, "BCURVE_1") ;
  UF_CALL(UF_OBJ_set_name(curve_array[0], newnam)) ;
  curve_cnt ++; 

  UF_CALL(UF_MODL_create_spline(5,
                                3,
                                bc2_knots,
                                bc2_poles,
                                &curve_array[1],
                                &knot2_fix,
                                &pole2_fix));

  strcpy(newnam, "BCURVE_2") ;
  UF_CALL(UF_OBJ_set_name(curve_array[1], newnam)) ;
  curve_cnt ++;

  /* loop over each curve and compute their inflections */
  for (i = 0; i < curve_cnt; i++)
  {
  /* used a pre-definied projection matrix and predefined curve's
     range for the inflection points calculation
  */
    UF_CALL(UF_CURVE_ask_curve_inflections(curve_array[i],
                                         proj_matrx,
                                         range,
                                         &num_infpts,
                                         &inf_pts));
    

   /* free the memory taken by the inflection points */
    if (num_infpts > 0)
    {
      printf("There are %d inflection points for curve %d\n",
             num_infpts, i+1);
      for(k = 0; k < (num_infpts * 4); k++)
      {
        printf("inf_pts[%d] = %f\n", k, inf_pts[k]);
      }
      UF_free(inf_pts);
    }
        
  }

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
