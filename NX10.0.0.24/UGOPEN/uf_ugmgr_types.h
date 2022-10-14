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
#include <uf_attr_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
* NX and TC are both moving to supporting string limits based on number of characters rather than
* on the number of bytes.  At the same time NX is moving to support multi-byte data everywhere, and 
* so buffer sizes will need to increase to support this.  These transitions will take place over 
* several releases, and so new definitions are being introduced that will help during the 
* transition period starting with NX 9.  
*
* The following constants with the "_SIZE" suffixes are the fixed allocated lengths of their
* corresponding TC Database fields in bytes (as of TC10) - independent of the character encoding 
* actually used when they are stored there. Each TC Database must use the same encoding for all
* of its strings. These are meant to be used only for string length limit validations.
*
* The constants with the "_NCHARS" suffix are number of characters the string are limited to. However,
* They are not to be used directly in the TCIN code as we are currently byte-limited to the "_SIZE"'s.
*
* The constants with the "_BUFSIZE" suffix are number of bytes to be used to allocate "char*" buffers to hold
* those strings in NX code. They include one more byte to add the trailing null "\0" terminator.  
* These are meant only for char* buffer allocations to make sure that they can hold "_NCHARS"
* characters in any language when encoded in UTF-8. They are not to be used for TC DB string length limit
* validations. Also
* once NX transitions to multi-byte character support, the NX_BUFSIZE() macro will guarantee that the
* buffers are large enough to hold the number of characters indicated.  So user written code allocating
* buffers should be switched use the _BUFSIZE definitions.
*
* New routines have been added which will help in this transition:
*     UF_TEXT_count_characters() will count the number of characters in a buffer.
*     UF_TEXT_terminate_chars() will terminate a C string after the given number of characters.
*

* The Teamcenter limits for Item-Id and WSOM name were previously increased from 32 to 128 chars.
* To support these Longer ID/Names, the NX/Manager basic limits for the Part-no and Part-name 
* and Part File-name were also increased to 128 chars.
*
* Teamcenter 10.x or before the database fields are limited by a number of bytes, so the 
* xxx_LIMIT values will be a byte based limit.  In Teamcenter 11 or later, the xxx_LIMIT 
* values will be character based because the database is limited by characters.  The 
* xxx_SIZE definitions are being deprecated as they were used for both declaring buffers 
* and limiting the data in those buffers.  The xxx_BUFSIZE should now be used to declare 
* buffers, as they will be big enough to hold the maximum amount of data, when working 
* with Teamcenter 11 and multi-byte data.
*/
#define    UF_UGMGR_PARTNO_LIMIT        900  /**< Part (Item) Number length in chars; increased to 128 to support TC Longer ID/Names */
#define    UF_UGMGR_PARTNO_BUFSIZE      NX_BUFSIZE(UF_UGMGR_PARTNO_LIMIT)  

#define    UF_UGMGR_PARTREV_LIMIT       32    /**< Part (Item) Revision length in chars */
#define    UF_UGMGR_PARTREV_BUFSIZE     NX_BUFSIZE(UF_UGMGR_PARTREV_LIMIT)

#define    UF_UGMGR_NAME_LIMIT          128    /**< Part (Item/Workspace object) Name length in chars; increased to 128 to support TC Longer ID/Names */
#define    UF_UGMGR_NAME_BUFSIZE        NX_BUFSIZE(UF_UGMGR_NAME_LIMIT)  

#define    UF_UGMGR_TYPE_LIMIT          32    /**< Part (Item) Type length in chars */
#define    UF_UGMGR_TYPE_BUFSIZE        NX_BUFSIZE(UF_UGMGR_TYPE_LIMIT)

#define    UF_UGMGR_DESC_LIMIT         240    /**< Part (Item/Workspace object) Description length in chars */
#define    UF_UGMGR_DESC_BUFSIZE       NX_BUFSIZE(UF_UGMGR_DESC_LIMIT)

