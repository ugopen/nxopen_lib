/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_CURVE_create_spline_thru_pts                                    *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates a    *
 *   spline through five points.                                              *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_curve.h>
#include <uf.h>

#define  NUMBER_POINTS  5
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

  /* B-spline parameters  */
  int degree = 3;
  int periodicity = 0;
  int num_points = NUMBER_POINTS;

  /* Point/slope curve attribute array */
  UF_CURVE_pt_slope_crvatr_t point_data[NUMBER_POINTS] =
   { 
      {  {-0.0539, 0.0511, 0.0000}, 
         UF_CURVE_SLOPE_AUTO,      {-0.3597, 0.9639, 0.0000},
         UF_CURVE_CRVATR_NONE,     {0.0000, 0.0000, 0.0000} 
      },
      {  {-0.4801, 0.8428, 0.0000}, 
         UF_CURVE_SLOPE_NONE,      {0.0000, 0.0000, 0.0000},
         UF_CURVE_CRVATR_NONE, {0.0000, 0.0000, 0.0000} 
      },
      {  {2.0000, 0.9000, 3.5956}, 
         UF_CURVE_SLOPE_NONE,      {0.0000, 0.0000, 0.0000},
         UF_CURVE_CRVATR_NONE,     {0.0000, 0.0000, 0.0000} 
      },
      {  {2.3456, 1.3456, 3.7890}, 
         UF_CURVE_SLOPE_DIR,       {0.5000, 1.0000, 0.5000},
         UF_CURVE_CRVATR_VEC,      {1.0000, -1.0000, 1.0000} 
      },
      {  {3.1000, 2.4567, 3.3214}, 
         UF_CURVE_SLOPE_VEC,       {1.0000, -2.0000, 1.0000},
         UF_CURVE_CRVATR_VEC,      {-1.0000, -1.0000, -1.0000} 
      }
   };


  /* Arrays of user's defining point data */
  double parameters[NUMBER_POINTS] = {0.00, 0.89,  1.73,  2.23,  2.85};

  int i, save_def_data = 1;
  tag_t spline_tag;


  /* Create B-spline curve */
  UF_CALL(UF_CURVE_create_spline_thru_pts(degree,
                                          periodicity,
                                          num_points,
		                          point_data,
                                          parameters,
                                          save_def_data,
                                          &spline_tag));
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
