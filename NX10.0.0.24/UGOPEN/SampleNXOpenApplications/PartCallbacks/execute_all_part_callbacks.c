/*****************************************************************************
                  Copyright (c) 2007 UGS Corp.
                      All rights reserved
******************************************************************************



    execute_all_part_callbacks.c

    This sample program works to invoke every possible
    part related callback.
        + Create New Part
        + Save Part As
        + Modify Part
        + Save Part
        + Close Part
        + Change Workpart
          (note the workpart changes automatically
          whenever parts are opened or closed)
        + Open Part
        + Rename Part
          (note rename part happens automatically
          whenever the part is 'saved as')

    This program will not register the callbacks for you!
    It is used to demo callbacks already registered by
    one of the following:
        + cpp_part_callbacks.cpp & cpp_part_callbacks.h
        + cs_part_callbacks.cs
        + java_part_callbacks.java
        + ufun_part_callbacks.c
        + vb_part_callbacks.vb
        + or any custom program you write
          with part related callbacks

    Note the path and filenames used in this demo are hard-coded.
    Please validate that the filenames used are valid on your machine
    or change them as needed before compiling this program.

    The default part names are:
        + c:\temp\part1_temp.prt
        + c:\temp\demo_part1.prt

    If you already have part files with those names at those locations
    on your machine the program will produce errors at runtime.
    You must delete the parts created at those locations between each
    time you run this demo program.

    After compiling and linking this file start NX and go to
    File->Execute->NX Open to run the demo.

*****************************************************************************/


/* Include files */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_modl.h>

#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))

static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133],
             msg[133];

        sprintf(msg, "*** ERROR code %d at line %d in %s:\n+++ ",
            irc, line, file);
        UF_get_fail_message(irc, err);

        UF_print_syslog(msg, FALSE);
        UF_print_syslog(err, FALSE);
        UF_print_syslog("\n", FALSE);
        UF_print_syslog(call, FALSE);
        UF_print_syslog(";\n", FALSE);

        if (!UF_UI_open_listing_window())
        {
            UF_UI_write_listing_window(msg);
            UF_UI_write_listing_window(err);
            UF_UI_write_listing_window("\n");
            UF_UI_write_listing_window(call);
            UF_UI_write_listing_window(";\n");
        }
    }

    return(irc);
}

/*
    run_part_demos()

    This function does all the work to execute the demos.

    Please validate that the filenames used are valid on your machine
    or change them as needed before compiling this program.

    The default part names are:
        * c:\temp\part1_temp.prt
        * c:\temp\demo_part1.prt

    If you already have part files with those names at those locations
    on your machine the program will produce errors at runtime.
    You must delete the parts created at those locations between each
    time you run this demo program.
*/
static void run_part_demos()
{
    tag_t part1 = NULL_TAG;
    char msg[256];
    double corner[3] = {0, 0, 0};
    char* edge_length[3] = {"100", "100", "100"};
    tag_t block = NULL_TAG;
    UF_PART_load_status_t load_status = {0};

    UF_UI_open_listing_window();
    sprintf( msg, "\nPreparing to create part...\n" );
    UF_UI_write_listing_window(msg);
    UF_PART_new( "c:\\temp\\part1_temp.prt", 1, &part1 );
    /* or on UNIX try:
    UF_PART_new( "/tmp/part1_temp.prt", 1, &part1 );
    */
    sprintf( msg, "Preparing to save part as...\n" );
    UF_UI_write_listing_window(msg);
    UF_CALL( UF_PART_save_as("c:\\temp\\demo_part1.prt") );
    /* or on UNIX try:
    UF_PART_new( "/tmp/demo_part1.prt", 1, &part1 );
    */
    sprintf( msg, "Preparing to modify part by creating block...\n" );
    UF_UI_write_listing_window(msg);
    UF_CALL( UF_MODL_create_block1(UF_NULLSIGN, corner, edge_length, &block ) );
    sprintf( msg, "Preparing to save and close part...\n" );
    UF_UI_write_listing_window(msg);
    UF_CALL( UF_PART_save() );
    UF_CALL( UF_PART_close( part1, 1, 1) );
    sprintf( msg, "Preparing to open part...\n" );
    UF_UI_write_listing_window(msg);
    UF_CALL( UF_PART_open( "c:\\temp\\demo_part1.prt", &part1, &load_status ) );
    /* or on UNIX try:
    UF_PART_new( "/tmp/demo_part1.prt", 1, &part1 );
    */

}


/*  Explicit Activation
**      This entry point is used to activate the application explicitly, as in
**      "File->Execute->NX Open" */
extern DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
    tag_t part_tag = NULL_TAG;



    /* Initialize the API environment */
    if( UF_CALL(UF_initialize()) )
    {
        /* Failed to initialize */
        return;
    }

    /* TODO: Add your application code here */
    run_part_demos();

    /* Terminate the API environment */
    UF_CALL(UF_terminate());
}


/*****************************************************************************
**  Utilities
*****************************************************************************/

/* Unload Handler
**     This function specifies when to unload your application from Unigraphics.
**     If your application registers a callback (from a MenuScript item or a
**     User Defined Object for example), this function MUST return
**     "UF_UNLOAD_UG_TERMINATE". */
extern int ufusr_ask_unload( void )
{
    return( UF_UNLOAD_UG_TERMINATE );
}

