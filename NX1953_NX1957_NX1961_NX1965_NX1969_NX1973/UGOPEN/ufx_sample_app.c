/*=======================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                   Unpublished - All rights reserved

=========================================================================
File Description

   This is a an example of adding an Internal User Function application
   to Unigraphics.  In addition to using this source file, the two
   menu files, ufx_add_sample_app_button.men and ufx_sample_app.men
   are also required and also reside in the ugopen kit.

   Please see the MenuScript chapter of the UG/Open Programmer's Guide
   for a detailed description of this example, the required MenuScript
   environment variables and directories, and the correct placement of
   the shared library and menu files.

   These files are intended to provide a template that can be modified
   by renaming the files, and renaming the variables and routines
   contained in this C file to allow you create your own application.

   The sample callbacks also illustrate the arguments to the callbacks
   you will write.

   Additional information on MenuScript can be found in:
     - the UG/Open MenuScript User Guide
     - the UG/Open API Reference Manual
     - the UG/Open API Programmer's Manual

   *** PLEASE NOTE ***
   The shared library created from this program must be placed in the
   "application" directory under a directory listed in the file pointed to by the
   environment variable in UGII_CUSTOM_DIRECTORY_FILE (i.e. the shared library must
   not be in the "startup" directory).


=========================================================================
*/

/******************* includes ****************************************/

#include <stdio.h>
#include <uf_defs.h>
#include <uf.h>
#include <uf_exit.h>
#include <uf_mb.h>
#include <uf_ui_types.h>
#include <uf_ui.h>

static void SAMPLE_APP__enter( void );
static void SAMPLE_APP__init( void );
static void SAMPLE_APP__exit( void );


static UF_MB_cb_status_t SAMPLE_APP__action1(
    UF_MB_widget_t             widget,
    UF_MB_data_t               client_data,
    UF_MB_activated_button_p_t call_button );

static UF_MB_cb_status_t SAMPLE_APP__action2(
    UF_MB_widget_t             widget,
    UF_MB_data_t               client_data,
    UF_MB_activated_button_p_t call_button );

static UF_MB_cb_status_t SAMPLE_APP__action3(
    UF_MB_widget_t             widget,
    UF_MB_data_t               client_data,
    UF_MB_activated_button_p_t call_button );

static UF_MB_cb_status_t SAMPLE_APP__action4(
    UF_MB_widget_t             widget,
    UF_MB_data_t               client_data,
    UF_MB_activated_button_p_t call_button );

static int app_id = 0;

static UF_MB_action_t actionTable[] =
{
 { "SAMPLE_APP__action1", SAMPLE_APP__action1, NULL    },
 { "SAMPLE_APP__action2", SAMPLE_APP__action2, NULL    },
 { "SAMPLE_APP__action3", SAMPLE_APP__action3, &app_id },
 { "SAMPLE_APP__action4", SAMPLE_APP__action4, NULL    },
 { NULL, NULL, NULL }
};

static void print_error( char* fun, int status );

static void print_message( char *msg );

/*----------------------------------------------------------------------------*
 *  PUBLIC void ufsta
 *
 *    Register the application
 *
 *----------------------------------------------------------------------------*/
/* ARGSUSED */
extern void ufsta( char *param, int *retcod, int param_len )
{
    UF_MB_application_t appData;
    char name[] = "SAMPLE_APP";
    int status;
    int ifail = 0;

    ifail = UF_initialize();                          /* Initialize User Function */

    if ( !ifail )
    {
      status = UF_MB_add_actions( actionTable );
      print_error( "UF_MB_add_actions", status );

            /* Initialize application data */

      appData.name       = name;
      appData.id         = 0;
      appData.init_proc  = SAMPLE_APP__init;
      appData.exit_proc  = SAMPLE_APP__exit;
      appData.enter_proc = SAMPLE_APP__enter;

            /* Initialize application support flags */

      appData.drawings_supported          = TRUE;
      appData.design_in_context_supported = TRUE;

            /* Register the application with UG */

      status = UF_MB_register_application( &appData );
      print_error( "UF_MB_register_application", status );

      app_id = appData.id;
    }

    ifail = UF_terminate();                          /* Exit User Function */
}

/*----------------------------------------------------------------------------*
 *  SAMPLE_APP__enter
 *
 *      Enter the application
 *----------------------------------------------------------------------------*/
