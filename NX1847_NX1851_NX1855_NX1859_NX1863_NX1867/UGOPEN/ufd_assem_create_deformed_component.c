
/*===================================================================

        Copyright (c) 2002-2007 UGS Inc.
                     Unpublished - All rights reserved

===================================================================*/

/*****************************************************************************
 *
 * DESCRIPTION -
 *   This program shows how to use the following UG/Open API routine(s):
 *
 *          UF_ASSEM_create_deformable_part
 *          UF_ASSEM_ask_deformable_definition_data
 *          UF_ASSEM_ask_deformable_definition
 *          UF_ASSEM_deform_part
 *          UF_ASSEM_ask_deformed_definition_data
 *          UF_ASSEM_is_part_deformable
 *          UF_ASSEM_ask_all_deformations_of_part_occ
 *          UF_ASSEM_ask_current_deformation_of_part_occ
 *          UF_ASSEM_ask_deformed_definition_of_part_occurrence
 *
 *
 * PROGRAM DESCRIPTION -
 *   The following example creates a cube and then moves it into a new
 *   component part, then defines the cube part as deformable.
 *   Then cube part is defomed in the assembly part "deformed block".
 *

 *
 ******************************************************************************/

/*==============================================================================
 TEXT ENCLOSED within delete markers will be REMOVED
=============================================================================*/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_obj.h>
#include <uf_assem.h>
#include <uf_object_types.h>

#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))

static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133],
             msg[133];

        sprintf(msg, "*** ERROR code %d at line %d in %s:\n+++ ",
            irc, line, file);
        UF_get_fail_message(irc, err);

    /*  NOTE:  UF_print_syslog is new in V18 */

        UF_print_syslog(msg, FALSE);
        UF_print_syslog(err, FALSE);
        UF_print_syslog("\n", FALSE);
        UF_print_syslog(call, FALSE);
        UF_print_syslog(";\n", FALSE);

        if (!UF_UI_open_listing_window())
        {
            UF_UI_write_listing_window(msg);
            UF_UI_write_listing_window(err);
            UF_UI_write_listing_window("\n");
            UF_UI_write_listing_window(call);
            UF_UI_write_listing_window(";\n");
        }
    }

    return(irc);
}

#define WRITE_L(X) (write_logical_to_listing_window(#X, X))

static void write_logical_to_listing_window(char *title, logical flag)
{
    char
        msg[UF_UI_MAX_STRING_BUFSIZE];

    UF_CALL(UF_UI_open_listing_window());
    if (flag)
        sprintf(msg, "%s = TRUE\n", title);
    else
        sprintf(msg, "%s = FALSE\n", title);
    UF_CALL(UF_UI_write_listing_window(msg));
}

#define WRITE_D(X) (write_integer_to_listing_window(#X, X))

static void write_integer_to_listing_window(char *title, int n)
{
    char
        msg[UF_UI_MAX_STRING_BUFSIZE];

    UF_CALL(UF_UI_open_listing_window());
    sprintf(msg, "%s = %d\n", title, n);
    UF_CALL(UF_UI_write_listing_window(msg));
}

static tag_t ask_next_feature(tag_t part, tag_t feat)
{
    while (!UF_CALL(UF_OBJ_cycle_objs_in_part(part, UF_feature_type, &feat))
        && (feat != NULL_TAG))
        if (UF_OBJ_ask_status(feat) == UF_OBJ_ALIVE) return feat;

    return NULL_TAG;
}

static int allocate_memory(unsigned int nbytes, void **where)
{
    int
        resp;

    *where = UF_allocate_memory(nbytes, &resp);

    return resp;
}

static int make_an_array(uf_list_p_t *object_list, tag_t **objects)
{
    int
        ii,
        n;
    uf_list_p_t
        temp;

    UF_CALL(UF_MODL_ask_list_count(*object_list, &n));

    UF_CALL(allocate_memory(n * sizeof(tag_t), (void **)objects));

    for (ii = 0, temp = *object_list; ii < n; temp = temp->next, ii++)
        (*objects)[ii] = temp->eid;

    UF_CALL(UF_MODL_delete_list(object_list));

    return n;
}

static int ask_all_features(tag_t part, tag_p_t *feats)
{
    tag_t
        feat = NULL_TAG;
    uf_list_p_t
        feat_list;

    UF_CALL(UF_MODL_create_list(&feat_list));

    while ((feat = ask_next_feature(part, feat)) != NULL_TAG)
        UF_CALL(UF_MODL_put_list_item(feat_list, feat));

    return (make_an_array(&feat_list, feats));
}

