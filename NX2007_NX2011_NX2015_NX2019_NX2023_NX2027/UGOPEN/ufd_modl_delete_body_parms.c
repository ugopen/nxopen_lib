/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_delete_body_parms                                          *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a part with a solid body. The example     *
 *   deletes all the parameters of the selected solid body.                   *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_ui.h>
#include <uf_object_types.h>
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

  tag_t       body,view;
  UF_UI_selection_options_t opts;
  UF_UI_mask_t mask = {UF_solid_type,0,UF_UI_SEL_FEATURE_BODY};
  uf_list_p_t delete_body_list;
  int         error = 0, response = 2, zero = 0;
  double      cursor[3];

  opts.num_mask_triples = 1;
  opts.mask_triples = &mask;
  opts.scope = UF_UI_SEL_SCOPE_WORK_PART;
  

  error = UF_UI_select_single("Select a solid body",
                              &opts,
                              &response,
                              &body,cursor,&view);

  if (!error && response != 1 && response != 2)
  { /* if there's no error & response is not CANCEL or BACK */
    /* Create a list to put the solid body in */
    UF_CALL(UF_MODL_create_list(&delete_body_list));
    UF_CALL(UF_MODL_put_list_item(delete_body_list, body));

    /* Deleting all of the parametric information from the */
    /* solid body in the delete_body_list.*/
    UF_CALL(UF_MODL_delete_body_parms(delete_body_list));
    UF_CALL(UF_MODL_delete_list(&delete_body_list));

    /* unhighlight selected body */
    UF_CALL(UF_DISP_set_highlight(body,zero)); 
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
