
/****************************************************************************
                Copyright (c) 1999,2000 Unigraphics Solutions, Inc.
                      Unpublished - All rights reserved
 ****************************************************************************
 *
 * File Name: uf_ui_ont.h
 *
 * 
 *
 * File description:
 *
 *    This file contains the utility functions for the UF_UI_ONT module.
 *    This module allows the CAM User Function programmer to interface
 *    with the Operation Navigation Tool(ONT). The prototypes, descriptions
 *    and typedef's here will only be usable by Internal Open API programs.
 *
 ******************************************************************************/
#ifndef UF_UI_ONT_H_INCLUDED
#define UF_UI_ONT_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_cam_errors.h>
#include <libugopenint_cam_exports.h>

/***************************** Public Defines *********************************/
typedef enum
{
    UF_UI_ONT_order = 0,      /*  program view  */
    UF_UI_ONT_machine_mode,   /*  method view   */
    UF_UI_ONT_geometry_mode,  /*  geometry view */
    UF_UI_ONT_machine_tool,   /*  tool view     */
    UF_UI_ONT_NUM_TREE_MODES
}  UF_UI_ONT_tree_mode_t;

/***************************** Public Typedefs ********************************/

/************************* Public Function Definitions ************************/

/*****************************************************************************
 * This function returns the number and the tags of the selected nodes in
 * the active view of the Operation Navigation Tool(ONT).
 *
 * Environment: Internal
 *
 * See Also:
 *
 * History: Originally released in V16.0
 ******************************************************************************/
extern UGOPENINT_CAMEXPORT int UF_UI_ONT_ask_selected_nodes
(
   int   *count,     /* <O> - Number of selected nodes ****/
   tag_t **objects   /* <OF,len:count> - the tags of the selected nodes.
                      *        The returned array must be freed by calling
                      *        UF_free.
                      */
);


/*****************************************************************************
 * This function refreshes the operation navigator.
 *
 * Return:
 *   = 0  Successful
 *   other  failing error number
 *
 * Environment: Internal
 *
 * See Also:
 *
 * History: Originally released in V19.0
 *****************************************************************************/
extern UGOPENINT_CAMEXPORT int UF_UI_ONT_refresh
(
    void
);

/*****************************************************************************
 * This function changes the view of the ONT to the specified view
 *
 * Return:
 *   = 0  Successful
 *   other  failing error number
 *
 * Environment: Internal
 * 
 * See Also:
 *
 * History: Originally released in NX3
 *****************************************************************************/
extern UGOPENINT_CAMEXPORT int UF_UI_ONT_switch_view
(
    UF_UI_ONT_tree_mode_t view /* <I> */
);

/*****************************************************************************
 * This function returns the current view mode of the ONT
 *
 * Return:
 *   = 0  Successful
 *   other  failing error number
 *
 * Environment: Internal
 * 
 * See Also:
 *
 * History: Originally released in NX3
 *****************************************************************************/
extern UGOPENINT_CAMEXPORT int UF_UI_ONT_ask_view
(
    UF_UI_ONT_tree_mode_t *view /* <O> */
);

/*****************************************************************************
 * This function expands all nodes of the current view
 *
 * Return:
 *   = 0  Successful
 *   other  failing error number
 *
 * Environment: Internal
 * 
 * See Also:
 *
 * History: Originally released in NX3
 *****************************************************************************/
extern UGOPENINT_CAMEXPORT int UF_UI_ONT_expand_view
(
    void
);

/*****************************************************************************
 * This function collapses all nodes of the current view
 *
 * Return:
 *   = 0  Successful
 *   other  failing error number
 *
 * Environment: Internal
 * 
 * See Also:
 *
 * History: Originally released in NX3
 *****************************************************************************/
extern UGOPENINT_CAMEXPORT int UF_UI_ONT_collapse_view
(
    void
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /*UF_UI_ONT_H_INCLUDED*/