static void create_deformed_definition( UF_MODL_udfs_def_data_p_t *udf_data   )
{

    UF_MODL_udfs_exp_p_t exp_data=   ( UF_MODL_udfs_exp_p_t )NULL;
    int num_exps;
    tag_t work_part = UF_ASSEM_ask_work_part();
    int inx;
    logical found_exp=false;
    tag_t *exps=( tag_t * )NULL;
    int error_code;

    *udf_data = ( UF_MODL_udfs_def_data_p_t) UF_allocate_memory( 1 * sizeof( UF_MODL_udfs_def_data_t ), &error_code  );

    (*udf_data)->exp_defs = (UF_MODL_udfs_exp_p_t *)UF_allocate_memory( 1 * sizeof( UF_MODL_udfs_exp_p_t ), &error_code );

    exp_data =  ( UF_MODL_udfs_exp_p_t ) UF_allocate_memory( 1 * sizeof( UF_MODL_udfs_exp_t ), &error_code  );

    (*udf_data)->exp_defs[0] = exp_data;
    (*udf_data)->num_ref = 0;
    (*udf_data)->explosion_flag = false;
    (*udf_data)->num_exp = 0;

    (*udf_data)->num_frecs = ask_all_features(work_part, &((*udf_data)->frecs) );

    UF_MODL_ask_exps_of_part( work_part, &num_exps, &exps );

    for ( inx = 0 ; inx < num_exps && !found_exp; inx ++ )
    {
        tag_t exp_tag=NULL_TAG;
        char *string=( char * )NULL;
        char *exp_name=( char * )NULL, *exp_rhs=( char * )NULL;
        UF_MODL_ask_exp_tag_string( exps[inx], &string );
        UF_MODL_dissect_exp_string( string, &exp_name, &exp_rhs, &exp_tag );

        if( strcmp( exp_name, "p1" ) == 0 )
        {
            char old_string[256];
            int error;
            strcpy( old_string, "p1=3.2" );
            exp_data->exp = ( char * ) UF_allocate_memory( sizeof( old_string ) *
                sizeof ( char ), &error );
            strcpy( exp_data->exp_name, "HEIGHT" );
            strcpy( exp_data->exp, old_string );
            exp_data->type = UF_UDFS_EXP;
            exp_data->num_def = 1;
            found_exp = true;
        }
        UF_free( exp_name );
        UF_free( exp_rhs );
        UF_free( string );

    }

    UF_free( exps );

    if( found_exp )
    {
        (*udf_data)->exp_defs[0]= exp_data;
        (*udf_data)->num_exp = 1;

    }
}

