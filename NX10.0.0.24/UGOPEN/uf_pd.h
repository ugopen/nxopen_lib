/*******************************************************************************

             Copyright (c) 1999,2001,2002,2003,2004,2005,2007 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved


********************************************************************************
File description:

*******************************************************************************/

#ifndef UF_PD_H_INCLUDED
#define UF_PD_H_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_drf_types.h>
#include <uf_pd_types.h>

#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
     Initializes the data structure for business modifier.  Please note that
     this does not guarantee the data in the structure is valid for
     creation operations, but will ensure all data is initialized.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_init_business_modifier(
    UF_PD_business_modifier_p_t business_modifier /*<I/O>*/
);

/******************************************************************************
     Initializes the data structure for attribute values.  Please note that
     this does not guarantee the data in the structure is valid for
     creation operations, but will ensure all data is initialized.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_init_attribute_value(
    UF_PD_attribute_value_p_t attribute_value_data /*<I/O>*/
);

/******************************************************************************
     Initializes the data structure for product attributes.  Please note
     that this does not guarantee the data in the structure is valid for
     creation operations, but will ensure all data is initialized.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_init_attribute(
    UF_PD_product_attribute_p_t attribute_data /*<OF>Free using UF_free*/
);

/******************************************************************************
     Initializes the data structure for leader associativity points.  Please
     note that this does not guarantee the data in the structure is valid for
     creation operations, but will ensure all data is initialized.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_init_leader_assoc_point(
    UF_PD_product_definition_leader_assoc_pnt_p_t leader_point_data /*<I/O>*/
);

/******************************************************************************
     Initializes the data structure for smart model leaders.  Please
     note that this does not guarantee the data in the structure is valid
     for creation operations, but will ensure all data is initialized.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_init_leader(
    UF_PD_product_definition_leader_p_t leader_data /*<I/O>*/
);

/******************************************************************************
     Initializes the data structure for instance objects.  Please
     note that this does not guarantee the data in the structure is valid
     for creation operations, but will ensure all data is initialized.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_init_instance(
    UF_PD_product_definition_instance_p_t instance_data /*<I/O>*/
);

/******************************************************************************
     Initializes the data structure for product definitions.  Please
     note that this does not guarantee the data in the structure is valid
     for creation operations, but will ensure all data is initialized.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_init_product_definition(
    UF_PD_product_definition_p_t product_definition_data /*<OF>Free using UF_free.*/
);

/******************************************************************************
     Creates a Product Definition in the work part.

     Notes: In NX4, each Product Definition can only contain one product attribute.
            The system will raise an error if there is more than one attribute
            in the product definition

            In NX6, following modifications are implemented -
            1. As part of product definition creation, a display instance will also
               be created in the TOP view.
            2. The system will provide a display instance for legacy product definition
               objects that didn't have a display instance. This display instance
               is visible in a view named MIGRATED_PMI.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0, modified in release NX4.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_create_product_definition(
    UF_PD_product_definition_p_t product_definition,  /* <I>
                                                         Specification for the
                                                         product definition to be
                                                         created in the work
                                                         part. Must be of type 
                                                         UF_smsp_product_definition_type 
                                                         and subtype 
                                                         UF_smsp_product_attribute_subtype
                                                      */
    tag_t *product_definition_created                 /* <O>
                                                            Tag of the created
                                                            product definition
                                                      */
);

/******************************************************************************
     Queries the data from a Product Definition.  Please use the function
     UF_PD_free_product_definition_data to free the allocated product
     definition data.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_definition_data(
    tag_t product_definition,                         /* <I>
                                                        Tag of the product
                                                        definition object to
                                                        query. Must be of type 
                                                        UF_smsp_product_definition_type 
                                                        and subtype 
                                                        UF_smsp_product_attribute_subtype
                                                      */
    UF_PD_product_definition_p_t *product_definitions /* <OF,free:UF_PD_free_product_definition_data>
                                                        Product definition data
                                                        for the given object.
                                                      */
);

/******************************************************************************
     Queries the data from a Product Definition.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Originally created in V19 - corrected naming in NX7
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_attributes(
    tag_t product_definition,                         /* <I>
                                                        Tag of the product
                                                        definition object to
                                                        query. Must be of type 
                                                        UF_smsp_product_definition_type 
                                                        and subtype 
                                                        UF_smsp_product_attribute_subtype
                                                      */
    tag_p_t *product_attributess,    /* <OF,len:num_product_attributes> Product attributes */
    int *num_product_attributes      /* <O>  Number of product attributes */

);

/******************************************************************************
     Queries the data from a Product Definition Attribute.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Originally created in V19 - corrected naming in NX7
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_attribute_data(
    tag_t attribute,                            /* <I>
                                                   Tag of the product
                                                   definition object to
                                                   query. Must be of type 
                                                   UF_smsp_product_definition_type 
                                                   and subtype 
                                                   UF_smsp_product_attribute_subtype
                                                */
    UF_PD_product_attribute_p_t attribute_data /* <O> Data of Product attributes */
);

