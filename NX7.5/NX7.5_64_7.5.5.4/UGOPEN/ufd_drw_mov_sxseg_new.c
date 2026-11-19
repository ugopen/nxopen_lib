/*===========================================================================

        Copyright (c) 1995,1996,1997 Electronic Data Systems Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_move_sxline_sxseg.  It is placed  
 *    directly in our UFUN documentation starting with the 
 *    include statements.
 *
 
 *
 ****************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_drf_types.h>
#include <uf_obj.h>

void ufusr(char *param, int *retcod, int param_len)
{


    int                         ifail = 0;
    int                         num_sxviews;
    int                         num_sxsegs;
    tag_t                       sxline1_tag;
    tag_t                       pview_tag;
    tag_t                       curve_tag;
    tag_t                       new_sxseg_tag;
    tag_t *                     sxview_tags = NULL;
    tag_t *                     sxseg_tags = NULL;
    double                      step_dir[3];
    double                      arrow_dir[3];
    char                        error_message[133];
    char *                      sxline1 = "unfolded_sxline1";
    UF_DRAW_sxline_status_t     sxline_status;
    UF_DRF_object_p_t           object;
    UF_DRAW_sxseg_info_t        sxseg_info;
    UF_DRAW_sxline_sxsegs_t     sxseg_data;


    ifail = UF_initialize();

    /* Find the tag of a section line from its name. */
    if( ifail == 0 )
        ifail = UF_OBJ_cycle_by_name( sxline1, &sxline1_tag );

    if( ifail == 0 )
    {
        /* Retrieve stepped section line information. */
        ifail = UF_DRAW_ask_unfolded_sxline( sxline1_tag, 
            step_dir, arrow_dir, &pview_tag, &num_sxviews,
            &sxview_tags, &num_sxsegs, &sxseg_tags, 
            &sxline_status );
    }

    /* Retrieve the last step sxseg's information. */
    if( ifail == 0 )
        ifail = UF_DRAW_ask_sxline_sxseg( sxseg_tags[num_sxsegs-2],
            &sxseg_info, &curve_tag, &object );

    if( ifail == 0 )
    {
        /* Move the newly created segment. */
        object->object_tag = NULL_TAG;
        object->object_view_tag = NULL_TAG;
        object->object_assoc_type = UF_DRF_dwg_pos;
        object->object_assoc_modifier = UF_DRF_assoc_type_none;
        object->assoc_dwg_pos[0] = object->assoc_dwg_pos[0] + .05;
        object->assoc_dwg_pos[1] = object->assoc_dwg_pos[1] + .05;

        sxseg_data.sxseg_object = object;
        sxseg_data.sxseg_angle = sxseg_info.sxseg_angle;
        sxseg_data.sxseg_type = sxseg_info.sxseg_type;
        ifail = UF_DRAW_move_sxseg( sxseg_tags[num_sxsegs-2], &sxseg_data );
    }

    if( ifail == 0 )
    {
        /* Add a new segment at a slightly moved location and new angle. */
        sxseg_data.sxseg_angle += 90.0;
        if( sxseg_data.sxseg_angle > 180.0 )
            sxseg_data.sxseg_angle -= 360.0;
        if( sxseg_data.sxseg_angle < -180.0 )
            sxseg_data.sxseg_angle += 360.0;
    
        sxseg_data.sxseg_object->assoc_dwg_pos[0] = 
            object->assoc_dwg_pos[0] + .05;
        sxseg_data.sxseg_object->assoc_dwg_pos[1] = 
            object->assoc_dwg_pos[1] + .05;

        UF_DRAW_add_sxseg( sxline1_tag, &sxseg_data, &new_sxseg_tag ); 
    }

    UF_free( object );
    UF_free( sxview_tags );
    UF_free( sxseg_tags );

    printf( "UF_DRAW_move_sxseg sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();

}
