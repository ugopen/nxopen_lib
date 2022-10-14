
/*=============================================================================
                 Copyright (c)  2001 Unigraphics Solutions, Inc.
                        Unpublished - All Rights Reserved
=============================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *   UF_CAMBND_append_bnd_from_curve                                          *
 *   UF_CAMBND_append_bnd_from_face                                           *
 *   UF_CAMBND_ask_boundaries                                                 *
 *   UF_CAMBND_ask_boundary_app_data                                          *
 *   UF_CAMBND_ask_boundary_data                                              *
 *   UF_CAMBND_ask_boundary_items                                             *
 *   UF_CAMBND_ask_item_app_data                                              *
 *   UF_CAMBND_ask_item_entity                                                *
 *   UF_CAMBND_delete_boundaries                                              *
 *   UF_CAMBND_delete_boundary                                                *
 *   UF_CAMBND_set_boundary_app_data                                          *
 *   UF_CAMBND_set_item_app_data                                              *
 *   UF_CAMBND_ask_boundary_group_data                                        *
 *   UF_CAMBND_set_boundary_group_data                                        *
 *   UF_CAMBND_ask_item_group_data                                            *
 *   UF_CAMBND_set_item_group_data                                            *
 *   UF_CAMBND_ask_item_udes                                                  *
 *   UF_CAMBND_delete_all_item_udes                                           *
 *   UF_CAMBND_append_item_ude                                                *
 *   UF_CAMBND_delete_item_ude                                                *
 *   UF_CAMBND_can_accept_item_ude                                            *
 *                                                                            *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example requires an open part, a manufacturing setup, and           *
 *   one or more highlighted geometry groups or operations.                   *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

/***************************** Include Files **********************************/
#include <stdlib.h>
#include <uf.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_ui_ont.h>
#include <uf_cambnd.h>
#include <uf_cam.h>
#include <uf_object_types.h>
#include <uf_disp.h>
#include <uf_ude.h>


#define     MAX_BND      20

/*******************************************************************/
static UF_CAMBND_boundary_data_p_t create_and_init_bnd_data
(
    UF_CAM_boundary_type_t   type,
    int                      plane_type,
    double                   *origin,
    double                   *matrix,
    UF_CAM_material_side_t   material_side,
    int                      ignore_holes,
    int                      ignore_islands,
    int                      ignore_chamfers,
    UF_CAMBND_app_data_p_t   app_data
);
static UF_CAMBND_app_data_p_t create_and_init_bnd_app_data(void);
static UF_CAMBND_group_data_p_t create_and_init_bnd_group_data(void);
static int init_proc1(UF_UI_selection_p_t select, void *user_data);
static int init_proc2(UF_UI_selection_p_t select, void *user_data);


