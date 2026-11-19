/*******************************************************************************
            Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                     Unpublished - All rights reserved
 *****************************************************************************
 *
 * 
 *
 *
 * File description:
 *
 *    This file contains documentation for the UF_LIB module. This module
 *    allows the Open API programmer to interface with the Libraries that NX
 *    uses for retrieving objects such as Machine Tools, Cutters, Tool
 *    Material and Feeds and Speeds. The programmer can perform functions
 *    such as retrieving objects into NX and asking for the values of
 *    attributes of objects in a Library.
 *
 *    The query syntax:
 *
 *    An application can create a query that contains the constraints which
 *    should be used in selecting objects in the Library. The query must be
 *    specified using the query language.  The language of a query is very
 *    simple. It is a collection of criteria which are connected to each other
 *    with certain logical operators. A criterion has the form:
 *
 *             [Attribute Name] [Relational Operator] [Expression]
 *
 *    where a(n)
 *
 *    [Attribute Name] is a NX name of one of the database attributes of the
 *                     objects being queried,
 *
 *
 *    [Relational Operator] is one of <, <=, ==, !=, >, >=, &=, &!,
 *
 *    [Expression] is an expression made up of (primarily) NX Expression
 *                 SubSystem (ESS) expressions and NX Names.
 *
 *    If the operator is &= or &! then [Expression] is an egrep style regular
 *    expression (see man pages on egrep or TCL regular expressions). We
 *    describe these expressions in more detail below.
 *
 *    The Relational Operators &=  and &! mean String Equal and String Not
 *    Equal, resp.
 *
 *    The logical operators allowed are && and || with && having
 *    precedence over ||.
 *
 *    An NX name is a non database-specific name for an attribute of an object
 *    that is stored in a library. (These names are defined in the Definition
 *    File of the DBC object used for the query.) For example, a query might
 *    use Tool_Diameter to specify the diameter of the tool, whereas, Genius
 *    may use a UNCT of -1001 to denote the tool diameter. In this case
 *    Tool_Diameter is the NX Name.
 *
 *    The query language places very few restrictions on the form of an
 *    [Expression].
 *    The restrictions are:
 *
 *    1) each occurrence of an NX ESS expression must be surrounded by
 *       delimiters and,
 *
 *    2) each occurrence of an NX name must be surrounded by delimiters.
 *       (The delimiters are also defined in the Definition File of the DBC
 *       object used for the query.)
 *
 *    3) the entire [Expression] must be a valid TCL expression.
 *
 *    In the following examples of QRY queries, we use DB( and ) as the NX Name
 *    start and end delimiters, resp., and ESS( and ) as the ESS start and end
 *    delimiters, resp. These are user-defined via the DBC Definition File
 *
 *    Here are 2 examples of QRY queries:
 *
 *    [DB(Tool_Diameter)] >= [0.25] && [DB(Tool_Diameter)] <= [0.50]
 *
 *    [DB(Tool_Diameter)] < [2 * ESS(Corner_Radius)] &&
 *    [DB(Num_Of_Flutes)] == [3 * ESS(Height)] && [DB(Material)] &=
 *    ["^STEEL[123]$"] && [DB(Catalog)] &! ["^.*VENDOR_A.*$"]
 *
 ******************************************************************************/
#ifndef UF_LIB_H_INCLUDED
#define UF_LIB_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_cam.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


/***************************** Public Typedefs ********************************/

/* This data type is the result of a query. The elements of this type may be
 * queried with UF_LIB_ask_record_in_rset() and UF_LIB_ask_rset_map().
 */
typedef void   *UF_RSET_t;

/************************* Public Function Definitions ************************/


/*****************************************************************************
 * This function will execute a query in a library and return a count of the
 * number of objects in the library that satisfy the query. See the above
 * File Description for a discussion of the query syntax. The Class Query in
 * the Definition File is &&ed to the query specified here as a parameter.
 *
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_execute_query_for_count
(
   UF_CAM_db_object_t  db,    /* <I> - the library object in which to
                                     execute the query */
   const char     *cls_name,  /* <I> - the class name */
   const char     *query, /* <I> - the query */
   int            *count  /* <O> - the number of objects in the library that
                           *     satisfy the query.
                           */
);

/*****************************************************************************
 * This function returns the number of records that the specified UF_RSET_t
 * contains.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V17.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_ask_rset_count
(
   UF_RSET_t   rset,    /* <I> - the UF_RSET_t whose record count is desired */
   int        *count    /* <O> - the number of records in the UF_RSET_t */
);

/*****************************************************************************
 * This function will execute a query in a library and return a record set
 * containing the objects in the library that satisfy the query.
 * See the above File Description for a discussion of the query syntax. The
 * Class Query in the Definition File is &&ed to the query specified here as
 * a parameter. The contents of the RSET returned is determined by the
 * RSET definition for the specified class name. This definition is found in the
 * Definition File.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_execute_query
(
   UF_CAM_db_object_t   db,    /* <I> - the library object in which to
                                      execute the query. */
   const char     *cls_name,  /* <I> - the class name */
   const char     *query, /* <I> - the query */
   int            *count, /* <O> - the number of objects satisfying the query */
   UF_RSET_t      *rset   /* <O> - the record of objects that satisfy
                                   the query */
);


/*****************************************************************************
 * This function provides a description (or map) of the contents of a record
 * set. It provides a list of the attributes that each record in the record
 * set has as well as the type of each of those attributes. One can think of
 * a record set as a table. The rows of the table are the individual records
 * in the record set. The columns headings are the attributes that are found
 * in the record set.
 *
 * E.g.:
 *
 *       libref   Tool Name  Diameter  Material
 *       --------------------------------------
 *       ref1     Drill       3.5      Steel
 *       ref2     Mill        1.3      Alloy
 *
 * In this record set the attributes are:
 *                  libref, Tool Name, Diameter and  Material and
 * the types are:   s,      s,         d,            s.
 *
 * The type characters are:  s == string
 *                           i == integer
 *                           d == double
 *
 *
 ****************************************************************************/