static void SAMPLE_APP__enter( void)
{
    print_message( "Entering application\n" );

    /* Place code to enter application here */
}

/*----------------------------------------------------------------------------*
 *  SAMPLE_APP__init
 *
 *      Initialize the application
 *----------------------------------------------------------------------------*/
static void SAMPLE_APP__init( void )
{
    print_message( "Initializing application\n" );

    /* Place code to initialize application here */
}

/*----------------------------------------------------------------------------*
 *  SAMPLE_APP__exit
 *
 *      Exit the application
 *----------------------------------------------------------------------------*/
static void SAMPLE_APP__exit( void )
{
    print_message( "Exiting application\n" );

    /* Place code to cleanup for application and exit here */
}

/*----------------------------------------------------------------------------*
 *  print_error
 *
 *      Print the error message corresponding to the status code specified if
 *      the status is non-zero.
 *----------------------------------------------------------------------------*/
static void print_error( char *fun, int status )
{
    if ( status != 0 )
    {
        char error_msg[133];
        char msg[133];

        UF_get_fail_message( status, error_msg );
        sprintf( msg, "%s failed with error = %d\n  %s\n", fun, status, error_msg );
        print_message( msg );
    }
}

/*----------------------------------------------------------------------------*
 *  print_message
 *
 *      Prints the given message to the syslog and the listing window.
 *----------------------------------------------------------------------------*/
static void print_message( char *msg )
{
    UF_print_syslog( msg, FALSE );
    if( !UF_UI_open_listing_window() )
    {
        UF_UI_write_listing_window( msg );
    }
}

/*----------------------------------------------------------------------------*
 *  get_button_id
 *
 *  Input:
 *      prompt - Cue prompt
 *
 *  Output:
 *      name - Button name specified by the user
 *      id   - ID corresponding the button name specified by the user
 *
 *  Return:
 *      Response
 *        1 = Back
 *        2 = Cancel
 *        3 = No data returned
 *        5 = Data returned
 *
 *----------------------------------------------------------------------------*/
static int get_button_id( char *prompt, char *name, int *id )
{
    int response = 0;
    int len = 0;

    UF_UI_lock_ug_access( UF_UI_FROM_CUSTOM );
    response = uc1600( prompt, name, &len );
    UF_UI_unlock_ug_access( UF_UI_FROM_CUSTOM );

    if ( response == 5 || ( response == 3 && len > 0 ) )
    {
        int status;

        response = 5;
        status = UF_MB_ask_button_id( name, id );
        print_error( "UF_MB_ask_button_id", status );
        if ( status != 0 )
        {
            char msg[133];

            response = 3;
            sprintf(msg, "%s button not found", name );
            UF_UI_lock_ug_access( UF_UI_FROM_CUSTOM );
            uc1601( msg, 0 );
            UF_UI_unlock_ug_access( UF_UI_FROM_CUSTOM );
        }
        else
        {
            char msg[133];
            sprintf( msg, "    %s(%d)\n", name, *id );
            print_message( msg );
        }
    }

    return( response );
}

/*----------------------------------------------------------------------------*
 *  SAMPLE_APP__action1
 *
 *      Allow the user to ask for the button ID corresponding to a button name
 *----------------------------------------------------------------------------*/
static UF_MB_cb_status_t SAMPLE_APP__action1(
    UF_MB_widget_t             widget,
    UF_MB_data_t               client_data,
    UF_MB_activated_button_p_t call_button )
{
    UF_MB_cb_status_t cb_status = UF_MB_CB_CONTINUE;
    char name[133] = "";
    int  id = 0;
    int  response = 0;
    int ifail = 0;

    ifail = UF_initialize();    /* Initialize User Function */

    if ( !ifail )
    {
        response = get_button_id( "Enter button to ask sensitivity of", name, &id );

        if ( response == 5 )
            cb_status = UF_MB_CB_CONTINUE;
        else if ( response == 1  || response == 2 )
            cb_status = UF_MB_CB_CANCEL;
        else
            cb_status = UF_MB_CB_ERROR;
    }

    ifail = UF_terminate();
    return( cb_status );
}

/*----------------------------------------------------------------------------*
 *  SAMPLE_APP__action2
 *
 *      Allow the user to specify this function's return value
 *----------------------------------------------------------------------------*/
