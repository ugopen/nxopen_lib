/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_PS_set_journal_state                                            *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates "ps_sample2" part. The example code        *
 *   calls routines related to Parasolid journaling. First, the current       *
 *   status of Parasolid journaling and the name of the journal file are      *
 *   determined. The name of the journal file is then output to the standard  *
 *   output device. Once journaling is enabled, a character string is         *
 *   written tothe journal file to describe the next set of Parasolid calls.  *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_part.h>
#include <uf_ps.h>

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
  int    journal_state, units = UF_PART_METRIC;
  char   *part_name = "ps_sample2";
  char   journal_name[ MAX_FSPEC_BUFSIZE ];
  tag_t  part;

  /* Create a new part. */
  UF_CALL(UF_PART_new(part_name, units, &part));
    
  /* Obtain the journaling status and the journal file name. */
  UF_CALL(UF_PS_ask_journal_data(&journal_state,
                                 journal_name));

  /* Print out the name of the journal file. */
  printf("Journal file name = %s\n",journal_name);

  /* If journaling is disabled, enable it. */
  if (journal_state == 0)
  {
    journal_state = 1;
    UF_CALL(UF_PS_set_journal_state(journal_state));
  }

  /* Add comment to file to reflect what is being done. */
  UF_CALL(UF_PS_write_to_journal(
          "** Modelling the Crank Shaft **"));

  /* Save the part file. */
  UF_CALL(UF_PART_save());
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
