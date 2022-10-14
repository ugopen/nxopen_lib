/*===================================================================

        Copyright (c) 1999, 2000 Unigraphics Solutions Corporation
                      2001, 2002 UGS
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_MODL_ask_vda_4955_compliance                                    *
 *                                                                            *
 *   The example should demonstrate the use of this function for checking     *
 *   parts with VDA Checker in an external batch run ( without user           *
 *   intervention ).                                                          *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example is executed as command line:                       *
 *                                                                            *
 *   ufd_vda_ext_example <optional RequestListFile>                           *
 *                                                                            *
 *   If the <optional request list file> parameter is omitted,                *
 *   the default "check_vda_compliance.lst" is used as RequestListFile.       *
 *   Each batch run of UF_MODL_ask_vda_4955_compliance requires a             *
 *   part file and configuration file.                                        *
 *   The RequestListFile is used to define part/configuration file pairs.     *
 *                                                                            *
 *     <PATH>/first.prt                                                       *
 *     <PATH>/first.cfg                                                       *
 *     <PATH>/second.prt                                                      *
 *     <PATH>/second.cfg                                                      *
 *     .                                                                      *
 *     .                                                                      *
 *   Each file is specified on a separate line.                               *
 *   An empty line or end of file immediately terminates the whole run        *      
 *                                                                            *
 *   NOTE:                                                                    * 
 *   Text file lines must not exceed length of 132 characters.                *
 *   Use the correct delimiters ( UNIX: /   NT: \ ).                          *
 *                                                                            *
 *   The *.cfg are names of VDA Checker configuration files, which must be    *
 *   created by running the VDA Checker in interactive mode:                  *
 *     Analysis-->Check VDA-4955 Compliance                                   *
 *                                                                            *
 *   The checking results will be written to *.log and *.ceo files            *
 *   ( Their names will be derived from the corresponding part file name ).   *
 *   The *.ceo files contain the session independent compliance error data    *
 *   and can be used to verify the results by reloading them during a         *
 *   subsequent interactive session.                                          *
 *                                                                            *
 
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_modl.h>
#include <uf_modl_vdac.h>
#include <uf_ui.h>
#include <uf_cfi.h>

/* end of file */
#define ERREOF  (-23)

typedef char ufd_path[  MAX_FSPEC_BUFSIZE];
typedef char ufd_msg[ 2 *  MAX_FSPEC_BUFSIZE];

/* prototypes of local routines */
static void error_list( char *msg );

/* when we encounter an error. an error message is displayed  */
static void error_list( char *msg )
{
    fprintf( stderr, ": %s.\n",msg );
}

extern int main( int argc, char **argv )
{
    char*                   batchFile;
    UF_PART_load_status_t   openStatus; /* open part status */
    tag_t                   inputPartTag = NULL_TAG;
    ufd_path                inputConfig, inputPart;
    ufd_msg                 message;
    int     channel;
    int     mode = 1;       /* READ */
    int     type = 2004;    /* NATIVE + TEXT */
    int     ret = 0;
    int     error = 0;
  
    /*
    Initialize user functions
    */
    if ( (ret = UF_initialize()) )
    {
        error_list( "Error in UF_initialize" );
        UF_get_fail_message( ret, message );
        error_list( message );
        return 0;
    }
    /*
    Open RequestListFile
    */
    if ( argc < 2 )
        batchFile = "check_vda_compliance.lst";
    else
        batchFile = argv[1];

    if ( (channel = uc4504 (batchFile, mode, type )) < 0 )
    {
        fprintf( stderr, ": Error in uc4504 (file open): %s.\n",batchFile );
        UF_get_fail_message( channel, message );
        error_list( message );
        return 0; 
    }
    /*
    Loop to execute a VDA Checker part/configuration file pair
    */
    while ( error != ERREOF ) /* End of file on read */
    {
        /*
        Try to read next part file name/path (*.prt)
        */
        if ( (error = uc4514( channel, inputPart )) <= 0 )
            break;
        /*
        Try to read next configuration file name/path (*.cfg)
        */
        if ( (error = uc4514( channel, inputConfig )) <= 0 )
            break;

        ret = UF_PART_open( inputPart, &inputPartTag, &openStatus );

        if ( openStatus.n_parts > 0 )
        {
            UF_free_string_array( openStatus.n_parts, openStatus.file_names );
            UF_free( openStatus.statuses );
        }
        if ( ret )
        {
            fprintf( stderr, ": Error in UF_PART_open: %s.\n",inputPart );
            UF_get_fail_message( ret, message );
            error_list( message );
            UF_PART_close_all();
            continue;
        }
        /*
        Check if configuration file exists
        */
        if ( (ret = uc4560( inputConfig, 0 )) )
        {
            fprintf( stderr, ": Error opening configuration file: %s.\n",inputConfig );

            if ( 1 == ret )
            {
                fprintf( stderr, ": File does not exist.\n" );
            }
            else
            {
                UF_get_fail_message( ret, message );
                error_list( message );
            }
            continue;
        }
        /*
        Run the VDA Checker
        */
        ret = UF_MODL_ask_vda_4955_compliance( inputPartTag, inputConfig, NULL, NULL );
        if ( ret )
        {
            fprintf( stderr, ": Error in UF_MODL_ask_vda_4955_compliance for %s.\n",inputPart );
            UF_get_fail_message( ret, message );
            error_list( message );
        }
        else
        {
            fprintf( stderr, ": VDA Checker passed for: %s.\n",inputPart );
            UF_PART_close_all();
        }
    } /* end while */

    UF_PART_close_all();

    return 0;
}
