/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_intersect_objects.c                                        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates a    *
 *   B-surface, arc, and two lines. One line intersects the B-surface and the *
 *   other line is coincident to an edge. The arc intersects the              *
 *   B-surface twice.                                                         *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_modl.h>
#include <uf.h>
#include <uf_obj.h>
#include <uf_curve.h>
#include <uf_defs.h>
#include <uf_csys.h>
#include <uf_disp.h>


#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static void get_intersect(tag_t curve, tag_t face, double tol);


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

  tag_t  base_sheet_id, line_id;
  tag_t face, arc_tag, line2_id;
  
  int num_pole_u = 4;
  int num_pole_v = 4;
  int u_ord = 4;
  int v_ord = 4;
  int knot_fix;
  int pole_fix;
  int color;

  int i, j, k = 0;

  UF_CURVE_line_t line_coords  = {1.5,1.5,-2,1.5,1.5,1.0};
  UF_CURVE_line_t line_coords2 = {0.0, 3.0, 0.0};
  UF_CURVE_arc_t arc_coords = {NULL_TAG,0.0,180*DEGRA,1.5,0.0,-1.5,0.25};
  uf_list_p_t list;

  double weight = 1.0;
  double u_knot[9] = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0};
  double v_knot[9] = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0};
  double pole[64];
  double tol = .001;
  double matrix_values[9] = {1.0, 0.0, 0.0,
                             0.0, 0.0, 1.0,
                             0.0, 1.0, 0.0};


/* Create pole array data. */
  for (i = 0; i < 4; i++) {
    for (j = 0; j < 4; j++) {
      pole[k++] = i;
      pole[k++] = j;
      pole[k++] = 0.0;
      pole[k++] = weight;
    }
  }


  /* Create base surface. */
  UF_CALL(UF_MODL_create_bsurf(num_pole_u, num_pole_v, u_ord, v_ord,
                       u_knot, v_knot,pole,&base_sheet_id,
                       &knot_fix,&pole_fix));

  /* Get faces. */
  UF_CALL(UF_MODL_ask_body_faces(base_sheet_id,&list));
  UF_CALL(UF_MODL_ask_list_item(list,0,&face));
  UF_CALL(UF_MODL_delete_list(&list));

  /* Create line. */
  UF_CALL(UF_CURVE_create_line(&line_coords,&line_id));

  /* Get line intersection. */
  get_intersect(line_id, face, tol);

  /* Create coincident line. */
  UF_CALL(UF_CURVE_create_line(&line_coords2,&line2_id));
  UF_CALL(UF_DISP_ask_closest_color_in_displayed_part(UF_DISP_MEDIUM_ORANGE_YELLOW_NAME,&color));
  UF_CALL(UF_OBJ_set_color(line2_id,color)) ;

  /* Get coincident line intersection data */
  get_intersect(line2_id, face, tol);

  /* Create arc. */
  UF_CALL(UF_CSYS_create_matrix(matrix_values,&arc_coords.matrix_tag));
  UF_CALL(UF_CURVE_create_arc(&arc_coords, &arc_tag));


  /* Get arc intersection. */
  get_intersect(arc_tag, face, tol);

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

static void get_intersect(tag_t curve, tag_t face, double tol)
{
  int num_intersects, type, i;
  UF_MODL_intersect_info_p_t *intersect_data;


  UF_CALL(UF_MODL_intersect_objects(curve,face,tol,
                                    &num_intersects,&intersect_data));
  printf("\n Number of intersections = %d\n", num_intersects);

  for(i = 0; i < num_intersects; i++)
  {

    type = (intersect_data[i])->intersect_type;

    switch(type)
    {
      case UF_MODL_INTERSECT_POINT:
        printf("\nx,y,z coordinates are: (%f, %f, %f)\n",
               (intersect_data[i])->intersect.point.coords[0],
               (intersect_data[i])->intersect.point.coords[1],
               (intersect_data[i])->intersect.point.coords[2]);
        printf("Object 1 UV parameters are: (%f, %f)\n",
               (intersect_data[i])->intersect.point.object_1_u_parm,
               (intersect_data[i])->intersect.point.object_1_v_parm);
        printf("Object 2 UV parameters are: (%f, %f)\n",
               (intersect_data[i])->intersect.point.object_2_u_parm,
               (intersect_data[i])->intersect.point.object_2_v_parm);
        break;

      case UF_MODL_INTERSECT_COINCIDE:
        printf("\nCoincident curve tag is: %d\n",
               intersect_data[i]->intersect.coincide.identifier);
        printf("Object 1 UV parameters are: (%f, %f)\n",
               intersect_data[i]->intersect.coincide.object_1_first_parm,
               intersect_data[i]->intersect.coincide.object_1_second_parm);
        printf("Object 2 UV parameters are: (%f, %f)\n",
               intersect_data[i]->intersect.coincide.object_2_first_parm,
               intersect_data[i]->intersect.coincide.object_2_second_parm);
        break;

      case UF_MODL_INTERSECT_CURVE:
        printf("\nThe curve identifier is: %d\n",
               (intersect_data[i])->intersect.curve.identifier);
        break;

      default:
        printf("\nSomething went wrong, we shouldn't be here!");
        break;
    }

    /* Free each element of the array. */
      UF_free(intersect_data[i]);
  }
  if(num_intersects != 0)
  {
    /* Free the array. */
    UF_free(intersect_data);
  }

}
