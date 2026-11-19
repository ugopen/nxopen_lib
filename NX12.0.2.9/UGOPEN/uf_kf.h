/***************************************************************************************************

    Copyright 2008 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.

====================================================================================================



File description:

    API to get data from and to Knowledge Fusion

    The functions declared in this file provide the interface to allow the user to define
    his or her own NX Knowledge Fusion function that will execute calls from NX Knowledge Fusion when
    invoked, and execute the user defined functions.

    Please refer to the section of Calling UFs from NX Knowledge Fusion in
    NX Knowledge Fusion End User Guide.
***************************************************************************************************/

#ifndef UF_KF_H_INCLUDED
#define UF_KF_H_INCLUDED

#include <uf_defs.h>
#include <uf_retiring.h>

#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/**************************************************
 *   Data types for Open API                      *
 **************************************************/

/*

*/

typedef enum
{
    UF_KF_null = 0,
    UF_KF_error_type,
    UF_KF_any,
    UF_KF_boolean,
    UF_KF_defeval,
    UF_KF_frame,            /* A UF_MTX4 transformation matrix.  All the UF_MTX4 functions apply. */
    UF_KF_tag,              /* This is hostpointer, not NX tag. */
    UF_KF_integer,
    UF_KF_list,
    UF_KF_marker,
    UF_KF_name,
    UF_KF_no_value,
    UF_KF_number,
    UF_KF_instance,
    UF_KF_point,
    UF_KF_string,
    UF_KF_vector,
    UF_KF_user

}UF_KF_type_t;

typedef enum
{
    UF_KF_ASK_USER_ONLY = 0,
    UF_KF_ASK_SYSTEM_ONLY,
    UF_KF_ASK_ALL
}UF_KF_class_type_t;

/*

*/

typedef void *UF_KF_value_t;    /* Obsolete in v19 - Use UF_KF_value_p_t    */
typedef void *UF_KF_instance_t; /* Obsolete in v19 - Use UF_KF_instance_p_t */
typedef void *UF_KF_list_t;     /* Obsolete in v19 - Use UF_KF_list_p_t     */

typedef void *UF_KF_value_p_t;
typedef void *UF_KF_instance_p_t;
typedef void *UF_KF_list_p_t;

typedef void ( UF_KF_routine_t ) ( UF_KF_value_p_t *data, int num, UF_KF_value_p_t *rv );

typedef UF_KF_routine_t *UF_KF_routine_p_t;

typedef void *UF_KF_rule_p_t;

/****************************************************************************
Create a Knowledge Fusion Boolean value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_boolean
(
    logical          data, /* <I>  Data of value */
    UF_KF_value_p_t *value /* <OF,free:UF_KF_free_rule_value> Knowledge Fusion value.
                                   Free with UF_KF_free_rule_value.
                                   Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion Name value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V18
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_name
(
    int              data, /* <I>  Data of value */
    UF_KF_value_p_t *value /* <OF> Knowledge Fusion value.
                                   Free with UF_KF_free_rule_value.
                                   Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion Integer value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_integer
(
    int              data, /* <I>  Data of value */
    UF_KF_value_p_t *value /* <OF> Knowledge Fusion value.
                                   Free with UF_KF_free_rule_value.
                                   Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion Number value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_number
(
    double           data, /* <I>  Data of value */
    UF_KF_value_p_t *value /* <OF> Knowledge Fusion value.
                                   Free with UF_KF_free_rule_value.
                                   Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion Point value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_point
(
    double           data [ 3 ], /* <I>  Data of value */
    UF_KF_value_p_t *value       /* <OF> Knowledge Fusion value.
                                         Free with UF_KF_free_rule_value.
                                         Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion Vector value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_vector
(
    double           data [ 3 ], /* <I>  Data of value */
    UF_KF_value_p_t *value       /* <OF> Knowledge Fusion value.
                                         Free with UF_KF_free_rule_value.
                                         Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion Frame value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V18
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_frame
(
    double           data [ 16 ], /* <I>  Data of value.
                                          A UF_MTX4 transformation matrix.
                                          All the UF_MTX4 functions apply. */
    UF_KF_value_p_t *value        /* <OF> Knowledge Fusion value.
                                          Free with UF_KF_free_rule_value.
                                          Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion Hostpointer value. This is a way to reference an
NX object without adopting it to Knowledge Fusion.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_tag
(
    tag_t            data, /* <I>  Data of value */
    UF_KF_value_p_t *value /* <OF> Knowledge Fusion value.
                                   Free with UF_KF_free_rule_value.
                                   Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion User value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V18
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_user
(
    void            *data, /* <I>  Data of value */
    UF_KF_value_p_t *value /* <OF> Knowledge Fusion value.
                                   Free with UF_KF_free_rule_value.
                                   Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion String value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_string
(
    const char      *data, /* <I>  Data of value */
    UF_KF_value_p_t *value /* <OF> Knowledge Fusion value.
                                   Free with UF_KF_free_rule_value.
                                   Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion instance value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_instance
(
    UF_KF_instance_p_t  data, /* <I>  Data of value */
    UF_KF_value_p_t    *value /* <OF> Knowledge Fusion value.
                                      Free with UF_KF_free_rule_value.
                                      Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion Error value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_error
(
    int              data, /* <I>  Data of value */
    UF_KF_value_p_t *value /* <OF> Knowledge Fusion value.
                                   Free with UF_KF_free_rule_value.
                                   Do not free if being returned from a CFunc. */
);

