/*******************************************************************************

             Copyright (c) 1999,2001,2002,2003,2004,2005 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved



File description:

    Open C API: The all data stucture/type for Product Definitions
    are defined in the header file

*******************************************************************************/

#ifndef UF_PD_DATATYPES_H_INCLUDED
#define UF_PD_DATATYPES_H_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ERROR_SMSP_base is originally defined in error_bases.h */
#define ERROR_SMSP_base                              3235000

/* match SMSP error code to UF_SMSP error code */
#define UF_SMSP_NO_ERROR                             0
#define UF_SMSP_ERR_NO_KLINK_OBJECT                  (ERROR_SMSP_base + 1)
#define UF_SMSP_ERR_KBE_PRODUCT_DEFINITION           (ERROR_SMSP_base + 2)
#define UF_SMSP_ERR_PD_NAME_INVALID                  (ERROR_SMSP_base + 3)
#define UF_SMSP_ERR_PD_NAME_IN_USE                   (ERROR_SMSP_base + 6)
#define UF_SMSP_ERR_PRODUCT_ATTRIBUTE_TYPE_INVALID   (ERROR_SMSP_base + 8)
#define UF_SMSP_ERR_PRODUCT_VALUE_TYPE_INVALID       (ERROR_SMSP_base + 9)
#define UF_SMSP_ERR_PD_TAG_INVALID                   (ERROR_SMSP_base + 10)
#define UF_SMSP_ERR_PD_INSTANCE_TYPE_INVALID         (ERROR_SMSP_base + 11)
#define UF_SMSP_ERR_INSTANCE_TAG_INVALID             (ERROR_SMSP_base + 12)
#define UF_SMSP_ERR_ATTR_NUMBER_INVALID              (ERROR_SMSP_base + 13)
#define UF_SMSP_ERR_GEOM_NUMBER_INVALID              (ERROR_SMSP_base + 15)
#define UF_SMSP_ERR_PD_GEOMETRY_TYPE_INVALID         (ERROR_SMSP_base + 16)
#define UF_SMSP_ERR_INST_LEADER_NUM_INVALID          (ERROR_SMSP_base + 17)
#define UF_SMSP_ERR_NO_ATTRIBUTES_SPECIFIED          (ERROR_SMSP_base + 24)
#define UF_SMSP_ERR_INVALID_ATTRIBUTE_SPECIFIED      (ERROR_SMSP_base + 25)
#define UF_SMSP_ERR_EMARKING_ATTRIBUTE_EXISTS        (ERROR_SMSP_base + 27)

#define ERROR_SMRT_MODEL_base                      3330000

#define UF_SMRT_MODEL_ERR_BUS_MODFR_EXISTS            (ERROR_SMRT_MODEL_base + 0)
#define UF_SMRT_MODEL_ERR_KF_OBJECT_NON_EXISTANT      (ERROR_SMRT_MODEL_base + 2)
#define UF_SMRT_MODEL_ERR_BUSMODFR_TAG_INVALID        (ERROR_SMRT_MODEL_base + 3)
#define UF_SMRT_MODEL_ERR_BUSMODFR_TITLE_INVALID      (ERROR_SMRT_MODEL_base + 4)

/*  This enumerated type defines the type of attributes
 *  current supported by the Smart Model tools.
 */
enum UF_PD_attribute_type_e
{
    UF_PD_NULL_ATTRIBUTE_TYPE,  /* system default attribute type */

    UF_PD_UG_USER_DEFINED, /* User defined attribute.
                            * For this attribute, the user may specify any number, and type of
                            * product attribute values.
                            */

    UF_PD_STRING_TYPE,   /* String attribute.
                          * This type contains a single attribute value which hold a title/value
                          * pair for a string parameter.
                          * Title: String
                          * Value: any string
                          */

    UF_PD_INTEGER_TYPE,   /* Integer attribute.
                           * This type contains a single attribute value which hold a title/value
                           * pair for an integer parameter.
                           * Title: Integer
                           * Value: any integer
                           */

    UF_PD_NUMBER_TYPE, /* Number attribute.
                        * This type contains a single attribute value which hold a title/value
                        * pair for a number parameter.
                        * Title: Number
                        * Value: any number
                        */

