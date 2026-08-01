/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_CURVE_CREATE_FILLET                                             *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates fillet.prt. The code creates 2-curve       *
 *   fillets between newly created lines.                                     *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_curve.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_csys.h>

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
  double center[3], radius;
  int  units = UF_PART_ENGLISH;
  int  trim_opts[3],arc_opts[3]={FALSE,FALSE,FALSE};
  char   *part_name = "fillet";
  UF_CURVE_line_t line_coords1 = {1.2,0.2,0.0,-0.5,2.5,0.0},
                  line_coords2 = {3.2,2.25,0.0,2.5,3.5,0.0};
  UF_CURVE_arc_t arc_coords1 = {NULL_TAG,238*DEGRA,357*DEGRA,
                                0.22,4.3,0.0,2.0},
                 arc_coords2 = {NULL_TAG,82*DEGRA,175*DEGRA,
                                3.0,0.43,0.0,2.0};
  tag_t  part,line1,line2,arc1,arc2,curve_objs[3];
  tag_t  fillet_obj1,fillet_obj2, wcs_tag, matrix_tag;
  
  
  UF_CALL(UF_PART_new(part_name,units,&part));

  /* create 2 lines */
  UF_CALL(UF_CURVE_create_line(&line_coords1,&line1));

  UF_CALL(UF_CURVE_create_line(&line_coords2,&line2));

  /* create 2 arcs */
  UF_CALL(UF_CSYS_ask_wcs(&wcs_tag));
  UF_CALL(UF_CSYS_ask_matrix_of_object(wcs_tag,&matrix_tag));
  arc_coords1.matrix_tag=matrix_tag;
  arc_coords2.matrix_tag=matrix_tag;

  
  UF_CALL(UF_CURVE_create_arc(&arc_coords1,&arc1));

  UF_CALL(UF_CURVE_create_arc(&arc_coords2,&arc2));

  /*create fillet between "arc1" and "line1"*/
  curve_objs[0] = arc1;
  curve_objs[1] = line1;
  center[0] = 0.0;
  center[1] = 2.1;
  center[2] = 0.0;
  radius = .25;
  trim_opts[0] = TRUE;          /*trim first curve*/
  trim_opts[1] = TRUE;         /*trim second curve*/
  UF_CALL(UF_CURVE_create_fillet(UF_CURVE_2_CURVE,
                                 curve_objs,
                                 center,
                                 radius,
                                 trim_opts,
                                 arc_opts,
                                 &fillet_obj1));

  /*create fillet between "line1" and "arc2"*/
  curve_objs[0] = line1;
  curve_objs[1] = arc2;
  center[0] = 0.8;
  center[1] = 1.0;
  center[2] = 0.0;
  radius = .25;
  trim_opts[0] = TRUE;          /*trim first curve*/
  trim_opts[1] = TRUE;         /*trim second curve*/

  UF_CALL(UF_CURVE_create_fillet(UF_CURVE_2_CURVE,
                                 curve_objs,
                                 center,
                                 radius,
                                 trim_opts,
                                 arc_opts,
                                 &fillet_obj2));
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
