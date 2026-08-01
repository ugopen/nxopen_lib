/*****************************************************************************
             Copyright (c) 2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about mswp.
*****************************************************************************/

#ifndef UF_MODL_MSWP_H_INCLUDED
#define UF_MODL_MSWP_H_INCLUDED


/*==========================================================================

  ==========================================================================*/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <uf_modl_mswp_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
This is to initialize the data structure for an extrude feature with the
following default values and options. 

    Section                    NULL_TAG
    Direction                  NULL_TAG
    Limit Type                 UF_MODL_MSWP_LIMIT_DISTANCE 
    Start Limit Distance       0.0/0.0   [in/mm]
    End Limit Distance         1.0/25.0  [in/mm]
    Taper Type                 UF_MODL_MSWP_TAPER_NONE
    Offset Type                UF_MODL_MSWP_OFFSET_NONE
    Boolean Sign               UF_NULLSIGN [create]
    Boolean Target             NULL_TAG

Environment: Internal  and  External
See Also: UF_MODL_mswp_create_extrude, UF_MODL_mswp_edit_extrude, UF_MODL_mswp_ask_extrude.
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_mswp_init_extrude_data(
UF_MODL_mswp_extrude_p_t extrude
                        /* <I/O>
                        The extrude data structure to be initialized.
                        */
);

/****************************************************************************
This is to create an extrude feature based on the input data. 

Environment: Internal  and  External
See Also: UF_MODL_mswp_edit_extrude, UF_MODL_mswp_ask_extrude.
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_mswp_create_extrude(
UF_MODL_mswp_extrude_p_t extrude, 
                        /* <I>
                        Input data to be used to create Extrude feature.
                        */
int *num_features,      /* <O> Number of features */
tag_t  **features       /* <OF>
                        List of feature identifiers created.  This 
                        must be freed by caller.
                        */
);

/****************************************************************************
This is to inquire the data for an extrude feature.

Environment: Internal  and  External
See Also: UF_MODL_mswp_edit_extrude, UF_MODL_mswp_create_extrude.
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_mswp_ask_extrude(
tag_t feature,          /* <I> 
                        Extrude feature to be asked */
UF_MODL_mswp_extrude_p_t extrude 
                        /* <O>
                        Data for the Extrude feature.
                        */
);

/****************************************************************************
This is to edit an extrude feature with given data.  The good practice to
edit a feature is to follow the following steps: 

    Call UF_MODL_mswp_ask_extrude to get the data
    Make necessary changes to the data
    Call UF_MODL_mswp_edit_extrude

Environment: Internal  and  External
See Also: UF_MODL_mswp_ask_extrude, UF_MODL_mswp_create_extrude.
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_mswp_edit_extrude(
tag_t feature,          /* <I/O> 
                        Extrude feature to be edited*/
UF_MODL_mswp_extrude_p_t extrude 
                        /* <I>
                        Data for the Extrude feature.
                        */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_MSWP_H_INCLUDED */
