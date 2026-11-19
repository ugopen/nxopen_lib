/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_feat_name                                              *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The example creates a *
 *   a block and then finds the type and time stamp of the block.             *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_ui.h>
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

  double block_orig[3] = {0.0,0.0,0.0};

  char *block_len[3] = {"1","2","3"};
  char err_msg[ MAX_LINE_BUFSIZE ];
  char buffer[ UF_UI_MAX_STRING_BUFSIZE ];
  char *feature_name = NULL;
  int err = 0;

  tag_t blk_obj;

  UF_CALL(UF_UI_open_listing_window());

  UF_CALL(UF_MODL_create_block1(sign, block_orig, block_len, &blk_obj));

  if(UF_CALL(UF_MODL_ask_feat_name(blk_obj,&feature_name)))
  {
    UF_get_fail_message(err,err_msg);
    sprintf(buffer, "Error: %s\n", err_msg);
    UF_UI_write_listing_window(buffer);
  }
  else
  {  
    UF_UI_write_listing_window(feature_name);
    UF_free(feature_name);
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