/****************************************************************************
Create a Knowledge Fusion List value.

The input to create a list is a Knowledge Fusion value
which can be created using the following routines:
UF_KF_make_string,
UF_KF_make_tag,
UF_KF_make_vector,
UF_KF_make_point ...

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_make_list
(
    UF_KF_list_p_t   data, /* <I>  Data of value */
    UF_KF_value_p_t *value /* <OF> Knowledge Fusion value.
                                   Free with UF_KF_free_rule_value. */
);

/****************************************************************************
Get the next element from the list. This routine will return the next list
element, it will not remove the pop element from the list.  You must remember
to free the head of the list since pop moves down the list to the tail.

    UF_KF_ask_list ( list_value, &list );     // Get list
    next = list;                              // Save next element
    UF_KF_list_pop ( next, &value1, &next );  // Get value from list
    UF_KF_list_pop ( next, &value2, &next );  // Get value from list
    UF_KF_free_list_object_contents ( list ); // Free list when finished
    // Use the newly created values ...
    UF_KF_free_rule_value ( value1 );         // Free value when finished
    UF_KF_free_rule_value ( value2 );         // Free value when finished

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_list_pop
(
    UF_KF_list_p_t   list,    /* <I>  Knowledge Fusion list */
    UF_KF_value_p_t *element, /* <OF> Knowledge Fusion value.
                                      Free with UF_KF_free_rule_value. */
    UF_KF_list_p_t  *next     /* <O>  Next on Knowledge Fusion list */
);

/****************************************************************************
Put the element at the top of the list. This routine will return the new list
element, it will add the push element to the list.  You must remember
to free the head of the list since push moves up the list to the new head.

    UF_KF_ask_list ( list_value, &list );     // Get list
    UF_KF_list_push ( list, value1, &list );  // Add value to list
    UF_KF_list_push ( list, value2, &list );  // Add value to list
    UF_KF_free_rule_value ( value1 );         // Free value when finished
    UF_KF_free_rule_value ( value2 );         // Free value when finished
    // Use the newly created list ...
    UF_KF_free_list_object_contents ( list ); // Free list when finished

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_list_push
(
    UF_KF_list_p_t   list,    /* <I> Knowledge Fusion list. */
    UF_KF_value_p_t  element, /* <I> Knowledge Fusion value to push onto the list */
    UF_KF_list_p_t  *next     /* <O> Next on Knowledge Fusion list */
);

/****************************************************************************
Count the number of elements in a list

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also: UF_KF_ask_list_item
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_list_count
(
    UF_KF_list_p_t  list, /* <I> Knowledge Fusion list */
    int            *count /* <O> Number of elements in the list */
);

/***************************************************************************
Ask the value of an item in a list object.

Return :
    int    - Error code indicating success (0) or failure (<>0)
Environment: Internal and External
See Also: UF_KF_ask_list_count
History: Originally release in v18.0
****************************************************************************/
extern UFUNEXPORT int UF_KF_ask_list_item
(
    UF_KF_list_p_t   list,       /* <I>  Knowledge Fusion list */
    int              index,      /* <I>  Index of item in the list.
                                         (1 is the first item) */
    UF_KF_value_p_t *value       /* <OF> The value of the list item.
                                         Free with UF_KF_free_rule_value. */
);

/****************************************************************************
Get the value of a Boolean Knowledge Fusion value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_boolean
(
    UF_KF_value_p_t  value, /* <I> Knowledge Fusion value */
    logical         *data   /* <O> Data of value */
);

/****************************************************************************
Get the value of a Name Knowledge Fusion value.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V18
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_name
(
    UF_KF_value_p_t  value, /* <I> Knowledge Fusion value */
    unsigned int    *data   /* <O> Data of value */
);

/****************************************************************************
Get the value of a Integer Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_integer
(
    UF_KF_value_p_t  value, /* <I> Knowledge Fusion value */
    int             *data   /* <O> Data of value */
);

