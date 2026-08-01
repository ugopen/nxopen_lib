/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_mass_props_3d                                          *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open part with solid bodies. The       *
 *   example prompts you to select sheet bodies. It then prints out the mass  *
 *   properties obtained from the analysis on the selected bodies.            *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_disp.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_object_types.h>

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
  UF_UI_selection_options_t opts;
  UF_UI_mask_t mask = {UF_solid_type, 0, UF_UI_SEL_FEATURE_BODY};
  tag_t   *solbody = NULL;
 
  int  response = 2;
  int type = 1; 
  int  unit = 3;
  int accuracy =  1;
  int  count = 0;
  int  zero = 0;
  int  i;
  double  acc_val[11] = {.01,0,0,0,0,0,0,0,0,0,0};
  double  density = 1.0;
  double  massprop[47];
  double  massprop_stat[13];
  opts.num_mask_triples = 1;
  opts.mask_triples = &mask;
  opts.scope = UF_UI_SEL_SCOPE_WORK_PART;
  UF_CALL(UF_UI_select_by_class("Select solid bodies",&opts,&response,
                                    &count,&solbody));

  /* if sheet bodies were selected */
  if ( solbody != NULL )     
  {
     UF_CALL(UF_MODL_ask_mass_props_3d(solbody,
                                       count,
                                       type,
                                       unit,
                                       density,
                                       accuracy,
                                       acc_val,
                                       massprop,
                                       massprop_stat));
     for (i=0; i<47; i++)
     {
       printf("[%d] = %f\n",i,massprop[i]);
     }
     for (i=0; i<count; i++)
     {
        UF_CALL(UF_DISP_set_highlight(solbody[i],zero));
     }
                                          
     UF_free(solbody);
  }
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
