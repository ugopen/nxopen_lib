/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_ASSEM_add_to_cset                                               *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example opens an existing assembly part and then creates            *
 *   a component set and adds all the components, at all levels explicitly,   *
 *   to the set.                                                              *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/



#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <uf_defs.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_assem.h>

static int cycle_components
(
  tag_t component,    /* Component to cycle           I/O */
  tag_t cset          /* Component set to be modified I/O */
)
{
  int inx, ifail = 0, component_count = 0;
  tag_t *child_components = NULL;
  logical level = FALSE;

  if (component == NULL_TAG) return 0;

  component_count = UF_ASSEM_ask_part_occ_children(component,
                                                   &child_components);

  for (inx = 0; inx < component_count; inx++)
  {
    ifail = UF_ASSEM_add_to_cset(cset, child_components[inx], level);
    if (ifail == 0) ifail = cycle_components(child_components[inx], cset);
    else break;
  }

  UF_free(child_components);

  return ifail;
}

/*ARGSUSED*/
extern void ufusr(char *name, int *rtcode, int rtlen)
{
/*  
    Short example of the use of creating component set in an assembly
*/
  int status = 0;
  tag_t root_part_occ = NULL_TAG;
  tag_t displayed_part = NULL_TAG;
  tag_t cset = NULL_TAG;
  static char* cset_name = "my_cset";

  status = UF_initialize();
  if(!status)
  {

    strcpy(name, "");
    displayed_part = UF_PART_ask_display_part();
    if (displayed_part != NULL_TAG)
    {
      root_part_occ = UF_ASSEM_ask_root_part_occ(displayed_part);
      if (root_part_occ != NULL_TAG) 
      {    
        *rtcode = UF_ASSEM_create_cset(displayed_part, cset_name, &cset);
        if (*rtcode == 0)
        {
          *rtcode = cycle_components(root_part_occ, cset);
        }
      }
    }

    if (*rtcode == 0)
    {
     /*  
       This assumes we have successfully executed the program
     */
      printf("The UG/Open API program has succeeded\n Return code is %d\n",
            *rtcode);
    }

    else
    {
     /*  
        This assumes we failed
     */
     printf("The UG/Open API program has failed\n Return code is %d\n",
            *rtcode);
    }
    UF_terminate();
  }
}