    UF_PD_ENTERPRISE_IDENTIFIER_TYPE, /* Enterprise Identifier.
                                       * An enterprise identifier is used to embed company information within
                                       * a part file.  The attributes of an enterprise identifier include:
                                       *    Company Name:     Name of the company owning the part.
                                       *    Company Address:  Street, City, State, and Zip of that company.
                                       *    Division / Site:  Division, or site information of authoring part.
                                       *    CAGE Code:        Government assigned code for tracking purposes,
                                       *                      if applicable.
                                       */

    UF_PD_PART_IDENTIFIER_TYPE,  /* Part Identifier.
                                  * A part identifier is used to embed part information within an NX
                                  * part file.  The attributes of a part identifier include:
                                  *    Identifier:       A unique identifier for that part
                                  *    Revision:         The revision assigned to that part identifier
                                  *    Item Name:
                                  *    Item Name Modifier:
                                  *    Descriptive Modifier:
                                  */

    UF_PD_MATERIAL_SPECIFICATION_TYPE,   /* Material Specification. The attributes include:
                                          *    Identifier:       A unique identifier for that part
                                          *    Revision:         The revision assigned to that part identifier
                                          *    Nomenclature:
                                          *    User Field:       A array of string defined by users
                                          */

    UF_PD_PROCESS_SPECIFICATION_TYPE,  /* Process Specification. The attributes include:
                                        *    Identifier:       A unique identifier for that part
                                        *    Revision:         The revision assigned to that part identifier
                                        *    Nomenclature:
                                        */

    UF_PD_SURFACE_FINISH_TYPE,     /* Surface Finish. The attributes include:
                                    * Standard:
                                    * Symbol Type:
                                    * a1, a2, b, c, d, e, f1, f2 (Check Standard for details)
                                    *
                                    * valid value for standard: "ANSI", "ISO", "JIS", "DIN"
                                    *
                                    * valid value for Symbol Type:
                                    * "Basic", "BasicProhibited", "BasicRequired", "Modifier",
                                    * "ModifierProhibited" , "ModifierRequired",  "ModifierAllAround",
                                    * "ModifierAllAroundProhibited", "ModifierAllAroundRequired"
                                    *
                                    */

    UF_PD_GENERIC_NOTE_TYPE, /* Generic Note. The attributes include:
                              * Category:
                              * Identifier
                              * Revision:
                              * Text:
                              */

    UF_PD_SPECIFIC_NOTE_TYPE, /* Specific Note. The attributes include:
                               * Category:
                               * Identifier
                               * Revision:
                               * Text:
                               */

    UF_PD_BALLOON_NOTE_TYPE,  /* Ballon note, The attributes include:
                               * Category:
                               * Identifier
                               * Revision:
                               * Text:
                               * Balloon Text:
                               */

    UF_PD_LOCATOR_DESIGNATOR_TYPE,  /* Locator Designator, the attributes include:
                                     * Locator Type:
                                     * Locator Letter:
                                     * Coordinate Plane:
                                     * Func Subscript:
                                     * Part Number:
                                     * Note Text
                                     * Hot Spot:
                                     */

    UF_PD_COORDINATE_NOTE_TYPE,     /* Coordinate Note, the attributes include:
                                     * Category
                                     * Identifier
                                     * Revision
                                     * Prefix X
                                     * Suffix X
                                     * Include X: prefix x and sufix x will be on if checked
                                     * Prefix Y
                                     * Suffix Y
                                     * Include Y: prefix y and sufix y will be on if checked
                                     * Prefix Z
                                     * Suffix Z
                                     * Include Z: prefix z and sufix z will be on if checked
                                     * Prefix I
                                     * Suffix I
                                     * Include I: prefix i and sufix i will be on if checked
                                     * Prefix J
                                     * Suffix J
                                     * Include J: prefix j and sufix j will be on if checked
                                     * Prefix K
                                     * Suffix K
                                     * Include_K: prefix k and sufix k will be on if checked
                                     * Prefix Label
                                     * Suffix Label
                                     * Include Label: prefix label and sufix label will be on if checked
                                     * Prefix Level
                                     * Suffix Level
                                     * Include Level:: prefix level and sufix level will be on if checked
                                     */

