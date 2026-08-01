/****************************************************************************

           Copyright (c) 2013 Siemens Co.
                         Unpublished - All rights reserved

===========================================================================

 

**********************************************************************************
File description:

This is part of the Open API for part and object attributes.
This file has the data types used by the API.

*/

#ifndef UF_ATTR_TYPES_INCLUDED
#define UF_ATTR_TYPES_INCLUDED

#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif



/***************************************************************************
           C O N S T A N T   &   T Y P E   D E F I N I T I O N S
*****************************************************************************/

/*
 * Maximum attribute string value and title length.
 * Note that UF_ATTR_MAX_STRING_LEN and UF_ATTR_MAX_TITLE_LEN have been
 * deprecated because NX is moving to support multibyte characters.  User
 * written programs should start using the new definitions:
 *     UF_ATTR_MAX_STRING_BUFSIZE
 *     UF_ATTR_MAX_TITLE_BUFSIZE
 *        should be used for buffer allocations and memory allocations, e.g.
 *          char buf[UF_ATTR_MAX_STRING_BUFSIZE];
 *          char my_title[UF_ATTR_MAX_TITLE_BUFSIZE];
 *
 *     UF_ATTR_MAX_STRING_NCHARS
 *     UF_ATTR_MAX_TITLE_NCHARS
 *        should be used to limit the number of characters in a buffer.
 *        NX code will enforce these limits.
 *
 * New routines have been added which will assist in this,
 *     UF_TEXT_count_characters() will count the characters in a string
 *     UF_TEXT_terminate_chars() will terminate a string after the given
 *                               number of characters.
 *
 */

#define UF_ATTR_MAX_STRING_NCHARS 132
#define UF_ATTR_MAX_STRING_BUFSIZE NX_BUFSIZE(UF_ATTR_MAX_STRING_NCHARS)
#define UF_ATTR_MAX_TITLE_NCHARS  50
#define UF_ATTR_MAX_TITLE_BUFSIZE NX_BUFSIZE(UF_ATTR_MAX_TITLE_NCHARS)

/*  */
#define UF_ATTR_MAX_STRING_LEN (UF_ATTR_MAX_STRING_BUFSIZE-1)
#define UF_ATTR_MAX_TITLE_LEN  (UF_ATTR_MAX_TITLE_BUFSIZE-1)
/*  */

/*****************************************************************************
 * Attribute type definitions
 ****************************************************************************/
#define UF_ATTR_integer    1
#define UF_ATTR_real       2
#define UF_ATTR_time       3
#define UF_ATTR_null       4
#define UF_ATTR_string     5
#define UF_ATTR_any        6
#define UF_ATTR_reference  7
#define UF_ATTR_bool       8

/****************************************************************************
 * Attribute Iterator Search Options Related To Arrays
 ****************************************************************************/
#define UF_ATTR_NOT_ARRAY -3
#define UF_ATTR_ANY_ATTRIBUTE -2
#define UF_ATTR_LAST_ELEMENT -1

/****************************************************************************
 * UF_ATTR_info_t
 *
 * User attribute information struct for setting and reading attributes
 *
 * All the data members of this struct are updated with values from the attribute when an attribute is read.
 *
 *        The following data members of this struct are not used (they are ignored) when setting an attribute:
 *        They are used only to report back information about the attribute when it is read.
 *          alias
 *          inherited
 *          override
 *          required
 *          unset
 *          locked (a separate function is used to manage locks)
 *          owned_by_system
 *          pdm_based
 *
 *      The following data of an attribute cannot be edited once the attribute is set:
 *          type
 *          title
 *          alias
 *          array
 *          array_element_index
 *          The dimensionality of the Unit specification (cannot change from mm to microA, but from mm to cm is fine)
 *
 *      The following data of an attribute can be set if and only if the attribute is not associated with a template. It cannot be modified once set.
 *          type
 *          alias
 *          array
 *          category
 *          The dimensionality of the Unit specification (cannot change from mm to microA, but from mm to cm is fine)
 *
 ****************************************************************************/
