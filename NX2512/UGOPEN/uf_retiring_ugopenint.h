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

enum UF_DISP_image_format_e
{
    UF_DISP_PNG,
    UF_DISP_JPEG,
    UF_DISP_TIFF,
    UF_DISP_COMPRESSED_TIFF,
    UF_DISP_GIF,
    UF_DISP_XWD,  /*  Supported only on UNIX workstations     */
    UF_DISP_BMP   /*  Supported only on Windows workstations  */
};

typedef enum UF_DISP_image_format_e UF_DISP_image_format_t;

enum UF_DISP_background_color_e
{
    UF_DISP_ORIGINAL,
    UF_DISP_WHITE,
    UF_DISP_INVALID_COLOR
};

typedef enum UF_DISP_background_color_e UF_DISP_background_color_t;

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
); /* <NON_NXOPEN> */

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
); /* <NON_NXOPEN> */


#ifdef UNX

#include <Xm/Xm.h>


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


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RETIRING_UGOPENINT */
