/*******************************************************************************
             Copyright (c) 1998-2000,2001 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File Description:
The Open API MenuScript which augments the menubar customization and
application integration features provided by MenuScript.

Extensive customization of the NX menubar can be accomplished using
menu files without performing any C programming.  These capabilites are
described in the "Open API MenuScript User Guide".

The integration of complete applications or extension of standard NX
applications using custom menu items that execute callbacks written in C is
documented in the MenuScript sections of the "Open API Reference" and the
"Open API Programmer's Guide".  The declarations and prototypes for the Open API
MenuScript are included below.

The functions prototyped in uf_mb.h provide the programmatic interface to
Open API MenuScript which provides:
.    Lets NX customers and third-party developers use ASCII files to
     edit NX menus and create custom menus for their own applications
     in an integrated, seamless manner. Menu files support custom tailoring of
     the main menu bar and the Quick View Pop-up menu.
.    supports pre and post actions for menu items, providing a capability
     similar to that of User Exits, for both standard NX menu items and
     those provided by third-party applications developed with the Open API
.    provides a Menubar Report Tool to help review menu customization, diagnose
     problems, and assist in upgrading to future NX releases.
.    provides for extensive customization of NX menus including adding,
     removing, and rearranging menu items, and duplicating or moving menu items
     from the main menu bar to the Quick View Pop-up menu. Added menu items can
     execute existing GRIP or Open API programs, perform system commands
     (including running a program or journal), open a UIStyler dialog, or open
     a User Tool palette.

All of these customization techniques can be accomplished without requiring any
C programming. These capabilities, along with complete information on the format
and usage of MenuScript menu files, MenuScript environment variables and command
line arguments, and the Menubar Report Tool are included in the Open
MenuScript User Guide.

NOTE:  You must be thoroughly familiar with the information in the Open
MenuScript User Guide to use the functions documented in this chapter. Please
review the information in the User Guide prior to using the MenuScript API.
 Open API - MenuScript Function
 Adding Functions to NX Menus
 Adding An Application to NX

*******************************************************************************/

#ifndef UF_MB_INCLUDED
#define UF_MB_INCLUDED

#include <uf_defs.h>
#include <uf_styler.h>
#include <libugopenint_exports.h>

/***************************************************************************

  ***************************************************************************/


#if !defined(_WIN32)
/*  */

#include <Xm/Xm.h>
#include <X11/Intrinsic.h>

typedef Widget    UF_MB_widget_t;
typedef XtPointer UF_MB_data_t;

/*  */
#else

typedef void *UF_MB_widget_t;
typedef void *UF_MB_data_t;

#endif

