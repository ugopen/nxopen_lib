/****************************************************************************

           Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                         Unpublished - All rights reserved

===========================================================================

 

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

Part Attribute Object Identifier

To obtain the object identifier for a part attribute to pass to other routines
please use UF_ATTR_ask_part_attribute. The following routines accept both a
part attribute tag or a part tag. If you pass in a part tag these routines find
the part attribute tag automatically:
     .  UF_ATTR_assign
     .  UF_ATTR_delete
     .  UF_ATTR_delete_all
     .  UF_ATTR_cycle
     .  UF_ATTR_read_value
     .  UF_ATTR_count_attributes
     .  UF_ATTR_find_attribute

NX Computational Date & Time Format

NX computational date and time is stored in an integer array consisting of two
elements. The first array element contains the NX Computational Date, while
the second contains the NX Computational Time.

NX Computational Time stores the number of six second intervals since midnight,
that is it is incremented every six seconds.  The computation is:

  NX_computations_time = 10* (60*Hour+Minute) + Second/6

where Hour = Hour of day on 24 hour clock and Minute = Minute of hour, and
Second is the Seconds of the minute.



 */

#ifndef UF_ATTR_INCLUDED
#define UF_ATTR_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif



/***************************************************************************
           C O N S T A N T   &   T Y P E   D E F I N I T I O N S
*****************************************************************************/

/*
 * Maximum attribute string value and title length
 */
#define UF_ATTR_MAX_STRING_LEN 132
#define UF_ATTR_MAX_TITLE_LEN   50

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

/*****************************************************************************
 * Attribute value
 ****************************************************************************/
union UF_ATTR_value_u
{
    int    integer;    /* If the attribute is an integer attribute,
                          this can be used to access the value. */
    double real;       /* If the attribute is a floating point attribute,
                          this can be used to access the value. */
    int    time[2];    /* If the attribute is a date/time attribute,
                          this can be used to access the value.
                          time[0] contains the NX computational date
                          time[1] contains the NX computational time. */
    char   *string;    /* If the attribute is a string attribute, then
                          this is a pointer to the value. The maximum length
                          of this string is limited by UF_ATTR_MAX_STRING_LEN */

    char   *reference; /* If the attribute is a reference attribute, then
                          this is a pointer to the value.  The value may
                          have an embedded expression with the following
                          syntax:
                              <Xm.n@exp_name> or <Xm,n@exp_name>
                          The X indicates that an expression is being
                          referenced.  The m specifies the minimum field
                          width.  If necessary, it is padded on the left to
                          make up the field width.  The n specifies the
                          maximum number of digits after the decimal point of
                          the expression value.  The decimal point can be
                          specified as either . or , thus either m.n or m,n
                          are acceptable.  */
} ;

typedef union UF_ATTR_value_u UF_ATTR_value_u_t, *UF_ATTR_value_u_p_t;
/*****************************************************************************
 * Typed attribute value
 ****************************************************************************/
struct UF_ATTR_value_s
{
    int type;                 /* The type of the attribute.  Valid types are:
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
    char      title[UF_ATTR_MAX_TITLE_LEN+1];  /* <len:UF_ATTR_MAX_TITLE_LEN+1>The title of the attribute */
    UF_ATTR_value_t value;                     /* The value for the part
                                                  attribute */
    char      string_value[UF_ATTR_MAX_STRING_LEN+1]; /*<len:UF_ATTR_MAX_STRING_LEN+1> Buffer for the part
                                                         attribute string value.
                                                         The character pointer
                                                         .value.value.string
                                                         will point to this
                                                         buffer. */
};

typedef struct UF_ATTR_part_attr_s UF_ATTR_part_attr_t, *UF_ATTR_part_attr_p_t;

/***************************************************************************
            P R O T O T Y P E    D E F I N I T I O N S
*****************************************************************************/

/*****************************************************************************
 * Assigns an attribute to the object specified. If the attribute does not
 * exist for the specified attribute type then create the attribute;
 * otherwise, modify its existing value.
 *
 * Passing an object tag will result in modifying or creating an attribute
 * on that object. Passing in a part tag will result in modifying or
 * creating a part attribute for that part.
 *
 * NOTE: Only part attributes of type UF_ATTR_string are supported. All
 * other data types are unsupported for part attributes.
 *
 * If the attribute is of type UF_ATTR_string or UF_ATTR_reference, the
 * maximum length of its value is limited by UF_ATTR_MAX_STRING_LEN.
 *
 * Environment: Internal  and  External
 * See Also : 
 * History:
 ****************************************************************************/
extern UFUNEXPORT int UF_ATTR_assign(
tag_t object ,/* <I>
              Part tag or part attribute tag.
              */
char * title ,/* <I>
              Attribute  Title (maximum character length is UF_ATTR_MAX_TITLE_LEN+1)
              */
UF_ATTR_value_t value  /* <I>
                       Typed Attribute Value
                       */
);