static UF_MB_cb_status_t SAMPLE_APP__action2(
    UF_MB_widget_t             widget,
    UF_MB_data_t               client_data,
    UF_MB_activated_button_p_t call_button )
{
#define NUM_OPTIONS 5

    char options[NUM_OPTIONS][38] = { "UF_MB_CB_CONTINUE",
                                      "UF_MB_CB_CANCEL",
                                      "UF_MB_CB_OVERRIDE_STANDARD",
                                      "UF_MB_CB_WARNING",
                                      "UF_MB_CB_ERROR"
                                    };
    int option_cnt = NUM_OPTIONS;
    int response = 0;
    UF_MB_cb_status_t cb_value = UF_MB_CB_CANCEL;
    int ifail = 0;
    char msg[133];

    ifail = UF_initialize();    /* Initialize User Function */

    if ( !ifail )
    {
        UF_UI_lock_ug_access( UF_UI_FROM_CUSTOM );
        response = uc1603( "Choose value to return", 0, options, option_cnt );
        UF_UI_unlock_ug_access( UF_UI_FROM_CUSTOM );

        switch ( response )
        {
            case 1:
            case 2:
                cb_value = UF_MB_CB_CANCEL;
                sprintf( msg, "    Response = \"%s\" (%d)\n",
                        ( response == 1 ? "Back" : "Cancel" ), response );
                print_message( msg );
                break;

            case 5:
                cb_value = UF_MB_CB_CONTINUE;
                break;

            case 6:
                cb_value = UF_MB_CB_CANCEL;
                break;

            case 7:
                cb_value = UF_MB_CB_OVERRIDE_STANDARD;
                break;

            case 8:
                cb_value = UF_MB_CB_WARNING;
                break;

            case 9:
                cb_value = UF_MB_CB_ERROR;
                break;

            default:
                cb_value = UF_MB_CB_ERROR;
                sprintf( msg, "    Response = \"%s\" (%d)\n", "Unexpected", response );
                print_message( msg );
                break;
        }
        sprintf( msg, "Return = %s\n", &options[response - 5][0] );
        print_message( msg );
    }

    ifail = UF_terminate();
    return( cb_value );
}

/*----------------------------------------------------------------------------*
 *  SAMPLE_APP__action3
 *
 *      Print the current application's ID
 *----------------------------------------------------------------------------*/
static UF_MB_cb_status_t SAMPLE_APP__action3(
    UF_MB_widget_t             widget,
    UF_MB_data_t               client_data,
    UF_MB_activated_button_p_t call_button )
{
    int curr_app_id = *((int *) client_data);
    int ifail = 0;
    char msg[133];

    ifail = UF_initialize();    /* Initialize User Function */

    if ( !ifail )
    {
        sprintf( msg, "Application ID = %d\n", curr_app_id );
        print_message( msg );
    }

    ifail = UF_terminate();
    return( UF_MB_CB_CONTINUE );
}

/**************************************************************************
 * Function Name: SAMPLE_APP__action4
 *
 * Functions Description:
 *   Print the callback data for a button
 *
 * Input
 *
 * Output
 *   None
 *
 * Description -
 *
 * Returns - status code to continue or terminate
 **************************************************************************/
static UF_MB_cb_status_t SAMPLE_APP__action4(
    UF_MB_widget_t             widget,
    UF_MB_data_t               client_data,
    UF_MB_activated_button_p_t call_button )
{
      char buf[1024];
      char *type_name;
      int ifail = 0;

      ifail = UF_initialize();    /* Initialize User Function */

      if ( !ifail )
      {

          sprintf(buf, "Button Name = %s\n", call_button->name );
          print_message( buf );
          sprintf(buf, "Button Id = %d\n", call_button->id );
          print_message( buf );
          if ( UF_MB_ask_button_type_name( call_button->type, &type_name ) == 0 )
          {
               sprintf(buf, "Button Type = %s\n", type_name );
               print_message( buf );
          }
          sprintf(buf, "Menubar Name = %s\n", call_button->menubar_name );
          print_message( buf );
          if ( call_button->num_ancestors > 0 )
          {
              int j;

              print_message( " \n" );
              print_message( "Button Ancestors:\n" );
              for ( j = call_button->num_ancestors - 1; j >= 0; j-- )
              {
                    sprintf(buf, "    %s\n", call_button->ancestors[j] );
                    print_message( buf );
              }
          }
          print_message( " \n" );
      }

      ifail = UF_terminate();
      return( UF_MB_CB_CONTINUE );
}

