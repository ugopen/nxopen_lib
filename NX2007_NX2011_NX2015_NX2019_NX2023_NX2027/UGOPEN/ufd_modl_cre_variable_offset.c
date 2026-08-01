/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_variable_offset                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates a    *
 *   B-surface and a variable offset.                                         *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_modl.h>
#include <uf.h>
#include <uf_obj.h>
#include <uf_curve.h>
#include <uf_layout.h>
#include <uf_obj_types.h>


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

  tag_t  base_sheet_id, varoff_sheet_id;
  char  *dist[4]={"-0.5", "0.5", "-0.5", "0.5"};

  double  uv_param[8]={0.0, 0.0,
                       1.0, 0.0,
                       1.0, 1.0,
                       0.0, 1.0};
  
  int num_pole_u = 4;
  int num_pole_v = 4;
  int u_ord = 4;
  int v_ord = 4;
  int knot_fix;
  int pole_fix;

  int viewnum = 1;
  int scale_opt = 2;
  int i, j, k = 0;
  
  const char *layout = "B_SURFACE";
  /*<Devansh Desai> : DES11050 :Refer to UF_OBJ_NAME_LEN instead of hard coded value */
  // +1 for null character
  const char view[][ UF_OBJ_NAME_BUFSIZE ] = { "TFR-ISO" };

  double weight = 1.0;
  double scale = 1.0;
  double u_knot[9] = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0};
  double v_knot[9] = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0};
  double pole[64];


/* Create pole array data. */
  for (i = 0; i < 4; i++) {
    for (j = 0; j < 4; j++) {
      pole[k++] = i;
      pole[k++] = j;
      pole[k++] = 0.0;
      pole[k++] = weight;
    }
  }



  /* Create base surface. */
  UF_CALL(UF_MODL_create_bsurf(num_pole_u, num_pole_v, u_ord, v_ord,
                       u_knot, v_knot,pole,&base_sheet_id,
                       &knot_fix,&pole_fix));


  /* Create layout. */ 
  UF_CALL(uc6460(layout,viewnum,view,scale_opt,scale));

  /* create variable offset surface */
  UF_CALL(UF_MODL_create_variable_offset(base_sheet_id,
                                         dist,
                                         uv_param,
                                         &varoff_sheet_id));
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