static void do_it(void)
{
    double origin[3] = {0.0, 0.0, 0.0};
    double add_component_origin[3] = {5.0, 20.0, 0.0};
    double csys[6] = {1.0, 0.0, 0.0,
                      0.0, 1.0, 0.0};
    double corner_pts[3] = {5.0, 2.0, 0.0};

    char *edge_lens[3] = {"1.0", "3.2", "1.5"};
    tag_t feature;
    tag_t work_part;
    tag_t instance;
    int units;
    UF_ASSEM_deform_data_t deformable_data;
    UF_MODL_udfs_def_data_p_t udf_data;
    tag_t deformed_feature = NULL_TAG;
    tag_t block, root_part_occ, part_occ;
    int num_part_occs;
    tag_t *all_part_occs;
    tag_t deformable_feature;
    tag_t exp_tag, old_exps[1];
    UF_ASSEM_deform_data_t deform_data;
    UF_ASSEM_deformed_definition_data_t deformed_data;
    logical is_deformable;
    char * rhs, *lhs ;
    UF_ASSEM_deform_part_data_t d_data;
    int error;
    char rhs_string[256];
    const char *null_string = ( const char* )NULL;
    tag_t root_part;
    UF_PART_load_status_t load_status;

    UF_ASSEM_deform_part_warnings_t warnings;

    UF_CALL(UF_ASSEM_init_deform_part_data( &d_data ));

    if (UF_CALL(UF_MODL_create_block1(UF_NULLSIGN, corner_pts, edge_lens, &feature)))
        return;

    if (UF_CALL(UF_MODL_ask_feat_body(feature, &block ))) return;

    work_part = UF_ASSEM_ask_work_part();
    UF_PART_ask_units(work_part, &units);

    if (UF_CALL(UF_ASSEM_create_component_part(work_part, "deformed_block.prt",
        null_string, null_string, units, 0, origin, csys, 1, &block, &instance))) return;

    is_deformable =  UF_ASSEM_is_part_deformable ( work_part );
    WRITE_L(is_deformable);

    deformable_data.part_occ = NULL_TAG;

    UF_CALL(UF_ASSEM_set_work_part( UF_PART_ask_part_tag( "deformed_block.prt" ) ));

    create_deformed_definition( &udf_data );

    deformable_data.udfs_data = udf_data;

    deformable_data.help_url_string = "TEST DEFORM";

    UF_CALL(UF_ASSEM_create_deformable_part( &deformable_data, &deformed_feature ));

    UF_free(udf_data->frecs);
    UF_free(udf_data->exp_defs[0]->exp);
    UF_free(udf_data->exp_defs[0]);
    UF_free(udf_data->exp_defs);
    UF_free(udf_data);

    UF_CALL(UF_ASSEM_set_work_part( work_part ));

    num_part_occs = UF_ASSEM_ask_part_occs_of_inst( instance, &all_part_occs  );
    WRITE_D(num_part_occs);

    root_part  = UF_ASSEM_ask_prototype_of_occ( all_part_occs[0] );

    root_part_occ = UF_ASSEM_ask_root_part_occ( root_part);

    part_occ = UF_ASSEM_ask_part_occ_of_inst( root_part_occ, instance );

    UF_CALL(UF_ASSEM_ask_deformable_definition(UF_PART_ask_part_tag("deformed_block.prt"),
        &deformable_feature ));

    UF_CALL(UF_ASSEM_ask_deformable_definition_data( deformable_feature, &deform_data ));

    /*
        Do this to get the old expression tag.
    */
    UF_CALL(UF_ASSEM_set_work_part( UF_PART_ask_part_tag( "deformed_block.prt" ) ));

    /*
        This requires the work part be set to the part that has the old expressions.
    */
    UF_CALL(UF_MODL_dissect_exp_string( deform_data.udfs_data->exp_defs[0]->exp, &lhs,
        &rhs, &exp_tag ));

    UF_CALL(UF_ASSEM_set_work_part( work_part ));

    old_exps[0] = exp_tag;
    UF_free( lhs );
    UF_free( rhs );

    d_data.convert_units_on_modified_parts = false;
    d_data.convert_units_on_read_only_modified_parts = false;
    d_data.part_occ_to_deform = part_occ;
    d_data.num_parents = 0;
    d_data.old_parents = 0;
    d_data.new_parents = 0;
    d_data.num_expressions = 1;
    d_data.old_expressions = old_exps;
    d_data.deformed_feature_tag = NULL_TAG;

    warnings.num_warnings = 0;
    warnings.warning_codes = 0;
    warnings.warning_strings = 0;

    strcpy( rhs_string, "1");

    d_data.new_expression_values = ( const char ** ) UF_allocate_memory( sizeof( char * ) *   1, &error );
    d_data.new_expression_values[0]  = rhs_string;

    UF_CALL(UF_ASSEM_deform_part( &d_data, &warnings ));

    UF_CALL(UF_ASSEM_free_deform_warnings_data( &warnings ));
    UF_free(d_data.new_expression_values);

    /*
        Gets the deformed feature for the display part deformation
    */
    UF_CALL(UF_ASSEM_ask_displayed_deformation_of_part_occ( part_occ, &deformed_feature ));

    /*
       Add deformable component into the existing assembly work part
    */
    UF_CALL(UF_ASSEM_add_part_to_assembly(work_part, "deformed_block.prt", null_string,
        null_string,  add_component_origin, csys, 1, &instance, &load_status ));

    part_occ = UF_ASSEM_ask_part_occ_of_inst(root_part_occ, instance);
    UF_CALL(UF_ASSEM_ask_deformable_definition( UF_ASSEM_ask_prototype_of_occ(
        part_occ), &deformable_feature ));

    UF_CALL(UF_ASSEM_ask_deformed_definition_data( deformable_feature, &deformed_data ));

    UF_CALL(UF_ASSEM_init_deform_part_data(&d_data));

    d_data.part_occ_to_deform = part_occ;
    d_data.num_expressions = 1;
    d_data.old_expressions = deformed_data.expressions;

    strcpy( rhs_string, "5");

    d_data.new_expression_values =
        ( const char ** ) UF_allocate_memory( sizeof( char * ) *   1, &error );
    d_data.new_expression_values[0]  = rhs_string;

    UF_CALL(UF_ASSEM_deform_part( &d_data, NULL));
    UF_free(d_data.new_expression_values);
}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
{
    if (UF_CALL(UF_initialize())) return;
    do_it();
    UF_terminate();
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
