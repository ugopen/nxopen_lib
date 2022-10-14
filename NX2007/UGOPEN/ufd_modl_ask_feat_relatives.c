/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_feat_relatives                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example program requires a work part with at least one feature. The *
 *   example extracts the features of a given solid body via                  *
 *   UF_MODL_ask_body_feats. For each feature on the solid, the program       * 
 *   extracts all the relatives (parents and children). The program then      *
 *   prints a report to the listing window.                                   *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <uf_defs.h>
#include <uf_assem.h>
#include <uf_modl.h>
#include <uf.h>
#include <stdio.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <string.h>

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

  int index, inx;
  int num_parents, num_children;
  int irc;
  int enttype;

  tag_t feat1;
  tag_t master_feature;
  tag_t *parent_array, *children_array;
  tag_t part_tag;

  char err_messg[133];
  char *feat_type;

  feat1 = 0;
  master_feature = 0;
  index = 0;
  enttype = UF_feature_type;

  /* Get the tag of the work part */
  part_tag = UF_ASSEM_ask_work_part();

  /* Cycle through all the features in the part */
  do
  {
    UF_OBJ_cycle_objs_in_part(part_tag, enttype, &feat1);
    if(feat1 == NULL_TAG) break;

/* Get the feature type */
    irc = UF_MODL_ask_feat_type(feat1,&feat_type);
    printf("\nfeature %d = %u is of type %s\n",
                index,feat1,feat_type);
    ++index;

/* If the feature is an INSTANCE, then get the master feature and its type */
    if (!strcmp(feat_type,"INSTANCE"))
    {
       irc = UF_MODL_ask_master(feat1,&master_feature);
       irc = UF_MODL_ask_feat_type(master_feature,&feat_type);
       printf(" master feature %u is of type = %s\n",master_feature,feat_type);
    }

    irc = UF_MODL_ask_feat_relatives(feat1,&num_parents,
                &parent_array,&num_children,&children_array);
    if(irc != 0)
    {
       UF_get_fail_message(irc,err_messg);
       printf("error in UF_MODL_ask_feat_relatives =%s\n",err_messg);
    }
    else
    {
       printf("  parent array for %u contains %d members:\n",
                               feat1, num_parents);
       if(num_parents > 0)
       {
         for (inx = 0;inx < num_parents; inx++)
         {
           irc = UF_MODL_ask_feat_type(parent_array[inx],
                              &feat_type);
           printf("  parent id %d = %u is of feature type %s\n",
                       inx,parent_array[inx],feat_type);
         }
       }
       printf("  children array for feature %u contains %d members:\n",
                                 feat1, num_children);
      if(num_children > 0)
      {
        for (inx = 0;inx < num_children; inx ++)
        {
           irc = UF_MODL_ask_feat_type(children_array[inx],
                              &feat_type);
           printf("    child id %d = %u is of feature type %s\n",
                       inx,children_array[inx],feat_type);
         }
       }
    } /* end of else */

    if(num_parents > 0) 
    {
      UF_free(parent_array);
    }
    if(num_children > 0)
    {
      UF_free(children_array);
    }

  }while(feat1);

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
