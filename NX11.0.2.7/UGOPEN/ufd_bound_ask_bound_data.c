/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_BOUND_ask_boundary_data, UF_BOUND_create_boundary               *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a "blank.prt" to retrieve. The code       *
 *   creates a square boundary and gets the data in the created boundary.     *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <uf_defs.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_bound.h>
#include <uf_curve.h>
#include <string.h>
#include <stdio.h>

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

const char            *prtnam = "blank";         /* Part Name */
tag_t                 part_tag;            /* part tag of new
                                              created part */
UF_PART_load_status_t error_status;
int                   i, num_members, open_closed_flag;
UF_BOUND_object_t     object_list[4];
tag_t                 bound_tag, view_tag, line_tags[4];
UF_BOUND_tolerance_t  tolerance;
UF_CURVE_line_t       line_coords;
UF_BOUND_all_data_t   boundary_data;
    

/* *** RETRIEVE A NEW BLANK PART */

    /* open a new test part */
    UF_CALL(UF_PART_open((char *)prtnam,&part_tag,&error_status));

    /* create lines which will be used to create boundary */
    line_coords.start_point[0] = -2.0;
    line_coords.start_point[1] = -2.0;
    line_coords.start_point[2] =  0.0;
    line_coords.end_point[0]   =  2.0;
    line_coords.end_point[1]   = -2.0;
    line_coords.end_point[2]   =  0.0;
    UF_CALL(UF_CURVE_create_line(&line_coords,&line_tags[0]));
    
    line_coords.start_point[0] =  2.0;
    line_coords.start_point[1] = -2.0;
    line_coords.start_point[2] =  0.0;
    line_coords.end_point[0]   =  2.0;
    line_coords.end_point[1]   =  2.0;
    line_coords.end_point[2]   =  0.0;
    UF_CALL(UF_CURVE_create_line(&line_coords,&line_tags[1]));

    line_coords.start_point[0] =  2.0;
    line_coords.start_point[1] =  2.0;
    line_coords.start_point[2] =  0.0;
    line_coords.end_point[0]   = -2.0;
    line_coords.end_point[1]   =  2.0;
    line_coords.end_point[2]   =  0.0;
    UF_CALL(UF_CURVE_create_line(&line_coords,&line_tags[2]));

    line_coords.start_point[0] = -2.0;
    line_coords.start_point[1] =  2.0;
    line_coords.start_point[2] =  0.0;
    line_coords.end_point[0]   = -2.0;
    line_coords.end_point[1]   = -2.0;
    line_coords.end_point[2]   =  0.0;
    UF_CALL(UF_CURVE_create_line(&line_coords,&line_tags[3]));
                         
    for ( i=0; i<4; i++)
    {
        object_list[i].on_tangent_to_flag = UF_BOUND_TANGENT_TO;
        object_list[i].object_tag = line_tags[i];
    }


    /* create a boundary */
    open_closed_flag = UF_BOUND_CLOSED;
    view_tag = NULL_TAG;
    tolerance.tol_specified =  UF_BOUND_NOT_SPECIFIED;
    num_members = 4;
    UF_CALL(UF_BOUND_create_boundary(open_closed_flag, view_tag, tolerance,
                                     num_members, object_list, &bound_tag));

   /* get boundary data */
    UF_CALL(UF_BOUND_ask_boundary_data(bound_tag, &boundary_data));

    /* ***********************************************

        The boundary data can be used here 

     * *********************************************** */
        
    /* free memory */
        UF_free(boundary_data.members_data); 
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
