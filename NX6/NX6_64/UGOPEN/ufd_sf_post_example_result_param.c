
/*============================================================================
                 Copyright (c)  2005 UGS Corp.
                     All Rights Reserved
============================================================================*/
/*****************************************************************************
**
** Example name:
** ufd_sf_post_example_result_param.c
**
** Description:
** An example demonstrating the use of the result parameter UGOPEN calls in
** UF_SF_POST. This example requires a SIM file with a result.
** Functions included here are:
**  1. UF_SF_POST_get_result_params
**  2. UF_SF_POST_initialise_result_parms
**  3. UF_SF_POST_select_results
**  4. UF_SF_POST_get_deformed_results
**  5. UF_SF_POST_initialise_deformed_result_params
**  6. UF_SF_POST_select_deformed_results
**
** Work Flow:
**  1. Initialize Post processor
**  2. Get current result params
**  3. Change necessary result param members
**  4. Get current deformed result params
**  5. Change necessary deformed result param members
**  6. Quit postprocessor
**
******************************************************************************
//
*/


/* C Include files */
#include <stdio.h>
#include <stdlib.h>

/* UGOPEN include files */
#include <uf.h>
#include <uf_cfi_types.h>
#include <uf_part.h>
#include <uf_sf.h>
#include <uf_sf_post_datatypes.h>
#include <uf_retiring.h>
#include <uf_retiring_ugopenint.h>
#include <uf_ui.h>
#include <uf_ui_types.h>
#include <uf_unit_types.h>

/* Macro definitions */
#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))

/* Global variables [*_g] */
char buffer_g[UF_UI_MAX_STRING_LEN+1];
int  response_g;
logical is_post_initialized_g = false;
logical lresponse_g;
/**/

/* Customized Write Listing Window function */
static void uf_write_listing_window(const char *mesg)
{
    UF_UI_is_listing_window_open(&lresponse_g);
    if(!lresponse_g)
        UF_UI_open_listing_window();

    UF_UI_write_listing_window(mesg);
}

/* Error wrapper function */
static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133],
             msg[133];

        sprintf(msg, "*** ERROR code %d at line %d in %s:\n+++ ",
            irc, line, file);
        UF_get_fail_message(irc, err);

        UF_print_syslog(msg, FALSE);
        UF_print_syslog(err, FALSE);
        UF_print_syslog("\n", FALSE);
        UF_print_syslog(call, FALSE);
        UF_print_syslog(";\n", FALSE);

        uf_write_listing_window(msg);
        uf_write_listing_window(err);
        uf_write_listing_window("\n");
        uf_write_listing_window(call);
        uf_write_listing_window(";\n");

        UF_UI_close_listing_window();

        if(is_post_initialized_g)
        {
            UF_SF_POST_quit_post_processor();
            is_post_initialized_g = false;
        }

/**/
    }

    return irc;
}

/**/

/* UGOPEN main user function */
static void do_ugopen_api(void)
{
    int test_count = 0;
    tag_t part_tag;
    UF_SF_POST_result_parms_t curr_res_param, *new_res_param = NULL;
    UF_SF_post_deform_result_t def_res_param, new_def_res_param;


    /* ufd_sf_post_example_result_param starts here */
    sprintf(buffer_g, "Executing ufd_sf_post_example_result_param.c ...\n");
    uf_write_listing_window(buffer_g);

/**/

    /* Make sure you have a SIM part */
    part_tag =  UF_PART_ask_display_part();
    if(part_tag == NULL_TAG || !UF_SF_is_simulation(part_tag))
    {
        sprintf(buffer_g, "%s", part_tag ? "Part loaded is NOT a simulation part!"
                                        : "There is no part loaded * in the active UG window!");
        uc1601(buffer_g, 1);
        uf_write_listing_window(buffer_g);
        strcat(buffer_g, "\n");

        sprintf(buffer_g, "Ending ...\n");
        uc1601(buffer_g, 1);
        strcat(buffer_g, "\n\n\n");
        uf_write_listing_window(buffer_g);

        UF_UI_close_listing_window();
/**/

        return;
    }


    /* We assume the SIM has a results file */
    /* Initialize post processor */
    if(UF_CALL(UF_SF_POST_initialize_post_processor()))
    {
        sprintf(buffer_g, "Possibility of a missing/corrupt * result file in SIM part directory ...\n");
        uc1601(buffer_g, 1);
        strcat(buffer_g, "\n\n\n");
        uf_write_listing_window(buffer_g);

        UF_UI_close_listing_window();
/**/
        return;
    }
    is_post_initialized_g = true;

    /* Get current post processor results test */
/**/

    UF_CALL(UF_SF_POST_get_result_params(&curr_res_param));

    /* Print the current settings to the listing window */
    sprintf(buffer_g, "Current MODEL POST PROCESSOR settings:\n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Results are requested in absolute coords = %d\n", curr_res_param.abs_sw);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Results are requested in average case = %d\n", curr_res_param.avg_sw);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Load Case number = %d\n", curr_res_param.lcase);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Optimization iteration = %d\n", curr_res_param.iter);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Scale to display results = %lf\n", curr_res_param.scale);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of coordinate system = %d\n", curr_res_param.coords);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Component to the result type to set = %d\n", curr_res_param.comp);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Units tag set = %d\n", curr_res_param.units_tag);
    uf_write_listing_window(buffer_g);

