/*===================================================================

        Copyright (c) 1998-2003 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_ASSEM_count_objs_in_comp                                        *
 *         UF_ASSEM_ask_component_data                                        *
 *         UF_ASSEM_ask_part_occ_children                                     *
 *         UF_ASSEM_cycle_objs_in_comp                                        *
 *         UF_ASSEM_ask_parent_component                                      *
 *         UF_ASSEM_ask_root_part_occ                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION - 
 *   The following example cycles the occurrenced members of the displayed    *
 *   part. It does some checking on the data and prints out the results of    *
 *   checking.                                                                *
 *                                                                            *
                   *
 *                                                                            *
 ******************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <uf_defs.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_cfi.h>

static int cycle_components(
/* Component to cycle    I/O */
  tag_t component,    
/* for formatting        I/O */
  char *indentation)
{
  int i;
  int ifail = 0;
  int component_count = 0;
  int check_number = 0;
  tag_t parent = NULL_TAG;
  tag_t member = NULL_TAG;
  tag_t *child_components = NULL;
  char p_name[ MAX_FSPEC_BUFSIZE ];
  char r_name[ UF_OBJ_NAME_BUFSIZE ];
  char c_name[ UF_CFI_MAX_FILE_NAME_BUFSIZE ];
  char local_indentation[256];
  double origin[3];
  double csys_matrix[9];
  double transform[4][4];

  if (component == NULL_TAG) return 0;

  strcpy(local_indentation, indentation);
  ifail = UF_ASSEM_ask_component_data( component,p_name,r_name,
                                       c_name,origin,csys_matrix,
                                       transform);

  if (ifail != 0)
  {
    return ifail;
  }

  printf("%s Part name %s component name %s reference set"
         " name %s with members ..\n",
         local_indentation, p_name,
         c_name == NULL ? "No component name" : c_name,
         r_name == NULL ? "No reference set name" : r_name);

  component_count = UF_ASSEM_ask_part_occ_children(component,
                                          &child_components);

  ifail = UF_ASSEM_count_objs_in_comp(component, &check_number);
  i = 0;

  printf("%s  ", local_indentation);
  ifail = UF_ASSEM_cycle_objs_in_comp(component, &member);
  if (ifail != 0)
  {
    return ifail;
  }
  while (member != NULL_TAG)
  {
    i++;

    /*
      Do a sanity check to make sure we get the correct parent back.
    */
    ifail = UF_ASSEM_ask_parent_component(member, &parent);
    if (ifail != 0 || parent != component)
    {
      printf("ERROR: got back the wrong parent %u for member %u\n",
             parent, member);
      return 11;
    }

    /* Print the tag of the member. */
    printf("%u, ", member);

    ifail = UF_ASSEM_cycle_objs_in_comp(component, &member);

    if (ifail != 0)
    {
      return ifail;
    }
  }
  printf("\n");

  if (i != check_number)
  {
    printf("ERROR: Got back the wrong number of members, expecting %d,"
           " got %d\n", check_number, i);
    return 12;
  }

  /* Now repeat for each child component, with an indentation
     for formatting.
  */
  strcat(local_indentation, "  ");
  for (i=0; i<component_count; i++)
  {
    ifail = cycle_components(child_components[i], local_indentation);
  }

  UF_free(child_components);

  return ifail;
}
/*ARGSUSED*/
extern void ufusr(char *name, int *rtcode, int rtlen)
{
  /*
    Short example of use of assemblies navigation routines to output an
    assemblies listing and the contents of each component.
  */
  tag_t root_part_occ = NULL_TAG;
  tag_t displayed_part = NULL_TAG;
  char indentation[256];

  UF_initialize();

  strcpy(name, "");
  displayed_part = UF_PART_ask_display_part();
  if (displayed_part != NULL_TAG)
  {
    root_part_occ = UF_ASSEM_ask_root_part_occ(displayed_part);
    if (root_part_occ != NULL_TAG)
    {
      strcpy(indentation, "  ");
      *rtcode = cycle_components(root_part_occ, indentation);
    }
  }

  if (*rtcode == 0)
  {
    /* This assumes we have successfully executed the program. */
    printf("The UG/Open API program has succeeded\n Return code is %d",
           *rtcode);
  }

  else
  {
     /* This assumes we failed. */
    printf("The UG/Open API program has failed\n Return code is %d",
           *rtcode);
  }


  UF_terminate();
}
