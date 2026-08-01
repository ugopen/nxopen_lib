/*******************************************************************************
             Copyright (c) 2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved

 *

File Description :
   Open API general interface for use in only internal Open API programs.  These
   are general purpose functions that will be common to most Open API programs,
   as well as specialized functions that do not belong to any of the other
   interfaces.

***************************************************************************/

#ifndef UF_UGOPENINT_INCLUDED
#define UF_UGOPENINT_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libugopenint_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/* return values for ufusr_ask_unload */
#define  UF_UNLOAD_IMMEDIATELY         1
#define  UF_UNLOAD_SEL_DIALOG          2
#define  UF_UNLOAD_UG_TERMINATE        3

/*****************************************************************************
 * Internal Open API Entry Point.
 *
 * You use ufusr as a main function entry point for all Internal Open API
 * programs. The ufusr function may also be used for user exits.
 *
 * For internal programs written in C, a third argument needs to be
 * passed into the "ufusr" function. This third variable is the length of the
 * character array param.
 *
 * Return: void
 *
 * Environment: Internal
 *
 * See Also:  ufusr_ask_unload
 *           See the discussion on user exits in  uf_exit.h
 *           
 *
 * History:
*****************************************************************************/
extern DllExport void ufusr (
    char   *param  ,         /* <I>
                   If this function is called from menuscript,
                   this argument will contain the name of the menu
                   button selected.  Otherwise this argument is unused.
                */
    int    *retcod ,        /* <O>
                   Return Code.  Not used by Internal
                   Open API.
                */
    int     param_len       /* <I>
                   Length of 'param' Argument.
                   NX handles this input for you.
                */
);

/*****************************************************************************
 * User supplied routine to specify how an Internal Open API shared image
 * is handled upon exit.  This function gives you the capability to unload an
 * internal Open API or user exit from NX. You can
 * specify any one of the three constants as a return value to
 * determine the type of unload to perform: immediately after Open
 * API execution, via an unload selection dialog, or when NX
 * terminates.
 *
 * If you choose UF_UNLOAD_SEL_DIALOG, then you have the option to unload
 * your image by selecting File--Utilities--Unload Shared Image.
 *
 * Please note the following restrictions:
 * A program which uses UF_UI_append_menubar_menu should not
 * use the option to unload an Open API image. Additionally, if
 * your code which defines UF_UI_append_menubar_menu itself
 * loads a shared library, this code should not attempt to unload the
 * library. NX always makes a strong attempt to prevent
 * unloading a library which was coded by using UF_UI_append_menubar_menu.
 *
 * A shared library that contains registered functions, such as any of
 * the User Defined Object registration methods, should not be
 * unloaded. NX must keep the library loaded to access the
 * address of the registered function.
 *
 * Unload immediately and Unload via dialog should not be used if the 
 * program has registered any sort of callbacks.
 *
 * Additionally, you have the option of coding the cleanup routine
 * ufusr_cleanup to perform any house keeping chores that may need
 * to be performed. If you code the cleanup routine it is automatically
 * called by NX.
 *
 * Return:
 *       UF_UNLOAD_IMMEDIATELY - unload immediately after Open API executes
 *       UF_UNLOAD_SEL_DIALOG - via an unload selection dialog
 *       UF_UNLOAD_UG_TERMINATE - when NX terminates
 *
 * Environment: Internal
 *
 * See Also:  ufusr
 *           
 *
 * History:
*****************************************************************************/
extern DllExport int ufusr_ask_unload (
    void
);

/*****************************************************************************
 * User supplied routine to clean up before the user function program is
 * unloaded.
 *
 * NX calls this entry point if it is defined in your source code.
 * The entry point is called immediately before a shared library is
 * unloaded and allows you to perform any cleanup tasks that must be
 * performed within NX. For example, if your internal program
 * opened up a database program you could use the call to
 * ufusr_cleanup as an opportunity to close any open database files
 * before the image is unloaded.
 *
 * NOTE: You use ufusr_cleanup in conjunction with ufusr_ask_unload.
 * If you code ufusr_cleanup without defining ufusr_ask_unload, then
 * the ufusr_cleanup entry point is ignored.
 *
 * Return: void
 *
 * Environment: Internal
 *
 * See Also: 
 *
 * History:
*****************************************************************************/
extern DllExport void ufusr_cleanup (
    void
);

