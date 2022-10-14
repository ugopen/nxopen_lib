
/* ====================================================================
 *
 *        Copyright (c) 2000 Unigraphics Solutions Inc.
 *                     Unpublished - All rights reserved
 *
 * ==================================================================== */

/* ============================================================================

   ========================================================================== */


/**********************************************************************

	The following example creates a block at origin (0,0,0) with
	edge lengths of (300,25,150) and a plane at XC = 100.  The
	plane is used to section the block.  Then the parent block and
	plane of the section curves feature are found.

	Next, the block is sectioned using the parallel planes function.

	Next, a smart point and axis are used to do a radial planes
        sectioning.

	Finally, the program creates a line for sectioning using the
	perpendicular to curves option.  The Join Type is set to poly-
	nomial cubic.  Again the block and parent (perpendicular)
	curve eid are found. Then the defining data is obtained using 
	UF_CURVE_section_ask_perpcrv_data.

**********************************************************************
*/

#include <stdio.h>
#include <uf.h>
#include <uf_curve.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_so.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static int report (char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char   messg[133];
        printf("%s, line %d, %s\n", file, line, call);
        UF_get_fail_message (irc, messg);

        printf("  returned a %d\n", irc);
        printf("  returned error %d, %s\n", irc, messg);
    }
    return (irc);
}

