/*===========================================================================

 	Copyright (c) 1998 Unigraphics Solutions Corporation
		     Unpublished - All rights reserved

=============================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_CAM_PREPRO_mark_model_as_cam                                    *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example program creates a sphere then it facets using the default   *
 *   faceting parameters that are modified for validity for CAM processor use,*
 *   and examines the facets produced. The facets are then marked for use by  *
 *   the CAM processors.                                                      *
 *                                                                            *
 
 *                                                                            *
 ******************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_cam_prepro.h>
#include <uf_facet.h>



static int example1( tag_t * faceted_model );


/*ARGSUSED*/
extern void ufusr( char *param, int *retcod, int param_len )
 {
   tag_t faceted_model;

   UF_initialize();
   *retcod = example1(&faceted_model);
   UF_terminate();
 }



/*--------------------------------------------------------------*/
static int example1( tag_t * new_faceted_model )
 {
   int          ifail;
   tag_t        part_tag;
   double       corner_point[3];
   char         diam[] = { "10"};
   tag_t        block_feature_tag;
   tag_t        block_tag;
   tag_t        faceted_model;
   UF_FACET_parameters_t faceting_params;
   double       tolerance;

               
   *new_faceted_model = NULL_TAG;

   /*
       First create a part in which we will initially create a
       sphere.
   */
   ifail = UF_PART_new( "uf_cam_p_exp2_test_part_o",
                        1 /* MM */,
                        &part_tag );    /* 1 = mm */
   if ( ifail != 0 )
     {
       printf( "**ERR: Failed to create new part ifail %d\n",
               ifail );
       return 1;
     }

   /* Set the work part */

   ifail = UF_ASSEM_set_work_part( part_tag );
   

   /* 
       Create a Sphere                 
   */
   corner_point[0] = 0.0;
   corner_point[1] = 0.0;
   corner_point[2] = 0.0;

   UF_MODL_create_sphere1( UF_NULLSIGN,
                          corner_point,
                          diam,
                          &block_feature_tag );

   UF_MODL_ask_feat_body( block_feature_tag, &block_tag );

   /* 
       Initialize the parameters for the faceting using CAM defaults 
   */
   UF_FACET_INIT_PARAMETERS(&faceting_params);
   UF_FACET_ask_default_parameters( (UF_FACET_parameters_p_t) &faceting_params) ;

   tolerance = faceting_params.surface_dist_tolerance;

   tolerance = 0.01;


   faceting_params.max_facet_edges             = 3;
   faceting_params.specify_surface_tolerance   = TRUE;
   faceting_params.surface_dist_tolerance      = tolerance;
   faceting_params.surface_angular_tolerance   = 0.4;
   faceting_params.specify_curve_tolerance     = true; 
   faceting_params.curve_dist_tolerance        = tolerance;
   faceting_params.curve_angular_tolerance     = 0.4; 
   faceting_params.curve_max_length            =  1000;
   faceting_params.specify_convex_facets       = TRUE;
   faceting_params.number_storage_type         = UF_FACET_TYPE_DOUBLE; 
   faceting_params.specify_parameters          = TRUE; 
   faceting_params.specify_view_direction      = TRUE;
   faceting_params.silh_chord_tolerance        = tolerance / 4.0; 

   faceting_params.silh_view_direction[0]  = 0;
   faceting_params.silh_view_direction[1]  = 0;
   faceting_params.silh_view_direction[2]  = 1.0;


   /* 
       Facet the solid body
   */
   UF_FACET_facet_solid( block_tag,
                         (UF_FACET_parameters_p_t) &faceting_params,
                         &faceted_model );

   /* 
       Mark the facets as CAM
   */
   if ( faceted_model != NULL_TAG )
     {
       ifail =  UF_CAM_PREPRO_mark_model_as_cam(faceted_model);
       if (ifail != 0)
          {
          printf( "**ERR: Failed to mark the facet model for cam  %d\n",
               ifail );
          return 1;
          }

       *new_faceted_model = faceted_model;
     }
   else
     {
       printf( "**ERR: Failed to create the facet model for the sphere  \n");
       return 1;
     }

   return 0;
}

