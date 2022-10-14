/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRF_ask_id_symbol_type.
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
    tag_t                         id_symbol_tag = NULL_TAG;
    char                          error_message[133] = "";
    int                           subtype, type;
    UF_DRF_id_symbol_type_t       id_symbol_type;

    /* Initialize User Function. */
    ifail = UF_initialize();

    /* Find the tag to a drafting entity. */
    ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                       UF_drafting_entity_type, 
                                       &id_symbol_tag );

    if( !ifail && id_symbol_tag )
    {
        ifail = UF_OBJ_ask_type_and_subtype( id_symbol_tag, 
                &type, &subtype );
    }

    if ( !ifail && type == UF_draft_id_symbol_subtype )
    {
        /* Retrieve the ID Symbol type. */
        ifail = UF_DRF_ask_id_symbol_type( id_symbol_tag, 
                &id_symbol_type );
    }

    printf( "UF_DRF_ask_id_symbol_type sample " );

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

