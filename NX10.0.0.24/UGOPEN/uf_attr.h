/****************************************************************************

           Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                         Unpublished - All rights reserved

===========================================================================

 

**********************************************************************************
File description:

This is the Open API interface to part and object attributes.

Using the UF_ATTR subroutines, you can:
     .  Assign an attribute title and value to an object.
     .  Count the attributes with a specific type for an object.
     .  Cycle through all attributes of a specific type from an object.
     .  Delete an attribute of a specific type from an object.
     .  Delete all attributes of a specific type from an object.
     .  Search an object for a specified attribute title.
     .  Read the value of an attribute with a specified type and title.

The API consists of two subsets, a post-NX8 set and a pre-NX8 set.

The pre-NX8 set.
The pre-NX8 set (legacy) set supports applications written against pre-NX8 versions of NX.
We have tried to make sure that such applications can continue to function without changes.
The functions in this set do not have string 'user_attribute' as part of the name.
It does not support some of the new enhancements that were introduced in NX8
during a major restructuring of the user attribute functionality. This set also
treats PDM-based attributes (attributes that are mapped to and from the
Teamcenter PDM system) differently from other attributes, as follows:

    a. Reading a set PDM-based attribute will return it as being of string type
       independent of its actual type. The actual value will be converted to a
       string using conversions similar to those converting PDM-based attributes
       to string type prior to NX8.
    b. An attempt to read an unset PDM-based attribute will return it a set
       attribute of string type with an empty string as its value.
    c. Setting a PDM-based attribute requires that the input be of string type.
       The actual value will be converted to a value of the actual type prior
       to creating an attribute of that (the actual) type.
    d. Setting a PDM-based attribute with an empty string as input will remove
       the attribute from NX.
       
The post-NX8 set.
The expanded set supports a number of enhancements that were introduced in NX8
during a major restructuring of the user attribute functionality. This set
is labelled 'recommended' below. All the functions in this set have the string
'user_attribute' as part of the name.
This set can be used to by legacy applications to take advantage of the 
NX8 attribute enhancements or it can be used to build new applications.

**********************************************************************************
Unset Attributes

Some functions in this API will return values for 'unset' attributes. While an
object has a virtual infinity of unset attributes, the ones returned by this API
are restricted to titles for which the object has an associated attribute template.
If there is no attribute, but there is a template, then the attribute is said to be
'unset'.
As noted above, the pre-NX8 API does not support this concept. Instead it will 
treat all 'unset' PDM-based attributes as 'set', but empty, string attributes.
The post-NX8 API fully supports the notion of 'unset' attributes.

**********************************************************************************
Object Tags

The functions in this file will accept the tag of any object that supports attributes.
The tags for a part object or for a part attribute object (UF_ATTR_ask_part_attribute) can be
used interchangeably.

**********************************************************************************
Units

When setting attributes with units, the functions here require the tag of a unit type.
These tags can be obtained via the UNIT API (see uf_unit.h).
The UNIT API also allows for the conversion of values between compatible units.

**********************************************************************************
NX Date & Time Formats

NX computational date and time is stored in an integer array consisting of two
elements. The first array element contains the NX Computational Date, while
the second contains the NX Computational Time.

NX Computational Time stores the number of six second intervals since midnight,
that is it is incremented every six seconds.  The computation is:

  NX_computations_time = 10* (60*Hour+Minute) + Second/6

where Hour = Hour of day on 24 hour clock and Minute = Minute of hour, and
Second is the Seconds of the minute.

NX also allows for time attribute values to be entered and read via a formatted string.
In order to understand such formatted strings, NX needs to know the format used to create them.
The time to string conversion format is set via the following environment variable:
'UGII_DEFAULT_DATE_ATTRIBUTE_DISPLAY_FORMAT'
It can also be set via this API (UF_ATTR_set_time_string_format).
Further, when NX is run in managed mode, then Teamcenter may also provide a format via the preferences 'NXDefaultDateFormat' (preferred) or 'DefaultDateFormat'.

The following describes the syntax of the format string. Constant strings may be interspersed between tokens.

              %b  abbreviated month name
              %B  full month name
              %d  day of the month(0-31)
              %H  hour(24-hour clock)(00-23)
              %I  hour(12-hour clock)(01-12)
              %m  month(01-12)
              %M  minute(00-59)
              %S  second(00-59)
              %y  year without century(00-99)
              %Y  year with century(1970-2069)

           Example:
              %d-%b-%Y %H:%M:%S    is the format that gives    01-Mar-2011 22:16:32

If no format is set, then the example format is used by default.

**********************************************************************************
Locks

To enable an NXOpen program to modify the locks of an attribute, the user name under which the 
program is run must have privilege to do so. This privilege is set via the
Customer Default option 
'UG_AllowAttributeLockingInNXOpen'

**********************************************************************************
Reference Strings

In NX8, reference type attributes (UF_ATTR_reference) are no longer supported as a different type.
These attributes are converted to string type with references to a string expression that
implements the formula describe the reference string.
When these attributes are read, the string expression formula is converted back
to a reference string.

When a reference string has a token that picks up a value from a number expression that
has units, then the resulting expression formula is created to format the expression's value
using the display units at the time of the creation of the referenced expression. This
formula does not change if the original expression's display units change. However, the
formula can be manually edited in the expression dialog as needed. Alternatively, the
attribute can be reset, at which time it will gain the new units.

**********************************************************************************
Templates

There are currently no plans to support the creation of templates in this API.

**********************************************************************************
Material and Mass Property Related System-Owned Attributes

Prior to NX10, certain system attributes had their titles defined
via Customer Defaults. In NX10, they were given hard-coded titles and aliases defined
via Customer Defaults. 
Given that external applications may be looking for these attributes via
their old titles, the functions in this API that specifically looks for attributes
via a title will work when given an alias of one of these attributes.
We list here the new hard-coded titles together with the old default titles and 
new default aliases. If, prior to NX10 you used
titles other than the defaults, then for this to work you need to set the new
alias to the same as what the titles were set to before.

New Title                     Old Default Title and New Default Alias
---------------------------------------------------------------------
NX_Material                   Material
NX_ObjectMaterial             ObjectMaterial
NX_MaterialMultipleAssigned   MaterialMultipleAssigned
NX_MaterialMissingAssignments MaterialMissingAssignments
NX_MaterialPreferred          MaterialPreferred
NX_MassPropDensity            MassPropDensity
NX_MassPropMass               MassPropMass
NX_MassPropWeight             MassPropWeight
NX_MassPropVolume             MassPropVolume
NX_MassPropArea               MassPropArea

NOTE: No other attributes than those converted in this way by Siemens will
be able to be reached by this API via an alias. Using aliases in applications
is not recommended because aliases can change. In fact the above mentioned changes
were partly made to ensure that access to these attributes by applications be
independent of the Customer Default settings. Using aliases also has
performance impacts because of the need to search for matching titles. Lastly,
in some applications it is possible for attributes to share aliases, so
an attribute cannot in all cases be uniquely identified via an alias.


 */

