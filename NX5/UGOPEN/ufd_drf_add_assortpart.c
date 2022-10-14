
/*===========================================================================

        Copyright (c) 1997 Electronic Data Systems Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function program:       *
 *                                                                            *
 *   UF_DRF_add_assortpart_to_ann: Add Assorted Parts to an Annotation        *
 *                                                                            *
 
 ******************************************************************************/

#include <stdlib.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_disp.h>
#include <uf_drf.h>
#include <uf_drf_types.h>
#include <uf_object_types.h>

void ufusr (char *param, int *retcod, int param_len)
{
    logical select = TRUE;
    int     status = 0;
    int     i = 0;
    int     response;
    int     number_of_objects;
    double  origin[3];
    tag_t   annotation_tag, assorted_part_tag, view_tag = NULL_TAG;
    tag_t   list_of_objects[20];
    UF_UI_selection_options_t opts;
    UF_UI_mask_t mask[4];

    status = UF_initialize ();

    if (!status)
    {
        /* set up selection options */
        opts.other_options = 0;
        opts.reserved = NULL;
        opts.scope = UF_UI_SEL_SCOPE_ANY_IN_ASSEMBLY;
        opts.num_mask_triples = 4;
        opts.mask_triples = mask;

        opts.mask_triples[0].object_type = UF_drafting_entity_type;
        opts.mask_triples[0].object_subtype = 0;
        opts.mask_triples[0].solid_type = 0;

        opts.mask_triples[1].object_type = UF_dimension_type;
        opts.mask_triples[1].object_subtype = 0;
        opts.mask_triples[1].solid_type = 0;

        opts.mask_triples[2].object_type = UF_line_type;
        opts.mask_triples[2].object_subtype = 0;
        opts.mask_triples[2].solid_type = 0;

        opts.mask_triples[3].object_type = UF_circle_type;
        opts.mask_triples[3].object_subtype = 0;
        opts.mask_triples[3].solid_type = 0;

        while (select)
        {
            /* select the annotation to which to add parts */
            UF_UI_select_single ("Select Annotation", &opts, &response,
                                 &annotation_tag, origin, &view_tag);
            if (response != 5) break;

            number_of_objects = 0;
            while (select)
            {
                /* select the assorted parts to add to the annotation */
                UF_UI_select_single ("Select Assorted Part", &opts, &response,
                                     &assorted_part_tag, origin, &view_tag);
                if (response != 5) break;
                list_of_objects[number_of_objects] = assorted_part_tag;
                number_of_objects++;
                if (number_of_objects > 19) break;
            }

            /* turn the attention off */
            UF_DISP_set_highlight (annotation_tag, i);

            /* add the assorted parts to the annotation */
            UF_DRF_add_assortpart_to_ann (annotation_tag,
                number_of_objects, list_of_objects);
        }
    }
    UF_terminate ();
}