/*****************************************************************************
 * This function provides a description (or map) of the contents of a record
 * set. It provides a list of the attributes that each record in the record
 * set has as well as the type of each of those attributes. One can think of
 * a record set as a table. The rows of the table are the individual records
 * in the record set. The columns headings are the attributes that are found
 * in the record set.
 * NOTE: Use UF_LIB_free_rset_map to free returned memory
 * 
 * Environment : Internal  and  External
 * See Also:  UF_LIB_free_rset_map
 * History : Released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_ask_rset_map
(
   UF_RSET_t       rset,       /* <I> - the record set of interest. This was
                                *     returned by execute_query.
                                */
   int            *count,      /* <O> - the number of attributes in the record
                                *     set.
                                */
   const char   ***attr_names, /* <OF,len:count> count - the name of the attributes in the
                                         record set.
                                */
   const char    **attr_types  /* <OF,len:count> count - the types of the attributes. The ith
                                *      attr_types is the type of the ith
                                *      attr_names.
                                */
);


/*****************************************************************************
 * This function frees the memory returned from UF_LIB_ask_rset_map
 *
 * Environment : Internal  and  External
 * See Also:  UF_LIB_ask_rset_map
 * History : Released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_free_rset_map
(
   int   count,  /* <I> - the number of attributes in the record set. */
   const char   **attr_names, /* <I,len:count> - the name of the attributes in the record
                               *     set. */
   const char    *attr_types  /* <I> - the types of the attributes. The ith
                               *     attr_types is the type of the ith
                               *     attr_names. */
);


/*****************************************************************************
 * This function provides a record from a record set. The record is returned
 * as an array of strings. Each element of the array is the value of an
 * attribute of the specified record. The ith element of the array is the
 * value of the ith attribute returned from ask_rset_map. Note that all values
 * are returned as strings. If the value has type double or int the caller
 * will need to convert as required by the application.
 *
 * The caller should use UF_free_string_array to free these returned arrays.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_ask_record_in_rset
(
   UF_RSET_t       rset,       /* <I> - the desired record set */
   int             record_num, /* <I> - the desired record number (0 based) */
   int            *count,      /* <O> - the number of values of attributes */
   const char   ***values      /* <OF,len:count> - the values of the attributes.  The
                                         caller should call UF_free_string_array
                                         to free this array. */
);

/*****************************************************************************
 * This function sorts the contents of a record set. The sort key is of the
 * form:
 *
 *       db_alias1/{a|d},db_alias2/{a|d},...,db_aliasN/{a|d}
 *
 * where a = ascending, d = descending. For example, if Diameter and Cost are
 * both DB Aliases that are found in the record set one could sort the set
 * primarily by Diameter in ascending order and then, within Diameter, sort by
 * Cost in decreasing order with a sort key of:
 *
 *                        Diameter/a,Cost/d
 *
 * Here Diameter is the primary key. Records of the set that have the same
 * Diameter are then sorted by Cost. The original record set is not changed.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V17.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_sort_rset
(
   UF_RSET_t   rset,       /* <I> - the record set to sort */
   const char *sort_key,   /* <I> - the sort key to sort by */
   UF_RSET_t  *sorted_rset /* <O> - the sorted record set */
);

/*****************************************************************************
 * This function merges the contents of two record sets. The merged record set
 * contains the records of 'rset1' followed by the records of 'rset2'. The
 * records appear in the same order they did in their original record sets.
 * 'rset1' and 'rset2' are unchanged.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V17.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_merge_rsets
(
   UF_RSET_t   rset1,      /* <I> - the record set to merge */
   UF_RSET_t   rset2,      /* <I> - the other record to merge */
   UF_RSET_t  *merged_rset /* <O> - the merged record set */
);

/*****************************************************************************
 * This function deletes the specified UF_RSET_t.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V17.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_delete_rset
(
   UF_RSET_t   rset      /* <I> - the record set to delete */
);

/*****************************************************************************
 * This function provides the library reference (or libref) of the specified
 * NX object. The libref is an attribute which is returned for every record
 * in every record set. It is also the attribute which is used to retrieve
 * an object from a library. An NX object will only have a libref if it was
 * created by being retrieved from a library.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_ask_libref
(
   tag_t          ug_object,   /* <I> - the desired NX object */
   const char   **libref       /* <OF> - the libref of the specified object */
);


/*****************************************************************************
 * This function provides a list of attribute values of an NX object that
 * was previously retrieved from a library. The library is referenced by the
 * specified UF_CAM_db_object_t. The values are the current values (in the
 * library) of the specified attributes of the NX object.
 *
 * The caller should use UF_free_string_array to free these returned arrays.
 *
 * Environment : Internal  and  External
 * See Also:
 * History : Released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_LIB_ask_lib_attribute_values
(
   UF_CAM_db_object_t   db,        /* <I> - the db object to query in */
   tag_t                ug_object, /* <I> - the NX object to query about */
   int                  count,     /* <I> - the number of attribute to ask their
                                    *     values of */
   const  char        **db_alias,  /* <I,len:count> - the list of attribute db aliases to
                                    *     ask the values of */
   char              ***values     /* <OF,len:count> - the requested values.  This is
                                         an array of strings that must be freed
                                         by calling UF_free_string_array. */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_LIB_H_INCLUDED */
