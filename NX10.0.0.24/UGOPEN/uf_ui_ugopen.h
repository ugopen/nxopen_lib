/*******************************************************************************
             Copyright (c) 2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       


 
File description :

This is the Open C API interface to the NX user interface function
which are available for use in internal or external Open applications,
with behavioral differences between the two environments.

 ****************************************************************************/

#ifndef UF_UI_UGOPEN_INCLUDED 
#define UF_UI_UGOPEN_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
Opens and manages (displays) a motif style Information
window if in internal Open API mode.  The first time
this window is opened it will be empty.  Further calls will
display the information previously displayed in the window. 
If in external Open API mode, sets the listing window 
flag to open.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_UI_open_listing_window( void );

/****************************************************************************
Closes the listing window. If in internal Open API, the window is
closed. If in external Open API, then the device is set to closed.

Environment: Internal  and  External

See Also:  UF_UI_exit_listing_window

History: For V15.0, this function was modified so that it closes the window but
         does not clear the windows contents. Prior to V15.0, this function
         closed and cleared the window in Internal Open API.

 ****************************************************************************/
extern UFUNEXPORT int UF_UI_close_listing_window( void );

/****************************************************************************
Closes and clears the listing window. If in internal Open API,
the window is closed and cleared. If in external Open API, the
device is set to closed.

Environment: Internal and External

See Also : UF_UI_close_listing_window  

History: This function was originally released in V15.0.
****************************************************************************/
extern UFUNEXPORT int UF_UI_exit_listing_window(void);

/****************************************************************************
Writes a character string to the Information window. You should add
your own new line after the string is placed. If in internal Open
API, text is displayed in the Information window. If in external
Open API, text is printed to standard out. The Information
window must be opened before you can write to it.

Once UF_terminate has completed in an external program, you can no
longer write to the console window.  It must be reinitialized with system
calls.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_UI_write_listing_window(
const char * string  /* <I>
                     pointer to character string
                     */
);

/****************************************************************************
Queries whether the Information window is open or closed. This
function returns a value of FALSE if the Information window:
has never been opened, has been closed with File-->Exit, File-->Close, 
has been closed by a call to UF_UI_close_listing_window or by selecting 
the Information button.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_UI_is_listing_window_open(
logical * response  /* <O>
                    Response flag:
                    TRUE = Window is open
                    FALSE = Window is closed
                    */
);

/****************************************************************************
Saves the contents of the Information window to the file specified by
the argument.

Note: The saved listing window information is limited to 256 characters
per line.  If a line is longer than 256 characters, it will be wrapped to
multiple lines in the saved file.

Environment: Internal and External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_UI_save_listing_window(
char * filename  /* <I>
                 filename to which Information  Window contents is
                 written.
                 */
);


/****************************************************************************
Adds the friendly name associated with the class name of a User
Defined Object (UDO) to the Type list of the class selection dialog.
The class becomes selectable.

Environment: Internal and External

See Also: UF_UI_delete_from_class_sel 

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_UI_add_to_class_sel (
unsigned int class_id  /* <I>
                       The identifier of the class.
                       */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /*  UF_UI_UGOPEN_INCLUDED  */