#ifndef UF_ATTR_INCLUDED
#define UF_ATTR_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_attr_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************
 * UF_ATTR_init_user_attribute_info
 *
 * Initializes a UF_ATTR_info_t struct as follows:
 *
 *   All strings are set to NULL.
 *   All numerical values are set to 0 or 0.0.
 *   All logical values are set to false.
 *   All tags are set to 0
 *
 * NOTE: This function must be called before the struct can be used
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_init_user_attribute_info
(
    UF_ATTR_info_p_t info           /* <I/O> the attribute information to be initialized */
);

/*****************************************************************************
 * UF_ATTR_free_user_attribute_info_strings
 *
 * Frees the strings held by a UF_ATTR_info_t struct.
 *
 *   All strings held by the struct are freed. 
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_free_user_attribute_info_strings
(
    UF_ATTR_info_p_t info          /* <I/O> the attribute information containing strings to be freed */
);

/*****************************************************************************
 * UF_ATTR_free_user_attribute_info_array
 *
 * Frees the strings held by an array of UF_ATTR_info_t structs as well as the array itself.
 * (Use after call to UF_ATTR_get_user_attributes)
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_free_user_attribute_info_array
(
    int count,                     /* <I>   the count of attribute information structs in the array */
    UF_ATTR_info_t info[]          /* <I>   the array of attribute information structs to be freed */
);

/*****************************************************************************
 * UF_ATTR_init_user_attribute_iterator
 *
 * Initializes a UF_ATTR_iterator_t struct as follows:
 *
 *   All strings are set to empty.
 *   All logical values are set to 'false'.
 *   The 'type' is set to 'UF_ATTR_any'.
 *   The 'array_element_index' is set to 'UF_ATTR_ANY_ATTRIBUTE'
 *   
 *   NOTE: If the info has pointers to strings that it does not own, such strings must be
 *         set to NULL before this function is called.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ******************************************************************************/
extern UFUNEXPORT int UF_ATTR_init_user_attribute_iterator
(
    UF_ATTR_iterator_p_t iter       /* <I/O> the attribute iterator to be initialized */
);

/*****************************************************************************
 * UF_ATTR_release_user_attribute_iterator
 *
 * Resets and releases for re-use a UF_ATTR_iterator_t struct.
 *
 *   This must be done in two situations:
 *
 *     a. Before the iterator is to be reused for another iteration.
 *     b. When the iterator is no longer in use
 *
 *   This function does not free the strings supplied with the iterator or the iterator itself,
 *   but it does free internal memory associated with the iterator.
 *
 *   If a release is not done after the iteration is completed, the iterator may
 *   produce unpredictable results when reused.
 *   If a release is not done after the iterator is retired, the iterator will leak internal memory.
 *
 *   NOTE: Releasing an iterator twice is OK.
 *         Iterations that are always completed (such when used in UFT_ATTR_has_user_attribute())
 *         will automatically release the iterator. Please see the individual functions for details.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ******************************************************************************/
extern UFUNEXPORT int UF_ATTR_release_user_attribute_iterator
(
    UF_ATTR_iterator_p_t iter       /* <I/O> the attribute iterator to be released */
);

/*****************************************************************************
 * UF_ATTR_free_user_attribute_iterator_strings
 *
 * Frees the strings held by a UF_ATTR_iterator_t struct.
 *
 *   All strings held by the struct are freed. 
 *   Note: The UF_ATTR API does not supply the strings held by this struct, this
 *         function for convenience only.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_free_user_attribute_iterator_strings
(
    UF_ATTR_iterator_p_t iterator          /* <I/O> the attribute iterator containing strings to be freed */
);


