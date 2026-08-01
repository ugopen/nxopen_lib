/******************************************************************************

                        Copyright (c) 2003 EDS PLM Solutions
                        Unpublished - All rights reserved
====================================================================================================


File description: 
    Open C API motion interface

*****************************************************************************/

#ifndef UF_MOTION_UGOPENINT_H_INCLUDED
#define UF_MOTION_UGOPENINT_H_INCLUDED


/*****************************************************************************

******************************************************************************/

#include <uf_defs.h>
#include <libugopenint_cae_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************

This function runs animation using the motion data in the specified
spreadsheet. Last argument decides whether the animation will be run
interactively by bringing up the user interface or not.

Environment:  Internal and External

See Also:   UF_MOTION_spreadsheet_run_from_file

History:  Released in NX3
******************************************************************************/
extern UGOPENINT_CAEEXPORT int UF_MOTION_spreadsheet_run_from_file
(
    const char * spreadsheet_file,  /* <I> Full path and name of spreadsheet file
                                           containing motion data */
    int          start_step,        /* <I> Step number in spreadsheet to start
                                           animation at */
    int          end_step,          /* <I> Step number in spreasheet till which to
                                           animate */
    logical      invoke_ui          /* <I> TRUE if spreadsheet run should be
                                           interactive FALSE if animation should be
                                           run without the user interface */
);

/*****************************************************************************

This function runs the articulation solve in interactive mode using the existing user interface.

Environment:  Internal and External

See Also:   UF_MOTION_animation_run

History:  Released in NX801
******************************************************************************/
extern UGOPENINT_CAEEXPORT int UF_MOTION_articulation_run
( 
    void
);

/*****************************************************************************

This function runs animation in interactive mode using the existing user interface.

Environment:  Internal and External

See Also:   UF_MOTION_articulation_run

History:  Released in NX801
******************************************************************************/
extern UGOPENINT_CAEEXPORT int UF_MOTION_animation_run
( 
    void
);

#undef EXPORTLIBRARY

#ifdef __cplusplus
}
#endif

#endif     /* UF_MOTION_UGOPENINT_H_INCLUDED */
