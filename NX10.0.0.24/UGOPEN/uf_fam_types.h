/*******************************************************************************
             Copyright (c) 2000-2001 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       



****************************************************************************/

#ifndef UF_FAM_TYPES_H_INCLUDED
#define UF_FAM_TYPES_H_INCLUDED


/*==========================================================================

  ==========================================================================*/

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

struct UF_FAM_attribute_data_s
{
    int                     subtype; /*A flag indicating the attribute type. 
                                     */
    tag_t                   base_object; /*The object this family attribute is 
                                         based on.
                                         When subtype is set to 
                                         UF_fam_attr_text_subtype,
                                         base_object should be set to NULL_TAG.

                                         When subtype is set to 
                                         UF_fam_attr_numeric_subtype,
                                         base_object should be set to NULL_TAG.

                                         When subtype is set to 
                                         UF_fam_attr_integer_subtype,
                                         base_object should be set to NULL_TAG.

                                         When subtype is set to 
                                         UF_fam_attr_double_subtype,
                                         base_object should be set to NULL_TAG.

                                         When subtype is set to 
                                         UF_fam_attr_string_subtype,
                                         base_object should be set to NULL_TAG.

                                         When subtype is set to 
                                         UF_fam_attr_part_subtype,
                                         base_object should be set to a part 
                                         attribute tag.

                                         When subtype is set to 
                                         UF_fam_attr_name_subtype,
                                         base_object should be set to NULL_TAG.

                                         When subtype is set to 
                                         UF_fam_attr_instance_subtype,
                                         base_object should be set to an 
                                         instance_tag.

                                         When subtype is set to 
                                         UF_fam_attr_exp_subtype,
                                         base_object should be set to an 
                                         expression tag.

                                         When subtype is set to 
                                         UF_fam_attr_mirror_subtype,
                                         base_object should be set to a mirror 
                                         feature tag.

                                         When subtype is set to 
                                         UF_fam_attr_density_subtype,
                                         base_object should be set to a solid 
                                         body tag.

                                         When subtype is set to 
                                         UF_fam_attr_feature_subtype,
                                         base_object should be set to a 
                                         suppressible feature tag.
                                         */ 
    char                    *rules; /*The rules for the attribute.  (NOT USED)
                                    */
    char                    *value; /*The current value of the attribute.
                                    */
    char                    *name; /*The name for the attribute.
                                   */
}; 

typedef struct UF_FAM_attribute_data_s UF_FAM_attribute_data_t,
                                      *UF_FAM_attribute_data_p_t;


struct UF_FAM_class_data_s
{
    int                             subtype; /*A flag indicating the type of 
                                             attributes in this class.
                                             Valid values are :

                                             UF_fam_attr_text_subtype
                                             UF_fam_attr_numeric_subtype
                                             UF_fam_attr_integer_subtype
                                             UF_fam_attr_double_subtype
                                             UF_fam_attr_string_subtype
                                             UF_fam_attr_part_subtype
                                             UF_fam_attr_name_subtype
                                             UF_fam_attr_instance_subtype
                                             UF_fam_attr_exp_subtype
                                             UF_fam_attr_mirror_subtype
                                             UF_fam_attr_density_subtype
                                             UF_fam_attr_feature_subtype
                                             */
    int                             attribute_count; /*The number of attributes
                                                      in this class
                                                     */
    UF_FAM_attribute_data_t        *attribute_data; /*<len:attribute_count>
                                                    An array of family 
                                                    attribute structures(see 
                                                    below).
                                                    Each attribute structure 
                                                    represents a member of the
                                                    attribute class.
                                                    */
    char                           *name; /*The name of the attribute class.
                                          */
};
typedef struct UF_FAM_class_data_s UF_FAM_class_data_t, *UF_FAM_class_data_p_t;


struct UF_FAM_family_data_s
{
    int                 subtype; /* A flag indicating which type of family 
                                 this is. Currently this can only be set to 
                                 UF_fam_part_subtype
                                 */ 
    int                 attribute_count; /*The number of attributes of the 
                                         family.  
                                         */
    int                 member_count; /*The number of members in the family.
                                      */
    tag_t              *attributes; /* <len:attribute_count> 
                                    An array of family attribute tags which 
                                    describe the parameters of the family.  
                                    */
    char               *name; /*The name for the family.
                              */
};
typedef struct UF_FAM_family_data_s UF_FAM_family_data_t,
                                   *UF_FAM_family_data_p_t;


struct UF_FAM_member_data_s
{
    int                             value_count; /*The number of member values.
                                                 */
    char                          **values; /*<len:value_count>
                                            An array of values for this 
                                            member.  When this array of values 
                                            is returned from an enquiry 
                                            function, each value is dynamically
                                            allocated, and must be freed with 
                                            UF_free.  
                                            */
};
typedef struct UF_FAM_member_data_s UF_FAM_member_data_t,
                                   *UF_FAM_member_data_p_t;


struct UF_FAM_intent_data_s
{
    tag_t                      family; /*The family involved in the intent.
                                       */
    int                        member_index; /* Desired family member...used 
                                             only when attribute_count equals 
                                             zero.
                                             */
    int                        attribute_count; /*The number of family 
                                                attributes involved in the 
                                                intent   
                                                */
    tag_t                     *attributes; /*<len:attribute_count>
                                            An array of attribute tags.
                                           */
    char                     **match_criteria; /*<len:attribute_count>
                                               The match criteria for this 
                                               intent...one per attribute.  
                                               NOTE: The match_criteria field
                                               only requires an attribute value 
                                               for part and feature attributes.
                                               All other attributes must be 
                                               initialized with both the
                                               name and value 
                                               (e.g. "<attribute_name> ==
                                               <attribute_value>".   
                                               */
    char                      *name; /*The name of the intent
                                     */
};
typedef struct UF_FAM_intent_data_s UF_FAM_intent_data_t,
                                   *UF_FAM_intent_data_p_t;

#ifdef __cplusplus
}
#endif

#endif /* UF_FAM_TYPES_H_INCLUDED */
