/*=================================================================

                    Copyright (c) 1998 Unigraphics Solutions Inc. 
                             Unpublished - All rights reserved

===================================================================
File description:

    This file contains the UF_EVAL example program.

===================================================================

=================================================================*/

#include <stdio.h>

#include <uf_object_types.h>
#include <uf_curve.h>
#include <uf_eval.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_so.h>
#include <uf.h>

#define UF_CALL( X ) ( report ( __FILE__, __LINE__, #X, ( X ) ) )

/*---------------------------------------------------------------*/
static int report ( char *file, int line, char *call, int irc )
{
    if ( irc )
    {
        char message [ 132 + 1 ];

        printf ( "%s, line %d:  %s\n", file, line, call );

        UF_get_fail_message ( irc, message ) ?
            printf ( "    error %d\n", irc ) :
            printf ( "    error %d:  %s\n", irc, message );
    }

    return irc;
}

/*---------------------------------------------------------------*/
int ufusr_ask_unload ( void )
{
    return UF_UNLOAD_IMMEDIATELY;
}

/*---------------------------------------------------------------*/
/* ARGSUSED */
extern void ufusr ( char *param, int *retcod, int param_len )
{
    tag_t line;
    tag_t arc;
    tag_t edge;
    tag_t edges [ 3 ];

    UF_EVAL_p_t line_evaluator;
    UF_EVAL_p_t arc_evaluator;
    UF_EVAL_p_t edge_evaluator;

    UF_CALL ( UF_initialize ( ) );

    /*  
        Create new part "ufd_eval.prt".
        
        Close part if it already exists.
    */
    {
        tag_t part = UF_PART_ask_part_tag ( "ufd_eval.prt" );

        if ( part != NULL_TAG )
        {
            UF_CALL ( UF_PART_close ( part, 0, 1 ) );
        }

        UF_CALL ( UF_PART_new ( "ugd_eval.prt", 
                                UF_PART_ENGLISH, 
                                &part ) );
    }

    /* 
        Create block and get edges. 
    */
    {
        double  origin [ ] = { 0.0, 0.0, 0.0 };
        char   *sizes  [ ] = { "1", "1", "1" };

        tag_t block_feature;
            
        UF_CALL ( UF_MODL_create_block1 ( UF_NULLSIGN, 
                                          origin, 
                                          sizes, 
                                          &block_feature ) );

        {
            uf_list_p_t edge_list;

            UF_CALL ( UF_MODL_ask_feat_edges ( block_feature, 
                                               &edge_list ) );
            
            UF_CALL ( UF_MODL_ask_list_item ( edge_list, 
                                              1, 
                                              &edge ) );

            edges [ 0 ] = edge;
            edges [ 1 ] = edge;

            UF_CALL ( UF_MODL_ask_list_item ( edge_list, 
                                              0, 
                                              &edges [ 2 ] ) );

            UF_CALL ( UF_MODL_delete_list ( &edge_list ) );
        }
    }

    /*  
        Create smart line.
    */
    UF_CALL ( UF_SO_create_curve_extract 
              ( 
                  edge, 
                  UF_SO_update_after_modeling, 
                  edge,
                  UF_line_type, /* enforce line type */
                  0,            /* no subtype to enforce */
                  NULL_TAG,
                  &line 
              ) );
        
    /*  
        Create smart arc.
    */
    {
        int i;

        tag_t points [ 3 ];

        for ( i = 0; i < 3; i++ )
        {
            char *strings [  ] = { "center=1.0", 
                                   "start=0.0", 
                                   "end=1.0" };

            tag_t exps    [ 3 ];
            tag_t scalars [ 3 ];

            UF_CALL ( UF_MODL_create_exp_tag ( strings [ i ], 
                                               &exps [ i ] ) );

            UF_CALL ( UF_SO_create_scalar_exp 
                      ( 
                          exps [ i ],
                          UF_SO_update_after_modeling, 
                          exps [ i ], 
                          &scalars [ i ]
                    ) );

            UF_CALL ( UF_SO_create_point_on_curve 
                      (
                          edges [ i ],
                          UF_SO_update_after_modeling, 
                          edges [ i ],
                          scalars [ i ], 
                          &points [ i ]
                    ) );
        }

        UF_CALL ( UF_SO_create_arc_center_2_pnts 
                  ( 
                      points [ 0 ], 
                      UF_SO_update_after_modeling,
                      points, 
                      &arc 
                  ) );
    }
        
    /* 
       Smart objects are created as invisible objects by 
       default.  UF_SO_set_visibility_option ( ) can be 
       used to make them visible in the graphics window.
    */
    UF_CALL ( UF_SO_set_visibility_option ( line, 
                                            UF_SO_visible ) );
    UF_CALL ( UF_SO_set_visibility_option ( arc,  
                                            UF_SO_visible ) );

    /*  
        Get line/arc/edge evaluators.
    */
    UF_CALL ( UF_EVAL_initialize ( line, &line_evaluator ) );
    UF_CALL ( UF_EVAL_initialize ( arc,  &arc_evaluator ) );
    UF_CALL ( UF_EVAL_initialize ( edge, &edge_evaluator ) );

    /*  
        Get line/arc/edge data.
    */
    {
        UF_EVAL_line_t line_data;
        UF_EVAL_arc_t  arc_data;
        UF_EVAL_line_t edge_data;

        UF_CALL ( UF_EVAL_ask_line ( line_evaluator, 
                                     &line_data ) );
        UF_CALL ( UF_EVAL_ask_arc  ( arc_evaluator,  
                                     &arc_data ) );
        UF_CALL ( UF_EVAL_ask_line ( edge_evaluator,  
                                     &edge_data ) );
    }

    /*  
        Check line/arc/edge periodicity.
    */
    {
        logical is_periodic;
        
        UF_CALL ( UF_EVAL_is_periodic ( line_evaluator, 
                                        &is_periodic ) );
        UF_CALL ( UF_EVAL_is_periodic ( arc_evaluator,  
                                        &is_periodic ) );
        UF_CALL ( UF_EVAL_is_periodic ( edge_evaluator,  
                                        &is_periodic ) );
    }

    /*  
        Evaluate line/arc/edge.
    */
    {
        double limits [ 2 ];        
        double mid_t;
        double point [ 3 ];
        double derivative [ 3 ];
        double tangent [ 3 ];
        double normal [ 3 ];
        double binormal [ 3 ];

        UF_CALL ( UF_EVAL_ask_limits ( line_evaluator, limits ) );

        mid_t = ( limits [ 1 ] - limits [ 0 ] ) / 2.0;

        UF_CALL ( UF_EVAL_evaluate ( line_evaluator, 
                                     1, 
                                     mid_t, 
                                     point, 
                                     derivative ) );
                  
        UF_CALL ( UF_EVAL_evaluate_unit_vectors ( line_evaluator, 
                                                  mid_t, 
                                                  point, 
                                                  tangent, 
                                                  normal, 
                                                  binormal ) );

        UF_CALL ( UF_EVAL_ask_limits ( arc_evaluator, limits ) );

        mid_t = ( limits [ 1 ] - limits [ 0 ] ) / 2.0;
        
        UF_CALL ( UF_EVAL_evaluate ( arc_evaluator, 
                                     1, 
                                     mid_t, 
                                     point, 
                                     derivative ) );
        
        UF_CALL ( UF_EVAL_evaluate_unit_vectors ( arc_evaluator, 
                                                  mid_t, 
                                                  point, 
                                                  tangent, 
                                                  normal, 
                                                  binormal ) );

        UF_CALL ( UF_EVAL_ask_limits ( edge_evaluator, limits ) );

        mid_t = ( limits [ 1 ] - limits [ 0 ] ) / 2.0;

        UF_CALL ( UF_EVAL_evaluate ( edge_evaluator, 
                                     1, 
                                     mid_t, 
                                     point, 
                                     derivative ) );
                  
        UF_CALL ( UF_EVAL_evaluate_unit_vectors ( edge_evaluator, 
                                                  mid_t, 
                                                  point, 
                                                  tangent, 
                                                  normal, 
                                                  binormal ) );
    }

    /*  
        Check line/arc/edge equality of evaluators.
    */
    {
        logical is_equal;

        UF_EVAL_p_t line_evaluator_copy;

        UF_CALL ( UF_EVAL_copy ( line_evaluator,
                                 &line_evaluator_copy ) );

        UF_CALL ( UF_EVAL_is_equal ( line_evaluator,
                                     line_evaluator_copy,
                                     &is_equal ) );

        UF_CALL ( UF_EVAL_free ( line_evaluator_copy ) );

        UF_CALL ( UF_EVAL_is_equal ( line_evaluator, 
                                     arc_evaluator, 
                                     &is_equal ) );

        UF_CALL ( UF_EVAL_is_equal ( line_evaluator, 
                                     edge_evaluator, 
                                     &is_equal ) );
    }

    /*  
        Check line/arc/edge type.
    */
    {
        logical is_line;
        logical is_arc;

        UF_CALL ( UF_EVAL_is_line ( line_evaluator, &is_line ) );
        UF_CALL ( UF_EVAL_is_arc  ( line_evaluator, &is_arc ) );
        UF_CALL ( UF_EVAL_is_arc  ( arc_evaluator,  &is_arc ) );
        UF_CALL ( UF_EVAL_is_line ( arc_evaluator,  &is_line ) );
        UF_CALL ( UF_EVAL_is_arc  ( edge_evaluator, &is_arc ) );
        UF_CALL ( UF_EVAL_is_line ( edge_evaluator, &is_line ) );
    }

    UF_CALL ( UF_EVAL_free ( line_evaluator ) );
    UF_CALL ( UF_EVAL_free ( arc_evaluator ) );
    UF_CALL ( UF_EVAL_free ( edge_evaluator ) );

    UF_CALL ( UF_terminate ( ) );
}