#ifdef __cplusplus
extern "C" {
#endif

/*  Each member of the UF_MB_cb_status_t enumerated type represents one
    of the possible return values from a callback function that has been
    registered via UF_MB_add_actions.

    To support possible future semantic differences between return codes, the
    five values shown below have been defined.  The comments next to each
    member identify its nominal meaning.  However, there are currently only
    two sets of semantics associated with these five values:

       UF_MB_CB_CONTINUE - this value will cause execution of any additional
        actions for a menu item to be executed.

       Any of the other four values will inhibit execution of the remaining
       actions.
*/

enum UF_MB_cb_status_e
{
    UF_MB_CB_CONTINUE,        /* Continue performing the menu item's actions */
    UF_MB_CB_CANCEL,          /* User interaction requested inhibiting the
                                 menu item's actions */
    UF_MB_CB_OVERRIDE_STANDARD,  /* Inhibit further actions because a pre
                                    action took the place of the standard
                                    action for a standard NX menu item. */
    UF_MB_CB_WARNING,            /* Inhibit further actions because a
                                    warning condition was raised. */
    UF_MB_CB_ERROR               /* Inhibit further actions because a
                                    error condition was raised. */
};
typedef enum UF_MB_cb_status_e UF_MB_cb_status_t, *UF_MB_cb_status_p_t;

/* button ID - a positive integer assigned by MenuScript that
       uniquely identifies a button.  The button id is a required input
       to many of the button utility routines whose prototypes appear
       below.  The button id can be obtained from the button name by
       using the routine, UF_MB_ask_button_id, and is also included
       in the UF_MB_activated_button_t structure pointed to by the
       third argument of a button's callback function.
*/
typedef int UF_MB_button_id_t, *UF_MB_button_id_p_t;


/* UF_MB_button_type_t is the type associated with a button defined via
   a MenuScript menu file.  When a callback action associated with a
   button is invoked, the button type is returned in the
   UF_MB_activated_button_t structure pointed to by the third argument
   to the callback (which is a function of type UF_MB_callback_t).

   The button type will be one the #defined button types documented
   below.
*/
typedef char UF_MB_button_type_t;  /* button types  */


/*  Button callback functions for MenuScript button actions are of type
    UF_MB_cb_status_t.  The third argument of for these callbacks is a pointer
    to a UF_MB_activated_button_t structure.  This structure provides
    information about the button that triggered the callback.  The ancestors
    array contains the names of all of the cascade buttons that were
    were traversed to reach the activated button.  The ancestor list will be
    the same regardless of whether the the ancestor hierarchy was actually
    traversed, or whether the button was activated via a tear-off menu or
    playing back a macro.
*/

struct MB_activated_button_s {
    UF_MB_button_id_t       id;            /* button's unique ID number      */
    UF_MB_button_type_t     type;          /* type of button                 */
    char                    *name;         /* name of the button             */
    char                    *menubar_name; /* name of parent menubar/popup   */
    int                     num_ancestors; /* number of ancestors (cascades) */
    char                    **ancestors;   /* <len:num_ancestors> names of ancestors             */
    int                     app_id;        /* application identifier for APP */
};
typedef struct MB_activated_button_s UF_MB_activated_button_t,
              *UF_MB_activated_button_p_t;

/*   Callbacks for activated MenuScript buttons are of type  UF_MB_callback_t.
     The arguments to each callback are:
        w           - the id of the button's widget that triggered the callback.
        client_data - The pointer to your callback data that was included in
                      the action registration table passed to UF_MB_add_actions.
        button      - Pointer to a structure of information about the activated
                      button (see description above).
*/

typedef UF_MB_cb_status_t (*UF_MB_callback_t) (
        UF_MB_widget_t w,           /* <I> trigger widget */
        UF_MB_data_t   client_data, /* <I> data pointer from action registration */
        UF_MB_activated_button_p_t button /* <I> */);


/*
    The UF_MB_cb_t is used to declare a callback and the callback argument
    for an action to be specified in a MenuScript menu file.  This
    structure is nested within each element of a UF_MB_action_t array that
    is passed to UF_MB_add_actions to build a table for binding action
    names specified on ACTION statements in menu files to their
    corresponding callbacks and callback arguments.
*/

struct UF_MB_cb_s
{
    UF_MB_callback_t cb;
    UF_MB_data_t     cb_data;
};
typedef struct UF_MB_cb_s UF_MB_cb_t, *UF_MB_cb_p_t;

/* The UF_MB_action_t typedef is used to declare an array of one
   or more action structures.  Each structure instance in this
   array specifies an action name that matches an action specification
   from a menu file, e.g.:

   Action registration in ufsta of Open API shared library:
   -----------------------------------------------------------

    static UF_MB_action_t actionTable[] =
    {
        { "select_test",         Select,              NULL },
        { "curvature",           Curvature,           NULL },
        { "curing",              Curing,              NULL },
        { "query",               Query,               NULL },
        { "open_curve_palette",  persistent_dlg,      NULL },
        { "close_curve_palette", closePalette,        NULL },
        { "dialog_test",         persistent_dlg_app2, NULL },
        { NULL, NULL, NULL}
    };
    ...
    UF_MB_add_actions( actionTable );

   Menu File exerpt:
   -----------------------------------------------------------

   BUTTON CURVATURE
   LABEL Curvature...
   ACTIONS curvature
*/

struct UF_MB_action_s
{
    char *action_name;
    UF_MB_cb_t action_cb;
};

typedef struct UF_MB_action_s UF_MB_action_t, *UF_MB_action_p_t;

/*
   Each member of the UF_MB_action_type_t enumerated type represents
   one of the action types that can be specified for an action declared
   in a MenuScript menu file.  This enumerated type is reserved for
   future use in the Open API; currently it is only used internally
   within MenuScript.
*/

enum UF_MB_action_type_e
{
    UF_MB_FUNCTION_ACTION,  /* Callback action registered via
                               UF_MB_add_actions */
    UF_MB_PROGRAM_ACTION,   /* Complete Open Program action */
    UF_MB_GRIP_ACTION,      /* GRIP program action */
    UF_MB_JOURNAL_ACTION = UF_MB_GRIP_ACTION, /* Journal action is equivalent to GRIP but with different file extension */
    UF_MB_IMMEDIATE_ACTION, /* System Command Action enclosed in quotes */
    UF_MB_USER_TOOL_ACTION, /* User Tool Definition File to be opened by the
                               action */
    UF_MB_STYLER_DIALOG_ACTION, /* Styler Dialog File to be opened by the
                                   the action */
    UF_MB_STYLER_TOP_DIALOG_ACTION, /* Styler Top Dialog File to be opened by
                                       the action */
    UF_MB_LEGACY_ACTION     /* Action defined via UF_UI_append_menubar_menu */
};
typedef enum UF_MB_action_type_e UF_MB_action_type_t, *UF_MB_action_type_p_t;


  /* UF_MB_CASCADE_BUTTON
     Cascade button that is used to open a submenu.
     Actions are not allowed for a cascade button.


     UF_MB_PUSH_BUTTON
     Push button that executes the button's actions


     UF_MB_TOGGLE_BUTTON
     A button that executes the button's actions and
     also maintains a value.  The toggle button value can be
     asked or set via the UF_MB_ask_toggle_state and
     UF_MB_set_toggle_state calls, respectively.

     UF_MB_SEPARATOR
     A button that displays a horizontal line used to visually
     separate two groups of logically related buttons.  The
     separator does not allow actions to be specified.


     UF_MB_APPLICATION_BUTTON
     An application button performs the action entering an
     internally developed NX application, or a custom
     application.  A custom application button must specify a
     Open API library containing a ufsta entry point that
     registers a set of actions for the application using
     UF_MB_add_action, and also registers the application using
     UF_MB_register_application.

     UF_MB_NULL_BUTTON
     The null button type is reserved for internal usage within
     MenuScript.
   */

#define UF_MB_CASCADE_BUTTON       'a'
#define UF_MB_PUSH_BUTTON          'b'
#define UF_MB_TOGGLE_BUTTON        'c'
#define UF_MB_SEPARATOR            'd'
#define UF_MB_APPLICATION_BUTTON   'e'
#define UF_MB_NULL_BUTTON          '\0'


/*  The elements of the UF_MB_state_t enumerated type correspond to
    ask or set routine argument for a button's sensitivity or a toggle
    button's current state.
*/

enum UF_MB_state_e
{
    UF_MB_ON,
    UF_MB_OFF
};
typedef enum UF_MB_state_e UF_MB_state_t, *UF_MB_state_p_t;

  /* Prototypes for the init, enter, and exit routines for a custom
     application.  The init routine should perform any necessary
     initialization of the application each time the application is
     activated.  The enter routine is called after the application's
     menu file has been read in and should be used to do any
     programmatic configuration of buttons that is needed, and
     should then create and display the application's main dialog.
  */

typedef void (*UF_MB_init_proc_t)( void );
typedef void (*UF_MB_enter_proc_t)( void );
typedef void (*UF_MB_exit_proc_t)( void );

  /* The UF_MB_application_t structure is used to register a custom
     application with NX and specify its characteristics.
  */

struct UF_MB_application_data_s
{
   int id;                              /* The application identifier assigned
                                           to the custom application by
                                           NX.  There are currently no
                                           MenuScript API routines that use this
                                           value, but there may be in
                                           the future.  This is returned by the
                                           UF_MB routines.
                                        */
   char *name;                          /* The application name.  This is
                                           provided by the Open API program.
                                           This name MUST match the name of the
                                           application button used to enter the
                                           application.
                                        */
   UF_MB_init_proc_t init_proc;         /* This is input by the Open API
                                           program.  This is the pointer to the
                                           application's initialization routine.
                                        */
   UF_MB_exit_proc_t exit_proc;         /* This is input by the Open API
                                           program.  This is the pointer to the
                                           application's exit/cleanup method.
                                        */
   UF_MB_enter_proc_t enter_proc;       /* This is input by the Open API
                                           program. This is the pointer to the
                                           application's main entry point.
                                        */
   logical drawings_supported;          /* This is input by the Open API
                                           program. Set to true if the custom
                                           application supports drawings.
                                        */
   logical design_in_context_supported; /* This is input by the Open API
                                           program. Should be set to true if the
                                           custom application supports design
                                           in context,
                                           e.g. work part different from the
                                           displayed part when in an assembly.
                                        */
   logical supports_undo;               /* This is input by the Open API
                                           program.  Should be set to true if
                                           the custom application supports undo.
                                        */
};
typedef struct UF_MB_application_data_s UF_MB_application_t,
               *UF_MB_application_p_t;

    /* Names of the NX menubars and popup menus that currently
       support customization.  One of these names will be returned in the
       menubar_name field of the button data pointed to by the third
       argument to each button callback. */

#define UF_MB_MAIN_MENUBAR_NAME "UG_GATEWAY_MAIN_MENUBAR"
#define UF_MB_VIEW_POPUP_NAME   "UG_GATEWAY_VIEW_POPUP"


/* These values inform the menubar of the positioning of a styler dialog
   It is only used in the is_top_dialog field of the structure,
   UF_MB_styler_actions_t */
#define UF_MB_STYLER_IS_TOP             ( TRUE )
#define UF_MB_STYLER_IS_NOT_TOP         ( FALSE )


/* The following structure is used to associate the callbacks of a UIStyler
   dialog to a menubar action.  This structure is used with the function
   UF_MB_add_styler_actions. You must have associated your UIStyler dlg file to
   a push button using MenuScript in order to use UF_MB_add_styler_actions.
   Please note that the information for this structure is automatically provided
   to you in your template source file.
*/

struct UF_MB_styler_actions_s {
        char *styler_file; /* The name of the styler file that you wish to
                              associate your callbacks with.
                                                   */
        void *client_data; /* This is an address of valid data.  Your client
                              data is passed to all of your callback functions
                              when they are invoked.  Client data is technically
                              the address of any value; for example, pointers to
                              variables, data structures or arrays.  */
        UF_STYLER_callback_info_p_t  callback_list;/* This is the list of
                              functions that you wish to associate to
                              your dialog.  The UIStyler automatically generates
                              this list and places it in the file associated
                              with your ".dlg" file.  This list should not be
                              modified directly.  If you wish to alter your
                              callback list, you must regenerate your template
                              code from the UIStyler. */
        int is_top_dialog; /* This is an indicator that informs the menubar of
                              the location of your dialog. UF_STYLER_IS_TOP or
                              UF_STYLER_IS_NOT_TOP are the acceptable values. */
};
typedef struct UF_MB_styler_actions_s UF_MB_styler_actions_t,
               *UF_MB_styler_actions_p_t;

/****************************************************************************
Registers custom Internal Open API applications for the NX
menubar.

Environment: Internal

See Also:

History:
 ****************************************************************************/
extern UGOPENINTEXPORT int UF_MB_add_actions(
UF_MB_action_t action_table[]  /* <I>
                               NULL terminated array of UF_MB_action_t
                               records containing action name, function address,
                               and callback argument.
                               */
);

/**********************************************************************
Returns the name of a button type. If the specified type corresponds
to the type of a menubar button, type_name is returned as a pointer to
the button type name, and the function returns 0; otherwise the
function type_name points to the string "UNKNOWN" and the return
value is UF_err_bad_parameter_number_1.

Environment: Internal

See Also:

History:
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_MB_ask_button_type_name(
UF_MB_button_type_t type ,/* <I>
                          The type of a menu bar button.
                          */
char ** type_name  /* <OF>
                   The name of the button type.
                   */
);

