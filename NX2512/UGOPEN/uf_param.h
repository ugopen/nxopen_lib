/*******************************************************************************
            Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                     Unpublished - All rights reserved
================================================================================



File description:
  This module allows programmers to work with the most general class of CAM
  User Function objects. It is used to query and set the parameters of most
  UF CAM objects and to control the inheritance of parameter values.

  It is also used to perform generic functions such as rename and duplicate.
  Most UF CAM objects, (e.g., UF_SETUP, UF_OPER, UF_NCGROUP), inherit from
  UF_PARAM. Due to module function inheritance, all the functions of
  UF_PARAM can be applied to any object of any module that belongs to the
  hierarchy rooted at UF_PARAM. This hierarchy can be found in <>.

*****************************************************************************/
#ifndef UF_PARAM_H_INCLUDED
#define UF_PARAM_H_INCLUDED

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_cam_errors.h>
#include <uf_ude.h>
#include <libufun_cam_exports.h>



#ifdef __cplusplus
extern "C" {
#endif

/******************************** Defines *************************************
   UF_PARAM_MAX_PARAM_NAME_LEN 
    is being deprecated because NX is moving to support multibyte
    characters. User written programs should start use the new definitions:
        MAX_LINE_BUFSIZE should be used for buffer allocations and memory 
                                           allocations, e.g. char my_data[MAX_FSPEC_BUFSIZE];
        MAX_LINE_NCHARS should be used to limit the number of characters in
                                             a buffer. NX code will enforce these limits.
    New routines have been added that will help in this transition:
        UF_TEXT_count_characters() will count the number of characters in a buffer.
        UF_TEXT_truncate() will truncate a string to a given byte and character count.
*/
/*  */
#define UF_PARAM_MAX_PARAM_NAME_LEN   (MAX_LINE_BUFSIZE-1)
/*  */ 


/*This value should be same as PARAM_REQUIRED_LIST_SIZE defined in param.h*/
#define UF_PARAM_REQUIRED_LIST_SIZE 1200

/******************************** Typedefs ************************************

 * These are the available options for a parameters regeneration type. They
 * inidicate what must be regenerated if the parameter changes value.
 */
enum UF_PARAM_regen_e
{
   UF_PARAM_REGEN_NONE,     /*   If parameter changes then no regeneration is needed */
   UF_PARAM_REGEN_POST,     /*   If parameter changes then regenerate post only */
   UF_PARAM_REGEN_PATH,     /*   If parameter changes then regenerate toolpath only */
   UF_PARAM_REGEN_ALL       /*   If parameter changes then regenerate both */
};

typedef enum UF_PARAM_regen_e UF_PARAM_regen_t;


/* These are the various states an object's parameter inheritence
 * can be in during run time.
 */
enum UF_PARAM_status_e
{
   UF_PARAM_DEFAULT,       /* Getting value from NX default */
   UF_PARAM_INHERITED,     /* Inheriting value from another run time object */
   UF_PARAM_OVERRIDDEN,    /* Using a value set by the object itself */
   UF_PARAM_INVALID_INDEX  /* Index does not exist for indicated object */
};

typedef enum UF_PARAM_status_e UF_PARAM_status_t;

/* These are the available data types that a parameter may be.
 *  LENGTH signifies that the value should be expressed based upon the
 *  units of the part, i.e., inch or mm. VLA signifies that it is an
 *  array with a variable number of elements (currently not supported
 *  in UFUN). 2D and 3D signify 2 doubles and 3 doubles, respectively. */
enum UF_PARAM_type_e
{
   UF_PARAM_TYPE_LOGICAL,
   UF_PARAM_TYPE_CHAR,
   UF_PARAM_TYPE_SHORT,
   UF_PARAM_TYPE_INT,
   UF_PARAM_TYPE_POINTER,
   UF_PARAM_TYPE_FLOAT,
   UF_PARAM_TYPE_DOUBLE,
   UF_PARAM_TYPE_BYTE,
   UF_PARAM_TYPE_DATE,
   UF_PARAM_TYPE_TAG,
   UF_PARAM_TYPE_STRING,
   UF_PARAM_TYPE_2D,
   UF_PARAM_TYPE_3D,
   UF_PARAM_TYPE_VLA_REAL,
   UF_PARAM_TYPE_VLA_INT,
   UF_PARAM_TYPE_VLA_TAG,
   UF_PARAM_TYPE_DOUBLE_LENGTH,
   UF_PARAM_TYPE_2D_LENGTH,
   UF_PARAM_TYPE_3D_LENGTH,
   UF_PARAM_TYPE_VLA_LENGTH,
   UF_PARAM_TYPE_VLA_STRING,
   UF_PARAM_TYPE_OBJECT,
   UF_PARAM_TYPE_VLA_LENGTH_COMPOSITE,
   UF_PARAM_TYPE_LAST
};

typedef enum UF_PARAM_type_e UF_PARAM_type_t;

/* The attributes that describe a parameter */
struct UF_PARAM_index_attribute_s
{
   int                key; /* The unique integer for this parameter */
   char               name[MAX_LINE_BUFSIZE]; /* The parameter's
                                                                name */
   UF_PARAM_type_t    type; /* See UF_PARAM_type_t definition */
   int                int_default; /* If type is integer then its default
                                      value */
   double             dbl_default; /* If type is double then its default
                                      value */
   UF_PARAM_regen_t   regen_flag; /* What to regenerate if parameter changes */
};

typedef struct UF_PARAM_index_attribute_s UF_PARAM_index_attribute_t,
*UF_PARAM_index_attribute_p_t;

/******************************** Prototypes **********************************/


/*******************************************************************************
 This function returns TRUE in 'answer' if the object specified by 'obj1_tag'
 is the same class as the object specified by 'obj2_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_is_same_class
(
   tag_t      obj1_tag, /* <I> - see above */
   tag_t      obj2_tag, /* <I> - see above */
   logical   *answer    /* <O> - see above */
);


