/*******************************************************************************
            Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                     Unpublished - All rights reserved
*****************************************************************************
 * 
 *
 * File Description:
 *
 *    This file contains the documentation required for using the User
 *    Function Interface to DBC_MOLD. DBC_MOLD is the module that allows
 *    NX MOLD to interface with the external database that stores the
 *    user's data. Note that this is not a UF layer for DBC; it only handles 
 *    DBC_MOLD.
 * 
 ******************************************************************************/

#ifndef UF_DBC_MLD_H_INCLUDED
#define UF_DBC_MLD_H_INCLUDED

#include <uf_defs.h>
#include <uf_cam.h>
#include <libufun_cam_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/********************************** Defines ***********************************/


/********************************** TypeDefs **********************************/

/* UF_DBC_MLD_id_t is the identifier for referring to a UF_DBC_MLD object */
typedef void   *UF_DBC_MLD_id_t;

/* UF_DBC_MLD_sheet_t - the data structure into which a spreadsheet is read */
typedef void   *UF_DBC_MLD_sheet_t;


/******************************* Prototypes **********************************/


/*****************************************************************************
 *    This function returns the UF_DBC_MLD_id_t that corresponds to the 
 *    UF_CAM_exit_id_t passed to the User Exit from NX.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * 
 * History: Originally released in V16.0
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_DBC_MLD_ask_dbc_mld
(
   UF_CAM_exit_id_t   exit_id,     /* <I> - exit_id passed to exit from NX */
   UF_DBC_MLD_id_t   *dbc_mld_id   /* <O> - the dbc_mld of this exit_id */
);


/*****************************************************************************
 *    This function creates an UF_DBC_MLD object. The 'object' returned is
 *    used in the other public functions of UF_DBC_MLD to identify the
 *    object to process.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * 
 * History: Originally released in V16.0
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_DBC_MLD_create
(
   UF_DBC_MLD_id_t   *object     /* <O> - the id of the created object */
);


/*****************************************************************************
 *    This function will execute the specified command in the interpreter
 *    associated with the specified UF_DBC_MLD object.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * 
 * History: Originally released in V16.0
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_DBC_MLD_exec_command
(
   UF_DBC_MLD_id_t   dbc_mld_id, /* <I> - see above description */
   const char       *command     /* <I> - the command to execute */
);


/*****************************************************************************
 *    Returns the sheet associated with the specified UF_DBC_MLD_id_t.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * 
 * History: Originally released in V16.0
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_DBC_MLD_ask_sheet
(
   UF_DBC_MLD_id_t       object,  /* <I> - see above description */
   UF_DBC_MLD_sheet_t   *sheet    /* <O> - see above description */
);


/*****************************************************************************
 *    Assign the specified sheet to the specified UF_DBC_MLD_id_t.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * 
 * History: Originally released in V16.0
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_DBC_MLD_set_sheet
(
   UF_DBC_MLD_id_t      object,  /* <I> - see above description */
   UF_DBC_MLD_sheet_t   sheet    /* <I> - see above description */
);

/*****************************************************************************
 *    Assign the specified string to the result in the interpreter associated
 *    with the specified UF_DBC_MLD_id_t. This will be the return value of
 *    the last TCL command executed in the interpreter.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * 
 * History: Originally released in V16.0
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_DBC_MLD_set_interp_result
(
   UF_DBC_MLD_id_t   object, /* <I> - see above description */
   const char       *result  /* <I> - see above description */
);


/*****************************************************************************
 *    Delete the specified UF_DBC_MLD object.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * 
 * History: Originally released in V16.0
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_DBC_MLD_delete
(
   UF_DBC_MLD_id_t   object   /* <I> - the object to delete */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_DBC_MLD_H_INCLUDED */
