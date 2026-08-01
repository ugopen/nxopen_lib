/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routines:        *
 *                                                                            *
 *       UF_FACET_ask_n_facets_in_model                                       *
 *       UF_FACET_ask_max_facet_verts                                         *
 *       UF_FACET_cycle_facets                                                *
 *       UF_FACET_ask_num_verts_in_facet                                      *
 *       UF_FACET_ask_plane_equation                                          *
 *       UF_FACET_is_facet_convex                                             *
 *       UF_FACET_ask_vertices_of_facet                                       *
 *       UF_FACET_ask_normals_of_facet                                        *
 *       UF_FACET_ask_vertex_convexity                                        *
 *       UF_FACET_cycle_facets                                                *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example program prints data about each of the facets and facet      *
 *   vertices in a faceted model. For each facet it prints the position,      *
 *   vertex normal, and vertex convexity for each vertex. The program assumes *
 *   that the function example used to illustrate UF_facet_create_model is    *
 *   available.
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

#include <uf.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_facet.h>

static int example1( tag_t *new_faceted_model );
static int example3( tag_t faceted_model );

/*--------------------------------------------------------------*/
/*ARGSUSED*/
extern void ufusr( char *param, int *retcod, int param_len )
 {
   tag_t faceted_model;

   UF_initialize();
   *retcod = example1( &faceted_model );
   if ( *retcod == 0 )
     {
       *retcod = example3( faceted_model );
     }
   UF_terminate();
 }

/*--------------------------------------------------------------*/
static int example3( tag_t model )
 {
   int          num_facets_in_model;
   int          max_vertices_in_facet;
   double     (* facet_vertices)[3];
   double     (* facet_normals)[3];
   double       plane_normal[3];
   double       d_coefficient;
   int          facet_id;
   int          facet_no = 0;
   int          i;
   int          vertex_array_size;

   UF_FACET_ask_n_facets_in_model( model, &num_facets_in_model );
   UF_FACET_ask_max_facet_verts( model, &max_vertices_in_facet );

   vertex_array_size = 3*max_vertices_in_facet*sizeof(double);
   facet_vertices = (double(*)[3])malloc(vertex_array_size);
   facet_normals  = (double(*)[3])malloc(vertex_array_size);

   printf( "Model contains %d facets\n", num_facets_in_model );
   printf( "Maxmium vertices in any facet is %d\n",
            max_vertices_in_facet );

   facet_id = UF_FACET_NULL_FACET_ID;
   UF_FACET_cycle_facets( model, &facet_id );

   while ( facet_id != UF_FACET_NULL_FACET_ID )
     {
       int      num_vertices_in_facet;
       int      verts_in_facet;
       logical  facet_convexity;

       UF_FACET_ask_num_verts_in_facet( model, facet_id,
                                        &num_vertices_in_facet );
                                        

       printf( "Facet %d has %d vertices\n", 
                facet_no++, num_vertices_in_facet );

       UF_FACET_ask_plane_equation( model,
                                    facet_id, 
                                    plane_normal,
                                    &d_coefficient
                                   );

       printf( " Facet normal (%g, %g, %g) d_coeff %g\n",
               plane_normal[0], plane_normal[1],
               plane_normal[2], d_coefficient );

       UF_FACET_is_facet_convex( model,
                                 facet_id,
                                 &facet_convexity );

       printf( " Facet %s convex\n", 
                (facet_convexity) ? "IS" : "IS NOT" );



       UF_FACET_ask_vertices_of_facet( model, 
                                       facet_id,
                                       &verts_in_facet,
                                       (double(*)[3])facet_vertices
                                     );

       UF_FACET_ask_normals_of_facet( model, 
                                      facet_id,
                                      &verts_in_facet,
                                      (double(*)[3])facet_normals
                                    );

       for ( i=0 ; i < num_vertices_in_facet ; i++ )
         {
           int vertex_convexity;

           printf( "  Vertex %d: (%g, %g, %g)\n",
                   i, facet_vertices[i][0], 
                      facet_vertices[i][1], 
                      facet_vertices[i][2] );
           printf( "    Normal (%g, %g, %g)\n",
                   facet_normals[i][0],
                   facet_normals[i][1],
                   facet_normals[i][2] );

           UF_FACET_ask_vertex_convexity( model,
                                          facet_id,
                                          i,
                                          &vertex_convexity );

           printf( "    Vertex convexity = %s\n",
                    (vertex_convexity == UF_FACET_IS_CONVEX)  ?
                            "IS CONVEX" :
                    (vertex_convexity == UF_FACET_IS_CONCAVE) ?
                            "IS CONCAVE" :
                            "CONVEXITY IS NOT DETERMINED"
                  );
         }

       UF_FACET_cycle_facets( model, &facet_id );
     }

   free( facet_vertices );
   free( facet_normals );
   return 0;
}

