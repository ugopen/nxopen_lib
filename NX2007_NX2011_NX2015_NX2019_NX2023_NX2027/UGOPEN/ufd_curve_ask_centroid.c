/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_CURVE_ask_centroid                                              *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following program requires a blank, open part. The code queries the  *
 *   centroid of an arc.                                                      *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_csys.h>
#include <uf_curve.h>

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

   tag_t wcs_tag;
   UF_CURVE_arc_t arc_coords;
   tag_t arc;
   double centroid[3];
   tag_t centroid_id;

   UF_CSYS_ask_wcs( &wcs_tag );
   UF_CSYS_ask_matrix_of_object( wcs_tag, &arc_coords.matrix_tag );
   arc_coords.start_angle = 0.0;
   arc_coords.end_angle = 180.0*DEGRA;
   arc_coords.arc_center[0] = 0.0;
   arc_coords.arc_center[1] = 0.0;
   arc_coords.arc_center[2] = 0.0;
   arc_coords.radius = 1.0;
   
   
   if (!UF_CALL(UF_CURVE_create_arc( &arc_coords, &arc)))
   {
      if (!UF_CALL(UF_CURVE_ask_centroid( arc, centroid)))
      {
	 UF_CALL(UF_CURVE_create_point(centroid, &centroid_id));
      }
   }   
   
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
