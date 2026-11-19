/****************************************************************************

           Copyright (c) 2000 Unigraphics Solutions Inc.
                         Unpublished - All rights reserved

 File description:  
          These routines are in the process of being removed from the UG/Open
          product.  Customers should use the designated replacement routines
          instead of the routines listed here.  Once a routine is placed
          here, it is eligible to be removed in the next release of Unigraphics.
 
****************************************************************************/

/*
 

*/

#ifndef UF_RETIRING_UGOPENINT
#define UF_RETIRING_UGOPENINT

#include <uf_disp_types.h>

#include <libugopenint_exports.h>
/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif

/*
UF_DISP_create_image and UF_DISP_create_framed_image have been replaced by
the new Gateway::ImageExportBuilder class.  Please refer to that class'
documentation for usage instructions.
*/

/*****************************************************************
 * Export a PNG/JPEG/TIFF/GIF/XWD/BMP full window area image
 * Creates an image file with the file type you specify using the image
 * currently displayed in the graphics window.
 *
 * Return:
 *  Return code:
 *        = 0 No error
 *        = not 0 Error code, including:
 *                UF_DISP_err_failed_to_create_image_file
 *                Standard UF error codes
 *                
 * Environment: Internal
 * See Also: 
 * History: Original release was in V13.0.  Retired in NX 12.0.1.
 *****************************************************************/
extern UGOPENINTEXPORT int UF_DISP_create_image(
 char* filename ,                  /* <I>
                                   Name of output image file
                                   */
 UF_DISP_image_format_t format ,   /* <I>
                                   Image type to produce:
                                   UF_DISP_PNG
                                   UF_DISP_JPEG
                                   UF_DISP_TIFF
                                   UF_DISP_COMPRESSED_TIFF
                                   UF_DISP_GIF
                                   UF_DISP_XWD (Only on UNIX workstations)
                                   UF_DISP_BMP (Only on Windows workstations)
                                   */
 UF_DISP_background_color_t color  /* <I>
                                   Back ground color:
                                   UF_DISP_ORIGINAL
                                   UF_DISP_WHITE
                                   */
); /* <RETIRE_NXOPEN> */

/*****************************************************************
 * Creates an image file with the file type and rectangular frame you
 * specify using the image currently displayed in the graphics window.
 * Export a PNG/JPEG/TIFF/GIF/XWD/BMP full window or rectangular area image
 * Full window image: set width and height to zero
 * Rectangular area image: set width, height greater than zero and set
 * upper left point window coordinate
 *
 * Return:
 *  Return code:
 *        = 0 No error
 *        = not 0 Error code, including:
 *                UF_DISP_err_failed_to_create_image_file
 *                Standard UF error codes
 *                
 * Environment: Internal
 * See Also:
 * History: Original release was in V15.0.  Retired in NX12.0.1.
 *****************************************************************/
extern UGOPENINTEXPORT int UF_DISP_create_framed_image(
    char* filename ,                    /* <I>
                                        Name of output image file
                                        */
    UF_DISP_image_format_t format ,     /* <I>
                                        Image type to produce:
                                        UF_DISP_PNG
                                        UF_DISP_JPEG
                                        UF_DISP_TIFF
                                        UF_DISP_COMPRESSED_TIFF
                                        UF_DISP_GIF
                                        UF_DISP_XWD (Only on UNIX workstations)
                                        UF_DISP_BMP (Only on Windows workstations)
                                        */
    UF_DISP_background_color_t color ,  /* <I>
                                        Back ground color:
                                        UF_DISP_ORIGINAL - original background
                                                           color
                                        UF_DISP_WHITE - white background color.
                                        */
    int upper_left_corner[2] ,          /* <I>
                                        The Image's upper left corner in the 
                                        window. Set both x and y to 0 (zero) 
                                        for a full screen image.
                                        upper_left_corner[0] = x position
                                        upper_left_corner[1] = y position
                                        */
    int width ,                         /* <I>
                                        Image width in pixels. Set to 0 (zero)
                                        for full screen image.
                                        */
    int height                          /* <I>
                                        Image height in pixels. Set to 0 
                                        (zero) for full screen image.
                                        */
); /* <RETIRE_NXOPEN> */

#ifdef UNX

#include <Xm/Xm.h>

