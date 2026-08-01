/*******************************************************************************
    Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
             Unpublished - All rights reserved
*****************************************************************************



File description:

This module is designed to be used primarily in the code that is in the
function called by the Event Handler via MOM_run_user_function.  It allows that
code to access the interpreter from which MOM_run_user_function was called. The
code can perform functions like asking and setting variables in the interpreter
and extending the interpreter with new functions. It can also be used with
CAM Exits that are associated with a TCL interpreter.

NOTE: Any function that sets a variable in the TCL interpreter, e.g., MOM_set_double,
      sets the variable as a global variable. Therefore, in order to use its
      value inside of a TCL proc you must declare that variable as "global"
      in the proc. For example, if you call

                UF_MOM_set_double( mom_id, "my_var", 1.23 );

      it will be known as "mom_my_var" inside of every TCL proc and it will
      be a global variable in every proc. So, e.g., to access it in
      MOM_start_of_program you need
        proc MOM_start_of_program {
                   global mom_my_var
                   ...
                }

 ******************************************************************************/

#ifndef UF_MOM_H
#define UF_MOM_H

#include <uf_defs.h>
#include <libufun_exports.h>

/*  */

#ifdef __cplusplus
extern "C" {
#endif

/********************************** Defines ***********************************/

/********************************** TypeDefs **********************************/

/****************************************************************************

   This is the identifier type that is passed to certain CAM User Exits.
   This identifier is only used upon the original call to the User
   Exit. After receiving this identifier the User Exit must call
   UF_<module>_ask_<module> to retrieve the identifier which will be used in
   further transactions with NX CAM via the User Function layer for a
   particular module.

*****************************************************************************/
typedef void   *UF_MOM_id_t;

/**/

/* This is the signature for any function that is used to extend the
 * interpreter.
 */
typedef int (*UF_MOM_command_func)( void *clientData, /* <I> */
                                   void *interp, /* <I> */
                                   int argc, /* <I> */
                                   char *argv[] /* <I,len:argc> */ );


/*******************************************************************************
This function attaches the entry point 'c_func' to the TCL procedure
named 'command_name' in the TCL interpreter owned by the UF_MOM_id_t
object 'mom_id'. After this call is completed, any calls to 'command_name'
from the interpreter will cause 'c_func' to be executed.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_extend_xlator
(
   UF_MOM_id_t          mom_id,        /* <I> - see above */
   char                *command_name,  /* <I> - see above */
   UF_MOM_command_func  c_func         /* <I> - see above */
);


/*******************************************************************************
This function returns the value of the TCL variable 'var_name' as it
currently is in the interpreter owned by 'mom_id'.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_ask_string
(
   UF_MOM_id_t          mom_id,    /* <I> - see above */
   char                *var_name,  /* <I> - see above */
   const char         **var_val    /* <OF> - see above */
);


/*******************************************************************************
This function sets the value of the TCL variable 'var_name' to the
value 'var_val' in the interpreter owned by 'mom_id'.


Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_set_string
(
   UF_MOM_id_t          mom_id,    /* <I> - see above */
   char                *var_name,  /* <I> - see above */
   char                *var_val    /* <I> - see above */
);


/*******************************************************************************
This function sets the value of the TCL variable 'var_name' to the
value 'var_val' in the interpreter owned by 'mom_id'.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_set_int
(
   UF_MOM_id_t          mom_id,    /* <I> - see above */
   char                *var_name,  /* <I> - see above */
   int                  var_val    /* <I> - see above */
);


/*******************************************************************************
This function sets the value of the TCL variable 'var_name' to the
value 'var_val' in the interpreter owned by 'mom_id'.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_set_double
(
   UF_MOM_id_t          mom_id,    /* <I> - see above */
   char                *var_name,  /* <I> - see above */
   double               var_val    /* <I> - see above */
);


/*******************************************************************************
Given the param argument passed as the first argument to a CAM exit
this function returns its associated TCL interpreter.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_ask_interp_from_param
(
   void    *param,   /* <I> - see above */
   void   **interp   /* <OF> - see above */
);


/*******************************************************************************
This function extracts and returns the UF_MOM object that is associated
with the User Exit (ufusr style) first parameter 'param'. This is useful
when coding an entry point in a library that is going to be called by
using the TCL extension MOM_run_user_function <library> <entry point>.
This enables you to get the UF_MOM_id_t that you need to pass to other
UF_MOM user function functions.

<entry point> has a ufusr signature.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_ask_mom
(
   void          *param,   /* <I> - see above */
   UF_MOM_id_t   *mom_id   /* <O> - see above */
);


