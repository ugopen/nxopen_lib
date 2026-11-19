
/*===========================================================================

        Copyright (c) 1997 Electronic Data Systems Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function programs:      *
 *                                                                            *
 *   UF_DRF_create_assortpart_aid:  Create and Display an Assorted Parts      *
 *                                  Drafting Aid (dimensions by parts)        *
 *   UF_DRF_create_assortpart_dim:  Create and Display an Assorted Parts      *
 *                                  Dimension (dimensions by parts)           *
 *   UF_DRF_init_assortpart_arc:    Initialize an Assorted Parts              *
 *                                  Arc Data Structure                        *
 *   UF_DRF_init_assortpart_arrow:  Initialize an Assorted Parts              *
 *                                  Arrow Data Structure                      *
 *   UF_DRF_init_assortpart_line:   Initialize an Assorted Parts              *
 *                                  Line Data Structure                       *
 *   UF_DRF_init_assortpart_text:   Initialize an Assorted Parts              *
 *                                  Text Data Structure                       *
 *   UF_DRF_ask_ann_data:           Ask Data of an Annotation Object          *
 *   UF_DRF_ask_ann_arc_seg_angles: Ask Start and End Angles of an Annotation *
 *                                  Object Arc Segment                        *
 *   UF_DRF_ask_ann_line_seg_ends:  Ask End Points of an Annotation Object    *
 *                                  Line Segment                              *
 *                                                                            *
 
 ******************************************************************************/

#include <stdlib.h>
#include <string.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_disp.h>
#include <uf_obj.h>
#include <uf_drf.h>
#include <uf_drf_types.h>
#include <uf_object_types.h>