/****************************************************************************
Handles managing and unmanaging of the dialog. The sequence of events is:

Manage the main widget of the dialog (dialog_widget).

Enter the Ungraphics event loop and stay there until UF_UI_exit_dialog is
called from a dialog callback function.

When the event loop is exited, the main widget of the dialog is unmanaged.

Return to the caller.

When creating a dialog, you must use the visuals from NX.  To do this
you must use  UF_UI_ask_default_parent_info, to get the information.

After the dialog has been defined (i.e., all widgets created as necessary), the
main widget is passed to UF_UI_run_dialog. This function manages the main
widget and enters the NX event loop allowing the dialog to "run"
(i.e., react to keyboard input and mouse gestures, execute callbacks, etc.).
UF_UI_run_dialog does not return to the user until UF_UI_exit_dialog has been
called.

When the UF_UI_run_dialog call has been made, some of the NX
application becomes inhibited.  This includes the non-global functions in the
main menubar and various DA1s.  Even though access to parts of NX is
inhibited, NX does not consider itself in a "lock" state.  This only
occurs with the call to UF_UI_lock_ug_access.  Unlike launching a custom dialog
with XtManageChild, with UF_UI_run_dialog you do not need to call
UF_UI_lock_ug_access when calling a Presentation API.  However, if you do not
call UF_UI_lock_ug_access then you are not allowed to call
UF_UI_cancel_uf_dialog.

When the dialog handling part of the Open API program (i.e.,
the dialog's callback functions) determines that it is time to terminate
the dialog (for example, after you press OK or Cancel on the dialog),
UF_UI_exit_dialog should be called. This function should only be
called from a callback function associated with a dialog initiated by a
call to UF_UI_run_dialog.

Always make sure to check the status of UF_UI_run_dialog. This will return an
error messages if something goes wrong.  You can use the Open API
UF_UI_get_fail_message to determine the exact problem UF_UI_run_dialog and
UF_UI_exit_dialog experienced.

A user of a custom dialog launched via UF_UI_run_dialog may not launch another
Open application that uses the lock & unlock mechanism or is launched via
UF_UI_run_dialog.

This example will launch a custom dialog with two push buttons.  Prior to
launching the custom dialog with UF_UI_run_dialog a call to
UF_UI_lock_ug_access is made.  This implies the necessary handshaking has been
done for the entire session, and therefore is not needed around each and every
Open dialog or UIStyler dialog call.  Both buttons within the custom dialog
always remain active so calls to UF_UI_cancel_uf_dialog have been made to
ensure the correct handling of the dialog when the user select another button in
the custom dialog while the Open dialog is up.  Also, a call to
UF_UI_cancel_uf_dialog has been made from within the cancel button navigation
callback.  Since, this custom dialog is always locked there is no need to check
the lock status prior to calling this function.  Because no Open API should
be called immediately following UF_UI_cancel_uf_dialog, a call to
XtAppAddTimeOut is made, which has a callback making the necessary call to
UF_UI_exit_dialog.  Once the UF_UI_run_dialog has terminated then the unlocking
of the custom dialog is done and the call to UF_terminate is made.

Environment: Internal

See Also: 

History:
 Deprecated in NX 2406
 ****************************************************************************/
extern UGOPENINTEXPORT int UF_UI_run_dialog(
    Widget dialog_widget  /* <I>
                          Main Widget of the Motif dialog.
                          */
); /* <RETIRE_NXOPEN> */

/****************************************************************************
Causes the event loop of the currently executing user Motif dialog to
exit which, in turn, causes UF_UI_run_dialog() (used to start the
dialog) to execute a return.  This is only used in relation with
UF_UI_run_dialog.  Always check the return status of UF_UI_exit_dialog
to be sure that exiting the dialog was successful.

If using the UF_UI_cancel_uf_dialog protocol then
UF_UI_exit_dialog should be called via a callback from
XtAppAddTimeOut, otherwise just call UF_UI_exit_dialog directly.
The call to UF_UI_exit_dialog causes the event loop to be terminated
which, in turn, causes UF_UI_run_dialog to return to its caller.

Environment: Internal

See Also: 

History:
 Deprecated in NX 2406
 ****************************************************************************/

extern UGOPENINTEXPORT int UF_UI_exit_dialog(void); /* <RETIRE_NXOPEN> */


/*****************************************************************************
When creating a Motif dialog it is required to use the visuals from
NX.  To do this you must ask for this information to be
returned back to you.  You must then set your visuals for your widget:

Visual   *visual;
Colormap cmap;
int      depth;
.
.
.
 UF_UI_ask_default_parent_info (&visual, &cmap, &depth);

 n = 0;
 XtSetArg( args[n], XmNvisual, visual); n++;
 XtSetArg( args[n], XmNcolormap, cmap); n++;
 XtSetArg( args[n], XmNdepth, depth); n++;
.
.
.
form = (Widget) XmCreateFormDialog ( parent, "form", args, n );



Environment: Internal

See Also:

History:
 Deprecated in NX 2406
 ****************************************************************************/
extern UGOPENINTEXPORT int UF_UI_ask_default_parent_info(
    Visual** visual, /* <I>
                     The default parent visual.
                     */
    Colormap* cmap, /* <I>
                    The default parent colormap.
                    */
    int* depth /* <I>
               The default parent depth.
               */
);  /* <RETIRE_NXOPEN> */


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
    const char* resource_file  /* <I>
                                The name of the vendor resource file to be loaded.
                                The name does not include the path.
                                */
); /*<NON_NXOPEN>*/


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
    const char* name,/* <I>
                 The name of the resource to be located.
                 */
    logical defvalue,/* <I>
                      The default value for the resource if not found.
                      */
    logical* value  /* <O>
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
    const char* name,/* <I>
                 The name of the resource to be located.
                 */
    double defvalue,/* <I>
                     The default value for the resource if not found.
                     */
    double* value  /* <O>
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
    const char* name,/* <I>
                 The name of the resource to be located.
                 */
    int defvalue,/* <I>
                  The default value for the resource if not found.
                  */
    int* value  /* <O>
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
    const char* name,/* <I>
                 The name of the resource to be located.
                 */
    const char* defvalue,/* <I>
                     The default value for the resource if not found.
                     */
    char   value[]  /* <O>
            The value of the resource.
            */
);/*<NON_NXOPEN>*/

