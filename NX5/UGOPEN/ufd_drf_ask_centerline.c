/*===================================================================

        Copyright (c) 1998-2001  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRF_ask_centerline_info.
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
    int                           subtype, type;
    tag_t                         centerline_tag = NULL_TAG;
    char                          error_message[133] = "";
    double                        centerline_origin[ 3 ];
    UF_DRF_valid_cline_form_t     centerline_type;
    UF_DRF_centerline_info_t      *centerline;

    /* Initialize User Function. */
    ifail = UF_initialize();

    /* Find the tag to a drafting entity. */
    ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                       UF_drafting_entity_type, 
                                       &centerline_tag );

    /* Retrieve the object subtype. */
    if( !ifail && centerline_tag )
    {
        ifail = UF_OBJ_ask_type_and_subtype( centerline_tag, 
                                             &type, &subtype );
    }

    /* Test centerline subtype. */
    if( !ifail && ( subtype >= UF_draft_linear_cntrln_subtype
               && subtype <= UF_draft_sym_cntrln_subtype ))
    {
        ifail = UF_DRF_ask_centerline_info ( centerline_tag, 
                &centerline_type, &centerline_origin[ 0 ],
                &centerline );

        /* Free the memory that contains centerline information. */
        if( !ifail )
        {
            ifail = UF_DRF_free_centerline(&centerline);
        }
    }

    printf( "UF_DRF_ask_centerline_info sample " );

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

