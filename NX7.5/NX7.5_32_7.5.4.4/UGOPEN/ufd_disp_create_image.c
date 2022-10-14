/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_DISP_create_image                                               *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part. The code creates several    *
 *   image file formats from the graphics window.                             *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_disp.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static int report( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char    messg[133];
        printf("%s, line %d:  %s\n", file, line, call);
        (UF_get_fail_message(irc, messg)) ?
            printf("    returned a %d\n", irc) :
            printf("    returned error %d:  %s\n", irc, messg);
    }
    return(irc);
}

static void do_ugopen_api(void)
{

        int upper_left_corners[2];
        int width , height ;

        /* create a full window TIFF file */

        UF_DISP_create_image("test.tif",
                             UF_DISP_TIFF,
                             UF_DISP_ORIGINAL);

        /* create a rectangular area compressed TIFF file */

        upper_left_corners[0] = 50;
        upper_left_corners[1] = 50;
        width = 200;
        height = 200;

        UF_DISP_create_framed_image("testc.tif",
                             UF_DISP_COMPRESSED_TIFF,
                             UF_DISP_ORIGINAL,
                             upper_left_corners,
                             width,
                             height);

        /* create a full window JPEG file */

        UF_DISP_create_image("test.jpg",
                             UF_DISP_JPEG,
                             UF_DISP_ORIGINAL);

        /* create a rectangular area GIF file */

        upper_left_corners[0] = 100;
        upper_left_corners[1] = 50;
        width = 250;
        height = 200;

        UF_DISP_create_framed_image("test.gif",
                             UF_DISP_GIF,
                             UF_DISP_WHITE,
                             upper_left_corners,
                             width,
                             height);

    
}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
{
    if (!UF_CALL(UF_initialize()))
    {
        do_ugopen_api();
        UF_CALL(UF_terminate());
    }
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