/*******************************************************************************
 This function creates a new object of the same type as 'old_obj_tag'. It
 initializes this object with the data of 'old_obj_tag'. It assigns 'name'
 to the new object as it's name. It returns the tag of this newly created
 object in 'new_obj_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_duplicate
(
   tag_t         old_obj_tag, /* <I> - see above */
   const char   *name,        /* <I> - see above */
   tag_t        *new_obj_tag  /* <O> - see above */
);


/*******************************************************************************
 This function assigns the name 'new_name' to the object specified by
 'param_tag'. The first character of 'new_name' must be an alphabetic
 character.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_rename
(
   tag_t         param_tag, /* <I> - see above */
   const char   *new_name   /* <I> - see above */
);


/*******************************************************************************
 This function returns back the list of required paramter indices for the
 object specifed in 'param_tag'. The number of indices is returned in 'count'
 and the list of indices is returned in 'indices'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_required_params
(
   tag_t   param_tag, /* <I> - see above */
   int    *count,     /* <O> - see above */
   int   **indices    /* <OF,len:count>- see above */
);


/*******************************************************************************
 This function returns back the list of inherited paramter indices of the
 object specifed in 'param_tag'. This is parameters that are currently
 inherited. Since data inheritance is dynamic this list can change each time
 this function is called. The number of indices is returned in 'count'
 and the list of indices is returned in 'indices'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_inherited_params
(
   tag_t   param_tag,  /* <I> - see above */
   int    *count,      /* <O> - see above */
   int    indices[UF_PARAM_REQUIRED_LIST_SIZE]     /* <O> - see above */
);


/*******************************************************************************
 This function deletes any override that object 'param_tag' might have for
 parameter 'param_index'. Whether or not 'param_tag' was overriding the value
 of this parameter, it will be inheriting its value after this call.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_inherit_value
(
   tag_t   param_tag,  /* <I> - see above */
   int     param_index /* <I> - see above */
);