/*****************************************************************************
 * UF_ATTR_set_time_string_format
 *
 * Sets the format used to convert a time attribute value to a string (and vice versa)
 * This function will override (replaces) any format set via the environment variable 'UGII_DEFAULT_DATE_ATTRIBUTE_DISPLAY_FORMAT'.
 * To allow setting a format temporarily, this function returns the existing format.
 *            The given format is a string that has the following tokens. Interspersed text will be copied:
 *              %b  abbreviated month name
 *              %B  full month name
 *              %d  day of the month(0-31)
 *              %H  hour(24-hour clock)(00-23)
 *              %I  hour(12-hour clock)(01-12)
 *              %m  month(01-12)
 *              %M  minute(00-59)
 *              %S  second(00-59)
 *              %y  year without century(00-99)
 *              %Y  year with century(1970-2069)
 *
 *           Example:
 *              %d-%b-%Y %H:%M:%S    is the format that gives    01-Mar-2011 22:16:32
 *
 * If no format is set (via the environment variable or via this function), then the example format is used by default.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_time_string_format
(
    const char *new_format, /* <I>  The new format to be used */
    char **old_format       /* <OF> The format previously in used (optional - may be NULL.
                                    If not NULL, the caller is responsible for freeing the returned old format string. 
                                    Free using UF_free() after use.*/
);

/*****************************************************************************
 * UF_ATTR_set_user_attribute
 *
 * Creates or modifies an attribute with the option to update or not.
 * 
 *  NOTE: To set a date/time type attribute, either a formatted string or a computational value may be used.
 *        If both are set (the string is not empty ("") and the computational value is not (0,0)), then the computational value will take precedence.
 *        The time value in either case is in the current time zone of the machine running the program.
 *
 *  NOTE: To set a real type attribute, there is the option to include a units specification.
 *        The supplied 'unit_type' must be consistent with the unit specification of an existing attribute or template with same title.
 *        In other words, the attribute's unit measure cannot change, but its display units can.
 *        If 'unit_type' are not supplied (the tag is NULL_TAG)
 *            If an existing attribute or template is found, then the units of that attribute or template are used.
 *            If no existing attribute or template is found, then the attribute is set to be unit-less.
 *        If 'unit_type' are supplied:
 *            If an existing attribute is found, then that attribute's display unit is modified to use the input 'unit_type'.
 *            If no existing attribute is found, then the attribute is created with the given 'unit_type' as its display units.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_user_attribute
(
    tag_t object,                   /* <I> The object receiving the attribute */
    const UF_ATTR_info_t *info,     /* <I> The attribute information for the attribute (make sure to initialize it first) */
    logical update                  /* <I> Perform an update immediately */
);

/*****************************************************************************
 * UF_ATTR_set_null_user_attribute
 *
 * Creates a null type attribute with the option to update or not.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_null_user_attribute
(
    tag_t object,                   /* <I> The object receiving the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    logical update                  /* <I> Perform an update immediately */
);
   
/*****************************************************************************
 * UF_ATTR_set_boolean_user_attribute
 *
 * Creates a boolean type attribute with the option to update or not.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_bool_user_attribute
(
    tag_t object,                   /* <I> The object receiving the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    logical value,                  /* <I> The value */
    logical update                  /* <I> Perform an update immediately */
);
   
/*****************************************************************************
 * UF_ATTR_set_integer_user_attribute
 *
 * Creates a integer type attribute with the option to update or not.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_integer_user_attribute
(
    tag_t object,                   /* <I> The object receiving the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    int value,                      /* <I> The value */
    logical update                  /* <I> Perform an update immediately */
);
   
/*****************************************************************************
 * UF_ATTR_set_real_user_attribute
 *
 * Creates a real type attribute with the option to update or not.
 *
 *  NOTE: The supplied 'unit_type' must be consistent with the unit specification of an existing attribute or template with same title.
 *        In other words, the attribute's unit measure cannot change, but its display units can.
 *        If 'unit_type' are not supplied (set to NULL_TAG), then:
 *            If an existing attribute or template is found, then the units of that attribute or template are used.
 *            If no existing attribute or template is found, then the attribute is set to be unit-less.
 *        If 'unit_type' are supplied, then:
 *            If an existing attribute is found, then that attribute's display unit is modified to use the input 'unit_type'.
 *            If no existing attribute is found, then the attribute is created with the given 'unit_type' as its display units.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_real_user_attribute
(
    tag_t object,                   /* <I> The object receiving the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    double value,                   /* <I> The value */
    tag_t unit_type,                /* <I> The unit type tag (may be NULL_TAG) */
    logical update                  /* <I> Perform an update immediately */
);
   
/*****************************************************************************
 * UF_ATTR_set_string_user_attribute
 *
 * Creates a string type attribute with the option to update or not.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_string_user_attribute
(
    tag_t object,                   /* <I> The object receiving the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    const char *value,              /* <I> The value */
    logical update                  /* <I> Perform an update immediately */
);
   
/*****************************************************************************
 * UF_ATTR_set_reference_string_user_attribute
 *
 * Creates a string type attribute with the option to update or not.
 * This string attribute will be created with the given reference string.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_reference_string_user_attribute
(
    tag_t object,                   /* <I> The object receiving the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    const char *reference_string,   /* <I> The reference string */
    logical update                  /* <I> Perform an update immediately */
);
   
/*****************************************************************************
 * UF_ATTR_set_computational_time_user_attribute
 *
 * Creates a time type attribute with the option to update or not.
 *
 * The time value must be entered in the current time zone of the machine running the program.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_computational_time_user_attribute
(
    tag_t object,                   /* <I> The object receiving the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    int value[2],                   /* <I> The time value {day,min} */
    logical update                  /* <I> Perform an update immediately */
);
   
/*****************************************************************************
 * UF_ATTR_set_string_time_user_attribute
 *
 * Creates a time type attribute with the option to update or not.
 *
 * The time value in either case is in the current time zone of the machine running the program.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_string_time_user_attribute
(
    tag_t object,                   /* <I> The object receiving the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    const char *value,              /* <I> Time/Date value as a formatted string */
    logical update                  /* <I> Perform an update immediately */
);
   
