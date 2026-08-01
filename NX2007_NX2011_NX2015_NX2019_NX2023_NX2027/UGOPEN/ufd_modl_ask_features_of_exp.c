/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_features_of_exp                                        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a work part with expressions. The example *
 *   finds each feature at least once by asking the related features of every *
 *   expression in the part.                                                  *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <uf.h>
#include <uf_defs.h>
#include <stdio.h>
#include <uf_modl.h>
#include <uf_assem.h>

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
  int i,j, num_exps = 0;
  tag_t  *oexps;
  tag_t part;
  int num_feats;
  tag_t *feats;
 
  char *string;
  char *feat_type;
  char *feat_name;

/* Test UF_MODL_ask_features_of_exp */
  if( NULL_TAG != (part = UF_ASSEM_ask_work_part()))
  {
    UF_CALL(UF_MODL_ask_exps_of_part(part, &num_exps, &oexps));
    printf ("Total number of expressions in part = %d\n", num_exps);
    for (i=0; i<num_exps; i++)
    {
      UF_CALL(UF_MODL_ask_exp_tag_string(oexps[i], &string));

      printf("\nExpression #%d: %s\n",i, string);
    
      UF_CALL(UF_MODL_ask_features_of_exp(oexps[i], &num_feats,
                                           &feats));
    
      if (num_feats > 0) 
      {

        printf ("Number of times expression %s is used = %d\n",
                 string, num_feats);
        printf ("The following features are affected:\n");
        for (j=0; j<num_feats; j++)
        {
          UF_CALL(UF_MODL_ask_feat_name(feats[j], &feat_name));
          UF_CALL(UF_MODL_ask_feat_type(feats[j], &feat_type));
          printf("Feature %u is named %s and is of type %s\n",
                 feats[j], feat_name, feat_type);
          UF_free(feat_name);
          UF_free(feat_type);
        }
        UF_free(feats);
      }
      UF_free(string);
    }
    if(num_exps > 0)
    {
      UF_free(oexps);
    }
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
