/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routines:        *
 *                                                                            *
 *         UF_CLEAR_create_dataset                                            *
 *         UF_CLEAR_copy_dataset                                              *
 *         UF_CLEAR_rename_dataset                                            *
 *         UF_CLEAR_count_datasets                                            *
 *         UF_CLEAR_ask_next_dataset                                          *
 *         UF_CLEAR_ask_dataset_name                                          *
 *         UF_CLEAR_ask_dataset_version                                       *
 *         UF_CLEAR_delete_dataset                                            *
 *         UF_CLEAR_find_dataset                                              *
 *         UF_CLEAR_set_obj_list                                              *
 *         UF_CLEAR_ask_num_lists                                             *
 *         UF_CLEAR_ask_default_clear_zone                                    *
 *         UF_CLEAR_ask_object_clear_zone                                     *
 *         UF_CLEAR_ask_pair_clear_zone                                       *
 *         UF_CLEAR_set_default_clear_zone                                    *
 *         UF_CLEAR_set_object_clear_zone                                     *
 *         UF_CLEAR_set_pair_clear_zone                                       *
 *         UF_CLEAR_ask_exclude_rules                                         *
 *         UF_CLEAR_is_pair_changed                                           *
 *         UF_CLEAR_is_pair_included                                          *
 *         UF_CLEAR_set_pair_exclusion                                        *
 *         UF_CLEAR_set_pair_inclusion                                        *
 *         UF_CLEAR_ask_analysis_mode                                         *
 *         UF_CLEAR_ask_results                                               *
 *         UF_CLEAR_count_interferences                                       *
 *         UF_CLEAR_ask_next_interf                                           *
 *         UF_CLEAR_ask_interf_data                                           *
 *         UF_CLEAR_set_interf_text                                           *
 *         UF_CLEAR_delete_interf                                             *
 *         UF_CLEAR_do_clearance_analysis                                     *
 *         UF_CLEAR_ask_preferences                                           *
 *         UF_CLEAR_set_preferences                                           *
 *         UF_CLEAR_delete_all                                                *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates example_uf_clear.prt which generates a new *
 *   part containing four solid bodies and then creates a dataset for         *
 *   for clearance analysis data.                                             *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

/**************
 ** Includes **
 **************/
#include <stdio.h>
#include <time.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_part.h>
#include <uf_modl.h>
#include <uf_clear.h>
/****************
 ** Prototypes **
 ****************/
static int example_uf_clear(void);
static int example_uf_clear_dataset(void);
static int example_uf_clear_object(void);
static int example_uf_clear_zone(void);
static int example_uf_clear_pair(void);
static int example_uf_clear_analysis(void);
static int example_uf_clear_misc(void);
/***************
 ** Variables **
 ***************/
static int          err;            /* General return code */
static int          num;            /* For number query */
static tag_t        part_tag;       /* Working part tag */
static tag_t        sphere_tag;     /* sphere tag */
static tag_t        block_tag;      /* block tag */
static tag_t        cone_tag;       /* cone tag */
static tag_t        cyl_tag;        /* cylinder tag */
static tag_t        dataset;        /* Working dataset tag */
static tag_t        obj_list[4];    /* Working object list array */
static tag_t        clr_zone;       /* General zone tag */
static UF_CLEAR_pref_t  pref;       /* Preferences structure */
/***************
 ** Functions **
 ***************/
