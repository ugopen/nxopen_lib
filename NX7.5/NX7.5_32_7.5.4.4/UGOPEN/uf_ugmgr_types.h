/**************************************************************************

                  Copyright (c) 1998-1999 ,2000 Unigraphics Solutions Inc.
                             Unpublished - All rights reserved
***************************************************************************



File description:

    Contains the type definitions, enumerations, structure definitions,
    #defines and macros for NX Manager user functions.

***************************************************************************/

#ifndef UF_UGMGR_TYPES_H_INCLUDED
#define UF_UGMGR_TYPES_H_INCLUDED

/*

 */
#define ERROR_UGMGR_base    940000
#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

/* The following constants are the lengths of the various character strings
   without the trailing null.  If you use these parameters to allocate a buffer,
   you must add 1 for the trailing NULL.

    The Teamcenter limits for Item-Id and WSOM name are increased  form 32 to 128 chars.
    To support this Longer ID/Names, the NX/Manager basic limits
    for the Part-no and part-name and partfile-name are also increased to 128 chars.
*/
#define    UF_UGMGR_PARTNO_SIZE         128    /* part number length    -> increased to 128 to support TCE Longer ID/Names */
#define    UF_UGMGR_PARTREV_SIZE        32    /* part revision length     */
#define    UF_UGMGR_NAME_SIZE           128    /* name length           -> increased to 128 to support TCE Longer ID/Names */
#define    UF_UGMGR_TYPE_SIZE           32    /* part (item) type length  */
#define    UF_UGMGR_DESC_SIZE          240    /* part description length  */
#define    UF_UGMGR_FTYPE_SIZE          42    /* file type length, now from 9 'multi-CAD' + 1 '-' + 32 TC datasettype name */
#define    UF_UGMGR_FNAME_SIZE          128    /* file name length      -> increased to 128 to support TCE Longer ID/Names */
#define    UF_UGMGR_ROLE_SIZE           32    /* role length              */


/*******************************************************************************
This structure is used to define the parameters for a new part
specification in a customization of the new-part dialog in NX Manager.
*******************************************************************************/
struct UF_UGMGR_new_part_no_s
{
    const char* old_item;                           /* Seed name for the new
                                                       item id, this may
                                                       be NULL */
    const char* item_type;                          /* Name of item type for
                                                       which number is being
                                                       generated. */
    logical     part_number_modifiable;             /* Flag whether the user can
                                                       change the returned
                                                       value of new_id */
    char        new_id[UF_UGMGR_PARTNO_SIZE+1];     /* Returned string for new
                                                       part number, this may
                                                       be an empty string */
    logical     part_name_modifiable;               /* Flag whether the user
                                                       can change the returned
                                                       value of new_name */
    char        new_name[UF_UGMGR_NAME_SIZE+1];     /* Returned string for new
                                                       part name, this may be
                                                       an empty string */
    logical     part_description_modifiable;        /* Flag whether the user can
                                                       change the returned value
                                                       of new description. */
    char      new_description[UF_UGMGR_DESC_SIZE+1];/* Returned string for new
                                                       part description, this
                                                       may be an empty string.*/
    int         ifail;                              /* Failure code returned
                                                       from the user program,
                                                       zero is success.  */
};
typedef struct UF_UGMGR_new_part_no_s UF_UGMGR_new_part_no_t,
               *UF_UGMGR_new_part_no_p_t;

/******************************************************************************
This structure is used to define the parameters for a new part
specification in a customisation of the new-part dialog in
NX Manager.
******************************************************************************/
struct UF_UGMGR_new_part_rev_s
{
    const char* item;                               /* Seed name for new item
                                                       id, this may be NULL */
    const char* item_type;                          /* Name of item type for
                                                       which revision is being
                                                       generated. */
    logical     part_revision_modifiable;           /* Flag whether the user can
                                                       change the returned value
                                                       of new_revision.  */
    char      new_revision[UF_UGMGR_PARTREV_SIZE+1];/* Returned string for new
                                                       part revision, this may
                                                       be an empty string. */
    int         ifail;                              /* Failure code returned
                                                       from the user program,
                                                       zero is success.  */
};
typedef struct UF_UGMGR_new_part_rev_s UF_UGMGR_new_part_rev_t,
               *UF_UGMGR_new_part_rev_p_t;
