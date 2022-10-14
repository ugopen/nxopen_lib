/*

===========================================================================
        Copyright (c) 2004 UGS PLM Solutions
          Unpublished - All Rights Reserved
===========================================================================

Program to cycle the drawings of a part and generate an HPGL plot for each
  
This program uses the Plotting functions available in NX3 (and later) to
generate HPGL output for each drawing of one or more parts. The part names
are supplied as command line arguments or via the stdin stream. Sample
usage:

    ufd_plot_drawings_hpgl v18_draw_00.prt d:\someloc\v17_draw.prt

    find parts_dir -name '*.prt' | ufd_plot_drawings_hpgl -

The program assumes that a printer named "HPGL" has been defined using the
NX Plot Administration tools. This printer should be defined as a "Render
File Then Execute" queue. Such a queue generates a temporary HPGL file
and then invokes a user supplied script to move or rename the temporary file
to a permanent file (or to do any other processing that the script desires).

A sample Perl script suitable for use with a "Render File Then Execute" queue
is provided as part of the NX Open kit, move_hpgl.pl. The script has directions
for defining the HPGL printer.

The script depends upon an environment variable, MOVE_HPGL_OUTPUT_DIR, being
defined which specifies the directory to which the generated HPGL files should
be moved. Messages about each file processed are written to A log file,
move_hpgl.log, located in the user's home directory. You must set the variable
before executing the program (or modify the program to set it).

The processing of this program is fairly simple.

 1) Check to see that a printer named HPGL has been defined. Exit if not.
 2) Check to see that environment variable PLOT_HPGL_OUTPUT_DIR has been
    defined. Exit if not.
 3) Process each command line argument: If the name is "-", read stdin for file
    names else use the argument as the file name.

    Open the part
    Cycle the drawings
      Generate a CGM file
      Print the CGM file to the HPGL printer
    Close the part file



*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <uf_defs.h>
#include <uf.h>
#include <uf_cfi_types.h>
#include <uf_draw.h>
#include <uf_obj.h>
#include <uf_obj_types.h>
#include <uf_part.h>
#include <uf_plot.h>

#define LOCAL_BUFSIZE   1025
#define CLOSE_ALL             1
#define CLOSE_UNCONDITIONALLY 1
#define HPGL_PRINTER_NAME "HPGL"
#define HPGL_PROFILE_NAME "<System Profile>"
#define HPGL_OUTPUT_DIR   "PLOT_HPGL_OUTPUT_DIR"

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
    }

    return(irc);
}

/*
    We need a full file spec for the name of the CGM to pass to the print
    routine. This routine generates the beginning of that spec by combining
    the current directory with the part file name up to the .prt. It appends
    an underscore to that result. This may then be combined with the drawing
    name and a .cgm extension to complete the file spec.
*/
static char * get_base_name( const char *part_name )
{
    char   *base_name;
    char    dir_name[ MAX_FSPEC_BUFSIZE ];
    char   *ext_loc = NULL;
    char    separator[] = "_";
    char   part_dir[ MAX_FSPEC_BUFSIZE ];
    char   leaf_name[ MAX_FSPEC_BUFSIZE ];

    uc4565( 1, dir_name );
    uc4576( part_name, 2, part_dir, leaf_name );
    base_name = (char *) malloc(  MAX_FSPEC_BUFSIZE * sizeof(char) );
    
    if(base_name != NULL)
    {
        uc4575( dir_name, 2, leaf_name, base_name );
        ext_loc = strrchr( base_name, '.' );
    
        if  ( ext_loc )
            *ext_loc = '\0';
   
        strcat( base_name, separator );
    }
    return base_name;
}