    UF_PD_EXPORT_CONTROL_TYPE,  /* Export Control e-Marking. The attributes include:
                                 * Identifier: The terse description of this attribute
                                 * Text:       The verbose description of this attribute
                                 */

    UF_PD_GOVERNMENT_SECURITY_INFO_TYPE, /* Government Security Info e-Marking. The attributes include:
                                          * Identifier: The terse description of this attribute
                                          * Text:       The verbose description of this attribute
                                          */

    UF_PD_COMPANY_PROPRIETARY_INFO_TYPE,   /* Company Proprietary Info e-Marking. The attributes include:
                                            * Identifier: The terse description of this attribute
                                            * Text:       The verbose description of this attribute
                                            */

    UF_PD_GENERIC_EMARKING_TYPE, /* Generic e-Marking. The attributes include:
                                  * Identifier: The terse description of this attribute
                                  * Text:       The verbose description of this attribute
                                  */

    UF_PD_SPUR_GEAR_TYPE,   /* Spur Gear. The attributes include:
                             * Number of teeth
                             * Internal/External
                             * Module
                             * Pressure Angle
                             * Pitch Diameter
                             * Base Diameter
                             * Major Diameter
                             * Minor Diameter
                             * Circular Tooth Thickness / Circular Space Width
                             * Measurement Over Two .xxxxx Dia Ball
                             * Ball Diameter
                             */

    UF_PD_HELICAL_GEAR_TYPE,     /* Helical Gear. The attributes include:
                                  * Number of teeth
                                  * Internal/External
                                  * Normal Module
                                  * Normal Pressure Angle
                                  * Helix Angle
                                  * Hand
                                  * Lead
                                  * Pitch Diameter
                                  * Base Diameter
                                  * Major Diameter
                                  * Minor Diameter
                                  * Circular Tooth Thickness / Circular Space Width
                                  * Measurement Over Two .xxxxx Dia Ball
                                  * Ball Diameter
                                  */

    UF_PD_STRAIGHT_SIDED_SPLINE_TYPE,  /* Straight Sided Spline. The attributes include:
                                        * Number of teeth
                                        * Internal/External
                                        * Tooth Profile Angle
                                        * Pitch Diameter
                                        * Base Diameter
                                        * Major Diameter
                                        * Minor Diameter
                                        * Minimum Form Diameter
                                        * Maximum Form Diameter
                                        * Minimum Effective Circular Tooth Thickness / Minimum
                                        Effective Circular Space Width
                                        * Maximum Effective Circular Tooth Thickness / Maximum
                                        Effective Circular Space Width
                                        * Minimum Actual Circular Tooth Thickness / Minimum
                                        Actual Circular Space Width
                                        * Maximum Actual Circular Tooth Thickness / Maximum
                                        Actual Circular Space Width
                                        * Measurement Over Two .xxxxx Dia Pin
                                        * Pin Diameter
                                        */

    UF_PD_INVOLUTE_SPLINE_TYPE,  /* Involute Spline. The attributes include:
                                  * Number of teeth
                                  * Internal/External
                                  * Pressure Angle
                                  * Pitch Diameter
                                  * Base Diameter
                                  * Major Diameter
                                  * Minor Diameter
                                  * Minimum Form Diameter
                                  * Maximum Form Diameter
                                  * Minimum Effective Circular Tooth Thickness / Minimum
                                  Effective Circular Space Width
                                  * Maximum Effective Circular Tooth Thickness / Maximum
                                  Effective Circular Space Width
                                  * Minimum Actual Circular Tooth Thickness / Minimum
                                  Actual Circular Space Width
                                  * Maximum Actual Circular Tooth Thickness / Maximum
                                  Actual Circular Space Width
                                  * Measurement Over Two .xxxxx Dia Pin
                                  * Pin Diameter
                                  */