/****************************************************************************
 * UF_ATTR_get_user_attribute_with_title_and_type
 *
 * Gets the information from the attribute with the given title and type
 *
 * Environment: Internal and External
 * History: NX8.5.3
*****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_user_attribute_with_title_and_type
(
    tag_t object,                   /* <I>  The object holding the attribute */
    const char *title,              /* <I>  The attribute title */
    int type,                       /* <I>  The attribute type 
                                            Valid values:
                                               UF_ATTR_integer
                                               UF_ATTR_real
                                               UF_ATTR_time
                                               UF_ATTR_null
                                               UF_ATTR_string
                                               UF_ATTR_bool
                                               UF_ATTR_any
                                            NOTE: If UF_ATTR_any is used, the first attribute encountered that matches
                                                  the given title (and index), is returned
                                    */
    int index,                      /* <I>  The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    UF_ATTR_info_t *info,           /* <OF> The attribute information for the first attribute (or unset template) found, if any.
                                            This struct must be freed using UF_ATTR_free_user_attribute_info_strings() after use. */
    logical *has_attribute          /* <O>  An attribute or (if the iterator allows it) an unset template has been found*/
);

/****************************************************************************
 * UF_ATTR_get_user_attribute
 *
 * Gets the information from the first attribute, if any, that satisfies the given iterator.
 *
 * Environment: Internal and External
 * History: NX8.5.3
*****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_user_attribute
(
    tag_t object,                   /* <I>  The object holding the attribute */
    const UF_ATTR_iterator_t *iter, /* <I>  Iterator describing the attribute being queried.
                                            The iterator is automatically reset. */
    UF_ATTR_info_t *info,           /* <OF> The attribute information for the first attribute (or unset template) found, if any.
                                            This struct must be freed using UF_ATTR_free_user_attribute_info_strings() after use. */
    logical *has_attribute          /* <O>  An attribute or (if the iterator allows it) an unset template has been found*/
);

/****************************************************************************
 * UF_ATTR_get_null_user_attribute
 *
 * Queries the presence of a null type attribute
 *
 * Environment: Internal and External
 * History: NX8.5.3
*****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_null_user_attribute
(
    tag_t object,                   /* <I> The object holding the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    logical *has_attribute          /* <O> An attribute has been found */
);

/****************************************************************************
 * UF_ATTR_get_bool_user_attribute
 *
 * Gets value of a boolean type attribute, if it exists
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_bool_user_attribute
(
    tag_t object,                   /* <I> The object holding the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    logical *value,                 /* <O> The value, if any */
    logical *has_attribute          /* <O> An attribute has been found */
);

/****************************************************************************
 * UF_ATTR_get_integer_user_attribute
 *
 * Gets the value of a integer type attribute, if it exists
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_integer_user_attribute
(
    tag_t object,                   /* <I> The object holding the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    int *value,                     /* <O> The value, if any */
    logical *has_attribute          /* <O> An attribute has been found */
);

/****************************************************************************
 * UF_ATTR_get_real_user_attribute
 *
 * Gets the value and units of a real type attribute, if it exists
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_real_user_attribute
(
    tag_t object,                   /* <I> The object holding the attribute */
    const char *title,              /* <I> The attribute title */
    int index,                      /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    double *value,                  /* <O> The value, if any. If attribute has units, this value is in the returned units. */
    tag_t *unit_type,               /* <O> The unit type tag (NULL_TAG may be returned if unit-less) */
    logical *has_attribute          /* <O> An attribute has been found */
);

/****************************************************************************
 * UF_ATTR_get_string_user_attribute
 *
 * Gets the value and reference string (if any) of a string type attribute, if it exists
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_string_user_attribute
(
    tag_t object,                    /* <I>  The object holding the attribute */
    const char *title,               /* <I>  The attribute title */
    int index,                       /* <I>  The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    char **string_value,             /* <OF> String attribute value (Free using UF_free() after use) */
    logical *has_attribute           /* <O>  An attribute has been found */
);

/****************************************************************************
 * UF_ATTR_get_reference_string_of_user_attribute
 *
 * Gets the reference string (if any) of a string type attribute, if it exists and it has a reference string
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_reference_string_of_user_attribute
(
    tag_t object,                    /* <I>  The object holding the attribute */
    const char *title,               /* <I>  The attribute title */
    int index,                       /* <I>  The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    char **reference_string,         /* <OF> Reference string (Free using UF_free() after use) */
    logical *has_attribute           /* <O>  An attribute has been found AND it has a reference string */
);

/****************************************************************************
 * UF_ATTR_get_computational_time_user_attribute
 *
 * Gets the value of a time type attribute, if it exists
 * The returned time is in the local time of the program that is running.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_computational_time_user_attribute
(
    tag_t object,                     /* <I> The object holding the attribute */
    const char *title,                /* <I> The attribute title */
    int index,                        /* <I> The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    int value[2],                     /* <O> Time/Date value as computational time */
    logical *has_attribute            /* <O> An attribute has been found */

);

/****************************************************************************
 * UF_ATTR_get_string_time_user_attribute
 *
 * Gets the value of a time type attribute, if it exists
 * The returned time is in the local time of the program that is running.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_string_time_user_attribute
(
    tag_t object,                     /* <I>  The object holding the attribute */
    const char *title,                /* <I>  The attribute title */
    int index,                        /* <I>  The array index (set to UF_ATTR_NOT_ARRAY if not an array) */
    char **time_string,               /* <OF> Time/Date value formatted as a string (Free using UF_free() after use) */
    logical *has_attribute            /* <O>  An attribute has been found */
);

