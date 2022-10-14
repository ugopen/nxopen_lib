
/*============================================================================
                 Copyright (c)  2005 UGS Corp.
                     All Rights Reserved
============================================================================*/
/*****************************************************************************
**
** Example name:
** ufd_sf_post_example_disp_param.c
**
** Description:
** An example demonstrating the use of the display parameter UGOPEN calls in
** UF_SF_POST. This example requires a SIM file with a result.
** Functions included here are:
**  1. UF_SF_POST_get_def_disp_params
**  2. UF_SF_POST_initialise_def_disp_params
**  3. UF_SF_POST_set_def_disp_params
**  4. UF_SF_POST_get_undef_disp_params
**  5. UF_SF_POST_initialise_undef_disp_params
**  6. UF_SF_POST_set_undef_disp_params
**
** Work Flow:
**  1. Initialize Post processor
**  2. Get current deformed display result params
**  3. Change necessary deform display params
**  4. Set the new deform display params
**  5. Get current undeformed display params
**  6. Change necessary undeform display params
**  7. Set the new undeform display params
**  8. Quit postprocessor
**
******************************************************************************
//
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
    UF_SF_POST_def_disp_t   def_disp, *new_def_disp;
    UF_SF_POST_undef_disp_t undef_disp, *new_undef_disp;



    /* ufd_sf_post_example_disp_param starts here */
    sprintf(buffer_g, "Executing ufd_sf_post_example_disp_param.c ...\n");
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

    /* Get the current deformed display parameters */
/**/

    UF_CALL(UF_SF_POST_get_def_disp_params(&def_disp));

/**/

    sprintf(buffer_g, "Current Deformed Display settings: \n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Display type of element edges = %d\n", def_disp.edge_style);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Color for displaying the element edges = %d\n", def_disp.edge_color);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of element face display = %d\n", def_disp.face_style);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Color for the displaying the element faces = %d\n", def_disp.face_color);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Marker to display the minimum and/or maximum values = %d\n", def_disp.display_marker);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Switch to decide whether to display the deformed model = %d\n", def_disp.def_sw);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Switch to decide whether to display the undeformed model = %d\n", def_disp.undef_sw);
    uf_write_listing_window(buffer_g);

    /* Initialise deform display params test */
    new_def_disp = NULL; /* Important assignment */
    def_disp.edge_style = UF_SF_POST_ELEM_EDGE_WIRE;
    def_disp.edge_color = UF_SF_POST_YELLOW_GREEN;
    def_disp.face_style = UF_SF_POST_ELEM_FACE_FILLED;
    def_disp.face_color = UF_SF_POST_WHITE;
    def_disp.display_marker = UF_SF_POST_DISPLAY_MARKER_MIN_MAX;
    def_disp.undef_sw = true;
    sprintf(buffer_g, "#%d: Calling UF_SF_POST_initialise_def_disp_params() ... ", ++test_count);
    uf_write_listing_window(buffer_g);
    UF_CALL(UF_SF_POST_initialise_def_disp_params(&new_def_disp, def_disp.edge_style, def_disp.edge_color, def_disp.face_style, def_disp.face_color, def_disp.display_marker, def_disp.def_sw, def_disp.undef_sw));

/**/

    /* Set deform display params test */
/**/

    UF_CALL(UF_SF_POST_set_def_disp_params(new_def_disp));

/**/

    sprintf(buffer_g, "Changed Deformed Display settings: \n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Display type of element edges = %d\n", new_def_disp->edge_style);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Color for displaying the element edges = %d\n", new_def_disp->edge_color);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of element face display = %d\n", new_def_disp->face_style);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Color for the displaying the element faces = %d\n", new_def_disp->face_color);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Marker to display the minimum and/or maximum values = %d\n", new_def_disp->display_marker);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Switch to decide whether to display the deformed model = %d\n", new_def_disp->def_sw);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Switch to decide whether to display the undeformed model = %d\n", new_def_disp->undef_sw);
    uf_write_listing_window(buffer_g);

    /* Update display */
    UF_CALL(UF_SF_POST_display_results());
    uc1601("Pause", 1);

    /* Get the undeformed display parameters */
/**/

    UF_CALL(UF_SF_POST_get_undef_disp_params(&undef_disp));

/**/

    sprintf(buffer_g, "Current Undeformed Display settings: \n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Display type of element edges = %d\n", undef_disp.edge_style);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Color for displaying the element edges = %d\n", undef_disp.edge_color);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of element face display = %d\n", undef_disp.face_style);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Color for the displaying the element faces = %d\n", undef_disp.face_color);
    uf_write_listing_window(buffer_g);

    /* Initialise the undeform display params test */
    new_undef_disp = NULL;
    undef_disp.edge_style = UF_SF_POST_ELEM_EDGE_NONE;
    undef_disp.edge_color = UF_SF_POST_MAGENTA;
    undef_disp.face_style = UF_SF_POST_ELEM_FACE_NONE;
    undef_disp.face_color = UF_SF_POST_RED;

/**/

    UF_CALL(UF_SF_POST_initialise_undef_disp_params(&new_undef_disp, undef_disp.edge_style, undef_disp.edge_color, undef_disp.face_style, undef_disp.face_color));

/**/

    /* Set the undeformed display parameters */
/**/

    UF_CALL(UF_SF_POST_set_undef_disp_params(new_undef_disp));

/**/

    sprintf(buffer_g, "Changed Undeformed Display settings: \n");
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Display type of element edges = %d\n", new_undef_disp->edge_style);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Color for displaying the element edges = %d\n", new_undef_disp->edge_color);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Type of element face display = %d\n", new_undef_disp->face_style);
    uf_write_listing_window(buffer_g);
    sprintf(buffer_g, "Color for the displaying the element faces = %d\n", new_undef_disp->face_color);
    uf_write_listing_window(buffer_g);

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

    UF_free(new_def_disp);
    UF_free(new_undef_disp);
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