    /* The number of Product Definition attribute types
     */
    UF_PD_NUM_ATTRIBUTE_TYPES  /* This must always be last */
};
typedef enum UF_PD_attribute_type_e
             UF_PD_attribute_type_t;

/*  This enumerated type defines the type of attribute values
 *  available.
 */
enum UF_PD_attribute_value_type_e
{
    UF_PD_INTEGER_VALUE,  /* NX product attribute integer value type */
    UF_PD_NUMBER_VALUE,   /* NX product attribute number value type */
    UF_PD_STRING_VALUE,   /* NX product attribute string value type */
    UF_PD_LIST_VALUE,     /* NX product attribute list value type */
    UF_PD_URL_VALUE       /* NX product attribute url value type */
};
typedef enum UF_PD_attribute_value_type_e
             UF_PD_attribute_value_type_t;

/*  Following is the enumerated type used to define the set of valid
 *  geometry types for a product definition attribute.
 */
typedef enum
{
    UF_PD_ALLOWABLE_GEOMETRY_ALL,
    UF_PD_ALLOWABLE_GEOMETRY_EDGE,
    UF_PD_ALLOWABLE_GEOMETRY_FACE,
    UF_PD_ALLOWABLE_GEOMETRY_BODY,
    UF_PD_ALLOWABLE_GEOMETRY_LINE,
    UF_PD_ALLOWABLE_GEOMETRY_POINT,
    UF_PD_ALLOWABLE_GEOMETRY_CONIC,
    UF_PD_ALLOWABLE_GEOMETRY_ARC,
    UF_PD_ALLOWABLE_GEOMETRY_SPLINE,
    UF_PD_ALLOWABLE_GEOMETRY_COMPONENT
} UF_PD_allowable_geometry_e;

/*  Following is the enumerated type used to define the set of valid
 *  business modifier types for a product definition attribute.
 */
typedef enum
{
    UF_PD_BUS_MODFR_STRING_TYPE = 0,         /* NX business modifier string type */
    UF_PD_BUS_MODFR_LIST_TYPE,               /* NX business modifier list type */
    UF_PD_BUS_MODFR_URL_TYPE,                /* NX business modifier url type */
    UF_PD_BUS_MODFR_REVISION_TYPE,           /* NX business modifier revision type */
    UF_PD_BUS_MODFR_SAFETY_CLASS_TYPE,       /* NX business modifier safety class type */
    UF_PD_BUS_MODFR_CUSTOMER_VALUE_TYPE      /* NX business modifier customer value type */
} UF_PD_BUS_MODFR_type_e;

/*  The following structure defines the attributes required
 *  to store a single attribute value. The data set is applied
 *  all NX product attribute except user defined attribute.
 */
struct UF_PD_attribute_value_s
{
    UF_PD_attribute_value_type_t value_type; /*  Type of attribute value (string, int, etc.)  */

    char *value_title; /* Title of the product attributes value,
                        * the valid value titles are defined in each product
                        * attribute, refer UF_PD_attribute_type_e
                       */

    int integer_value; /* Integer value of the attribute coresponding to the value_type */

    double number_value; /* Number value of the attribute coresponding to the value_type */

    char *string_value;  /* String value/list value of the attribute coresponding to the value_type */

};
typedef struct UF_PD_attribute_value_s
               UF_PD_attribute_value_t, *UF_PD_attribute_value_p_t;

/*  The following structure defines the business modifier required
 *  to store a single modifier value.
 */
struct UF_PD_business_modifier_s
{
    char *title; /* title of the defined business modifier */

    char *value; /* value of the defined business modifier */

};
typedef struct UF_PD_business_modifier_s
               UF_PD_business_modifier_t, *UF_PD_business_modifier_p_t;

/*  The following structure defines the attribute value data structure
 *  required define a product attributes. An attribute can has its own
 *  child value defined by UF_PD_attribute_value_s that is a real NX object.
 */
struct UF_PD_attribute_value_string_s
{
    int num_strings; /* number of strings defined for the attribute value data */

    char **strings;  /* <len:num_strings>
                        array of char * to hold multiple string text
                      */
};
typedef struct UF_PD_attribute_value_string_s
               UF_PD_attribute_value_string_t, *UF_PD_attribute_value_string_p_t;