/******************************************************************************
This structure may be used to define the parameters for a new part
specification in a customisation of the new-part dialog in
NX Manager.
*******************************************************************************/

struct UF_UGMGR_new_dataset_name_s
{
    const char* owner;                           /* Owner of existing dataset,
                                                    this may be NULL */
    const char* owner_revision;                  /* Revision name of owner */
    const char* dataset_type;                    /* Name of dataset type for
                                                    which a name is being
                                                    generated. */
    const char* relation_type;                   /* Name of relation between
                                                    owner and dataset */
    const char* basis_name;                      /* Basis name of new dataset
                                                    (this may be an empty
                                                     string)
                                                 */
    logical     dataset_name_modifiable;         /* Flag whether user can
                                                    change the returned value
                                                    of dataset_name */
    char      dataset_name[UF_UGMGR_NAME_SIZE+1];/* Returned string for new
                                                    dataset name, this may be
                                                    an empty string. */
    int         ifail;                        /* Failure code returned
                                                 from the user program,
                                                 zero is success. */
};
typedef struct UF_UGMGR_new_dataset_name_s UF_UGMGR_new_dataset_name_t,
                                          *UF_UGMGR_new_dataset_name_p_t;


/******************************************************************************
This structure may be used to define the parameters for a
non-master, dataset name in a customisation of the saveas master
part dialog in NX Manager.
******************************************************************************/
struct UF_UGMGR_saveas_dataset_name_s
{
    const char* old_owner;                       /* Owner of existing dataset,
                                                    this may be NULL.  */
    const char* old_owner_revision;              /* revision of owner of
                                                    existing dataset, this may
                                                    be NULL. */
    const char* old_dataset;                     /* Name of existing dataset,
                                                    this may be NULL.  */
    const char* relation_type;                   /* Name of relation type
                                                    between the owner and the
                                                    dataset. */
    const char* new_owner;                       /* Name of the new owner of
                                                    the dataset. */
    const char* new_owner_revision;              /* Revision of the new owner
                                                    of the dataset. */
    logical     dataset_name_modifiable;         /* Flag whether the user can
                                                    change the returned value
                                                    of dataset_name. */
    char      dataset_name[UF_UGMGR_NAME_SIZE+1];/* Returned string for saveas
                                                    dataset name, this may be
                                                    an empty string. */
    int         ifail;                           /* Failure code returned
                                                    from the user program,
                                                    zero is success. */
};
typedef struct UF_UGMGR_saveas_dataset_name_s UF_UGMGR_saveas_dataset_name_t,
               *UF_UGMGR_saveas_dataset_name_p_t;

/******************************************************************************

This structure is used to hold the input and output arguments to
UF_UGMGR_saveas_dataset_info, which supercedes
UF_UGMGR_saveas_dataset_name.  This user exit is called when
NX Manager is about to save a part with non-masters attached to it.
It collects information about how to save these non-masters and
returns it to NX.

******************************************************************************/

struct UF_UGMGR_saveas_dataset_info_s
{
    const char              *old_part_number;       /* Original item id */
    const char              *old_rev_name;          /* Original revision id */
    const char              *new_part_number;       /* New item id */
    const char              *new_rev_name;          /* New revision id */
    const char              *new_part_type;         /* New item type */
    int                     dataset_count;          /* Number of datasets */
    char                    **dataset_list;         /* Names of datasets */

    /* Return arguments; for arrays, it is one for each non-master dataset */
    char                    ***dataset_name_list;   /* Array of dataset names */
    int                     **copy_state;           /* Array of values, each one of
                                                       {USER_DATASET_always_copy,
                                                        USER_DATASET_never_copy,
                                                        USER_DATASET_user_chooses}
                                                        */
    logical                 **name_locked;          /* Array of values; indicates whether the
                                                       user is allowed to change the suggested name
                                                       returned from the user exit.
                                                       */
    logical                 **validation_required;  /* Array of values.  Indicates whether or not
                                                       the name must pass the validation check.
                                                       */
    logical                 **original_owner;       /* Array of values.  Indicates whether the
                                                       new non-masters are to be owned by the original
                                                       owner or by the user doing the saving.
                                                       */

