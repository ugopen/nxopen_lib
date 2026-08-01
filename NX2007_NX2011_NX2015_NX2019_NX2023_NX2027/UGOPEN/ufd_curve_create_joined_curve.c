/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routines:        *
 *                                                                            *
 *         UF_CURVE_create_joined_curve                                       *
 *         UF_CURVE_create_joined_feature                                     *
 *         UF_CURVE_edit_joined_feature                                       *
 *         UF_CURVE_ask_joined_parms                                          *
 *         UF_CURVE_ask_feature_curves                                        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open, blank part. The code creates     *
 *   a line, two arcs, and then joins them into a single spline.              *
 *   The code then creates a joined curve feature out of the same set of      *
 *   input curves and asks for the joined curve.  Then it fetches the         *
 *   creation parameters of the feature.  It then changes the creation        *
 *   method to General Spline and updates the feature.                        *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_modl.h>
#include <uf.h>
#include <uf_curve.h>
#include <uf_csys.h>
#include <uf_defs.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))
#define POLYCUBIC 1
#define GENERAL   2

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

  int status;
  int creation_method;
  int num_curves;

  double tolerances[3];

  UF_CURVE_line_t line_coords = {0.0,0.0,0.0,
                                -0.21270493542778,
                                 0.70074856926871,0.0};
  UF_CURVE_arc_t arc_coords1 = {NULL_TAG,28.04*DEGRA,241.95*DEGRA,
                                -0.01574459461337,1.07054857743090,
                                0.0,0.41898140995808},
                 arc_coords2 = {NULL_TAG,213.8*DEGRA,440.21*DEGRA,
                                0.94059259791199,1.66017663043580,
                                0.0,0.70584261761220};

  tag_t line1;
  tag_t arc1;
  tag_t arc2;
  tag_t joined_curve, wcs_tag, matrix_tag;
  tag_t joined_feature, *curves; 

  uf_list_p_t curves_list;
 
  UF_STRING_t uf_string, ask_uf_string;
  
  /* Create lines */
  UF_CALL(UF_CURVE_create_line(&line_coords, &line1));

  /* Create arc1 */
  UF_CALL(UF_CSYS_ask_wcs(&wcs_tag));
  UF_CALL(UF_CSYS_ask_matrix_of_object(wcs_tag,&matrix_tag));
  arc_coords1.matrix_tag=matrix_tag;
  arc_coords2.matrix_tag=matrix_tag;

  UF_CALL(UF_CURVE_create_arc(&arc_coords1,&arc1));



  /* Create arc2 */
  UF_CALL(UF_CURVE_create_arc(&arc_coords2,&arc2));

  /* create list of curves */
  UF_CALL(UF_MODL_create_list(&curves_list));

  /* put curve objects in list */
  UF_MODL_put_list_item(curves_list, line1);
  UF_MODL_put_list_item(curves_list, arc1);
  UF_MODL_put_list_item(curves_list, arc2);
  creation_method = POLYCUBIC;

  /* join arcs and line */
  if(UF_CALL(UF_CURVE_create_joined_curve(curves_list, 
                                          creation_method,
                                          &joined_curve,
                                          &status)))
  {
     /* error check */
  }
  else
  {
     /* Check the status */
     if (status)
       printf("\nJoined Curve spline has corners.\n");
     else
       printf("\nJoined Curve spline has no corners.\n");
  }

  /* create UF_STRING as input to create a feature */
  UF_MODL_init_string_list(&uf_string);
  UF_MODL_create_string_list(1,
                             3,
                             &uf_string);

  uf_string.num = 1;
  uf_string.string[0] = 3;
  uf_string.dir[0] = 1;
  uf_string.id[0] = line1;
  uf_string.id[1] = arc1;
  uf_string.id[2] = arc2;

  /* Create a joined curve feature */
  UF_MODL_delete_list(&curves_list);
  if(UF_CALL(UF_CURVE_create_joined_feature(&uf_string, 
                                            creation_method,
                                            &joined_feature,
                                            &status)))
  {
     /* error check */
  }
  else
  {
     /* Check the status */
     if (status)
       printf("\nJoined Curve spline has corners.\n");
     else
       printf("\nJoined Curve spline has no corners.\n");
  }
  UF_MODL_free_string_list(&uf_string);

  /* Ask for the joined curve from the feature */
  if(UF_CALL(UF_CURVE_ask_feature_curves(joined_feature, 
                                         &num_curves,
                                         &curves)))
  {
     /* error check */
  }

  /* Ask for the creation parameters of the feature */
  if(UF_CALL(UF_CURVE_ask_joined_parms(joined_feature,
                                       &ask_uf_string, 
                                       &creation_method,
                                       tolerances)))
  {
     /* error check */
  }

  /* Change the creation method to General Spline */  
  creation_method = GENERAL;
  if(UF_CALL(UF_CURVE_edit_joined_feature(joined_feature,
                                          &ask_uf_string, 
                                          creation_method,
                                          tolerances)))
  {
     /* error check */
  }
  UF_MODL_free_string_list(&ask_uf_string);

  /* Trigger update */  
  if(UF_CALL(UF_MODL_update()))
  {
     /* error check */
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