struct UF_PD_attribute_value_data_s
{
    char *title; /* title of the defined attribute value data
                    this value data type is ONLY for user defined
                    attribute abd its value, and can't apply to
                    other NX existing product attribute
                  */

    UF_PD_attribute_value_string_t dat; /* value data structure to hold value data title and its strings */

};
typedef struct UF_PD_attribute_value_data_s
               UF_PD_attribute_value_data_t, *UF_PD_attribute_value_data_p_t;

/*  The following structure defines the attributes required
 *  define a product attributes.
 */
struct UF_PD_product_attribute_s
{
    UF_PD_attribute_type_t attribute_type; /* Type of attribute */

    char *attribute_group;     /* High level classification of the attribute */

    char *attribute_type_name;

    char *attribute_name; /* Name of the product attributes */

    char *symbolic_display;    /* Symbol in the format of <library>:<name> used to render the
                                  display of this attribute.  This information is extracted verbatim
                                  from the .dfa file, so it may be translated into a KF "rule".
                                */

    char *kf_name;     /* Name of product attributes defined from dfa file */

    int number_busmods;     /* Optional Business Modifiers for the attribute, it uses */

    UF_PD_business_modifier_p_t busmods; /* <len:number_busmods> */

    UF_PD_attribute_value_p_t values;    /* <len:num_attribute_values>
                                             Values for the product attribute.

                                             NOTE:
                                             An attribute can has its own child value object defined
                                             by UF_PD_attribute_value_s, it can also has its own value
                                             data set defined by UF_PD_product_attribute_value_data_s.

                                             UF_PD_attribute_value_s is for an existing NX object
                                             UF_PD_product_attribute_value_data_s is for user defined
                                             attribute or the user defined value data set.
                                             For example, the attribute value for UF_PD_UG_USER_DEFINED attribute
                                             type shall be defined here, and also user defined note text
                                             shall be defined here. */
    int num_attribute_values;

    UF_PD_attribute_value_data_p_t value_dats; /* <len:num_attribute_value_dats>
                                                  This is for NX user defined attribute and its value only,
                                                  please reference above for details.
                                                */
    int num_attribute_value_dats;
};
typedef struct UF_PD_product_attribute_s
               UF_PD_product_attribute_t, *UF_PD_product_attribute_p_t;

/*  Defines the type of user defined instance object  */
enum UF_PD_product_definition_instance_type_e
{
    UF_PD_PRODUCT_DEFINITION_INSTANCE_COMBINED,
    UF_PD_PRODUCT_DEFINITION_INSTANCE_USER_DEFINED
};
typedef enum UF_PD_product_definition_instance_type_e
             UF_PD_product_definition_instance_type_t;

/* The following structure is used to defined instance leader
 * associated point information
 */
enum UF_PD_product_definition_leader_assoc_pnt_type_e
{
    UF_PD_INSTANCE_LEADER_ASSOC_PNT_TAG_TYPE,
    UF_PD_INSTANCE_LEADER_ASSOC_NOMINAL_TYPE
};
typedef enum UF_PD_product_definition_leader_assoc_pnt_type_e
             UF_PD_product_definition_leader_assoc_pnt_type_t;

/*

    */

/* 
 */
struct UF_PD_product_definition_leader_assoc_pnt_s
{
    UF_PD_product_definition_leader_assoc_pnt_type_t type;
    union
    {
        tag_t pnt_tag;
        double pnt[3];
    } point;
};

/*

*/
typedef struct UF_PD_product_definition_leader_assoc_pnt_s
               UF_PD_product_definition_leader_assoc_pnt_t,
              *UF_PD_product_definition_leader_assoc_pnt_p_t;

/*  The following structure is used to define the leader data for the
 *  instance. The leader will look like
 *                             --- attachment (to annotation)
 *                            /
 *                           /
 *                       terminator (to geometry)
 *
 */
