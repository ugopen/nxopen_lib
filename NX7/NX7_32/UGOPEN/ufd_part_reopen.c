/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_PART_reopen                                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example creates and saves a blank part, then makes some             *
 *   modifications. After the modifications, it reopens the part. The result  *
 *   should be an open, blank part.
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

/*
    1. Create a new part called a_blank_part.prt
    2. Save the part with no geometry.
    3. Create some geometry.
    4. Reopen the part.
*/
#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_defs.h>
#include <uf_part.h>

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
  /* scope and mode are for UF_PART_reopen. Scope = 0
     sets the scope for the part only and excludes
     subassemblies. Mode = 1 means reopen even if
     modified in the session.
  */
  int scope = 0;
  int mode = 1; 
  char   *edge_len[] = {"1.0","1.0","1.0"};
  double corner_pt[] = {0.0,0.0,0.0};
  tag_t  block_tag;
  tag_t  part_tag;
  tag_t  reopen_part_tag;

  /* Open a new part then save it. */
  UF_CALL(UF_PART_new("a_blank_part.prt",UF_PART_ENGLISH,&part_tag));
  UF_CALL(UF_PART_save());

  /* Create a unit block. This modifies the part. */
  UF_CALL(UF_MODL_create_block1(UF_NULLSIGN,
                                corner_pt,edge_len,&block_tag));

  /* Reopens unmodified part because of mode setting. */
  UF_CALL(UF_PART_reopen(part_tag,scope,mode,&reopen_part_tag));

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
