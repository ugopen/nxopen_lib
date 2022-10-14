/*****************************************************************************
             Copyright (c) 2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    UG/Open modeling routines to inquire, edit and update import body features.

*****************************************************************************/

#ifndef UF_MODL_IMPORT_BODY_H_INCLUDED
#define UF_MODL_IMPORT_BODY_H_INCLUDED

/*==========================================================================

  ==========================================================================*/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Is feature an import body feature ?

Environment:Internal and External
See Also:                                                   
History:                                                    
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_import_body_feature 
(
    tag_t    feature,               /* <I> Feature */
    logical *is_import_body_feature /* <O> TRUE if an import body feature, else FALSE */
);

/*----------------------------------------------------------------------------*/
typedef enum UF_MODL_import_body_feature_edit_option_e
{
    /*  
        Import body feature edit options.
    */
    UF_MODL_import_body_feature_update_link,   /* Update the link if it is out of date */
    UF_MODL_import_body_feature_redefine_link, /* Redefine the link */
    UF_MODL_import_body_feature_delete_link    /* Delete the link */
} UF_MODL_import_body_feature_edit_option_t, *UF_MODL_import_body_feature_edit_option_p_t;

/******************************************************************************
Edit import body feature by either reimporting the body from an out of date
file, importing the body from a new file or deleting the reference to the
file and converting the import body feature to an unparameterized feature.

Environment:Internal and External
See Also:                                                   
History:                                                    
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_import_body_feature 
(
    tag_t                                      import_body_feature, /* <I> Import body feature to edit */
    UF_MODL_import_body_feature_edit_option_t  edit_option,         /* <I> Update, redefine or delete link */ 
    const char                                *import_body_filename /* <I> Import body file name, if redefine link */
);

/******************************************************************************
Edit import body features by either reimporting the body from an out of date 
file or deleting the reference to the file and converting the import body 
feature to an unparameterized feature.  This is done for all loaded parts.

Environment:Internal and External
See Also:                                                   
History:                                                    
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_import_body_features 
(
    UF_MODL_import_body_feature_edit_option_t edit_option /* <I> Update or delete link */ 
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_IMPORT_BODY_H_INCLUDED */
