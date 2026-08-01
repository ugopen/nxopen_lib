/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_PS_ask_object_of_ps_tag                                         *
 *         UF_PS_ask_ps_tag_of_object                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *    The following example creates a new "ps_sample" part. The example code  *
 *    creates a block, gets the solid body object identifier of the block     *
 *    feature, and then converts this identifier to its corresponding         *
 *    Parasolid tag in preparation for calling Parasolid solid modeler        *
 *    routines. The Parasolid tag is then converted back to the object        *
 *    identifier of the block.                                                *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_ps.h>

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
  int  units = UF_PART_METRIC;
  char *part_name = "ps_sample";
  char buffer[133];
  char *block_len[3] = {"10","10","5"};
  tag_t  part,block_feat_id,block_body_id,ps_tag, ug_tag;
  double block_origin[3] = {0.0,0.0,0.0};
  UF_FEATURE_SIGN sign = UF_NULLSIGN;

  /* Create a new part. */
  UF_CALL(UF_PART_new(part_name,units,&part));

  /*create a block that is 10 x 10 x 5*/
  UF_CALL(UF_MODL_create_block1(sign,block_origin,block_len,
                          &block_feat_id));

  /* Convert feature object id to body object id. */
  UF_MODL_ask_feat_body(block_feat_id,&block_body_id);


  /* Interface with the Parasolid routines using the ps tag. */

  /* Open the Information Window */
  UF_UI_open_listing_window();

  /* Obtain the Parasolid identifier for the given UG tag. */
  if(UF_CALL(UF_PS_ask_ps_tag_of_object(block_body_id,
               &ps_tag)))
  {
    return;
  } 
  if(UF_CALL(UF_PS_ask_object_of_ps_tag(ps_tag, &ug_tag)))
  {
    return;
  }

  /* Print a report on tag information. */
  sprintf(buffer,"\nThe Parasolid Tag is: %d", ps_tag);
  UF_UI_write_listing_window(buffer);
  sprintf(buffer, "\nThe UG tag is: %d", ug_tag);
  UF_UI_write_listing_window(buffer);
  sprintf(buffer, "\nThe block feature tag is: %d", block_feat_id);
  UF_UI_write_listing_window(buffer);
  sprintf(buffer, "\nThe solid body tag is: %d", block_body_id);
  UF_UI_write_listing_window(buffer);
  UF_PART_save();
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
