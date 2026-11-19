/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_promotion                                           *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates base_part.prt and assem_prt.prt. The code  *
 *   creates a block in the base part and adds this base part to the assembly *
 *   part. It then finds the body occurrence in the assembly part and         *
 *   promotes it.                                                             *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_obj.h>
#include <uf_assem.h>
#include <uf_part.h>
#include <uf.h>

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
  int err = 0;
  char *base_part_name = "base_part";
  char *assem_part_name = "assem_part";
  char *refset_name = NULL;
  char *instance_name = NULL;                                                                                                                                  
  tag_t base_part_tag, assem_part_tag;
  tag_t inst_tag, block_tag, prom_feat_tag, dummy_feat_tag;
  tag_t *part_occs, dumb_tag;
  tag_t base_body, prom_body, solid_occ; 
  tag_t  *instance_path;
  int  num_instances;
  logical  full_path;
  double block_pt[] = {0.0, 0.0, 0.0};
  char *block_len[] = {"10", "10", "1"};    
  int layer = 0;
  double origin[] = {0.0, 0.0, 0.0};
  double abs_csys[] = {1.0, 0.0, 0.0, 0.0, 1.0, 0.0};
  UF_PART_load_status_t load_status; 
  int i, count, num_occs;
  uf_list_p_t face_list;
 
  UF_CALL(UF_PART_new(base_part_name, UF_PART_ENGLISH, &base_part_tag));
  UF_CALL(UF_MODL_create_block1(UF_NULLSIGN, block_pt, block_len, &block_tag));
  UF_CALL(UF_MODL_ask_feat_body (block_tag, &base_body));
  UF_CALL(UF_PART_new(assem_part_name, UF_PART_ENGLISH, &assem_part_tag));
  UF_ASSEM_add_part_to_assembly(assem_part_tag, base_part_name, refset_name, 
                                instance_name, origin, abs_csys, layer,   
                                &inst_tag, &load_status);

  num_occs = UF_ASSEM_ask_occs_of_part (assem_part_tag, base_part_tag, &part_occs);
  if (num_occs != 1)
  {
     fprintf(stderr, "Unexpected number of part occs: %d\n", num_occs);
 
  }
  solid_occ = UF_ASSEM_find_occurrence (part_occs[0], base_body);
  if(solid_occ == NULL_TAG)
  {
     fprintf(stderr, "Cannot find occurrence for base body\n");
     exit(1);
  }
  err = UF_MODL_create_promotion(solid_occ, &prom_feat_tag);
  if(err)
  {
     fprintf(stderr, "Promotion operation failed\n");
     exit(1);
  }
  UF_MODL_ask_solid_of_prom_feat(prom_feat_tag, &prom_body);
  if(!UF_OBJ_is_object_a_promotion (prom_body))
  {
     fprintf(stderr, "Promotion operation failed\n");
     exit(1);
  }
  UF_MODL_ask_prom_feat_of_solid (prom_body, &dummy_feat_tag);
  if (dummy_feat_tag != prom_feat_tag)
  {
     fprintf(stderr, "Promotion solid to feature link failed\n"); 
     exit(1);
  }
  full_path = true;
  UF_MODL_ask_promotion_path (prom_body, full_path, &instance_path, &num_instances);
  if (num_instances != 1 || instance_path[0] != inst_tag)
  {
     fprintf(stderr, "Promotion path incorrect\n"); 
     exit(1);
  }
  UF_free (instance_path);
  UF_MODL_prom_map_object_up (base_body, prom_feat_tag, &dumb_tag);
  if(dumb_tag != prom_body)
  {
     fprintf(stderr, "Promotion body map up failed\n");
     exit(1);
  }
  UF_MODL_prom_map_object_down(prom_body, &dumb_tag);
  if(dumb_tag != base_body)
  {
     fprintf(stderr, "Promotion body map down failed\n");
     exit(1);
  }
  UF_MODL_ask_body_faces (base_body, &face_list);
  UF_MODL_ask_list_count (face_list, &count);
  for(i=0; i < count; i++)
  {
     tag_t prom_face, base_face, base_face1; 
     UF_MODL_ask_list_item (face_list, i, &base_face);
        
     UF_MODL_prom_map_object_up (base_face, prom_feat_tag, &prom_face);
     UF_MODL_prom_map_object_down (prom_face, &base_face1);
     if( base_face != base_face1)
     {
        fprintf(stderr, "Promotion face map not valid\n");
        exit(1);
     }
  }
  UF_MODL_delete_list (&face_list);
  UF_free (part_occs);
  
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
