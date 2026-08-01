/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRF_ask_ud_symbol_font_info.
 *    It is placed directly in our UFUN documentation starting with
 *    the include statements.
 *
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
    int                           ifail = 0;
    int                           num_symbols;
    int                           type, subtype;
    tag_t                         ud_symbol_tag = NULL_TAG;
    char                          error_message[133] = "";
    UF_DRF_ud_symbol_font_info_t  *font_info;

    /* Initialize User Function. */
    ifail = UF_initialize();

    /* Find the tag of a drafting entity. */
    ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                       UF_drafting_entity_type, 
                                       &ud_symbol_tag );

    while( !ifail && ud_symbol_tag )
    {
        ifail = UF_OBJ_ask_type_and_subtype( ud_symbol_tag, &type,
                                             &subtype );

        /* Retrieve the User Defined Symbol font information. */
        if( !ifail && subtype == UF_draft_user_defined_subtype )
        {
            ifail = UF_DRF_ask_ud_symbol_font_info( ud_symbol_tag, 
                    &num_symbols, &font_info );

            /* Free the memory containing the font information. */
            if( !ifail )
                ifail = UF_DRF_free_font( num_symbols, &font_info );
        }

        /* Find the tag of a drafting entity. */
        if ( !ifail )
            ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                               UF_drafting_entity_type, 
                                               &ud_symbol_tag );
    }

    printf( "UF_DRF_ask_ud_symbol_font_info sample " );

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