/*******************************************************************/
static void do_cambnd_api(void)
{
    UF_CAMBND_boundary_data_p_t  bnd_data, bnd_data_list[MAX_BND];
    UF_CAMBND_app_data_p_t       app_data_list[MAX_BND]; 
    tag_t                        part_tag, *objects, entity_list[MAX_BND];
    int                          i, j, object_count, blank_count, blank_item_count;
    int                          type, subtype;
    UF_CAMBND_boundary_t         *blank_bnd_list;
    UF_CAMBND_item_t             *blank_item_list;
    logical                      rep;
    int                          ude_num;
    static char udevents[] [20] = { "spindle",
                                    "spindle_off"};                      
    UF_CAMBND_UDE_t              ude_obj, *udes;

    /* Get the displayed part. */
    part_tag = UF_PART_ask_display_part( );
    
    if( part_tag != null_tag )
    {
        /* Get the highlighted/selected objects from Navigation Tool. */
        UF_UI_ONT_ask_selected_nodes( &object_count, &objects ); 

        if (object_count > 0)
        {
            tag_t     eid, view;
            double    cursor[3], origin[3], matrix[9];
            int       entity_count, response;

            char      cue_face[]   = "Select faces";
            char      cue_edge[]   = "Select edges";
            char      title[]      = "Boundary Selection";

            entity_count = 0;

            /* Allow the user to select faces. */
            while (TRUE)
            {
                UF_UI_select_with_single_dialog(cue_face, title,
                                                UF_UI_SEL_SCOPE_NO_CHANGE, init_proc1, NULL,
                                                &response, &eid, cursor, &view);

                if (response == UF_UI_OBJECT_SELECTED)
                {                    
                    entity_list[entity_count] = eid;

                    /* Allocate the memory for the boundary data of an item without app data.  */
                    bnd_data_list[entity_count] = create_and_init_bnd_data(UF_CAM_boundary_type_closed,
                                                                           1, origin, matrix, 
                                                                           UF_CAM_material_side_out_right,
                                                                           0, 0, 0, NULL);

                    entity_count++;
                }
                else if (response == UF_UI_OK || response == UF_UI_CANCEL || 
                         response == UF_UI_BACK)
                {
                    /* Geometry selection is finished. */
                    break;
                }
            }

            /* Append the face boundaries. */
            if (entity_count > 0)
            {
                for(i=0; i<object_count; i++)
                {
                    UF_OBJ_ask_type_and_subtype(objects[i], &type, &subtype);

                    /* The object type must be Operation or Geometry Group. */
                    if( type == UF_machining_operation_type || type == UF_machining_geometry_grp_type)
                    {
                        for (j=0; j<entity_count; j++)
                        {
                            /***********************************************************************/
                            /*
                             * UF_CAMBND_append_bnd_from_face
                             */
                            /***********************************************************************/
                            UF_CAMBND_append_bnd_from_face(objects[i], UF_CAM_part, 
                                                           entity_list[j], bnd_data_list[j]);
                            UF_CAMBND_append_bnd_from_face(objects[i], UF_CAM_blank, 
                                                           entity_list[j], bnd_data_list[j]);
                            UF_CAMBND_append_bnd_from_face(objects[i], UF_CAM_check, 
                                                           entity_list[j], bnd_data_list[j]);
                            UF_CAMBND_append_bnd_from_face(objects[i], UF_CAM_trim, 
                                                           entity_list[j], bnd_data_list[j]);
                        }
                    }
                }
            }

            /* Free the boundary data. */
            for (i=0; i<entity_count; i++)
            {
                UF_free(bnd_data_list[i]);
            }

            entity_count = 0;
            
            /* Allow the user to select edges. */
            while (TRUE)
            {
                UF_UI_select_with_single_dialog(cue_edge, title,
                                                UF_UI_SEL_SCOPE_NO_CHANGE, init_proc2, NULL,
                                                &response, &eid, cursor, &view);

                if (response == UF_UI_OBJECT_SELECTED)
                {                    
                    entity_list[entity_count] = eid;
                    app_data_list[entity_count] = create_and_init_bnd_app_data();
                    entity_count++;
                }
                else if (response == UF_UI_OK || response == UF_UI_CANCEL || 
                         response == UF_UI_BACK)
                {
                    /* Geometry selection is finished. */
                    break;
                }
            }

            /* Append curve boundaries. */
            if (entity_count > 0)
            {
                bnd_data = create_and_init_bnd_data(UF_CAM_boundary_type_open,
                                                    1, origin, matrix, 
                                                    UF_CAM_material_side_out_right,
                                                    0, 0, 0, NULL);
                for(i=0; i<object_count; i++)
                {
                    UF_OBJ_ask_type_and_subtype(objects[i], &type, &subtype);

                    if( type == UF_machining_operation_type || 
                        type == UF_machining_geometry_grp_type)
                    {
                        /***********************************************************************/
                        /*
                         * UF_CAMBND_append_bnd_from_curve
                         */
                        /***********************************************************************/
                        UF_CAMBND_append_bnd_from_curve(objects[i], UF_CAM_part, entity_count, 
                                                        entity_list, bnd_data, app_data_list);
                        UF_CAMBND_append_bnd_from_curve(objects[i], UF_CAM_blank, entity_count, 
                                                        entity_list, bnd_data, app_data_list);
                        UF_CAMBND_append_bnd_from_curve(objects[i], UF_CAM_check, entity_count, 
                                                        entity_list, bnd_data, app_data_list);
                        UF_CAMBND_append_bnd_from_curve(objects[i], UF_CAM_trim, entity_count, 
                                                        entity_list, bnd_data, app_data_list);
                    }
                }
            
                /* Free memory. */
                for (i=0; i<entity_count; i++)
                {
                    UF_free(app_data_list[i]);
                }
                
                UF_free (bnd_data);
            }

            /***********************************************************************/
            /*
             * UF_CAMBND_ask_boundaries
             */
            /***********************************************************************/
            UF_CAMBND_ask_boundaries(objects[0], UF_CAM_blank, &blank_count, &blank_bnd_list);

            for (i=0; i<blank_count; i++)
            {
                UF_CAMBND_boundary_data_t boundary_data;
                UF_CAMBND_app_data_t      app_data;
                UF_CAMBND_group_data_p_t  ask_group_data, set_group_data;
                ask_group_data = create_and_init_bnd_group_data();
                set_group_data = create_and_init_bnd_group_data();
                ask_group_data->has_offset = 0;
                ask_group_data->offset = 0.0;

                /***********************************************************************/
                /*
                 * UF_CAMBND_ask_boundary_data
                 */
                /***********************************************************************/
                UF_CAMBND_ask_boundary_data(blank_bnd_list[i], &boundary_data);

                /***********************************************************************/
                /*
                 * UF_CAMBND_ask_boundary_app_data
                 */
                /***********************************************************************/
                UF_CAMBND_ask_boundary_app_data(blank_bnd_list[i], &app_data);

                /***********************************************************************/
                /*
                 * UF_CAMBND_set_boundary_app_data
                 */
                /***********************************************************************/
                UF_CAMBND_set_boundary_app_data(objects[0], UF_CAM_blank, blank_bnd_list[i], &app_data);

                /***********************************************************************/
                /*
                 * UF_CAMBND_set_boundary_group_data
                 */
                /***********************************************************************/
                UF_CAMBND_set_boundary_group_data(objects[0], UF_CAM_blank, blank_bnd_list[i], set_group_data);

                /***********************************************************************/
                /*
                 * UF_CAMBND_ask_boundary_group_data
                 */
                /***********************************************************************/
                UF_CAMBND_ask_boundary_group_data(blank_bnd_list[i], ask_group_data);

                /***********************************************************************/
                /*
                 * UF_CAMBND_ask_boundary_items
                 */
                /***********************************************************************/
                UF_CAMBND_ask_boundary_items(blank_bnd_list[i], &blank_item_count, &blank_item_list);

                for (j=0; j<blank_item_count; j++)
                {
                    tag_t                 entity;
                    UF_CAMBND_app_data_t  item_app_data;
                    UF_CAMBND_group_data_p_t  ask_item_group_data, set_item_group_data;
                    ask_item_group_data = create_and_init_bnd_group_data();
                    set_item_group_data = create_and_init_bnd_group_data();

                    /***********************************************************************/
                    /*
                     * UF_CAMBND_ask_item_entity
                     */
                    /***********************************************************************/
                    UF_CAMBND_ask_item_entity(blank_item_list[j], &entity);

                    /***********************************************************************/
                    /*
                     * UF_CAMBND_ask_item_app_data
                     */
                    /***********************************************************************/
                    UF_CAMBND_ask_item_app_data(blank_item_list[j], &item_app_data);


                    /***********************************************************************/
                    /*
                     * UF_CAMBND_set_item_app_data
                     */
                    /***********************************************************************/
                    UF_CAMBND_set_item_app_data(objects[0], UF_CAM_blank, blank_bnd_list[i],
                                                blank_item_list[j], NULL);

                    /***********************************************************************/
                    /*
                     * UF_CAMBND_set_item_group_data
                     */
                    /***********************************************************************/
                    UF_CAMBND_set_item_group_data(objects[0], UF_CAM_blank, blank_bnd_list[i], 
                                                  blank_item_list[j], set_item_group_data);

                    /***********************************************************************/
                    /*
                     * UF_CAMBND_ask_boundary_group_data
                     */
                    /***********************************************************************/
                    UF_CAMBND_ask_item_group_data(blank_item_list[j], ask_item_group_data);

                    /***********************************************************************/
                    /*
                     * UF_CAMBND_can_accept_ude
                     */
                    /***********************************************************************/
                    UF_CAMBND_can_accept_item_ude(blank_item_list[j], UF_CAMBND_UDE_START_SET, udevents[0], &rep);

                    if (rep)
                    {
                        /***********************************************************************/
                        /*
                         * UF_CAMBND_append_item_ude
                         */
                        /***********************************************************************/
                        UF_CAMBND_append_item_ude(blank_item_list[j],UF_CAMBND_UDE_START_SET, udevents[0], &ude_obj, &rep);

                        if (rep)
                            UF_UDE_set_double(ude_obj, "spindle_speed", 333.0);
                    }
                    UF_CAMBND_can_accept_item_ude(blank_item_list[j], UF_CAMBND_UDE_END_SET, udevents[0], &rep);
                    if (rep)
                    {
                        UF_CAMBND_append_item_ude(blank_item_list[j],UF_CAMBND_UDE_END_SET, udevents[1], &ude_obj, &rep);
                    }

                    /***********************************************************************/
                    /*
                     * UF_CAMBND_ask_item_udes
                     */
                    /***********************************************************************/
                    UF_CAMBND_ask_item_udes(blank_item_list[j], UF_CAMBND_UDE_START_SET, &ude_num, &udes);

                    /***********************************************************************/
                    /*
                     * UF_CAMBND_delete_item_ude
                     */
                    /***********************************************************************/
                    UF_CAMBND_delete_item_ude(blank_item_list[j], UF_CAMBND_UDE_END_SET, ude_obj);

                    /***********************************************************************/
                    /*
                     * UF_CAMBND_delete_all_item_udes
                     */
                    /***********************************************************************/
                    UF_CAMBND_delete_all_item_udes(blank_item_list[j], UF_CAMBND_UDE_START_SET);

                }

                /***********************************************************************/
                /*
                 * UF_CAMBND_delete_boundary
                 */
                /***********************************************************************/
                
                UF_CAMBND_delete_boundary(objects[0], UF_CAM_blank, blank_bnd_list[i]);
            }

            /***********************************************************************/
            /*
             * UF_CAMBND_delete_boundaries
             */
            /***********************************************************************/

            UF_CAMBND_delete_boundaries(objects[0], UF_CAM_part);
            UF_CAMBND_delete_boundaries(objects[0], UF_CAM_check);
            UF_CAMBND_delete_boundaries(objects[0], UF_CAM_trim);

        }        
    }

    return;
}


