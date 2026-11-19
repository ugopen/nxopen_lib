/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_FLTR_auto_create_box_zones                                      *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The code in the following example creates zones automatically with 1 in  *
 *   the X direction of the WCS, 2 in the Y direction and 3 in the Z          *
 *   direction.  The volume to be zoned is a box which measures 100 by 150 by *
 *   50 (XYZ, respectively) and has its origin at -10,10,5.                   *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>  
#include <uf_part.h>
#include <uf_fltr.h>

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
  int num_in_dir[3], num_zones_created;
  double zone_vol[3];
  double vol_origin[3];
  logical use_part = FALSE; /* This would be set to TRUE if user 
                             * desires that the whole part volume
                             * is to be zoned */

  num_in_dir[0] = 1;
  num_in_dir[1] = 2;
  num_in_dir[2] = 3;

  zone_vol[0] = 100.0; 
  zone_vol[1] = 150.0; 
  zone_vol[2] = 50.0;

  vol_origin[0] = -10.0; 
  vol_origin[1] = 10.0; 
  vol_origin[2] = 5.0;

  displayed_part_tag = UF_PART_ask_display_part();

  UF_CALL(UF_FLTR_auto_create_box_zones(displayed_part_tag,
                                          "ZONE_BOX",
                                          num_in_dir,
                                          use_part,
                                          zone_vol,
                                          vol_origin,
                                          &zone_list,
                                          &num_zones_created));
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