#endif


/*
    Routing selection methods

    Use one of these values as the "method" parameter to 
    UF_UI_select_routing_objects to set the default selection method

    NOTE: The FLOW_PATH and FABRICATION selection methods are not
    currently implemented.

*/
#define UF_UI_ROUTE_SEL_METHOD_STANDARD      0
#define UF_UI_ROUTE_SEL_METHOD_PATH          1
#define UF_UI_ROUTE_SEL_METHOD_BRANCH        2
#define UF_UI_ROUTE_SEL_METHOD_ROUTING       3
#define UF_UI_ROUTE_SEL_METHOD_FLOW_PATH     4
#define UF_UI_ROUTE_SEL_METHOD_FABRICATION   5



/* 
    Selection type bits for Routing object selection

    The following defines are bit values that can be logically OR-ed 
    to specify the types of objects allowed for selection using the
    UF_UI_select_routing_objects routine.

    For example, to specify that Route Control Points and Segments
    may be selected, pass in UF_UI_ROUTE_SEL_RCP | UF_UI_ROUTE_SEL_SEG

*/
#define UF_UI_ROUTE_SEL_RCP     (1 << 0) /* enables selection of rcp-s     */
#define UF_UI_ROUTE_SEL_SEG     (1 << 1) /* enables selection of segments  */
#define UF_UI_ROUTE_SEL_STOCK   (1 << 2) /* enables selection of stock     */
#define UF_UI_ROUTE_SEL_PART    (1 << 3) /* enables selection of parts     */
#define UF_UI_ROUTE_SEL_PORT    (1 << 4) /* enables selection of ports     */
#define UF_UI_ROUTE_SEL_ANCHOR  (1 << 5) /* enables selection of anchors   */
#define UF_UI_ROUTE_SEL_STD     ( UF_UI_ROUTE_SEL_RCP   | \
                                  UF_UI_ROUTE_SEL_SEG   | \
                                  UF_UI_ROUTE_SEL_STOCK | \
                                  UF_UI_ROUTE_SEL_PART  | \
                                  UF_UI_ROUTE_SEL_PORT  | \
                                  UF_UI_ROUTE_SEL_ANCHOR )
#define UF_UI_ROUTE_SEL_INT_SEG (1 << 6) /* interior segments of a fitting */
#define UF_UI_ROUTE_SEL_INT_RCP (1 << 7) /* interior rcps of a fitting */
#define UF_UI_ROUTE_SEL_SPLINE_DATA (1 << 8) /* enables selection of spline points/extensions */
#define UF_UI_ROUTE_SEL_ALL     ( UF_UI_ROUTE_SEL_STD     | \
                                  UF_UI_ROUTE_SEL_INT_SEG | \
                                  UF_UI_ROUTE_SEL_INT_RCP | \
                                  UF_UI_ROUTE_SEL_SPLINE_DATA )
#define UF_UI_ROUTE_NONRM_RUN (1 << 9)
#define UF_UI_ROUTE_NONRM_LOGICAL (1 << 10)
#define UF_UI_ROUTE_SEL_CURVES (1 << 11)  /* enables selection of curves */

/*  */
/*
    Routing specify item modes.
*/
#define UF_UI_ROUTE_PLV_INDEX_PARTS                  0
#define UF_UI_ROUTE_PLV_INDEX_STOCK                  1
#define UF_UI_ROUTE_PLV_INDEX_OUTLET                 2
#define UF_UI_ROUTE_PLV_INDEX_ELBOWS                 3
#define UF_UI_ROUTE_PLV_INDEX_CUT_ELBOWS             4
#define UF_UI_ROUTE_PLV_INDEX_REPLACE_PART           5
#define UF_UI_ROUTE_PLV_INDEX_WIRES                  6
#define UF_UI_ROUTE_PLV_INDEX_CABLES                 7
#define UF_UI_ROUTE_PLV_INDEX_SHIELDS                8
#define UF_UI_ROUTE_PLV_INDEX_SPACE_RESERVATION      9
#define UF_UI_ROUTE_PLV_INDEX_FILLERS               10
#define UF_UI_ROUTE_PLV_INDEX_OVERSTOCK             11
#define UF_UI_ROUTE_PLV_INDEX_CABLE_CONDUITS        12
#define UF_UI_ROUTE_PLV_INDEX_PLATFORM_PLATE        13
#define UF_UI_ROUTE_PLV_INDEX_DUCT_REINFORCEMENT    14
#define UF_UI_ROUTE_PLV_INDEX_CONN_POST_PLACEMENT   15
#define UF_UI_ROUTE_PLV_INDEX_ENDFORMS              16
#define UF_UI_ROUTE_PLV_INDEX_HANGER                17

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RETIRING_UGOPENINT */
