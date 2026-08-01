/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_CURVE_ask_spline_thru_pts                                       *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part with splines. The example    *
 *   code uses the select by class function to allow a user to select         *
 *   multiple splines. The splines are then queried for spline thru points    *
 *   data and a report is printed to the information window.                  *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_object_types.h>
#include <uf_disp.h>
#include <uf_curve.h>

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
  char *message = "Select Spline";
  char buffer[ UF_UI_MAX_STRING_BUFSIZE ];
  UF_UI_selection_options_t opts;
  UF_UI_mask_t mask = {UF_spline_type, 0, 0};
  int response, count;
  tag_p_t objects;
  int i,j;
  int off = 0;
  int slope;
  int curve;

  /* Ask spline parameters. */
  int degree;
  int periodicity;
  int num_points;
  double *parameters;
  UF_CURVE_pt_slope_crvatr_t *point_data;
    
  opts.other_options = 0;
  opts.reserved = NULL;
  opts.num_mask_triples = 1;
  /* Set selection scope to be work part & occurrence. */
  opts.scope = UF_UI_SEL_SCOPE_WORK_PART_AND_OCC;
  opts.mask_triples = &mask;


 /* if no error, print information about selected spline objects. */
  if(!UF_CALL(UF_UI_select_by_class( message,&opts,&response,
                                     &count,&objects )))
  {
    /* Opens the information window for a report on spline data. */
    UF_CALL(UF_UI_open_listing_window());

    sprintf(buffer,"response= %d, object count= %d\n",response,count);
    /* Fall through only if objects selected. */
    if (objects != NULL)
    {
      /* For each spline in the array of objects, get the spline
         data and print the data to the information window.
      */
      for (j=0; j < count; j++)
      {
        /* Unhighlight selected objects. */
        UF_DISP_set_highlight(objects[j],off);

        /* Get the spline data. */
        UF_CALL(UF_CURVE_ask_spline_thru_pts(objects[j],
                                             &degree,
                                             &periodicity,
                                             &num_points,
                                             &point_data,
                                             &parameters));

        /* Print a header that identifies the spline number. */
        sprintf(buffer, "\n\n------Data for Spline %d ------\n",j+1);
        UF_UI_write_listing_window(buffer);

        /*Print the degree and periodicity. A value of 0 indicates
          a nonperiodic spline. A value of 1 indicates a periodic
          spline.
        */
        sprintf(buffer,"\nDegree is: %d\n", degree);
        UF_UI_write_listing_window(buffer);
        sprintf(buffer,"Periodicity is : %d\n",periodicity);
        UF_UI_write_listing_window(buffer);

        /* Print the parametric values of the spline. */
        for(i = 0; i < num_points; i++)
        {
          sprintf(buffer,"parameters[%d]: %f\n",i,parameters[i]);
          UF_UI_write_listing_window(buffer);
        }

        /* Print the spline points. */
        for(i = 0; i < num_points; i++)
        {

          /* Print out spline data. */
          sprintf(buffer,"\nPoints (%d):\n", i+1);
          UF_UI_write_listing_window(buffer);
          sprintf(buffer,"point_data[%d]->point[0]: %f\n",
                  i,point_data[i].point[0]);
          UF_UI_write_listing_window(buffer);
          sprintf(buffer,"point_data[%d]->point[1]: %f\n",
                  i,point_data[i].point[1]);
          UF_UI_write_listing_window(buffer);
          sprintf(buffer,"point_data[%d]->point[2]: %f\n",
                  i,point_data[i].point[2]);
          UF_UI_write_listing_window(buffer);

          /* Print out the slope type. */
          slope = point_data[i].slope_type;
          switch(slope)
          {
            case UF_CURVE_SLOPE_NONE:
              sprintf(buffer, "slope type: UF_CURVE_SLOPE_NONE\n");
              UF_UI_write_listing_window(buffer);
              break;
            case UF_CURVE_SLOPE_AUTO:
              sprintf(buffer, "slope type: UF_CURVE_SLOPE_AUTO\n");
              UF_UI_write_listing_window(buffer);
              break;
            case UF_CURVE_SLOPE_VEC:
              sprintf(buffer, "slope type: UF_CURVE_SLOPE_VEC\n");
              UF_UI_write_listing_window(buffer);
              break;
            case UF_CURVE_SLOPE_DIR:
              sprintf(buffer, "slope type: UF_CURVE_SLOPE_DIR\n");
              UF_UI_write_listing_window(buffer);
              break;
            default:
              sprintf(buffer,"Unknown slope type: %d\n",slope);
              UF_UI_write_listing_window(buffer);
              break;
          }

          /* Print the slope vector coordinates. */
          sprintf(buffer,"point_data[%d]->slope[0]: %f\n",
                  i,point_data[i].slope[0]);
          UF_UI_write_listing_window(buffer);
          sprintf(buffer,"point_data[%d]->slope[1]: %f\n",
                  i,point_data[i].slope[1]);
          UF_UI_write_listing_window(buffer);
          sprintf(buffer,"point_data[%d]->slope[2]: %f\n",
                  i,point_data[i].slope[2]);
          UF_UI_write_listing_window(buffer);

          /* Print out curvature type.*/
          curve = point_data[i].crvatr_type;
          switch(curve)
          {
            case UF_CURVE_CRVATR_NONE:
              sprintf(buffer, "curvature type: UF_CURVE_CRVATR_NONE\n");
              UF_UI_write_listing_window(buffer);
              break;
            case UF_CURVE_CRVATR_AUTO_DIR:
              sprintf(buffer, "curvature type: UF_CURVE_CRVATR_AUTO_DIR\n");
              UF_UI_write_listing_window(buffer);
              break;
            case UF_CURVE_CRVATR_VEC:
              sprintf(buffer, "curvature type: UF_CURVE_CRVATR_VEC\n");
              UF_UI_write_listing_window(buffer);
              break;
            default:
              sprintf(buffer,"Unknown curvature type: %d\n",curve);
              UF_UI_write_listing_window(buffer);
              break;
          }

          /* Print the curvature vector coordinates. */
          sprintf(buffer,"point_data[%d]->crvatr[0]: %f\n",
                  i,point_data[i].crvatr[0]);
          UF_UI_write_listing_window(buffer);
          sprintf(buffer,"point_data[%d]->crvatr[1]: %f\n",
                  i,point_data[i].crvatr[1]);
          UF_UI_write_listing_window(buffer);
          sprintf(buffer,"point_data[%d]->crvatr[2]: %f\n",
                  i,point_data[i].crvatr[2]);
          UF_UI_write_listing_window(buffer);
        } 
      }
    }
  }
  /* Deallocate memory for the array of spline object tags. */
  UF_free(objects);
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