void ufusr(char *param, int *retcod, int param_len)
{
    logical done, select = TRUE;
    static  int typmsk[4] = {1, 1, 1, 1};
    int     i = 0;
    int     status = 0;
    int     cyclfl = 0;
    int     response, index;
    int     daform, datype, ann_data[10];
    int     num_segments, type, subtype;
    int     base_arc, base_arrow, base_line, base_text, base_origin;
    int     count;
    double  origin[3], radang, offset = 1.0;
    char    *txtstr1 = "First String";
    char    *txtstr2 = "Second String";
    tag_t   annotation_tag, assorted_part_tag, view_tag = NULL_TAG;
    UF_UI_selection_options_t opts;
    UF_UI_mask_t mask[2];
    UF_DRF_assortpart_arc_t   arc;
    UF_DRF_assortpart_arrow_t arrow;
    UF_DRF_assortpart_line_t  line;
    UF_DRF_assortpart_text_t  text;

    status = UF_initialize ();

    if (!status)
    {
        /* set up selection options */
        opts.other_options = 0;
        opts.reserved = NULL;
        opts.scope = UF_UI_SEL_SCOPE_ANY_IN_ASSEMBLY;
        opts.num_mask_triples = 2;
        opts.mask_triples = mask;

        opts.mask_triples[0].object_type = UF_drafting_entity_type;
        opts.mask_triples[0].object_subtype = 0;
        opts.mask_triples[0].solid_type = 0;

        opts.mask_triples[1].object_type = UF_dimension_type;
        opts.mask_triples[1].object_subtype = 0;
        opts.mask_triples[1].solid_type = 0;

        while (select)
        {
            /* select the annotation from which to extract parts */
            UF_UI_select_single ("Select Annotation", &opts, &response,
                                 &annotation_tag, origin, &view_tag);
            if (response != 5) break;

            /* initialize the bases */
            base_arc = base_arrow = base_line = base_text = base_origin = 0;

            /* initialize the assorted part data structures */
            UF_DRF_init_assortpart_arc (&arc);
            UF_DRF_init_assortpart_arrow (&arrow);
            UF_DRF_init_assortpart_line (&line);
            UF_DRF_init_assortpart_text (&text);

            done = FALSE;

            while (!done)
            {
                /* extract the parts data from the annotation */
                UF_DRF_ask_ann_data
                    (&annotation_tag, typmsk, &cyclfl, ann_data, &datype, &daform,
                     &num_segments, origin, &radang);

                switch (datype + 1) 
                {
                case 1:
                    done = TRUE;
                    break;
                /* add lines */
                case 2:
                    ++line.num_lines;

                    line.num_line_segments = (int *) realloc
                        (line.num_line_segments, line.num_lines * sizeof (int));
                    line.num_line_segments[line.num_lines - 1] = num_segments;

                    count = 0;
                    for (index = 0; index < line.num_lines; ++index) 
                    {
                        count += line.num_line_segments[index];
                    }
                    line.line_data = (double *) realloc
                        (line.line_data, 4 * count * sizeof (double));
                    for (index = 1; index <= num_segments; ++index) 
                    {
                        UF_DRF_ask_ann_line_seg_ends
                            (&index, ann_data, &line.line_data[4 * (index - 1) + base_line]);
                    }
                    for (index = 1; index <= 4 * num_segments; ++index)
                    {
                        line.line_data[index - 1 + base_line] += offset;
                    }
                    base_line += 4 * num_segments;

                    break;
                /* add arcs */
                case 3:
                    ++arc.num_arcs;

                    arc.num_arc_segments = (int *) realloc
                        (arc.num_arc_segments, arc.num_arcs * sizeof (int));
                    arc.num_arc_segments[arc.num_arcs - 1] = num_segments;

                    count = 0;
                    for (index = 0; index < arc.num_arcs; ++index) 
                    {
                        count += arc.num_arc_segments[index];
                    }
                    arc.arc_data = (double *) realloc
                        (arc.arc_data, (2 * count + 3 * arc.num_arcs) * sizeof (double));
                    arc.arc_data[base_arc    ] = origin[0] + offset;
                    arc.arc_data[base_arc + 1] = origin[1] + offset;
                    arc.arc_data[base_arc + 2] = radang;
                    for (index = 1; index <= num_segments; ++index)
                    {
                        UF_DRF_ask_ann_arc_seg_angles
                            (&index, ann_data, &arc.arc_data[2 * (index - 1) + 3 + base_arc]);
                    }
                    base_arc += 2 * num_segments + 3;

                    break;
                /* add text */
                case 4:
                    ++text.num_text;

                    text.num_lines_text = (int *) realloc
                        (text.num_lines_text, text.num_text * sizeof (int));
                    text.num_lines_text[text.num_text - 1] = 2;

                    count = 0;
                    for (index = 0; index < text.num_text; ++index) 
                    {
                        count += text.num_lines_text[index];
                    }
                    text.text = (char **) realloc (text.text, count * sizeof (char *));
                    text.text[base_text    ] =
                        (char *) malloc (strlen (txtstr1) * sizeof (char) + 1);
                    text.text[base_text + 1] =
                        (char *) malloc (strlen (txtstr2) * sizeof (char) + 1);
                    strcpy (text.text[base_text    ], txtstr1);
                    strcpy (text.text[base_text + 1], txtstr2);
                    base_text += 2;

                    text.text_origin = (double *) realloc
                        (text.text_origin, 2 * text.num_text * sizeof (double));
                    text.text_origin[base_origin    ] = origin[0] + offset * text.num_text;
                    text.text_origin[base_origin + 1] = origin[1] + offset * text.num_text;
                    base_origin += 2;

                    break;
                /* add arrow */
                case 5:
                    ++arrow.num_arrows;

                    arrow.arrowhead_subtype = (int *) realloc
                        (arrow.arrowhead_subtype, arrow.num_arrows * sizeof (int));
                    arrow.arrowhead_subtype[arrow.num_arrows - 1] = daform;

                    arrow.arrow_data = (double *) realloc
                        (arrow.arrow_data, 3 * arrow.num_arrows * sizeof (double));
                    arrow.arrow_data[base_arrow    ] = origin[0] + offset;
                    arrow.arrow_data[base_arrow + 1] = origin[1] + offset;
                    arrow.arrow_data[base_arrow + 2] = radang;
                    base_arrow += 3;

                    break;
                default:
                    break;
                }
            }

            UF_OBJ_ask_type_and_subtype (annotation_tag, &type, &subtype);
            if (type == UF_drafting_entity_type)
            {
                /* create and display an assorted parts drafting aid */
                UF_DRF_create_assortpart_aid
                    (&arc, &arrow, &line, &text, &assorted_part_tag);
            }
            else
            {
                /* create and display an assorted parts dimension */
                UF_DRF_create_assortpart_dim
                    (&arc, &arrow, &line, &text, &assorted_part_tag);
            }

            /* turn the attention off */
            UF_DISP_set_highlight (annotation_tag, i);

            /* free the malloced areas */
            if (arc.num_arc_segments) free (arc.num_arc_segments);
            if (arc.arc_data) free (arc.arc_data);
            if (arrow.arrowhead_subtype) free (arrow.arrowhead_subtype);
            if (arrow.arrow_data) free (arrow.arrow_data);
            if (line.num_line_segments) free (line.num_line_segments);
            if (line.line_data) free (line.line_data);
            count = 0;
            for (index = 0; index < text.num_text; ++index) 
            {
                count += text.num_lines_text[index];
            }
            for (index = 0; index < count; index++)
            {
                if (text.text[index]) free (text.text[index]);
            }
            if (text.num_lines_text) free (text.num_lines_text);
            if (text.text) free (text.text);
            if (text.text_origin) free (text.text_origin);
        }
    }
    UF_terminate ();
}
