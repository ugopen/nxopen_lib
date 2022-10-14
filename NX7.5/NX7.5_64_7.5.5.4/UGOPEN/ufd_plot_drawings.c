/*****************************************************************************

          Copyright (c) 2004 UGS PLM Solutions
            Unpublished - All rights reserved

 *****************************************************************************

  ufd_plot_drawings.c
   
    Print all drawing sheets of the displayed part (using the default settings)
    to a known printer / profile. This example assumes that the default Printer
    Group has a printer named "Printer One" and it uses the SDI "system" profile


*****************************************************************************/

/* Include files */
#include <stdio.h>
#include <uf.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_plot.h>
#include <uf_ui.h>
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

extern DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
	UF_PLOT_job_options_t		job_options;
	UF_PLOT_banner_options_t	banner_options;
	char					   *job_name;
	int							copies;
    tag_t                       display_part;
	tag_t					    drawing_sheet;

    /* Initialize the API environment */
    if( UF_CALL(UF_initialize()) ) 
    {
        /* Failed to initialize */
        return;
    }

    /*  If no part is displayed, do nothing.  */

    display_part = UF_PART_ask_display_part();
    if (display_part == NULL_TAG)
    {
        return;
    }
    
/*
    Get the default job options and banner options for use in
    the "print" call for each sheet
*/
    UF_CALL( UF_PLOT_ask_default_job_options( &job_options) );
    UF_CALL( UF_PLOT_ask_default_banner_options( &banner_options ) );

    copies = 1;

    drawing_sheet = NULL_TAG;
    while ((UF_CALL(UF_OBJ_cycle_objs_in_part(display_part,
                                              UF_drawing_type,
                                              &drawing_sheet)) == ERROR_OK) &&
           (drawing_sheet != NULL_TAG))
    {
        /*  Supplying a drawing sheet tag causes the default job
            name to have the sheet name appended to it
        */
		UF_CALL( UF_PLOT_ask_default_job_name( drawing_sheet, &job_name ) );

        /*  Print the sheet. The "Printer One" printer MUST be
            defined in the default Printer group for your system.
            The "<System Profile>" profile is the default SDI
            profile. You can alter these two parameters to match
            your installation.
        */
        UF_CALL( UF_PLOT_print( drawing_sheet, &job_options, job_name,
                                &banner_options, "Printer One",
                                "<System Profile>", copies ) );
		UF_free( job_name );
    }

    /* Terminate the API environment */
    UF_CALL(UF_terminate());
}

/*****************************************************************************
**  Utilities
*****************************************************************************/

/* Unload Handler
**     This function specifies when to unload your application from Unigraphics.
**     If your application registers a callback (from a MenuScript item or a
**     User Defined Object for example), this function MUST return
**     "UF_UNLOAD_UG_TERMINATE". */
extern int ufusr_ask_unload( void )
{
    return( UF_UNLOAD_IMMEDIATELY );
}