/****************************************************************************
Get the value of a Number Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_number
(
    UF_KF_value_p_t  value, /* <I> Knowledge Fusion data structure */
    double          *data   /* <O> Data of value */
);

/****************************************************************************
Get the value of a Point Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_point
(
    UF_KF_value_p_t value,     /* <I> Knowledge Fusion value */
    double          data [ 3 ] /* <O> Data of value */
);

/****************************************************************************
Get the value of a Vector Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_vector
(
     UF_KF_value_p_t value,     /* <I> Knowledge Fusion value */
     double          data [ 3 ] /* <O> Data of value */
);

/****************************************************************************
Get the value of a Frame Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V18
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_frame
(
     UF_KF_value_p_t value,      /* <I> Knowledge Fusion value */
     double          data [ 16 ] /* <O> Data of value.
                                        A UF_MTX4 transformation matrix.
                                        All the UF_MTX4 functions apply. */
);

/****************************************************************************
Get the value of a Hostpointer Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_tag
(
    UF_KF_value_p_t  value, /* <I> Knowledge Fusion value */
    tag_t           *data   /* <O> Data of value */
);

/****************************************************************************
Get the value of a User Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V18
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_user
(
    UF_KF_value_p_t   value, /* <I> Knowledge Fusion value */
    void            **data   /* <O> Data of value.  Free if necessary. */
);

/****************************************************************************
Get the value of a String Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
         Modified in NX 11 user is now responsible for freeing the returned
         string
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_string
(
    UF_KF_value_p_t   value, /* <I> Knowledge Fusion value */
    char            **string /* <OF> Value. Must be freed. */
);

/****************************************************************************
Get the value of an Error from Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_error
(
    UF_KF_value_p_t  value, /* <I> Knowledge Fusion value */
    int             *error  /* <O> Data of value */
);

/****************************************************************************
Get the value of an Instance Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_instance
(
    UF_KF_value_p_t     value,   /* <I> Knowledge Fusion value */
    UF_KF_instance_p_t *instance /* <O> Data of value */
);
/****************************************************************************
Get the value of a List Knowledge Fusion structure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_list
(
    UF_KF_value_p_t  value, /* <I>  Knowledge Fusion value */
    UF_KF_list_p_t  *list   /* <OF,free:UF_KF_free_list_object_contents> Knowledge Fusion list
                                    Free with UF_KF_free_list_object_contents. */
);


/****************************************************************************
Get the type of a Knowledge Fusion structure.

The supported types are defined in UF_KF_type_t

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_type
(
    UF_KF_value_p_t  data, /* <I> Knowledge Fusion data structure */
    UF_KF_type_t  *type  /* <O> Value type */
);


/****************************************************************************
Get the NX object from a Knowledge Fusion object

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_ug_object
(
    UF_KF_instance_p_t  instance, /* <I> Knowledge Fusion instance structure */
    tag_t            *ug_object /* <O> NX object */
);

/****************************************************************************
Get a fusion object from an NX object. Returns a NULL_TAG when the NX object
has no associated Knowledge Fusion instance object.

Note: For some Knowledge Fusion instance types the associated NX object
will be a feature not an object. For example, to get a ug_block type
Knowledge Fusion instance, you would need to pass the BLOCK feature's tag_t
not the resulting UF_solid_type/UF_solid_body_subtype object's tag_t.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_fusion_object
(
    tag_t             ug_object, /* <I> NX object */
    UF_KF_instance_p_t *instance   /* <O> Knowledge Fusion instance object */
);


/****************************************************************************
Get the name representation in KF of an input string. For example determine the
name in KF for the boolean name "Unite".

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also: UF_KF_ask_string_of_name
          UF_KF_ask_name
          UF_KF_make_name
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_name_of_string
(
    const char   *string, /* <I> Name string */
    unsigned int *name    /* <O> Knowledge Fusion name of the string */
);

/****************************************************************************
Get the string representation of a name in KF.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also: UF_KF_ask_name_of_string
          UF_KF_ask_name
          UF_KF_make_name
History: Released in V17
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_string_of_name
(
    unsigned int   name,  /* <I>  Knowledge Fusion name */
    char         **string /* <OF> Name string.
                                  Free with UF_free. */
);


/***************************************************************************
    Open API for access to NX KF.
***************************************************************************/

/****************************************************************************
This routine will verify if KF is initialized in the part and its
availablilty. If initializing KF in the part succeeds then this function will
return TRUE.

Return :
      int    - Error code indicating success (0) or failure (<>0)

Environment: Internal and External
See Also: UF_KF_init_part
History: Originally released in v18.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_initialized
(
    logical *is_initialized    /* <O> TRUE if KF is initialized and is
                                      available, else FALSE */
);

