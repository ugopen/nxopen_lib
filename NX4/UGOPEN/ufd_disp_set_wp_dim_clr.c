/*===================================================================

              Copyright (c) 1998 - 2004 Unigraphics Solutions Inc.
                        Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_DISP_set_work_plane_dim_clr                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part. The code sets the work      *
 *   plane emphasis dim color to white.                                       *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <uf_defs.h>
#include <uf.h>
#include <uf_disp.h>
#include <uf_obj.h>
#include <stdio.h>

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
    int    color;

    UF_DISP_ask_closest_color_in_part(NULL_TAG, UF_DISP_WHITE_NAME, &color);

    UF_CALL(UF_DISP_set_work_plane_dim_clr(color));
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
