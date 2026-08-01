/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_cre_surf_cloud                                             *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates a    *
 *   B-surface from a list of cloud points.                                   *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>

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

  int             pnt_cnt = 16;
  int             u_degree = 3, v_degree = 3;
  int             u_patches = 1, v_patches = 1;
  int             corner_switch = 0;
  int             max_err_index;
  double          average_error, max_error;
  tag_t           surface_tag = NULL_TAG;
 
  static double   mtx[2][3] = { {1.0, 0.0, 0.0}, {0.0, 1.0, 0.0} };
  static double   cloud_pnts[][3]= 
        { { 2200.0,  548.0, 1472.0 }, { 1400.0, 1168.0, 1213.0 }, 
          { 1000.0,  285.0, 1377.0 }, { 1000.0, 1107.0, 1154.0 }, 
          { 1000.0, -254.0,  950.0 }, { 2200.0,  951.0, 1462.0 }, 
          { 1400.0, -353.0, 1049.0 }, { 1800.0,  605.0, 1388.0 }, 
          { 1400.0,  222.0, 1550.0 }, { 1800.0, -426.0, 1121.0 }, 
          { 2200.0,  207.0, 1750.0 }, { 1800.0, 1007.0, 1406.0 }, 
          { 1800.0,  259.0, 1655.0 }, { 1400.0,  649.0, 1301.0 }, 
          { 2200.0, -479.0, 1175.0 }, { 1000.0,  704.0, 1167.0 } };  
          
  
  UF_CALL(UF_MODL_create_surf_from_cloud( pnt_cnt,
                                          cloud_pnts,
                                          mtx,
                                          NULL,
                                          u_degree,
                                          v_degree,
                                          u_patches,
                                          v_patches,
                                          corner_switch,
                                          &average_error,
                                          &max_error,
                                          &max_err_index,
                                          &surface_tag ));
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
