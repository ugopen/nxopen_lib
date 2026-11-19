/*============================================================================

                    Copyright (c) 2000 Unigraphics Solutions
                       Unpublished - All rights reserved
==============================================================================
File description:

This is a sample UG/Routing callback program. The UG/Routing module allows
you to define an internal UG/Open program to be invoked at the conclusion
of various interactive functions within UG/Routing. Currently, these 
functions are:

Place Part
Move Part
Remove Part
Transform Path
Delete Path
Assign Stock

We refer to customer supplied functions invoked at the conclusion of
the Routing function as "callbacks".

To define a callback for one of the UG/Routing functions, modify your
Application View file (.apv) to include a CALLBACKS section. Shown below
is a sample:

CALLBACKS "Assign Stock" 
handle_cb libbates.so
END_OF_CALLBACKS

The above CALLBACKS description tells UG/Routing to execute a user callback
function after the UG/Routing Assign Stock function completes. UG/Routing
will try to load the shared library (DLL), libbates.so, and then invoke the 
"handle_cb" entry point within that shared library (DLL). It will call the
function with a single argument which is a pointer to a structure of type 
UF_ROUTE_cb_data_s (defined in uf_route.h).

struct UF_ROUTE_cb_data_s
{
    int reason;
    int num_objects;
    tag_t *objects;
};

The "reason" code will be one of the UF_ROUTE_CB_REASON_{xxx} values defined
in uf_route.h, indicating which UG/Routing function just completed. The 
"num_objects" and "objects" variables are the count and the tags of the
objects involved in the function. For example, for the 
UF_ROUTE_CB_REASON_PLACE_PART callback, the "objects" will be the tags of
the part occurrences of the just placed parts.

Note that the same function / library can be specified to handle different 
callbacks and that more than one callback function / library can be specified 
for a given reason. In the latter case, the different functions will be 
executed in the order in which they are listed in the CALLBACKS entry 
for that reason.

This sample program uses a "C" switch statement based on the reason code, so
that it could be used to perform callback functions for more than one
UG/Routing function. To define callbacks for different reason codes, you 
must have separate CALLBACKS entries. 

Note that the UGII_SHARE environment variable is used to determine the
paths to be searched to locate the libraries referenced by the CALLBACKS
entries.

==============================================================================
 
=============================================================================*/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_route.h> 
#include <uf_ui_ugopen.h>
#include <ufd_route_sample.h> 

#define LINESIZE 120

static  void print_objects( char *reason_text, int num, tag_t *tags )
{
    char    buf[2*LINESIZE+1];
    char    tags_line[] = "Tags:   ";
    char    none_line[] = "        ";
    int     len,i;

    sprintf( buf, "\nCallback function invoked: %s\n", reason_text );
    UF_UI_write_listing_window( buf );
    if  ( num > 0 )
    {
        sprintf( buf, "Number of Objects = %d\n", num );
        UF_UI_write_listing_window( buf );
        strcpy( buf, tags_line );
        len = strlen(buf);
        for ( i=0 ; i<num  ; i++ )
        {
            if  ( len + 8 > LINESIZE )
            {
                strcat( buf, "\n" );
                UF_UI_write_listing_window( buf );
                strcpy( buf, none_line );
                len = strlen(buf );
            }
            sprintf( &buf[len], "%8d", tags[i] );
            len = strlen( buf );
        }
        if  ( len > strlen( none_line ) )
        {
            strcat( buf, "\n" );
            UF_UI_write_listing_window( buf );
        }
    }
}

#ifdef __cplusplus
extern "C" {
#endif

extern void DllExport handle_cb( UF_ROUTE_cb_data_p_t callback )
{
    UF_initialize();
    UF_UI_open_listing_window();

    switch ( callback->reason )
    {
      case UF_ROUTE_CB_REASON_PLACE_PART:
        print_objects( "Place Part", 
                       callback->num_objects, callback->objects );
        break;

      case UF_ROUTE_CB_REASON_MOVE_PART:
        break;

      case UF_ROUTE_CB_REASON_REMOVE_PART:
        break;

      case UF_ROUTE_CB_REASON_DELETE_PATH:
        break;

      case UF_ROUTE_CB_REASON_TRANSFORM_PATH:
        break;

      case UF_ROUTE_CB_REASON_OFFSET_PATH:
        break;

      case UF_ROUTE_CB_REASON_ASSIGN_STOCK:
        print_objects( "Assign Stock", 
                       callback->num_objects, callback->objects );
        break;

      default:
        break;
    }

    UF_UI_close_listing_window();
    UF_terminate();
}
#ifdef __cplusplus
}
#endif
