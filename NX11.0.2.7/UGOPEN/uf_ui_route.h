
/*****************************************************************************
 *                    Copyright (c) 1999-2006 UGS Corp.
 *                    Unpublished - All rights reserved
 *
 *============================================================================
 *
 * File Name: uf_ui_route.h
 *
 * 
 *
 * File description:
 *
 *    This file contains functions for the Routing interactive routines
 *    callable from Internal NX Open C programs. 
 *
 ******************************************************************************/
#ifndef UF_UI_ROUTE_H_INCLUDED
#define UF_UI_ROUTE_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <libugopenint_exports.h>

/***************************** Public Defines *********************************/

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
    Routing specify item modes.
*/

#define UF_UI_ROUTE_PLV_INDEX_PARTS             0
#define UF_UI_ROUTE_PLV_INDEX_STOCK             1
#define UF_UI_ROUTE_PLV_INDEX_OUTLET            2
#define UF_UI_ROUTE_PLV_INDEX_ELBOWS            3
#define UF_UI_ROUTE_PLV_INDEX_CUT_ELBOWS        4
#define UF_UI_ROUTE_PLV_INDEX_REPLACE_PART      5
#define UF_UI_ROUTE_PLV_INDEX_WIRES             6
#define UF_UI_ROUTE_PLV_INDEX_CABLES            7
#define UF_UI_ROUTE_PLV_INDEX_SHIELDS           8
#define UF_UI_ROUTE_PLV_INDEX_SPACE_RESERVATION 9
#define UF_UI_ROUTE_PLV_INDEX_FILLERS           10
#define UF_UI_ROUTE_PLV_INDEX_OVERSTOCK         11
#define UF_UI_ROUTE_PLV_INDEX_CABLE_CONDUITS    12

/*  */
/* Index used for identifying node of platform plate */
#define UF_UI_ROUTE_PLV_INDEX_PLATFORM_PLATE    13 

/*  */
/* Index used for identifying node of duct reinforcement*/
#define UF_UI_ROUTE_PLV_INDEX_DUCT_REINFORCEMENT    14

/*  */
/* Index used for identifying node for connection post placement parts*/
#define UF_UI_ROUTE_PLV_INDEX_CONN_POST_PLACEMENT   15


/***************************** Public Typedefs ********************************/

/************************* Public Function Definitions ************************/

/*****************************************************************************
Select Routing objects using the standard Routing selection tool

There must be an active part for this function to be called.

Environment: Internal

See Also:

History:Original release was in V18.0.
*****************************************************************************/
extern UGOPENINTEXPORT int UF_UI_select_routing_objects(
char * title ,       /* <I>
                        Dialog Title or Null
                     */
char * message,      /* <I>
                        Cue line message to display
                     */
int types,           /* <I>
                        Selectable Routing types - this should be specified by
                        logically OR-ing the desired types from the list of
                        types defined defined in uf_ui_route.h which have
                        a prefix of UF_UI_ROUTE_SEL.
                     */
int *method,         /* <I/O>
                        Default (starting) Routing selection method. This
                        should be one of the method definitions defined in
                        uf_ui_route.h starting with the prefix:

                        UF_UI_ROUTE_SEL_METHOD

                        This will be set to last selection method used by
                        the interactive user during this invocation. Using
                        this, you can "remember" the user's last method
                        setting for the next call
                     */
int scope,           /* <I>
                        Selection scope (include uf_ui.h)
                           UF_UI_SEL_SCOPE_NO_CHANGE
                           UF_UI_SEL_SCOPE_ANY_IN_ASSEMBLY
                           UF_UI_SEL_SCOPE_WORK_PART
                           UF_UI_SEL_SCOPE_WORK_PART_AND_OCC
                     */
int * response,      /* <O>
                        UF_UI_BACK
                        UF_UI_CANCEL
                        UF_UI_OK
                     */
int *count,          /* <O>
                        Count of objects selected.  0 if no objects selected.
                     */
tag_p_t *objects     /* <OF,len:count>
                        Array of object identifiers of the selected objects.
                        This must be freed with UF_free.
                     */
);

/*****************************************************************************
Execute Routing callback functions(internal\external) on passed in objects.

There must be an active part for this function to be called.

Environment: Internal

See Also:

History:Original release was in NX404 IP2 MP4
*****************************************************************************/
extern UGOPENINTEXPORT int UF_UI_route_invoke_callback(
    char *     call_back_name,  /* <I>
                                   Callback Name
                                   The list of available callbacks is documented in the 
                                   ugroute_mech_mm.xml file under the Callbacks section.
                                 */
    int        num_objects,     /* <I>
                                   Number of objects being passed to the callback
                                 */
    tag_t*     objects          /* <I>
                                   Array of objects to pass
                                 */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /*UF_UI_ROUTE_H_INCLUDED*/