/******************************************************************************
     Queries the attribute value data from a Product Definition Attribute Value.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Originally created in V19 - corrected naming in NX7
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_attribute_value_data(
    tag_t attribute_value,                     /* <I>
                                                  Tag of the product
                                                  definition object to
                                                  query.
                                               */
    UF_PD_attribute_value_p_t value_data     /* <O> Data of Product attributes */
);

/******************************************************************************
     Queries Product Definition in part

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V19.0
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_definitions(
    tag_t context,                   /* <I> Part context for the query */
    tag_p_t *product_definitions,    /* <OF,len:num_product_definitions> Array of product definition objects */
    int *num_product_definitions     /* <O>  Number of product attributes */

);

/******************************************************************************
     Frees a previously allocated product attribute structure.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_free_product_attribute_data(
    UF_PD_product_attribute_p_t attr    /* <I/O>
                                           Product attribute data
                                           for the given object. Must be of type 
                                           UF_smsp_product_definition_type 
                                           and subtype 
                                           UF_smsp_product_attribute_subtype
                                        */
);

/******************************************************************************
     Frees a previously allocated product attribute value structure.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_free_product_attribute_value_data(
    UF_PD_attribute_value_p_t value_data  /* <I/O>
                                              Product attribute data
                                              for the given object.
                                           */
);

/******************************************************************************
     Frees a previously allocated product definition structure.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_free_product_definition_data(
    UF_PD_product_definition_p_t *product_definition /* <I/O>
                                                        Product definition data
                                                        for the given object. Must be of type 
                                                        UF_smsp_product_definition_type 
                                                        and subtype 
                                                        UF_smsp_product_attribute_subtype
                                                     */
); /* <NON_NXOPEN> */

/******************************************************************************

     Sets the data for a Product Definition.

     Notes: In NX4, each Product Definition can only contain one
            product attribute. The system will raise an error if
            there is more than one attribute in the product definition

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0, modified in release NX4.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_set_product_definition_data(
    tag_t product_definition,                         /* <I>
                                                        Tag of the product
                                                        definition object to
                                                        query.
                                                      */
    UF_PD_product_definition_p_t product_definition_data  /* <I>
                                                           Product definition data
                                                           for the given object. Must be of type 
                                                           UF_smsp_product_definition_type 
                                                           and subtype 
                                                           UF_smsp_product_attribute_subtype
                                                          */
);

/******************************************************************************
     Creates a Product Definition Display Instance in the specified part file.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_create_instance(
    tag_t product_definition,                        /* <I>
                                                        Tag of the product
                                                        definition object to
                                                        query. Must be of type 
                                                        UF_smsp_product_definition_type 
                                                        and subtype 
                                                        UF_smsp_product_attribute_subtype
                                                     */
    UF_PD_product_definition_instance_p_t instance_definition,
    /* <I>
       Product definition
       instance data to apply
       to the new display. 
    */
    tag_t *instance                                  /* <O>
                                                        Instance created.
                                                     */
);

/******************************************************************************

     Queries the product definitions associated with the specified geometry.  Please
     note that those Product Definitions that reference more geometry than what is
     specified will be returned by this function.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_definitions_of_geometry(
    tag_t *geometry_references,    /* <I,len:num_geometry_references>
                                      Geometry to cross reference with product
                                      definition objects.
                                         */
    int num_geometry_references,   /* <I>
                                      Number of tags references in geometry array.
                                   */
    tag_p_t *product_definitions,    /* <OF,len:num_product_definitions>
                                      Product definition objects referencing the
                                      specified geometry.
                                         */
    int *num_product_definitions   /* <O> num_product_definitions
                                      Number of product definition objects in
                                      array.
                                   */
);

/******************************************************************************
     This function will ask the allowable geometry that can be associated to
     the defined product attribute

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_definition_allowable_geometry(
    tag_t definition,              /* <I> Product definition to query. Must be of type 
                                      UF_smsp_product_definition_type 
                                      and subtype 
                                      UF_smsp_product_attribute_subtype
                                   */
    int *num_allowable_geometry,   /* <O> Number of the allowable meometry */
    char *** allowable_geom        /* <OF,len:num_allowable_geometry> Array of allowable geometry */
);

/******************************************************************************
     This function will query the Product Definition Display Instances for the
     given Product Definition.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_definitions_instances(
    tag_t product_definition,   /* <I>
                                   Product definition to query. Must be of type 
                                   UF_smsp_product_definition_type 
                                   and subtype 
                                   UF_smsp_product_attribute_subtype
                                */
    tag_p_t *instances,         /* <OF,len:num_instances>
                                   Array of instances created from the Product
                                   Definition in the work part.
                                */
    int *num_instances          /* <O>
                                   Number of instances in the array.
                                */
);

/******************************************************************************

     This function will query the Product Definition that defines the Product
     Definition Display Instance.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_definition_from_instance(
    tag_t instance,             /* <I>
                                   Product definition display instance to query. 
                                */
    tag_t *product_definition   /* <O>
                                   Product definition defined by the instance
                                */
);