/****************************************************************************
Initialize a part class.

Return :
           Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also: UF_KF_is_initialized
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_init_part
(
    tag_t part /* <I> Tag of the part to initialize */
);

/****************************************************************************
Add a path to the search path for classes.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_add_search_library
(
    const char *path_name /* <I> Path name of directory that contains the
                                 .dfa files.  This will be added to the
                                 current search path for .dfa files. */
);

/****************************************************************************
Get the component classes of a given class.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_ancestor_classes
(
    const char   *class_name,    /* <I>  name of the class for which components
                                   are asked */
    int    *n_ancestors,   /* <O>  Number of components found in the class */
    char ***ancestor_names /* <OF,len:n_ancestors> Array of component names found in the class.
                                   Free with UF_free_string_array. */
);

/****************************************************************************
Get all the rules in a class.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_rules_of_class
(
    const char      *class_name, /* <I>  name of the class of which rules are to be found */
    int             *num_rules,  /* <O>  Number of rules found in the class */
    UF_KF_rule_p_t **rules       /* <OF,len:num_rules> Array of rules found in the class.
                                         Free with UF_free. */
);

/****************************************************************************
Create or modify a rule for a given instance.  If the rule already exists
then replace the existing rule.  The input parameters will be formatted
into an Knowledge Fusion rule as follows: "(rule_type) rule_name: rule_text;"
This routine can create/modify both child rules and attribite rules.  This
routine calls UF_MODL_update for the user.  UF_KF_create_rule_no_update()
does not.  Note that child rules can only be created on the "Root:"

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_create_rule
(
    const char *name_chain,     /* <I> Reference chain of instance, with trailing colon, where rule will
                                       be created or modified */
    const char *rule_name,      /* <I> Name of rule */
    const char *rule_type,      /* <I> Type of rule. Type names may be obtained by
                                       calling UF_KF_ask_rule_types.  This can also
                                       contain behavior flags, so "Number Parameter"
                                       is a valid rule_type, as is "Child".  If create
                                       "Child" then must be "Root:" or NULL.  Child
                                       rules can only be created on the "Root:" */
    const char *rule_text,      /* <I> Text for rule. For an instance rule, this must
                                       must be enclosed in curly braces.  For an
                                       attribute rule, just the formula */
    const char *leading_comment /* <I> Leading comment for rule. OPTIONAL-can be null.
                                       If non-null, make sure that the string is preceded by
                                       the pound sign '#' and followed by a new-line
                                       character '\n'
                                       Example: "#Leading Comment\n" */
);

/****************************************************************************
Create or modify a rule for a given instance.  If the rule already exists
then replace the existing rule.  The input parameters will be formatted
into an Knowledge Fusion rule as follows: "(rule_type) rule_name: rule_text;"
This routine can create/modify both child rules and attribute rules.  This
routine does not call UF_MODL_update so the user needs to.  Note that child
rules can only be created on the "Root:"


Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v18.01
***************************************************************************/
extern UFUNEXPORT int UF_KF_create_rule_no_update
(
    const char *name_chain,     /* <I> Reference chain of instance, with trailing colon, where rule will
                                       be created or modified */
    const char *rule_name,      /* <I> Name of rule */
    const char *rule_type,      /* <I> Type of rule. Type names may be obtained by
                                       calling UF_KF_ask_rule_types.  This can also
                                       contain behavior flags, so "Number Parameter"
                                       is a valid rule_type, as is "Child".  If create
                                       "Child" then must be "Root:" or NULL.  Child
                                       rules can only be created on the "Root:" */
    const char *rule_text,      /* <I> Text for rule. For an instance rule, this must
                                       must be enclosed in curly braces.  For a
                                       attribute rule, just the formula */
    const char *leading_comment /* <I> Leading comment for rule. OPTIONAL-can be null. */
);

/****************************************************************************
Create or modify a child rule for a given instance.  If the rule already
exists then replace the existing rule.  The input parameters will be formatted
into an Knowledge Fusion rule as follows: "(rule_type) rule_name: rule_text;"
This routine should be used only to create/edit child rules.  This
routine does not call UF_MODL_update so the user needs to.  Note that child
rules can only be created on the "Root:"


Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_create_child_rule
(
    tag_t  part_of_rule,           /* <I>  Part to create or modify rule in */
    const char  *name_chain,       /* <I>  Reference chain of instance, with trailing colon, where rule will
                                           be created or modified.  If create
                                           then must be "Root:" or NULL.  Child
                                           rules can only be created on the "Root:" */
    const char  *rule_name,        /* <I>  Name of rule. */
    const char  *child_class_name, /* <I>  Class of instance */
    int    num_parameters,         /* <I>  number of parameters in the parameter_names
                                           array */
    char **parameter_names,        /* <I,len:num_parameters> num_parameters
                                           array of names of parameters specified
                                           by the user.*/
    char **parameter_rules,        /* <I,len:num_parameters> num_parameters
                                           array of rules for the parameters whose
                                           names are in "parameter_names" above.
                                           Each rule may or may not have a trailing
                                           semicolon. */
    char **generated_name          /* <OF> name generated for the child object.
                                           Currently always returns NULL. */
);