#define    UF_UGMGR_FTYPE_LIMIT        42    /**< Dataset File Type length in chars; now from 9 'multi-CAD' + 1 '-' + 32 TC datasettype name */
#define    UF_UGMGR_FTYPE_BUFSIZE       NX_BUFSIZE(UF_UGMGR_FTYPE_LIMIT)

#define    UF_UGMGR_FNAME_LIMIT         128    /**< Dataset File Name length in chars; increased to 128 to support TC Longer ID/Names */
#define    UF_UGMGR_FNAME_BUFSIZE       NX_BUFSIZE(UF_UGMGR_FNAME_LIMIT)

#define    UF_UGMGR_ROLE_LIMIT         32    /**< User Role length in chars */
#define    UF_UGMGR_ROLE_BUFSIZE        NX_BUFSIZE(UF_UGMGR_ROLE_LIMIT)

#define    UF_UGMGR_PARTNO_SIZE_EX_LIMIT         32    /**< Part Item Id limit (currently in bytes) */
#define    UF_UGMGR_NAME_SIZE_EX_LIMIT           32    /**< Part Name limit (currently in bytes)  */
#define    UF_UGMGR_FNAME_SIZE_EX_LIMIT          32    /**< Dataset Filename limit (currently in bytes) */
    
/*  */ 
#define    UF_UGMGR_PARTNO_SIZE         (UF_UGMGR_PARTNO_BUFSIZE-1)    /**< Part (Item) Number length in bytes; increased to 128 to support TC Longer ID/Names */
#define    UF_UGMGR_PARTREV_SIZE        (UF_UGMGR_PARTREV_BUFSIZE-1)   /**< Part (Item) Revision length in bytes */
#define    UF_UGMGR_NAME_SIZE           (UF_UGMGR_NAME_BUFSIZE-1)      /**< Part (Item/Workspace object) Name length in bytes; increased to 128 to support TC Longer ID/Names */
#define    UF_UGMGR_TYPE_SIZE           (UF_UGMGR_TYPE_BUFSIZE-1)      /**< Part (Item) Type length in bytes */
#define    UF_UGMGR_DESC_SIZE           (UF_UGMGR_DESC_BUFSIZE-1)      /**< Part (Item/Workspace object) Description length in bytes */
#define    UF_UGMGR_FTYPE_SIZE          (UF_UGMGR_FTYPE_BUFSIZE-1)     /**< Dataset File Type length in bytes; now from 9 'multi-CAD' + 1 '-' + 32 TC datasettype name */
#define    UF_UGMGR_FNAME_SIZE          (UF_UGMGR_FNAME_BUFSIZE-1)     /**< Dataset File Name length in bytes; increased to 128 to support TC Longer ID/Names */
#define    UF_UGMGR_ROLE_SIZE           (UF_UGMGR_ROLE_BUFSIZE-1)      /**< User Role length in bytes */
/*  */ 


/**
* This structure is used to define the parameters for a new Part
* specification in a customization of the new-Part dialog in NX Manager.
*/
struct UF_UGMGR_new_part_no_s
{
    const char* old_item;                            /**< Seed name for the new item id, this may be NULL */
    const char* item_type;                           /**< Name of item type for which number is being generated. */
    logical     part_number_modifiable;              /**< Flag whether the user can change the returned value of new_id */
    char        new_id[UF_UGMGR_PARTNO_BUFSIZE];     /**< Returned string for new part number, this may be an empty string */
    logical     part_name_modifiable;                /**< Flag whether the user can change the returned value of new_name */
    char        new_name[UF_UGMGR_NAME_BUFSIZE];     /**< Returned string for new part name, this may be an empty string */
    logical     part_description_modifiable;         /**< Flag whether the user can change the returned value of new description. */
    char        new_description[UF_UGMGR_DESC_BUFSIZE];/**< Returned string for new part description, this may be an empty string.*/
    int         ifail;                               /**< Failure code returned from the user program, zero is success.  */
};

/**
* This structure is used to define the parameters for a new Part
* specification in a customization of the new-Part dialog in NX Manager.
*/
typedef struct UF_UGMGR_new_part_no_s UF_UGMGR_new_part_no_t,
               *UF_UGMGR_new_part_no_p_t;