/******************************************************************************
     This function will check the Product Definition retain status

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_is_retained(
    tag_t product_definition,   /* <I> Product definition to query. Must be of type 
                                   UF_smsp_product_definition_type 
                                   and subtype 
                                   UF_smsp_product_attribute_subtype
                                */
    logical *retained           /* <O> Object retain status        */
);

/*****************************************************************************
   The following function will query the business process modifiers from
   the product attribute object.

   Return:

   Environment: Internal or External

   See also:

   History: Created in V19.0
*******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_business_process_modifiers(
    tag_t product_attributes,
    /* <I>
       Product attribute to query. Must be of type 
       UF_smsp_product_definition_type 
       and subtype 
       UF_smsp_product_attribute_subtype
    */
    tag_p_t *modifiers,
    /* <OF,len:num_modifiers>
       Array of business process modifiers applied to the product attribute.
    */
    int *num_modifiers
    /* <O>
       Number of business process modifiers in array.
    */
);

/*********************************************************************
   The following function will add a business process modifier
   to the product attribute.

   Return:

   Environment: Internal or External

   See also:

   History: Created in V19.0
*****************************************************************************/
extern UFUNEXPORT int UF_PD_add_business_process_modifier(
    tag_t product_attribute, /* <I>
                                Product attribute in which to add modifier. Must be of type 
                                UF_smsp_product_definition_type 
                                and subtype 
                                UF_smsp_product_attribute_subtype
                             */
    char *modifier_name      /* <I>
                              * Knowledge Fusion (KF) name of the modifier to add.
                              */
);

/***************************************************************
   The following function will query the business process modifier data from
   the business process modifier.

   Return:

   Environment: Internal or External

   See also:

   History: Created in V19.0
**************************************************************/
extern UFUNEXPORT int UF_PD_ask_business_process_modifier_data(
    tag_t business_process_modifier, /* <I>
                                      * Business process modifier to query.
                                      */
    UF_PD_business_modifier_p_t business_modifier /* <O>
                                                   * Data of the business process modifier.
                                                   */
);

/****************************************************************
    The following function will edit the business process modifier data from the
    business process modifier.

    Return:

    Environment: Internal or External

    See also:

    History: Created in V19.0
****************************************************************/
extern UFUNEXPORT int UF_PD_set_business_process_modifier_data(
    tag_t business_process_modifier, /* <I>
                                      * Business process modifier to query.
                                      */
    UF_PD_business_modifier_t business_modifier /* <I>
                                                 * Data of the business process modifier.
                                                 */
);

/*****************************************************************
    The following function will ask the business process modifier type

    The valid types are:

    UF_PD_BUS_MODFR_STRING_TYPE = 0,
    UF_PD_BUS_MODFR_LIST_TYPE,
    UF_PD_BUS_MODFR_URL_TYPE,
    UF_PD_BUS_MODFR_REVISION_TYPE,
    UF_PD_BUS_MODFR_SAFETY_CLASS_TYPE,
    UF_PD_BUS_MODFR_CUSTOMER_VALUE_TYPE

    Return:

    Environment: Internal or External

    See also:

    History: Created in V19.0
*****************************************************************/
extern UFUNEXPORT int UF_PD_ask_business_process_modifier_type(
    tag_t business_process_modifier, /* <I>
                                      * Business process modifier to query.
                                      */
    UF_PD_BUS_MODFR_type_e *type  /* <O>
                                   * Business process modifier type.
                                   */
);

/******************************************************************************
     Frees a previously allocated business modifier structure.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in V18.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_free_business_modifier_data(
    UF_PD_business_modifier_p_t business_modifier   /* <I/O>
                                                        Business Modifier data
                                                        for the given object.
                                                     */
);

/******************************************************************************
     This function will modify the product attribute data
     defined by user

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Created in NX2.0
******************************************************************************/
extern UFUNEXPORT int UF_PD_modify_product_attribute(
    tag_t attribute,                    /* <I> Product attribute to be modified */
    UF_PD_product_attribute_p_t data    /* <I> Product attribute data */
);

/******************************************************************************
     Queries the data from a Product Definition Attribute.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: Originally created in V19 - corrected naming in NX7
 ******************************************************************************/
extern UFUNEXPORT int UF_PD_ask_product_attribute_data_2(
    tag_t attribute,                            /* <I>
                                                   Tag of the product
                                                   definition object to
                                                   query. Must be of type 
                                                   UF_smsp_product_definition_type 
                                                   and subtype 
                                                   UF_smsp_product_attribute_subtype
                                                */
    UF_PD_product_attribute_2_p_t attribute_data /* <O> Data of Product attributes */
);
/******************************************************************************
     Frees a previously allocated product attribute structure.

     Return:
     Return code:
     0 = No error
     not 0 = Error code

     Environment: Internal and External

     See Also:

     History: 
******************************************************************************/
extern UFUNEXPORT int UF_PD_free_product_attribute_data_2(
    UF_PD_product_attribute_2_p_t attr    /* <I/O>
                                           Product attribute data
                                           for the given object.
                                        */
);
#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_PD_H_INCLUDED */
