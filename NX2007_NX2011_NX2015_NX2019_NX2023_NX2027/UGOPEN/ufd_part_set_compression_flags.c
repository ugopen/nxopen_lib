/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_PART_set_compression_flags                                      *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example requires a work part. The example gets and prints the       *
 *   status of the compression flag. If compression is off, it is turned on.  *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_assem.h>
#include <uf_part.h>
#include <uf_ui.h>

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
  char buffer[ UF_UI_MAX_STRING_BUFSIZE ];
  char err_msg[ MAX_LINE_BUFSIZE ];
  int err = 0;
  tag_t part;
  UF_PART_compress_flags_t compress;

  /* Open the Information Window for messages. */
  UF_CALL(UF_UI_open_listing_window());

  /* Get the part tag of the work part. */
  part = UF_ASSEM_ask_work_part();

  /* Continue execution if the part tag is valid. */
  if(part != NULL_TAG)
  {
    /* Get the compression flag. */
    if(!UF_CALL(UF_PART_ask_compression_flags(part, &compress)))
    {
      /* If the standard field is true, print a message saying
         the flag is set. Otherwise, print a message saying the
         flag is off and set the flag to on.
      */
      if(compress.standard)
      {
        UF_UI_write_listing_window(
               "The compression flag is on.\n");
      }
      else
      {
        UF_UI_write_listing_window(
                "The compression flag is off.\n");
        compress.standard = TRUE;
        
        if(!UF_CALL(UF_PART_set_compression_flags(part, &compress)))
        {
          UF_UI_write_listing_window(
                   "The compression flag has been set.\n");
        }
      }
    }
  }
  else
  {
    UF_UI_write_listing_window(
               "Couldn't get tag of the work part.\n");
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
