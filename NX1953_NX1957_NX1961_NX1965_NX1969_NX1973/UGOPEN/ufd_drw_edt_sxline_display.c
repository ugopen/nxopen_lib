/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_edit_sxline_display.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/


#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_obj.h>

void ufusr(char *param, int *retcod, int param_len)
{

    int                         ifail = 0;
    int                         numchrs;
    char                        error_message[133];
    char *                      sxline = "half_sxline1";
    tag_t                       sxline_tag;
    UF_DRAW_arrow_parms_t       arrow_parms;
    UF_DRAW_sxline_display_t    sxline_display;


    ifail = UF_initialize();
    if( !ifail )
    {
        /* Find the tag of the section line from its name. */
        numchrs = strlen( sxline );
        ifail = uc5028( sxline, numchrs, &sxline_tag );
    }

    if( !ifail )
    {
        /* Retrieve this section line's preferences. */
        ifail = UF_DRAW_ask_sxline_display( sxline_tag, 
            &arrow_parms, &sxline_display );
    }

    if( !ifail )
    {
        /* Change arrow_parm values and then edit the sxline. */
        arrow_parms.size = .2;
        arrow_parms.total_length = .4;
        arrow_parms.incl_angle = 30.0;
        arrow_parms.past_part_dist = 0.4;
        arrow_parms.stub_len = .3;
        arrow_parms.head_type = UF_DRAW_ansi_arrow;
        arrow_parms.head_control = UF_DRAW_open_arrowhead;

        ifail = UF_DRAW_edit_sxline_display( sxline_tag, 
            &arrow_parms, sxline_display );
    } 

    printf( "UF_DRAW_edit_sxline_display sample " );
    if( ifail )
    {
        UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();

}
