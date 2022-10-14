/*******************************************************************************
             Copyright (c) 1998-1999 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       






File Description:
   Contains prototypes of functions that are common to both internal and
   external UG/Open sample code for cycling a part. The source code is
   available in the routine ufx_cycle_common.c.
*******************************************************************************/

#ifndef UFX_CYCLE_INCLUDED
#define UFX_CYCLE_INCLUDED


/* UFUN header files */
#include <uf_defs.h>




/* Function prototypes */

/* -----------------------------------------------------------------------------
Output information about the part.  This routine also calls the routine
which cycles the part.

Return: void.
   -----------------------------------------------------------------------------
*/
 
extern void UFX_CYCLE_data(
tag_t part_tag  /* <I>
                Tag of part file that is going to be cycled.
                */
);


/* -----------------------------------------------------------------------------
Opens the part and gets the units of the part and then calls the
functions that get history and attribute information.

Return: void.
   -----------------------------------------------------------------------------
*/ 

extern int UFX_CYCLE_open_part(
char *part_name, /* <I>
                 Name of part file to open.
                 */
tag_t *part_tag  /* <O>
                 Tag of part file that was opened.
                 */
);


/* -----------------------------------------------------------------------------
Prints the error message from UF_get_fail_message to the open listing
device or prints an alternate message if UF_get_fail_message fails. 

Return: void
   -----------------------------------------------------------------------------
*/

extern void report_err(
int status, /* <I>
            return value from a User Function.
            */
char *alt_msg  /* <I>
               Alternate message to use if UF_get_fail_message fails. Note that
               alt_msg cannot be NULL.
               */
);


#endif /* UFX_CYCLE_INCLUDED */

