/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_OBJ_cycle_objs_in_part                                          *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example requires an open part containing features. The routine      *
 *   cycles the features in a part.                                           *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_defs.h>
#include <uf.h>
#include <uf_object_types.h>
#include <uf_obj.h>
#include <uf_part.h>

static  char    title0[] = "\nFeature report for part %s\n";

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
  char            part_fspec[ MAX_FSPEC_BUFSIZE ];
  int             curr_part, num_parts;
  int             type;
  int             count_1;
  tag_t           part;
  tag_t           feature;
    
  /* Get the total number of loaded parts. */
  num_parts = UF_PART_ask_num_parts();

  for ( curr_part=0 ; curr_part < num_parts ; curr_part++ )
  {
    /* Get the part tag for the current part number of the
       loaded part and get its part name.
    */
    part = UF_PART_ask_nth_part( curr_part );

    UF_PART_ask_part_name( part, part_fspec );

    printf( title0, part_fspec );
    count_1 = 0;
    type = UF_feature_type;
    feature = NULL_TAG;

    /* Start the cycling process by passing in a NULL_TAG. */
    UF_OBJ_cycle_objs_in_part( part, type, &feature );

    /* Keep cycling until there are no more features to cycle. */
    while ( feature != NULL_TAG )
    {
      count_1++;
      UF_OBJ_cycle_objs_in_part( part, type, &feature );
    }

    printf("UF_OBJ_cycle_objs_in_part shows %d features\n",
           count_1 );

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