struct UF_ATTR_info_s
{
    int     type;                /* The type of the attribute. Valid values:
                                        UF_ATTR_bool
                                        UF_ATTR_integer
                                        UF_ATTR_real
                                        UF_ATTR_time
                                        UF_ATTR_null
                                        UF_ATTR_string
                                    (NOTE: The UF_ATTR_reference is not supported in the functions that use this struct)
                                 */
    char    *category;           /* The category of the attribute (may be NULL) */
    char    *title;              /* The title of the attribute (may be NULL when used to find attributes) */
    char    *alias;              /* The title alias of the attribute (may be NULL) */
    logical bool_value;          /* Boolean (logical) attribute value (default is returned when reading templates of non-set attributes) */
    int     integer_value;       /* Integer attribute value (default is returned when reading templates of non-set attributes) */
    double  real_value;          /* Real (double-precision real) attribute value (default is returned when reading templates of non-set attributes) */
    tag_t   unit_type;           /* The tag of the unit type, if any, if the attribute is a real-type attribute (may be NULL_TAG) */
    char    *unit_name;          /* The name of the unit type, if any, if the attribute is a real-type attribute (may be NULL)
                                    NOTE: This string is used only to return units in UF_ATTR_get_user_attributes_in_file */
    tag_t   expression;          /* An expression from which the attribute should get its value
                                    NOTE: This is not supported if the attribute has a reference string (in such case the attribute maintains a system expression internally).
                                    NOTE: This is not supported for attributes of type UF_ATTR_null or of type UF_ATTR_time */
    char    *string_value;       /* String attribute value (the default value is returned when reading templates of non-set attributes).
                                    This string is also returned for non-string attributes. */
    int     time_value[2];       /* Time/Date value (the default value is returned when reading templates of non-set attributes). 
                                    The time zone of the machine running the program is assumed */
    char    *time_string;        /* Time/Date value (the default value is returned when reading templates of non-set attributes).
                                    NULL is returned for non-time attributes */
    char    *reference_string;   /* Reference string of a string type attribute if it is defined using a reference string.
                                    NOTE: For these attributes, an expression reference cannot be used, as the attribute will maintain a system expression internally).
                                    NULL is returned for attributes that are not defined using a reference string. */
    logical inherited;           /* The attribute is inherited from another object and not overridden */
    logical override;            /* The attribute is overriding an inherited attribute */
    logical locked;              /* The attribute is locked.
                                    When an existing attribute is read, this flag indicates that the attribute cannot currently be modified.
                                    The flag is set if the attribute is created from a template that has the 'Locked' flag, or if
                                    it is reserved by the system or if is explicitly locked when set.
                                    When an unset attribute template is read, this flag indicates whether attributes created from the template will be
                                    locked when the part is saved and reloaded. */
    logical owned_by_system;     /* The attribute is a reserved system attribute.
                                    When this flag is set, the attribute can be set and removed only by the system. It is also created locked. It cannot be unlocked. */
    logical required;            /* This attribute is required on the given object */
    logical unset;               /* The attribute has not been set (i.e. has no value) on the object (used when getting attribute information) */
    logical array;               /* The attribute is an array attribute */
    int     index;               /* If this struct represents an array attribute element, this is the index (numerical, starting with 0).
                                    After reading an attribute, it is valid only if 'Unset' is 'false' and 'Array' is 'true'.
                                    The array size can be resized only one element at a time (adding or removing the last element). */
    logical pdm_based;           /* The attribute is synchronized with data in a PDM-system (Teamcenter). */
    void    *__initialized;      /* Mark used to determine if this struct has been initialized.
                                    (For internal use only - do not set/modify this member) */
};
typedef struct UF_ATTR_info_s UF_ATTR_info_t, *UF_ATTR_info_p_t;
typedef const struct UF_ATTR_info_s UF_ATTR_info_c_t, *UF_ATTR_info_pc_t;

/*****************************************************************************
 * UF_ATTR_iterator_t
 *
 * Iterator struct for querying and modifying user attributes
 *
 * This struct is used to identify attributes to be read, edited or deleted
 *
 *****************************************************************************/
struct UF_ATTR_iterator_s
{
    char    *category;                   /* Restricts search to attributes with this category (if 'check_category' is set to 'true') */
    logical check_category;              /* If set to 'true', restricts searches to attributes with the category specified by 'category'.
                                            (setting this to 'true' with 'category' = NULL allows searching for attributes that have no category) */
    char    *title;                      /* Restricts search to attributes with this title (if not NULL) */
    int     type;                        /* Restricts search to attributes with this type (if not set to UF_ATTR_any)
                                            Valid values:
                                                UF_ATTR_bool
                                                UF_ATTR_integer
                                                UF_ATTR_real
                                                UF_ATTR_time
                                                UF_ATTR_null
                                                UF_ATTR_string
                                                UF_ATTR_any
                                            (NOTE: The UF_ATTR_reference is not supported in the functions that use this struct) */
    int     index;                       /* Restricts search to attributes with a particular array element index, as follows:
                                                For all operations except deleting and locking/unlocking attributes:
                                                    If set to a non-negative number, the iterator will restrict search to array elements with the given index.
                                                    If set to UF_ATTR_ANY_ATTRIBUTE (default), the iterator will not restrict search to array elements.
                                                For delete operations:
                                                    If set to a non-negative number that is not equal to the last index of the array, the function will return an error.
                                                    If set to UF_ATTR_ANY_ATTRIBUTE (default), the iterator will not restrict search to array elements.
                                                    If set to UF_ATTR_LAST_ELEMENT, the iterator will delete the last element of an array.
                                                For locking/unlocking operations:
                                                    If set to UF_ATTR_ANY_ATTRBUTE (default), the iterator wil not restrict search to array elements.
                                                    For arrays, locks are always set/unset on all the elements.
                                                For all operations:
                                                    If set to anything other than specified above, the function will return an error */
    logical include_also_unset;          /* Expands search to the object's unset associated user attribute templates (if values are returned for these, they are the default values) */
    logical include_only_unset;          /* Restricts search to the object's unset associated user attribute templates (if values are returned for these, they are the default values) */
    logical include_only_pdm_based;      /* Restricts search to DM-based attributes (attributes that are synchronized with Teamcenter) */
    void    *__initialized;              /* Mark used to determine if this struct has been initialized and/or reset.
                                            (For internal use only - do not set/modify this member) */
};
typedef struct UF_ATTR_iterator_s UF_ATTR_iterator_t, *UF_ATTR_iterator_p_t;
typedef const struct UF_ATTR_iterator_s UF_ATTR_iterator_c_t, *UF_ATTR_iterator_pc_t;
    
