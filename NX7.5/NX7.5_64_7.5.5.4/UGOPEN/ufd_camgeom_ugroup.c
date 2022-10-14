
/*=============================================================================
                 Copyright (c)  2001 Unigraphics Solutions, Inc.
                        Unpublished - All Rights Reserved
=============================================================================*/
/******************************************************************************
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   Allows selection of part, blank, check and cut area geometry.            *
 *                                                                            *
                   *
 *                                                                            *
 ******************************************************************************/

/***************************** Include Files **********************************/
#include <stdlib.h>
#include <stdio.h>

#include <uf.h>
#include <uf_object_types.h>
#include <uf_ui.h>
#include <uf_disp.h>
#include <uf_obj.h>
#include <uf_cam.h>
#include <uf_camgeom.h>

#include <ufd_camgeom_ugroup.h>

#define  MAX_CAMGEOM  20
#define  EXIT_SUCCESS 0

/*#define  DEBUG*/

    static char             *title1 = "Select an API routine...";

    static int              geoption;
    static char             *title3 = "Select Geometry Type(s) for operation then Selection Complete";
    static char             menu3[][38] = { "1) Part Geometry",
                                            "2) Blank Geometry",
                                            "3) Check Geometry",
                                            "4) Cut Area Geometry",
                                            "5) Trim Geometry",
                                            "6) Selection Complete" };

static int init_proc(UF_UI_selection_p_t select, void *user_data);

static void init_camgeom_app_data(UF_CAMGEOM_app_data_p_t app_data);

int ufd_camgeom_ugroup( tag_t objTag, int obj_count )

