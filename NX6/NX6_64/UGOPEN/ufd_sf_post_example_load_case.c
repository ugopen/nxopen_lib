
/*============================================================================
                 Copyright (c)  2005 UGS Corp.
                     All Rights Reserved
============================================================================*/
/*****************************************************************************
**
** Example name:
** ufd_sf_post_example_load_case.c
**
** Description:
** An example demonstrating the use of the load case UGOPEN calls in
** UF_SF_POST. This example requires a SIM file with a result.
** Functions included here are:
**  1. UF_SF_POST_create_combined_lcase
**  2. UF_SF_POST_delete_combined_lcase
**
** Work Flow:
**  1. Initialize Post processor
**  2. Create loadcase 1
**  3. Create loadcase 2
**  4. Delete load case 1
**  5. Quit postprocessor
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
    char clc_name[66], clc_name2[66];	/* Can we convert this into a macro */
    int num_lcases, *lcase_list, new_clc_num;
    double *lcase_scales;

    tag_t part_tag;


    /* ufd_sf_post_example_load_case starts here */
    sprintf(buffer_g, "Executing ufd_sf_post_example_load_case.c ...\n");
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

    /* Create and delete load case tests */
    strcpy(clc_name, "Pull_and_Pressure");
    num_lcases   = 2;
    lcase_list   = (int*)UF_allocate_memory(sizeof(int)* num_lcases, &response_g);
    if(response_g)
    {
        sprintf(buffer_g, "Failed to allocate memory!\n");
        uf_write_listing_window(buffer_g);
        UF_CALL(UF_SF_POST_quit_post_processor());
        return;
    }
    lcase_list[0] = 1;
    lcase_list[1] = 2;
    lcase_scales = (double*)UF_allocate_memory(sizeof(double)* num_lcases, &response_g);
    if(response_g)
    {
        sprintf(buffer_g, "Failed to allocate memory!\n");
        uf_write_listing_window(buffer_g);
        UF_CALL(UF_SF_POST_quit_post_processor());
        return;
    }
    lcase_scales[0] = 1.5;
    lcase_scales[1] = 2.5;

/**/

    UF_CALL(UF_SF_POST_create_combined_lcase(clc_name, num_lcases, lcase_list, lcase_scales, &new_clc_num));

/**/

    /* Update display */
    UF_CALL(UF_SF_POST_display_results());
    uc1601("Observe case 1 created!", 1);

    /* Create another load case */
    strcpy(clc_name2, "Pull_and_compress");
    lcase_list[0] = 1;
    lcase_list[1] = 2;
    lcase_scales[0] = 3.25;
    lcase_scales[1] = 5.75;
    UF_CALL(UF_SF_POST_create_combined_lcase(clc_name2, num_lcases, lcase_list, lcase_scales, &new_clc_num));

    /* Update display */
    UF_CALL(UF_SF_POST_display_results());
    uc1601("Observe case 2 created!", 1);

    /* Delete load case one */
/**/

    UF_CALL(UF_SF_POST_delete_combined_lcase(clc_name));

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

    UF_free(lcase_list);
    UF_free(lcase_scales);
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
