/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_ASSEM_create_explosion                                          *
 *                                                                            *
 * PROGRAM DESCRIPTION - 
 *   Creates an explosion in the specified display part;  the components in   * 
 *   the assembly are initially at their real assembly positions, and the     *
 *   explosion is initially not used in any views.                            *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <uf_defs.h>
#include <uf.h>
#include <uf_part.h>   
#include <uf_assem.h>   

static int explode_work_subassembly( char* explosion_name,
                                     double standard_offset );

static int explode_assy_below_component(tag_t display_part_tag,
                                         tag_t explosion_tag, 
                                         tag_t component_tag, 
                                         double standard_offset);

/*ARGSUSED*/
extern void ufusr(char* param, int* retcod, int param_len)
{
  int error = 0;

  UF_initialize();

  error = explode_work_subassembly("MY_EXPLOSION", 1.0);

  UF_terminate();

  *retcod = error;
}

static int explode_work_subassembly( char* explosion_name, 
                                     double standard_offset )
{
  tag_t work_occ_tag;
  tag_t display_part_tag;
  int error;
  tag_t explosion_tag;

  display_part_tag = UF_PART_ask_display_part();

  /* Get the component tag for the work part. */
  work_occ_tag = UF_ASSEM_ask_work_occurrence();

  /* If not working in context, there is no work component. */
  if (work_occ_tag == NULL_TAG) 
  { 
    work_occ_tag = UF_ASSEM_ask_root_part_occ(display_part_tag);
  }

  error = UF_ASSEM_create_explosion ( display_part_tag, 
                                      explosion_name, 
                                      &explosion_tag );  
  if (error != 0) return error;

  error = explode_assy_below_component( display_part_tag,
                                        explosion_tag,
                                        work_occ_tag,
                                        standard_offset );
  return error;
}


static int explode_assy_below_component(tag_t display_part_tag, 
                                        tag_t explosion_tag, 
                                        tag_t component_tag, 
                                        double standard_offset)
{
  int i, child_count; 
  tag_p_t child_tags;
  int error;

  child_count = 
        UF_ASSEM_ask_part_occ_children(component_tag, &child_tags);

  for(i = 0; i < child_count; i++)
  {
    double mc_transform[4][4] =      
                         {{1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1}};
    double vector[3];

    error = UF_ASSEM_ask_explosion_vector(child_tags[i], vector);
    if (error == 0)
    {
       /* The output vector is guaranteed to be normalized 
          (adds up to 1.0)
       */
      mc_transform[0][3] = standard_offset * vector[0];
      mc_transform[1][3] = standard_offset * vector[1];
      mc_transform[2][3] = standard_offset * vector[2];
          
      error = UF_ASSEM_explode_component(explosion_tag,
                                         child_tags[i], 
                                         mc_transform);
      if (error != 0) return error;
    }    
  
    error = explode_assy_below_component(display_part_tag,
                                         explosion_tag, 
                                         child_tags[i],
                                         standard_offset);
    if (error != 0) return error;
  }

  if (child_count > 0) UF_free(child_tags);

  return 0;
}
