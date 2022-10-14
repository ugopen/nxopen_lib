/*
================================================================================

          Copyright (c) 1998 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    This source file includes the code that is used by both the internal and
    external versions of the "Cycle the Data Model" program. It does all the
    work of getting the part file history, cycling the data Model, and printing
    a report on its results.

================================================================================

*/

// ****************************************************************************
// Include files for needed types
// ****************************************************************************

#include <ufx_cycle.hxx>

#include <ug_displayable.hxx>
#include <ug_info_window.hxx>
#include <ug_exception.hxx>
#include <ug_iterator.hxx>
#include <ug_string.hxx>
#include <ug_vector.hxx>

#include <uf_object_types.h>
#include <uf_error_bases.h>
#include <uf_ui.h>

#include <stdio.h>
#include <time.h>

#if !defined(__sgi) && ! (defined(__hpux) && !defined(_HP_NAMESPACE_STD)) || defined(__GNUG__)
#   include <iostream>
    using std::ostream;
    using std::cout;
    using std::endl;
#   include <strstream>
    using std::ostrstream;
    using std::ends;
#else
#   include <strstream.h>
#   include <iostream.h>
#endif

// ****************************************************************************
// Class implementation for Cycle
// ****************************************************************************

Cycle::Cycle ( )
{
} 

Cycle::~Cycle ( ) 
{
}
        
// Prints the part report to the info window.

void Cycle::askPartReport ( const UgPart *part )
{
    try
    {
        UgInfoWindow::open ( );

        Cycle::askHistoryReport ( part );
        Cycle::askAttributeReport ( part );
        Cycle::askCustomerReport ( part );
        Cycle::askObjectReport ( part );
    }
    catch ( UgException &exception )
    {
        cout << "============================================" << endl;
        cout << "== Exception encountered in askPartReport ==" << endl;
        cout << "== " << exception.askErrorText ( ).c_str()    << endl;
        cout << "============================================" << endl;

        throw;
    }
} 
        
// Prints the part history report to the info window.

void Cycle::askHistoryReport ( const UgPart *part )
{
    ostrstream               buffer;
    const std::string           part_name    = part->getFullName ( );
    UF_PART_history_list_p_t history_list = NULL;
    int                      n_histories;
     
    // Print out the part units
    
    if ( part->isInches ( ) )
    {
        buffer << "This part is in inches" << endl;
    }
 
    if ( part->isMillimeters ( ) )
    {
        buffer << "This part is in millimeters" << endl;
    }

    buffer << endl << endl;

    // Get the full partfile name and print it 
    
    buffer << "Part History for part: " << part_name.c_str ( ) << endl;

    buffer << endl;

    buffer << "Version  Time/Date        Machine  User                  Program" << endl;
    buffer << "-------  ---------------  -------  ----                  -------" << endl;
    
    // Get the part history 
    
    UF_PART_create_history_list ( &history_list );
    UF_PART_clear_history_list ( history_list );
    UF_PART_ask_part_history ( part->getTag ( ), history_list );
    UF_PART_ask_num_histories ( history_list, &n_histories );
    
    for ( int current_history = 0; current_history < n_histories; current_history++ )
    {
        char *program;
        char *user;
        char *machine;
        int   version_number;
        int   version_time;
        
        UF_PART_ask_nth_history ( history_list, current_history, &program, &user, &machine, &version_number, &version_time );

        time_t     displayed_time;
        struct tm *time_ptr;
        char       t_buffer [ UF_UI_MAX_STRING_LEN + 1 ];
        char       time_buffer [ 21 ];
        
        displayed_time = ( time_t ) version_time;
        
        time_ptr = localtime ( &displayed_time );
        
        strftime ( time_buffer, sizeof ( time_buffer ), "%d %b %y %H:%M", time_ptr );
        
        sprintf ( t_buffer, "%7d  %-15.15s  %-7.7s  %-20.20s  %s", version_number, time_buffer, machine, user, program );

        buffer << t_buffer << endl;
    }
    
    UF_PART_delete_history_list ( history_list );

    buffer << endl << endl << ends;
    
    UgInfoWindow::write ( std::string ( buffer.str ( ) ) );
    delete buffer.str ( );  
}

// Prints the part attribute report to the info window.

