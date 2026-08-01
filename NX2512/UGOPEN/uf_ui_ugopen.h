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