{
    UF_CAMGEOM_app_data_p_t app_data_list[MAX_CAMGEOM];
    tag_t                   *objects, entity_list[MAX_CAMGEOM];
    int                     i, entity_count, object_count, err_code, type, subtype;

    char                    atitle[] = "Geometry Selection.";
    char                    *cue    = "Identify  Geometry - Wait for the Filter!";
    char                    errorstrg[133];
    int                     response, irc;
    tag_t                   eid, view;
    double                  cursor[3];

#ifdef DEBUG
            printf( "Object tag passed into camgeom_ugroup is %d \n", objTag );
#endif

    geoption = 0;
      
    while ( geoption < 10 )
     {
                    /* Statements go here for each geometry selection type. */

    	     geoption = uc1603(title3, 1, menu3, 6);
    	    
    	    if (geoption == 1 || geoption == 2 || geoption == 10 )
    	    {
             break;
    	    }
#ifdef DEBUG
    	    printf("\n Geometry option returns %d\n", geoption);
#endif
                              /* Allow the user to select faces or bodies. */                           

                           /* Pass in this function the object to be assigned geometry */

            if (obj_count > 0 )
            {
                entity_count = 0;

            while (TRUE)

            {
               
            UF_UI_select_with_single_dialog(cue,atitle,
                                                UF_UI_SEL_SCOPE_NO_CHANGE, init_proc, NULL,
                                                &response, &eid, cursor, &view);

                if (response == UF_UI_OBJECT_SELECTED)
                {
                    entity_list[entity_count] = eid;
#ifdef DEBUG
                    printf(" EID number returns %d\n", eid );
#endif

                               /* Allocate the memory for the application data of an item. */

                    app_data_list[entity_count] = (UF_CAMGEOM_app_data_p_t)UF_allocate_memory(sizeof(UF_CAMGEOM_app_data_t), 
                                                                     &err_code);

                                 /* Initialize the application data. */

                    init_camgeom_app_data(app_data_list[entity_count]);

                    entity_count++;
                }
                else if (response == UF_UI_OK || UF_UI_BACK || UF_UI_CANCEL )
                {                   
                                 /* Geometry selection is finished. */
                    break;
                }
            }
#ifdef DEBUG
            printf(" Entity count this selection is %d\n",entity_count);
#endif

            if (entity_count > 0)
            {
/*                 UF_CAMGEOM_item_t     *items;
                   int                   item_count;*/

                for( i = 0; i < obj_count;  i++ )
                  {
                     irc = UF_OBJ_ask_type_and_subtype( objTag, &type, &subtype );
                    
                      if( type == UF_machining_operation_type ||
                      type == UF_machining_geometry_grp_type)

#ifdef DEBUG
                      printf("\n Current entity count is %d", entity_count);
                      printf("\n Current object count is %d", obj_count);
                      printf("\n Geometry option is %d \n", geoption );
#endif

                            /* Above prints to help in debugging if "DEBUG" defined. */
 
                    {
                        switch (geoption)
                        {
                            case 1:
                            case 2:
                            case 3:
                            case 4:
                            case 5:             /* Part Geometry */
                             {
#ifdef DEBUG
                                 printf("\n Type returned is    %d", type);
                                 printf("\n Subtype returned is %d", subtype);
#endif
                                   {
                                  irc = UF_CAMGEOM_append_items( objTag, UF_CAM_part, entity_count, 
                                                                             entity_list, app_data_list );
                                   }
                                  if ( irc != 0 )
                    		   {
                     		    UF_get_fail_message( irc, errorstrg );
                     		    printf("\n The return code is %d\n", irc);
                     		    printf("\n Error code translates to %s\n", errorstrg);
                     		    return objTag;
                    		   }
                                   break;
                             }

			     case 6:	       /* Blank Geometry */
			     {
#ifdef DEBUG
                                 printf("\n Type returned is    %d", type);
                                 printf("\n Subtype returned is %d", subtype);
#endif
                                   {
                                  irc = UF_CAMGEOM_append_items( objTag, UF_CAM_blank, entity_count, 
                                                                             entity_list, app_data_list );
                                   }
                                  if ( irc != 0 )
                    		   {
                     		    UF_get_fail_message( irc, errorstrg );
                     		    printf("\n The return code is %d\n", irc);
                     		    printf("\n Error code translates to %s\n", errorstrg);
                     		    return objTag;
                    		   }
                                   break;

                             }
                        
			     case 7:	       /*   Check Geometry  */
                             {
#ifdef DEBUG
                                 printf("\n Type returned is    %d", type);
                                 printf("\n Subtype returned is %d", subtype);
#endif
                                   {
                                  irc = UF_CAMGEOM_append_items( objTag, UF_CAM_check, entity_count, 
                                                                             entity_list, app_data_list );
                                   }
                                  if ( irc != 0 )
                    		   {
                     		    UF_get_fail_message( irc, errorstrg );
                     		    printf("\n The return code is %d\n", irc);
                     		    printf("\n Error code translates to %s\n", errorstrg);
                     		    return objTag;
                    		   }
                                   break;

                             }

			     case 8:	       /* Cut Area Geometry */
                             {
#ifdef DEBUG
                                 printf("\n Type returned is    %d", type);
                                 printf("\n Subtype returned is %d", subtype);
#endif
                                  {
                                  irc = UF_CAMGEOM_append_items( objTag, UF_CAM_cut_area, entity_count, 
                                                                             entity_list, app_data_list );
                                  }
                                  if ( irc != 0 )
                    		   {
                     		    UF_get_fail_message( irc, errorstrg );
                     		    printf("\n The return code is %d\n", irc);
                     		    printf("\n Error code translates to %s\n", errorstrg);
                     		    return objTag;
                    		   }
                                   break;
                             }
			     case 9:	       /*   Trim Geometry   */
                             {
                                   printf("This case not implemented.\n");
                                   break;
                             }
			     default:	       /*   Selection Complete   */
                             {
                                 break;
                             }
                    }
            }
            }            
        }
     }
    }  
                                           /* Free the Allocated Memory. */
    for (i=0; i<entity_count; i++)
    {
        UF_free (app_data_list[i]);
    }

/*    UF_free (objects);*/

    return(0);
}                                       
                                       /* Selection initialization procedure */
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

                         /* Enable Faces and Solid Bodies */

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


static void init_camgeom_app_data
(
    UF_CAMGEOM_app_data_p_t app_data
)
{
    if (app_data)
    {
                                                              /* Set flags. */

        app_data->has_stock = 0;                           /* Used 1 - Else 0 */
        app_data->has_cut_stock = 0;                       /* Used 1 - Else 0 */
        app_data->has_tolerances = 0 ;                     /* Used 1 - Else 0 */
        app_data->has_feedrate = 0 ;                       /* Used 1 - Else 0 */
        app_data->has_offset = 0;                          /* Used 1 - Else 0 */
        app_data->has_avoidance_type = 0 ;                 /* Used 1 - Else 0 */

                                                             /* Set values. */
        app_data->stock = 0.033 ;
        app_data->cut_stock[0] = 0.2 ;
        app_data->cut_stock[1] = 0.1 ;
        app_data->cut_stock[2] = 0.5 ;
        app_data->tolerances[0] = 0.003 ;
        app_data->tolerances[1] = 0.003 ;
        app_data->feedrate_unit = UF_CAM_feedrate_unit_per_minute ;
        app_data->feedrate_value = 33.0 ;
        app_data->offset = 0.055 ;
        app_data->avoidance_type =  UF_CAM_avoidance_type_warning;
    }
}


