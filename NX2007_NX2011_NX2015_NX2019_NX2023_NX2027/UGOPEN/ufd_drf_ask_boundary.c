/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRF_ask_boundaries.
 *    It is placed directly in our UFUN documentation starting with
 *    the include statements.
 *
 *  
 ********************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_assem.h>
#include <uf_defs.h>
#include <uf_drf.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>

void ufusr(char *param, int *retcod, int param_len)
{
    int                   ifail = 0;
    int                   type, subtype, num_boundaries;
    tag_t                 boundary_tag = NULL_TAG;
    tag_p_t               boundary_tags;
    char                  error_message[133] = "";

    ifail = UF_initialize();

    /* Get an annotation type. */
    ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                       UF_drafting_entity_type, 
                                       &boundary_tag );

    while( !ifail && boundary_tag )
    {
        /* Get annotation subtype. */
        ifail = UF_OBJ_ask_type_and_subtype( boundary_tag, &type,
                                             &subtype );

        if( !ifail && ( subtype == UF_draft_crosshatch_subtype ||
                        subtype == UF_draft_area_fill_subtype ||
                        subtype == UF_draft_solid_fill_subtype ))
        {
            ifail = UF_DRF_ask_boundaries( boundary_tag, 
                                           &num_boundaries,
                                           &boundary_tags );
            /* Free the memory. */
            if( !ifail )
                UF_free( &boundary_tags );
        } 

        /* Find the tag of next drafting entity. */
        if ( !ifail )
            ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                               UF_drafting_entity_type, 
                                               &boundary_tag );
    }

    printf( "UF_DRF_ask_boundaries sample " );

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

