/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_trim_sheet                                                 *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requiers a blank, open part. The code creates      *
 *   a b-surface and then trims the sheet body by projecting two curves.      *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_modl_error.h>

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
    int    knot_fixup,pole_fixup;
    tag_t  bcurv1,bcurv2,bsurf;

    int    bsurf_idata[] = {4,4,4,4};
    double bsurf_uknot[] = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0};
    double bsurf_vknot[] = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0};
    double bsurf_poles[] = {0.0,0.0,6.0,1.0,
                            2.0,2.0,6.0,1.0,
                            5.0,1.5,6.0,1.0,
                            8.0,3.0,6.0,1.0,
                            0.0,2.0,4.0,1.0,
                            2.0,4.0,4.0,1.0,
                            5.0,3.5,4.0,1.0,
                            8.0,5.0,4.0,1.0,
                            0.0,2.0,2.0,1.0,
                            2.0,4.0,2.0,1.0,
                            5.0,3.5,2.0,1.0,
                            8.0,5.0,2.0,1.0,
                            0.0,0.0,0.0,1.0,
                            2.0,2.0,0.0,1.0,
                            5.0,1.5,0.0,1.0,
                            8.0,3.0,0.0,1.0} ;
    int    bcurv1_idata[] = {3,3} ;
    double bcurv1_knots[] = {0.0,0.0,0.0,1.0,1.0,1.0};
    double bcurv1_poles[] = {-0.5,-2.5,3.5,1.0,
                              2.5,-2.5,3.5,1.0,
                              2.5,-2.5,6.5,1.0};

    int    bcurv2_idata[] = {8,4} ;
    double bcurv2_knots[] = {-0.6,-0.4,-0.2,0.0,0.2,
                              0.4, 0.6, 0.8,1.0,1.2,
                              1.4, 1.6};
    double bcurv2_poles[] = {3.0,-2.5,2.0,1.0,
                             4.0,-2.5,1.0,1.0,
                             7.0,-2.5,1.0,1.0,
                             6.0,-2.5,3.0,1.0,
                             3.0,-2.5,3.0,1.0,
                             3.0,-2.5,2.0,1.0,
                             4.0,-2.5,1.0,1.0,
                             7.0,-2.5,1.0,1.0};

    UF_MODL_trim_object_t   trim_objects[2];
    UF_MODL_trim_object_p_t trim_objects_p[2];

    int num_gaps,return_code,discard = 0;
    double proj_vector[] = {0.0,1.0,0.0};
    double ptdata[] = {1.312,1.896,4.8,
                       4.464,3.312,2.4};
    double *gap_pts,tol = 0.001;
 
/*
   Create the b-surface.
*/
    UF_CALL(UF_MODL_create_bsurf(bsurf_idata[0],
                                       bsurf_idata[1],
                                       bsurf_idata[2],
                                       bsurf_idata[3],
                                       bsurf_uknot,
                                       bsurf_vknot,
                                       bsurf_poles,
                                       &bsurf,
                                       &knot_fixup,
                                       &pole_fixup));
/*
   Create the splines.
*/
    UF_CALL(UF_MODL_create_spline(bcurv1_idata[0],
                                        bcurv1_idata[1],
                                        bcurv1_knots,
                                        bcurv1_poles,
                                        &bcurv1,
                                        &knot_fixup,
                                        &pole_fixup));

    UF_CALL(UF_MODL_create_spline(bcurv2_idata[0],
                                        bcurv2_idata[1],
                                        bcurv2_knots,
                                        bcurv2_poles,
                                        &bcurv2,
                                        &knot_fixup,
                                        &pole_fixup));
/*
   Build the trim_object structures.
*/
    trim_objects_p[0] = &trim_objects[0];
    trim_objects_p[1] = &trim_objects[1];

    trim_objects_p[0]->object_tag = bcurv1;
    trim_objects_p[0]->curve_project_method = 2;
    trim_objects_p[1]->object_tag = bcurv2;
    trim_objects_p[1]->curve_project_method = 2;
/*
   Trim the sheet.
*/
    return_code = UF_CALL(UF_MODL_trim_sheet(bsurf,2,trim_objects_p,
                                     proj_vector,discard,2,ptdata,
                                     tol,&num_gaps,&gap_pts));
    if (return_code == CURVES_HAVE_GAPS) UF_free(gap_pts);

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
