/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_ASSEM_restore_load_options                                      *
 *         UF_ASSEM_ask_assem_options                                         *
 *         UF_ASSEM_set_assem_options                                         *
 *         UF_ASSEM_set_default_ref_sets                                      *
 *         UF_ASSEM_ask_default_ref_sets                                      *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open assembly part and a load options  *
 *   default file. The code restores the load options file, applies the       *
 *   options to all levels of default reference sets, sets the default        *
 *   reference sets, and queries the results.                                 *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/
#include <stdlib.h>
#include <stdio.h>
#include <uf_assem.h>
#include <uf.h>

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
  UF_ASSEM_options_t  assy_options;
  char          *default_ref_sets[2], **result;
  char          *facet_ref_set = "FACET", *empty_ref_set = "Empty";
  int            n_default_ref_sets, status;

  /* First restore the load_options from the a central file. */
  status = UF_ASSEM_restore_load_options("/central/load_options.def");
  if (status != 0)
  {
    printf("UF_ASSEM_restore_load_options() returned %d\n",status);
    return;
  }
  /*
    Now turn on the `Apply to All Levels' setting for default
    reference sets.
  */
  UF_ASSEM_ask_assem_options(&assy_options);
  assy_options.apply_to_all_levels = UF_ASSEM_do_apply_to_all_levels; 
  UF_ASSEM_set_assem_options(&assy_options);
  /* 
    Set the default reference sets to look for facets first.  The result of
    this call should be to have a reference set list of:
        FACET
        Empty Part
        As Saved
        Entire Part

    since the `As Saved' and `Entire Part' will be added 
    automatically at the end.
  */
  default_ref_sets[0] = facet_ref_set;
  default_ref_sets[1] = empty_ref_set;

  status = UF_ASSEM_set_default_ref_sets(2, default_ref_sets);
  if (status != 0)
  {
    printf("UF_ASSEM_set_default_ref_sets() returned %d\n",status);
    return;
  }
  /*
    Now just output the resulting reference sets just to confirm they are
    correctly set.  Remember to free the returned memory.
  */
  status = UF_ASSEM_ask_default_ref_sets(&n_default_ref_sets,
                                         &result);
  if (status == 0)
  {
    int i;

    for (i=0; i<n_default_ref_sets; i++)
    {
      printf("Default ref set %d now set to %s\n", i, result[i]);
      UF_free(result[i]);
    }
  }
  else
  {
    printf("UF_ASSEM_ask_default_ref_sets() returned %d\n",status);
  }

  UF_free(result);

}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
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
