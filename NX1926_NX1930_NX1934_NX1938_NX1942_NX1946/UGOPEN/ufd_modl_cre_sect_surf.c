/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_init_section_surface                                       *
 *         UF_MODL_create_section_surface                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates a    *
 *   section surface.                                                         *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_curve.h>
#include <uf_modl.h>
#include <uf_modl_types.h>

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
    
    int knot_fix, pole_fix;
    tag_t start_tag;
    tag_t apex_tag;
    tag_t end_tag;
    tag_t spine_tag;
    tag_t feature_tag;
    double start_poles[] = {0.0, 4.0, 2.0, 1.0,
                            3.0, 4.0, 2.0, 1.0,
                            6.0, 4.0, 1.0, 1.0};

    double start_knots[] = {0.0, 0.0, 0.0, 
                            1.0, 1.0, 1.0};

    double end_poles[] = {0.0, 0.0, 0.0, 1.0,
                          3.0, 0.0, 0.0, 1.0,
                          6.0, 1.0, 0.0, 1.0};

    double end_knots[] = {0.0, 0.0, 0.0, 
                          1.0, 1.0, 1.0};

    double apex_poles[] = {0.0, 0.0, 2.0, 1.0,
                           3.0, 0.0, 2.0, 1.0,
                           6.0, 1.0, 1.0, 1.0};

    double apex_knots[] = {0.0, 0.0, 0.0,
                           1.0, 1.0, 1.0};

    UF_CURVE_line_t spine_coords;

    UF_MODL_secsrf_data_t section_surface;
    UF_STRING_t ss_string[2];
    UF_STRING_t apex_string;
    UF_STRING_t spine_string;

    spine_coords.start_point[0] = 6.0;
    spine_coords.start_point[1] = 4.0;
    spine_coords.start_point[2] = 0.0;
    
    spine_coords.end_point[0] = 0.0;
    spine_coords.end_point[1] = 4.0;
    spine_coords.end_point[2] = 0.0;
 
/* Create the input curves. */
    UF_CALL(UF_MODL_create_spline (3, 3, start_knots, start_poles, 
                                   &start_tag, &knot_fix, &pole_fix));
    UF_CALL(UF_MODL_create_spline (3, 3, end_knots, end_poles, 
                                   &end_tag, &knot_fix, &pole_fix));
    UF_CALL(UF_MODL_create_spline (3, 3, apex_knots, apex_poles, 
                                   &apex_tag, &knot_fix, &pole_fix ));

    UF_CALL(UF_CURVE_create_line(&spine_coords,&spine_tag));

/* Create Strings from the curves. 
   Each string contains 1 curve. */

    UF_MODL_init_string_list(&ss_string[0]);
    UF_MODL_create_string_list(1,1,&ss_string[0]);
    ss_string[0].num = 1;
    ss_string[0].string[0] = 1;
    ss_string[0].dir[0] = 1;
    ss_string[0].id[0] = start_tag;
    
    UF_MODL_init_string_list(&ss_string[1]);
    UF_MODL_create_string_list(1,1,&ss_string[1]);
    ss_string[1].num = 1;
    ss_string[1].string[0] = 1;
    ss_string[1].dir[0] = 1;
    ss_string[1].id[0] = end_tag;

    UF_MODL_init_string_list(&apex_string);
    UF_MODL_create_string_list(1,1,&apex_string);
    apex_string.num = 1;
    apex_string.string[0] = 1;
    apex_string.dir[0] = 1;
    apex_string.id[0] = apex_tag;

    UF_MODL_init_string_list(&spine_string);
    UF_MODL_create_string_list(1,1,&spine_string);
    spine_string.num = 1;
    spine_string.string[0] = 1;
    spine_string.dir[0] = 1;
    spine_string.id[0] = spine_tag;

/* Initialize the section surface data structure. */
    UF_CALL(UF_MODL_init_section_surface (&section_surface));

/* Populate the structure with appropriate data. */
    section_surface.create_method = UF_MODL_secsrf_ends_apex_rho;
    section_surface.polynomial_status = 0;
    section_surface.tolerance = .001;

    section_surface.control_strings[0] = &ss_string[0]; /* start */
    section_surface.control_strings[1] = &apex_string;  /* apex */
    section_surface.control_strings[2] = &ss_string[1]; /* end */
    section_surface.control_strings[3] = (UF_STRING_p_t)NULL_TAG;
    section_surface.control_strings[4] = (UF_STRING_p_t)NULL_TAG;
    section_surface.control_strings[5] = (UF_STRING_p_t)NULL_TAG;

    section_surface.spine_string = &spine_string;

    section_surface.rho_data.data_method = UF_MODL_secsrf_cubic;
    section_surface.rho_data.data_values.data_value[0] = 0.40;
    section_surface.rho_data.data_values.data_value[1] = 0.70;
    section_surface.rho_data.data_values.data_exp[0] = NULL_TAG;
    section_surface.rho_data.data_values.data_exp[1] = NULL_TAG;
    section_surface.rho_data.data_values.general_law = NULL;
    section_surface.rho_data.data_values.data_constant = 0.0;

    section_surface.tangent_faces[0] = NULL_TAG;
    section_surface.tangent_faces[1] = NULL_TAG;

    section_surface.radius_data.data_method = UF_MODL_secsrf_no_data ;
    section_surface.angle_data.data_method = UF_MODL_secsrf_no_data ;

/* Build the section surface. */
    UF_CALL(UF_MODL_create_section_surface(&section_surface, &feature_tag));

/* Free all the strings. */
    UF_MODL_free_string_list(&ss_string[0]);
    UF_MODL_free_string_list(&ss_string[1]);
    UF_MODL_free_string_list(&apex_string);
    UF_MODL_free_string_list(&spine_string);
 
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
