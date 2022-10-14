/*===================================================================

        Copyright (c) 1998-1999 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_load_library                                                    *
 *         UF_unload_library                                                  *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following external UG/Open API program works in conjuction with      *
 *   with a shared library. The file for the shared library is                *
 *   ufd_example_shlib.c. Together, this file and the shared library demo the *
 *   UF_load_library and UF_unload_library UG/Open API functions. The program *
 *   allows the user to execute either of two functions defined in the        *
 *   ufd_example_shlib.c file, unload the library, or terminate the program.  *
 *   The program prompts the user for a selection which then executes. After  *
 *   execution, all options are displayed again. Compile and link this file   *
 *   as an external UG/Open API.                                              *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <ctype.h>
#include <stdio.h>
#include <uf.h>
#include <error_bases.h>

#define MAX_INPUT_SIZE  (8)  /* Larger than needed input buffer. */

typedef int (*XMPL_f_p_t)( int argc, char *argv[] );

 /*****************************************************************
 Please add the correct file extension for a particular platform as follows:
 HP - .sl
 Windows NT - .dll
 Digital Unix, IBM/AIX, SUN, SGI - .so
 */
#define XMPL_SHLIB    ("ufd_example_shlib")

#define XMPL_FNC_A    ("ep_a")
#define XMPL_FNC_B    ("ep_b")

 /*****************************************************************
  *
  * Loads a library and finds the function entry point specified by
  * the symbol name (sym), if necessary.  Calls the function with
  * supplied arguments and returns status.  The function pointer is
  * output for future use.
  *
  ***/

static int execute_lib(
  char       *lib,      /* I - Library Name.               */
  char       *sym,      /* I - Symbol Name.                */
  int         argc,     /* I - Argument Count.             */
  char       *argv[],   /* I - Arguments.                  */
  XMPL_f_p_t *fnc )     /* IO - Function Pointer for 'sym'.*/
{
    int error;

   /* Load library if necessary... */
  if( NULL == *fnc )
  {
      UF_load_f_p_t generic_fnc;

    if( !(error = UF_load_library( lib, sym, &generic_fnc )) )
    {
      *fnc = (XMPL_f_p_t) generic_fnc;
    }
    else      /* Library load failed... */
    {
         char message[133];

      UF_get_fail_message( error, message );
      fprintf( stderr,
        "ERROR: While loading \"%s\" (%s)...\n\t%s\n", lib, sym,
        message );
    }
  }
  else
    error = ERROR_OK;

   /* Execute function... */
  if( NULL != *fnc )
    error = (**fnc)( argc, argv );

  return( error );
}

 /*****************************************************************
  *
  * A simple program to demonstrate dynamic loading and
  * unloading of shared libraries using UF_load_library
  * and UF_unload_library.  The program allows the user
  * to select one of two libraries to load and execute,
  * unload both libraries, or terminate the program.  Target
  * function prototypes are expected to match the 'C' 'main'
  * prototype (i.e. int fnc(int argc, char *argv[])).
  *
  ***/

/*ARGSUSED*/
extern int main(
  int   argc,
  char *argv[] )
{
    int error;

  if( !(error = UF_initialize()) )
  {
      int done;

    done = 0;
    do
    {
        char input[MAX_INPUT_SIZE+1];

       /* Display user choices... */
      printf( "\n\n" );
      printf( " 1 - Load and execute \"%s\" function.\n",
        XMPL_FNC_A );
      printf( " 2 - Load and execute \"%s\" function.\n",
        XMPL_FNC_B );
      printf( " 3 - Unload libraries.\n" );
      printf( " 4 - Terminate.\n\n" );
      printf( "Enter selection: " );

       /* Get user selection. */
      fgets( input, sizeof(input), stdin );

      printf( "\n\n" );

       /* Selection must be a single digit. */
      if( isdigit(input[0]) && '\n' == input[1] )
      {
          static XMPL_f_p_t fnc_a = NULL;
          static XMPL_f_p_t fnc_b = NULL;

         /* Process selection... */
        switch( input[0] )
        {
          case '1':   /* Load and execute first function... */
          {
               char *xmpl_argv[] =
                 {
                   XMPL_SHLIB,  /* Library to load. */
                   XMPL_FNC_A,  /* Function to execute. */
                   "Called function ep_a in library ufd_example_shlib."
                 };
               int xmpl_argc = sizeof(xmpl_argv) /
                               sizeof(*xmpl_argv);

            error = execute_lib( xmpl_argv[0], xmpl_argv[1],
              xmpl_argc, xmpl_argv, &fnc_a );
          }
          break;

          case '2':   /* Load and execute second function... */
          {
               char *xmpl_argv[] =
                 {
                   XMPL_SHLIB,  /* Library to load. */
                   XMPL_FNC_B,  /* Function to execute. */
                   "Called function ep_b in library ufd_example_shlib."
                 };
               int xmpl_argc = sizeof(xmpl_argv) /
                               sizeof(*xmpl_argv);

            error = execute_lib( xmpl_argv[0], xmpl_argv[1],
              xmpl_argc, xmpl_argv, &fnc_b );
          }
          break;

          case '3':   /* Unload library... */
            UF_unload_library( XMPL_SHLIB );
            fnc_a = NULL;
            fnc_b = NULL;
          break;

          case '4':   /* Finished - set termination flag. */
            done = 1;
          break;

          default:    /* Input character is out of range... */
            fprintf( stderr, "\nERROR: Invalid selection.\n" );
            break;
        }
      }
      else
        fprintf( stderr, "\nERROR: Select with digit only.\n" );

    } while( !done && !error );

    UF_terminate();
  }
  else
  {
       char message[133];

    UF_get_fail_message( error, message );
    fprintf( stderr, "ERROR: %s\n", message );
  }

  return( 0 );
}
