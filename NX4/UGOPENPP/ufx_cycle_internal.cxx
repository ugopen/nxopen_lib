/*
================================================================================

          Copyright (c) 1998 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    This file contains the internal Cycle example program.

================================================================================

*/

// ****************************************************************************
// Include files for needed types
// ****************************************************************************

#include <ufx_cycle.hxx>

#include <ug_info_window.hxx>
#include <ug_exception.hxx>
#include <ug_session.hxx>
#include <ug_part.hxx>

#include <uf_error_bases.h>
#include <uf_assem.h>
#include <uf_ui.h>

#if !defined(__sgi) && ! (defined(__hpux) && !defined(_HP_NAMESPACE_STD)) || defined(__GNUG__)
#include <iostream>
    using std::ostream;
    using std::cout;
    using std::endl;
#else
#include <iostream.h>
#endif

static void report_part ( );
static int  put_file_selection ( std::string *part_name );
static void menu ( int *response );

//  

// The entry point for the Internal UG/Open++ application 
// that generates a part report via the Cycle example class.
extern void ufusr ( char *param, int *retcod, int param_len )
{
    try 
    {        
        UgSession session ( true );   // Start a UG Session
        
        report_part ( );   
    }
    catch ( UgException &exception )  // Begin exception handling
    {
        cout << endl << "AN ERROR !!!!" << endl;
        cout << exception.askErrorText ( ).c_str() << endl << endl;
    }
}

static bool is_there_a_work_part ( void )
{
    try
    {
        UgSession::getWorkPart ( );
        
        return true;
    }
    catch ( UgException &exception )    // Catch no work part
    {         
        if ( UF_err_no_work_part != exception.askErrorCode ( ) )
        {
            throw;
        }
        
        return false;
    }
}

//
// Function Name: report_part
//
// Function Description:
//   Main driver for the part report functions.
//   If there is a work part, the user is
//   asked to choose between cycling the work
//   part or specifying another part file.
//
//   If there is no work part, the user is presented
//   with the part file selection dialog.
//
// Inputs:
//   None.
//
// Outputs:
//   Part reports to the listing device
//
static void report_part ( )
{
    int response = UF_UI_OK;

    do
    {
        if ( is_there_a_work_part ( ) )
        {
            menu ( &response );
        } 
        else 
        {
            std::string part_name;
            
            response = put_file_selection ( &part_name );
            
            if ( UF_UI_OK == response )
            {
                Cycle::askPartReport ( UgPart::open ( part_name ) );
            }
        }
    } while ( UF_UI_OK == response );
}

//
// Function Name: put_file_selection
//
// Function Description:
//   Displays the file selection dialog and gets a part name.
//
// Inputs:
//   None.
//
// Outputs:
//   part_name - part name from file selection dialog.
//
// Returns:
//   response - Back or cancel from file selection dialog.
//
static int put_file_selection ( std::string *part_name )
{  
    int response;
    int error;
    
    do
    {
        char          file_name [ MAX_FSPEC_SIZE + 1 ] = { '\0' };
        const logical use_display = FALSE;
        
        error = UF_UI_ask_open_part_filename ( file_name, const_cast < logical * > ( &use_display ), &response );
        
        if ( ( UF_UI_OK == response ) && ! error )
        {
            *part_name = file_name;
        }
        
        if ( ( UF_UI_CANCEL != response ) && error )
        {   
            cout << "Invalid Part Name or Part Not In This Directory. " << endl;
        }
    } while ( ( UF_UI_OK == response ) && error );
    
    return response;  
}

//
// Function Name: menu
//
// Function Description:
//   Displays a multiple menu dialog which offers the choice of cycling the work
//   part or a part specified from the file list dialog.
//
// Inputs:
//   None.
//
// Outputs:
//   response - Back, OK, or Cancel
//
// Returns:
//   None.
//
static void menu ( int *response )
{
    bool menu_choice;
    
    do
    {
        menu_choice = FALSE;
     
        const char *menu_title              = "Select Only One Option To Cycle";
        char        menu_items [ 2 ] [ 38 ] = { "Cycle Work Part", "Specify Part to Cycle" };
        const int   n_items                 = 2;
        int         select_array [ 2 ];

        int temp_return = uc1605 ( const_cast < char * > ( menu_title ), 0, menu_items, n_items, select_array );
       
        if ( 1 == temp_return )
        {
            *response = UF_UI_BACK;
        }
        else if ( 2 == temp_return )
        {
            *response = UF_UI_CANCEL;
        }
        else 
        {
            *response = UF_UI_OK;
            
            if ( select_array [ 0 ] == select_array [ 1 ] )  // No option selected
            {
                menu_choice = TRUE;

                uc1601 ( "Please select one option.", 1 );
            }
            else if ( 1 == select_array [ 0 ] )              // Cycle work part
            {             
                Cycle::askPartReport ( UgSession::getWorkPart ( ) );
            }
            else                                             // Specify a different part
            {
                std::string part_name;

                *response = put_file_selection ( &part_name );
                
                if ( UF_UI_OK == *response )
                {
                    tag_t part_tag = UF_PART_ask_part_tag ( ( char * ) part_name.c_str ( ) );
                    
                    if ( NULL_TAG == part_tag )
                    {
                        Cycle::askPartReport ( UgPart::open ( part_name ) );
                    }                    
                    else                                     // The specified part is already loaded
                    {    
                        Cycle::askPartReport ( dynamic_cast < UgPart * > ( UgObject::find ( part_tag ) ) );
                    }
                }
                
                menu_choice = ( UF_UI_CANCEL != *response );   
            }
        }
    } while ( menu_choice );    
}