/****************************************************************************
 * UF_ATTR_get_next_user_attribute
 *
 * Gets the information from the next attribute that satisfies the given iterator
 *
 *   NOTE: If the iteration is allowed to completed, the iterator is automatically reset.
 *         If not, it must be reset with 'UF_ATTR_release_user_attribute_iterator()', or the iterator will leak memory.
 *   NOTE: The supplied 'info' struct must be initialized before use.
 *         Between calls to this function, the 'info' struct's strings do not have to be freed, as this is done prior to reading an attribute.
 *         However after the last call, the returned 'info' struct's strings must be freed.
 *         This can be done with UF_ATTR_free_user_attribute_info_strings().
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_next_user_attribute
(
    tag_t object,                   /* <I>  The object holding the attribute */
    UF_ATTR_iterator_t *iter,       /* <I>  Iterator describing the attribute being queried.
                                            If iteration is allowed to complete, iterator is reset by the system.
                                            If not, reset with UF_ATTR_release_user_attribute_iterator() after use. */
    UF_ATTR_info_t *info,           /* <OF,free:UF_ATTR_free_user_attribute_info_strings> The attribute information for the first attribute (or unset template) found, if any.
                                            After iteration ends, free embedded strings using UF_ATTR_free_user_attribute_info_strings(). */
    logical *has_attribute          /* <O>  An attribute (or unset template) has been found. If 'false', this ends the iteration. */
);

/****************************************************************************
 * UF_ATTR_has_user_attribute_with_title_and_type
 *
 * Query the object for the existence of an attribute that satisfies the given title and type.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_has_user_attribute_with_title_and_type
(
    tag_t object,                   /* <I> The object holding the attributes */
    const char *title,              /* <I> The title of the attribute */
    int type,                       /* <I> The attribute type 
                                           Valid values:
                                              UF_ATTR_integer
                                              UF_ATTR_real
                                              UF_ATTR_time
                                              UF_ATTR_null
                                              UF_ATTR_string
                                              UF_ATTR_bool
                                              UF_ATTR_any
                                           NOTE: If UF_ATTR_any is used, the first attribute encountered that matches
                                                 the given title (and index), is noted as being present
                                    */
    int index,                      /* <I> The array index ((set to UF_ATTR_NOT_ARRAY if not an array) */
    logical *has_attribute          /* <O> An attribute (or unset template) has been found */
);

/****************************************************************************
 * UF_ATTR_has_user_attribute
 *
 * Query the object for the existence of an attribute that satisfies the given iterator
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_has_user_attribute
(
    tag_t object,                   /* <I> The object holding the attributes */
    const UF_ATTR_iterator_t *iter, /* <I> Iterator describing the attributes being queried.
                                           The iterator is automatically reset. */
    logical *has_attribute          /* <O> An attribute (or unset template) has been found */
);

/****************************************************************************
 * UF_ATTR_count_user_attributes
 *
 * Count the number of attributes that satisfy the given iterator
 *
 * NOTE: This function counts individual array elements of arrays
 *       (in other words, an array with 'n' elements adds 'n' to the returned count.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_count_user_attributes
(
    tag_t object,                   /* <I> The object holding the attributes */
    const UF_ATTR_iterator_t *iter, /* <I> Iterator describing the attributes being counted.
                                           The iterator is automatically reset. */
    int *count                      /* <O> The count of attributes (and/or unset templates) found */
);

/****************************************************************************
 * UF_ATTR_count_user_attribute_titles
 *
 * Count the number of attributes that satisfy the given iterator
 *
 * NOTE: This function counts array attributes as one title.
 *       (in other words, an array with 'n' elements adds only one to the returned count.
 *
 * Environment: Internal and External
 * History: NX10.0.0
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_count_user_attribute_titles
(
    tag_t object,                   /* <I> The object holding the attributes */
    const UF_ATTR_iterator_t *iter, /* <I> Iterator describing the attributes being counted.
                                           The iterator is automatically reset. */
    int *count                      /* <O> The count of attributes (and/or unset templates) found */
);

/****************************************************************************
 * UF_ATTR_get_user_attributes
 *
 * Get information for all the attributes that satisfy the given iterator.
 * This function will return an array of UF_ATTR_info_t structs that must be
 * freed after use with UF_ATTR_free_user_attribute_info_array()
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_get_user_attributes
(
    tag_t object,                   /* <I>  The object holding the attributes */
    const UF_ATTR_iterator_t *iter, /* <I>  Iterator describing the attributes being queried.
                                            The iterator is automatically reset. */
    int *num_attributes,            /* <O>  The number of attributes returned */
    UF_ATTR_info_t **info           /* <OF,len:num_attributes,free:UF_ATTR_free_user_attribute_info_array> 
                                            The information for the attributes (and/or unset templates) found.
                                            Free using UF_ATTR_free_user_attribute_info_array() after use */
);

/****************************************************************************
 * UF_ATTR_delete_user_attribute_with_title_and_type
 *
 * Delete the attribute with the given title and type
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_delete_user_attribute_with_title_and_type
(
    tag_t object,                   /* <I> The object holding the attributes */
    const char *title,              /* <I> The title of the attribute */
    int type,                       /* <I> The attribute type 
                                           Valid values:
                                              UF_ATTR_integer
                                              UF_ATTR_real
                                              UF_ATTR_time
                                              UF_ATTR_null
                                              UF_ATTR_string
                                              UF_ATTR_bool
                                              UF_ATTR_any
                                           NOTE: If UF_ATTR_any is used, the first attribute encountered that matches
                                                 the given title (and index), is deleted
                                    */
    int index,                      /* <I> The array index 
                                           Set to UF_ATTR_NOT_ARRAY if the attribute is not an array.
                                           Set to UF_ATTR_LAST_ELEMENT if the attribute is an array.
                                    */
    logical update                  /* <I> Perform an update immediately */
);