/**
* This structure is used to descripbe the properties that are required for a new Part
* specification in a customization of the new-Part dialog in NX Manager.
*/
struct UF_UGMGR_property_info_s
{
    char*       property_name;          /**< The name of the property. */
    logical     is_key_field;           /**< Flag whether this is a key field of MFK id. */
    logical     is_mandatory;           /**< Flag whether this is a mandatory mapped attribute. */
    logical     is_create_descriptor;   /**< Flag whether this is a required or auto-assignable create descriptor. */
    char*       property_value;         /**< The value of the property. */
    logical     is_modifiable;           /**< Indicates whether the value is modifiable. */
};

typedef struct UF_UGMGR_property_info_s UF_UGMGR_property_info_t,
               *UF_UGMGR_property_info_p_t;

/**
* This structure is used to define the parameters for a new Part
* specification in a customization of the new-Part dialog in NX Manager.
*/
struct UF_UGMGR_new_id_s
{
    const char*                 old_item;                               /**< <I> Seed name for the new item id, this may be NULL. */
    const char*                 item_type;                              /**< <I> Name of item type for which the id is being generated. */
    int                         num_properties;                         /**< <I> Number of properties. */
    UF_UGMGR_property_info_t*   properties;                             /**< <I/O> Array of UF_UGMGR_property_info_t. One of the properties can be "item_id".
                                                                                   The property_value and is_modifiable are the outputs. */
    logical                     part_name_modifiable;                   /**< <O> Flag whether the user can change the returned value of new_name. */
    char                        new_name[UF_UGMGR_NAME_BUFSIZE];        /**< <O> Returned string for new part name, this may be an empty string. */
    logical                     part_description_modifiable;            /**< <O> Flag whether the user can change the returned value of new description. */
    char                        new_description[UF_UGMGR_DESC_BUFSIZE]; /**< <O> Returned string for new part description, this may be an empty string. */
    int                         ifail;                                  /**< <O> Failure code returned from the user program, zero is success. */
};

/**
* This structure is used to define the parameters for a new Part
* specification in a customization of the new-Part dialog in NX Manager.
*/
typedef struct UF_UGMGR_new_id_s UF_UGMGR_new_id_t,
               *UF_UGMGR_new_id_p_t;

/**
* This structure is used to define the parameters for a new Part
* specification in a customisation of the new-Part dialog in
* NX Manager.
*/
struct UF_UGMGR_new_part_rev_s
{
    const char* item;                                /**< Seed name for new item id for default domain item. This may be MFK id for non-default domain item. This may be NULL. */
    const char* item_type;                           /**< Name of item type for which revision is being generated. */
    logical     part_revision_modifiable;            /**< Flag whether the user can change the returned value of new_revision.  */
    char        new_revision[UF_UGMGR_PARTREV_BUFSIZE];/**< Returned string for new part revision, this may be an empty string. */
    int         ifail;                               /**< Failure code returned from the user program, zero is success.  */
};

/**
* This structure is used to define the parameters for a new Part
* specification in a customisation of the new-Part dialog in
* NX Manager.
*/
typedef struct UF_UGMGR_new_part_rev_s UF_UGMGR_new_part_rev_t,
               *UF_UGMGR_new_part_rev_p_t;

/**
* This structure may be used to define the parameters for a new Part
* specification in a customisation of the new-Part dialog in
* NX Manager.
*/
struct UF_UGMGR_new_dataset_name_s
{
    const char* owner;                           /**< Owning Item of existing dataset, this may be NULL */
    const char* owner_revision;                  /**< Revision name of Owning Item */
    const char* dataset_type;                    /**< Name of dataset type for which a name is being generated. */
    const char* relation_type;                   /**< Name of relation between Owning Item and dataset */
    const char* basis_name;                      /**< Basis name of new dataset (this may be an empty string) */
    logical     dataset_name_modifiable;         /**< Flag whether user can change the returned value of dataset_name */
    char        dataset_name[UF_UGMGR_NAME_BUFSIZE];/**< Returned string for new dataset name, this may be an empty string. */
    int         ifail;                           /**< Failure code returned from the user program, zero is success. */
};

