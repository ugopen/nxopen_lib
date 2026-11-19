/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API program:         *
 *                                                                            *
 *         UF_layer_create_category                                           *
 *         UF_layer_edit_category_name                                        *
 *         UF_layer_edit_category_descr                                       *
 *         UF_layer_edit_category_layer                                       *
 *         UF_layer_ask_category_info                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code creates a    *
 *   category, edits and then queries the information.                        *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_layer.h>
#include <uf_obj.h>


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
  UF_LAYER_category_info_t cat;
  tag_t cat_tag;
  int i;
  int count;
  
 
  /* Create a new category */
  strcpy(cat.name, "ASM_15");
  strcpy(cat.descr, "Assembly Line 15");
  count = 1;
  for (i = 0; i < 256; ++i)
      {
      if (count == 5)
          {
          cat.layer_mask[i] = TRUE;
          count = 1;
          }
      else
          cat.layer_mask[i] = FALSE;
      count++;
      }
  UF_CALL(UF_LAYER_create_category(&cat, &cat_tag));
  /* Edit the category */
  UF_CALL(UF_LAYER_edit_category_name(cat_tag, "ASM_20"));
  UF_CALL(UF_LAYER_edit_category_descr(cat_tag, "Assembly Line 20"));
  for (i = 0; i < 256; ++i)
      cat.layer_mask[i] = !cat.layer_mask[i];
  UF_CALL(UF_LAYER_edit_category_layer(cat_tag, cat.layer_mask));
  /* Get the category information */
  UF_CALL(UF_LAYER_ask_category_info(cat_tag, &cat));
  printf("\nCategory name is: %s\n",cat.name);
  printf("\nCategory description is %s\n",cat.descr);
  for(i = 0; i < 256; i++)
  {
     printf("Category layer_mask[%d] = %d\n",i,cat.layer_mask[i]);
  }
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
