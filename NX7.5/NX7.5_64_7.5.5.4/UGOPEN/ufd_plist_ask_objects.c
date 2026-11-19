/*===========================================================================

                        Copyright (c) 2007 UGS Corp.
                      Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_PLIST_ask_objects() and 
 *    UF_PLIST_ask_tags(). 
 *    It is placed directly in our UFUN documentation starting 
 *    with the include statements.
 *
 
 *
 ****************************************************************************/
#include <stdio.h>
#include <uf.h>
#include <uf_plist.h>


void ufusr(char *param, int *retcod, int param_len)
{
    int         ifail = 0, num=0, i, j;
    tag_p_t     plist = NULL;

    /* Initialize User Function*/
    ifail = UF_initialize();

    if( !ifail )
    {
        /* Lists all the parts list tags */
        ifail = UF_PLIST_ask_tags(&plist, &num);
    }

    if( !ifail && num > 0)
    {
        for( j=0; j<num; j++)
        {
            int num_objects = 0;
            tag_p_t objects = NULL;

            printf( "Parts List tag is %d", plist[j]);

            /* Lists objects associated with the parts list */
            ifail = UF_PLIST_ask_objects( plist[j], &num_objects, &objects );

            if( !ifail && num_objects > 0 )
            {
                printf( "There were %i objects found in the parts list", num_objects );
                for( i = 0; i < num_objects; i++ )
                {
                    printf( "Object number %i is %d", i+1, objects[i] );
                }
                /* Free the memory containing the objects */
                UF_free( objects );
            }
            else
            {
                printf( "There were %i objects found in the parts list.", num_objects );
            }
        }
        /* Free the memory containing the parts list tags */
        UF_free(plist);
    }
    else
    {
        printf( "There were %i Parts List", num);
    }

    ifail = UF_terminate();
}