/**
* This structure may be used to define the parameters for a new Part
* specification in a customisation of the new-Part dialog in
* NX Manager.
*/
typedef struct UF_UGMGR_new_dataset_name_s UF_UGMGR_new_dataset_name_t,
                                          *UF_UGMGR_new_dataset_name_p_t;

/**
* This structure may be used to define the parameters for a
* non-master, dataset name in a customisation of the saveas master
* part dialog in NX Manager.
*/
struct UF_UGMGR_saveas_dataset_name_s
{
    const char* old_owner;                       /**< Owning Item of existing dataset, this may be NULL.  */
    const char* old_owner_revision;              /**< Revision of Owning Item of existing dataset, this may be NULL. */
    const char* old_dataset;                     /**< Name of existing dataset, this may be NULL.  */
    const char* relation_type;                   /**< Name of relation type between the Owning Item and the dataset. */
    const char* new_owner;                       /**< Name of the new Owning Item of the dataset. */
    const char* new_owner_revision;              /**< Revision of the new Owning Item of the dataset. */
    logical     dataset_name_modifiable;         /**< Flag whether the user can change the returned value of dataset_name. */
    char        dataset_name[UF_UGMGR_NAME_BUFSIZE];/**< Returned string for saveas dataset name, this may be an empty string. */
    int         ifail;                           /**< Failure code returned from the user program, zero is success. */
};

/**
* This structure may be used to define the parameters for a
* non-master, dataset name in a customisation of the saveas master
* part dialog in NX Manager.
*/
typedef struct UF_UGMGR_saveas_dataset_name_s UF_UGMGR_saveas_dataset_name_t,
               *UF_UGMGR_saveas_dataset_name_p_t;

/**
* This structure is used to hold the input and output arguments to
* UF_UGMGR_saveas_dataset_info, which supercedes
* UF_UGMGR_saveas_dataset_name.  This user exit is called when
* NX Manager is about to save a part with non-masters attached to it.
* It collects information about how to save these non-masters and
* returns it to NX.
*/
struct UF_UGMGR_saveas_dataset_info_s
{
    const char              *old_part_number;       /**< <I> Original item id */
    const char              *old_rev_name;          /**< <I> Original revision id */
    const char              *new_part_number;       /**< <I> New item id */
    const char              *new_rev_name;          /**< <I> New revision id */
    const char              *new_part_type;         /**< <I> New item type */
    int                     dataset_count;          /**< <I> Number of datasets */
    char                    **dataset_list;         /**< <I> Names of datasets */

    /**
    * Return arguments; for arrays, it is one for each non-master dataset.
    */
    char                    ***dataset_name_list;   /**< <OF> For each non-master Dataset: dataset name */
    int                     **copy_state;           /**< <OF> For each non-master Dataset: each one of {USER_DATASET_always_copy, USER_DATASET_never_copy,
                                                        USER_DATASET_user_chooses} */
    logical                 **name_locked;          /**< <OF> For each non-master Dataset: indicates whether the user is allowed to change the suggested name
                                                       returned from the user exit. */
    logical                 **validation_required;  /**< <OF> For each non-master Dataset: Indicates whether or not the name must pass the validation check. */
    logical                 **original_owner;       /**< <OF> For each non-master Dataset: Indicates whether the new non-masters are to be owned by the original
                                                       owner or by the user doing the saving. */
    logical                 *allow_duplicates;      /**< <O> Whether or not duplicate non-master names are allowed. */
    int                     ifail;                  /**< <O> Failure code returned from the user program, zero is success. */
};

/**
* This structure is used to hold the input and output arguments to
* UF_UGMGR_saveas_dataset_info, which supercedes
* UF_UGMGR_saveas_dataset_name.  This user exit is called when
* NX Manager is about to save a part with non-masters attached to it.
* It collects information about how to save these non-masters and
* returns it to NX.
*/
typedef struct UF_UGMGR_saveas_dataset_info_s UF_UGMGR_saveas_dataset_info_t,
               *UF_UGMGR_saveas_dataset_info_p_t;