struct UF_PD_product_definition_leader_s
{
    UF_PD_product_definition_leader_assoc_pnt_t terminator;   /* terminator       */
    UF_PD_product_definition_leader_assoc_pnt_t attachment;   /* attached point   */
    tag_t assoc_object;                                       /* associate object */
};
typedef struct UF_PD_product_definition_leader_s
               UF_PD_product_definition_leader_t, *UF_PD_product_definition_leader_p_t;

/*  The following structure is used to define the instance data for the
 *  part.
 */
struct UF_PD_product_definition_instance_s
{
    UF_PD_product_definition_instance_type_t type; /* Type of instance to create */

    tag_t object_to_instance; /* Product definition object (either an attribute or an entire product
                               * definition) that needs to be instanced.
                               */

    double origin[3];     /* Origin of instance */

    UF_PD_product_definition_leader_p_t leaders;     /* <len:num_leaders>
                                                         Leaders data
                                                     */

    int num_leaders;
};
typedef struct UF_PD_product_definition_instance_s
               UF_PD_product_definition_instance_t, *UF_PD_product_definition_instance_p_t;

/*  The following structure defined the attributes required to
 *  define a product definition.
 */
struct UF_PD_product_definition_s
{
    char *name;     /*  Required name for the product definition  */

    tag_t *geometry_references; /* <len:num_geometry_references>
                                   Optional geometry references for a product definition
                                 */

    int num_geometry_references;

    logical retained;      /* Product Definition retain status */

    UF_PD_product_attribute_p_t product_attributes; /* <len:num_product_attributes>
                                                        Required (at least 1) attributes for a product definition
                                                     */
    int num_product_attributes;                     /* In NX4, product definition can only have ONE
                                                     * product attribute. num_product_attributes = 1 is accepted
                                                     * number, otherwise system will raise an error
                                                     */
};
typedef struct UF_PD_product_definition_s
               UF_PD_product_definition_t, *UF_PD_product_definition_p_t;

struct UF_PD_attribute_value_data_2_s
{
    char *title; /* title of the defined attribute value data
                    this value data type is ONLY for user defined
                    attribute abd its value, and can't apply to
                    other NX existing product attribute
                  */

    UF_PD_attribute_value_string_p_t dat; /* value data structure to hold value data title and its strings */

};
typedef struct UF_PD_attribute_value_data_2_s
               UF_PD_attribute_value_data_2_t, *UF_PD_attribute_value_data_2_p_t;

/*  The following structure defines the attributes required
 *  define a product attributes.
 */
struct UF_PD_product_attribute_2_s
{
    UF_PD_attribute_type_t attribute_type; /* Type of attribute */

    char *attribute_group;     /* High level classification of the attribute */

    char *attribute_type_name;

    char *attribute_name; /* Name of the product attributes */

    char *symbolic_display;    /* Symbol in the format of <library>:<name> used to render the
                                  display of this attribute.  This information is extracted verbatim
                                  from the .dfa file, so it may be translated into a KF "rule".
                                */

    char *kf_name;     /* Name of product attributes defined from dfa file */

    int number_busmods;     /* Optional Business Modifiers for the attribute, it uses */

    UF_PD_business_modifier_p_t busmods; /* <len:number_busmods> */

    UF_PD_attribute_value_p_t values;    /* <len:num_attribute_values>
                                             Values for the product attribute.

                                             NOTE:
                                             An attribute can has its own child value object defined
                                             by UF_PD_attribute_value_s, it can also has its own value
                                             data set defined by UF_PD_product_attribute_value_data_s.

                                             UF_PD_attribute_value_s is for an existing NX object
                                             UF_PD_product_attribute_value_data_s is for user defined
                                             attribute or the user defined value data set.
                                             For example, the attribute value for UF_PD_UG_USER_DEFINED attribute
                                             type shall be defined here, and also user defined note text
                                             shall be defined here. */
    int num_attribute_values;

    UF_PD_attribute_value_data_2_p_t value_dats; /* <len:num_attribute_value_dats>
                                                */
    int num_attribute_value_dats;
};
typedef struct UF_PD_product_attribute_2_s
               UF_PD_product_attribute_2_t, *UF_PD_product_attribute_2_p_t;

#ifdef __cplusplus
}
#endif

#endif /* UF_PD_DATATYPES_H_INCLUDED */
