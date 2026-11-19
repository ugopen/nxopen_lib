/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_FACET_create_model                                              *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example program creates a faceted model of a tetrahedron. It then   *
 *   examines the adjacency and convexity of the edges in the model. Finally  *
 *   it removes a facet from the tetrahedron and adds another three facets    *
 *   the apex of which is pushed up inside of the tetrahedron so that the     *
 *   there are three concave edges in the resulting model. It then inquires   *
 *   and prints the convexity of all of the edges in the model.               *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_facet.h>

static int example2(void);

/*--------------------------------------------------------------*/
/*ARGSUSED*/
extern void ufusr( char *param, int *retcod, int param_len )
 {
   UF_initialize();
   *retcod = example2();
   UF_terminate();
 }

/*--------------------------------------------------------------*/
static int example2( void )
 {
   int          ifail;
   tag_t        part_tag;
   int          i;
   tag_t        new_model;
   double       facet_vertices[30][3];
   double       facet_normals[30][3];
   int          adjacencies[30];
   int          facets[7];
   int          edge;
   int          adjacent_facets[3];
   int          facet_id;
   int          edge_in_adjacent_facet;
   int          num_facets_in_model;
   logical      model_convexity;

   /*
       First create a part in which we will initially create a
       block.
   */
   ifail = UF_PART_new( "uf_facet_exp2_test_part",
                        1 /* MM */,
                        &part_tag );    /* 1 = mm */
   if ( ifail != 0 )
     {
       printf( "**ERR: Failed to create new part ifail %d\n",
               ifail );
       return 1;
     }

   ifail = UF_ASSEM_set_work_part( part_tag );

   UF_FACET_create_model( part_tag, &new_model );

   /* The units are in mm.*/
   facet_vertices[0][0] = 0.0;
   facet_vertices[0][1] = 0.0;
   facet_vertices[0][2] = 0.0;
   
   facet_vertices[1][0] = 30.0;
   facet_vertices[1][1] = 50.0;
   facet_vertices[1][2] = 0.0;

   facet_vertices[2][0] = 60.0;
   facet_vertices[2][1] = 0.0;
   facet_vertices[2][2] = 0.0;

   adjacencies[0] = UF_FACET_NULL_FACET_ID;
   adjacencies[1] = UF_FACET_NULL_FACET_ID;
   adjacencies[2] = UF_FACET_NULL_FACET_ID;

   UF_FACET_add_facet_to_model( new_model,
                                3,
                                facet_vertices, 
                                NULL,
                                adjacencies,
                                facets+0 );
   /* The units are in mm.*/
   facet_vertices[0][0] = 0.0;
   facet_vertices[0][1] = 0.0;
   facet_vertices[0][2] = 0.0;
   
   facet_vertices[1][0] = 60.0;
   facet_vertices[1][1] = 0.0;
   facet_vertices[1][2] = 0.0;


   facet_vertices[2][0] = 30.0;
   facet_vertices[2][1] = 30.0;
   facet_vertices[2][2] = 50.0;

   adjacencies[0] = facets[0];

   UF_FACET_add_facet_to_model( new_model,
                                3,
                                facet_vertices, 
                                NULL,
                                adjacencies,
                                facets+1 );
   /* The units are in mm.*/
   facet_vertices[0][0] = 60.0;
   facet_vertices[0][1] = 0.0;
   facet_vertices[0][2] = 0.0;

   facet_vertices[1][0] = 30.0;
   facet_vertices[1][1] = 50.0;
   facet_vertices[1][2] = 0.0;

   facet_vertices[2][0] = 30.0;
   facet_vertices[2][1] = 30.0;
   facet_vertices[2][2] = 50.0;

   adjacencies[0] = facets[0];
   adjacencies[1] = UF_FACET_NULL_FACET_ID;
   adjacencies[2] = facets[1];

   UF_FACET_add_facet_to_model( new_model,
                                3,
                                facet_vertices, 
                                NULL,
                                adjacencies,
                                facets+2 );
   /* The units are in mm.*/
   facet_vertices[0][0] = 30.0;
   facet_vertices[0][1] = 50.0;
   facet_vertices[0][2] = 0.0;

   facet_vertices[1][0] = 0.0;
   facet_vertices[1][1] = 0.0;
   facet_vertices[1][2] = 0.0;
   
   facet_vertices[2][0] = 30.0;
   facet_vertices[2][1] = 30.0;
   facet_vertices[2][2] = 50.0;

   adjacencies[0] = facets[0];
   adjacencies[1] = facets[1];
   adjacencies[2] = facets[2];

   UF_FACET_add_facet_to_model( new_model,
                                3,
                                facet_vertices, 
                                NULL,
                                adjacencies,
                                facets+3 );

   facet_id = UF_FACET_NULL_FACET_ID;
   UF_FACET_cycle_facets( new_model, &facet_id );

   while ( facet_id != UF_FACET_NULL_FACET_ID )
     {
       for ( edge = 0; edge < 3; edge++ )
         {
           UF_FACET_ask_adjacent_facet( new_model, 
                                        facet_id,
                                        edge,
                                        &adjacent_facets[edge],
                                        &edge_in_adjacent_facet );
         }

       printf( "facet index: %d\n", facet_id );
       
       printf( "\tadjacent_facets: [%d,%d,%d]\n",
               adjacent_facets[0],
               adjacent_facets[1],
               adjacent_facets[2] );

       UF_FACET_cycle_facets( new_model, &facet_id );
     }

   UF_FACET_is_model_convex( new_model, &model_convexity );
   printf( "Model %s convex\n", 
           (model_convexity) ? "IS" : "IS NOT" );

   /*  
       Now create a facet topology containing some concave
       edges, to get this delete the first facet in the tetrahedron
       and replace it with three facets the shared vertex of which
       is towards the top vertex of the tetrahedron.
   */

   UF_FACET_del_facet_from_model( new_model, facets[0] );
   /* The units are in mm.*/
   facet_vertices[0][0] = 60.0;
   facet_vertices[0][1] = 0.0;
   facet_vertices[0][2] = 0.0;

   facet_vertices[1][0] = 0.0;
   facet_vertices[1][1] = 0.0;
   facet_vertices[1][2] = 0.0;

   facet_vertices[2][0] = 20.0;
   facet_vertices[2][1] = 20.0;
   facet_vertices[2][2] = 10.0;

   adjacencies[0] = facets[1];
   adjacencies[1] = UF_FACET_NULL_FACET_ID;
   adjacencies[2] = UF_FACET_NULL_FACET_ID;

   UF_FACET_add_facet_to_model( new_model,
                                3,
                                facet_vertices, 
                                NULL,
                                adjacencies,
                                facets+5 );
   /* The units are in mm.*/
   facet_vertices[0][0] = 30.0;
   facet_vertices[0][1] = 50.0;
   facet_vertices[0][2] = 0.0;

   facet_vertices[1][0] = 60.0;
   facet_vertices[1][1] = 0.0;
   facet_vertices[1][2] = 0.0;

   facet_vertices[2][0] = 20.0;
   facet_vertices[2][1] = 20.0;
   facet_vertices[2][2] = 10.0;

   adjacencies[0] = facets[2];
   adjacencies[1] = facets[5];
   adjacencies[2] = UF_FACET_NULL_FACET_ID;

   UF_FACET_add_facet_to_model( new_model,
                                3,
                                facet_vertices, 
                                NULL,
                                adjacencies,
                                facets+6 );
   /* The units are in mm.*/
   facet_vertices[0][0] = 0.0;
   facet_vertices[0][1] = 0.0;
   facet_vertices[0][2] = 0.0;
   
   facet_vertices[1][0] = 30.0;
   facet_vertices[1][1] = 50.0;
   facet_vertices[1][2] = 0.0;

   facet_vertices[2][0] = 20.0;
   facet_vertices[2][1] = 20.0;
   facet_vertices[2][2] = 10.0;

   adjacencies[0] = facets[3];
   adjacencies[1] = facets[6];
   adjacencies[2] = facets[5];

   UF_FACET_add_facet_to_model( new_model,
                                3,
                                facet_vertices, 
                                NULL,
                                adjacencies,
                                facets+7 );

   UF_FACET_model_edits_done( new_model );

   /*
       Now look at the edge convexity again.
   */
   printf( "Edge convexity for %u\n", new_model );
   facet_id = UF_FACET_NULL_FACET_ID;
   UF_FACET_cycle_facets( new_model, &facet_id );

   while ( facet_id != UF_FACET_NULL_FACET_ID )
     {
       int verts_in_facet;

       UF_FACET_ask_num_verts_in_facet( new_model,
                                        facet_id,
                                        &verts_in_facet );
       /*
           For each vertex print the vertex coordinates and the
           vertex normal.
       */

       UF_FACET_ask_vertices_of_facet( new_model, 
                                       facet_id,
                                       &verts_in_facet,
                                       facet_vertices );

       UF_FACET_ask_normals_of_facet( new_model, 
                                      facet_id,
                                      &verts_in_facet,
                                      facet_normals );

       for ( i=0 ; i < verts_in_facet ; i++ )
         {
           printf( "  Vertex %d: (%g, %g, %g)\n",
                   i, facet_vertices[i][0], 
                      facet_vertices[i][1], 
                      facet_vertices[i][2] );
           printf( "  Normal %d (%g, %g, %g)\n",
                   i, facet_normals[i][0],
                      facet_normals[i][1],
                      facet_normals[i][2] );
         }

       for ( i=0 ; i < verts_in_facet ; i++ )
         {
           int convexity;

           UF_FACET_ask_edge_convexity( new_model,
                                        facet_id,
                                        i,
                                        &convexity );

           printf( "  Facet %d: Edge %d: %s\n", facet_id, i,
                    (convexity == UF_FACET_IS_CONVEX)  ?
                            "IS CONVEX" :
                    (convexity == UF_FACET_IS_CONCAVE) ?
                            "IS CONCAVE" :
                            "CONVEXITY IS NOT DETERMINED"
                  );

           /*  
               Now check that the convexity of the corresponding
               edge in the adjacent facet is consistent.
           */
             {
               int adjacent_facet_id;
               int adj_convexity;

               UF_FACET_ask_adjacent_facet( new_model,
                                            facet_id,
                                            i,
                                            &adjacent_facet_id,
                                            &edge_in_adjacent_facet
                                           );
  
               UF_FACET_ask_edge_convexity( new_model,
                                            adjacent_facet_id,
                                            edge_in_adjacent_facet,
                                            &adj_convexity );

               if ( convexity != adj_convexity )
                 {
                   printf( "  **ERR: Edge convexity wrong\n" );
                 }
             }
         }

       UF_FACET_cycle_facets( new_model, &facet_id );
     }

   UF_FACET_ask_n_facets_in_model(new_model, &num_facets_in_model);
   printf( "There are %d facets in the final model\n",
           num_facets_in_model );

   UF_FACET_is_model_convex( new_model, &model_convexity );
   printf( "Model %s convex\n", 
           (model_convexity) ? "IS" : "IS NOT" );

   return 0;
 }

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
