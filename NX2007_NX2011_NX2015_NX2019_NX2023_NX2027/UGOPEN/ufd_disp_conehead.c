/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_DISP_conehead                                                   *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code displays a   *
 *   conehead vector in all active views.                                     *
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

  double pt1[3] = {0.0, 0.0, 0.0};
  double pt2[3] = {2.0, 2.0, 2.0};
  double pt3[3] = {-2.0,-2.0,-2.0};
  double vect1[3] = {1.0, 1.0, 1.0};

  UF_DISP_conehead_attrb_s attrb;

  UF_DISP_conehead(UF_DISP_ALL_ACTIVE_VIEWS,
                   pt1, vect1, 1);
   /* Example to draw the vector with the base of its staff 
      anchored at the origin so that the vector appears to point 
      away from the origin
   */
  UF_DISP_conehead(UF_DISP_ALL_ACTIVE_VIEWS,
                   pt2, vect1, 0);
  UF_DISP_labeled_conehead(UF_DISP_ALL_ACTIVE_VIEWS,
                           pt3, vect1, 0, "Normal");
  UF_DISP_get_conehead_attrb(&attrb);

  /* Use color index three */
  attrb.color = 3;

  /* Update the current attribute settings */
  UF_DISP_set_conehead_attrb(&attrb);

  printf("\nCurrent conhead display settings:\n");
  printf("\tLength of Staff: %g\n", attrb.staff_length);
  printf("\tTotal Length: %g\n", attrb.total_length);
  printf("\tRadius of Cone Base: %g\n", attrb.cone_radius);
  printf("\tColor Index: %d\n", attrb.color);
  printf("\tFont Index: %d\n", attrb.font);
  printf("\tDensity Index: %d\n", attrb.density);
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
