/*****************************************************************************
             Copyright (c) 1995-2003 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File Description:
 This file contains the documentation required for using the Open API
 Interface to the pre-v16 Oper module.

 ******************************************************************************/

#ifndef UF_OPER__SPEC_H
#define UF_OPER__SPEC_H


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_cam.h>
#include <uf_path.h>
#include <uf_oper_spec.h>
#include <libufun_cam_exports.h>

/***************************************************************************

  ***************************************************************************/
#define ERROR_UF_OPER_base     1360000

#ifdef __cplusplus
extern "C" {
#endif

/********************************** Defines ***********************************/

#define UF_OPER_OPNAME_NCHARS 133 
#define UF_OPER_OPNAME_BUFSIZE NX_BUFSIZE(UF_OPER_OPNAME_NCHARS)

/*  */
#define UF_OPER_OPNAME_LEN (UF_OPER_OPNAME_BUFSIZE-1)
/*  */

#define ERROR_UF_OPER_WRONG_OPER_TY       (ERROR_UF_OPER_base + 1)
#define ERROR_UF_OPER_NOT_IMPLEMENTED     (ERROR_UF_OPER_base + 2)
#define ERROR_UF_OPER_INVALID_PARAMETER   (ERROR_UF_OPER_base + 3)

/****************************************************************************

   NOTE :

    An operation identifier of the type UF_OPER_id_t has to be used as the
    input for all functions querying an operation

*****************************************************************************/

/********************************* Typedefs *********************************/

/* UF_OPER_id_t is the identifier for referring to a UF_OPER */
typedef void   *UF_OPER_id_t;


/******************************* Prototypes **********************************/


/*****************************************************************************
Returns the UF_oper_id_t that corresponds to the UF_CAM_exit_id_t passed to the
User Exit from NX.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_oper(
UF_CAM_exit_id_t exit_id ,/* <I>
                          exit_id passed to user exit from NX
                          */
UF_OPER_id_t * oper_id  /* <O>
                        Operation Identifier
                        */
);

/*****************************************************************************
This function copies the Operation name associated with "oper_id" to the memory
pointed at "op_name". This memory must be the same as UF_OPER_OPNAME_BUFSIZE bytes.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_name(
UF_OPER_id_t oper_id ,/* <I>
                      Operation identifier
                      */
char  op_name[UF_OPER_OPNAME_BUFSIZE]  /* <O>
                Pointer to at least UF_OPER_OPNAME_BUFSIZE bytes
                */
);

/*****************************************************************************
Returns the path identifier associated with "oper_id".

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_OPER_ask_path(
UF_OPER_id_t oper_id ,/* <I>
                      Operation identifier
                      */
UF_PATH_id_t * path_id  /* <O>
                        Path identifier of this oper's path
                        */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_OPER_SPEC_INCLUDED */
