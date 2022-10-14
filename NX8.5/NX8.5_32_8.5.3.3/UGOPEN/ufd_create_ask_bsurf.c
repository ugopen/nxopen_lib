

/* ========================================================================== * 
 *                                                                            * 
 *          Copyright (c) 1995-2000 Unigraphics Solutions Inc.                *
 *                     Unpublished - All rights reserved                      * 
 *                                                                            * 
 * ========================================================================== */

/* ========================================================================== * 
 * 
 *  Description: This file contains the following external functions that 
 *               support b-surface functions:
 *
 *      UF_MODL_ask_bsurf
 *      UF_MODL_create_bsurf
 *      UF_MODL_edit_bsurf
 *
 * ========================================================================== */


#include <stdio.h>
#include <stdlib.h>
#include <uf.h>
#include <uf_part.h>
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

  char    *prtnam = "create_bsurf"; 

  /* Points for B-surface  */
  double points[16][3] = { 3.5, 2.5, 0.0,
			   4.0, 2.6, 0.2,
			   4.5, 2.6, 0.2,
			   5.0, 2.5, 0.0,
			   3.3, 3.0, 0.2,
			   4.1, 3.2, 0.3, 
			   4.5, 3.2, 0.3,
			   5.0, 3.0, 0.2,
			   3.0, 3.5, 0.2,
			   3.8, 3.6, 0.3,
			   4.5, 3.6, 0.3,
			   5.0, 3.5, 0.2,
			   2.6, 4.0, 0.0,
			   3.3, 4.0, 0.2,
			   4.5, 4.0, 0.2,
			   5.0, 4.0, 0.0 };	

  int create_mode = 1;
  int u_closed_status = 0;
  int v_closed_status = 0;
  int u_degree = 3;
  int v_degree = 3;
  int num_rows = 4;
  int pts_per_row[4] = {4, 4, 4, 4};
    
  int ii, jj, kk, indx;
        
  tag_t   part_tag;
  tag_t   bsurf_obj_id = NULL_TAG;

  UF_MODL_bsurf_row_info_t *pts_info_per_row; /* pts info for each row */
  UF_MODL_bsurface_t   bsurf;


  /* Open a new part */
  UF_CALL( UF_PART_new(prtnam, METRIC, &part_tag) );

  pts_info_per_row = ( UF_MODL_bsurf_row_info_t *)malloc( num_rows *
                       sizeof(UF_MODL_bsurf_row_info_t) );
   
  /* allocate and load point and other information for each row of points */
  indx = 0;
  for (ii=0; ii<num_rows; ii++)
  {
    pts_info_per_row[ii].num_points = pts_per_row[ii];  /* can vary */
    pts_info_per_row[ii].points = (double *)malloc( pts_per_row[ii] * 3 *
                                   sizeof(double) );
      
    pts_info_per_row[ii].weight = (double *)malloc( pts_per_row[ii] * 
                                   sizeof(double) );
               
    /* load up point and weight info */
    for (jj=0, kk = 0; kk<pts_per_row[ii]; kk++, jj+=3, indx++)
    {
      pts_info_per_row[ii].points[jj] = points[indx][0];
      pts_info_per_row[ii].points[jj+1] = points[indx][1];
      pts_info_per_row[ii].points[jj+2] = points[indx][2];
      pts_info_per_row[ii].weight[kk] = 1.0;
    
    }
  }
  
  /* create B-surface */
  UF_CALL(UF_MODL_create_bsurf_thru_pts( create_mode, u_closed_status, 
                                         v_closed_status, u_degree, 
                                         v_degree, num_rows, pts_info_per_row,
	                                 &bsurf_obj_id));
	           
  if ( bsurf_obj_id == NULL_TAG )
    printf("*** ERROR CREATING B-SURFACE ***\n");

  /* free allocated memory */
  for (ii=0; ii<num_rows; ii++)
  {
    free(pts_info_per_row[ii].points);
    free(pts_info_per_row[ii].weight);
  }
  
  free(pts_info_per_row);
    
    
  /* ask the B-surface information */
  UF_CALL(UF_MODL_ask_bsurf( bsurf_obj_id, &bsurf ));
  
  /* validate the surface */
  if ( (bsurf.order_u != u_degree+1) || (bsurf.order_v != v_degree+1) )
    printf("*** ERROR ASKING B-SURFACE ***\n");
  
  UF_CALL(UF_MODL_free_bsurf_data(&bsurf));


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



