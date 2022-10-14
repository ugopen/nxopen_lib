/*===========================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_add_sxline_sxseg.  It is placed  
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
#include <uf_drf.h>
#include <uf_drf_types.h>
#include <uf_obj.h>

void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    int                         numchrs;
    tag_t                       sxline1_tag;
    char                        error_message[133];
    char *                      sxline1 = "step_sxline1";
    UF_DRF_object_t             new_object;
    tag_t                       new_sxseg_tag;


    ifail = UF_initialize();

    if( !ifail )
    {
        /* Get the tag of the section line named step_sxline1. */
        numchrs = strlen( sxline1 );
        ifail = uc5028( sxline1, numchrs, &sxline1_tag );
    }

    /* Initialize the object used to define the drawing position
       of the new section line segment. */
    if( !ifail ) 
        ifail = UF_DRF_init_object_structure( &new_object );

    if( !ifail )
    {
        /* Set the associativity type and X,Y coordinate 
           position of the object used to define the new
           section line segment. */
        new_object.object_assoc_type = UF_DRF_dwg_pos;
        new_object.assoc_dwg_pos[0] = 3.6;
        new_object.assoc_dwg_pos[1] = 6.3;

        /* Create the new section segment. The tag of the 
           newly created segment is returned. */
        ifail = UF_DRAW_add_sxline_sxseg( sxline1_tag,
            UF_DRAW_sxseg_cut, UF_DRAW_sxline_leg1, 
            &new_object, &new_sxseg_tag );

    }

    printf( "UF_DRAW_add_sxline_sxseg sample " );
    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();

}
