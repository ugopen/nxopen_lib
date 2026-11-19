/*==================================================================================================

            Copyright (c) 2014 Siemens Product Lifecycle Management Software Inc.
                            Unpublished - All rights reserved

====================================================================================================


File Description:

Modeling functions that are specific to VDA   

=============================================================================*/
#ifndef UF_MODL_VDAC_H_INCLUDED
#define UF_MODL_VDAC_H_INCLUDED

#include <uf_defs.h>
#include <libufun_vdac_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/************************************************************************
Analyzes curves, surfaces and drawings for quality according to
specified check criteria which include those described by VDA 4955.
The results of an analysis run will be saved and allow error
tracing of failing objects.

Environment : Internal  and  External
See Also:
History :
 ************************************************************************/
extern UFUN_VDACEXPORT int UF_MODL_ask_vda_4955_compliance
(
    tag_t part,             /* <I>
                            NX part tag, required
                            */
    char *cfg_file_name,    /* <I>
                            VDA Checker configuration file name, required
                            */
    char *log_file_name,    /* <I>
                            Results Log file name, optional.  If NULL, the file
                            name (*.log) is derived from the NX part file name.
                            The file will be placed into the first directory
                            with write permission in the order:
                            1. Same directory as the NX part file
                            2. Working directory
                            3. system defined temporary directory
                            */
    char *ceo_file_name     /* <I>
                            Compliance Error Objects file name, optional.
                            This file will contain the session independent
                            compliance error lists. This may be reloaded during
                            a subsequent dialog session for further error
                            diagnostic.

                            If NULL is provided the file name (*.ceo) is derived
                            from the NX part file name. The file will be placed
                            into the first directory with write permission in
                            the order:
                            1. Same directory as the NX part file
                            2. Working directory
                            3. system defined temporary directory
                            */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_MODL_VDAC_H_INCLUDED */
