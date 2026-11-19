/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRF_ask_draft_aid_text_info.
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
    int                           num_text;
    tag_t                         draft_aid_tag = NULL_TAG;
    char                          error_message[133] = "";
    UF_DRF_draft_aid_text_info_t  *text_info;

    /* Initialize User Function. */
    ifail = UF_initialize();

    /* Find the tag to a drafting entity. */
    ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                       UF_drafting_entity_type, 
                                       &draft_aid_tag );

    if( !ifail && draft_aid_tag )
    {
        /* Retrieve the text information of the drafting entity. */
        ifail = UF_DRF_ask_draft_aid_text_info ( draft_aid_tag, 
                                                 &num_text, 
                                                 &text_info );

        if( !ifail )
        {
            /* Free the memory that contains the text information. */
            ifail = UF_DRF_free_text( num_text, &text_info );
        } 
    }

    printf( "UF_DRF_ask_draft_aid_text_info sample " );

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