/* -------------------------------------------------------------------------- *
 *             User Function Calling GRIP, And Argument Sharing               *
 * -------------------------------------------------------------------------- */

/* Argument types that are valid in the variable length argument lists */

#define  UF_TYPE_DOUBLE         1   /* Used to pass a single variable of
                                       type double. */
#define  UF_TYPE_DOUBLE_ARRAY   3   /* Used to pass an array of type double. */
#define  UF_TYPE_TAG_T          5   /* Used to pass a single object identifier*/
#define  UF_TYPE_TAG_T_ARRAY    7   /* Used to pass an array of object
                                       identifiers. */
#define  UF_TYPE_CHAR           9   /* Used to pass a single character string.*/
#define  UF_TYPE_CHAR_ARRAY    11   /* Used to pass an array of character
                                       strings. */

/* Structure definition for the variable length argument lists */

struct UF_args_s
{   int   type;            /* one of the types, UF_TYPE_DOUBLE,
                                   UF_TYPE_DOUBLE_ARRAY, UF_TYPE_TAG_T,
                                   UF_TYPE_TAG_T_ARRAY, UF_TYPE_CHAR or
                                   UF_TYPE_CHAR_ARRAY. */
    int   length;        /* the number of elements in an array, for
                                   types UF_TYPE_DOUBLE_ARRAY,
                                   UF_TYPE_TAG_T_ARRAY or UF_TYPE_CHAR_ARRAY. */
    void  *address;        /* A pointer to an array of the given
                                   type and length.  Note that for an array
                                   of UF_TYPE_CHAR, if the argument list
                                   is built by the Open program, it must
                                   initialize this array whether it is input or
                                   output.  An output array can be initialized
                                   by setting the first byte to '\0'.  */
};

typedef struct UF_args_s UF_args_t, *UF_args_p_t;

/**************************************************************************
 * This routine is used to receive arguments from a grip program.  The
 * grip program sets up these arguments with the GRIP command, GRARGS.
 * The GRIP program then invokes execution of the internal Open API program
 * with the GRIP XSPAWN command. The Open API program, during execution,
 * maintains complete control of the system including any interactive
 * statements or error messages.
 *
 * To receive the arguments from GRIP, define the structure, UF_args_s, that
 * describes the arguments to share with the GRIP program. This definition
 * must match the definition supplied to the GRIP GRARGS command so that the
 * contents of the GRIP variables can be copied to the contents of the Open
 * API variables.
 *
 * Please note the following limitations:
 *    . The GRARGS command is limited to 103 arguments.
 *    . The size of character strings input to UF_ask_grip_args should be
 *      declared to the largest GRIP string (132 characters) plus a null
 *      character or 133 characters.
 *    . Calls cannot be nested. For example, a sequence where GRIP XPAWNs an
 *      internal Open API program which uses UF_call_grip to execute GRIP,
 *      and anything similar, is not allowed.
 *
 * Environment: Internal
 *
 * See Also: 
 *
 * History:
 ****************************************************************************/
extern UGOPENINTEXPORT int UF_ask_grip_args (
    int argument_count,        /* <I>
                                Count of arguments from GRIP executable
                                */
    UF_args_p_t gruf_arg_list    /* <I/O>
                                The data arguments from GRIP. An array of
                                structures where each element in the array is
                                a structure that contains an arguments type,
                                size, and address.  The actual values will
                                be modified by this call.
                                */
); /* <RETIRE_NXOPEN> */

/**************************************************************************
 * Updates the contents of the matching GRIP argument list with the
 * contents of the Open API addresses.  This is used to return data
 * to the GRIP program.
 *
 * Environment: Internal
 *
 * See Also:
 *
 * History:
 ****************************************************************************/
extern UGOPENINTEXPORT int UF_set_grip_args (
    int argument_count,        /* <I>
                                Count of arguments to set in GRIP.
                                */
    UF_args_p_t gruf_arg_list    /* <I,len:argument_count>
                                The arguments to set in GRIP. An array of
                                structures where each element in the array is
                                a structure that contains an arguments type,
                                size, and address.
                                */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_UGOPENINT_INCLUDED */
