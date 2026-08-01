/*=============================================================================

             Copyright (c) 2000 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

===============================================================================
File description:

    This is a small sample program that demonstrates the invocation
    of UF_DRAW_create_breakout along with UF_DRAW_ask_breakout_data,
    UF_DRAW_set_breakout_data, and UF_DRAW_remove_breakout.  It is
    placed directly in our UFUN documentation starting with the include
    statements.

 
=============================================================================*/

#include <stdio.h>
#include <uf.h>
#include <uf_assem.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_so.h>
#include <uf_view.h>


/* ARGSUSED */
void ufusr(char *param, int *retcod, int param_len)
{
    int      indx = 0;
    int      num_curves = 0;
    int      ifail = 0;
    tag_t    view_tag = NULL_TAG;
    tag_t    old_anchor = NULL_TAG;
    tag_t    *new_curves = NULL;
    tag_t    new_region = NULL_TAG;
    tag_t    new_anchor = NULL_TAG;
    tag_t    part_tag = UF_ASSEM_ask_work_part();
    logical  delete_curves = TRUE;
    double   tolerance = 0.0;
    char     error_message[ MAX_LINE_BUFSIZE ];
    UF_DRAW_break_region_data_t region_data = {0};
    UF_DRAW_break_region_boundary_p_t curves = NULL;
    UF_DRAW_view_boundary_t *segments = NULL;

    ifail = UF_initialize();

    printf("UF_DRAW_create_break_region sample ");

    /* Get the first view in the part. */
    ifail = UF_OBJ_cycle_objs_in_part(UF_ASSEM_ask_work_part(),
                                      UF_view_type, &view_tag);

    /* Get break first region in the part. */
    while (!ifail && view_tag != NULL_TAG)
    {
        UF_VIEW_type_t    type;
        UF_VIEW_subtype_t subtype;

        ifail = UF_VIEW_ask_type(view_tag, &type, &subtype);

        if (subtype == UF_VIEW_BREAK_SUBTYPE)
            break;

        ifail = UF_OBJ_cycle_objs_in_part(UF_ASSEM_ask_work_part(),
                                          UF_view_type, &view_tag);
    }

    if (!ifail)
        ifail = UF_DRAW_ask_view_anchor(view_tag, &old_anchor);

    /* Get the region data of the existing break region in the part. */
    if (!ifail)
        ifail = UF_DRAW_ask_break_region_data(view_tag, &region_data);

    /* Extract the anchor point before removing it.  It is needed to create a
       new region. */
    if (!ifail && old_anchor != NULL_TAG)
        ifail = UF_SO_create_point_extract(part_tag, UF_SO_update_after_modeling,
                                           old_anchor, NULL_TAG, &new_anchor);
    if (!ifail)
        ifail = UF_DRAW_ask_boundary_curves(view_tag, &tolerance, &num_curves, &segments);

    if (!ifail)
    {
        curves = (UF_DRAW_break_region_boundary_p_t)UF_allocate_memory(num_curves * sizeof(UF_DRAW_break_region_boundary_t), &ifail);
        new_curves = (tag_t *)UF_allocate_memory(num_curves * sizeof(tag_t), &ifail);
        
        for (indx = 0; indx < num_curves; indx++)
        {
            curves[indx].curve_tag = segments[indx].curve_tag;
            curves[indx].construction_curve = segments[indx].const_status;
            curves[indx].hatch_curve = (segments[indx].hatch_tag != NULL_TAG);
        }

        ifail = UF_DRAW_free_boundary(num_curves, segments);

        /* If there are construction lines in the region, extract them before
           they are deleted.  They are needed to create a new region.
        */
        for (indx = 0; !ifail && indx < num_curves; indx++)
        { 
            if (curves[indx].construction_curve)
            {
                ifail = UF_SO_create_curve_extract(part_tag,
                                                   UF_SO_update_after_modeling,
                                                   curves[indx].curve_tag,
                                                   UF_line_type,
                                                   UF_line_normal_subtype,
                                                   NULL_TAG, &new_curves[indx]);

                /* Make the curve not view dependent to the drawing view. */
                if (!ifail)
                    ifail = uc6401("", new_curves[indx]);
            }
            else
                new_curves[indx] = NULL_TAG; 
        }
 
        if (!ifail)
        {
            /* Delete the break region, but don't delete the break curves. */
            ifail = UF_DRAW_remove_break_region(view_tag, !delete_curves);

            if (!ifail)
                /* Create another break region like the one before. */
                ifail = UF_DRAW_create_break_region(region_data.view_tag, new_anchor, num_curves, curves, &new_region);

            for (indx = 0; indx < num_curves; indx++)
                UF_OBJ_delete_object(new_curves[indx]);
        }

        UF_free(curves);
        UF_free(new_curves);
    }

    if (!ifail)
    {
        /* Modify the distance between regions */
        region_data.distance += 0.25;

        /* Modify the position option of region data. */
        if (region_data.position_type == UF_DRAW_BREAK_POSITION_TWO_REGIONS)
            region_data.position_type = UF_DRAW_BREAK_POSITION_DISTANCE;
        else
        if (region_data.position_type == UF_DRAW_BREAK_POSITION_DISTANCE)
            region_data.position_type = UF_DRAW_BREAK_POSITION_INFERRED;
        else
            region_data.position_type = UF_DRAW_BREAK_POSITION_DEFAULT;

        /* Set new region data. */
        ifail = UF_DRAW_set_break_region_data(new_region, &region_data);
    }

    /* Delete the break region along with the break curves. */
    if (!ifail)
        ifail = UF_DRAW_remove_break_region(new_region, delete_curves);

    if (ifail)
        ifail = UF_get_fail_message(ifail, error_message);
    else if (view_tag == NULL_TAG)
        printf("fails.\nError is: no break region to run test.\n");
    else
        printf("is successful.\n");

    ifail = UF_terminate();
}
