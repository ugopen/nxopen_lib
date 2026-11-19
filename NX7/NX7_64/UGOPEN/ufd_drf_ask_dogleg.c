/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRF_ask_dogleg_info.
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
    tag_t                         orddim_tag = NULL_TAG;
    UF_DRF_dogleg_info_t          dogleg_info;

    /* Initialize User Function. */
    ifail = UF_initialize();

    /* Find the tag to a dimension entity. */
    ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                       UF_dimension_type, 
                                       &orddim_tag );

    /* Find the tag of an ordinate dimension. */
    while( !ifail && orddim_tag )
    {
        ifail = UF_OBJ_ask_type_and_subtype( orddim_tag, &type, 
                                             &subtype );

        /* Test type for the ordinate dimension. */
        if( !ifail && ( subtype == UF_dim_ordinate_horiz_subtype ||
                        subtype == UF_dim_ordinate_vert_subtype ))
        {
            /* Retrieve ordinate dimension dog leg information. */
            ifail = UF_DRF_ask_dogleg_info ( orddim_tag, &dogleg_info );
        }

        /* Find the tag to a dimension entity. */
        if ( !ifail )
            ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                               UF_dimension_type, 
                                               &orddim_tag );
    }

    printf( "UF_DRF_ask_dogleg_info sample " );

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

