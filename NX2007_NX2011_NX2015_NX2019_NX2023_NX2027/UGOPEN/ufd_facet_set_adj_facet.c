/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_FACET_set_adjacent_facet                                        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example creates a faceted model and two facets which have a common  *
 *   edge.  It then uses the vertices from the shared edge in one facet to    *
 *   find the edge_id of the corresponding edge in the other facet. Finally   *
 *   it joins the two facets along the shared edge.                           *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_facet.h>

static void example4( void );

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
   example4();
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
static void example4( void )
 {
   
   tag_t        part_tag;
   tag_t        new_model;
   double       facet_vertices[30][3];
   int          adjacencies[30];
   int          facets[7];
   int          sense;
   int          shared_edge_id;

   /*
       First create a part in which we will initially create a
       block.
   */
   UF_CALL(UF_PART_new( "uf_facet_exp4_test_part",
                        1 /* MM */,
                        &part_tag ));    /* 1 = mm */

   UF_CALL(UF_ASSEM_set_work_part( part_tag ));

   UF_CALL(UF_FACET_create_model( part_tag, &new_model ));

   facet_vertices[0][0] = 0.0;
   facet_vertices[0][1] = 0.0;
   facet_vertices[0][2] = 0.0;
   
   facet_vertices[1][0] = 0.03;
   facet_vertices[1][1] = 0.05;
   facet_vertices[1][2] = 0.0;
   facet_vertices[2][0] = 0.060;
   facet_vertices[2][1] = 0.0;
   facet_vertices[2][2] = 0.0;

   adjacencies[0] = UF_FACET_NULL_FACET_ID;
   adjacencies[1] = UF_FACET_NULL_FACET_ID;
   adjacencies[2] = UF_FACET_NULL_FACET_ID;

   UF_CALL(UF_FACET_add_facet_to_model( new_model,
                                3,
                                facet_vertices, 
                                NULL,
                                adjacencies,
                                facets+0 ));

   facet_vertices[0][0] = 0.0;
   facet_vertices[0][1] = 0.0;
   facet_vertices[0][2] = 0.0;
   
   facet_vertices[1][0] = 0.060;
   facet_vertices[1][1] = 0.0;
   facet_vertices[1][2] = 0.0;
   
   facet_vertices[2][0] = 0.03;
   facet_vertices[2][1] = 0.03;
   facet_vertices[2][2] = 0.05;

   UF_CALL(UF_FACET_add_facet_to_model( new_model,
                                3,
                                facet_vertices, 
                                NULL,
                                adjacencies,
                                facets+1 ));

   /*
      Check that an edge exists in both facets.
   */
   UF_CALL(UF_FACET_find_edge_in_facet( new_model,
                                facets[0],
                                &(facet_vertices[0][0]),
                                &(facet_vertices[1][0]),
                                &sense, 
                                &shared_edge_id
                              ));

   printf( "Shared edge in first facet is %d\n",
           shared_edge_id );

   /*
      Stitch the two facets together along the shared edge.
   */
   UF_CALL(UF_FACET_set_adjacent_facet( new_model,
                                facets[0],
                                shared_edge_id,
                                facets[1] ));

 }