void Cycle::askAttributeReport ( const UgPart *part )
{
    ostrstream buffer;
  
    try
    {
        const std::vector < std::string > titles = part->askStringAttributeTitles ( );
        
        for ( int i = 0; i < titles.size ( ); i++ )
        {
            if ( 0 == i )
            {
                const std::string part_name = part->getFullName ( );
                
                buffer << "Part Attributes for part: " << part_name.c_str ( ) << endl;
                buffer << "-------------------------" << endl;
            }
            
            std::string value = part->getStringAttributeValue ( titles [ i ] );
            
            buffer << "Title: " << titles [ i ].c_str ( ) << " ";
            buffer << "Value: " << value.c_str ( ) << endl;
        }
        
        if ( 0 == titles.size ( ) )
        {
            buffer << "No part attributes found" << endl;
        }
    }
    catch ( UgException &exception )
    {
        cout << "============================================" << endl;
        cout << "== Exception encountered in askAttrReport ==" << endl;
        cout << "== " << exception.askErrorText ( ).c_str()    << endl;
        cout << "============================================" << endl;
        
        throw;
    }

    buffer << endl << endl << ends;

    UgInfoWindow::write ( std::string ( buffer.str ( ) ) );
    delete buffer.str ( );
}
        
// Prints the part status, customer area and description report to the info window.

void Cycle::askCustomerReport ( const UgPart *part )
{
    ostrstream buffer;

    buffer << "The Customer status is: " << part->getStatus ( ) << endl;
    buffer << endl;

    const std::string cust_area = part->getCustomerArea ( );

    if ( cust_area.empty ( ) )
    {
         buffer << "The Customer area is not defined." << endl;
    }
    else
    {
         buffer << "The Customer area is: " << cust_area.c_str ( ) << endl;
    }

    buffer << endl;

    const std::string description = part->getDescription ( );

    if ( description.empty ( ) )
    {
         buffer << "The Customer description is not defined." << endl;
    }
    else
    {
        buffer << "The Customer description is: " << description.c_str ( ) << endl;
    }    
    
    buffer << endl << endl << ends;

    UgInfoWindow::write ( std::string ( buffer.str ( ) ) );
    delete buffer.str ( );
}
        
// Prints the part object report by type and by layer to the info window.

void Cycle::askObjectReport ( const UgPart *part )
{
    int i;

    int n_displayable = 0;
    int n_alive       = 0;
    int n_condemned   = 0;

    std::vector < int > n_objects_by_type ( UF_max_entity_type );
    std::vector < int > n_objects_by_layer ( 256 ); 

    ostrstream buffer;
    
    for ( UgTypedObject *typed_object = part->iterateFirst ( ); 
          typed_object; 
          typed_object = part->iterateNext ( typed_object ) )
    {        
        const UgDisplayableObject *displayable_object = dynamic_cast < UgDisplayableObject * > ( typed_object );
        
        if ( 0 != displayable_object )
        {
            n_displayable++;
        }

        if ( typed_object->isAlive( ) )
        {
            n_alive++;
        }

        if ( typed_object->isCondemned ( ) )
        {
            n_condemned++;
        }    
        
        n_objects_by_type [ typed_object->askType ( ) - 1 ]++;

        if ( 0 != displayable_object )
        {
            const int layer_number = displayable_object->getLayer ( );

            if ( ( layer_number > 0 ) && ( layer_number < 257 ) )
            {
                n_objects_by_layer [ layer_number - 1 ]++;
            }
        }
    } 
    
    // Print out the number of objects by type
    
    buffer << "Object Type       Count of Objects" << endl;
    buffer << "-----------       ----------------" << endl;
    
    for ( i = 0; i < n_objects_by_type.size ( ); i++ )
    {
        if ( 0 != n_objects_by_type [ i ] )
        {
            buffer.width ( 5 );
            buffer << i + 1 << "              " ;

            buffer.width ( 5 );
            buffer << n_objects_by_type [ i ] << endl;
        }
    }
        
    buffer << endl << endl;
    
    // Print out the object information including
    // The number of displayable objects
    // The number of alive objects
    // The number of condemned objects
    // The total count of objects in this part
   
    buffer << "Displayable objects: "; 
    buffer.width ( 10 );
    buffer << n_displayable << endl;

    buffer << "Alive objects:       ";
    buffer.width ( 10 );   
    buffer << n_alive << endl;

    buffer << "Condemned objects:   "; 
    buffer.width ( 10 );    
    buffer << n_condemned << endl;

    buffer << "Total objects:       ";
    buffer.width ( 10 );  
    buffer << n_alive + n_condemned << endl;

    buffer << endl << endl;

    // Print out the number of objects by layer
    
    buffer << "The following is the object count by layer."                   << endl;
    buffer << "Only layers containing objects will be listed."                << endl;
    buffer << "Note that this count does not include internal system layers." << endl;

    buffer << endl;

    buffer << "Layer       Count of Objects" << endl;
    buffer << "-----       ----------------" << endl;
    
    for ( i = 0; i < n_objects_by_layer.size ( ); i++ ) 
    {
        if ( 0 != n_objects_by_layer [ i ] )
        {
            buffer.width ( 5 );
            buffer << i + 1 << "           ";

            buffer.width ( 5 );
            buffer << n_objects_by_layer [ i ] << endl;
        }
    }

    buffer << endl << endl << ends;

    UgInfoWindow::write ( std::string ( buffer.str ( ) ) );
    delete buffer.str ( );
}
