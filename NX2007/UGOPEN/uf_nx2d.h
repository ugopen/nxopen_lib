/*******************************************************************************

             Copyright (c) 2002 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved



File description:

    Open API interface routine to enable users to import NX2D data into NX
    parts as model geometry on the specified orientation planes.

================================================================================
*/

#ifndef UF_NX2D_H_INCLUDED
#define UF_NX2D_H_INCLUDED

#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Imports an NX-2D file into NX.  The geometry imported will be created in
the current work part.

Return:
        Return code:
        0 = No error
        not 0 = Error code

Environment: Internal  and  External

See Also:

History: Originally released in nx1.0.1
 ******************************************************************************/
extern UFUNEXPORT int UF_NX2D_import_file(
    const char *filename,            /* <I>
                                        File specification for the NX2D
                                        file to import.
                                      */
    logical skip_hidden_wireframe,   /* <I>
                                        Not used.  The NX2D import file will
                                        not contain hidden wireframe geometry
                                        in the first place so this parameter
                                        has no effect.  May be True or False.
                                      */
    logical import_as_sketch         /* <I>
                                        If TRUE, the NX-2D wireframe data
                                        will be imported as sketches.
                                      */
);/*<NON_NXOPEN>*/

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_NX2D_H_INCLUDED */