static  void process_drawings( const char *part_name )
{
    int     num, i;
    tag_p_t drawings;
    char    drawing_name[ UF_OBJ_NAME_BUFSIZE ];
    char   *job_name;
    char   *base_name;
    char   *cgm_name;
    char    extension[] = ".cgm";

    cgm_name = NULL;
    base_name = get_base_name( part_name );
    UF_CALL( UF_DRAW_ask_drawings( &num, &drawings ) );
    for ( i=0 ; i < num ; i++ )
    {
        UF_CALL( UF_OBJ_ask_name( drawings[i], drawing_name ) );
        printf("  Drawing %s\n", drawing_name );
        UF_CALL( UF_PLOT_ask_default_job_name( drawings[i], &job_name ) );
        cgm_name = (char *) realloc( cgm_name, strlen(base_name)+
                                               strlen(drawing_name)+
                                               strlen(extension)+1 );
        if(cgm_name != NULL)
        {
            strcpy( cgm_name, base_name );
            strcat( cgm_name, drawing_name );
            strcat( cgm_name, extension );
        }
        UF_CALL( UF_PLOT_save_cgm( drawings[i], NULL, job_name,
                                   NULL, cgm_name ) );
/*
    NOTE that cgm_name must be a full file spec.
*/
        UF_CALL( UF_PLOT_print_file( cgm_name, HPGL_PRINTER_NAME,
                                     HPGL_PROFILE_NAME, 1 ) );
        uc4561( cgm_name, 0 );
        UF_free( job_name );
    }

    free( base_name );
    if  ( cgm_name )
        free( cgm_name );

    UF_free( drawings );
}

static  void usage( void )
{
    printf( 

"\nGenerates HPGL plot files for the drawings in the part files supplied as\n"
"arguments to the command line.\n\n"

    );

    printf(

"Part file names can be supplied as arguments on the command line. The special\n"
"name \"-\" indicates that standard input should be read and each line taken as a\n"
"part name to process. Example usages:\n"
"    ufd_plot_drawings_hpgl v17_part_00.prt v18_part_01.prt\n"
"    ls somedirectory/* | ufd_plot_drawings_hpgl - \n"
    );
}

static  void process_part( const char *name )
{
    int                     err;
    char                    msg[133];
    tag_t                   part;
    UF_PART_load_status_t   load_status;

    err = UF_PART_open( name, &part, &load_status );
    if  ( err )
    {
        UF_get_fail_message( err, msg );
        printf( "Unable to open part %s\n%s\n", name, msg );
        UF_free_string_array( load_status.n_parts, load_status.file_names );
        UF_free( load_status.statuses );
        return;
    }

    printf("Part %s\n", name );
    process_drawings( name );

    UF_CALL( UF_PART_close( part, CLOSE_ALL, CLOSE_UNCONDITIONALLY ) );
}

static int check_hpgl_printer( void )
{
    int     result;
    int     i, num;
    char  **printers;

    UF_CALL( UF_PLOT_ask_printer_names( &num, &printers ) );
    for ( result=0,i=0; i < num; i++ )
    {
        if  ( strcmp( printers[i], HPGL_PRINTER_NAME ) == 0 )
        {
            result = 1;
            break;
        }
    }
    UF_free( printers );
    return result;
}

static int check_hpgl_output_dir( void )
{
    int     result;
    
    result = getenv( HPGL_OUTPUT_DIR ) ? 1 : 0;
    return result;
}

int main(int argc,char *argv[])
{
    int     irc;

    if  ( argc == 1 )
    {
        usage();
        return 0;
    }

    irc = UF_initialize();

    if ( irc != 0 ) {
        fprintf(stderr,"++ error initializing system - irc = %d\n",irc);
        fprintf(stderr,"   ***** aborting execution *****\n" );
        return(1);
    }

    if  ( ! check_hpgl_printer() )
    {
        fprintf( stderr, "Printer named " HPGL_PRINTER_NAME " is not defined.\n" );
        fprintf( stderr, "Please define this and rerun.\n" );
        return(1);
    }

    if  ( ! check_hpgl_output_dir() )
    {
        fprintf( stderr, "Environment variable " HPGL_OUTPUT_DIR " is not defined.\n" );
        fprintf( stderr, "Please define this and rerun.\n" );
        return(1);
    }

    while ( --argc )
    {
        char   *filename = *++argv;

        if  ( ! strcmp( filename, "-" ) )
        {
            char    line[LOCAL_BUFSIZE];

            while ( fgets( line, sizeof(line), stdin ) )
            {
                process_part( line );
            }
        }
        else
        {
            process_part( filename );
        }
    }

    UF_terminate();
    return 0;
}
