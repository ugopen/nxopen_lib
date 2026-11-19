/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_PART_open_cset                                                  *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example opens an existing assembly part and then creates   *
 *   several component sets containing all the components at all levels of    *
 *   the assembly. A function is then applied to each member of one of the    *
 *   sets.                                                                    *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_assem.h>
#include <uf_obj.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static tag_t ask_cset_of_unloaded_children(tag_t part,
                                           tag_t part_occ);

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
  tag_t displayed_part = NULL_TAG;
  tag_t root_part_occ = NULL_TAG;

  displayed_part = UF_PART_ask_display_part();

  if (displayed_part != NULL_TAG)
  { 
    /* We have a displayed part, find the root part occurrence. */

    root_part_occ = UF_ASSEM_ask_root_part_occ(displayed_part);

    if (root_part_occ != NULL_TAG)
    { 
      /* It is an assembly, get a cset of unloaded children. */

      tag_t unloaded_child_cset = 
               ask_cset_of_unloaded_children(displayed_part, 
                                             root_part_occ);

      if (unloaded_child_cset != NULL_TAG)
      { 
        UF_PART_load_status_t load_status;
        int                   i;

        /* Now load the component set. */
 
        UF_CALL(UF_PART_open_cset(unloaded_child_cset, 
                          &load_status));

        for (i = 0;i < load_status.n_parts;i++)
        { 
          printf("Error number %d. Open child part %s failed\n",
                 load_status.statuses[i],
                 load_status.file_names[i]);
        }

        if (load_status.n_parts > 0)
        {
          UF_free_string_array(load_status.n_parts, 
                               load_status.file_names);

          UF_free(load_status.file_names);
        }

        /* And unload the parts. */

        UF_CALL(UF_PART_close_cset(unloaded_child_cset));

        /* We're now done with the cset so delete it. */

        UF_CALL(UF_OBJ_delete_object(unloaded_child_cset));
      }
    }
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

static tag_t ask_cset_of_unloaded_children(tag_t part,
                                           tag_t part_occ)
{ 
  tag_t cset = NULL_TAG;

  if (UF_CALL(UF_ASSEM_create_cset(part, 
                   "UNLOADED_CHILDREN", &cset)))
  { 
    return NULL_TAG;
  }
  else
  { 
    tag_t *children;
    int   n_children = 
               UF_ASSEM_ask_part_occ_children(part_occ, &children);
    int   i;

    for (i = 0;i < n_children;i++)
    { 
      tag_t instance = 
                    UF_ASSEM_ask_inst_of_part_occ(children[i]);
      char  part_fspec[ MAX_FSPEC_BUFSIZE ];

      UF_ASSEM_ask_part_name_of_child(instance, part_fspec);

      if (!UF_PART_is_loaded(part_fspec))
      { 
       /* This is an unloaded child part, add to set. */

        logical no_children = false;

        UF_ASSEM_add_to_cset(cset, children[i],
                             no_children);
      }
    }

    return cset;
  }
}
