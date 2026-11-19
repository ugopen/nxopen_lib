/*****************************************************************************
             Copyright (c) 2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
    Open modeling routines to inquire, edit and update import body features.

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
Is input_tag an import body feature or involved with an Interop part/feature?

The argument input_tag can be NULL_TAG, in which case the current work part is determined
to be an Interop part.  It can be the tag of a part, in which case that part is determined
to be an Interop part.  Or it can be the tag of a feature, in which case the feature is determined
to be an Interop feature or an import body feature.

Environment:Internal and External
See Also:                                                   
History:                                                    
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_is_import_body_feature 
(
    tag_t    input_tag,               /* <I> The tag to check */
    logical *is_import_body_feature   /* <O> TRUE if Interop or an import body feature, else FALSE */
);

/*  
        Import body feature edit options.
*/
enum UF_MODL_import_body_feature_edit_option_e
{
    UF_MODL_import_body_feature_update_link,   /* Update the link if it is out of date */
    UF_MODL_import_body_feature_redefine_link, /* Redefine the link */
    UF_MODL_import_body_feature_delete_link    /* Delete the link */
};
typedef enum UF_MODL_import_body_feature_edit_option_e
             UF_MODL_import_body_feature_edit_option_t, *UF_MODL_import_body_feature_edit_option_p_t;

/******************************************************************************
Edit the input tag.

The argument input_tag can be NULL_TAG, in which case the current work part is updated as an Interop
part.  The update can either be from an out-of-date foreign part file, a specified different foreign
part file, or deleting the reference to the foreign part file.

The argument can be the tag of a part, in which case that part is updated as an Interop part.  The
update can either be from an out-of-date foreign part file, a specified different foreign part file,
or deleting the reference to the foreign part file.

Or it can be the tag of a feature, in which case the feature is determined to be an Interop feature
or an import body feature.  If the feature is an Interop feature, then the part of the feature is updated.
The update can either be from an out-of-date foreign part file, a specified different foreign part file,
or deleting the reference to the foreign part file.  If the feature is an import body feature, then it is
editted by either reimporting the body from an out of date file, importing the body from a new file, or
deleting the reference to the file and converting the import body feature to an unparameterized feature.

Environment:Internal and External
See Also:                                                   
History:                                                    
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_import_body_feature
(
    tag_t                                      input_tag,           /* <I> Object to edit */
    UF_MODL_import_body_feature_edit_option_t  edit_option,         /* <I> Update, redefine or delete link */ 
    const char                                *import_body_filename /* <I> Import body file name, if redefine link */
);

/******************************************************************************
Edit features in loaded part files.

If the current work part is an Interop part then that part will be updated from an out-of-date foreign
part file or deleting the reference to the foreign part file.

If the current work part is not an Interop part then import body features are editted by either
reimporting the body from an out of date file or deleting the reference to the file and converting
the import body feature to an unparameterized feature.  This is done for all loaded parts.

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
