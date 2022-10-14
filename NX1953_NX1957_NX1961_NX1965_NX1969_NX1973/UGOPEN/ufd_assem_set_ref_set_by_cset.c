/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_ASSEM_set_ref_set_by_cset                                       *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a displayed part with components.  The    *
 *   example sets the reference set for all the components in an assembly to  *
 *   be the SOLID reference set.                                              *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <uf.h>
#include <uf_part.h>
#include <uf_assem.h>

/*---------------------------------------------------------------*/
/*ARGSUSED*/
extern void  ufusr(char *def, int *ret_code, int retlen)
{ 
  tag_t displayed_part = NULL_TAG;

  UF_initialize();

  displayed_part = UF_PART_ask_display_part();

  if (displayed_part != NULL_TAG)
  { 
    tag_t   cset;

    UF_ASSEM_ask_all_comp_cset(displayed_part, &cset);

    if (cset != NULL_TAG)
    { 
      UF_ASSEM_set_ref_set_by_cset(cset, "SOLID");
    }
  }

  UF_terminate();
}
