/*******************************************************************************
             Copyright (c) 2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       




File description:

    Open C API interface to the Routing (ROUTE) module.

	Please refer to uf_route.h's documentation for a discussion of Concepts
	and Terminology.
******************************************************************************/
#ifndef UF_ROUTE_UGOPENINT_H_INCLUDED
#define UF_ROUTE_UGOPENINT_H_INCLUDED


/**************
 ** Includes **                                   
 **************/

#include <libugopenint_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*********************************************************************
                      ** Function Prototypes **
 ********************************************************************/

/* Custom Routing Applications */

/**********************************************************************
Registers a Routing custom application. This routine should be
called just after UF_MB_register_application().

Environment: Internal

See Also:


History: Original release was in V14.0.
**********************************************************************/
extern UGOPENINTEXPORT int UF_ROUTE_register_custom_app( 
int app_id /* <I>
           Application ID for this application.  This is returned
           from UF_MB_register_application.
           */
);

/**********************************************************************
Enters a custom Routing application.

Environment: Internal

See Also:


History: Original release was in V14.0.
**********************************************************************/
extern UGOPENINTEXPORT int UF_ROUTE_enter_custom_app( void );

/**********************************************************************
Initializes a Routing custom application.

Environment: Internal

See Also:


History: Original release was in V14.0.
 ***********************************************************************/
extern UGOPENINTEXPORT int UF_ROUTE_init_custom_app( void );

/**********************************************************************
Exits a custom Routing application.

Environment: Internal

See Also:


History: Original release was in V14.0.
 ***********************************************************************/
extern UGOPENINTEXPORT int UF_ROUTE_exit_custom_app( void );

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_ROUTE_UGOPENINT_H_INCLUDED */
