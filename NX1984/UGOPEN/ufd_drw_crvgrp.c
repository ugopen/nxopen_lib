/*===========================================================================

        Copyright (c) 1997 Electronic Data Systems Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_group_of_curve.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_assem.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_drf_types.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_view.h>

#define N_ELEMENTS(array) (sizeof(array)/sizeof(array[0]))


void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    int                         ndx;
    int                         curve_group_type;
    int                         curve_group_subtype;
    int                         curve_types[]={UF_line_type,
                                               UF_circle_type,
                                               UF_conic_type,
                                               UF_spline_type};
    int                         num_curve_types = 
                                    N_ELEMENTS( curve_types );
    tag_t                       curve_tag = NULL_TAG;
    tag_t                       curve_group_tag = NULL_TAG;
    char                        error_message[133];


    ifail = UF_initialize();

    for( ndx=0; ndx<num_curve_types; ndx++ )
    {

        /* Cycle all curves in the part. 
           Print out each curve's group. */
        if( ifail == 0 )
            ifail = UF_OBJ_cycle_objs_in_part( 
                UF_ASSEM_ask_work_part(), 
                curve_types[ndx], &curve_tag );
        
        while( ( curve_tag != NULL_TAG ) && ( ifail == 0 ) )
        {
            ifail = UF_DRAW_ask_group_of_curve( curve_tag, 
                &curve_group_tag, &curve_group_type, 
                &curve_group_subtype );
            
            if( ifail == 0 )
            {
                printf( "Curve %d ", curve_tag );
                switch( curve_group_type )
                {
                    case 0:
                    {
                        printf( "is not a drawing edge. \n" );
                        break;
                    }
                    case UF_solid_section_type:
                    {
                        printf( "of group %d is ",
                                curve_group_tag );
                        printf( "a section edge.\n" );
                        break;
                    }
                    case UF_solid_silhouette_type:
                    {
                        printf( "of group %d is ",
                                curve_group_tag );
                        if( curve_group_subtype == 
                            UF_solid_silhouette_sl_subtype )
                            printf( "a silhouette.\n" );

                        else if( curve_group_subtype == 
                            UF_solid_silhouette_uvhatch_subtype )
                            printf( "a uv hatch curve.\n" );

                        else if( curve_group_subtype == 
                            UF_vicurve_subtype )
                            printf( "a vicurve.\n" );

                        else
                            printf( "a silhouette.\n" );

                        break;
                    }
                    case UF_curve_group_type:
                    {
                        printf( "of group %d is ",
                                curve_group_tag );
                        if( curve_group_subtype == 
                            UF_dropped_edge_group_subtype )
                        {
                           printf("an extracted drawing edge.\n");
                        }
                        else if( curve_group_subtype == 
                                 UF_simplified_group_subtype )
                        {
                           printf("a simplified drawing edge.\n");
                        }
                        break;
                    }
                    default:
                    {
                        printf( "is not a drawing edge.\n" );
                    }
                }
                
                ifail = UF_OBJ_cycle_objs_in_part( 
                    UF_ASSEM_ask_work_part(), 
                    UF_line_type, &curve_tag );
                
            }
        }
    }
        
    printf( "UF_DRAW_ask_group_of_curve sample " );
    if( ifail > 0 )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );
    
    ifail = UF_terminate();
    
}

