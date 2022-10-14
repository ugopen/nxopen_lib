/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_exps_of_part                                           *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example program requires a blank, open part. The example   *
 *   creates two blocks then queries the part for expressions and prints the  *
 *   results.                                                                 *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_ui.h>
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
    double block_orig[3] = {0.0,0.0,0.0};
    double block_orig1[3] = {0.5,0.5,0.5};
    char *block_len[3] = {"1","2","3"};
    tag_t blk_obj,blk_obj1;
    int ifail=0;
    char *string;
    tag_t *exps;
    int number_of_exps=0,i;
    char buf[ UF_UI_MAX_STRING_BUFSIZE ];
    char err_msg[ MAX_LINE_BUFSIZE ];
    tag_t part; 
    
    UF_CALL(UF_MODL_create_block1(UF_NULLSIGN,block_orig,
                                  block_len,&blk_obj));
    UF_CALL(UF_MODL_create_block1(UF_NULLSIGN,block_orig1,
                                  block_len,&blk_obj1));

    UF_CALL(UF_UI_open_listing_window());

    if((part=UF_PART_ask_display_part()) == NULL_TAG)
    {
        UF_UI_write_listing_window("Failed to get part tag\n");
        return;
    }
        

    ifail=UF_MODL_ask_exps_of_part(part,&number_of_exps,&exps);
    if(ifail)
    {
      UF_get_fail_message(ifail,err_msg);
      sprintf(buf,"Error: %s\n", err_msg);
      UF_UI_write_listing_window(buf);
    }
    else
    {
      sprintf(buf,"number_of_exps=%d\n",number_of_exps);
      UF_UI_write_listing_window(buf);
      UF_UI_write_listing_window("Asking expression strings\n");

      for(i=0;i<number_of_exps;i++)
      {
        ifail=UF_MODL_ask_exp_tag_string(exps[i],&string);
        if(ifail)
        {
          UF_get_fail_message(ifail, err_msg);
          sprintf(buf, "Error: %s\n", err_msg);
          UF_UI_write_listing_window(buf);
        }
        else
        {
          sprintf(buf,"Expression %d: %s\n",i,string);
          UF_UI_write_listing_window(buf);
          UF_free(string);
        }
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
