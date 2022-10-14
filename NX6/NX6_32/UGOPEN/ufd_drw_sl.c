/*===========================================================================

        Copyright (c) 1998 Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/***************************************************************************/
/*
 *  Description
 *    This function is a small sample program that demonstrates
 *    the invocation of UF_DRAW_ask_face_of_sil and 
 *    UF_DRAW_ask_body_sils_in_view.  It is placed
 *    directly in our UFUN documentation starting with the
 *    include statements.
 *
 
 *
 ****************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_draw.h>
#include <uf_draw_types.h>
#include <uf_drf_types.h>
#include <uf_obj.h>
#include <uf_view.h>


void ufusr(char *param, int *retcod, int param_len)
{
    int                         ifail = 0;
    int                         num_silhouettes = 0;
    int                         ndx = 0;
    tag_t                       body_tag = NULL_TAG;
    tag_t                       view_tag = NULL_TAG;
    tag_t                       face_tag = NULL_TAG;
    tag_t *                     silhouette_tags = NULL;
    char                        error_message[133];
    char *                      body_name = "body1";
    char *                      view_name = "TOP@1";
    char *                      face_name = "face1";


    ifail = UF_initialize();

    /* Find the tags of the body and view from their names. */
    if( ifail == 0 )
        ifail = UF_OBJ_cycle_by_name( body_name, &body_tag );

    if( ifail == 0 )
        ifail = UF_VIEW_ask_tag_of_view_name( view_name,
            &view_tag );

    /* Retrieve the sils of the body in the top view. */
    if( ifail == 0 )
        ifail = UF_DRAW_ask_body_sils_in_view( body_tag, 
            view_tag, &num_silhouettes, &silhouette_tags );

    if( ifail == 0 )
    {
        for( ndx=0; ndx<num_silhouettes; ndx++ )
        {
            tag_t sil_face_tag = NULL_TAG;

            ifail = UF_DRAW_ask_face_of_sil(
                silhouette_tags[ndx], 
                &sil_face_tag );

            /* Add code here to process silhouette and face. */

        }
    }

    UF_free( silhouette_tags );

    /* Or retrieve the sils of a known face on the body. */
    silhouette_tags = NULL;
    if( ifail == 0 )
        ifail = UF_OBJ_cycle_by_name( face_name, &face_tag );

    if( ifail == 0 )
        ifail = UF_DRAW_ask_face_sils_in_view( face_tag, 
            view_tag, &num_silhouettes, &silhouette_tags );

    if( ifail == 0 )
    {
        for( ndx=0; ndx<num_silhouettes; ndx++ )
        {
            /* Add code here to process silhouettes of face. */
        }
    }

    UF_free( silhouette_tags );

    printf( "UF_DRAW_ask_body_sils_in_view sample " );
    if( ifail > 0 )
    {
        ifail = UF_get_fail_message( ifail, error_message );
        printf( "fails.\nError is: %s\n", error_message );
    }
    else
        printf( "is successful.\n" );

    ifail = UF_terminate();

}