/*ARGSUSED*/
void ufusr (char *param, int *retcod, int param_len)
{
    char    errmsg[ MAX_LINE_BUFSIZE ];
    *retcod = example_uf_clear();
    if (*retcod < 0)
        fprintf(stderr, "example_uf_clear failed. See stderr.\n");
    else if (*retcod > 0)
    {
        UF_get_fail_message(*retcod, errmsg);
        fprintf(stderr, "%s\n", errmsg);
    }
    else
    {
        /* fall through */
    }
    return;
}
/*
  Name:
    example_uf_clear.
  Return:
    0 for success, or an error code.
*/
static int example_uf_clear (
    void
) {
    double  origin[3];
    double  corner[3];
    double  center[3];
    double  dir[3];
    char    *len[3];
    char    *diam[2];
    char    *diameter;
    char    *height;
    tag_t   feature_tag;
    err = UF_initialize();
    if (err) return err;
    /* Create a simple part with 4 solid objects */
    err = UF_PART_new("example_uf_clear.prt", UF_PART_METRIC,
        &part_tag);
    if (err) return err;
    /* First, a sphere */
    center[0] = 0.1, center[1] = 0.2, center[2] = 0.3;
    diameter = "1.4";
    err = UF_MODL_create_sphere1(UF_NULLSIGN, center, diameter,
        &feature_tag);
    if (err) return err;
    err = UF_MODL_ask_feat_body(feature_tag, &sphere_tag);
    if (err) return err;
    /* and a block */
    corner[0] = 0.7, corner[1] = 0.3, corner[2] = 1.3;
    len[0] = "1.0", len[1] = "1.0", len[2] = "1.0";
    err = UF_MODL_create_block1(UF_NULLSIGN, corner, len,
        &feature_tag);
    if (err) return err;
    err = UF_MODL_ask_feat_body(feature_tag, &block_tag);
    if (err) return err;
    /* and a cone */
    origin[0] = -0.5, origin[1] = 0.2, origin[2] = -0.2;
    height = "3.3";
    diam[0] = "1.2", diam[1] = "2.0";
    dir[0] = 0.2, dir[1] = -0.5, dir[2] = 0.84;
    err = UF_MODL_create_cone1(UF_NULLSIGN, origin, height,
        diam, dir, &feature_tag);
    if (err) return err;
    err = UF_MODL_ask_feat_body(feature_tag, &cone_tag);
    if (err) return err;
    /* and finally a cylinder */
    origin[0] = 0.5, origin[1] = 0.2, origin[2] = 1.2;
    height = "2.0";
    diameter = "3.5";
    dir[0] = 0.2, dir[1] = 0.5, dir[2] = -0.84;
    err = UF_MODL_create_cyl1(UF_NULLSIGN, origin, height,
        diameter, dir, &feature_tag);
    if (err) return err;
    err = UF_MODL_ask_feat_body(feature_tag, &cyl_tag);
    if (err) return err;
    err = example_uf_clear_dataset();
    if (err) return err;
    err = example_uf_clear_object();
    if (err) return err;
    err = example_uf_clear_pair();
    if (err) return err;
    err = example_uf_clear_zone();
    if (err) return err;
    err = example_uf_clear_analysis();
    if (err) return err;
    err = example_uf_clear_misc();
    if (err) return err;
    UF_terminate();
    return 0;
}
/*
  Name:
    example_uf_clear_dataset.
  Description:
    Show UF_CLEAR dataset routines.
  Return:
    0 for success; -1 for non-UF_CLEAR errors, or an
    UF_CLEAR error code.
*/
static int example_uf_clear_dataset (
    void
) {
    char    name[ MAX_LINE_BUFSIZE ];
    int     ver;
    tag_t   dataset1;
    tag_t   dataset2;
    /* Creating a dataset called "working dataset" */
    err = UF_CLEAR_create_dataset(part_tag, "working dataset",
        &dataset);
    if (err) return err;
    /* Copy it to "copied dataset" */
    err = UF_CLEAR_copy_dataset(dataset, "copied dataset",
        UF_CLEAR_COPY_NO_RESULTS, &dataset1);
    if (err) return err;
    /* Rename "copied dataset" to "renamed dataset" */
    err = UF_CLEAR_rename_dataset(dataset1, "renamed dataset");
    if (err) return err;
    /* Count the number of datasets */
    err = UF_CLEAR_count_datasets(part_tag, &num);
    if (err) return err;
    fprintf(stderr, "it is %d.\n", num);
    /* Looping through all datasets */
    dataset2 = NULL_TAG;
    while (TRUE)
    {
        err = UF_CLEAR_ask_next_dataset(part_tag, &dataset2);
        if (err) return err;
        if (dataset2 == NULL_TAG)
            break;
        err = UF_CLEAR_ask_dataset_name(dataset2, name);
        if (err) return err;
        fprintf(stderr, "found \"%s\".\n", name);
        err = UF_CLEAR_ask_dataset_version(dataset2, &ver);
        if (err) return err;
        fprintf(stderr, "its version is %d.\n", ver);
    }
    /* Deleting "renamed dataset" */
    err = UF_CLEAR_delete_dataset(dataset1);
    if (err) return err;
    /* Find "working dataset" */
    err = UF_CLEAR_find_dataset(part_tag, "working dataset",
        &dataset2);
    if (err) return err;
    return 0;
}
/*
  Name:
    example_uf_clear_object.
  Description:
    Show UF_CLEAR object list routines.
    
  Return:
    0 for success; -1 for non-UF_CLEAR errors, or an
    UF_CLEAR error code.
*/
static int example_uf_clear_object (
    void
) {
    tag_t   *obj_list_2;
    int     type;
    int     size;
    /* Explicitly set up a fixed object list */
    obj_list[0] = sphere_tag;
    obj_list[1] = block_tag;
    obj_list[2] = cone_tag;
    obj_list[3] = cyl_tag;
    err = UF_CLEAR_set_obj_list(dataset, 1, UF_CLEAR_FIXED_LIST,
        4, obj_list);
    if (err) return err;
    /* Tell UG not to use object list #2 */
    err = UF_CLEAR_set_obj_list(dataset, 2,
        UF_CLEAR_LIST2_NOT_USED, 0, (tag_t *)NULL_TAG);
    if (err) return err;
    /* Find out number of object lists set up */
    err = UF_CLEAR_ask_num_lists(dataset, &num);
    if (err) return err;
    fprintf(stderr, "it is %d.\n", num);
    /* Ask for object list #1 */
    err = UF_CLEAR_ask_obj_list(dataset, 1, &type, &size,
        &obj_list_2);
    if (err) return err;
    fprintf(stderr, "type is %d, size is %d.\n", type, size);
    if (size > 0)
        UF_free(obj_list_2);
    return 0;
}
/* cf: example_uf_clear_zone() below */
static int ask_zones (
    void
) {
    double  value;
    int     source;
    err = UF_CLEAR_ask_default_clear_zone(dataset, &clr_zone);
    if (err) return err;
    if (clr_zone == NULL_TAG)
        value = 0.0;
    else if (UF_MODL_ask_exp_tag_value(clr_zone, &value))
    {
        fprintf(stderr, "UF_MODL_ask_exp_tag_value failed.\n");
        return -1;
    }
    else
    {
        /* fall through */
    }
    fprintf(stderr, "The default clearance zone is %f.\n", value);
    err = UF_CLEAR_ask_object_clear_zone(dataset, cone_tag,
        &clr_zone, &source);
    if (err) return err;
    if (clr_zone == NULL_TAG)
        value = 0.0;
    else if (UF_MODL_ask_exp_tag_value(clr_zone, &value))
    {
        fprintf(stderr, "UF_MODL_ask_exp_tag_value failed.\n");
        return -1;
    }
    else
    {
        /* fall through */
    }
    fprintf(stderr, "The clearance zone for the cone is %f.\n",
        value);
    fprintf(stderr, "its source is %d.\n", source);
    err = UF_CLEAR_ask_pair_clear_zone(dataset,
        sphere_tag, cyl_tag, &clr_zone, &source);
    if (err) return err;
    if (clr_zone == NULL_TAG)
        value = 0.0;
    else if (UF_MODL_ask_exp_tag_value(clr_zone, &value))
    {
        fprintf(stderr, "UF_MODL_ask_exp_tag_value failed.\n");
        return -1;
    }
    else
    {
        /* fall through */
    }
    fprintf(stderr, "The zone for sphere and cyl pair is %f.\n",
        value);
    fprintf(stderr, "its source is %d.\n", source);
    return 0;
}
/*
  Name:
    example_uf_clear_zone.
  Description:
    Show clearance zone routines.
  Return:
    0 for success; -1 for non-UF_CLEAR errors, or an
    UF_CLEAR error code.
*/
static int example_uf_clear_zone (
    void
) {
    err = ask_zones();
    if (err) return err;
    /* Set default zone to 4. */
    if (UF_MODL_create_exp_tag("2.5 * 4 - 6", &clr_zone))
    {
        fprintf(stderr, "UF_MODL_create_exp_tag failed.\n");
        return -1;
    }
    err = UF_CLEAR_set_default_clear_zone(dataset, clr_zone);
    if (err) return err;
    /* Set block's clearance zone to 4.75 */
    if (UF_MODL_create_exp_tag("9.5 / 2", &clr_zone))
    {
        fprintf(stderr, "UF_MODL_create_exp_tag failed.\n");
        return -1;
    }
    err = UF_CLEAR_set_object_clear_zone(dataset, block_tag,
        clr_zone);
    if (err) return err;
    /* Set cone and cyl's zone to 7.5 */
    if (UF_MODL_create_exp_tag("7.5", &clr_zone))
    {
        fprintf(stderr, "UF_MODL_create_exp_tag failed.\n");
        return -1;
    }
    err = UF_CLEAR_set_pair_clear_zone(dataset, cone_tag, cyl_tag,
        clr_zone);
    if (err) return err;
    err = ask_zones();
    if (err) return err;
    return 0;
}
/* cf: example_uf_clear_pair() below */
static int ask_rules (
    void
) {
    int     reason;
    int     rules;
    logical ans;
    char    *text;
    err = UF_CLEAR_ask_exclude_rules(dataset, &rules);
    if (err) return err;
    fprintf(stderr, "Exclusion rules value is %d.\n", rules);
    /* See whether cone and cyl pair has changed since last run */
    err = UF_CLEAR_is_pair_changed(dataset, cone_tag, cyl_tag,
        &ans);
    if (err) return err;
    if (ans)
        fprintf(stderr, "it has changed.\n");
    else
        fprintf(stderr, "it has *not* changed.\n");
    /* See whether sphere and block pair is to be included */
    err = UF_CLEAR_is_pair_included(dataset, sphere_tag, block_tag,
        &ans, &reason, &text);
    if (err) return err;
    if (ans)
        fprintf(stderr, "yes, it will be (reason=%d, \"%s\").\n",
            reason, text);
    else
        fprintf(stderr, "no, it will not (reason=%d, \"%s\").\n",
            reason, text);
    UF_free(text);
    return 0;
}
/*
  Name:
    example_uf_clear_pair.
  Description:
    Show clearance analysis object pair routines.
  Return:
    0 for success; -1 for non-UF_CLEAR errors, or an
    UF_CLEAR error code.
*/
static int example_uf_clear_pair (
    void
) {
    err = ask_rules();
    if (err) return err;
    /* Exclude same components */
    err = UF_CLEAR_set_exclude_rules(dataset,
        UF_CLEAR_EXCLUDE_WITHIN_COMP);
    if (err) return err;
    /* Exclude block and cone pair */
    err = UF_CLEAR_set_pair_exclusion(dataset,
        block_tag, cone_tag, "too far to interfere...");
    if (err) return err;
    /* Make sure sphere and block is included */
    err = UF_CLEAR_set_pair_inclusion(dataset,
        sphere_tag, block_tag, "just to be sure.");
    if (err) return err;
    err = ask_rules();
    if (err) return err;
    return 0;
}
/* cf: example_uf_clear_analysis() below */
static int ask_ca (
    void
) {
    int                     mode;
    UF_CLEAR_summary_t      summary;
    UF_CLEAR_interf_data_t  interf;
    tag_t                   obj1;
    tag_t                   obj2;
    tag_t                   dobj1;
    tag_t                   dobj2;
    time_t                  t;
    err = UF_CLEAR_ask_analysis_mode(dataset, &mode);
    if (err) return err;
    fprintf(stderr, "Clearance analysis mode is %d.\n", mode);
    err = UF_CLEAR_ask_results(dataset, &summary);
    if (err == UF_CLEAR_err_no_results)
        return 0;
    else if (err > 0)
        return err;
    else
    {
        /* fall through */
    }
    fprintf(stderr, "<<< Clearance Analysis Run Results >>>\n");
    t = (time_t) summary.start_time;
    fprintf(stderr, "-> Starting time: %s",
        asctime(gmtime((const time_t *) &t)));
    t = (time_t) summary.end_time;
    fprintf(stderr, "-> Ending time: %s",
        asctime(gmtime((const time_t *) &t)));
    fprintf(stderr, "-> Run length: %d seconds\n",
        summary.run_time);
    fprintf(stderr, "-> Run version: %d\n",
        summary.version);
    fprintf(stderr, "-> Number of object lists: %d\n",
        summary.num_lists);
    fprintf(stderr, "-> Number of objects in list #1: %d\n",
        summary.n_list1);
    fprintf(stderr, "-> Number of objects in list #2: %d\n",
        summary.n_list2);
    fprintf(stderr, "-> Number of pairs: %d\n",
        summary.n_pairs);
    fprintf(stderr, "-> Excluded pairs: %d\n",
        summary.excluded_pairs);
    fprintf(stderr, "---> Changed pairs: %d\n",
        summary.changed_pairs);
    fprintf(stderr, "---> Changed objects: %d\n",
        summary.changed_objs);
    fprintf(stderr, "-> Checked pairs: %d\n",
        summary.checked_pairs);
    fprintf(stderr, "---> New hard interferences: %d\n",
        summary.new_n_hard);
    fprintf(stderr, "---> New soft interferences: %d\n",
        summary.new_n_soft);
    fprintf(stderr, "---> New touching interferences: %d\n",
        summary.new_n_touching);
    fprintf(stderr, "---> New containment interferences: %d\n",
        summary.new_n_containment);
    fprintf(stderr, "---> Total # of new interferences: %d\n",
        summary.new_n_all_interf);
    fprintf(stderr, "-> Total # of hard interferences: %d\n",
        summary.n_hard);
    fprintf(stderr, "-> Total # of soft interferences: %d\n",
        summary.n_soft);
    fprintf(stderr, "-> Total # of touching interferences: %d\n",
        summary.n_touching);
    fprintf(stderr,
        "-> Total # of containment interferences: %d\n",
        summary.n_containment);
    fprintf(stderr, "-> Total number of interferences: %d\n",
        summary.n_all_interf);
    fprintf(stderr, "-> job_aborted?  Value is %d\n",
        summary.job_aborted);
    fprintf(stderr,
        "-> Total number of assembly zones (batch only): %d\n",
        summary.num_zones);
    fprintf(stderr, "<<< End of The Summary >>>\n");
    err = UF_CLEAR_count_interferences(dataset, &num);
    if (err) return err;
    fprintf(stderr, "Total number of interferences is %d.\n", num);
    if (num > 0)
    {
        obj1 = obj2 = dobj1 = dobj2 = NULL_TAG;
        /* Loop through all interferences */
        while (TRUE)
        {
            err = UF_CLEAR_ask_next_interf(dataset, &obj1, &obj2);
            if (err) return err;
            /* Normal exit */
            if (obj1 == NULL_TAG || obj2 == NULL_TAG) 
                break;
            /* Save first pair for manipulation */
            else if (dobj1 == NULL_TAG || dobj2 == NULL_TAG)
            {
                dobj1 = obj1;
                dobj2 = obj2;
            }
            else
            {
                /* fall through */
            }
            err = UF_CLEAR_ask_interf_data(dataset, obj1, obj2,
                &interf);
            if (err) return err;
            fprintf(stderr, "interf type is %d.\n", interf.type);
            fprintf(stderr, "new_interference is %s.\n",
                interf.new_interference ? "TRUE" : "FALSE");
            fprintf(stderr, "n_bodies is %d.\n", interf.n_bodies);
            fprintf(stderr, "interf_num is %d.\n",
                interf.interf_num);
            fprintf(stderr, "interf text is %s.\n", interf.text);
            if (interf.n_bodies > 0)
                UF_free(interf.interf_bodies);
        }
        /* Set text for first pair */
        err = UF_CLEAR_set_interf_text(dataset, dobj1, dobj2,
            "this pair's interf will be deleted next!");
        if (err) return err;
        /* Deleting first interference in above loop */
        err = UF_CLEAR_delete_interf(dataset, dobj1, dobj2);
        if (err) return err;
        /* Check the number of interferences now */
        err = UF_CLEAR_count_interferences(dataset, &num);
        if (err) return err;
        fprintf(stderr, "it is %d.\n", num);
    }
    return 0;
}
/*
  Name:
    example_uf_clear_analysis.
  Description:
    Show clearance analysis run routines.
  Return:
    0 for success; -1 for non-UF_CLEAR errors, or an
    UF_CLEAR error code.
*/
static int example_uf_clear_analysis (
    void
) {
    err = ask_ca();
    if (err) return err;
    /* Set analysis mode to quick facet */
    err = UF_CLEAR_set_analysis_mode(dataset,
        UF_CLEAR_QUICK_FACET);
    if (err) return err;
    /* Starting clearance analysis */
    err = UF_CLEAR_do_clearance_analysis(dataset);
    if (err) return err;
    err = ask_ca();
    if (err) return err;
    return 0;
}
/* cf: example_uf_clear_misc */
static int ask_misc (
    void
) {
    fprintf(stderr, "Query preferences.\n");
    err = UF_CLEAR_ask_preferences(dataset, &pref);
    if (err) return err;
    fprintf(stderr, "interactive_msg_filter is %d\n",
        pref.interactive_msg_filter);
    fprintf(stderr, "save_interference is %s\n",
        pref.save_interference ? "TRUE" : "FALSE");
    fprintf(stderr, "interference_layer is %d\n",
        pref.interference_layer);
    fprintf(stderr, "interference_color is %d\n",
        pref.interference_color);
    fprintf(stderr, "interf_attn_color is %d\n",
        pref.interf_attn_color);
    fprintf(stderr, "parent_attn_color is %d\n",
        pref.parent_attn_color);
    return 0;
}
/*
  Name:
    example_uf_clear_misc.
  Return:
    0 for success; -1 for non-UF_CLEAR errors, or an
    UF_CLEAR error code.
*/
static int example_uf_clear_misc (
    void
) {
    err = ask_misc();
    if (err) return err;
    /* Set new save_interference and interf_attn_color */
    pref.save_interference = FALSE;
    fprintf(stderr, "Set interf_attn_color to 10.\n");
    pref.interf_attn_color = 10;
    err = UF_CLEAR_set_preferences(dataset, pref);
    if (err) return err;
    err = ask_misc();
    if (err) return err;
    /* Deleting all clearance analysis data in the part */
    err = UF_CLEAR_delete_all(part_tag);
    if (err) return err;
    /* Count the number of datasets now */
    err = UF_CLEAR_count_datasets(part_tag, &num);
    if (err) return err;
    fprintf(stderr, "it is %d.\n", num);
    return 0;
}