/*******************************************************************************
 This function returns TRUE in 'answer' if the object specified by 'param_tag'
 is currently inheriting the parameter specified by 'param_index'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_is_inherited
(
   tag_t      param_tag, /* <I> - see above */
   int        param_index, /* <I> - see above */
   logical   *answer /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'definer_tag' the object from which object 'param_tag'
 is currently getting the value of the parameter 'param_index'. It is
 possible that 'definer_tag' is the same as 'param_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_param_definer
(
   tag_t    param_tag, /* <I> - see above */
   int      param_index, /* <I> - see above */
   tag_t   *definer_tag /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'attributes' the data documented in the structure
 UF_PARAM_index_attribute_t. This data will be for the parameter specified by
 'param_index'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_param_attributes
(
   int                           param_index, /* <I> - see above */
   UF_PARAM_index_attribute_t   *attributes /* <O> - see above */
);


/******************************************************************************
 This function returns in 'value' the value of the parameter specified by
 'param_index'. It is the value of this parameter that is currently being
 used by the object specified by 'param_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_int_value
(
   tag_t   param_tag, /* <I> - see above */
   int     param_index, /* <I> - see above */
   int    *value /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'value' the value of the parameter specified by
 'param_index'. It is the value of this parameter that is currently being
 used by the object specified by 'param_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_double_value
(
   tag_t     param_tag, /* <I> - see above */
   int       param_index, /* <I> - see above */
   double   *value /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'value' the 2d array of the parameter specified by
 'param_index'. It is the value of this parameter that is currently being
 used by the object specified by 'param_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in NX2.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_2d_value
(
   tag_t     param_tag, /* <I> - see above */
   int       param_index, /* <I> - see above */
   double    value[2] /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'value' the 3d array of the parameter specified by
 'param_index'. It is the value of this parameter that is currently being
 used by the object specified by 'param_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in NX2.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_3d_value
(
   tag_t     param_tag, /* <I> - see above */
   int       param_index, /* <I> - see above */
   double    value[3] /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'value' the value of the parameter specified by
 'param_index'. It is the value of this parameter that is currently being
 used by the object specified by 'param_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_logical_value
(
   tag_t      param_tag, /* <I> - see above */
   int        param_index, /* <I> - see above */
   logical   *value /* <O> - see above */
);


/*******************************************************************************
 This function copies to 'value' the contents of the memory pointed at by the
 pointer parameter specified by 'param_index'. It is the value of this
 parameter that is currently being used by the object specified by 'param_tag'.

 The caller must ensure that value points at a UF_PARAM_<type>_t that
 corresponds to the type of object that is pointed at by this parameter index.
 The proper type of object is specified in uf_param_indices.h in the comments
 about the parameter index.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_subobj_ptr_value
(
   tag_t   param_tag, /* <I> - see above */
   int     param_index, /* <I> - see above */
   void   *value /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'value' the value of the parameter specified by
 'param_index'. It is the value of this parameter that is currently being
 used by the object specified by 'param_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_tag_value
(
   tag_t   param_tag, /* <I> - see above */
   int     param_index, /* <I> - see above */
   tag_t  *value /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'value' the value of the parameter specified by
 'param_index'. It is the value of this parameter that is currently being
 used by the object specified by 'param_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_str_value
(
   tag_t   param_tag, /* <I> - see above */
   int     param_index, /* <I> - see above */
   char    value[ MAX_LINE_BUFSIZE ] /* <O> - see above */
);


/*******************************************************************************
 This function returns in 'tag_array' the array of tags of the parameter
 specified by 'param_index'. It is the array of values of this parameter
 that is currently being used by the object specified by 'param_tag'.  The
 number of tags is returned in 'count.'

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_tag_vla
(
   tag_t   param_tag,     /* <I> - see above */
   int     param_index,   /* <I> - see above */
   int     *count,        /* <O> - number of tags in tag_array  */
   tag_t  **tag_array     /* <OF,len:count> - see above.  This must be freed by the
                          caller using UF_free */
);

/*******************************************************************************
 This function returns in 'int_array' the array of integer values of the
 parameter specified by 'param_index'. It is the array of values of this
 parameter that is currently being used by the object specified by 'param_tag'.
 The number of integer values is returned in 'count.'

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_int_vla
(
   tag_t   param_tag,     /* <I> - see above */
   int     param_index,   /* <I> - see above */
   int     *count,        /* <O> - number of integers in int_array  */
   int     **int_array    /* <OF,len:count> - see above.  This must be freed by the
                          caller using UF_free */
);

/*******************************************************************************
 This function returns in 'dbl_array' the array of doubles of the parameter
 specified by 'param_index'. It is the array of values of this parameter
 that is currently being used by the object specified by 'param_tag'.  The
 number of doubles is returned in 'count.'

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_double_vla
(
   tag_t   param_tag,     /* <I> - see above */
   int     param_index,   /* <I> - see above */
   int     *count,        /* <O> - number of doubles in dbl_array  */
     double  **dbl_array    /* <OF,len:count> - see above.  This must be freed by the
                          caller using UF_free */
);

/*******************************************************************************
 This function assigns the value 'value' to the parameter specified by
 'param_index' for the object specified by 'param_tag'. This has the effect
 of 'param_tag' overriding the inherited value of parameter 'param_index'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_int_value
(
   tag_t   param_tag, /* <I> - see above */
   int     param_index, /* <I> - see above */
   int     value /* <I> - see above */
);


/*******************************************************************************
 This function assigns the value 'value' to the parameter specified by
 'param_index' for the object specified by 'param_tag'. This has the effect
 of 'param_tag' overriding the inherited value of parameter 'param_index'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_double_value
(
   tag_t    param_tag, /* <I> - see above */
   int      param_index, /* <I> - see above */
   double   value /* <I> - see above */
);