/****************************************************************************
Delete a rule from a given class.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_delete_class_rule
(
    const char *class_name, /* <I> Class that rule is part of  */
    const char *rule_name   /* <I> Name of rule */
);

/****************************************************************************
Delete a rule from a given instance.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_delete_instance_rule
(
    const char *name_chain, /* <I> Instance that rule is part of. */
    const char *rule_name   /* <I> Name of rule */
);

/****************************************************************************
Re-read the Knowledge Fusion language description of all loaded classes from
the text files.  The filenames are not needed, as the Knowledge Fusion search
rules are used to find them.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_revert
(
    const char *class_name /* <I> If it is not NULL, it is the class_name whose
                                  design needs to reloaded. If it is NULL, all the
                                  existing classes in the system need to reload. */
);

/****************************************************************************
Get the data type of a rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_rule_type
(
    UF_KF_rule_p_t   rule,     /* <I>  Rule object*/
    char           **rule_type /* <OF> Rule type string.
                                       Free with UF_free. */
);

/****************************************************************************
Get the name of a rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_rule_name
(
    UF_KF_rule_p_t   rule,     /* <I>  Rule object */
    char           **rule_name /* <OF> Rule name string.
                                       Free with UF_free. */
);

/****************************************************************************
Check whether a rule is a child rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_child_rule
(
    UF_KF_rule_p_t  rule, /* <I> Rule object */
    logical        *child /* <O> TRUE if the rule is a child rule, else FALSE */
);

/****************************************************************************
Check whether a rule is a parameter rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_parameter_rule
(
    UF_KF_rule_p_t  rule,     /* <I> Rule object */
    logical        *parameter /* <O> TRUE if the rule is a parameter rule,
                                     else FALSE */
);

/****************************************************************************
Check whether a rule is a canonical rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_canonical_rule
(
    UF_KF_rule_p_t  rule,     /* <I> Rule object */
    logical        *canonical /* <O> TRUE if the rule is a canonical rule,
                                     else FALSE */
);

/****************************************************************************
Check whether a rule is a modifiable rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_modifiable_rule
(
    UF_KF_rule_p_t  rule,      /* <I> Rule object */
    logical        *modifiable /* <O> TRUE if the rule is a modifiable rule,
                                      else FALSE */
);

/****************************************************************************
Check whether a rule is an uncached rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_uncached_rule
(
    UF_KF_rule_p_t  rule,    /* <I> Rule object */
    logical        *uncached /* <O> TRUE if the rule is an uncached rule,
                                    else FALSE */
);

/****************************************************************************
Check whether a rule is a lookup rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_lookup_rule
(
    UF_KF_rule_p_t  rule,  /* <I> Rule object */
    logical        *lookup /* <O> TRUE if the rule is a lookup rule,
                                  else FALSE */
);


/****************************************************************************
Check whether a rule is a hidden rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_hidden_rule
(
    UF_KF_rule_p_t  rule,  /* <I> Rule object */
    logical        *hidden /* <O> TRUE if the rule is a hidden rule,
                                  else FALSE */
);

/****************************************************************************
Check whether a rule is a cached rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_cached_rule
(
    UF_KF_rule_p_t  rule,  /* <I> Rule object */
    logical        *cached /* <O> TRUE if the rule is a cached rule,
                                  else FALSE */
);

/****************************************************************************
Check whether a rule is local (defined on this class, not on an
ancestor).

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_local
(
    const char           *class_name, /* <I> The name of the class in question */
    UF_KF_rule_p_t  rule,       /* <I> Rule object*/
    logical        *local       /* <O> TRUE if the rule is a local rule,
                                       else FALSE */
);

/****************************************************************************
Check whether a rule is a method.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_method
(
    UF_KF_rule_p_t  rule,  /* <I> Rule object */
    logical        *method /* <O> TRUE if the rule is a method, else FALSE */
);

/****************************************************************************
Check whether a rule is dynamic.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_dynamic
(
    UF_KF_rule_p_t  rule,   /* <I> Rule object */
    logical        *dynamic /* <O> TRUE if the rule is dynamic, else FALSE */
);