/****************************************************************************
 * UF_ATTR_delete_user_attributes
 *
 * Delete all the attributes that satisfy the given iterator.
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_delete_user_attributes
(
    tag_t object,                   /* <I> The object holding the attributes */
    const UF_ATTR_iterator_t *iter, /* <I> Iterator describing the attributes to be deleted.
                                           The iterator is automatically reset. */
    logical update                  /* <I> Perform an update immediately */
);

/****************************************************************************
 * UF_ATTR_set_user_attribute_lock_with_title_and_type
 *
 * Set the locks on the attributes with the given title and type
 *
 * NOTE: This function cannot set locks on individual array elements
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_user_attribute_lock_with_title_and_type
(
    tag_t object,                   /* <I> The object holding the attributes */
    const char *title,              /* <I> The title of the attribute */
    int type,                       /* <I> The attribute type 
                                           Valid values:
                                              UF_ATTR_integer
                                              UF_ATTR_real
                                              UF_ATTR_time
                                              UF_ATTR_null
                                              UF_ATTR_string
                                              UF_ATTR_bool
                                              UF_ATTR_any
                                           NOTE: If UF_ATTR_any is used, the first attribute encountered that matches
                                                 the given title will have its lock modified
                                    */
    logical locked                  /* <I> The status of the lock to be set ('true': locked or 'false': unlocked) */
);
 
/****************************************************************************
 * UF_ATTR_set_user_attribute_locks
 *
 * Set the locks on all the attributes that satisfy the given iterator.
 *
 * NOTE: This function cannot set locks on individual array elements
 *
 * Environment: Internal and External
 * History: NX8.5.3
 *****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_user_attribute_locks
(
    tag_t object,                   /* <I> The object holding the attributes */
    const UF_ATTR_iterator_t *iter, /* <I> Iterator describing the attributes to be locked.
                                           The iterator is automatically reset. */
    logical locked                  /* <I> The status of the lock to be set ('true': locked or 'false': unlocked) */
);
 
/*****************************************************************************
 * Assigns an attribute to the object specified. If the attribute does not
 * exist for the specified attribute type then create the attribute;
 * otherwise, modify its existing value.
 *
 * The calling routine must call UF_MODL_update() to propagate the attribute
 * change.
 *
 * Passing an object tag will result in modifying or creating an attribute
 * on that object. Passing in a part tag will result in modifying or
 * creating a part attribute for that part.
 *
 * The part in which the object resides must be fully loaded.
 *
 * If the attribute is of type UF_ATTR_string or UF_ATTR_reference, the
 * maximum length of its value is limited by UF_ATTR_MAX_STRING_BUFSIZE.
 *
 * If the attribute is of type UF_ATTR_time, then the value is assumed to be
 * in the current timezone of the machine running the program. 
 * The value, when stored in NX, is converted from that timezone to UTC.
 * The valid range for attributes of type UF_ATTR_time is from 01-Jan-1970 to 31-Dec-2105.
 *
 * Environment: Internal  and  External
 * See Also : 
 *
 * Discouraged in new applications
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_assign(
tag_t object ,/* <I>
              Part tag or part attribute tag.
              */
char * title ,/* <I>
              Attribute  Title (maximum character length is UF_ATTR_MAX_TITLE_BUFSIZE)
              */
UF_ATTR_value_t value  /* <I>
                       Typed Attribute Value
                       */
);

/*****************************************************************************
 * Sets the lock status of an attribute on the object specified. If the attribute does not
 * exist for the specified attribute type then an error is returned.
 *
 * Passing an object tag will result in modifying an attribute
 * on that object. Passing in a part tag will result in modifying
 * a part attribute for that part.
 *
 * The part in which the object resides must be fully loaded.
 *
 * Unlocking a locked attribute requires access via a Customer Default setting
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 * See Also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_set_locked(
tag_t object ,/* <I>
              Part tag or part attribute tag.
              */
char * title ,/* <I>
              Attribute  Title (maximum character length is UF_ATTR_MAX_TITLE_BUFSIZE)
              */
logical locked  /* <I>
             The new locked status
             */
);

/*****************************************************************************
 * Gets the lock status of an attribute on the object specified. If the attribute does not
 * exist for the specified attribute type then an error is returned.
 *
 * Passing an object tag will result in querying an attribute
 * on that object. Passing in a part tag will result in querying
 * a part attribute for that part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 * See Also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_ask_locked(
tag_t object ,/* <I>
              Part tag or part attribute tag.
              */
char * title ,/* <I>
              Attribute  Title (maximum character length is UF_ATTR_MAX_TITLE_BUFSIZE)
              */
logical *locked  /* <O>
             The attribute's locked status
             */
);

/*****************************************************************************
 * Deletes the attribute of the specified type from the object. If the type
 * is UF_ATTR_any (or 6), then this function will delete all attributes with
 * the given title.
 *
 * The calling routine must call UF_MODL_update() to propagate the attribute
 * change.
 *
 * The part in which the object resides must be fully loaded.
 *
 * Passing in an object tag will result in deleting the attribute from that
 * object.  Passing in a part tag will result in deleting a part attribute from
 * that part.  Attributes that are inherited will not be deleted (and no error
 * message will be returned).  To delete an inherited attribute, the object that 
 * owns that attribute must be passed into the function.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 * See Also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_delete(
tag_t object ,/* <I>
            Part tag or part attribute tag.
            */
