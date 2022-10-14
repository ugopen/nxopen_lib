/*****************************************************************************
**                  Copyright (c) 2007 UGS Corp.
**                      All rights reserved
******************************************************************************
** 
**
**
** ufun_part_callbacks.c
**
** Description:
**     This simple demo registers part callbacks for every available reason
**     via the legacy Open C language.
**     After compiling and linking this demo program, the output library needs
**     to be placed in a folder called startup (for example c:\user_dir\startup).
**     Also the UGII_USER_DIR enviornment variable needs to point to the startup
**     directory's parent folder (for example: UGII_USER_DIR=c:\user_dir).
**     Once you have the startup directory and user dir environment variable
**     set up, start NX.  The part callbacks will be registered at startup.
**     Now anytime you create new, open, save, save as, close, modify, rename,
**     or change the workpart your callbacks will be executed.
**
**     To demo all of the available part callbacks at runtime - compile and link
**     execute_all_part_callbacks.c.
**     Then start NX and go to File->Execute->NX Open and select your compiled
**     execute_all_callbacks program.
**
*****************************************************************************/

/* Include files */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_part.h>
#include <uf_assem.h>



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

void register_cbs();
extern DllExport void ufsta( char *param, int *returnCode, int rlen );


/* Called when a new part is created
   Prints the name of the created part to the listing window
*/
static void my_create_callback(UF_callback_reason_e_t reason,
    const void *application_data, void *user_data)
{
    const tag_p_t
        part = (tag_p_t)application_data;
    char
        part_name[ MAX_FSPEC_BUFSIZE ];
    char msg[256];

    if (UF_CALL(UF_initialize())) return;

    UF_PART_ask_part_name(*part, part_name);

    UF_CALL(UF_UI_open_listing_window());
    sprintf(msg, "    UF created: %s\n", part_name);
    UF_CALL(UF_UI_write_listing_window(msg));

    UF_terminate();
}

/* Called when a part is opened
   Prints the name of the opened part to the listing window
*/
static void my_open_callback(UF_callback_reason_e_t reason,
    const void *application_data, void *user_data)
{
    const tag_p_t
        part = (tag_p_t)application_data;
    char
        part_name[ MAX_FSPEC_BUFSIZE ];
    char msg[256];

    if (UF_CALL(UF_initialize())) return;

    UF_PART_ask_part_name(*part, part_name);

    UF_CALL(UF_UI_open_listing_window());
    sprintf(msg, "    UF opened: %s\n", part_name);
    UF_CALL(UF_UI_write_listing_window(msg));

    UF_terminate();
}

/* Called when a part is saved
   Prints the name of the saved part to the listing window
*/
static void my_save_callback(UF_callback_reason_e_t reason,
    const void *application_data, void *user_data)
{
    const tag_p_t
        part = (tag_p_t)application_data;
    char
        part_name[ MAX_FSPEC_BUFSIZE ];
    char msg[256];

    if (UF_CALL(UF_initialize())) return;

    UF_PART_ask_part_name(*part, part_name);

    UF_CALL(UF_UI_open_listing_window());
    sprintf(msg, "    UF saved: %s\n", part_name);
    UF_CALL(UF_UI_write_listing_window(msg));

    UF_terminate();
}

/* Called when a part is saved as
   Prints the name of the saved as part to the listing window
*/
static void my_save_as_callback(UF_callback_reason_e_t reason,
    const void *application_data, void *user_data)
{
    const tag_p_t
        part = (tag_p_t)application_data;
    char
        part_name[ MAX_FSPEC_BUFSIZE ];
    char msg[256];

    if (UF_CALL(UF_initialize())) return;

    UF_PART_ask_part_name(*part, part_name);

    UF_CALL(UF_UI_open_listing_window());
    sprintf(msg, "    UF saved as: %s\n", part_name);
    UF_CALL(UF_UI_write_listing_window(msg));

    UF_terminate();
}

/* Called when a part is closed
   Prints the name of the closed part to the listing window
*/
static void my_close_callback(UF_callback_reason_e_t reason,
    const void *application_data, void *user_data)
{
    const tag_p_t
        part = (tag_p_t)application_data;
    char
        part_name[ MAX_FSPEC_BUFSIZE ];
    char msg[256];

    if (UF_CALL(UF_initialize())) return;

    UF_PART_ask_part_name(*part, part_name);

    UF_CALL(UF_UI_open_listing_window());
    sprintf(msg, "    UF closed: %s\n", part_name);
    UF_CALL(UF_UI_write_listing_window(msg));

    UF_terminate();
}

/* Called when a part is modified for the first time
   Prints the name of the modified part to the listing window
*/
static void my_modify_callback(UF_callback_reason_e_t reason,
    const void *application_data, void *user_data)
{
    const tag_p_t
        part = (tag_p_t)application_data;
    char
        part_name[ MAX_FSPEC_BUFSIZE ];
    char msg[256];

    if (UF_CALL(UF_initialize())) return;

    UF_PART_ask_part_name(*part, part_name);

    UF_CALL(UF_UI_open_listing_window());
    sprintf(msg, "    UF modified: %s\n", part_name);
    UF_CALL(UF_UI_write_listing_window(msg));

    UF_terminate();
}

