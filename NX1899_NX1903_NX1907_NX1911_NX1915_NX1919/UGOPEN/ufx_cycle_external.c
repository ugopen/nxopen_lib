/*==============================================================================
          Copyright (c) 1998  Unigraphics Solutions Corporation
                   Unpublished - All rights reserved

================================================================================
 File Name: UFX_cycle_external.c

 File Description:
   This is the external User Function source code for cycling the data model
   of a part. The program accepts a file name from the command line. The major
   work is done by UFX_CYCLE_open_part() and UFX_CYCLE_data() which are common 
   to both the internal and external versions. See UFX_cycle_common.c for 
   details.
================================================================================


*******************************************************************************/

 
/* Include Files */
#include <ufx_cycle.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_text.h>

/* Function prototypes */
static int get_args(int argc, char **argv, char *part_name);

/* -----------------------------------------------------------------------------
 Function Name: main

 Function Description:
   The main for external User Function.

 Input:
   argc - Argument count
   argv - Pointers to character strings.

 Output: None.

 Returns:
   0 - Indicates success.
   -----------------------------------------------------------------------------
*/

extern int main(int argc, char **argv)
{
  int err;
  tag_t part_tag;

  char part_name[ MAX_FSPEC_BUFSIZE ], err_msg[ MAX_LINE_BUFSIZE ];

  err = get_args(argc, argv, part_name);

  if(!err)
  {
    err = UF_initialize();
    if(err)
    {
       fprintf(stderr,"\nError: Could not init UFUN.\n");
       UF_get_fail_message(err,err_msg);
       fprintf(stderr, "Error %d: %s \n",err,err_msg);
    }
    else
    {
      err = UF_UI_open_listing_window();
      if(err)
      {
        fprintf(stderr, "\nUnable to open listing window.\n");
      }
      else
      {
         err = UFX_CYCLE_open_part(part_name, &part_tag);
         if(err)
         {
           report_err(err, "\nUnable to open part.\n");
         }
         else
         {
           UFX_CYCLE_data(part_tag);
         }
      }
    UF_terminate();
      
    }

  }
  return(err ? EXIT_FAILURE : EXIT_SUCCESS);
}


/* -----------------------------------------------------------------------------
 Function Name: get_args

 Function Description:
   Error checks that a part name was received as a command line argument
   from main and that the part name is the correct length. Copies part
   name into part_name.

 Input:
   argc - Argument count from main.
   argv - Pointers to string arguments from main.

 Output:
   part_name - Part name character string from command line arguments.

 Returns:
   0 - Indicates success. A part name was received.
   1 - Indicates failure. Either the command line argument was missing
        or the file name was too long.
   -----------------------------------------------------------------------------
*/

static int get_args(int argc, char **argv, char *part_name)
{

  if(argc !=2)
  {
    part_name[0] = '\0';

    fprintf(stderr, "\nThis program requires a part file name as input.\n");
    fprintf(stderr, "The syntax for this program is as follows:\n\n");
    fprintf(stderr, "\t%s <part_name>\n", argv[0]);

    return(1);
  }
  else
  {
      int numch = 0;
      int err = UF_TEXT_count_characters ( argv[1] , &numch );
      if ( ( err != 0 ) || ( numch > MAX_FSPEC_NCHARS ) ) 
      {
          printf("Error: File name is too long.");
          return 1;
      }
      else
      {
          strcpy(part_name, argv[1]);
          return(0);
      }
  }
}

/* -----------------------------------------------------------------------------
 Function Name: report_err

 Function Description:
   Prints the error message from UF_get_fail_message to the open listing
   device or prints an alternate message if UF_get_fail_message fails. 

 Inputs:
   status - return value from a User Function.
   alt_msg - Alternate message to use if UF_get_fail_message fails. Note that
             alt_msg cannot be NULL.

 Outputs: None.

 Returns: None
   -----------------------------------------------------------------------------
*/

extern void report_err(int status, char *alt_msg)
{
  char message[ MAX_LINE_BUFSIZE ];

  int err = UF_get_fail_message(status, message);

  if(err)
  {
     fprintf(stderr, "Error: %s \n", alt_msg);
  }
  else
  {
     fprintf(stderr, "Error: %s \n", message);
  }
}

