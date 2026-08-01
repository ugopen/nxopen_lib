/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_ASSEM_ask_all_comp_cset                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION - 
 *   The following example opens an existing assembly part and then creates   *
 *   several component sets containing all the components, at all levels      *
 *   explicitly. It then removes certain components from two of the sets by   *
 *   applying a function to the all_components sets.                          *
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

/*
    Define a structure to pass data to cycle routine.
*/

typedef struct pass_s
{
    tag_t first_set;
    tag_t second_set;
} pass_t, *pass_p_t;


/*---------------------------------------------------------------*/
static logical split_sets
(
        tag_t component,    /* Component from set being cycled  I   */
        void *applData      /* Data supplied                    I/O */
)
{
/*
    If component is a member of the first set then remove it from the second,
    or
    If component is a member of the second set then remove it from the first,
    else
    print an error message.

*/
  pass_p_t data = (pass_p_t)applData;
  logical result;

  UF_ASSEM_is_member_of_cset(data->first_set, component, &result);
  if (result)
  {
    UF_ASSEM_remove_from_cset(data->second_set, component);
  }

  else
  {
    UF_ASSEM_is_member_of_cset(data->second_set, component, &result);
    if (result)
    {
      UF_ASSEM_remove_from_cset(data->first_set, component);
    }

    else
    {
      printf("Found component %u not a member of either set\n", component);
    }
  }

  return TRUE;
}

/*---------------------------------------------------------------*/
static int cycle_components
(
  tag_t component,    /* Component to cycle               I/O */
  tag_t cset,         /* Component set to be modified     I/O */
  logical recurse     /* Switch for recurse on children   I   */
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
    ifail = UF_ASSEM_add_to_cset(cset, child_components[inx],
                                 level);
    if (recurse && ifail == 0) ifail =
            cycle_components(child_components[inx], cset, recurse);
    if (ifail != 0) break;
  }

  UF_free(child_components);

  return ifail;
}

/*---------------------------------------------------------------*/
/*ARGSUSED*/
extern void ufusr(char *name, int *rtcode, int rtlen)
{
/*  
    Short example of the use of creating component set in an assembly
*/
  tag_t root_part_occ = NULL_TAG;
  tag_t displayed_part = NULL_TAG;
  tag_t cset1 = NULL_TAG;
  tag_t cset2 = NULL_TAG;
  tag_t all_cset = NULL_TAG;
  static char* top_name = "top_cset";
  static char* low_name = "low_cset";
  pass_t my_data;

  UF_initialize();

  strcpy(name, "");
  displayed_part = UF_PART_ask_display_part();
  if (displayed_part != NULL_TAG)
  {
    root_part_occ = UF_ASSEM_ask_root_part_occ(displayed_part);
    if (root_part_occ != NULL_TAG) 
    {    
      *rtcode = UF_ASSEM_create_cset(displayed_part,
                                     top_name, &cset1);
      if (*rtcode == 0)
      {
        *rtcode = cycle_components(root_part_occ, cset1,
                                   FALSE);
      }

      if (*rtcode == 0)
      {
        *rtcode = UF_ASSEM_create_cset(displayed_part,
                                       low_name, &cset2);
        if (*rtcode == 0)
        {
          *rtcode = cycle_components(root_part_occ,
                                     cset2, TRUE);
        }
      }

      *rtcode = UF_ASSEM_ask_all_comp_cset(displayed_part,
                                           &all_cset);
      if (*rtcode == 0)
      {
        my_data.first_set = cset1;
        my_data.second_set = cset2;
        *rtcode = UF_ASSEM_apply_to_cset(all_cset,
                                         split_sets, &my_data);
      }
    }
  }

  if (*rtcode == 0)
  {
    /*  
       This assumes we have successfully executed the program.
    */
    printf("The UG/Open API program has succeeded\n Return code is %d\n", 
           *rtcode);
  }

  else
  {
    /*  
       This assumes we failed.
    */
    printf("The UG/Open API program has failed\n Return code is %d\n", 
               *rtcode);
  }


  UF_terminate();
}