/*******************************************************************************
This function sets the values of an integer array in the Event Handler
attached to the specified UF_MOM object.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_set_int_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to set */
   int           num_of_values, /* <I> - the number of values to set */
   int          values[]         /* <I,len:num_of_values>
                                 the values to set */
);


/*******************************************************************************
This function asks the values of an integer array in the Event Handler
attached to the specified UF_MOM object.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_ask_int_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to ask */
   int           num_of_values, /* <I> - the number of values to ask */
   int          *values         /* <I/O,len:num_of_values>
                                the values asked for, this must
                                   point at num_of_values * sizeof(int) bytes */
);


/*******************************************************************************
This function sets the values of an double array in the Event Handler
attached to the specified UF_MOM object.

The indicies will be 0, 1, ..., num_of_values - 1.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_set_double_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to set */
   int           num_of_values, /* <I> - the number of values to set */
   double       values[]         /* <I,len:num_of_values>
                                 - the values to set */
);


/*******************************************************************************
This function asks the values of an double array in the Event Handler
attached to the specified UF_MOM object.

The indicies will be 0, 1, ..., num_of_values - 1.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_ask_double_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to ask */
   int           num_of_values, /* <I> - the number of values to ask */
   double       *values         /* <I/O,len:num_of_values>
                                the values asked for. This must
                                   point at num_of_values * sizeof(double)
                                   bytes */
);


/*******************************************************************************
This function sets the values of a string array in the Event Handler
attached to the specified UF_MOM object.

The indicies will be 0, 1, ..., num_of_values - 1.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_set_string_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to set */
   int           num_of_values, /* <I> - the number of values to set */
   char        **values         /* <I,len:num_of_values> - the values to set */
);


/*******************************************************************************
This function asks the values of a string array in the Event Handler
attached to the specified UF_MOM object.

The indicies will be 0, 1, ..., num_of_values - 1.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_ask_string_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to ask */
   int           num_of_values, /* <I> - the number of values to ask */
   char        **values         /* <OF,len:num_of_values> - the values asked for. The caller
                                     has already allocated memory for the
                                     pointers. The memory pointed at by the
                                     pointers is allocated by this function
                                     and must be freed by caller.           */

);


/*******************************************************************************
This function sets the value of an associative integer array in the
Event Handler attached to the specified UF_MOM object.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_set_assoc_int_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to set */
   char         *index_name, /* <I> - the name of the index */
   int           value       /* <I> - the value to set */
);


/*******************************************************************************
This function returns the value of an associative integer array in the
Event Handler attached to the specified UF_MOM object.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_ask_assoc_int_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to ask */
   char         *index_name, /* <I> - the name of the index */
   int          *value       /* <O> - the value asked for */
);


/*******************************************************************************
This function sets the value of an associative double array in the
Event Handler attached to the specified UF_MOM object.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_set_assoc_double_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to set */
   char         *index_name, /* <I> - the name of the index */
   double        value       /* <I> - the value to set */
);


/*******************************************************************************
This function returns the value of an associative double array in the
Event Handler attached to the specified UF_MOM object.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_ask_assoc_double_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to ask */
   char         *index_name, /* <I> - the name of the index */
   double       *value       /* <O> - the value asked for */
);


/*******************************************************************************
This function sets the value of an associative string array in the
Event Handler attached to the specified UF_MOM object.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_set_assoc_string_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to set */
   char         *index_name, /* <I> - the name of the index */
   char         *value       /* <I> - the value to set */
);


/*******************************************************************************
This function returns the value of an associative string array in the
Event Handler attached to the specified UF_MOM object.

Environment: Internal  and  External

See Also:

History: Originally released in V14.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_ask_assoc_string_array
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array to ask */
   char         *index_name, /* <I> - the name of the index */
   char        **value       /* <OF> - the value asked for */
);


/*******************************************************************************
This function execute a given command in the TCL Interpreter via Tcl_Eval

Environment: Internal  and  External

See Also:

History: Originally released in NX2
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_execute_command
(
   UF_MOM_id_t   mom,        /* <I> - the mom object */
   char         *command     /* <I> - the name of the command to be eval'ed */
);


/*******************************************************************************
This function returns the value of an element of a 2D double array in the Event
Handler attached to the specified UF_MOM object.

Environment: Internal  and  External

See Also:

History: Originally released in NX2.0
*******************************************************************************/
extern UFUNEXPORT int UF_MOM_ask_double_array_2d
(
   UF_MOM_id_t   mom,        /* <I> - the mom object that owns the array */
   char         *array_name, /* <I> - the name of the array */
   int           index1,     /* <I> - the first index */
   int           index2,     /* <I> - the second index */
   double       *value       /* <O> - the value */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif
