/*****************************************************************************
                    Copyright (c) 2000 Unigraphics Solutions
                       Unpublished - All rights reserved
==============================================================================
File description:

This file contains prototype definitions for external routines defined in
the various UG/Routing sample programs provided as part of the UG/Open
kit.
==============================================================================
 
******************************************************************************/

#ifndef UFD_ROUTE_SAMPLE_INCLUDED
#define UFD_ROUTE_SAMPLE_INCLUDED

#include <uf_defs.h>
#include <uf_route.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Function prototypes */
/**********************************************************************
This is the prototype for a sample Routing callback function. 

Environment: Internal  and  External

See Also:


History: Created in V17.0
 ***********************************************************************/
extern  DllExport void handle_cb( 
    UF_ROUTE_cb_data_p_t callback /* <I>
                                     Pointer to data for the callaback.
                                     See ufd_route_sample_2.c for explanation
                                  */
    );
/**********************************************************************
This is the prototype for a sample Routing plug-in function. 

Environment: Internal  and  External

See Also:


History: Created in V18.0
 ***********************************************************************/
extern DllExport void compute_bundle( 
    UF_ROUTE_bundle_data_p_t bundle /* <I>
                                     Pointer to data for the plug-in
                                     See ufd_route_sample_3.c for explanation
                                    */
    );


/**********************************************************************
This is the prototype for a design rule that checks clip clearance.

Environment: Internal  and  External

See Also:


History: Created in V18.0
 ***********************************************************************/

extern DllExport void DESIGN_RULE_clip_clearance( 
        tag_t rule, /* <I> */
        UF_ROUTE_design_rule_data_p_t incoming /* <I> */
    );

#ifdef __cplusplus
}
#endif

#endif /* UFD_ROUTE_SAMPLE_INCLUDED */