/**
* This function is called by NX when it wants to ensure that a dataset
* name is valid.  It is typically called in the context of saving an
* existing part to a new part, and these details are passed to it in
* case the function wants to use them to check the name.
*/
struct UF_UGMGR_validate_dataset_name_s
{
    const char              *old_part_number;       /**< <I> Original item id */
    const char              *old_rev_name;          /**< <I> Original revision id */
    const char              *new_part_number;       /**< <I> New item id */
    const char              *new_rev_name;          /**< <I> New revision id */
    const char              *new_part_type;         /**< <I> New item type */
    const char              *new_dataset_name;      /**< <I> New dataset name */
    logical                 *valid;                 /**< <O> Whether or not the name is considered valid  */
    int                     ifail;                  /**< Failure code returned from the user program, zero is success. */
};

/**
* This function is called by NX when it wants to ensure that a dataset
* name is valid.  It is typically called in the context of saving an
* existing part to a new part, and these details are passed to it in
* case the function wants to use them to check the name.
*/
typedef struct UF_UGMGR_validate_dataset_name_s UF_UGMGR_validate_dataset_name_t,
               *UF_UGMGR_validate_dataset_name_p_t;

typedef int (*UF_UGMGR_new_part_no_fn_t)(UF_UGMGR_new_part_no_p_t /* <I> */);
typedef int (*UF_UGMGR_new_id_fn_t)(UF_UGMGR_new_id_p_t /* <I> */);
typedef int (*UF_UGMGR_new_part_rev_fn_t)(UF_UGMGR_new_part_rev_p_t /* <I> */);
typedef int (*UF_UGMGR_new_dataset_name_fn_t)(UF_UGMGR_new_dataset_name_p_t /* <I> */);

/**
* This structure is used to define the parameters for a new Alternate Identifier
* as a customization of the Add Alternate dialog in NX Manager.
*/
struct UF_UGMGR_new_alternate_part_no_s
{
    tag_t        part_tag;                            /**< Tag of part to assign alternate ID. */
    const char  *context;                             /**< Context for which an alternate number is being requested.  */
    const char  *id_type;                             /**< ID type of part for which the number is being requested. May be NULL */
    char         alt_item_id[UF_UGMGR_PARTNO_BUFSIZE];/**< Alternate Item ID. The string must freed after use with UF_free(). */
    char         alt_rev_id[UF_UGMGR_PARTREV_BUFSIZE];/**< Alternate Revision ID. The string must freed after use with UF_free() */
    char         alt_name[UF_UGMGR_NAME_BUFSIZE];     /**< Returned string for new part name, this may be an empty string */
    char         alt_description[UF_UGMGR_DESC_BUFSIZE];/**< Returned string for new part description, this may be an empty string.*/
    logical      modifiable;                          /**< Boolean; is the alternate ID allowed to be modified */
};

/**
* This structure is used to define the parameters for a new Alternate Identifier
* as a customization of the Add Alternate dialog in NX Manager.
*/
typedef struct UF_UGMGR_new_alternate_part_no_s UF_UGMGR_new_alternate_part_no_t,
               *UF_UGMGR_new_alternate_part_no_p_t;

/**
* Valid revision configuration options
*/
enum UF_UGMGR_rev_config_options_e
{
    UF_UGMGR_configure_none,            /*< No revision option has been set */
    UF_UGMGR_configure_latest,          /*< The latest revision will be returned, even for configured input */
    UF_UGMGR_configure_by_rev_rule,     /*< Use the specified Revision Rule for configuration, even for configured input */
    UF_UGMGR_configure_all_revisions    /*< All revisions will be returned, even for configured input */
} ;

/**
* Valid revision configuration options
*/
typedef enum UF_UGMGR_rev_config_options_e UF_UGMGR_rev_config_options_t;