/*******************************************************************************
 This function assigns the 2d array 'value' to the parameter specified by
 'param_index' for the object specified by 'param_tag'. This has the effect
 of 'param_tag' overriding the inherited value of parameter 'param_index'.

Environment: Internal  and  External

See Also:

History: Originally released in NX2.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_2d_value
(
   tag_t    param_tag, /* <I> - see above */
   int      param_index, /* <I> - see above */
   double   value[2] /* <I> - see above */
);


/*******************************************************************************
 This function assigns the 3d array 'value' to the parameter specified by
 'param_index' for the object specified by 'param_tag'. This has the effect
 of 'param_tag' overriding the inherited value of parameter 'param_index'.

Environment: Internal  and  External

See Also:

History: Originally released in NX2.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_3d_value
(
   tag_t    param_tag, /* <I> - see above */
   int      param_index, /* <I> - see above */
   double   value[3] /* <I> - see above */
);

/*******************************************************************************
 This function assigns the value 'value' to the parameter specified by
 'param_index' for the object specified by 'param_tag'. This has the effect
 of 'param_tag' overriding the inherited value of parameter 'param_index'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_logical_value
(
   tag_t     param_tag, /* <I> - see above */
   int       param_index, /* <I> - see above */
   logical   value /* <I> - see above */
);


/*******************************************************************************
 This function sets the value of the specified 'parm_index' to the contents of
 the memory pointed at by 'value'. This will be the value for 'parm_index' that
 will be used by the object specified by 'param_tag'.

 The caller must ensure that value points at a UF_PARAM_<type>_t that
 corresponds to the type of object that is pointed at by this parameter index.
 The proper type of object is specified in uf_param_indices.h in the comments
 about the parameter index.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_subobj_ptr_value
(
   tag_t   param_tag, /* <I> - see above */
   int     param_index, /* <I> - see above */
   void   *value /* <I> - see above */
);


