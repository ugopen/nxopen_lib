/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_CURVE_create_combine_curves                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates      *
 *   geometry and shows a sample for creating a combined curve.               *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_curve.h>
#include <uf_defs.h>
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

  UF_CURVE_combine_curves_direction_t first_dir;
  UF_CURVE_combine_curves_direction_t second_dir;
  UF_CURVE_combine_curves_direction_t ask_first_dir;
  UF_CURVE_combine_curves_direction_t ask_second_dir;
  UF_CURVE_line_t line_coords;
  uf_list_p_t curve_list;
  double first_vect[3] = {0.,0.,1.};
  double second_vect[3] = {0.,-1.,0.};
  double curve_tol;
  tag_t line1;
  tag_t line2;
  tag_t line3;
  tag_t feature_tag;
  tag_t ask_line1;
  tag_t ask_line2;
  char crv_aprox_tol[133];
  char *ask_tol;
  
/* Ask system distance tolerance */
  UF_MODL_ask_distance_tolerance(&curve_tol);
  sprintf(crv_aprox_tol, "%.15g", curve_tol);

/* Create geometry */
  line_coords.start_point[0] = 0.0;
  line_coords.start_point[1] = 0.0;
  line_coords.start_point[2] = 0.0;
  line_coords.end_point[0] = 0.0;
  line_coords.end_point[1] = 2.0;
  line_coords.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&line_coords, &line1));

  line_coords.start_point[0] = -2.0;
  line_coords.start_point[1] = 3.0;
  line_coords.start_point[2] = 4.0;
  line_coords.end_point[0] = 4.0;
  line_coords.end_point[1] = 3.0;
  line_coords.end_point[2] = 4.0;
  UF_CALL(UF_CURVE_create_line(&line_coords, &line2));

  line_coords.start_point[0] = 0.0;
  line_coords.start_point[1] = 0.0;
  line_coords.start_point[2] = 0.0;
  line_coords.end_point[0] = 2.0;
  line_coords.end_point[1] = 2.0;
  line_coords.end_point[2] = 0.0;
  UF_CALL(UF_CURVE_create_line(&line_coords, &line3));


/* Initialize the projection information */
  first_dir.direction_type = UF_CURVE_ALONG_FIXED_VECTOR;
  first_dir.direction_struct.vector[0] = first_vect[0];
  first_dir.direction_struct.vector[1] = first_vect[1];
  first_dir.direction_struct.vector[2] = first_vect[2];

  second_dir.direction_type = UF_CURVE_ALONG_FIXED_VECTOR;
  second_dir.direction_struct.vector[0] = second_vect[0];
  second_dir.direction_struct.vector[1] = second_vect[1];
  second_dir.direction_struct.vector[2] = second_vect[2];

/* Create the combined curve */
  UF_CALL(UF_CURVE_create_combine_curves(line1, &first_dir, line2,
                                         &second_dir, crv_aprox_tol,
                                         &feature_tag));

/* Ask the input parameters for the combined feature just created */
  UF_CALL(UF_CURVE_ask_combine_curves(feature_tag, &ask_line1,
                                      &ask_first_dir, &ask_line2,
                                      &ask_second_dir, &ask_tol,
                                      &curve_list));

  UF_MODL_delete_list(&curve_list);

/* Edit the combined curve feature just created, by replacing one
   of the input curves */
  UF_CALL(UF_CURVE_edit_combine_curves(feature_tag, line3,
                                       &ask_first_dir, ask_line2,
                                       &ask_second_dir, ask_tol));

  UF_free(ask_tol);
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
