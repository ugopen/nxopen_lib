
/*=============================================================================
                 Copyright (c)  2001 Unigraphics Solutions, Inc.
                        Unpublished - All Rights Reserved
=============================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *   UF_CAMGEOM_append_items                                                  *
 *   UF_CAMGEOM_ask_items                                                     *
 *   UF_CAMGEOM_delete_geometry                                               *
 *   UF_CAMGEOM_ask_item_entity                                               *
 *   UF_CAMGEOM_ask_item_app_data                                             *
 *   UF_CAMGEOM_set_item_app_data                                             *
 *   UF_CAMGEOM_delete_item                                                   *
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
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_ui_ont.h>
#include <uf_disp.h>
#include <uf_obj.h>

#include <uf_cam.h>
#include <uf_camgeom.h>

#define  MAX_CAMGEOM   20

static int init_proc(UF_UI_selection_p_t select, void *user_data);

static void set_camgeom_app_data(tag_t item, int geom_type,int num_app_data,
    UF_CAMGEOM_app_data_p_t *app_data);

static void do_camgeom_api(void)
{
    UF_CAMGEOM_app_data_p_t app_data_list[MAX_CAMGEOM] = {0};
    tag_t                   *objects = NULL, entity_list[MAX_CAMGEOM] = {0};
    int                     i, entity_count = 0, object_count,
                                err_code, type, subtype;

    char                    title[] = "Geometry Selection";
    char                    cue[] = "Select a body or a face";
    int                     response;
    tag_t                   eid, view;
    double                  cursor[3];



    if( UF_PART_ask_display_part() != null_tag )
    {
        /* Get the highlighted/selected objects from Navigation Tool. */
        UF_UI_ONT_ask_selected_nodes( &object_count, &objects ); 

        if (object_count > 0)
        {
            entity_count = 0;

            /* Allow the user to select the faces and bodies. */
            while (TRUE)
            {
                UF_UI_select_with_single_dialog(cue,title,
                                                UF_UI_SEL_SCOPE_NO_CHANGE, init_proc, NULL,
                                                &response, &eid, cursor, &view);

                if (response == UF_UI_OBJECT_SELECTED)
                {
                    entity_list[entity_count] = eid;

/* Allocate the memory for the application data of an item.  This will be
    filled in later.  */
                    app_data_list[entity_count] =
                        (UF_CAMGEOM_app_data_p_t)UF_allocate_memory(
                        sizeof(UF_CAMGEOM_app_data_t),&err_code);

                    entity_count++;
                }
                else if (response == UF_UI_OK || response == UF_UI_CANCEL || 
                         response == UF_UI_BACK)
                {
                    /* Geometry selection is finished. */
                    break;
                }
            }

            if (entity_count > 0)
            {
                UF_CAMGEOM_item_t     *items;
                int                   item_count;

                for( i = 0; i < object_count; i++ )
                {
                    UF_OBJ_ask_type_and_subtype( objects[i], &type, &subtype );
                    if( type == UF_machining_operation_type ||
                        type == UF_machining_geometry_grp_type)
                    {

/***********************************************************************/
/*
 * UF_CAMGEOM_append_items
 */
/***********************************************************************/
                        set_camgeom_app_data(objects[i],UF_CAM_part,entity_count,
                            app_data_list);
                        UF_CAMGEOM_append_items(objects[i], UF_CAM_part, entity_count, 
                                                entity_list, app_data_list);

                        set_camgeom_app_data(objects[i],UF_CAM_blank,entity_count,
                            app_data_list);
                        UF_CAMGEOM_append_items(objects[i], UF_CAM_blank, entity_count, 
                                                entity_list, app_data_list);

                        set_camgeom_app_data(objects[i],UF_CAM_check,entity_count,
                            app_data_list);
                        UF_CAMGEOM_append_items(objects[i], UF_CAM_check, entity_count, 
                                                entity_list, app_data_list);

                        set_camgeom_app_data(objects[i],UF_CAM_cut_area,entity_count,
                            app_data_list);
                        UF_CAMGEOM_append_items(objects[i], UF_CAM_cut_area, entity_count, 
                                                entity_list, NULL);                
                    }
                }
            
                /***********************************************************************/
                /*
                 * UF_CAMGEOM_ask_items
                 */
                /***********************************************************************/
                
                UF_CAMGEOM_ask_items(objects[0], UF_CAM_part, &item_count, &items);

                if (item_count > 0)
                {
                    UF_CAMGEOM_app_data_t app_data;
                    tag_t                 entity;

                    /***********************************************************************/
                    /*
                     * UF_CAMGEOM_ask_item_entity
                     */
                    /***********************************************************************/

                    UF_CAMGEOM_ask_item_entity(items[0], &entity);

                    /***********************************************************************/
                    /*
                     * UF_CAMGEOM_ask_item_app_data
                     */
                    /***********************************************************************/

                    UF_CAMGEOM_ask_item_app_data(items[0], &app_data);

                    /***********************************************************************/
                    /*
                     * UF_CAMGEOM_set_item_app_data
                     */
                    /***********************************************************************/
                    
                    UF_CAMGEOM_set_item_app_data(objects[0], UF_CAM_part, items[0], NULL);
                    
                    /***********************************************************************/
                    /*
                     * UF_CAMGEOM_delete_item
                     */
                    /***********************************************************************/

                    UF_CAMGEOM_delete_item(objects[0], UF_CAM_part, items[0]);

                }

                /***********************************************************************/
                /*
                 * UF_CAMGEOM_delete_geometry
                 */
                /***********************************************************************/

                UF_CAMGEOM_delete_geometry(objects[0], UF_CAM_part);
                UF_CAMGEOM_delete_geometry(objects[0], UF_CAM_blank);
                UF_CAMGEOM_delete_geometry(objects[0], UF_CAM_check);
                UF_CAMGEOM_delete_geometry(objects[0], UF_CAM_cut_area);

            }
        }
    }

