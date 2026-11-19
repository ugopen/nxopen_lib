
/****************************************************************************
                Copyright (c) 1999,2000 Unigraphics Solutions, Inc.
                      Unpublished - All rights reserved
 *****************************************************************************
 *
 * File Name: uf_ui_param.h
 *
 * 
 *
 * File description:
 *
 *    This file contains the information required to use the UF_UI_PARAM module.
 *    This module allows the CAM User Function programmer to interface
 *    with the Graphical User Interface tools available to the UF_PARAM objects.
 *    The prototypes, descriptions and typedef's here will only be usable by
 *    Internal Open API programs.
 *
 ******************************************************************************/
#ifndef UF_UI_PARAM_H_INCLUDED
#define UF_UI_PARAM_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_cam_errors.h>
#include <libugopenint_cam_exports.h>

/***************************** Public Defines *********************************/

/***************************** Public Typedefs ********************************/

/************************* Public Function Definitions ************************/

/*****************************************************************************
 * This function displays the dialog for the object of the input "obj_tag".
 * The obj_tag has to be CAM object. The dialog that is displayed will be the
 * default dialog for the object. In the interactive session editing a CAM
 * object from the Operation Navigator causes the dialog of the object to be
 * brought up. Calling this function will have the same effect.
 *
 * Environment: Internal
 *
 * See Also:
 *
 * History: Originally released in V16.0
 ******************************************************************************/
extern UGOPENINT_CAMEXPORT int UF_UI_PARAM_edit_object
(
   tag_t  obj_tag,        /* <I> - tag of the UF_PARAM object for which the
                           *       dialog is requested
                           */
   int   *dialog_response /* <O> - Response from the dialog of the object
                           *       Possible values
                           *       UF_UI_OK
                           *       UF_UI_APPLY
                           *       UF_UI_BACK
                           *       UF_UI_CANCEL
                           */
);

/***************************************************************************
 *
 * This function queries the current object the manufacturing wizard
 * is working with. If there is no current object in the wizard process
 * the function will return NULL. The current object is returned through
 * the output parameter 'param_tag'
 *
 * Environment: Internal
 *
 * History: Released in NX4
 ************************************************************************/
extern UGOPENINT_CAMEXPORT int UF_CAM_wizard_ask_current_object
(
    tag_t *param_tag /*<O> see above */
);

/***************************************************************************
 *
 * This function sets the current object the manufacturing wizard
 * should work with. The object must exists in the current work part and
 * must be a valid manufacturing object.
 *
 * Environment: Internal
 *
 * History: Released in NX4
 ************************************************************************/
extern UGOPENINT_CAMEXPORT int UF_CAM_wizard_set_current_object
(
    tag_t param_tag /*<I> see above */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /*UF_UI_PARAM_H_INCLUDED*/