/****************************************************************************
Get the default formula for a rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_default_formula
(
    UF_KF_rule_p_t   rule,   /* <I>  Rule object */
    char           **formula /* <OF> Text of formula. May be NULL if no default exists.
                                     Free with UF_free. */
);

/****************************************************************************
Check whether a given rule exists for a class.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_rule_in_class(
    const char * class_name,      /* <I>  Name of class to check for rule */
    const char * rule_name,       /* <I>  Name of rule to check for */
    logical *rule_in_class  /* <O> TRUE if the rule is in the class,
                                   else FALSE */
);

/****************************************************************************
Find the rule object for a name in a class.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_rule_of_name
(
    const char           *class_name, /* <I>  Name of class to find rule in. */
    const char           *rule_name,  /* <I>  Name of rule to find. */
    UF_KF_rule_p_t *rule        /* <O> Found rule object. */
);

/****************************************************************************
Find the rule object of a given name in an instance.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_rule_of_instance
(
    const char     *name_chain, /* <I> Reference chain of instance, with trailing colon */
    const char     *rule_name,  /* <I> Name of rule */
    UF_KF_rule_p_t *rule        /* <O> Found rule object */
);

/****************************************************************************
Get list of parameters that have been specified for an instance.  The
formula for each individual parameter can be obtained by calling
UF_KF_ask_parameter_formula.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_parameters
(
    const char   *name_chain,      /* <I>  Reference chain of instance, with trailing colon */
    char       ***parameter_names, /* <OF,len:num_params> Array of parameter names that were specified.
                                           Free with UF_free_string_array. */
    int          *num_params       /* <O>  Number of parameters found */
);

/****************************************************************************
Get datatype of a given parameter rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_parameter_type
(
    const char  *name_chain, /* <I>  Reference chain of instance, with trailing colon */
    const char  *param_name, /* <I>  Name of the parameter */
    char       **data_type   /* <OF> Data type of the parameter.
                                     Free with UF_free. */
);

/****************************************************************************
Get formula of a given parameter rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_parameter_formula
(
    const char  *name_chain, /* <I>  Reference chain of instance, with trailing colon */
    const char  *param_name, /* <I>  Name of the parameter */
    char       **formula     /* <OF> Formula for the rule.
                                     Free with UF_free. */
);

/****************************************************************************
Ask whether a rule has been evaluated yet.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_rule_computed
(
    const char *name_chain, /* <I> Reference chain of instance, with trailing colon */
    const char *rule_name,  /* <I> Name of the rule */
    logical    *evaluated   /* <O> TRUE if it has been evaluated, FALSE otherwise.*/
);

/****************************************************************************
Free a value returned by UF_KF_evaluate_rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_free_rule_value
(
    UF_KF_value_p_t value /* <I> value to free returned by UF_KF_evaluate_rule */
);

/****************************************************************************
Force a rule to be evaluated.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_evaluate_rule
(
    const char      *name_chain, /* <I>  Reference chain for the rule */
    UF_KF_value_p_t *value       /* <OF> Value of the rule after evaluation.
                                         Free with UF_KF_free_rule_value */
);

/****************************************************************************
Force a rule to be evaluated and return the result as a printable string.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_evaluate_rule_to_string
(
    const char  *name_chain, /* <I>  Reference chain of instance, with trailing colon */
    char       **value       /* <OF> Value of the rule after evaluation.
                                     Free with UF_free */
);

/****************************************************************************
Get the class for an instance.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_instance_class
(
    const char  *name_chain, /* <I>  Reference chain of instance, with trailing colon */
    char       **class_name  /* <OF> Name of the class that this instance uses.
                                     Free with UF_free */
);


/****************************************************************************
Get the list object from an instance that is a list datatype.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally release in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_list_of_instance
(
    const char      *name_chain, /* <I>  Reference chain of instance, with trailing colon */
    UF_KF_value_p_t *list_object /* <OF> The list value.
                                         Free with UF_KF_free_rule_value. */
);

/****************************************************************************
Count the number of items in a list object.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally release in v17.0 will be obsoleted after v19 use
UF_KF_ask_list_count
***************************************************************************/
extern UFUNEXPORT int UF_KF_count_list_items
(
    UF_KF_list_p_t  list,   /* <I> Knowledge Fusion list */
    int            *n_items /* <O> number of items in list object. */
);

