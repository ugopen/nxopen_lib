/*===================================================================

        Copyright (c) 1998,1999 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

===================================================================*/

/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRF_edit_dim_assoc.
 *
 *    It is placed directly in our UFUN documentation starting with
 *    the include statements.
 *
 *  
 * 
 ********************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_disp.h>
#include <uf_draw.h>
#include <uf_drf.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_vec.h>
#include <uf_view.h>

static int map_model2dwg
(
    double pos[3],
    tag_t  member_view
)
{
    int    part_units;
    int    ifail = 0;
    double dwg_ref[2] = {0.0};
    double factor = 1;
    double mdl_ref[3] = {0.0};
    double mx[9] = {0.0};
    double scale = 0.0;
    double tmp_pos[3];
    char   member_view_name[ UF_OBJ_NAME_BUFSIZE ];
    tag_t  dsp_prt_tag;
    tag_t  drawing_tag = NULL_TAG;
    UF_DRAW_info_t drawing_info;

    /* find the view reference point and scale */
    ifail = UF_OBJ_ask_name( member_view, member_view_name );
    if ( !ifail )
        ifail = uc6442(member_view_name, mdl_ref, &scale);
    
    /* find the drawing that the view exists in */
    if ( !ifail )
        ifail = UF_DRAW_ask_drawing_of_view( member_view, &drawing_tag );

    /* find the drawing reference point */
    if ( !ifail )
        ifail = UF_DRAW_ask_drawing_ref_pt( member_view, dwg_ref );

    /* find the view rotation matrix */
    if ( !ifail )
        ifail = uc6433(member_view_name, mx);

    if ( !ifail )
    {
        /* subtract the view reference point */
        UF_VEC3_sub(pos, mdl_ref, pos);

        /* map through the view rotation matrix */
        tmp_pos[0] = pos[0] * mx[0] + pos[1] * mx[1] + pos[2] * mx[2];
        tmp_pos[1] = pos[0] * mx[3] + pos[1] * mx[4] + pos[2] * mx[5];
        tmp_pos[2] = pos[0] * mx[6] + pos[1] * mx[7] + pos[2] * mx[8];

        /* scale by the view's drawing scale */
        UF_VEC3_scale(scale, tmp_pos, pos);
    }

    /* find drawing units (1 = inches, 2 = mm) */
    ifail = UF_DRAW_ask_drawing_info( drawing_tag, &drawing_info );        
    
    if ( !ifail )
    {
        if (drawing_info.units == 2) factor = 25.4;

        /* find part units (1 = mm, 2 = inches) */
        dsp_prt_tag = UF_PART_ask_display_part();
        UF_PART_ask_units(dsp_prt_tag, &part_units);   

        if (part_units == 1) factor = factor / 25.4;

        /* convert to drawing units */
        UF_VEC3_scale(factor, pos, pos);

        /* add the drawing reference point */
        UF_VEC2_add(pos, dwg_ref, pos);

        /* convert back to part units */
        UF_VEC3_scale(1.0/factor, pos, pos);

        /* set Z to 0.0 */
        pos[2] = 0.0;
    }
    return ( ifail );
}

static tag_t select_an_object
(
    int     selection_type,
    double  cursor_position[3],
    tag_t  *view_tag
)
{
    int                        return_code;
    char                      *text;
    tag_t                      object_tag;
    UF_UI_selection_options_t  opts;
    UF_UI_mask_t               mask[7];

    if (selection_type == 1)
    {
        opts.num_mask_triples             = 1;
        opts.mask_triples                 = &mask[0];

        opts.mask_triples->object_type    = UF_dimension_type;
        opts.mask_triples->object_subtype = UF_all_subtype;
        opts.mask_triples->solid_type     = 0;

        text = "Select a dimension at arrow to be reassociated";
    }
    else
    {
        opts.num_mask_triples               = 7;
        opts.mask_triples                   = mask;

        opts.mask_triples[0].object_type    = UF_line_type;
        opts.mask_triples[0].object_subtype = 0;
        opts.mask_triples[0].solid_type     = 0;

        opts.mask_triples[1].object_type    = UF_circle_type;
        opts.mask_triples[1].object_subtype = 0;
        opts.mask_triples[1].solid_type     = 0;

        opts.mask_triples[2].object_type    = UF_conic_type;
        opts.mask_triples[2].object_subtype = UF_all_subtype;
        opts.mask_triples[2].solid_type     = 0;

        opts.mask_triples[3].object_type    = UF_spline_type;
        opts.mask_triples[3].object_subtype = 0;
        opts.mask_triples[3].solid_type     = 0;

        opts.mask_triples[4].object_type    = UF_point_type;
        opts.mask_triples[4].object_subtype = 0;
        opts.mask_triples[4].solid_type     = 0;

        opts.mask_triples[5].object_type    = UF_solid_type;
        opts.mask_triples[5].object_subtype = UF_solid_edge_subtype;
        opts.mask_triples[5].solid_type     = UF_UI_SEL_FEATURE_ANY_EDGE;

        opts.mask_triples[6].object_type    = UF_solid_silhouette_type;
        opts.mask_triples[6].object_subtype = 0;
        opts.mask_triples[6].solid_type     = 0;

        text = "Select the edge to associate";
    }
    opts.scope = UF_UI_SEL_SCOPE_ANY_IN_ASSEMBLY;
    UF_UI_select_single(text, &opts,
                       &return_code, &object_tag, cursor_position, view_tag);
    if (return_code == 5)
        return object_tag;
    else
        return NULL_TAG;
}

/* ARGSUSED */
void ufusr(char *param, int *retcode, int param_len)
{
    int             ifail = 0;
    int             any_view  = 0;
    int             new_assoc_type = 1;
    double          old_leader_position[3];
    double          new_leader_position[3];
    char            error_message[MAX_LINE_BUFSIZE] = "";
    tag_t           view_tag;
    tag_t           dimension_tag;
    UF_DRF_object_t new_assoc_object;

    if (!UF_initialize())
    {
    /* set the cursor to select in any view */
        UF_UI_set_cursor_view(any_view);

        /* select the dimension to edit */
        dimension_tag = select_an_object(1, old_leader_position, &view_tag);
        if (dimension_tag)
        {
            /* initialize the new object structure */
            UF_DRF_init_object_structure(&new_assoc_object);

            /* select the new object to associate the dimension to */
            new_assoc_object.object_tag
        = select_an_object(2, new_leader_position, &view_tag);

            /* map the leader position to the drawing */
            ifail = map_model2dwg(new_leader_position, view_tag);

            if (!ifail && new_assoc_object.object_tag)
            {
                new_assoc_object.object_view_tag       = view_tag;
                new_assoc_object.object_assoc_type     = UF_DRF_end_point;
                new_assoc_object.object_assoc_modifier = UF_DRF_first_end_point;
                new_assoc_object.object2_tag           = NULL_TAG;

                /*  edit the dimension associativity */
                ifail = UF_DRF_edit_dim_assoc(dimension_tag,
                                              old_leader_position,
                                              new_leader_position,
                                              new_assoc_type,
                                              &new_assoc_object);

                /* unhighlight the new object */
                UF_DISP_set_highlight(new_assoc_object.object_tag, FALSE);
            }
            /* unhighlight the dimension */
            UF_DISP_set_highlight(dimension_tag, FALSE);
        }

        printf("UF_DRF_edit_dim_assoc sample ");
        if(ifail)
        {
            ifail = UF_get_fail_message( ifail, error_message );
            printf( "fails.\nError is: %s\n", error_message );
        }
        else
            printf( "is successful.\n" );

        UF_terminate();
    }
}
