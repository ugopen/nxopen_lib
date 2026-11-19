/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_spline                                              *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates a    *
 *   tube using a spline for the path.                                        *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <math.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_disp.h>
#define POLES 384
#define R1 2.25
#define R2 0.35
#define ANG PI/24
#define WEIGHT 1.0
#define ORDER 4

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
  char *diams[2] = {"0.5", "0.0"};
  
  int i;
  int k_fixup;
  int p_fixup;

  tag_t spline_id;
  uf_list_p_t tubelist, tubefeats;
  UF_FEATURE_SIGN create = UF_NULLSIGN;

  double knotseq[POLES+ORDER];
  double pole_array[POLES*4];
  double x,y,z,t,w = WEIGHT;
  double delta_u = 1.0/((double)(POLES-ORDER+1));

  for(i = 0; i < ORDER; i++) {
    knotseq[i] = 0.0;
  }
  for(i = POLES; i < POLES + ORDER; i++) {
    knotseq[i] = 1.0;
  }
  i = 0;
  t =0.0;
  while( i < POLES*4){
    x = R1*cos(t) + .001;
    y = R1*sin(t) + .001;
    z = R2 + (R2/PI)*t;
    t += ANG;
    pole_array[i++] = x;
    pole_array[i++] = y;
    pole_array[i++] = z;
    pole_array[i++] = w;
    printf("%f, %f, %f, %f, %d\n",pole_array[i-4],pole_array[i-3],
	pole_array[i-2],pole_array[i-1],i-4);
  }
  for(i = ORDER; i < POLES ; i++){
    knotseq[i] = (i-ORDER+1)*delta_u;
  } 
  
  printf("\nDelta u is = %f\n",delta_u);
  printf("Knot Sequence Values:\n");

  for(i = 0; i < POLES + ORDER; i++) printf("%f\n",knotseq[i]);
  UF_CALL(UF_MODL_create_spline(POLES,ORDER,knotseq,pole_array,
                        &spline_id,&k_fixup,&p_fixup));
  if(k_fixup == 1) printf("Knot sequence was fixed.\n");
  if(p_fixup == 1) printf("Pole array was fixed.\n");
  UF_CALL(UF_MODL_create_list(&tubelist));
  UF_CALL(UF_MODL_put_list_item(tubelist, spline_id));
  UF_CALL(UF_MODL_create_tube(tubelist, diams, create, &tubefeats));

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