/**********************************************************************
Associates a UIStyler dialog to an associated action specified in a Menuscript
file. The dialog file must be generated from the UIStyler and must be located
in the "application" directory underneath the directory which has been added to
the file $UGII_BASE_DIR/ugii/menu/custom_dirs.dat.

For example, on an NT system, you could specify d:\my_application
as your directory.

The actions structure provides the binding of callbacks and client data
to the dialog.  You may associate multiple dialogs in your actions
structure provided that the list is NULL terminated.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_add_styler_actions(
UF_MB_styler_actions_p_t actions  /* <I>
                                  Action definition of menubar dialog(s)
                                  */
);

/**********************************************************************
Register the user application defined by the application button.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_register_application(
UF_MB_application_p_t app  /* <I>
                           User application data containing name of
                           application to register.
                           */
);

/**********************************************************************
Gets the button's ID.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_ask_button_id(
char * button_name ,/* <I>
                    Name of the button
                    */
int * button_id  /* <O>
                 Button Identification
                 */
);

/**********************************************************************
Gets the button's sensitivity.  Note that this function is intended for customized
Menuscript buttons only.  The NX buttons are insensitive when running any NXOpen program and
are returned to their normal sensitivity state when the NXOpen program completes.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_ask_button_sensitivity(
int button_id ,/* <I>
               Button Identification
               */
