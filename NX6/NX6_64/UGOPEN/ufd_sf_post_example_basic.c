
/*============================================================================
                 Copyright (c)  2005 UGS Corp.
                     All Rights Reserved
============================================================================*/
/*****************************************************************************
**
** Example name:
** ufd_sf_post_example_basic.c
**
** Description:
** An example demonstrating the use of the basic UGOPEN calls in UF_SF_POST.
** This example requires a SIM file with a result.
** Functions included here are:
**  1. UF_SF_POST_initialize_post_processor
**  2. UF_SF_POST_quit_post_processor
**  3. UF_SF_POST_get_unit_tag
**  4. UF_SF_POST_get_component_unit_tag
**  5. UF_SF_POST_display_results
**  6. UF_SF_POST_save_template
**  7. UF_SF_POST_apply_template
**
** Work Flow:
**  1. Initialize Post processor
**  2. Get current results from loaded SIM file
**  3. Save template
**  4. Get the appropriate unit to be set for the new params using unit_tag
**  5. Change necessary params
**  6. Apply changes and refresh
**  7. Apply back the old template
**  8. Quit postprocessor
**
******************************************************************************

*/

/* C Include files */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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
/* */


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

/* */
    }

    return irc;
}
/* */

/*  UGOPEN main user function */
static void do_ugopen_api(void)
{
    char xml_filename[UF_CFI_MAX_PATH_NAME_SIZE], name_text_data[UF_CFI_MAX_FILE_NAME_LEN];
    char *ptr;
    char *data_string = NULL;
    int test_count = 0;
    int post_view_id;
    int use_icon;
    int is_default;

    tag_t                      part_tag;
    UF_SF_POST_template_type_t template_type;
    UF_SF_POST_result_parms_t  curr_res_param;



    /* ufd_sf_post_example_basic starts here */
    sprintf(buffer_g, "Executing ufd_sf_post_example_basic.c ...\n");
    uf_write_listing_window(buffer_g);

/* */

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
/* */
        return;
    }


    /* We assume the SIM has a results file */
    /* Initialize post processor test */
/* */

    if(UF_CALL(UF_SF_POST_initialize_post_processor()))
    {
        sprintf(buffer_g, "Possibility of a missing/corrupt * result file in SIM part directory ...\n");
        uc1601(buffer_g, 1);
        strcat(buffer_g, "\n\n\n");
        uf_write_listing_window(buffer_g);

        UF_UI_close_listing_window();
/* */
        return;
    }
    is_post_initialized_g = true;

/*  */

    /* Get current post processor results test */
/* */

    UF_CALL(UF_SF_POST_get_result_params(&curr_res_param));

    /* Print the current settings to the listing window */
    sprintf(buffer_g, "\nCurrent MODEL POST PROCESSOR settings:\n");
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
    /* */


    /* Get the template directory path */
    UF_CALL(UF_translate_variable("UGII_CAE_POST_TEMPLATE_USER_DIR", &ptr));
    sprintf(buffer_g, "Saving template at path = %s\n", ptr);
    uf_write_listing_window(buffer_g);

    /* Save template test */
/* */
    template_type = UF_SF_POST_TEMPLATE_TYPE_POSTVIEW;
    strcpy(name_text_data, ptr);
    strcat(name_text_data, "\\TEMPLATE_NAME_TEST");
    strcpy(xml_filename, name_text_data);
    strcat(xml_filename, ".xml");
    use_icon = 1;
    is_default = 0;
    /* Passing 0 as second argument as it is to be deprecated soon */
    post_view_id = 0;
    UF_CALL(UF_SF_POST_save_template(template_type, post_view_id, xml_filename, name_text_data, use_icon, is_default));

/* */

    /* Change the necessary members of curr_res_param */
    /* Let us investigate the COMPonent_X of the APPLIED FORCEs at the MIDdle of the NODES */
    curr_res_param.res_type.quan = UF_SF_POST_APPLIED_FORCE;
    curr_res_param.res_type.lay = UF_SF_POST_AT_MID;
    /*curr_res_param.res_type.loc = UF_SF_POST_AT_NODES; */
    curr_res_param.comp = UF_SF_POST_COMP_X;

    /* Get unit tag test */
/* */

    if((curr_res_param.units_tag = UF_SF_POST_get_unit_tag(UF_SF_POST_APPLIED_FORCE, UF_UNIT_FORCE_N)) == NULL_TAG)
    {
        UF_CALL(UF_UI_close_listing_window());
        UF_CALL(UF_SF_POST_quit_post_processor());
/* */
        return;
    }

/* */
    sprintf(buffer_g, "Units tag set = %d\n", curr_res_param.units_tag);
    uf_write_listing_window(buffer_g);


    /* Print the current settings to the listing window */
    sprintf(buffer_g, "Changed MODEL POST PROCESSOR settings:\n");
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

    /* Display post processor test */
/* */

    UF_CALL(UF_SF_POST_display_results());

/* */


    /* Apply template test */
/* */

    UF_CALL(UF_SF_POST_apply_template(name_text_data));

/* */

    /* Update display */
    UF_CALL(UF_SF_POST_display_results());
    uc1601("Pause", 1);

    /* Last test */
    /* Quit post processor test */
/* */

    UF_CALL(UF_SF_POST_quit_post_processor());

/*  */

    /* Pause for a user input */
    sprintf(buffer_g, "Ending ...\n");
    uc1601(buffer_g, 1);
    strcat(buffer_g, "\n\n\n");
    uf_write_listing_window(buffer_g);

    UF_UI_close_listing_window();
/*  */

    return;
}


/*****************************************************************************
**  Activation Methods
*****************************************************************************/
/*  Explicit Activation
**  This entry point is used to activate the application explicitly, as in
**  "File->Execute UG/Open->User Function..."
*/
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