    logical                 *allow_duplicates;      /* Whether or not duplicate non-master names are
                                                       allowed.
                                                       */

    int         ifail;                           /* Failure code returned
                                                    from the user program,
                                                    zero is success. */
};
typedef struct UF_UGMGR_saveas_dataset_info_s UF_UGMGR_saveas_dataset_info_t,
               *UF_UGMGR_saveas_dataset_info_p_t;

/******************************************************************************

This function is called by NX when it wants to ensure that a dataset
name is valid.  It is typically called in the context of saving an
existing part to a new part, and these details are passed to it in
case the function wants to use them to check the name.

******************************************************************************/

struct UF_UGMGR_validate_dataset_name_s
{
    const char              *old_part_number;       /* <I> Original item id */
    const char              *old_rev_name;          /* <I> Original revision id */
    const char              *new_part_number;       /* <I> New item id */
    const char              *new_rev_name;          /* <I> New revision id */
    const char              *new_part_type;         /* <I> New item type */
    const char              *new_dataset_name;      /* <I> */

    logical                 *valid;                 /* <O> Whether or not the name is considered valid  */

    int         ifail;                           /* Failure code returned
                                                    from the user program,
                                                    zero is success. */
};
typedef struct UF_UGMGR_validate_dataset_name_s UF_UGMGR_validate_dataset_name_t,
               *UF_UGMGR_validate_dataset_name_p_t;

typedef int (*UF_UGMGR_new_part_no_fn_t)(UF_UGMGR_new_part_no_p_t /* <I> */);
typedef int (*UF_UGMGR_new_part_rev_fn_t)(UF_UGMGR_new_part_rev_p_t /* <I> */);
typedef int (*UF_UGMGR_new_dataset_name_fn_t)(UF_UGMGR_new_dataset_name_p_t /* <I> */);
/*******************************************************************************
This structure is used to define the parameters for a new Alternate Identifier
as a customization of the Add Alternate... dialog in NX Manager.
*******************************************************************************/
struct UF_UGMGR_new_alternate_part_no_s
{
    tag_t        part_tag;                           /* Tag of part to assign
                                                        alternate ID. */
    const char  *context;                            /* Context for which an
                                                         alternate number
                                                         is being requested.  */
    const char  *id_type;                            /* ID type of part for
                                                        which  number is being
                                                        requested.May be NULL */
    char         alt_item_id[UF_UGMGR_PARTNO_SIZE+1];/* Alternate Item ID.  The
                                                        string must freed after
                                                        use with UF_free(). */
    char         alt_rev_id[UF_UGMGR_PARTREV_SIZE+1];/* Alternate Revision ID.
                                                        The string must freed
                                                        after use with UF_free()
                                                      */
    char         alt_name[UF_UGMGR_NAME_SIZE+1];     /* Returned string for new
                                                       part name, this may be
                                                       an empty string */
    char       alt_description[UF_UGMGR_DESC_SIZE+1];/* Returned string for new
                                                       part description, this
                                                       may be an empty string.*/
    logical      modifiable;                         /* Boolean;is the alternate
                                                        ID allowed to be
                                                        modified */
};
typedef struct UF_UGMGR_new_alternate_part_no_s UF_UGMGR_new_alternate_part_no_t,
               *UF_UGMGR_new_alternate_part_no_p_t;

typedef int (*UF_UGMGR_saveas_dataset_name_fn_t)
                                            (UF_UGMGR_saveas_dataset_name_p_t /* <I> */);
typedef int (*UF_UGMGR_saveas_dataset_info_fn_t)
                                            (UF_UGMGR_saveas_dataset_info_p_t /* <I> */);

typedef int (*UF_UGMGR_validate_dataset_name_fn_t)
                                            (UF_UGMGR_validate_dataset_name_p_t /* <I> */);
