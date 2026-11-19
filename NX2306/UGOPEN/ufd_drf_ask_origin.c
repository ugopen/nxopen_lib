/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRF_ask_ordorigin_info.
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
    int                           ifail = 0;
    int                           type, subtype;
    char                          error_message[133] = "";
    tag_t                         ordorigin_tag = NULL_TAG;
    int                           ord_num_assoc;
    UF_DRF_orddisp_info_t         origin_disp;
    UF_DRF_assoc_info_t           **ord_assoc_objs = NULL;

    /* Initialize User Function. */
    ifail = UF_initialize();

    /* Find the tag to a dimension entity. */
    ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                       UF_dimension_type, 
                                       &ordorigin_tag );

    /* Find the tag of an ordinate dimension. */
    while( !ifail && ordorigin_tag )
    {
        ifail = UF_OBJ_ask_type_and_subtype( ordorigin_tag, &type, 
                                             &subtype );

        /* Retrieve the ordinate dimension origin information. */
        if( !ifail && subtype == UF_dim_ordinate_origin_subtype )
        {
            ifail = UF_DRF_ask_ordorigin_info ( ordorigin_tag, 
                                                &origin_disp, 
                                                &ord_num_assoc, 
                                                ord_assoc_objs );
        }

        /* Find the next tag to a dimension entity. */
        if ( !ifail )
            ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                               UF_dimension_type, 
                                               &ordorigin_tag );
    }

    printf( "UF_DRF_ask_ordorigin_info sample " );

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

