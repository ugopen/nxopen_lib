/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRF_ask_id_symbol_info.
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

void ufusr(char *param, int *retcod, int param_len)
{
    char                          error_message[133] = "";
    int                           ifail = 0;
    int                           type, subtype;
    tag_t                         id_symbol_tag = NULL_TAG;
    double                        id_symbol_origin[ 3 ];
    UF_DRF_id_symbol_type_t       id_symbol_type;
    UF_DRF_id_symbol_info_t       *id_symbol_info;

    /* Initialize User Function. */
    ifail = UF_initialize();

    /* Find the tag of a drafting entity. */
    ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                       UF_drafting_entity_type,
                                       &id_symbol_tag );

    while( !ifail && id_symbol_tag )
    {
        ifail = UF_OBJ_ask_type_and_subtype( id_symbol_tag, &type, 
                                             &subtype );

        /* Test type for the ID Symbol. */
        if( !ifail && subtype == UF_draft_id_symbol_subtype )
        {
            /* Retrieve ID Symbol information. */
            ifail = UF_DRF_ask_id_symbol_info ( id_symbol_tag,
                                                &id_symbol_type,
                                                &id_symbol_origin[ 0 ],
                                                &id_symbol_info );

            /* Free the memory containing the ID Symbol information. */
            ifail = UF_DRF_free_idsymbol( &id_symbol_info );
        }

        /* Find the tag of next drafting entity. */
        if ( !ifail )
            ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                               UF_drafting_entity_type,
                                               &id_symbol_tag );
    }

    printf( "UF_DRF_ask_id_symbol_info sample " );

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