/*******************************************************************************
 This function assigns the value 'value' to the parameter specified by
 'param_index' for the object specified by 'param_tag'. This has the effect
 of 'param_tag' overriding the inherited value of parameter 'param_index'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_tag_value
(
   tag_t   param_tag, /* <I> - see above */
   int     param_index, /* <I> - see above */
   tag_t   value /* <I> - see above */
);


/*******************************************************************************
 This function assigns the value 'value' to the parameter specified by
 'param_index' for the object specified by 'param_tag'. This has the effect
 of 'param_tag' overriding the inherited value of parameter 'param_index'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_str_value
(
   tag_t   param_tag, /* <I> - see above */
   int     param_index, /* <I> - see above */
   char   *value /* <I> - see above */
);


/*******************************************************************************
 This function assigns the array values defined in 'tag_array' to the parameter
 specified by 'param_index' for the object specified by 'param_tag'.  This has
 the effect of 'param_tag' overriding the inherited value of the parameter
 'param_index.'  The number of tags to be assigned is in 'count.'

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_tag_vla
(
   tag_t   param_tag,     /* <I> - see above */
   int     param_index,   /* <I> - see above */
   int     count,         /* <I> - number of tags in tag_array  */
   tag_t   *tag_array     /* <I,len:count> - see above. */
);

/*******************************************************************************
 This function assigns the array values defined in 'int_array' to the parameter
 specified by 'param_index' for the object specified by 'param_tag'.  This has
 the effect of 'param_tag' overriding the inherited value of the parameter
 'param_index.'  The number of integers to be assigned is in 'count.'

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_int_vla
(
   tag_t   param_tag,     /* <I> - see above */
   int     param_index,   /* <I> - see above */
   int     count,         /* <I> - number of integers in int_array  */
   int     *int_array     /* <I,len:count> - see above. */
);

/*******************************************************************************
 This function assigns the array values defined in 'dbl_array' to the parameter
 specified by 'param_index' for the object specified by 'param_tag'.  This has
 the effect of 'param_tag' overriding the inherited value of the parameter
 'param_index.'  The number of doubles to be assigned is in 'count.'

Environment: Internal  and  External

See Also:

History: Originally released in NX3.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_set_double_vla
(
   tag_t   param_tag,     /* <I> - see above */
   int     param_index,   /* <I> - see above */
   int     count,         /* <I> - number of doubles in dbl_array  */
   double  *dbl_array     /* <I,len:count> - see above. */
);

/*******************************************************************************
 This function returns in 'status' the current inheritance status of the
 parameter 'param_index' for the object 'param_tag'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_param_status
(
   tag_t                param_tag, /* <I> - see above */
   int                  param_index, /* <I> - see above */
   UF_PARAM_status_t   *status /* <O> - see above */
);


/*******************************************************************************
 This function generates the tool path for the operations associated with
 the object specified by 'param_tag'. If this object is a group then the tool
 paths for all operations in the group will be generated. If the object is an
 operation then the tool path for that single operation will be generated.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_generate
(
   tag_t      param_tag, /* <I> - see above */
   logical   *generated  /* <O> - see above */
);


/*******************************************************************************
 This function will check if all the parameters of UF_PARAM object 'param' are
 in a state which is valid for generation. If they are then TRUE is returned in
 'is_ok' else FALSE is returned in 'is_ok'. What 'generation' means is
 determined by the type of the UF_PARAM object. E.g., if it is a UF_OPER object
 then 'generation' means tool path generation.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_check
(
   tag_t      param, /* <I> - see above */
   logical   *is_ok  /* <O> - see above */
);


/*******************************************************************************
 This function will reinitialize the data of 'param_to_reinit' with the data of
 'param_to_init_from'.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_reinit
(
   tag_t   param_to_reinit,     /* <I> - the param to reinit */
   tag_t   param_to_reinit_from /* <I> - the param whose data is used to reinit
                                         param_to_reinit */
);