typedef int (*UF_UGMGR_new_alternate_part_no_fn_t)
                                            (UF_UGMGR_new_alternate_part_no_p_t /* <I> */);

/** PDM object types that can be accessed from NX Manager **/
enum UF_UGMGR_object_type_e
{
    UF_UGMGR_type_unknown,
    UF_UGMGR_type_folder,
    UF_UGMGR_type_part,
    UF_UGMGR_type_part_revision
} ;
typedef enum UF_UGMGR_object_type_e UF_UGMGR_object_type_t;

enum UF_UGMGR_partno_status_e
{
    UF_UGMGR_partno_valid,
    UF_UGMGR_partno_invalid,
    UF_UGMGR_partno_modified,
    UF_UGMGR_partno_override
} ;
typedef enum UF_UGMGR_partno_status_e UF_UGMGR_partno_status_t;

enum UF_UGMGR_alt_id_status_e
{
    UF_UGMGR_alt_id_valid,
    UF_UGMGR_alt_id_invalid,
    UF_UGMGR_alt_id_modified,
    UF_UGMGR_alt_id_override
} ;
typedef enum UF_UGMGR_alt_id_status_e UF_UGMGR_alt_id_status_t;

/** tags related to database **/
typedef    tag_t UF_UGMGR_tag_t;

#define UF_UGMGR_null_tag  ((UF_UGMGR_tag_t)0)

#define    UF_UGMGR_error_base                 ERROR_UGMGR_base + 3000
/** Error numbers for the errors returned **/
#define    UF_UGMGR_not_supported              (UF_UGMGR_error_base + 0)
#define    UF_UGMGR_apiserver_inactive         (UF_UGMGR_error_base + 1)
#define    UF_UGMGR_invalid_input              (UF_UGMGR_error_base + 2)
#define    UF_UGMGR_invalid_type               (UF_UGMGR_error_base + 3)
#define    UF_UGMGR_invalid_partno             (UF_UGMGR_error_base + 4)
#define    UF_UGMGR_invalid_partrev            (UF_UGMGR_error_base + 5)
#define    UF_UGMGR_invalid_fname              (UF_UGMGR_error_base + 6)
#define    UF_UGMGR_not_part_name              (UF_UGMGR_error_base + 7)
#define    UF_UGMGR_invalid_role               (UF_UGMGR_error_base + 8)
#define    UF_UGMGR_not_loaded_part            (UF_UGMGR_error_base + 9)
#define    UF_UGMGR_no_export_dir              (UF_UGMGR_error_base + 10)
#define    UF_UGMGR_part_does_not_exist        (UF_UGMGR_error_base + 11)
#define    UF_UGMGR_invalid_object             (UF_UGMGR_error_base + 12)
#define    UF_UGMGR_invalid_rule               (UF_UGMGR_error_base + 13)
#define    UF_UGMGR_part_exists                (UF_UGMGR_error_base + 14)
#define    UF_UGMGR_configured_rev_not_found   (UF_UGMGR_error_base + 15)
#define    UF_UGMGR_invalid_part_name          (UF_UGMGR_error_base + 16)
#define    UF_UGMGR_invalid_part_desc          (UF_UGMGR_error_base + 17)
#define    UF_UGMGR_invalid_seed               (UF_UGMGR_error_base + 18)
#define    UF_UGMGR_user_exit_failure          (UF_UGMGR_error_base + 19)
#define    UF_UGMGR_terminate_obsolete         (UF_UGMGR_error_base + 20)
#define    UF_UGMGR_iddisp_rule_not_in_pdm     (UF_UGMGR_error_base + 21)
#define    UF_UGMGR_invalid_altids_data        (UF_UGMGR_error_base + 22)
#define    UF_UGMGR_not_admin                  (UF_UGMGR_error_base + 23)
#define    UF_UGMGR_invalid_db_setting         (UF_UGMGR_error_base + 24)

#ifdef __cplusplus
}
#endif

#endif /* UF_UGMGR_TYPES_H_INCLUDED */