int type ,/* <I>
          Attribute  Type:
            UF_ATTR_bool
            UF_ATTR_integer
            UF_ATTR_real,
            UF_ATTR_time
            UF_ATTR_null,
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
          */
char * title  /* <I>
              Attribute Title (maximum character length is
              UF_ATTR_MAX_TITLE_BUFSIZE)
              */
);


/*****************************************************************************
 * Deletes all attributes of the specified type from the object. If the type
 * is UF_ATTR_any (or 6) then this function removes all attributes from the
 * object.
 *
 * The calling routine must call UF_MODL_update() to propagate the attribute
 * change.
 *
 * The part in which the object resides must be fully loaded.
 *
 * Passing in an object tag will result in deleting attributes from that
 * object.  Passing in a part tag will result in deleting part attributes from
 * that part.  Attributes that are inherited will not be deleted (and no error
 * message will be returned).  To delete an inherited attribute, the object that 
 * owns that attribute must be passed into the function.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 * See Also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_delete_all(
tag_t object ,/* <I>
              Part tag or part attribute tag.
              */
int type  /* <I>
          Attribute  Type:
            UF_ATTR_bool
            UF_ATTR_integer
            UF_ATTR_real,
            UF_ATTR_time
            UF_ATTR_null,
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
          */
);

/*****************************************************************************
 * Cycle through all the object's attributes of the specified type,
 * returning the title and value of the next attribute. 
 *
 * If the type specified is UF_ATTR_any (or 6) then cycle through all the 
 * attributes of the object.
 *
 * NOTE: Callers should not rely on attributes being returned in any
 *       particular order.
 *
 * If there are no more attributes to cycle then
 * a zero will be returned as the cycle status(indx).
 *
 * Passing an object tag will result in cycling the attributes of that object.
 * Passing in a part tag will result in cycling the part attributes of that
 * part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 * See Also:  Sample program ufx_cycle_internal.c
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_cycle(
tag_t object ,/* <I>
              Part tag or object tag.
              */
int * indx ,/* <I/O>
            Cycle Status:(input)
               0 = Begin Cycling
            Cycle Status:(output)
               0 = Done Cycling or No Attribute Returned
               1 = Next Attribute Returned
            */
int type ,/* <I>
          Attribute Type to Cycle:
             UF_ATTR_bool
             UF_ATTR_integer
             UF_ATTR_real,
             UF_ATTR_time
             UF_ATTR_null,
             UF_ATTR_string
             UF_ATTR_any
             UF_ATTR_reference
          */
char  title[ UF_ATTR_MAX_TITLE_BUFSIZE ] ,/* <O>
                 Attribute Title (maximum character length is
                 UF_ATTR_MAX_TITLE_BUFSIZE)
              */
UF_ATTR_value_p_t value /* <I/O>
                     Typed Attribute Value:(Input)
                         If type is UF_ATTR_string then
                         value->value.string must point to the character
                         array where the string value will be returned.
                         If type is UF_ATTR_reference then
                         value->value.reference must point to the
                         character array where the string value will be
                         returned.
                     Typed Attribute Value:(Output)
                         If type is UF_ATTR_any and the returned
                         value->type is UF_ATTR_string or
                         UF_ATTR_reference then the string returned
                         was dynamically allocated and you must use
                         UF_free to deallocate the memory.
                         If the returned value->type is UF_ATTR_time, then
                         the value will be in the current time zone of the 
                         machine on which the program is being executed.
                    */
);

/*****************************************************************************
 * Read the value of the attribute of the given type with the specified
 * title. If the attribute's type is UF_ATTR_any (or 6) then return the
 * value of the first attribute found with the given title.
 *
 * NOTE: Callers should not rely on attributes being returned in any
 *       particular order.
 * UF_ATTR_bool (8)
 *
 * If no attribute was found then a zero will be returned as the attribute's
 * type.  Passing an object tag will result in reading a value from the
 * attributes of that object. Passing in a part tag will result in reading a
 * value from the part attribute of that part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 * See Also :  
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_read_value(
tag_t object ,/* <I>
              Part tag or object tag.
              */
char * title ,/* <I>
              Attribute Title (maximum character length is
              UF_ATTR_MAX_TITLE_BUFSIZE)
              */
int type ,/* <I>
          Attribute Type to Search:
            UF_ATTR_bool
            UF_ATTR_integer
            UF_ATTR_real
            UF_ATTR_time
            UF_ATTR_null
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
          */
UF_ATTR_value_p_t value /* <IOF>
                         Typed Attribute Value:
                            If "type" is UF_ATTR_string then
                            "value->value.string" must either be NULL or
                            point to a character buffer of size
                            UF_ATTR_MAX_STRING_BUFSIZE.  If the value is
                            NULL, then the returned buffer will be allocated,
                            and the user is responsible for freeing it
                            by calling UF_free().

                            If "type" is UF_ATTR_reference then
                            "value->value.string" must either be NULL or
                            point to a character buffer of size
                            UF_ATTR_MAX_STRING_BUFSIZE.  If the value is
                            NULL, then the returned buffer will be allocated,
                            and the user is responsible for freeing it
                            by calling UF_free().

                            If "value->type" = 0, then the attribute does not
                            exist for the type searched.

                            If "type" is UF_ATTR_any and the returned
                            "value->type" is UF_ATTR_string or
                            UF_ATTR_reference, then the string returned
                            was dynamically allocated and you must use
                            UF_free to deallocate the memory.

                            If "value->type" is UF_ATTR_time, then
                            the value will be in the current time zone of the 
                            machine on which the program is being executed.
                         */
);

