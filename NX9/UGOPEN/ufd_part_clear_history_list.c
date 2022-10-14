/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_PART_clear_history_list                                         *
 *         UF_PART_ask_part_history                                           *
 *         UF_PART_ask_nth_history                                            *
 *         UF_PART_ask_num_histories                                          *
 *         UF_PART_create_history_list                                        *
 *         UF_PART_delete_history_list                                        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example cycles over all currently loaded parts and prints  *
 *   their save histories.  It allocates a history_list object and then, for  *
 *   each part in the session, obtains its save history and prints the        *
 *   information.
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <time.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_part.h>

static  char    title0[] =
  "\nPart History for part: %s\n";

static  char    title1[] =
  "Version  Time/Date        Machine  User                 Program";

static  char    title2[] =
  "-------  ---------------  -------  ----                 -------";

static  char    format[] = 
  "%7d  %-15.15s  %-7.7s  %-20.20s  %s\n";

static char     time_format[] = "%d %b %y %H:%M";

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
  UF_PART_history_list_p_t history_list = NULL;
  char    part_fspec[ MAX_FSPEC_BUFSIZE ];
  char    time_buff[21];
  struct  tm  *time_ptr;
  time_t  displayed_time;
  char    *program, *user, *machine;
  int     vers_num, vers_time;
  int     num_parts, num_hists;
  int     curr_part, curr_hist;
  tag_t   part;

  /* Get the total number of parts loaded in the current session. */ 
  num_parts = UF_PART_ask_num_parts();

  
  for ( curr_part=0 ; curr_part < num_parts ; curr_part++ )
  {
    /* Get the part tag and part name of each loaded part. */
    part = UF_PART_ask_nth_part( curr_part );
    UF_PART_ask_part_name( part, part_fspec );
    printf( title0, part_fspec );

    /* Create the history list if it has not been created. */
    if( !history_list )
    {
      UF_CALL(UF_PART_create_history_list( &history_list ));
    }

    /* Clear the history list of the previous part. */
    UF_CALL(UF_PART_clear_history_list( history_list ));

    /* Get the history of the current part. */
    UF_CALL(UF_PART_ask_part_history( part, history_list ));

    /* Get the total number of save histories of the part. */
    UF_CALL(UF_PART_ask_num_histories( history_list, &num_hists ));

    /* Get information about each particular save history and
       print a report.
    */
    for ( curr_hist=0 ; curr_hist < num_hists ; curr_hist++ )
    {
      UF_PART_ask_nth_history( history_list, curr_hist,
                               &program, &user, &machine,
                               &vers_num, &vers_time );
      displayed_time = (time_t) vers_time;
      time_ptr = localtime ( &displayed_time );
      strftime( time_buff, sizeof(time_buff),
                time_format, time_ptr );
      if( curr_hist == 0 )
      {
        printf("\n%s\n%s\n", title1, title2 );
      }
      printf(format,vers_num,time_buff,machine,user,program);
    }
  }
  /* Deallocate memory for the history list. */
  if ( history_list ) UF_PART_delete_history_list(history_list);
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
