/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_FLTR_auto_create_plane_zones                                    *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part. The code in the following   *
 *   example automatically divides the part into 3 plane zones along the      *
 *   Z axis of the current WCS.  The function is using the entire Z           *
 *   displacement of the part as the region to be zoned (as indicated by      *
 *   use_part = TRUE).                                                        * 
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_fltr.h>
#include <uf_part.h>

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
  tag_t displayed_part_tag; 
  tag_t *zone_list; 
  int num_zones_created; 
  int num_in_z_dir = 3;
  double zone_disp = 0.0;
  double disp_origin[3] = {0.0,0.0,0.0};
  logical use_part = TRUE; /* Causes zone_disp and disp_origin to
                            * be ignored */

  num_in_z_dir = 3;

  displayed_part_tag = UF_PART_ask_display_part();

  UF_CALL(UF_FLTR_auto_create_plane_zones(displayed_part_tag,
                                            "ZONE_PLANE",
                                            num_in_z_dir,
                                            use_part,
                                            zone_disp,
                                            disp_origin,
                                            &zone_list,
                                            &num_zones_created));

 /* First zone created is zone_list[0], last created is
  * zone_list[num_zones_created - 1]
  */

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