UF_MB_state_p_t state  /* <O>
                       Button sensitivity can be one of the following:
                       UF_MB_ON
                       UF_MB_OFF
                       */
);

/**********************************************************************
Sets the button's sensitivity.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_set_button_sensitivity(
int button_id ,/* <I>
               Button ID
               */
UF_MB_state_t state  /* <I>
                     The button's sensitivity can be set to one of the
                     following states:
                      UF_MB_ON
                      UF_MB_OFF
                     */
);


/**********************************************************************
Gets a toggle button's current state.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_ask_toggle_state(
int button_id ,/* <I>
               Button ID
               */
UF_MB_state_t * state  /* <O>
                       The button's sensitivity can be one of the following:
                       UF_MB_ON
                       UF_MB_OFF
                       */
);



/**********************************************************************
Sets the state of a toggle button.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_set_toggle_state(
int button_id ,/* <I>
               Button ID
               */
UF_MB_state_t state  /* <I>
                     Sets the toggle buttons state on or off. Use one of
                     the following constants:
                     UF_MB_ON
                     UF_MB_OFF
                     */
);


/**********************************************************************
Loads a resource file. Locates the requested resource file in the
vendor, site, or user application directory (specified by one of the
following environment variables: UGII_UGOPEN_VENDOR_DIR,
UGII_UGOPEN_SITE_DIR, or UGII_UGOPEN_USER_DIR), loads it into a new,
temporary XrmDatabase, and then merges it into the master XrmDatabase
for the display connection (i.e. the application session). The merge
automatically destroys the temporary database.

NOTE:  This function is only available on Unix.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_load_resource_file(
const char * resource_file  /* <I>
                            The name of the vendor resource file to be loaded.
                            The name does not include the path.
                            */
);/*<NON_NXOPEN>*/

