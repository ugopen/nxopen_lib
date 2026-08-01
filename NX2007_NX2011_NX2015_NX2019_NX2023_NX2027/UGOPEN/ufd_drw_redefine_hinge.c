/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_redefine_sxline_hinge.
 *    It is placed directly in our UFUN documentation starting with
 *    the include statements.
 *
 
 *
 ****************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_assem.h>
#include <uf_draw.h>
#include <uf_defs.h>
#include <uf_drf.h>
#include <uf_drf_types.h>
#include <uf_obj.h>
#include <uf_object_types.h>

void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    tag_t                       sxline_tag = NULL_TAG;
    tag_t                       edge1_tag = NULL_TAG;
    tag_t                       arc1_tag = NULL_TAG;
    tag_t                       arc2_tag = NULL_TAG;
    char*                       edge1_name = "edge1";
    char*                       arc1_name = "arc1";
    char*                       arc2_name = "arc2";
    char                        error_message[133];
    UF_DRF_line_object_t        hinge_line;


    ifail = UF_initialize();
    if( !ifail )
    {
        /* Loop through all the part entities counting 
           the number of section lines
           and of those how many are invalid. */
        ifail = UF_OBJ_cycle_objs_in_part(
            UF_ASSEM_ask_work_part(),
            UF_section_line_type, &sxline_tag);
    }
    if( !ifail )
    {
        UF_DRF_init_line_object( &hinge_line );
        hinge_line.line_assoc_type = UF_DRF_DWG_LINE;

        hinge_line.object1.assoc_dwg_pos[0] = 0.0;
        hinge_line.object1.assoc_dwg_pos[1] = 0.0;
        hinge_line.point_object2.assoc_dwg_pos[0] = 1.0;
        hinge_line.point_object2.assoc_dwg_pos[1] = 1.0;

        /* Redefine the hinge line, defined by two points
           on the drawing. */
        ifail = UF_DRAW_redefine_sxline_hinge( 
                    sxline_tag, &hinge_line, TRUE );
    }
    if( !ifail )
    {
        /* Redefine the hinge line again.  This time 
           associate it to a model edge. */
        UF_OBJ_cycle_by_name ( edge1_name, &edge1_tag );

        UF_DRF_init_line_object( &hinge_line );
        hinge_line.line_assoc_type = UF_DRF_EXISTING_LINE;
        hinge_line.object1.object_tag = edge1_tag;

        ifail = UF_DRAW_redefine_sxline_hinge( 
                    sxline_tag, &hinge_line, TRUE );
    }
    if( !ifail )
    {
        /* Redefine the hinge line again.  This time 
           associate using the two points method
           by designating two arc centers. */
        UF_OBJ_cycle_by_name( arc1_name, &arc1_tag );
        UF_OBJ_cycle_by_name( arc2_name, &arc2_tag );

        UF_DRF_init_line_object( &hinge_line );

        hinge_line.line_assoc_type = UF_DRF_TWO_POINTS;

        hinge_line.object1.object_tag = arc1_tag;
        hinge_line.object1.object_assoc_type = UF_DRF_arc_center;

        hinge_line.point_object2.object_tag = arc2_tag;
        hinge_line.point_object2.object_assoc_type = UF_DRF_arc_center;

        ifail = UF_DRAW_redefine_sxline_hinge( 
                    sxline_tag, &hinge_line, TRUE );
    }
    printf( "UF_DRAW_redefine_sxline_hinge sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );
    ifail = UF_terminate();

}