/*******************************************************************************
 This function sets the 'response' to TRUE if the Machine Control 'set_type' is
 valid for the param object 'param' or to FALSE if it is not valid.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_can_accept_ude_set
(
   tag_t               param,        /* <I> - see above */
   UF_UDE_set_type_t   ude_set_type, /* <I> - see above */
   logical            *response      /* <O> - see above */
);

/*******************************************************************************
 This function returns all the User Defined Machine Control Event objects in
 'ude_objs' contained in the Machine Control Event set of type 'ude_set_type'
 in the param object 'param'. It also returns the number of User Defined
 Machine Control Events in 'num_of_udes'.

Environment: Internal  and  External

See Also:
 Functions in the UF_UDE module to interrogate or edit any of the 'ude_objs'

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_ask_udes
(
   tag_t               param,        /* <I> see above */
   UF_UDE_set_type_t   ude_set_type, /* <I> see above */
   int                *num_of_udes,  /* <O> see above */
   UF_UDE_t          **ude_objs      /* <OF,len:num_of_udes> see above
                                        This should be freed by
                                        calling UF_free. */
);

/*******************************************************************************
 This deletes all the User Defined Machine Control Event objects contained in
 the Machine Control Event set of type 'ude_set_type' in the param object
 'param'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_delete_all_udes
(
   tag_t               param,        /* <I> see above */
   UF_UDE_set_type_t   ude_set_type  /* <I> see above */
);

/*******************************************************************************
 This function appends the User Defined Machine Contol Event with name
 'ude_name' to the Machine Control set of type 'ude_set_type' in the
 param object 'param'. It also returns the created User Defined Machine Control
 Event object in 'ude_obj'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_append_ude
(
   tag_t               param,        /* <I> see above */
   UF_UDE_set_type_t   ude_set_type, /* <I> see above */
   char               *ude_name,     /* <I> see above */
   UF_UDE_t           *ud_obj        /* <O> see above */
);

/*******************************************************************************
 This function deletes the specified User Defined Machine Control Event object
 'ude_obj' from the Machine Control Event set of type 'ude_set_type' in the
 param object 'param'.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_delete_ude
(
   tag_t               param,        /* <I> see above */
   UF_UDE_set_type_t   ude_set_type, /* <I> see above */
   UF_UDE_t            ude_obj       /* <I> see above */
);

/*******************************************************************************
 This function sets the 'response' to TRUE if the specified User Defined
 Machine Control of name 'ude_name' is valid for the Machine Control set of
 type 'set_type' in the param object 'param' or to FALSE if it is not valid.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_can_accept_ude
(
   tag_t               param,        /* <I> - see above */
   UF_UDE_set_type_t   ude_set_type, /* <I> - see above */
   char               *ude_name,     /* <I> - see above */
   logical            *response      /* <O> - see above */
);
/*******************************************************************************
 This function sets the 'response' to TRUE if the specified param object is set
 as template or to FALSE otherwise.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_is_template
(
   tag_t      param,     /* <I> - see above */
   logical   *response   /* <O> - see above */
);

/*******************************************************************************
 This function sets the 'response' to TRUE if the specified param object is set
 as load with parent or to FALSE otherwise.

Environment: Internal  and  External

See Also:

History: Originally released in V18.0
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_is_load_with_parent
(
   tag_t      param,     /* <I> - see above */
   logical   *response   /* <O> - see above */
);

/*******************************************************************************
 This function replays the tool path for the operations associated with
 the object specified by 'param_tag'. If this object is a group then the tool
 paths for all operations in the group will be replayed. If the object is an
 operation then the tool path for that single operation will be replayed.

Environment: Internal  and  External

See Also:

History: Originally released in NX3
*******************************************************************************/
extern UFUN_CAMEXPORT int UF_PARAM_replay_path
(
   tag_t      param_tag  /* <I> - see above */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_PARAM_H_INCLUDED */
