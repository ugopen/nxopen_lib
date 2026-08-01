/*===================================================================

        Copyright (c) 1998-1999 Unigraphics Solutions, Inc.
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This file is a sample shared library that is to be used in conjunction   *
 *   with ufd_load_library, and external routine. The external routine loads  *
 *   this shared library. Compile and link this file as an internal UG/Open   *
 *   API routine. Then compile and link ufd_load_library.c as an external     *
 *   UG/Open API routine.                                                     *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/


#include <stdio.h>
#include <ufd_load.h>

 /*****************************************************************
  *
  * A sample shared library to be loaded using UF_load_library.
  * If three or more arguments are passed, the first, second, and
  * third arguments should be the name of the library loaded, the
  * name of the function called, and a printf format string (taking
  * two string arguments) respectively.
  *
  * Example:
  *
  *     Given:
  *
  *         argc = 3;
  *
  *         argv[0] = "shlib_a"
  *         argv[1] = "ep_a"
  *         argv[2] = "Call to %s() in library %s succeeded."
  *
  *     ep_a( argc, argv );     yields:
  *
  *         Call to ep_a() in library shlib_a succeeded.
  *
  *         3 arguments passed.
  *
  *         argv[0] = "shlib_a"
  *         argv[1] = "ep_a"
  *         argv[2] = "Call to %s() in library %s succeeded."
  *
  *
  ***/

extern DllExport int ep_a(
    int   argc,
    char *argv[] )
{
    int indx;
    if( 3 <= argc )
        printf( argv[2], argv[1], argv[0] );

    printf( "\n\n%d arguments passed.\n\n", argc );

     /* Show each argument. */
    for( indx = 0; indx < argc; indx++ )
    {
        printf( "argv[%d] = \"%s\"\n", indx, argv[indx] );
    }

    printf( "\n" );

    return( 0 );
}

 /*****************************************************************
  *
  * This second entry point illustrates access to
  * multiple entry points in the same shared library using
  * UF_load_library. Each entry point must be looked up
  * individually with separate calls to UF_load_library; but,
  * the library is only loaded once (on locating the first entry
  * point).
  *
  ***/

extern DllExport int ep_b(
    int   argc,
    char *argv[] )
{
     /* Borrow ep_a to keep example terse. */
    return( ep_a( argc, argv ) );
}
