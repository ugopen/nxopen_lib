/*===========================================================================

        Copyright (c) 1998,2000  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_sxline_type.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_drf_types.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>

void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    tag_t                       sxline_tag = NULL_TAG;
    char                        error_message[133];
    UF_DRAW_sxline_type_t       sxline_type;


    ifail = UF_initialize();
    if( !ifail )
    {
        ifail = UF_OBJ_cycle_objs_in_part( 
            (UF_PART_ask_display_part()),
            UF_section_line_type, &sxline_tag );
    }
 
    if( !ifail )
    {
        while( sxline_tag )
        {
            /* Find the section line type from its tag. */
            ifail = UF_DRAW_ask_sxline_type( sxline_tag, 
                &sxline_type );
            if( ifail ) break;

            switch ( sxline_type )
            {
                case UF_DRAW_simple_sxline:
                {
                    /* Process simple sxline here. */
                };
                break;

                case UF_DRAW_stepped_sxline:
                {
                    /* Process stepped sxline here. */
                };
                break;

                case UF_DRAW_revolved_sxline:
                {
                    /* Process revolved sxline here. */
                };
                break;

                case UF_DRAW_half_sxline:
                {
                    /* Process half sxline here. */
                };
                break;

                case UF_DRAW_unfolded_sxline:
                {
                    /* Process unfolded sxline here. */
                };
                break;

                case UF_DRAW_breakline:
                {
                    /* Process breakline here. */
                };
                break;

                default:
                {
                };
                break;

            } /* End of switch on section line type. */

            ifail = UF_OBJ_cycle_objs_in_part(
                (UF_PART_ask_display_part()),
                UF_section_line_type, &sxline_tag );
            if( ifail ) break;
       }
    }

    printf( "UF_DRAW_ask_sxline_type sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n",  error_message );
    }
    else
        printf( "is successful.\n" );

    ifail = UF_terminate();

}