/* Called when a part is renamed
   Prints the name of the renamed part to the listing window
*/
static void my_rename_callback(UF_callback_reason_e_t reason,
    const void *application_data, void *user_data)
{
    const tag_p_t
        part = (tag_p_t)application_data;
    char
        part_name[ MAX_FSPEC_BUFSIZE ];
    char msg[256];

    if (UF_CALL(UF_initialize())) return;

    UF_PART_ask_part_name(*part, part_name);

    UF_CALL(UF_UI_open_listing_window());
    sprintf(msg, "    UF renamed: %s\n", part_name);
    UF_CALL(UF_UI_write_listing_window(msg));

    UF_terminate();
}

/* Called when the workpart changes
   Prints the name of old workpart and new workpart to the listing window
*/
static void my_cwp_callback(UF_callback_reason_e_t reason,
    const void *application_data, void *user_data)
{
    tag_t wk_part = NULL_TAG;
    const tag_p_t
        part = (tag_p_t)application_data;
    char
        part_name[ MAX_FSPEC_BUFSIZE ];
    char msg[256];

    if (UF_CALL(UF_initialize())) return;

    UF_CALL(UF_UI_open_listing_window());
    sprintf(msg, "    UF work part changed\n");
    UF_CALL(UF_UI_write_listing_window(msg));

    if( part != NULL && *part != NULL_TAG )
    {
        UF_PART_ask_part_name(*part, part_name);
    }
    else
    {
        sprintf( part_name, "NULL" );
    }
    sprintf(msg, "        Old Work Part: %s\n", part_name);
    UF_CALL(UF_UI_write_listing_window(msg));
    sprintf( part_name, "" );

    wk_part = UF_ASSEM_ask_work_part();
    if( wk_part != NULL_TAG )
    {
        UF_PART_ask_part_name(wk_part, part_name);
    }
    else
    {
        sprintf( part_name, "NULL" );
    }
    sprintf(msg, "        New Work Part: %s\n", part_name);
    UF_CALL(UF_UI_write_listing_window(msg));
    UF_terminate();
}


static UF_registered_fn_p_t function_create_id = NULL;
static UF_registered_fn_p_t function_open_id = NULL;
static UF_registered_fn_p_t function_save_id = NULL;
static UF_registered_fn_p_t function_save_as_id = NULL;
static UF_registered_fn_p_t function_close_id = NULL;
static UF_registered_fn_p_t function_modify_id = NULL;
static UF_registered_fn_p_t function_rename_id = NULL;
static UF_registered_fn_p_t function_cwp_id = NULL;

/* Registers the callbacks in NX */
void register_cbs()
{
    char msg[256];
    sprintf( msg, "\n\nREGISTERING UFUN CALLBACKS\n\n" );
    UF_print_syslog(msg, FALSE);


    UF_CALL(UF_add_callback_function(UF_create_part_reason,
            my_create_callback, NULL, &function_create_id));
    UF_CALL(UF_add_callback_function(UF_open_part_reason,
            my_open_callback, NULL, &function_open_id));
    UF_CALL(UF_add_callback_function(UF_save_part_reason,
            my_save_callback, NULL, &function_save_id));
    UF_CALL(UF_add_callback_function(UF_save_as_part_reason,
            my_save_as_callback, NULL, &function_save_as_id));
    UF_CALL(UF_add_callback_function(UF_close_part_reason,
            my_close_callback, NULL, &function_close_id));
    UF_CALL(UF_add_callback_function(UF_modified_part_reason,
            my_modify_callback, NULL, &function_modify_id));
    UF_CALL(UF_add_callback_function(UF_rename_part_reason,
            my_rename_callback, NULL, &function_rename_id));
    UF_CALL(UF_add_callback_function(UF_change_work_part_reason,
            my_cwp_callback, NULL, &function_cwp_id));

}

/*****************************************************************************
**  Activation Methods
*****************************************************************************/
/*  Unigraphics Startup
**      This entry point activates the application at Unigraphics startup */
extern DllExport void ufsta( char *param, int *returnCode, int rlen )
{
    /* Initialize the API environment */
    if( UF_CALL(UF_initialize()) )
    {
        /* Failed to initialize */
        return;
    }
    /* TODO: Add your application code here */
    register_cbs();

    /* Terminate the API environment */
    UF_CALL(UF_terminate());
}

/*  Explicit Activation
**      This entry point is used to activate the application explicitly, as in
**      "File->Execute-> NX Open" */
extern DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
    tag_t part_tag = NULL_TAG;



    /* Initialize the API environment */
    if( UF_CALL(UF_initialize()) )
    {
        /* Failed to initialize */
        return;
    }

    /* TODO: Add your application code here */
    if( function_create_id == NULL )
    {
        uc1601( "Registering ufun callbacks", 1 );
        register_cbs();
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
    return( UF_UNLOAD_UG_TERMINATE );
}

