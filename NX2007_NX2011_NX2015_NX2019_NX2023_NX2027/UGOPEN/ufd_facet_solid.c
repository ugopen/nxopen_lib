/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_FACET_facet_solid                                               *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example program creates a simple block, facets it using the default *
 *   faceting parameters, and examines the facets produced. The program then  *
 *   adds blend to the block, checks that the faceted model is indeed out of  *
 *   date and regenerates the faceted model specifying that facets are        *
 *   allowed to have four rather than only three sides. Finally it            *
 *   disassociates the faceted model from the generating solid.               *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_facet.h>

static int example1( tag_t *new_faceted_model);

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

   UF_FACET_INIT_PARAMETERS( &faceting_params);
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

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