/* Free the allocated memory and turn off the highlighting of the selected objects. */
    for (i=0; i<entity_count; i++)
    {
        UF_free (app_data_list[i]);
        UF_DISP_set_highlight(entity_list[i],0);
    }

    UF_free (objects);

    return;
}


/* selection initialization procedure */
static int init_proc
(
    UF_UI_selection_p_t select,
    void* user_data
)
{
    int num_triples = 3;
    UF_UI_mask_t mask_triples[] = {
         UF_line_type, 0, 0,
         UF_solid_type, 0, UF_UI_SEL_FEATURE_ANY_FACE,
         UF_solid_type, 0, UF_UI_SEL_FEATURE_BODY};

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


static void set_camgeom_app_data
(
    tag_t item,
    int geom_type,
    int num_app_data,
    UF_CAMGEOM_app_data_p_t *app_data_list
)
{
    int type,subtype,i;
    UF_CAMGEOM_app_data_p_t app_data;

/*  get the type and subtype of the target object to determine what
    type of application data is allowed.  */
    UF_OBJ_ask_type_and_subtype(item,&type,&subtype);

/*  cycle through the application data list, setting each as needed.  */
    for (i = 0; i < num_app_data; i++)
    {
        app_data = app_data_list[i];

/*  start by turning all application data flags off.  */
        app_data->has_stock = 0;
        app_data->has_cut_stock = 0;
        app_data->has_tolerances = 0 ;
        app_data->has_feedrate = 0 ;
        app_data->has_offset = 0;
        app_data->has_avoidance_type = 0 ;

/*  check for Mill geometry group.  */
        if (type == UF_machining_geometry_grp_type &&
            subtype == UF_mill_geom_featr_subtype &&
            geom_type == UF_CAM_part)
        {
            app_data->has_offset = 1;
            app_data->offset = 0.1 ;
        }

/*  Now for operations  */
        else if (type == UF_machining_operation_type)
        {
            if (subtype == UF_mach_cavity_milling_subtype)
            {
                if (geom_type == UF_CAM_part || geom_type == UF_CAM_blank)
                {
                    app_data->has_stock = 1;
                    app_data->has_tolerances = 1 ;
                    app_data->stock = 0.001 ;
                    app_data->tolerances[0] = 0.001 ;
                    app_data->tolerances[1] = 0.001 ;
                }
            }
            else if (subtype == UF_mach_zlevel_milling_subtype)
            {
                if (geom_type == UF_CAM_part)
                {
                    app_data->has_stock = 1;
                    app_data->has_tolerances = 1 ;
                    app_data->stock = 0.001 ;
                    app_data->tolerances[0] = 0.001 ;
                    app_data->tolerances[1] = 0.001 ;
                }
            }
            else if (subtype == UF_mach_surface_contour_subtype ||
                     subtype == UF_mach_vasc_subtype)
            {
                if (geom_type == UF_CAM_part || geom_type == UF_CAM_check)
                {
                    app_data->has_cut_stock = 1;
                    app_data->cut_stock[0] = 0.2 ;
                    app_data->cut_stock[1] = 0.1 ;
                    app_data->cut_stock[2] = 0.5 ;
                }
                if (geom_type == UF_CAM_part)
                {
                    app_data->has_feedrate = 1;
                    app_data->feedrate_unit = UF_CAM_feedrate_unit_per_minute ;
                    app_data->feedrate_value = 10.0 ;
                }
                else if (geom_type == UF_CAM_check)
                {
                    app_data->has_avoidance_type = 1;
                    app_data->avoidance_type =  UF_CAM_avoidance_type_warning;
                }
            }
        }
    }
}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
{
    UF_initialize();

    do_camgeom_api();

    UF_terminate();
}

int ufusr_ask_unload(void)
{
 return (UF_UNLOAD_IMMEDIATELY);
}