/**
* This structure is used to represent an NX PartFile for the purpose of resolving
* a part file name and used as input to the service UF_UGMGR_resolve_part_file_infos.
*
* Note: -If fileName is specified then partId, revisionID, modelType, datasetName are ignored.
        -If fileName is not provided then partID has to be provided for the input to be valid.
        -If partID is provided then modelType, datasetName can be provided along with partID and revisionID.
        -For unconfigured input( i.e., revision information not available) and revisionOption is UF_UGMGR_configure_none
          the current revision Rule in effect will be used to resolve the NX PartFile.
*/
struct UF_UGMGR_part_file_info_s
{
    const char                          *fileName;                             /**< %UGMGR filename(This is what is returned from methods such as UF_UGMGR_encode_part_filename),
                                                                                   or @DB- Command line Input name (This is what is returned from methods such as
                                                                                   UF_UGMGR_convert_file_name_to_cli) of the NX PartFile. If this is not specified/used, 
                                                                                   it has to be initialized to NULL*/
    const char                          *partID;                               /**< PartID of the NX PartFile to be resolved. If this is not specified/used, it has to be
                                                                                    initialized to NULL. */
    const char                          *revisionId;                           /**< RevisionID of the part to be resolved. If the revisionOption is set to UF_UGMGR_configure_by_rev_rule,
                                                                                    this will be ignored. If this is not specified/used, it has to be initialized to NULL.*/
    const char                          *modelType;                            /**< PDI Model Type, valid values are "master","specification", "manifestation", "altrep", 
                                                                                   "scenario", "simulation", "cae_motion", "cae_solution", "cae_mesh" and "cae_geometry".
                                                                                    If this is not specified/used, it has to be initialized to NULL.*/
    const char                          *datasetName;                          /**< Dataset name of the NX PartFile to be resolved. 
                                                                                    If this is not specified/used, it has to be initialized to NULL.*/
    const char                          *revisionRule;                         /**< Teamcenter Revision Rule to use for configuration, This will be used only if revisionOption is 
                                                                                    set to UF_UGMGR_configure_by_rev_rule. If this is not specified/used, it has to be initialized to NULL.*/
    UF_UGMGR_rev_config_options_t       revisionOption;                        /**< Revision configuration option.*/  

};

/**
* This structure is used to represent an NX PartFile for the purpose of resolving 
* a part file name and used as input to the service UF_UGMGR_resolve_part_file_infos.
*/
typedef struct UF_UGMGR_part_file_info_s UF_UGMGR_part_file_info_t,
               *UF_UGMGR_part_file_info_p_t;

/**
* This structure is used to hold information about an NX partFile that is resolved by
* the service UF_UGMGR_resolve_part_file_infos. The elements of this structure are
* valid only if iFail is zero.
*/
struct UF_UGMGR_part_file_object_s
{
    char                          *fullSpec;                             /**< Returned string, %UGMGR filename. The string must freed after use with UF_free()  */
    char                          *cliSpec;                              /**< Returned string, @DB-CommandLineInput filename of the part. The string must freed after use with UF_free()  */
    char                          *partID;                               /**< Returned string, ID of the part. The string must freed after use with UF_free()  */
    char                          *datasetName;                          /**< Returned string, Datasetname of the part. The string must freed after use with UF_free()  */
    char                          *revisionID;                           /**< Returned string, Revision ID of the part. The string must freed after use with UF_free()  */
    char                          *partNumber;                           /**< Returned string, PartNumber of the part. The string must freed after use with UF_free()  */
    char                          *datasetType;                          /**< Returned string, The TC dataset type for this Part. The string must freed after use with UF_free()*/
    char                          *pdiModelType;                         /**< Returned string, The equivalent PDI model type for this part. The string must freed after use with UF_free()*/
    tag_t                          partTag;                              /**< Returned Database tag of the part */
    int                            iFail;                                /**< Returned Error code for this object, zero is success.  */
};

/**
* This structure is used to define the parameters for PartFileObject used as output
* in the service UF_UGMGR_resolve_part_file_infos.
*/
typedef struct UF_UGMGR_part_file_object_s UF_UGMGR_part_file_object_t,
               *UF_UGMGR_part_file_object_p_t;