/**********************************************************************
Locates the requested resource in the X Resource Database. If it is
found, its value is set to the value found. If the resource is not found,
value is set to the default. 0 is returned unless there are any argument
or exception errors.

NOTE:  This function is only available on Unix.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_ask_logical_resource(
const char * name ,/* <I>
             The name of the resource to be located.
             */
logical defvalue ,/* <I>
                  The default value for the resource if not found.
                  */
logical * value  /* <O>
                 The value of the resource.
                 */
);/*<NON_NXOPEN>*/

/**********************************************************************
Locates the requested resource in the X Resource Database. If it is
found, its value is set to the value found. If the resource is not found,
value is set to the default. 0 is returned unless there are any argument
or exception errors.

NOTE:  This function is only available on Unix.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_ask_double_resource(
const char * name ,/* <I>
             The name of the resource to be located.
             */
double defvalue ,/* <I>
                 The default value for the resource if not found.
                 */
double * value  /* <O>
                The value of the resource.
                */
);/*<NON_NXOPEN>*/

/**********************************************************************
Locates the requested resource in the X Resource Database. If it is
found, its value is set to the value found. If the resource is not found,
value is set to the default. 0 is returned unless there are any argument
or exception errors.

NOTE:  This function is only available on Unix.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_ask_int_resource(
const char * name ,/* <I>
             The name of the resource to be located.
             */
int defvalue ,/* <I>
              The default value for the resource if not found.
              */
int * value  /* <O>
             The value of the resource.
             */
);/*<NON_NXOPEN>*/

/**********************************************************************
Locates the requested resource in the X Resource Database. If it is
found, its value is set to the value found. If the resource is not found,
value is set to the default. 0 is returned unless there are any argument
or exception errors.

NOTE:  This function is only available on Unix.

Environment: Internal

See Also:

History:
 *********************************************************************/
extern UGOPENINTEXPORT int UF_MB_ask_string_resource(
const char * name ,/* <I>
             The name of the resource to be located.
             */
const char * defvalue ,/* <I>
                 The default value for the resource if not found.
                 */
      char   value[]  /* <O>
              The value of the resource.
              */
);/*<NON_NXOPEN>*/


/**********************************************************************
Initializes the custom application data.  This routine should be called
before calling UF_MB_register_application.

  Return: void

  Environment: Internal

  See Also:

  History:     Introduced in V18.0
**********************************************************************/
extern UGOPENINTEXPORT int UF_MB_init_application_data(
UF_MB_application_p_t app_data /* <I/O>
                               Pointer to application data structure.
                               */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif   /*  END  UF_MB_INCLUDED  */