/****************************************************************************
Ask the value of an item in a list object.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally release in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_value_of_list_item
(
    UF_KF_value_p_t   list_obj,   /* <I>  List value */
    int              list_index,  /* <I>  Index of item in the list.
                                          (1 is the  first item) */
    char           **value_str,   /* <OF> Text of item's value.
                                          Free with UF_free. */
    char           **datatype,    /* <OF> Data type of item.
                                          Free with UF_free */
    UF_KF_value_p_t *sub_list_obj /* <OF> If this item is a list value, then
                                          this parameter contains the list value.
                                          If this item is not a list value, then
                                          this parameter will be NULL.
                                          Free with UF_KF_free_rule_value. */
);

/****************************************************************************
Get list of data types that rules can be.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_rule_types(
    int    *num_types, /* <O>  Number of rule types existing */
    char ***data_types /* <OF,len:num_types> Array of data type names.
                               Free with UF_free_string_array. */
);

/****************************************************************************
Return a sorted array of all classes currently known by NX KF.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also: UF_KF_ask_classes
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_all_classes(
    int    *num_classes, /* <O>  Number of class names found */
    char ***classes      /* <OF,len:num_classes> num_classes Array of class names.
                                 Free with UF_free_string_array. */
);

/****************************************************************************
Return a sorted array of classes. Use the filter option to filter the type
of classes desired.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also: UF_KF_ask_all_classes
History: Originally released in v18.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_classes(
    UF_KF_class_type_t    filter_choice, /* <I>  filter choice:
                                                 UF_KF_ASK_USER_ONLY
                                                 UF_KF_ASK_SYSTEM_ONLY
                                                 UF_KF_ASK_ALL */
    int                  *num_classes,   /* <O>  Number of class names found */
    char               ***classes        /* <OF,len:num_classes>
                                                 Array of class names.
                                                 Free with UF_free_string_array */
);

/****************************************************************************
Set the user class dir.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_set_user_class_dir
(
    char **new_dirs, /* <I,len:num_dirs> . Array of directories to set as user class dir */
    int    num_dirs  /* <I> Number of directories */
);

/****************************************************************************
Return the user class directory.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_user_class_dir
(
    char **dir /* <OF> User class directory path.
                       Free with UF_free. */
);

/****************************************************************************
Check whether a rule is a child list rule.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_child_list_rule
(
    UF_KF_rule_p_t  rule,          /* <I> Rule object returned from
                                          UF_KF_ask_rules_of_class */
    logical        *is_child_list  /* <O> TRUE if the rule is a child list
                                          rule, else FALSE */
);

/****************************************************************************
Find out if the instance is a child list.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_is_child_list_instance
(
    const char *name_chain,      /* <I> Reference chain of instance, with trailing colon */
    logical    *is_list_instance /* <O> TRUE if the instance is a child list,
                                        else FALSE */
);

/****************************************************************************
Free the contents of the list object returned from UF_KF_ask_list.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally release in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_free_list_object_contents
(
    UF_KF_list_p_t list /* <I> Knowledge Fusion list */
);

/****************************************************************************
get the names of all the rules under a given instance.
Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally release in v17.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_rules
(
    const char   *name_chain, /* <I>  Reference chain of the instance */
    int    *num_rules,  /* <O>  Number of rules found for this instance */
    char ***rules       /* <OF,len:num_rules> Array of rules found under the instance.
                                Free with UF_free_string_array. */
);

/****************************************************************************
Adopt NX objects into the Knowledge Fusion world

If NX classes are enabled, then an instance of an NX object will be adopted.
Otherwise, an instance of an NX object will be adopted.
For example, if you are adopting and instance of a block feature, you will
either get an NX_block or a NX_block instance.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
UF_KF_set_nx_classes_enabled
UF_KF_ask_nx_classes_enabled
History: Originally release in v18.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_adopt_ug_objects
(
    tag_t               *ug_objects,        /* <I,len:number_of_objects> array of tags of NX objects
                                                   to be adopted into Fusion */
    int                  number_of_objects, /* <I>  number of objects in the
                                                    above array */
    UF_KF_instance_p_t **instances          /* <OF,len:number_of_objects> array of adopted instances.
                                                    Free with UF_free. */
);
/****************************************************************************
Adopt NX objects into the Knowledge Fusion world

If NX classes are enabled, then an you can determine which type of instance you
will adopt by using the nx_type argument. If nx_type is set to TRUE, then you will
adopt an NX instance. If nx_type is set to false, then you will adopt an NX instance.

However, if NX classes are disabled, then you can only adopt NX instances, regardless
of the setting of nx_type.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
UF_KF_set_nx_classes_enabled
UF_KF_ask_nx_classes_enabled
UF_KF_adopt_ug_object
History: released in NX5.0
***************************************************************************/
extern UFUNEXPORT int UF_KF_adopt_nx_objects
(
    tag_t               *ug_objects,        /* <I,len:number_of_objects> array of tags of NX objects
                                                   to be adopted into Fusion */
    int                  number_of_objects, /* <I>  number of objects in the
                                                    above array */
    logical              nx_type,           /* <I>  = TRUE  - adopt as NX instance object
                                                    = FALSE - adopt as NX instance object */
    UF_KF_instance_p_t **instances          /* <OF,len:number_of_objects> array of adopted instances.
                                                    Free with UF_free. */
);

