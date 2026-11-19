
/*============================================================================
                 Copyright (c)  2005 UGS Corp.
                     All Rights Reserved
============================================================================*/
/*****************************************************************************
**
** Example name:
** ufd_sf_post_example_clip_param.c
**
** Description:
** An example demonstrating the use of the clip parameter UGOPEN calls in
** UF_SF_POST. This example requires a SIM file with a result.
** Functions included here are:
**  1. UF_SF_POST_get_clipping
**  2. UF_SF_POST_initialise_def_disp_params
**  3. UF_SF_POST_set_clipping
**
** Work Flow:
**  1. Initialize Post processor
**  2. Get current clip params
**  3. Change necessary clip param members
**  4. Quit postprocessor
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
    UF_SF_post_clipping_data_t clip_params, *new_clip_params;


    /* ufd_sf_post_example_clip_param starts here */
    sprintf(buffer_g, "Executing ufd_sf_post_example_clip_param.c ...\n");
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

    /* Get clip params test */
/**/

    UF_CALL(UF_SF_POST_get_clipping(&clip_params));

/**/

    sprintf(buffer_g, "Current clip param settings: \n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Clip toggle = %d\n", clip_params.clip_tgl_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Ghost model toggle = %d\n", clip_params.ghost_tgl_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Outline model toggle = %d\n", clip_params.outline_tgl_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Auto update toggle = %d\n", clip_params.auto_update_tgl_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of clip plane = %d\n", clip_params.plane_type_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Clip side data = %d\n", clip_params.clip_side_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Distance along the axis = %lf\n", clip_params.clip_value_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Clip scale toggle = %d\n", clip_params.clip_scale_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Clip Scaling minimum = %lf\n", clip_params.clip_scale_curr_min);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Clip Scaling maximum = %lf\n", clip_params.clip_scale_curr_max);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Scaling minimum = %lf\n", clip_params.scale_min);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Scaling maximum = %lf\n", clip_params.scale_max);
    uf_write_listing_window(buffer_g);

    /* Initialise clip params test */
    new_clip_params = NULL;
    clip_params.clip_tgl_data = 1;
    clip_params.ghost_tgl_data = 0;
    clip_params.outline_tgl_data = 0;
    clip_params.auto_update_tgl_data = 0;
    clip_params.plane_type_data = UF_SF_CLIP_ABS_YZ;
    clip_params.clip_side_data = UF_SF_CLIP_NEGATIVE;
    clip_params.clip_value_data = 50.0;
    clip_params.clip_scale_data = 1;
    clip_params.clip_scale_curr_min = 0;
    clip_params.clip_scale_curr_max = 100;
    clip_params.scale_min = 1.;
    clip_params.scale_max = 1.;
    UF_CALL(UF_SF_POST_initialise_clip_params(&new_clip_params, clip_params.clip_tgl_data, clip_params.ghost_tgl_data, clip_params.outline_tgl_data, clip_params.auto_update_tgl_data, clip_params.plane_type_data, clip_params.clip_side_data, clip_params.clip_value_data, clip_params.clip_scale_data, clip_params.clip_scale_curr_min, clip_params.clip_scale_curr_max, clip_params.scale_min, clip_params.scale_max));

/**/

    sprintf(buffer_g, "Changed clip param settings: \n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Clip toggle = %d\n", new_clip_params->clip_tgl_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Ghost model toggle = %d\n", new_clip_params->ghost_tgl_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Outline model toggle = %d\n", new_clip_params->outline_tgl_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Auto update toggle = %d\n", new_clip_params->auto_update_tgl_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of clip plane = %d\n", new_clip_params->plane_type_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Clip side data = %d\n", new_clip_params->clip_side_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Distance along the axis = %lf\n", new_clip_params->clip_value_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Clip scale toggle = %d\n", new_clip_params->clip_scale_data);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Clip Scaling minimum = %lf\n", new_clip_params->clip_scale_curr_min);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Clip Scaling maximum = %lf\n", new_clip_params->clip_scale_curr_max);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Scaling minimum = %lf\n", new_clip_params->scale_min);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Scaling maximum = %lf\n", new_clip_params->scale_max);
    uf_write_listing_window(buffer_g);

    /* Set clip params test */
/**/

    UF_CALL(UF_SF_POST_set_clipping(new_clip_params));

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
