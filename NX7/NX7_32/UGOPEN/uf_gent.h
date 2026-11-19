/*******************************************************************************

             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File Description:
   This include file contains the prototypes and descriptions of the
   generic entity/object functions that follow the old naming convention.

   FYI:
   To avoid confusion with uf_obj.h which does operations on objects,
   this file has maintained using the term entity when referring to generic
   entities (in lieu of generic objects).  Else this file would have the
   prefix uf_gobj.h.  However, object is the correct term.
  *****************************************************************************/

#ifndef UF_GENT_INCLUDED
#define UF_GENT_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libufun_exports.h>
#include <uf_retiring.h>



#ifdef __cplusplus
extern "C" {
#endif



/****************************************************************************
   Old naming convention prototypes - Generic Entities/Objects functions
  **************************************************************************/

/*****************************************************************************
 *****     WARNING:  The routines that follow will be obsoleted in        ****
 *****     soon.  Do not use them!  Use their indicated replacements.     ****
 ****************************************************************************/

/* uc6573 add/append character data to a generic entity
   -- replaced by UF_UDOBJ_add_strings */
extern UFUNEXPORT int uc6573(tag_t np1, int jp2, char cp3[][133]);

/* uc6578 read character data from a generic entity
   -- replaced by UF_UDOBJ_ask_udo_data */
extern UFUNEXPORT int uc6578(tag_t np1, int jp2, int jp3, char cr4[][133]);

/* uc6582 modify character data in a generic entity
   -- replaced by UF_UDOBJ_ask_udo_data
      and UF_UDOBJ_edit_strings */
extern UFUNEXPORT int uc6582(tag_t np1, int jp2, int jp3, char cp4[][133]);

/* uf6586 set/reset a generic entity modified
   -- replaced by UF_UDOBJ_clear_udo_status */
extern UFUNEXPORT void FTN(uf6586)(const tag_t *np1, const int *ip2, int *ir3);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif   /* END UF_GENT_INCLUDED */