/*****************************************************************************
 * Deletes the attribute of the specified type from the object. If the type
 * is UF_ATTR_any (or 6), then this function will delete all attributes with
 * the given title.
 *
 * Passing in an object tag will result in deleting the attribute from that
 * object.  Passing in a part tag will result in deleting a part attribute from
 * that part.  Attributes that are inherited will not be deleted (and no error
 * message will be returned).  To delete an inherited attribute, the object that 
 * owns that attribute must be passed into the function.
 *
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
              UF_ATTR_MAX_TITLE_LEN+1)
              */
);


/*****************************************************************************
 * Deletes all attributes of the specified type from the object. If the type
 * is UF_ATTR_any (or 6) then this function removes all attributes from the
 * object.
 *
 * Passing in an object tag will result in deleting attributes from that
 * object.  Passing in a part tag will result in deleting part attributes from
 * that part.  Attributes that are inherited will not be deleted (and no error
 * message will be returned).  To delete an inherited attribute, the object that 
 * owns that attribute must be passed into the function.
 *
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
             UF_ATTR_integer
             UF_ATTR_real,
             UF_ATTR_time
             UF_ATTR_null,
             UF_ATTR_string
             UF_ATTR_any
             UF_ATTR_reference
          */
char * title ,/* <O>
                 Attribute Title (maximum character length is
                 UF_ATTR_MAX_TITLE_LEN+1)
              */
UF_ATTR_value_p_t value /* <I/O>
                     Typed Attribute Value:(Input)
                         If type is UF_ATTR_string then
                         value.value.string must point to the character
                         array where the string value will be returned.
                         If type is UF_ATTR_reference then
                         value.value.reference must point to the
                         character array where the string value will be
                         returned.
                     Typed Attribute Value:(Output)
                         If type is UF_ATTR_any and the returned
                         value.type is UF_ATTR_string or
                         UF_ATTR_reference then the string returned
                         was dynamically allocated and you must use
                         UF_free to deallocate the memory.
                    */
);
/*****************************************************************************
 * Read the value of the attribute of the given type with the specified
 * title. If the attribute's type is UF_ATTR_any (or 6) then return the
 * value of the first attribute found with the given title.
 *
 * NOTE: Callers should not rely on attributes being returned in any
 *       particular order.
 *
 * If no attribute was found then a zero will be returned as the attribute's
 * type.  Passing an object tag will result in reading a value from the
 * attributes of that object. Passing in a part tag will result in reading a
 * value from the part attribute of that part.
 *
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
              UF_ATTR_MAX_TITLE_LEN+1)
              */
int type ,/* <I>
          Attribute Type to Search:
            UF_ATTR_integer
            UF_ATTR_real,
            UF_ATTR_time
            UF_ATTR_null,
            UF_ATTR_string
            UF_ATTR_any
            UF_ATTR_reference
          */
UF_ATTR_value_p_t value /* <IOF>
                         Typed Attribute Value:
                            If "type" is UF_ATTR_string then
                            "value->value.string" must either be NULL or
                            point to a character buffer of size
                            UF_ATTR_MAX_STRING_LEN + 1.  If the value is
                            NULL, then the returned buffer will be allocated,
                            and the user is responsible for freeing it
                            by calling UF_free().
                            If "type" is UF_ATTR_reference then
                            "value->value.string" must either be NULL or
                            point to a character buffer of size
                            UF_ATTR_MAX_STRING_LEN + 1.  If the value is
                            NULL, then the returned buffer will be allocated,
                            and the user is responsible for freeing it
                            by calling UF_free().
                         Typed Attribute Value:
                            If "value.type" = 0, then the attribute does not
                            exist for the type searched.
                            If "type" is UF_ATTR_any and the returned
                            "value.type" is UF_ATTR_string or
                            UF_ATTR_reference, then the string returned
                            was dynamically allocated and you must use
                            UF_free to deallocate the memory.
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
            UF_ATTR_integer
            UF_ATTR_real,
            UF_ATTR_time
            UF_ATTR_null,
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
 * If the attribute was found then the title_type parameter returns its
 * attribute type; otherwise, a zero is returned.
 *
 * Passing an object tag will result in finding the attributes of
 * that object. Passing in a part tag will result in finding the
 * part attributes of that part.
 *
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
          */
char * title ,/* <I>
              Attribute Title (maximum character length is
              UF_ATTR_MAX_TITLE_LEN+1)
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
                  */
);

/*****************************************************************************
 * Find the part attribute object for the work part.  Once the part attribute
 * object identifier is obtained, it may be used as
 * input to other routines that handle user defined attributes.
 * Each part has one and only one part attribute object.
 *
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
                                    */
);

/*****************************************************************************
 * Reads all of the part attributes from the specified part. The part must
 * be loaded to use this function.
 *
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
                                    */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#include <uf_retiring.h>

#endif /* UF_ATTR_INCLUDED */
