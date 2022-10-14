/*===========================================================================

        Copyright (c) 1997-1998 Electronic Data Systems Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function demonstrates how to invoke UF_PLOT_compare_ughpgl_files.
 *    You may also refer to UGSAMPLES for the use of this function and it's 
 *    application.
 *    The function is placed directly in our UFUN documentation starting with 
 *    the include statements.
 *
 
 *
 ****************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_plot.h>

void ufusr( char *param, int *retcod, int param_len )
{
    char      plot_of_original[ MAX_FSPEC_BUFSIZE ] = "original_plot.hpp"; 
    char      plot_of_revised [ MAX_FSPEC_BUFSIZE ] = "revised_plot.hpp";
    char      result_plot     [ MAX_FSPEC_BUFSIZE ] = "result_plot.hpp";
    char      error_message   [ MAX_LINE_BUFSIZE ];
    int       ifail = 0;
    UF_PLOT_ughpgl_cmp_options_t compare_options;
    UF_PLOT_diff_cmp_status_t comparison_result = UF_PLOT_CMP_NO_DIFF_FOUND;

    /* Initialize UGOpen/API */
    ifail = UF_initialize();

    if ( ifail == 0 )
    {
        /* Set the compare options */
        compare_options.color_width_option = UF_PLOT_CMP_COLOR_WIDTH;
        compare_options.resulting_plot_option = UF_PLOT_CREATE_CMP_PLOT;

        ifail = UF_PLOT_compare_ughpgl_files( plot_of_original,
                                              plot_of_revised,
                                             &compare_options,
                                              result_plot,
                                             &comparison_result );
    }

    if ( ifail == 0 )
    {
        if ( comparison_result == UF_PLOT_CMP_NO_DIFF_FOUND )
           printf( "%s - differences found: NO \n", result_plot );
        else
           printf( "%s - differences found: YES \n", result_plot );
    }

    printf( "UF_PLOT_compare_ughpgl_files" );
    if ( ifail == 0 )
        printf( "is successful. \n");
    else
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails. \nERROR is: %s \n", error_message );
    }

    UF_terminate();
}
