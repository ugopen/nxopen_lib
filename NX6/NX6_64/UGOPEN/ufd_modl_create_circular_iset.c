/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_circular_iset                                       *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates a cover plate, a two-inch diameter,        *
 *   .25 inch height cylinder with a .5625 inch hole in the center. There is  *
 *   a .21875 inch hole that is instanced in a circular array at 120 degree   *
 *   intervals.                                                               *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
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

  double origin[3] = {0.0, 0.0, 0.0};
  double orig_iset[3] = {0.0, -0.75, 0.0};
  double direction[3] = {0.0, 0.0, 1.0};
  char *height = ".25";
  char *diam_cover = "2.0";
  char *diam_hole = "0.5625";
  char *diam_iset = "0.21875";
  char *part_name = "cover";
  UF_FEATURE_SIGN create = UF_NULLSIGN;
  UF_FEATURE_SIGN sub = UF_NEGATIVE;
  tag_t cover_id, hole_id, iset_id, feat_obj, part;
  uf_list_p_t feat_list;
  int english_units = 2;
  
  UF_CALL(UF_PART_new(part_name, english_units, &part));
  
  
  UF_CALL(UF_MODL_create_cyl1(create,origin,height,diam_cover,direction,
                      &cover_id));
  UF_CALL(UF_MODL_create_cyl1(sub,origin,height,diam_hole,direction,
                      &hole_id));
  UF_CALL(UF_MODL_create_cyl1(sub,orig_iset,height,diam_iset,direction,
                      &iset_id));
  UF_CALL(UF_MODL_create_list(&feat_list));
  UF_CALL(UF_MODL_put_list_item(feat_list,iset_id));
  UF_CALL(UF_MODL_create_circular_iset(0,origin,direction,"3","120",
                               feat_list,&feat_obj));
   
  UF_CALL(UF_MODL_delete_list(&feat_list));
  UF_CALL(UF_PART_save());

}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
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
