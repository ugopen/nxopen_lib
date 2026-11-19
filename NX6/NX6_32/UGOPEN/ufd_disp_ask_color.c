/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_DISP_ask_color_count                                            *
 *         UF_DISP_ask_color                                                  *
 *         UF_DISP_set_color                                                  *
 *         UF_DISP_load_color_table                                           *
 *         UF_DISP_ask_closest_color                                          *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part. The code reduces the        *
 *   saturation of each color in the color table by 10%. The background color *
 *   is changed to blue.                                                      *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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

  int     count, clr_num, name_len;
  char   *clr_name;
  char   *new_name;
  double  clr_values[3];

  UF_CALL(UF_DISP_ask_color_count( &count ));

  for (clr_num = 1; clr_num < count; clr_num++ )
  {
    /* Request "hsv" color values */
    UF_CALL(UF_DISP_ask_color( clr_num,
                                 UF_DISP_hsv_model,
                                 &clr_name,
                                 clr_values ));

    /* Reduce the saturation by 10% */
    clr_values[1] *= 0.9;

    /* Append "_dil" (i.e. diluted) to the color name */

    name_len = strlen( clr_name );
    new_name = (char *)malloc( name_len+5 );
    strcpy( new_name, clr_name );

    if (name_len < (UF_DISP_MAX_NAME_SIZE-4))
    {
      strcat( new_name, "_dil" );
    }
    UF_CALL(UF_DISP_set_color( clr_num,
                                 UF_DISP_hsv_model,
                                 new_name,
                                 clr_values ));

    free( new_name );

    UF_free( clr_name );
  }

  /* Set background color to blue using "rgb" model. */
  /* Color name is ignored for background.           */

  clr_values[0] = 0.0;          /* red   */
  clr_values[1] = 0.0;          /* green */
  clr_values[2] = 1.0;          /* blue  */
  UF_CALL(UF_DISP_set_color( UF_DISP_BACKGROUND_COLOR,
                             UF_DISP_rgb_model,
                             NULL,
                             clr_values ));

  UF_CALL(UF_DISP_load_color_table());

  /* Determine the closest color to blue.  Note that */
  /* the background color is not considered.         */

  clr_values[0] = 240.0;
  clr_values[1] =   0.0;
  clr_values[2] =   0.0;
  UF_CALL(UF_DISP_ask_closest_color(
                             UF_DISP_hsv_model,
                             clr_values,
                             UF_DISP_CCM_EUCLIDEAN_DISTANCE,
                             &clr_num ));

  printf( "The closest color to blue is #: %d", clr_num );

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