/**/

    /* Initialise the necessary members of curr_res_param */
    curr_res_param.res_type.quan = UF_SF_POST_APPLIED_FORCE;
    curr_res_param.res_type.lay = UF_SF_POST_AT_MID;
    curr_res_param.res_type.loc = UF_SF_POST_AT_NODES;
    curr_res_param.comp = UF_SF_POST_COMP_MAG;

/**/

    UF_CALL(UF_SF_POST_initialise_result_parms(&new_res_param, curr_res_param.abs_sw, curr_res_param.avg_sw, curr_res_param.lcase, curr_res_param.iter, curr_res_param.scale, curr_res_param.coords, curr_res_param.res_type.quan, curr_res_param.res_type.lay, curr_res_param.comp, curr_res_param.units_tag));

/**/

    /* Get unit tag */
    if((curr_res_param.units_tag = UF_SF_POST_get_unit_tag(UF_SF_POST_APPLIED_FORCE, UF_UNIT_FORCE_N)) == NULL_TAG)
    {
        UF_CALL(UF_UI_close_listing_window());
        UF_CALL(UF_SF_POST_quit_post_processor());
/**/
        return;
    }

    /* Select the changed param and set as the result test */
/**/

    UF_CALL(UF_SF_POST_select_results(new_res_param));

    /* Print the changed settings to the listing window */
    sprintf(buffer_g, "Changed MODEL POST PROCESSOR settings:\n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Results are requested in absolute coords = %d\n", new_res_param->abs_sw);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Results are requested in average case = %d\n", new_res_param->avg_sw);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Load Case number = %d\n", new_res_param->lcase);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Optimization iteration = %d\n", new_res_param->iter);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Scale to display results = %lf\n", new_res_param->scale);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of coordinate system = %d\n", new_res_param->coords);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Component to the result type to set = %d\n", new_res_param->comp);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Units tag set = %d\n", new_res_param->units_tag);
    uf_write_listing_window(buffer_g);

/**/

    /* Update display */
    UF_CALL(UF_SF_POST_display_results());
    uc1601("Pause", 1);

    /* Get current deformed result params test */
/**/

    UF_CALL(UF_SF_POST_get_deformed_results(&def_res_param));

    /* Print the current settings to the listing window */
    sprintf(buffer_g, "Current MODEL DEFORMED RESULT settings:\n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Loadcase selected = %d\n", def_res_param.loadcase);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Iteration Selected = %d\n", def_res_param.iteration);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Result Type Parameter = %d\n", def_res_param.res_type.quan);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Result Type Parameter for Layer = %d\n", def_res_param.res_type.lay);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Deformation scaling value = %lf\n", def_res_param.scaling_value);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Deformation value choice = %d\n", def_res_param.scaling_choice);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Undeformation choice = %d\n", def_res_param.undef_toggle);

/**/

    /* Initialise the necessary members of def_res_param */
    def_res_param.scaling_value = 1000000;
    def_res_param.scaling_choice = 1;
    def_res_param.undef_toggle = 1;

/**/

    UF_CALL(UF_SF_POST_initialise_deformed_result_params(&new_def_res_param, def_res_param.loadcase, def_res_param.iteration, def_res_param.res_type.quan, def_res_param.res_type.lay, def_res_param.scaling_value, def_res_param.scaling_choice, def_res_param.undef_toggle));

/**/


    /* Get current deformed result params test */
/**/

    UF_CALL(UF_SF_POST_select_deformed_results(&def_res_param));

    /* Print the changed settings to the listing window */
    sprintf(buffer_g, "Changed MODEL DEFORMED RESULT settings:\n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Loadcase selected = %d\n", new_def_res_param.loadcase);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Iteration Selected = %d\n", new_def_res_param.iteration);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Result Type Parameter = %d\n", new_def_res_param.res_type.quan);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Result Type Parameter for Layer = %d\n", new_def_res_param.res_type.lay);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Deformation scaling value = %lf\n", new_def_res_param.scaling_value);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Deformation value choice = %d\n", new_def_res_param.scaling_choice);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Undeformation choice = %d\n", new_def_res_param.undef_toggle);

/**/

    /* Update display */
    UF_CALL(UF_SF_POST_display_results());
    uc1601("Pause", 1);

    /* Last test */
    /* Quit post processor test */
    UF_CALL(UF_SF_POST_quit_post_processor());

    /* Pause for a user input */
    sprintf(buffer_g, "Ending ...\n");
    uc1601(buffer_g, 1);
    strcat(buffer_g, "\n\n\n");
    uf_write_listing_window(buffer_g);

    UF_UI_close_listing_window();
/**/
    if(new_res_param)
        free(new_res_param);

    return;
}


/*****************************************************************************
**  Activation Methods
*****************************************************************************/
/*  Explicit Activation
**  This entry point is used to activate the application explicitly, as in
**  "File->Execute UG/Open->User Function..." */
extern DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
    /* Initialize the API environment */
    if( UF_CALL(UF_initialize()) )
    {
        /* Failed to initialize */
        return;
    }

    /* TODO: Add your application code here */
    do_ugopen_api();

    /* Terminate the API environment */
    UF_CALL(UF_terminate());
}

/*****************************************************************************
**  Utilities
*****************************************************************************/

/* Unload Handler
** This function specifies when to unload your application from Unigraphics.
*/
extern int ufusr_ask_unload( void )
{
    return( UF_UNLOAD_IMMEDIATELY );
}