/****************************************************************************
Ask the name chain of a Knowledge Fusion instance

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally release in v18.0
         Modified in NX 11 user is now responsible for freeing the returned
         string
***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_name_chain_of_instance
(
    UF_KF_instance_p_t   instance,  /* <I> Knowledge Fusion instance */
    char         **name_chain /* <OF> Name chain of instance. Free with UF_free. */
);

/****************************************************************************
Return rule text for referencing an NX object in Knowledge Fusion.  Note 
that the rule text may reference the container object rather than the given 
object.  For example, the rule text may reference the owning CSYS feature 
rather than the given datum plane or datum axis.  If the rule text of the
given object is desired then call in the NXOpen API the method GetObjectText
which is on the class RuleManager.

Return:

    0 if function succeeds, otherwise
      error code (non-zero).

Environment: Internal and External
See Also:
History: Released in V18
****************************************************************************/
extern UFUNEXPORT int UF_KF_ask_rule_text_of_referencing_object(
    tag_t   ug_object_tag, /* <I>  Tag of the NX object */
    char  **rule_text      /* <OF> Rule text to be used in Knowledge Fusion.
                                   Free with UF_free. */
);

/****************************************************************************
Return the calling instance of Defun.

Return:

    0 if function succeeds, otherwise
      error code (non-zero).

Environment: Internal and External
See Also:
History: Released in V18.1
****************************************************************************/
extern UFUNEXPORT int UF_KF_ask_instance_of_args
(
    UF_KF_value_p_t    *values,    /* <I,len:n_values> Argument values of Defun */
    int                 n_values,  /* <I> Number of argument values */
    UF_KF_instance_p_t *instance   /* <O,len:n_values> Instance calling Defun */
);

/****************************************************************************
Remove all rules in the current part.

Return:

    0 if function succeeds, otherwise
      error code (non-zero).

Environment: Internal and External
See Also:
History: Released in NX204
****************************************************************************/
extern UFUNEXPORT int UF_KF_remove_all_rules
(
    void
);

/****************************************************************************
Get the measure of a Number Knowledge Fusion structure.  This function returns
strings like "Length", "Area" and "Volume".  The empty string is returned for
number values that do not have a measure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in NX301
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_measure_of_value
(
    UF_KF_value_p_t   value,  /* <I> Knowledge Fusion data structure */
    const char      **measure /* <O> Measure of value */
);

/****************************************************************************
Set the measure of a Number Knowledge Fusion structure.  This function accepts
strings like "Length", "Area" and "Volume".  The empty string is accepted for
number values that do not have a measure.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in NX301
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_set_measure_of_value
(
    UF_KF_value_p_t  value,  /* <I> Knowledge Fusion data structure */
    const char      *measure /* <I>  Measure of value */
);

/****************************************************************************
Get the base unit of a measure.  For example, "mm" will be returned for "Length"
in a metric part.  The empty string will be returned for an invalid unit.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in NX301
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_base_unit_of_measure
(
    const char  *measure,  /* <I> Measure of value */
    char **base_unit       /* <OF> Base unit of measure 
                             Free with UF_free()*/
);
/****************************************************************************
Return true if NX classes are enabled for the Create Child rule dialog and for
adoption in the specified part.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in NX400
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_ask_nx_classes_enabled
(
    const tag_t  object_in_part,    /* <I> Tag of object in part */
    logical     *nx_classes_enabled /* <O> True --> nx classes enabled */
);

/****************************************************************************
If true then set NX classes enabled for the Create Child rule dialog and for
adoption in the specified part.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Released in NX400
 ***************************************************************************/
extern UFUNEXPORT int UF_KF_set_nx_classes_enabled
(
    const tag_t object_in_part,    /* <I> Tag of object in part */
    logical     nx_classes_enabled /* <I> True --> nx classes enabled */
);
/****************************************************************************
Remove a dynamic child or attribute rule, but leave the geometry.

Return :
          Return code :
           = 0 : successful
           > 0 : failing error number
           < 0 : failing error number

Environment: Internal and External
See Also:
History: Originally released in NX 3.0.4
***************************************************************************/
extern UFUNEXPORT int UF_KF_remove_rule_only
(
    const char *name_chain, /* <I> Instance that rule is part of. */
    const char *rule_name   /* <I> Name of rule */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_KF_H_INCLUDED */
