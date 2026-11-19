/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_exps_of_feature                                        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The example creates a *
 *   block, queries this feature, then prints the dimensions of the block.    *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
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
  char *block_len[3] = {"1","2","3"};
  char *string;
  char buf[100];

  double block_orig[3] = {0.0,0.0,0.0};

  tag_t blk_obj;
  tag_t *exps;

  int number_of_exps=0,i;
    
  UF_UI_open_listing_window();

/* Create a block we can query */
  UF_CALL(UF_MODL_create_block1(UF_NULLSIGN,
                                block_orig,
                                block_len,
                               &blk_obj));

  if(!UF_CALL(UF_MODL_ask_exps_of_feature(blk_obj,
                                      &number_of_exps,
                                      &exps)))
  {
    sprintf(buf,"number_of_exps=%d\n",number_of_exps);
    UF_UI_write_listing_window(buf);
    UF_UI_write_listing_window("Asking expression strings\n");

    for(i=0;i<number_of_exps;i++)
    {
      UF_CALL(UF_MODL_ask_exp_tag_string(exps[i],&string));

      sprintf(buf,"Expression %d: %s\n",i,string);
      UF_UI_write_listing_window(buf);
      UF_free(string);
    }
    UF_free(exps);
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
