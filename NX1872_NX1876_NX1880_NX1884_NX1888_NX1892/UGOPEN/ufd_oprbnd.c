
/*=============================================================================
                 Copyright (c)  2001 Unigraphics Solutions, Inc.
                        Unpublished - All Rights Reserved
=============================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *   UF_OPRBND_ask_boundary_app_data                                          *
 *   UF_OPRBND_ask_item_app_data                                              *
 *   UF_OPRBND_set_boundary_app_data                                          *
 *   UF_OPRBND_set_item_app_data                                              *
 *   UF_OPRBND_ask_item_udes                                                  *
 *   UF_OPRBND_delete_all_item_udes                                           *
 *   UF_OPRBND_append_item_ude                                                *
 *   UF_OPRBND_delete_item_ude                                                *
 *   UF_OPRBND_can_accept_item_ude                                            *
 *                                                                            *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example requires a part, a manufacturing setup, and one geometry    *
 *   group inherited to a highlighted operation.                              *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

/***************************** Include Files **********************************/
#include <stdlib.h>

#include <uf.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_ui_ont.h>
#include <uf_cam.h>
#include <uf_ude.h>
#include <uf_oprbnd.h>
#include <uf_cambnd.h>

/*******************************************************************/

static UF_OPRBND_app_data_p_t create_and_init_bnd_app_data(void);

/*******************************************************************/
static void do_cambnd_api(void)
{
    tag_t                        part_tag, *objects;
    int                          i, j, object_count, blank_count, blank_item_count;
    UF_OPRBND_boundary_t         *blank_bnd_list;
    UF_OPRBND_item_t             *blank_item_list;
    logical                      rep;
    int                          ude_num;
    static char udevents[] [20] = { "spindle",
                                    "spindle_off"};                      
    UF_OPRBND_UDE_t              ude_obj, *udes;

    /* Get the displayed part. */
    part_tag = UF_PART_ask_display_part( );
    
    if( part_tag != null_tag )
    {
        /* Get the highlighted/selected objects from Navigation Tool. */
        UF_UI_ONT_ask_selected_nodes( &object_count, &objects ); 

        /***********************************************************************/
        /*
         * UF_CAMBND_ask_boundaries
         */
        /***********************************************************************/
        UF_CAMBND_ask_boundaries(objects[0], UF_CAM_blank, &blank_count, 
                                 &blank_bnd_list);

        for (i=0; i<blank_count; i++)
        {
            UF_CAMBND_is_inherited(objects[0], UF_CAM_blank, &rep);

            if (rep) /* inherited geometry */
            {
                UF_OPRBND_app_data_p_t      ask_app_data = create_and_init_bnd_app_data();
                UF_OPRBND_app_data_p_t      set_app_data = create_and_init_bnd_app_data();

                /***********************************************************************/
                /*
                 * UF_OPRBND_ask_boundary_app_data
                 */
                /***********************************************************************/
                UF_OPRBND_ask_boundary_app_data(objects[0], UF_CAM_blank, blank_bnd_list[i], 
                                                ask_app_data);

                /***********************************************************************/
                /*
                 * UF_OPRBND_set_boundary_app_data
                 */
                /***********************************************************************/
                UF_OPRBND_set_boundary_app_data(objects[0], UF_CAM_blank, blank_bnd_list[i], 
                                                set_app_data);

                /***********************************************************************/
                /*
                 * UF_CAMBND_ask_boundary_items
                 */
                /***********************************************************************/
                UF_CAMBND_ask_boundary_items(blank_bnd_list[i], &blank_item_count, 
                                             &blank_item_list);

                for (j=0; j<blank_item_count; j++)
                {
                    UF_OPRBND_app_data_p_t  ask_item_app_data = create_and_init_bnd_app_data();
                    UF_OPRBND_app_data_p_t  set_item_app_data = create_and_init_bnd_app_data();

                    /***********************************************************************/
                    /*
                     * UF_OPRBND_ask_item_app_data
                     */
                    /***********************************************************************/
                    UF_OPRBND_ask_item_app_data(objects[0], UF_CAM_blank, blank_bnd_list[i],
                                                blank_item_list[j], ask_item_app_data);

                    /***********************************************************************/
                    /*
                     * UF_OPRBND_set_item_app_data
                     */
                    /***********************************************************************/
                    UF_OPRBND_set_item_app_data(objects[0], UF_CAM_blank, blank_bnd_list[i],
                                                blank_item_list[j], set_item_app_data);

                    /***********************************************************************/
                    /*
                     * UF_OPRBND_can_accept_ude
                     */
                    /***********************************************************************/
                    UF_OPRBND_can_accept_item_ude(objects[0], UF_CAM_blank, blank_bnd_list[i],
                                                  blank_item_list[j], UF_OPRBND_UDE_START_SET, 
                                                  udevents[0], &rep);

                    if (rep)
                    {
                        /***********************************************************************/
                        /*
                         * UF_OPRBND_append_item_ude
                         */
                        /***********************************************************************/
                        UF_OPRBND_append_item_ude(objects[0], UF_CAM_blank, blank_bnd_list[i],
                                                  blank_item_list[j],UF_OPRBND_UDE_START_SET, 
                                                  udevents[0], &ude_obj, &rep);

                        if (rep)
                            UF_UDE_set_double(ude_obj, "spindle_speed", 333.0);
                    }

                    UF_OPRBND_can_accept_item_ude(objects[0], UF_CAM_blank, blank_bnd_list[i],
                                                  blank_item_list[j], UF_OPRBND_UDE_END_SET, 
                                                  udevents[0], &rep);
                    if (rep)
                    {
                        UF_OPRBND_append_item_ude(objects[0], UF_CAM_blank, blank_bnd_list[i],
                                                  blank_item_list[j],UF_OPRBND_UDE_END_SET, 
                                                  udevents[1], &ude_obj, &rep);
                    }

                    /***********************************************************************/
                    /*
                     * UF_OPRBND_ask_item_udes
                     */
                    /***********************************************************************/
                    UF_OPRBND_ask_item_udes(objects[0], UF_CAM_blank, blank_bnd_list[i],
                                            blank_item_list[j], UF_OPRBND_UDE_START_SET, 
                                            &ude_num, &udes);

                    /***********************************************************************/
                    /*
                     * UF_OPRBND_delete_item_ude
                     */
                    /***********************************************************************/
                    UF_OPRBND_delete_item_ude(objects[0], UF_CAM_blank, blank_bnd_list[i],
                                              blank_item_list[j], UF_OPRBND_UDE_END_SET, ude_obj);

                    /***********************************************************************/
                    /*
                     * UF_OPRBND_delete_all_item_udes
                     */
                    /***********************************************************************/
                    UF_OPRBND_delete_all_item_udes(objects[0], UF_CAM_blank, blank_bnd_list[i],
                                              blank_item_list[j], UF_OPRBND_UDE_START_SET);
                }
            }
        }
    }

    return;
}

static UF_OPRBND_app_data_p_t create_and_init_bnd_app_data(void)
{
    UF_OPRBND_app_data_p_t  app_data; 
    int                     err_code;

    app_data = (UF_OPRBND_app_data_p_t) UF_allocate_memory(
                                          sizeof(UF_OPRBND_app_data_t), &err_code);

    if (err_code)
        return(NULL);

    /* Set flags. */
    app_data->has_stock = 1;
    app_data->has_feedrate = 1 ;
    app_data->has_tool_position = 1;
    
    /* Set values. */
    app_data->stock = 0.1 ;
    app_data->feedrate_unit = UF_CAM_feedrate_unit_per_minute ;
    app_data->feedrate_value = 10.0 ;
    app_data->tool_position = UF_CAM_tool_position_tanto;

    return(app_data);
}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
{
    UF_initialize();

    do_cambnd_api();

    UF_terminate();
}

