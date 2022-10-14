/****************************************************************************

           Copyright (c) 2000 Unigraphics Solutions Inc.
                         Unpublished - All rights reserved

 File description:  
          These routines are in the process of being removed from the UG/Open
          product.  Customers should use the designated replacement routines
          instead of the routines listed here.  Once a routine is placed
          here, it is eligible to be removed in the next release of Unigraphics.
 
****************************************************************************/

/*
 

*/

#ifndef UF_RETIRING_UGOPENINT
#define UF_RETIRING_UGOPENINT
#include <uf_defs.h>
#include <uf_sf_post_datatypes.h>
#include <libugopenint_exports.h>
/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif


/*****************************************************************
Displays a WorldView help file page given the map file and the
WorldView locator.  This routine allows access to the help system
one level below the level of the routines UF_HELP_display_context and
UF_HELP_display_current_context. In the case of WorldView, the
UG translation map file contains the name of the map file and a
locator within the file.  It also allows the displaying of a WorldView
page by directly specifying the map file and locator.  Finally it
invokes WorldView if the program is not already running then loads
and positions the requested document page for viewing.

Environment: Internal
See Also:
History:
 *****************************************************************/
extern UGOPENINTEXPORT int UF_HELP_display_wv(
char * map_file ,/* <I>
                 Name of map file to use.
                 */
char * locator  /* <I>
                World View locator
                */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_RETIRING_UGOPENINT */
