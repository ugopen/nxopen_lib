/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_PATT_create_point                                               *
 *         UF_PATT_set_archiving                                              *
 *         UF_PATT_set_shading                                                *
 *         UF_PATT_is_archiving_on                                            *
 *         UF_PATT_is_shading_on                                              *
 *         UF_PATT_set_params                                                 *
 *         UF_PATT_ask_params                                                 *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates a pattern master part file, saves it,      *
 *   and then retrieves the pattern data as a pattern object into another     *
 *   part.                                                                    *
 *                                                                            *
 *   NOTE: This program must be executed as an internal user function.        *
 *                                                                            *
 
 *                                                                            *
 ******************************************************************************/

/* Internal user function program to demonstrate pattern function calls */

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_curve.h>
#include <uf_part.h>
#include <uf_csys.h>
#include <uf_patt.h>

/* Prototype */
static void patt_example(void);

/* Sample funtion */
static void patt_example(void)
{
    tag_t point_tag;
    tag_t pat_master_tag;
    tag_t parent_tag;
    tag_t pat_tag;
    tag_t circle_tag;

    tag_t wcs;
    UF_CURVE_arc_t circle;
    logical on;

    double pat_point[3] =  { 0.0, 0.2, 0.0 };
    double pat_data[13] = { 1.0, 0.0, 0.0,  /* pattern object orientation */
                              0.0, 1.0, 0.0,  /*  "       "      "          */
                              0.0, 0.0, 1.0,  /*  "       "      "          */
                              1.5, 1.5, 0.0,  /* pattern object origin */
                              1.25};          /* pattern object scale */
    UF_PATT_switch_t pat_marker = UF_PATT_on;
    UF_PATT_switch_t pat_maxmin = UF_PATT_off;
    UF_PATT_switch_t pat_control_pt = UF_PATT_on;


    /* Create a pattern master part file */
    UF_PART_new("patt_master", UF_PART_ENGLISH, &pat_master_tag);

    /* Add geometry (a circle) */
    circle.start_angle = 0.0;
    circle.end_angle = 360.0 * DEGRA;
    circle.arc_center[0] = 0.0;
    circle.arc_center[1] = 0.0;
    circle.arc_center[2] = 0.0;
    circle.radius = 0.25;
    UF_CSYS_ask_wcs(&wcs);
    UF_CSYS_ask_matrix_of_object(wcs, &circle.matrix_tag);
    UF_CURVE_create_arc(&circle, &circle_tag);

    /* Create pattern point */
    UF_PATT_create_point(pat_point, &point_tag);

    /* Set up switches */
    UF_PATT_set_archiving(UF_PATT_on);
    UF_PATT_set_shading(UF_PATT_off);
     
    /* Verify switches before saving */
    UF_PATT_is_archiving_on(&on);
    if (on)
        printf("Pattern data archiving switch is on\n");
    else
        printf("Pattern data archiving switch is off\n");

    UF_PATT_is_shading_on(&on);
    if (on)
        printf("Pattern shaed data archiving switch is on\n");
    else
        printf("Pattern shaded data archiving switch is off\n");

    /* Save the pattern master part file */
    UF_PART_save();


    /* Create a parent part */
    UF_PART_new("patt_parent", UF_PART_ENGLISH, &parent_tag);
    
    /* Retrieve the pattern */
    uc5823("patt_master", "", 1, pat_data, &pat_tag);

    /* Set pattern diaply parameters */
    UF_PATT_set_params(pat_tag, pat_marker, pat_maxmin, pat_control_pt);

    /* Read the parameters */
    UF_PATT_ask_params(pat_tag, &pat_marker, &pat_maxmin, &pat_control_pt);

    if (pat_marker == UF_PATT_on)
        printf("The pattern origin marker display is turned on\n");
    else
        printf("The pattern origin marker display is turned off\n");
    
    if (pat_maxmin == UF_PATT_on)
        printf("The pattern's Max/Min box display is turned on\n");
    else
        printf("The pattern's Max/Min box display is turned off\n");
    
    if (pat_control_pt == UF_PATT_on)
        printf("The pattern's control point display is turned on\n");
    else
        printf("The pattern's control point display is turned off\n");
}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
{
  if (!UF_initialize())
  {
    patt_example();
    UF_terminate();
  }
}