/****************************************************************************
 *
 *  THE FOLLOWING STRUCTS AND FUNCTIONS ARE NOT RECOMMENDED FOR USE IN NEW APPLICATIONS
 *
 ****************************************************************************/

/*****************************************************************************
 * Attribute value
 ****************************************************************************/
union UF_ATTR_value_u
{
    logical  boolean;  /* If the attribute is a boolean attribute, 
                          this can be used to access the value.
                          The values taken are 'true' and 'false'. */
    int    integer;    /* If the attribute is an integer attribute,
                          this can be used to access the value. */
    double real;       /* If the attribute is a floating point attribute,
                          this can be used to access the value. */
    int    time[2];    /* If the attribute is a date/time attribute,
                          this can be used to access the value.
                          time[0] contains the NX computational date
                          time[1] contains the NX computational time. 
                          The time here is assumed to be in the time zone of the user.
                          When saved, the time is converted to UTC.*/
    char   *string;    /* If the attribute is a string or reference attribute, then
                          this is a pointer to the value. The maximum length
                          of this string is limited by UF_ATTR_MAX_STRING_BUFSIZE */

    char   *reference; /* If the attribute is a reference attribute, then
                          this is a pointer to the reference string value.  
                          The value may have an embedded expression with 
                          the following syntax:
                              <Xm.n@exp_name> or <Xm,n@exp_name>
                          The X indicates that an expression is being
                          referenced.  The m specifies the minimum field
                          width.  If necessary, it is padded on the left to
                          make up the field width.  The n specifies the
                          maximum number of digits after the decimal point of
                          the expression value.  The decimal point can be
                          specified as either . or , thus either m.n or m,n
                          are acceptable.  
                          This field is only used when setting a reference
                          value and when specifically asking for the reference
                          string value. UF_ATTR_cycle and UF_ATTR_read_value
                          will return the evaluated value, not the reference string.*/
} ;

typedef union UF_ATTR_value_u UF_ATTR_value_u_t, *UF_ATTR_value_u_p_t;
/*****************************************************************************
 * Typed attribute value
 ****************************************************************************/
struct UF_ATTR_value_s
{
    int type;                 /* The type of the attribute.  Valid types are:
                                 UF_ATTR_bool
                                 UF_ATTR_integer
                                 UF_ATTR_real
                                 UF_ATTR_time
                                 UF_ATTR_null
                                 UF_ATTR_string
                                 UF_ATTR_reference
                              */
    UF_ATTR_value_u_t value;  /* The attribute value */
} ;

typedef struct UF_ATTR_value_s UF_ATTR_value_t, *UF_ATTR_value_p_t;

/*****************************************************************************
 * Structure used to return part attribute values.
 *
 ****************************************************************************/
struct UF_ATTR_part_attr_s
{
    char      title[UF_ATTR_MAX_TITLE_BUFSIZE];  /* <len:UF_ATTR_MAX_TITLE_BUFSIZE>
                                                  The title of the attribute */
    UF_ATTR_value_t value;                     /* The value for the part attribute */
    char      string_value[UF_ATTR_MAX_STRING_BUFSIZE]; 
                                               /* <len:UF_ATTR_MAX_STRING_BUFSIZE> 
                                                  Buffer for the part
                                                  attribute string value 
                                                  (if of type string).
                                                  The character pointer 
                                                  .value.value.string
                                                  will then point to this buffer. */
};

typedef struct UF_ATTR_part_attr_s UF_ATTR_part_attr_t, *UF_ATTR_part_attr_p_t;

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_ATTR_INCLUDED */
