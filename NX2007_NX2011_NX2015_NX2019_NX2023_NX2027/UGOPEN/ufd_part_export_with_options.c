/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_PART_export_with_options                                        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example must be run with an active work part. The code in the       *
 *   following example creates a cube of size 1.0 x 3.2 x 1.5 at the origin   *
 *   and then exports it into a new part. In this example, feature parameters *
 *   are retained and expressions are copied deeply.                          *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_defs.h>
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
  UF_PART_export_options_t export_options;
  double corner_pt[3] = {0.0, 0.0, 0.0};
  char *edge_lens[3] = {"1.0", "3.2", "1.5"};
  tag_t feature;
  tag_t block;
 

  /* Create a block feature from which we can obtain a
     solid for export purposes.
  */
  UF_CALL(UF_MODL_create_block1(UF_NULLSIGN, corner_pt, 
                                edge_lens, &feature));

  /* Get the body tag of the feature because UF_feature_type
     is not transferable but UF_solid_type is.
  */
  UF_CALL(UF_MODL_ask_feat_body(feature, &block));

  /* Fill out the structure to specify how the object is to be
     exported. See the header file for descriptions of these fields.
  */
  export_options.new_part = TRUE;
  export_options.params_mode = UF_PART_maintain_params;
  export_options.expression_mode = UF_PART_copy_exp_deeply;

  UF_CALL(UF_PART_export_with_options("exported_block", 1,
                                       &block, &export_options));
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
