/*******************************************************************************

         Copyright (c) 1998-2002 Unigraphics Solutions Inc.
                Unpublished - All rights reserved

******************************************************************************





File Description :

This file contains routines to implement context sensitive help.
The Open API routines in this section are for users and third
party vendors who want to implement context sensitive help for
Dialog Area 1 (DA1) and Dialog Area 2 (DA2) dialogs.

The routines in this section allow you to:
 . Load an NX translation map file for context sensitive help.
 . Unload an NX translation map file for context sensitive help.
 . Reload an NX translation map file for context sensitive help.
 . Push the current application context onto the stack.
 . Clear all application contexts from the stack.
 . Clear the stack then push an application context.
 . Pop the application context from the top of the stack.
 . Display context sensitive help for the application context
   currently on the top of the stack.
 . Display context sensitive help for a specific application
   context.
 . Display an HTML or text help file page given
   the translation table specifications.
 . Turn printing of status messages for context sensitive help to
   standard out on or off.


*****************************************************************************/

#ifndef UF_HELP_INCLUDED
#define UF_HELP_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_retiring.h>
#include <libugopenint_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 * 
 */

/*****************************************************************
Load an NX translation map file for context sensitive help.
An NX translation map file is an ascii file that contains the associations
between an application context and the location in the documentation
for the help text.

The "filename" parameter can either be a fully qualified path to the
map file, or just the file name.  In the case of a file name, NX looks 
first in the working directory for the map file.  If the file is not 
in the working directory, NX then looks in the directory defined by 
the environment variable named UGDOCPL_DIR.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_load_map_file(
char * filename  /* <I>
                 Name of map file to load.
                 */
);

/*****************************************************************
Unloads an NX translation map file for context sensitive help.
NOTE: Once an NX translation map file has been loaded, additional
calls to load a map file are ignored until the map file has been
unloaded.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_unload_map_file(
char * filename  /* <I>
                 Name of map file to unload.
                 */
);

/*****************************************************************
Reloads an NX translation map file for context sensitive help. Performs
an unload/load. This is mainly intended as a utility routine to assist
with the debugging process.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_reload_map_file(
char * filename  /* <I>
                 Name of map file to reload.
                 */
);

/*****************************************************************
Push an application context onto the stack.
An application context is the key string used to look up help
documentation using the NX translation map file. Application
contexts are normally defined by the document writer after the
application developer has defined the areas of the code that requires
context sensitive help.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_push_context(
char * app_context  /* <I>
                    Name of application context to push onto stack.
                    */
);

/*****************************************************************
Clear all application contexts from the stack.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_clear_context( void );

/*****************************************************************
Clears the stack then pushes an application context. Normally used at
the start of an application when a DA1 dialog is displayed.
Using this routine insures that the context sensitive help stack and the
application are in sync and is especially useful in cases where signal
handlers or application errors have disrupted the normal program
flow. UF_HELP_push_primary_context clears the stack before pushing
the new application context to insure that the help system and the
application are in sync.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_push_primary_context(
char * app_context  /* <I>
                    Name of primary application context to push onto
                    stack.
                    */
);


/*****************************************************************
Pops the application context from the top of the stack.
This routine is called just before the end of a function that has made a
call to UF_HELP_push_context.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_pop_context( void );

/*****************************************************************
Displays context sensitive help on the application context currently on
the top of the stack. This function is useful for implementation
of a "Help On Context" button within the application. It gets the
application context from the top of the stack and looks that
context up in the NX translation map file, and uses the data in the
NX translation map file to start up the appropriate help display
mechanism, load the proper document, and position the document to
display the appropriate help text.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_display_current_context( void );

/*****************************************************************
Displays context sensitive help on a specific application context.
This routine performs a very similar function to
UF_HELP_display_current_context, except you pass in the
application context instead of using the context on the stack.
is useful for implementation of HELP buttons on modal dialogs.
It performs the same context lookup functions and display functions
as UF_HELP_display_current_context.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_display_context(
char * app_context  /* <I>
                    Name of application context to display help on.
                    */
);


/*****************************************************************
Turns printing of status messages for context sensitive help to standard
out either on or off.  These message provide more detailed information
about the process of displaying context sensitive help and can be useful
in debugging.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_set_context_debug(
int state  /* <I>
           Sets the state for printing messages for context
           sensitive help on or off.
              0 = Off
              1 = On
           */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif    /*  END  UF_HELP_INCLUDED  */
