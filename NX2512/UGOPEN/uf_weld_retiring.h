/*==================================================================================================

            Copyright (c) 2014 Siemens Product Lifecycle Management Software Inc.
                            Unpublished - All rights reserved

====================================================================================================



 File description:
          These routines are in the process of being removed from the NX Open API
          product.  Customers should use the designated replacement routines
          instead of the routines listed here.  Once a routine is placed
          here, it is eligible to be removed in the next release of NX.

====================================================================================================*/

#ifndef UF_WELD_RETIRING
#define UF_WELD_RETIRING
#include <uf_defs.h>
#include <uf_weld_types.h>
#include <libufun_weld_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************
 To fetch an array of all weld objects in the specified assembly.
Optionally, filter the weld objects by weld type.
The weld_array must be freed using UF_free.

Environment : Internal and External
See Also :

History : Originally released in v16.0.1
This function should be replaced by UF_WELD_locate_welds2
*****************************************************************************/
extern UFUN_WELDEXPORT int UF_WELD_locate_welds(
tag_t           work_part,   /* <I>
                                The specified assembly to query
                             */
UF_WELD_types_t weld_type,   /* <I>
                                The weld type filter to apply to this query.
                                If no filtering is desired, then input
                                UF_WELD_ALL_TYPES . This filter can have
                                combinations like UF_WELD_GROOVE_TYPE+
                                UF_WELD_SPOT_TYPE+...
                             */
int             *count,      /* <O>
                                Pointer to the number of weld object which
                                answer the query. This may be 0.

                                This storage is not allocated by the
                                function. Pass in a valid integer location

                                If the count is not desired, pass in a NULL
                                instead of a pointer
                             */
tag_p_t         *weld_array  /* <OF,len:count>
                                The pointer in which to return the array
                                containing the tags of the found
                                weld_objects. If UF_WELD_ALL_TYPES,
                                then all of the weld objects in the
                                assembly will be returned. If any other
                                filter option, then only the objects of
                                the specified type are returned.

                                If NULL is passed in instead of a pointer,
                                then the array is not returned.
                                Such an option might be used to simply
                                obtain a count of the objects.

                                If the pointer is returned as non_NULL,
                                then the array must be freed by UF_free
                              */
                                           );

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_WELD_RETIRING */
