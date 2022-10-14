/*
================================================================================

          Copyright (c) 1998 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    This file contains the external Cycle example program.

================================================================================

*/

// ****************************************************************************
// Include files for needed types
// ****************************************************************************

#include <ufx_cycle.hxx>

#include <ug_exception.hxx>
#include <ug_session.hxx>
#include <ug_part.hxx>
#include <string.h>

#if !defined(__sgi) && ! (defined(__hpux) && !defined(_HP_NAMESPACE_STD)) || defined(__GNUG__)
#include <iostream>
    using std::cout;
    using std::endl;
#else
#include <iostream.h>
#endif
#include <uf_text.h>

static int get_args ( int argc, char **argv, char *part_name );

//
// Function Name: main
//
// Function Description:
//   The main for external User Function.
//
// Input:
//   argc - Argument count
//   argv - Pointers to character strings.
//
// Output: None.
//
// Returns:
//   0 - Indicates success.
//
extern int main ( int argc, char **argv )
{
    try                                   // Begin error protection
    {                                   
        int error;
        
        char part_name [  MAX_FSPEC_BUFSIZE ];
        
        error = get_args ( argc, argv, part_name );
        
        if ( ! error )
        {
            UgSession session ( true );   // Start a UG session
                                    
            // Generate report
                        
            Cycle::askPartReport ( UgPart::open ( part_name ) ); 

            return 0;
        }
        else
        {
            return 1;
        }
    }
    catch ( UgException &exception )      // Start of exception handler
    {
        cout << endl << "AN ERROR !!!!" << endl;
        cout << exception.askErrorText ( ).c_str ( ) << endl << endl;

        return 1;
    }
}

//
// Function Name: get_args
//
// Function Description:
//   Error checks that a part name was received as a command line argument
//   from main and that the part name is the correct length. Copies part
//   name into part_name.
//
// Input:
//   argc - Argument count from main.
//   argv - Pointers to string arguments from main.
//
// Output:
//   part_name - Part name character string from command line arguments.
//
// Returns:
//   0 - Indicates success. A part name was received.
//   1 - Indicates failure. Either the command line argument was missing
//        or the file name was too long.
//
static int get_args ( int argc, char **argv, char *part_name )
{
    int len = 0;
    if ( 2 != argc )
    {
        part_name [ 0 ] = '\0';

        cout << endl; 
        cout << "This program requires a part file name as input." << endl;
        cout << "The syntax for this program is as follows:" << endl;
        cout << argv [ 0 ] << " <part_name>" << endl;

        return 1;
    }
    else if ( ( UF_TEXT_count_characters ( argv[1] , &len ) != 0 ) || ( len > MAX_FSPEC_NCHARS ) )
    {
        cout << "File name is too long." << endl;

        return 1;
    } 
    else
    {  
        strcpy ( part_name, argv [ 1 ] );
        
        return 0;
    }
}