typedef int (*UF_UGMGR_saveas_dataset_name_fn_t)
                                            (UF_UGMGR_saveas_dataset_name_p_t /* <I> */);
typedef int (*UF_UGMGR_saveas_dataset_info_fn_t)
                                            (UF_UGMGR_saveas_dataset_info_p_t /* <I> */);

typedef int (*UF_UGMGR_validate_dataset_name_fn_t)
                                            (UF_UGMGR_validate_dataset_name_p_t /* <I> */);
typedef int (*UF_UGMGR_new_alternate_part_no_fn_t)
                                            (UF_UGMGR_new_alternate_part_no_p_t /* <I> */);

/**
* PDM object types that can be accessed from NX Manager.
*/
enum UF_UGMGR_object_type_e
{
    UF_UGMGR_type_unknown,       /**< Unknown object type */
    UF_UGMGR_type_folder,        /**< Folder object type */
    UF_UGMGR_type_part,          /**< Part Item object type */
    UF_UGMGR_type_part_revision  /**< Part Item Revision object type */
} ;

/**
* PDM object types that can be accessed from NX Manager.
*/
typedef enum UF_UGMGR_object_type_e UF_UGMGR_object_type_t;

/**
* Part Number creation validation codes.
*/
enum UF_UGMGR_partno_status_e
{
    UF_UGMGR_partno_valid,    /**< Part Number is valid */
    UF_UGMGR_partno_invalid,  /**< Part Number is invalid, such as has invalid character, violates database pattern rules, etc. */
    UF_UGMGR_partno_modified, /**< Part Number is valid but has been modified as output, due to naming rules, etc. */
    UF_UGMGR_partno_override  /**< Part Number is valid but has been overwritten due to user exit, etc. */
} ;

/**
* Part Number creation validation codes.
*/
typedef enum UF_UGMGR_partno_status_e UF_UGMGR_partno_status_t;

/**
* Alternate Id creation validation codes.
*/
enum UF_UGMGR_alt_id_status_e
{
    UF_UGMGR_alt_id_valid,    /**< Alternate Id is valid */
    UF_UGMGR_alt_id_invalid,  /**< Alternate Id is invalid, such as has invalid character, violates database pattern rules, etc. */
    UF_UGMGR_alt_id_modified, /**< Alternate Id is valid but has been modified as output, due to naming rules, etc. */
    UF_UGMGR_alt_id_override  /**< Alternate Id is valid but has been overwritten due to user exit, etc. */
} ;

/**
* Alternate Id creation validation codes.
*/
typedef enum UF_UGMGR_alt_id_status_e UF_UGMGR_alt_id_status_t;

/**
* Tags related to NX database objects.
*/
typedef  tag_t UF_UGMGR_tag_t;

/**
* Null NX database tag. Indicates unknown or invalid object tags.
*/
#define UF_UGMGR_null_tag  ((UF_UGMGR_tag_t)0)

/**
* Constants for the TCIN error return codes.
*/
#define    UF_UGMGR_error_base                 ERROR_UGMGR_base + 3000
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


/****************************************************************************
 * UF_UGMGR_ATTR_info_t
 *
 * User attribute information struct representing a creation parameter
 * for creating a new part in Teamcenter. This struct is used by
 * UF_UGMGR_get_creation_parameters.
 *
 ****************************************************************************/
struct UF_UGMGR_ATTR_info_s
{
    logical create_descriptor;  /**< Flag indicating if this parameter is a create descriptor */
    logical key_identifier;     /**< Flag indicating if this parameter is a field of the multi field key */
    UF_ATTR_info_t basic_info;  /**< Other informarion viz. title, alias, whether required, etc. */
};
typedef struct UF_UGMGR_ATTR_info_s UF_UGMGR_ATTR_info_t, *UF_UGMGR_ATTR_info_p_t;
typedef const struct UF_UGMGR_ATTR_info_s UF_UGMGR_ATTR_info_c_t, *UF_UGMGR_ATTR_info_pc_t;

#ifdef __cplusplus
}
#endif

#endif /* UF_UGMGR_TYPES_H_INCLUDED */
