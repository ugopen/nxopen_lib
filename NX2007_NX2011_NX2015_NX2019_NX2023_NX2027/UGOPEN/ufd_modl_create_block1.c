/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_block1                                              *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank open part. The code creates two   *
 *   blocks. The second block is added to the first block.
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>

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
  UF_FEATURE_SIGN sign = UF_NULLSIGN;
  UF_FEATURE_SIGN sign1 = UF_POSITIVE;
  double block_orig[3] = {0.0,0.0,0.0};
  double block_orig1[3] = {0.0,0.0,2.5};
  char *block_len[3] = {"1","2","3"};
  char *block_len1[3] = {"1", "1", "1"};
  tag_t blk_obj;
  tag_t blk1_obj;


  UF_CALL(UF_MODL_create_block1(sign, block_orig, block_len, &blk_obj));
  UF_CALL(UF_MODL_create_block1(sign1, block_orig1, block_len1, &blk1_obj));
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
