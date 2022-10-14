/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/*******************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRF_ask_dim_info.
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
    char                          error_message[133] = "";
    int                           ifail = 0;
    tag_t                         dim_tag = NULL_TAG;
    int                           dim_type;
    double                        dim_origin[ 3 ];
    UF_DRF_dim_info_t             *dim_info;

    /* Initialize User Function. */
    ifail = UF_initialize();

    /* Retrieve a dimension type. */
    ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                       UF_dimension_type, 
                                       &dim_tag );

    /* Retrieve dimension information. */
    while( !ifail && dim_tag )
    {
        {
            ifail = UF_DRF_ask_dim_info ( dim_tag, &dim_type, 
                                          &dim_origin[ 0 ],
                                          &dim_info );

            /* Free the memory containing the dimension information. */
            if( !ifail )
                UF_DRF_free_dimension( &dim_info );
        }

        /* Retrieve a dimension type. */
        ifail = UF_OBJ_cycle_objs_in_part( UF_ASSEM_ask_work_part(),
                                           UF_dimension_type, 
                                           &dim_tag );
    }

    printf( "UF_DRF_ask_dim_info sample " );

    if( ifail )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    UF_terminate();
}

