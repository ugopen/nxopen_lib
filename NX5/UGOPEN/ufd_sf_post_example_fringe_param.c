
/*============================================================================
                 Copyright (c)  2005 UGS Corp.
                     All Rights Reserved
============================================================================*/
/*****************************************************************************
**
** Example name:
** ufd_sf_post_example_fringe_param.c
**
** Description:
** An example demonstrating the use of the fringe parameter UGOPEN calls in
** UF_SF_POST. This example requires a SIM file with a result.
** Functions included here are:
**  1. UF_SF_POST_get_fringe_params
**  2. UF_SF_POST_initialise_fringe_params
**  3. UF_SF_POST_set_fringe_params
**
** Work Flow:
**  1. Initialize Post processor
**  2. Get current fringe params
**  3. Change necessary fringe param members
**  4. Quit postprocessor
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
    UF_SF_POST_fringe_t  curr_fringe_params, *new_fringe_params = NULL;


    /* ufd_sf_post_example_fringe_param starts here */
    sprintf(buffer_g, "Executing ufd_sf_post_example_fringe_param.c ...\n");
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
    /* Initialize post processor test */
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

    /* Get the current fringe display settings test */
/**/

    UF_CALL(UF_SF_POST_get_fringe_params(&curr_fringe_params));

    /* Print the current fringe settings to the listing window*/
    sprintf(buffer_g, "Current MODEL FRINGE settings:\n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of fringe style = %d\n", curr_fringe_params.style);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of color spectrum = %d\n", curr_fringe_params.spec);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of scale spectrum = %d\n", curr_fringe_params.fringe_scale);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Whole model threshold switch = %s\n", curr_fringe_params.whole_sw ? "TRUE" : "FALSE");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Threshold value maximum limit = %lf\n", curr_fringe_params.threshold_max);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Threshold value minimum limit = %lf\n", curr_fringe_params.threshold_min);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "No of colors used = %d\n", curr_fringe_params.colors_used);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Translucency switch = %s\n", curr_fringe_params.trans_sw ? "TRUE" : "FALSE");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of legend option = %d\n", curr_fringe_params.legend);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Threshold switch = %s\n", curr_fringe_params.thresh_sw ? "TRUE" : "FALSE");
    uf_write_listing_window(buffer_g);

/**/

    /* Initialise the fringe display settings to the user ones */
    curr_fringe_params.style = UF_SF_POST_FRINGE_CONTOUR_BANDS;
    curr_fringe_params.spec = UF_SF_POST_FRINGE_COLOR_TEMP;
    curr_fringe_params.fringe_scale = UF_SF_POST_FRINGE_SCALE_AUTOMATIC;
    curr_fringe_params.colors_used = 10;
    curr_fringe_params.legend = UF_SF_POST_FRINGE_LEGEND_COLOR;

/**/

    UF_CALL(UF_SF_POST_initialise_fringe_params(&new_fringe_params, curr_fringe_params.style, curr_fringe_params.spec, curr_fringe_params.fringe_scale, curr_fringe_params.whole_sw, curr_fringe_params.threshold_max, curr_fringe_params.threshold_min, curr_fringe_params.colors_used, curr_fringe_params.trans_sw, curr_fringe_params.legend, curr_fringe_params.thresh_sw));

    sprintf(buffer_g, "\nChanged MODEL FRINGE settings:\n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of fringe style = %d\n", new_fringe_params->style);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of color spectrum = %d\n", new_fringe_params->spec);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of scale spectrum = %d\n", new_fringe_params->fringe_scale);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Whole model threshold switch = %s\n", new_fringe_params->whole_sw ? "TRUE" : "FALSE");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Threshold value maximum limit = %lf\n", new_fringe_params->threshold_max);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Threshold value minimum limit = %lf\n", new_fringe_params->threshold_min);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "No of colors used = %d\n", new_fringe_params->colors_used);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Translucency switch = %s\n", new_fringe_params->trans_sw ? "TRUE" : "FALSE");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of legend option = %d\n", new_fringe_params->legend);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Threshold switch = %s\n", new_fringe_params->thresh_sw ? "TRUE" : "FALSE");
    uf_write_listing_window(buffer_g);

/**/

    /* Set the new user fringe parameters */
/**/

    UF_CALL(UF_SF_POST_set_fringe_params(&curr_fringe_params));

/**/

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
    if(new_fringe_params)
        free(new_fringe_params);

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