/*****************************************************************************
 * Read the reference string of the given attribute, which must be of reference type.
 *
 * If no attribute was found then a zero will be returned as the attribute's
 * type.  Passing an object tag will result in reading a value from the
 * attributes of that object. Passing in a part tag will result in reading a
 * value from the part attribute of that part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_read_reference_string(
tag_t object ,/* <I>
              Part tag or object tag.
              */
char * title ,/* <I>
              Attribute Title (maximum character length is
              UF_ATTR_MAX_TITLE_BUFSIZE)
              */
UF_ATTR_value_p_t reference_string /* <IOF>
                         Typed Attribute Value:
                            "value->value.reference" must either be NULL or
                            point to a character buffer of size
                            UF_ATTR_MAX_STRING_BUFSIZE.  If the value is
                            NULL, then the returned buffer will be allocated,
                            and the user is responsible for freeing it
                            by calling UF_free().
                         */
);

/*****************************************************************************
 * Count the number of attributes of the specified type that belong to the
 * object. If the attribute type specified is UF_ATTR_any then return
 * the count for all types.
 *
 * Passing an object tag will result in counting the attributes of
 * that object. Passing in a part tag will result in counting the
 * part attributes of that part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 * See Also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_count_attributes(
tag_t object ,/* <I>
              Part tag or object tag.
              */
int type ,/* <I>
          Attribute Type:
            UF_ATTR_bool
            UF_ATTR_integer
            UF_ATTR_real
            UF_ATTR_time
            UF_ATTR_null
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
          */
int * count  /* <O>
             Attribute Count
             */
);

/*****************************************************************************
 * Searches the specified attribute type for the attribute title. If the type
 * specified is UF_ATTR_any (or 6) then return the first attribute found with
 * the given title. 
 *
 * NOTE: Callers should not rely on attributes being returned in any
 *       particular order.
 *
 * UF_ATTR_bool(8)
 * If the attribute was found then the title_type parameter returns its
 * attribute type; otherwise, a zero is returned.
 *
 * Passing an object tag will result in finding the attributes of
 * that object. Passing in a part tag will result in finding the
 * part attributes of that part.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 * See Also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_find_attribute(
tag_t object ,/* <I>
              Part tag or object tag.
              */
int type ,/* <I>
          Attribute Type:
            UF_ATTR_integer
            UF_ATTR_real,
            UF_ATTR_time
            UF_ATTR_null,
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
            UF_ATTR_bool
          */
char * title ,/* <I>
              Attribute Title (maximum character length is
              UF_ATTR_MAX_TITLE_BUFSIZE)
              */
int * title_type  /* <O>
                  Type of Attribute Found:
                      0 = Attribute Not Found.
                      UF_ATTR_integer
                      UF_ATTR_real
                      UF_ATTR_time
                      UF_ATTR_null
                      UF_ATTR_reference
                      UF_ATTR_string
                      UF_ATTR_bool
                  */
);

/*****************************************************************************
 * Find the part attribute object for the work part.  Once the part attribute
 * object identifier is obtained, it may be used as
 * input to other routines that handle user defined attributes.
 * Each part has one and only one part attribute object.
 *
 * NOTE: This function is no longer needed for any of the UF_ATTR functions, new and old.
 *       Instead, the part tag may be used when reading and writing part attributes.
 *
 * Discouraged in new applications
 * Environment: Internal  and  External
 * See Also:
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_ask_part_attribute(
tag_t * attribute  /* <O>
                   Object Identifier of part attribute of the work part
                   */
);

/*****************************************************************************
 * Reads all the part attributes from a part file without requiring that the
 * part be opened. The values returned are always those stored on disk
 * even if the part is currently loaded in memory (use
 * UF_ATTR_ask_part_attrs for such a part). This routine is normally
 * considerably more efficient than opening the part and finding the part
 * attribute.
 *
 * Environment: Internal and External
 * See Also:  UF_ATTR_part_attr_s
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_ask_part_attrs_in_file(
const char * part_name ,/* <I>
                        Part file name to read part attributes from or
                        part name when using NX Manager (internal name).
                        */
int * n_attributes ,/* <O>
                    Count of attributes returned.
                    */
UF_ATTR_part_attr_p_t * attributes  /* <OF,len:n_attributes>
                                    Allocated array of structures holding
                                    attribute titles and values. This must
                                    be freed by the caller using UF_free.

                                    If a returned attribute type is UF_ATTR_string or
                                    UF_ATTR_reference then the string returned
                                    was dynamically allocated and you must use
                                    UF_free to deallocate the memory.

                                    If a returned attribute type is UF_ATTR_time, then
                                    the value will be in the current time zone of the 
                                    machine on which the program is being executed.
                                    */
);

/*****************************************************************************
 * Reads all of the part attributes from the specified part. The part must
 * be loaded to use this function.
 *
 * Discouraged in new applications
 * Environment: Internal and External
 * See Also:  UF_ATTR_part_attr_s
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_ask_part_attrs(
const tag_t part_tag ,/* <I>
                      part tag of the part from which to read attributes.
                      */
int * n_attributes ,/* <O>
                    Count of attributes returned.
                    */
UF_ATTR_part_attr_p_t * attributes  /* <OF,len:n_attributes>
                                    Allocated array of structures holding
                                    attribute titles and values.  This must
                                    be freed by the caller using UF_free.
                     
                                    If a returned attribute type is UF_ATTR_string or
                                    UF_ATTR_reference then the string returned
                                    was dynamically allocated and you must use
                                    UF_free to deallocate the memory.

                                    If a returned attribute type is UF_ATTR_time, then
                                    the value will be in the current time zone of the 
                                    machine on which the program is being executed.
                                    */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#include <uf_retiring.h>

#endif /* UF_ATTR_INCLUDED */
