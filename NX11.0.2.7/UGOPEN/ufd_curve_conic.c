/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routines:        *
 *                                                                            *
 *         UF_CURVE_create_conic                                              *
 *         UF_CURVE_ask_conic_data                                            *
 *         UF_CURVE_convert_conic_to_std                                      *
 *         UF_CURVE_convert_conic_to_gen                                      *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates curve.prt. The code creates an elliptical  *
 *   arc that starts at 0 degrees and ends at 240 degrees, not rotated.       *
 *                                                                            *
 * NOTE - Rotation angles do not always reproduce when an ellipse is          *
 *   converted from general to standard form.                                 *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_curve.h>
#include <uf_csys.h>
#include <uf_defs.h>

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

static void do_conic_api(void)
{
  char *part_name = "curve";
  tag_t part, conic_id, wcs_tag;
  UF_CURVE_conic_t orig_conic;
  UF_CURVE_conic_t read_conic;
  UF_CURVE_conic_t conv_conic;
  UF_CURVE_genconic_t gen_conic;
  logical conv_sense;
  
  /* Fill out the data structure for the standard form of an ellipse */
  orig_conic.matrix_tag = NULL_TAG;
  orig_conic.conic_type = UF_conic_ellipse_subtype;
  orig_conic.rotation_angle = 0.0 * DEGRA;
  orig_conic.start_param = 0.0;
  orig_conic.end_param = 240 * DEGRA;
  orig_conic.center[0] = 0.0;
  orig_conic.center[1] = 0.0;
  orig_conic.center[2] = 1.0;
  orig_conic.k1 = 2.0;
  orig_conic.k2 = 4.0;
  
  UF_CALL(UF_PART_new(part_name, UF_PART_ENGLISH, &part));
  UF_CALL(UF_CSYS_ask_wcs(&wcs_tag));
  UF_CALL(UF_CSYS_ask_matrix_of_object(wcs_tag,
                                       &orig_conic.matrix_tag));
  UF_CALL(UF_CURVE_create_conic(&orig_conic,&conic_id));
 
  /* Read the conic back */
  UF_CALL(UF_CURVE_ask_conic_data(conic_id, &read_conic));
  /* This data should match the original */

  /* Convert the conic to general form */
  UF_CALL(UF_CURVE_convert_conic_to_gen(&read_conic, &gen_conic));

  /* Convert the conic to standard form */
  UF_CALL(UF_CURVE_convert_conic_to_std(&gen_conic, &conv_conic, &conv_sense));
  /* 
   * This data should match the original, except that the original 
   * rotation angle may not be reproduced, in which case it is hard to
   * tell if the conversion worked.
   */
}

void ufusr(char *param, int *retcode, int paramLen)
{
    if (!UF_CALL(UF_initialize()))
    {
        do_conic_api();
        UF_CALL(UF_terminate());
    }
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