/*--------------------------------------------------------------*/
static int example1( tag_t * new_faceted_model )
 {
   int          ifail;
   tag_t        part_tag;
   double       corner_point[3];
   char       * edge_lengths[] = { "10", "30", "40" };
   tag_t        block_feature_tag;
   tag_t        block_tag;
   tag_t        faceted_model;
   logical      up_to_date = true;
   tag_t        blend_feature;
   uf_list_p_t  edge_list = NULL;
   tag_t        tag_of_solid;
   int          i;
   tag_t      * facet_models;
   int          n_facet_models;
   UF_FACET_parameters_t faceting_params;
   *new_faceted_model = NULL_TAG;

   /*
       First create a part in which we will initially create a
       block.
   */
   ifail = UF_PART_new( "uf_facet_exp1_test_part",
                        1 /* MM */,
                        &part_tag );    /* 1 = mm */
   if ( ifail != 0 )
     {
       printf( "**ERR: Failed to create new part ifail %d\n",
               ifail );
       return 1;
     }

   ifail = UF_ASSEM_set_work_part( part_tag );

   corner_point[0] = 0.0;
   corner_point[1] = 0.0;
   corner_point[2] = 0.0;

   UF_MODL_create_block1( UF_NULLSIGN,
                          corner_point,
                          edge_lengths,
                          &block_feature_tag );

   UF_MODL_ask_feat_body( block_feature_tag, &block_tag );

   UF_FACET_INIT_PARAMETERS(&faceting_params);
   UF_FACET_ask_default_parameters( &faceting_params) ;

   UF_FACET_facet_solid( block_tag,
                         &faceting_params,
                         &faceted_model );

   if ( faceted_model != NULL_TAG )
     {
       UF_FACET_ask_solid_of_model( faceted_model, &tag_of_solid );

       if ( block_tag != tag_of_solid )
         {
           printf( "**ERR: Failed find solid from facet model\n" );
           return 1;
         } 

       UF_FACET_ask_models_of_solid( block_tag,
                                     &n_facet_models,
                                     &facet_models );

       /*
          Just check that the association between the solid and 
          the new faceted model has been established.
       */
       for ( i=0 ; i < n_facet_models ; i++ )
         {
           if ( facet_models[i] == faceted_model )
             {
               printf( "Faceted model is attached to solid\n" );
             }
         }

       UF_free( facet_models );

       /*
           Now blend all of the edges of the block.
       */
       UF_MODL_ask_body_edges( block_tag, &edge_list );

       UF_MODL_create_blend( "2.0", edge_list, 
                             0, 0, 0, 0.0,
                             &blend_feature );

       UF_MODL_delete_list( &edge_list );

       UF_MODL_update();

       ifail = UF_FACET_is_model_up_to_date( faceted_model,
                                             &up_to_date );

       if ( up_to_date )
         {
           printf( "**ERR: Faceted model is up to date\n" );
           return 1;
         }

       ifail = UF_FACET_ask_model_parameters( faceted_model,
                                              &faceting_params );

       /*
          Set the number of sides for facets to four and use that
          when refaceting the solid.
       */
       faceting_params.max_facet_edges = 4;

       ifail = UF_FACET_update_model( faceted_model,
                                      &faceting_params );
       if ( ifail != 0 )
         {
           printf( "**ERR: Failed to refacet model\n" );
           return 1;
         }

       ifail = UF_FACET_is_model_up_to_date( faceted_model,
                                             &up_to_date );

       if (!up_to_date)
         {
           printf( "**ERR: Model is not up to date\n" );
           return 1;
         }
       /*
           Finally, disassociate the faceted model from
           the generating solid.
       */
       UF_FACET_disassoc_from_solid( faceted_model );

       *new_faceted_model = faceted_model;
     }
   else
     {
       return 1;
     }

   return 0;
}