/* Selection initialization procedures.*/
static int init_proc1
(
    UF_UI_selection_p_t select,
    void* user_data
)
{
    int num_triples = 1;
    UF_UI_mask_t mask_triples[] = {UF_solid_type, 0, UF_UI_SEL_FEATURE_ANY_FACE};

    /* enable only lines and edges */
    if((UF_UI_set_sel_mask(select,
                           UF_UI_SEL_MASK_CLEAR_AND_ENABLE_SPECIFIC,
                           num_triples, mask_triples)) == 0)
    {
        return (UF_UI_SEL_SUCCESS);
    }
    else
    {
        return (UF_UI_SEL_FAILURE);
    }
}

static int init_proc2
(
    UF_UI_selection_p_t select,
    void* user_data
)
{
    int num_triples = 1;
    UF_UI_mask_t mask_triples[] = {UF_solid_type, 0, UF_UI_SEL_FEATURE_ANY_EDGE};

    /* enable only lines and edges */
    if((UF_UI_set_sel_mask(select,
                           UF_UI_SEL_MASK_CLEAR_AND_ENABLE_SPECIFIC,
                           num_triples, mask_triples)) == 0)
    {
        return (UF_UI_SEL_SUCCESS);
    }
    else
    {
        return (UF_UI_SEL_FAILURE);
    }
}

