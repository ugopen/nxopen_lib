/*******************************************************************************
             Copyright (c) 1995-2003 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       

******************************************************************************


File Description:

This is the Open C API interface to User-Defined Operations.

The user should use either an attribute (see uf_attr.h) or a User Defined 
Object (see uf_udobj.h) to associate data with a User Defined Operation. If 
the data is of type integer, double or string one can use either an attribute 
or a User Defined Object. If the data is a link to another object and that 
link must be considered for update and delete processing then a User Defined 
Object is most appropriate. Attributes are simpler to use than User Defined 
Objects but don't allow for automatic update and delete processing. User 
Defined Objects do participate in update and delete processing.

See uf_attr.h and uf_udobj.h and the Open API User Documentation for more 
information.

******************************************************************************/

#ifndef UF_UDOP_H
#define UF_UDOP_H


/***************************************************************************

  ***************************************************************************/


/***************************************************************************

  ***************************************************************************/
#include <uf_defs.h>
#include <uf_cam.h>
#include <uf_oper.h>
#include <libufun_cam_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/********************************** Defines ***********************************/


/********************************** TypeDefs **********************************/

/* UF_UDOP_id_t is the identifier for referring to a UF_UDOP */
typedef void   *UF_UDOP_id_t;


/*****************************************************************************
   
   The following enum describes the purposes a UDO may be calling a User
   Exit.
******************************************************************************/
enum UF_UDOP_purpose_e
{
   UF_UDOP_USER_PARAMS,  /* The user exit is being called so it can
                            do whatever processing it wishes to
                            capture the parameters for generating this
                            operation's toolpath.
                         */
   UF_UDOP_GENERATE      /* The user exit is being called to generate
                            the tool path for this operation.
                         */
};

typedef enum UF_UDOP_purpose_e UF_UDOP_purpose_t;

/****************************************************************************

   NOTE :

    A User Defined Operation identifier of the type UF_UDOP_id_t has to be 
    used as the input for all functions querying an User Defined operation

*****************************************************************************/

/******************************* Prototypes **********************************/


/*****************************************************************************
Returns the UF_UDOP_id_t that corresponds to the UF_CAM_exit_id_t passed to 
the User Exit from NX.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDOP_ask_udop(
UF_CAM_exit_id_t exit_id ,/* <I>
                          exit_id passed to user exit from NX
                          */
UF_UDOP_id_t* udop_id  /* <O>
                       The udop of this exit_id
                       */
);

/*****************************************************************************
Returns an Operation Identifier for the input UF_UDOP_id_t.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDOP_ask_oper(
UF_UDOP_id_t udop_id ,/* <I>
                      The udop of requested oper
                      */
UF_OPER_id_t* oper_id  /* <O>
                       The oper of this udop_id
                       */
);

/*****************************************************************************
Returns why the User Exit is being called. The purpose must be of type 
UF_UDOP_purpose_t.

Environment: Internal  and  External

See Also: See  UF_UDOP_purpose_t 

History:
******************************************************************************/
extern UFUN_CAMEXPORT int UF_UDOP_ask_purpose(
UF_UDOP_id_t udop_id ,/* <I>
                      The udop of requested operation.
                      */
UF_UDOP_purpose_t* purpose  /* <O>
                            The reason the User Exit was called
                            */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif
