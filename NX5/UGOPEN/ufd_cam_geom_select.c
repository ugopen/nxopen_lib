
/*=============================================================================
                 Copyright (c)  2004 UGS Corp.
                     All Rights Reserved
=============================================================================*/
/******************************************************************************
 *                                                                            *
 * FILE NAME -                                                                *
 *   ufd_cam_geom_select.c                                                    *
 *                                                                            *
 * PART FILES -                                                               *
 *   ufd_face_mill_case1.prt ufd_vap_case1.prt in CAM samples directory.      *
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   Program will allow selection of Part, Cut Area (Floor) and Wall Geometry *
 *   to a single Face Mill or Variable Axis Surface Contour operation using   *
 *   the Contour Profile Drive Method.                                        *
 *   If "Automatic Wall" is toggled on in operation, the Wall Geometry will   *
 *   be selected without user input. This is "ON" in the samples.             *
 *   Geometry may be selected by cursor selection or by "Name".               *  
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The program requires an open part, a manufacturing setup, and one        *
 *   highlighted Face Mill or Contour Profile operation.                      *
 *                                                                            *
 
 *                                                                            *
 ******************************************************************************/

/***************************** Include Files **********************************/


#include <uf.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_ui_ont.h>
#include <uf_disp.h>
#include <uf_retiring.h>
#include <uf_obj.h>

#include <uf_cam.h>
#include <uf_camgeom.h>
#include <uf_param.h>

#include <string.h>

#define  MAX_CAMGEOM   20

static int init_proc_body(UF_UI_selection_p_t select, void *user_data);
static int init_proc_face(UF_UI_selection_p_t select, void *user_data);
static void init_camgeom_app_data(UF_CAMGEOM_app_data_p_t app_data);

static void do_camgeom_api(void)
{
    UF_CAMGEOM_app_data_p_t app_data_list[MAX_CAMGEOM] = {NULL}; 
	tag_t                   *objects = NULL, entity_list[MAX_CAMGEOM] = {NULL_TAG};
    int                     i, entity_count=0, object_count=0, err_code=0, type=0, subtype=0;
    int                     response=0;
    tag_t                   eid = NULL_TAG, view = NULL_TAG;
	double                  cursor[3] = {0.0,0.0,0.0};
    logical                 auto_wall_selection = FALSE;

    for (i=0; i<MAX_CAMGEOM; i++)
        app_data_list[i] = NULL;

    if( UF_PART_ask_display_part() != null_tag )
    {
			/* Get the highlighted/selected objects from Navigation Tool. */

        UF_UI_ONT_ask_selected_nodes( &object_count, &objects );

			/* Part Selection */

        if (object_count > 0)
        {
            char                    title[] = "Part Selection";
            char                    cue[] = "Select a body";
            entity_count = 0;

            /* Allow the user to select the faces and bodies. */

            while (TRUE)
            {
                UF_UI_select_with_single_dialog(cue,title,
                                                UF_UI_SEL_SCOPE_NO_CHANGE, init_proc_body, NULL,
                                                &response, &eid, cursor, &view);
			    
                if (response == UF_UI_OBJECT_SELECTED || response == UF_UI_OBJECT_SELECTED_BY_NAME)
				{	
                    entity_list[entity_count] = eid;

			/* Allocate the memory for the application data of an item.*/

                    app_data_list[entity_count] = (UF_CAMGEOM_app_data_p_t)
						UF_allocate_memory(sizeof(UF_CAMGEOM_app_data_t), &err_code);
					
					if (response == UF_UI_OBJECT_SELECTED)

			/* Initialize the application data. */
					{
                    init_camgeom_app_data(app_data_list[entity_count]);
					}
					
                    entity_count++;				    
				}
				
                else if (response == UF_UI_OK || response == UF_UI_CANCEL ||
                         response == UF_UI_BACK)
                {
                    
			/* Geometry selection is finished. */

                    break;
				}				
				
			/*				Unhighlight selected object.				*/

					UF_DISP_set_highlight(eid,0);
                		      
			}

            if (entity_count > 0)
            {
                for( i = 0; i < object_count; i++ )
                {
                    UF_OBJ_ask_type_and_subtype( objects[i], &type, &subtype );
                    if( type == UF_machining_operation_type )
                    {
                        /***********************************************************************/
                        /*
                         * UF_CAMGEOM_append_items
                         */
                        /***********************************************************************/

                        UF_CAMGEOM_append_items(objects[i], UF_CAM_part, entity_count,
                                                entity_list, app_data_list);

                    }
                }
            }
        }
        
			/* Cut Area Selection */

        if (object_count > 0)
        {
            char                    title[] = "Floor Selection";
            char                    cue[] = "Select a face";
            entity_count = 0;

            /* Allow the user to select the faces and bodies. */

            while (TRUE)
            {
                UF_UI_select_with_single_dialog(cue,title,
                                                UF_UI_SEL_SCOPE_NO_CHANGE, init_proc_face, NULL,
                                                &response, &eid, cursor, &view);

                if (response == UF_UI_OBJECT_SELECTED || response == UF_UI_OBJECT_SELECTED_BY_NAME)
                {
                    entity_list[entity_count] = eid;

			/* Allocate the memory for the application data of an item.*/
                    app_data_list[entity_count] = (UF_CAMGEOM_app_data_p_t)
						UF_allocate_memory(sizeof(UF_CAMGEOM_app_data_t), &err_code);

			/* Initialize the application data. */

                    init_camgeom_app_data(app_data_list[entity_count]);

                    entity_count++;
                }
                else if (response == UF_UI_OK || response == UF_UI_CANCEL ||
                         response == UF_UI_BACK)
                {
                    
			/* Geometry selection is finished. */

                    break;
                }

			/*				Unhighlight selected object.				*/

					UF_DISP_set_highlight(eid,0);
            }

            if (entity_count > 0)
            {
                for( i = 0; i < object_count; i++ )
                {
                    UF_OBJ_ask_type_and_subtype( objects[i], &type, &subtype );
                    if( type == UF_machining_operation_type )
                    {
                        /***********************************************************************/
                        /*
                         * UF_CAMGEOM_append_items
                         */
                        /***********************************************************************/

                        UF_CAMGEOM_append_items(objects[i], UF_CAM_cut_area, entity_count,
                                                entity_list, app_data_list);

                    }
                }
            }
        }
        
			/* Wall Selection */

        UF_PARAM_ask_logical_value(objects[0], UF_PARAM_AUTO_WALL_SELECTION, &auto_wall_selection);
        if (object_count > 0 && auto_wall_selection == FALSE)
        {
            char                    title[] = "Wall Selection";
            char                    cue[] = "Select faces";
            entity_count = 0;

            /* Allow the user to select the faces and bodies. */

            while (TRUE)
            {
                UF_UI_select_with_single_dialog(cue,title,
                                                UF_UI_SEL_SCOPE_NO_CHANGE, init_proc_face, NULL,
                                                &response, &eid, cursor, &view);

                if (response == UF_UI_OBJECT_SELECTED || response == UF_UI_OBJECT_SELECTED_BY_NAME)
                {
                    entity_list[entity_count] = eid;

			/* Allocate the memory for the application data of an item.*/

                    app_data_list[entity_count] = (UF_CAMGEOM_app_data_p_t)
						UF_allocate_memory(sizeof(UF_CAMGEOM_app_data_t), &err_code);

			/* Initialize the application data. */

                    init_camgeom_app_data(app_data_list[entity_count]);

                    entity_count++;
                }
                else if (response == UF_UI_OK || response == UF_UI_CANCEL ||
                         response == UF_UI_BACK)
                {
                    
			/* Geometry selection is finished. */

                    break;
                }

				/*				Unhighlight selected object.				*/

					UF_DISP_set_highlight(eid,0);
            }

            if (entity_count > 0)
            {
                for( i = 0; i < object_count; i++ )
                {
                    UF_OBJ_ask_type_and_subtype( objects[i], &type, &subtype );
                    if( type == UF_machining_operation_type )
                    {
                        /***********************************************************************/
                        /*
                         * UF_CAMGEOM_append_items
                         */
                        /***********************************************************************/

                        UF_CAMGEOM_append_items(objects[i], UF_CAM_wall, entity_count,
                                                entity_list, app_data_list);

                    }
                }
            }
        }

    }

			/* Free the allocated memory. */

    for (i=0; i<entity_count; i++)
    {
        UF_free (app_data_list[i]);
    }

    UF_free (objects);

    return;
}

			/* Selection initialization procedure */

static int init_proc_body
(
    UF_UI_selection_p_t select,
    void* user_data
)
{
    int nums = 1;
    UF_UI_mask_t masks[] = {
         UF_solid_type, 0, UF_UI_SEL_FEATURE_BODY};

			/* Enable  Solid */

    if((UF_UI_set_sel_mask(select,                        
						   UF_UI_SEL_MASK_CLEAR_AND_ENABLE_SPECIFIC,
                           nums, masks)) == 0)

    {
        return (UF_UI_SEL_SUCCESS);
    }
    else
    {
        return (UF_UI_SEL_FAILURE);
    }
}

static int init_proc_face
(
    UF_UI_selection_p_t select,
    void* user_data
)
{
    int nums = 1;
    UF_UI_mask_t masks[] = {
         UF_solid_type, 0, UF_UI_SEL_FEATURE_ANY_FACE};

			/* Enable Faces */

    if((UF_UI_set_sel_mask(select,
                           UF_UI_SEL_MASK_CLEAR_AND_ENABLE_SPECIFIC,
                           nums, masks)) == 0)
    {
        return (UF_UI_SEL_SUCCESS);
    }
    else
    {
        return (UF_UI_SEL_FAILURE);
    }
}

static void init_camgeom_app_data
(
    UF_CAMGEOM_app_data_p_t app_data
)
{
    if (app_data)
    {
			/* Set flags. */

        app_data->has_stock = 0;
        app_data->has_cut_stock = 0;
        app_data->has_tolerances = 0 ;
        app_data->has_feedrate = 0 ;
        app_data->has_offset = 0;
        app_data->has_avoidance_type = 0 ;

			/* Set values. */

        app_data->stock = 0.0 ;
        app_data->cut_stock[0] = 0.0 ;
        app_data->cut_stock[1] = 0.0 ;
        app_data->cut_stock[2] = 0.0 ;
        app_data->tolerances[0] = 0.0 ;
        app_data->tolerances[1] = 0.0 ;
        app_data->feedrate_unit = UF_CAM_feedrate_unit_per_minute ;
        app_data->feedrate_value = 10.0 ;
        app_data->offset = 0.0 ;
        app_data->avoidance_type =  UF_CAM_avoidance_type_warning;
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
/************************************************************/
