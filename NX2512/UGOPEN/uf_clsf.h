/*****************************************************************************
                   Copyright (c) 2000-2003 Unigraphics Solutions
                        Unpublished - All Rights Reserved



File Description: 
  
Contains Open C API for the NX Oper module.
  
******************************************************************************/

#ifndef UF_CLSF_H
#define UF_CLSF_H


/*==========================================================================

  ==========================================================================*/

#include <uf_defs.h>
#include <uf_cam.h>
#include <libufun_cam_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/********************************** Defines ***********************************/

/******************************* Prototypes **********************************/


/*****************************************************************************
 * Function Name: UF_CLSF_import
 *
 * Function Description:
 *    This function imports the CLS tool paths into the part specified 
 *
 ******************************************************************************/
extern UFUN_CAMEXPORT int  UF_CLSF_import
(
   tag_t             part_tag, /* <I> 
                                 the NX part tag
                                */
   char             *clsf_name  /* <I> 
                                   the name of the cls file from which the tool paths are imported
                                 */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif
