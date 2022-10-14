/*===================================================================

        Copyright (c) 1998 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_ASSEM_create_component_part                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION - 
 *   The following example creates two cubes and then moves them into a new   *
 *   component part. This example must be run with a valid work part.         *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_defs.h>
#include <uf_part.h>
#include <uf_assem.h>

/*ARGSUSED*/
extern void ufusr(char *param, int *retcod, int param_len)
{
  double origin[3] = {0.0, 0.0, 0.0};
  double csys[6] = {1.0, 0.0, 0.0, 
                    0.0, 1.0, 0.0};
  double corner_pts[2][3] = { {5.0, 2.0, 0.0},
                              {0.0, 0.0, 0.0} };
  char *edge_lens[3] = {"1.0", "3.2", "1.5"};
  tag_t features[2];
  tag_t blocks[2];
  tag_t work_part;
  tag_t instance;
  int units;
  int status;
  int i;

  UF_initialize();

  for (i = 0; i < 2; i++)
  {
    status = UF_MODL_create_block1(UF_NULLSIGN, corner_pts[i], 
                                   edge_lens, &features[i]);

    if (status != 0)
    {
      fprintf(stderr, "Failed to create block\n");
      UF_terminate();

      return;
    }

    status = UF_MODL_ask_feat_body(features[i], &blocks[i]);

    if (status != 0)
    {
      fprintf(stderr, "Failed to get body from block\n");
      UF_terminate();

      return;
    }
  }

  work_part = UF_ASSEM_ask_work_part();
  UF_PART_ask_units(work_part, &units);
 
  status = UF_ASSEM_create_component_part(work_part, "blocks.prt", 
                                          NULL, NULL, units, 0, 
                                          origin, csys, 2, blocks, 
                                          &instance);

  if (status != 0)
  {
    fprintf(stderr, "Failed to move blocks to new component\n");
  }
  UF_terminate();
}