static UF_CAMBND_boundary_data_p_t create_and_init_bnd_data
(
    UF_CAM_boundary_type_t   type,
    int                      plane_type,
    double                   *origin,
    double                   *matrix,
    UF_CAM_material_side_t   material_side,
    int                      ignore_holes,
    int                      ignore_islands,
    int                      ignore_chamfers,
    UF_CAMBND_app_data_p_t   app_data
)
{
    UF_CAMBND_boundary_data_p_t bnd_data;
    int                         i, err_code;

    bnd_data = (UF_CAMBND_boundary_data_p_t) UF_allocate_memory(
                                             sizeof(UF_CAMBND_boundary_data_t), &err_code);

    bnd_data->boundary_type = type;
    bnd_data->plane_type = plane_type ;
    for (i=0; i<3; i++)
        bnd_data->origin[i] = origin[i] ;
    for (i=0; i<9; i++)
        bnd_data->matrix[i] = matrix[i] ;
    bnd_data->material_side = material_side;
    bnd_data->ignore_holes = ignore_holes ;
    bnd_data->ignore_islands = ignore_islands ; 
    bnd_data->ignore_chamfers = ignore_chamfers ;    
    bnd_data->app_data = app_data;

    return(bnd_data);
}

static UF_CAMBND_app_data_p_t create_and_init_bnd_app_data(void)
{
    UF_CAMBND_app_data_p_t  app_data; 
    int                     err_code;

    app_data = (UF_CAMBND_app_data_p_t) UF_allocate_memory(
                                          sizeof(UF_CAMBND_app_data_t), &err_code);

    if (err_code)
return(NULL);

    /* Set flags. */
    app_data->has_stock = 1;
    app_data->has_tolerances = 1 ;
    app_data->has_feedrate = 0 ;
    app_data->has_blank_distance = 0;
    app_data->has_tool_position = 0;
    
    /* Set values. */
    app_data->stock = 0.1 ;
    app_data->tolerances[0] = 0.1 ;
    app_data->tolerances[1] = 0.1 ;
    app_data->feedrate_unit = UF_CAM_feedrate_unit_per_minute ;
    app_data->feedrate_value = 0.1 ;
    app_data->blank_distance = 0.0 ;
    app_data->tool_position = UF_CAM_tool_position_tanto;

    return(app_data);
}

static UF_CAMBND_group_data_p_t create_and_init_bnd_group_data(void)
{
    UF_CAMBND_group_data_p_t  group_data; 
    int                       err_code;

    group_data = (UF_CAMBND_group_data_p_t) UF_allocate_memory(
                                          sizeof(UF_CAMBND_group_data_t), &err_code);

    if (err_code)
return(NULL);

    /* Set flags. */
    group_data->has_offset = 1;
    /* Set values. */
    group_data->offset = 0.1 ;

    return (group_data);
}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
{
    UF_initialize();

    do_cambnd_api();

    UF_terminate();
}

int ufusr_ask_unload(void)
{
 return (UF_UNLOAD_IMMEDIATELY);
}

