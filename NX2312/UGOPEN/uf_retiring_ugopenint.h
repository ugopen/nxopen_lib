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
#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_disp_types.h>
#include <uf_sf_post_datatypes.h>

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
);

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
);

/*****************************************************************
Displays a WorldView help file page given the map file and the
WorldView locator.  This routine allows access to the help system
one level below the level of the routines UF_HELP_display_context and
UF_HELP_display_current_context. In the case of WorldView, the
UG translation map file contains the name of the map file and a
locator within the file.  It also allows the displaying of a WorldView
page by directly specifying the map file and locator.  Finally it
invokes WorldView if the program is not already running then loads
and positions the requested document page for viewing.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_display_wv(
char * map_file ,/* <I>
                 Name of map file to use.
                 */
char * locator  /* <I>
                World View locator
                */
);


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

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RETIRING_UGOPENINT */
