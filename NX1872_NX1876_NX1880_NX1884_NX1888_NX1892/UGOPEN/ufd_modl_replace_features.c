/*==============================================================================

             Copyright (c) 1999,2000 Unigraphics Solutions Inc.
                          Unpublished - All rights reserved
================================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_replace_features()                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates replace_features.prt via code that         *
 *   invokes commands to create a cylinder, a cone, and an offset face        *
 *   feature on the cylinder. The program then invokes commands to replace    *
 *   the cylinder with a copy of the cone after prompting the  users for      *
 *   faces on the cone that correspond to the faces on the cylinder that are  *
 *   used by the offset. The replace feature command also reparents the       *
 *   offset feature (which was a child of the original cylinder) to the       *
 *   copied cone feature.                                                     *
 *                                                                            *
 *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_disp.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_obj.h>
#include <uf_object_types.h>

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
    int    units= UF_PART_METRIC;
    char   *part_name="replace_features";
    tag_t  part_tag,
           cyl_tag,
           cone_tag,
           offset_tag;
    double origin[3] = { 0.0, 0.0, 0.0 };
    char   *height="1.0";
    char   *diam="1.0";
    char   *cone_dia[2] = {"1.0", "2.0"};
    double direction[3] = { 0.0, 0.0, 1.0 };
    char   *offset = "0.1";
    uf_list_p_t flist;
    UF_MODL_replace_features_t * replm_map=NULL;
    int                          n_replm_map, i;

    UF_PART_new(part_name, units, &part_tag);

    /*  Create a cone and a cylinder
    */
    UF_CALL(UF_MODL_create_cyl1(UF_NULLSIGN, origin, height, diam, direction, &cyl_tag));
    UF_CALL(UF_MODL_create_cone1(UF_NULLSIGN,origin, height, cone_dia, direction, &cone_tag));
    
    /*  Offset faces of the cylinder by 0.1"
    */
    UF_CALL(UF_MODL_create_list(&flist));
    UF_CALL(UF_MODL_put_list_item(flist,cyl_tag));
    UF_CALL(UF_MODL_create_feature_offset(offset, flist, &offset_tag));
    UF_CALL(UF_MODL_delete_list(&flist));

    /*  Get a list of entities that must be mapped. This will be all the faces of the 
        cylinder that are being used by the offset feature
    */
    UF_CALL(UF_MODL_replace_features(&cyl_tag, 1,
                                     &cone_tag, 1,
                                     true,
                                     false,
                                     &replm_map,
                                     &n_replm_map ));

    /* Since the parents of the offset will be replaced to faces on the copy of the cone feature,
       Get the faces on the replacement feature from the user for the offset.
    */
    for (i=0; i<n_replm_map; i++)
    {
        char *message="Select object on cone that corresponds to the highlighted object";
        UF_UI_selection_options_t opts;
        UF_UI_mask_t mask;
        tag_t object, view;
        double cursor[3];
        int type, subtype, response;
        
        UF_CALL(UF_DISP_set_highlight( replm_map[i].original_entity, 1));
        
        /*  Set up selection options for the replacement entity
        */
        UF_CALL(UF_OBJ_ask_type_and_subtype(replm_map[i].original_entity, &type, &subtype));
        opts.other_options = 0;
        opts.reserved = NULL;
        opts.num_mask_triples = 1;
        opts.mask_triples = &mask;
        
        if (subtype == UF_solid_face_subtype)
            opts.mask_triples->solid_type = UF_UI_SEL_FEATURE_ANY_FACE;
        else if (subtype == UF_solid_edge_subtype)
            opts.mask_triples->solid_type = UF_UI_SEL_FEATURE_ANY_EDGE;
        opts.mask_triples->object_type = type;  
        opts.mask_triples->object_subtype = subtype;
        opts.scope = UF_UI_SEL_SCOPE_WORK_PART;
        
        /*  Select the replacement entity
        */
        UF_CALL(UF_UI_select_single(message,&opts,&response, &object,cursor,&view));
        UF_CALL(UF_DISP_set_highlight( replm_map[i].original_entity, 0));
        UF_CALL(UF_DISP_set_highlight( replm_map[i].replacement_entity, 0));
        if (response==1 || response==2)
            break;
        
        replm_map[i].replacement_entity=object;
    }
    /*  Replace the cylinder with a copy of the cone
    */
    if (i==n_replm_map)
        UF_CALL(UF_MODL_replace_features(&cyl_tag, 1,
                                         &cone_tag, 1,
                                         false,
                                         true,
                                         &replm_map,
                                         &n_replm_map ));    

    UF_free ( replm_map );

    
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