static void do_ugopen_api (void)
{
    double origin[3] = {0.0,0.0,0.0};

    double plane_data[9] = {100.0,0.0,50.0, 100.0,0.0,49.0, 100.0,1.0,50.0};

    double vect[3] = {250.0, 0.0, 0.0};
    double vect2[3] = {250.0, 50.0, 0.0};

    tag_t  smart_point, smart_axis;
    tag_t  smart_point2, smart_dirr;

    tag_t  part_tag, block_feat, block_tag, plane_tag;
    tag_t  line_tag, line_tag2, point_tag;
    tag_t  objects[1], planes[1];
    tag_t  section_curves_feature, *section_curves;
    tag_t  defining_feature, defining_target, sectioning_objects[2];
    tag_t  object_in_part, dbl_tag;

    const UF_SO_dirr_on_curve_option_t  option = UF_SO_dirr_on_curve_tangent;

    const logical   flip = TRUE;

    int    num_section_curves, type;

    double                           point_data[3];
    UF_CURVE_line_t                  line_data;
    UF_CURVE_section_general_data_t  general_data;
    UF_CURVE_section_planes_data_t   planes_data;
    UF_CURVE_section_parallel_data_t parallel_data;
    UF_CURVE_section_radial_data_t   radial_data;
    UF_CURVE_section_perpcrv_data_t  perpcrv_data;

    char  *part_name = "section_curves";

    char  *edge_lens[3] = {"300.0","25.0","150.0"};

    
    UF_CALL (UF_PART_new (part_name, ENGLISH, &part_tag));

    UF_CALL (UF_MODL_create_block1 (UF_NULLSIGN, origin, edge_lens,
                              &block_feat));

    UF_CALL (UF_MODL_ask_feat_body (block_feat, &block_tag));

    objects[0] = block_tag;

    FTN(uf5374) (&plane_data[0], &plane_data[3], &plane_data[6],
                     &plane_tag);

    point_data[0] = 300.0;
    point_data[1] = 25.0;
    point_data[2] = 150.0;

    UF_CALL (UF_CURVE_create_point (point_data, &point_tag));

    object_in_part =  block_tag;

    line_data.start_point[0] = 25.0;
    line_data.start_point[1] = 50.0;
    line_data.start_point[2] = 25.0;

    line_data.end_point[0]   = line_data.start_point[0] + vect[0];
    line_data.end_point[1]   = line_data.start_point[1] + vect[1];
    line_data.end_point[2]   = line_data.start_point[2] + vect[2];

    UF_CALL (UF_CURVE_create_line (&line_data, &line_tag));

    line_data.end_point[0]   = line_data.start_point[0] + vect2[0];
    line_data.end_point[1]   = line_data.start_point[1] + vect2[1];
    line_data.end_point[2]   = line_data.start_point[2] + vect2[2];

    UF_CALL (UF_CURVE_create_line (&line_data, &line_tag2));

    planes[0] = plane_tag;

    general_data.associate     = 1;
    general_data.objects       = objects;
    general_data.num_objects   = 1;
    general_data.grouping      = 0;
    general_data.join_type     = 0;
    general_data.tolerance     = 0.0254;

    planes_data.planes         = planes;
    planes_data.num_planes     = 1;

    UF_CALL (UF_CURVE_section_from_planes (&general_data, &planes_data,
                     &section_curves_feature));

    printf (" section curves feature tag is %d\n", section_curves_feature);

    UF_CALL (UF_CURVE_ask_feature_curves (section_curves_feature,
                       &num_section_curves, &section_curves));

      UF_CALL (UF_CURVE_section_curve_ask_parents (section_curves[0],
                 &defining_feature, &type, &defining_target,
                 sectioning_objects));

    printf (" block tag is %d\n", block_tag);

      printf (" type of planes is  %d\n", type);
      printf (" sectioned object is  %d\n", defining_target);
      printf (" sectioning curve eid is %d\n", sectioning_objects[0]);

    parallel_data.base_plane     = plane_tag;
    parallel_data.step_distance  = 3.0;
    parallel_data.start_distance = 0.0;
    parallel_data.end_distance   = 10.0;

    UF_CALL (UF_CURVE_section_from_parallel_planes (&general_data, &parallel_data,
                     &section_curves_feature));

    UF_CALL (UF_CURVE_ask_feature_curves (section_curves_feature,
                       &num_section_curves, &section_curves));

    UF_free (section_curves);

    UF_CALL (UF_SO_create_scalar_double (object_in_part,
                       UF_SO_update_within_modeling, 0.5, &dbl_tag) );

    UF_CALL (UF_SO_create_point_on_curve (object_in_part, 
            UF_SO_update_within_modeling, line_tag, dbl_tag, &smart_point) );

    printf (" smart point is %d\n", smart_point);

    UF_CALL (UF_SO_create_dirr_on_curve (object_in_part, 
                 UF_SO_update_within_modeling, line_tag, 
                   dbl_tag, option, flip,
                              &smart_dirr));

    printf (" smart dirr is %d\n", smart_dirr);

    UF_CALL (UF_SO_create_scalar_double (object_in_part,
                       UF_SO_update_within_modeling, 1.0, &dbl_tag) );

    UF_CALL (UF_SO_create_point_on_curve (object_in_part, 
            UF_SO_update_within_modeling, line_tag2, dbl_tag, &smart_point2) );

    UF_CALL (UF_SO_create_axis_point_dir (object_in_part, 
                 UF_SO_update_within_modeling, smart_point2, smart_dirr,
                         &smart_axis));

    printf (" smart axis is %d\n", smart_axis);


    radial_data.base_point       = smart_point;
    radial_data.base_axis        = smart_axis;
    radial_data.step_angle       = 10.0;
    radial_data.start_angle      = 10.0;
    radial_data.end_angle        = 30.0;

    UF_CALL (UF_CURVE_section_from_radial_planes (&general_data, &radial_data,
                     &section_curves_feature));

/* Get the section curve type and data */

    UF_CALL (UF_CURVE_section_ask_type (section_curves_feature, &type));

    printf ("Section curve type is %d\n", type);

    if (type == 2)
    {
        UF_CALL (UF_CURVE_section_ask_radial_data ( section_curves_feature,
                    &general_data, &radial_data));
        printf (" Step angle is  %f\n", radial_data.step_angle);
        printf (" Start angle is  %f\n", radial_data.start_angle);
        printf (" End angle is  %f\n", radial_data.end_angle);
    }

    UF_free (general_data.objects);


    general_data.join_type     = 1;
    general_data.objects       = objects;

    perpcrv_data.curve_eid     = line_tag;
    perpcrv_data.direction     = 1;
    perpcrv_data.space_meth    = 1;
    perpcrv_data.num_points    = 4;
    perpcrv_data.start_pct     = 20.0;
    perpcrv_data.end_pct       = 80.0;
    perpcrv_data.ratio         = 0.0;
    perpcrv_data.chord_tol     = 0.0;
    perpcrv_data.increment     = 0.0;

    UF_CALL (UF_CURVE_section_from_perpcrv_planes (&general_data,
                        &perpcrv_data, &section_curves_feature));

    printf (" section curves feature tag is %d\n", section_curves_feature);

    UF_CALL (UF_CURVE_ask_feature_curves (section_curves_feature,
                       &num_section_curves, &section_curves));

    UF_CALL (UF_CURVE_section_curve_ask_parents (section_curves[0],
                 &defining_feature, &type, &defining_target,
                 sectioning_objects));

    UF_free (section_curves);

/* Get the section curve type and data */

    UF_CALL (UF_CURVE_section_ask_type (section_curves_feature, &type));

    printf ("Section curve type is %d\n", type);

    if (type == 3)
    {
        UF_CALL (UF_CURVE_section_ask_perpcrv_data ( section_curves_feature,
                    &general_data, &perpcrv_data));

        printf (" Direction is  %d\n", perpcrv_data.direction);
        printf (" Number of planes is  %d\n", perpcrv_data.num_points);
        printf (" Start percent is  %f\n", perpcrv_data.start_pct);
        printf (" End percent is  %f\n", perpcrv_data.end_pct);

        UF_free (general_data.objects);
    }
}

void ufusr (char *param, int *retcode, int paramLen)
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

