
/*=============================================================================
						Copyright (c) 2004 UGS Corp.
							All Rights Reserved
=============================================================================*/
/*****************************************************************************
* File Name: ufd_cam_criticaLevels.c
*
* File Description:
*   Show Critical Levels functions use. Writes to the Information Window.   
*
*   Files: ufd_cam_criticaLevels.
*
*   Part file: ufd_cam_criticaLevels.prt located in the CAM sample directory.
*
*   Usage: Requires the part file be active.
*          Four operations are pre-defined to a Default Range.
*          The operation "load_level" is the seed for the user defined cut level
*          function. It must remain in the Workpiece geometry group for inheritance.        
*          Select ALL of the nodes in the Workpiece.
*          Execute the program for the following results.
*          Queries and Sets the Critical Levels parameters for Cavity Milling's 
*          NX3 requirement. It sets a Single Range with Top Off Critical Depths.
*          A User Defined Range using Load Data. A User Defined Range by selecting
*          faces and a System Range cutting at Range Bottoms only.
*          Optionally the part file could be saved, but it is not.
*
*	Hints: Be patient when selecting faces. Wait for the filter if necessary. 
*          Each of the five horizontal faces are named to assist in selection.
*          These names will show in the filter.
*          The Cue also shows the selection requirement - Bottom to Top.
*
*          Resize the Info Window so that it does not overlay the graphics window.
*          Information is written to this window during program execution.
*


******************************************************************************/

/*===========================================================================*/
/*================================ INCLUDES =================================*/
/*===========================================================================*/	

/******************************************* Include Files *******************************************/

#include <stdio.h>

#include <uf_obj.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_ui_ont.h>
#include <uf_object_types.h>
#include <uf.h>
#include <uf_param.h>
#include <uf_ugopenint.h>
#include <uf_disp.h>
#include <uf_retiring.h>
#include <uf_param_indices.h>
#include <uf_cut_levels.h>

#include <uf_camgeom.h>

/*********************************************** MAIN ************************************************/

#define MAX_CAMGEOM 20

static int init_proc_face(UF_UI_selection_p_t select, void *user_data);

static void do_cam_clevel_api(void)

{
	int irc, ii, isSet, jj=0, kk=1;
	int object_count, response;
	int entity_count = 0;

	double isReal;
	double udlevels[5] = {0.0,0.0,0.0,0.0,0.0};
	double uzlevels[5] = {0.0,0.0,0.0,0.0,0.0};
	double cursor[3];

	char message[133];
	char title[] = "User Interaction required...";
    char cue[] = "Select the Five Horizontal Faces - Bottom to Top.";

	logical getResult;

	tag_t operTag=null_tag;
	tag_t *objects;
	tag_t entity_list[MAX_CAMGEOM];
	tag_t eid, view;

	UF_CUT_LEVELS_t *level_data;

	irc = UF_initialize();
	if( irc != 0 )
	{
		printf( "Failed to initialize uf %d\n", irc );
		return;
	}

	if( UF_PART_ask_display_part() != null_tag )
 {
        /* Get the highlighted/selected object from the ONT. */

        irc = UF_UI_ONT_ask_selected_nodes( &object_count, &objects ); 
		      UF_UI_open_listing_window( );

       /* Check for Tool Holder usage. */

			irc = UF_PARAM_ask_logical_value(objects[0],UF_PARAM_CUT_TL_HOLDER_USAGE, &getResult );
			if ( getResult == FALSE )
			{
			irc = UF_PARAM_set_logical_value(objects[0],UF_PARAM_CUT_TL_HOLDER_USAGE, TRUE );
			irc = UF_PARAM_ask_logical_value(objects[0],UF_PARAM_CUT_TL_HOLDER_USAGE, &getResult );
					UF_UI_write_listing_window("Tool Holder usage has been toggled ON.\n");
			}
				else
				{
				UF_UI_write_listing_window("Tool Holder usage was toggled ON.\n");
				}
	
		while ( jj <= object_count )
		{
		   switch(kk)
		   {
			case 1:	    /* Set the Single Range. */						

			 irc = UF_CUT_LEVELS_set_range_type( objects[jj], UF_PARAM_clv_range_single, NULL );
		     irc = UF_PARAM_ask_int_value(objects[jj],UF_PARAM_CUTLEV_RANGE_TYPE, &isSet );
		 					
			/* Set the cut range division to equal steps. */

			irc = UF_PARAM_set_int_value(objects[jj],UF_PARAM_CUTLEV_RANGE_SUBDIV_TYPE, 0);
			irc = UF_PARAM_ask_int_value(objects[jj],UF_PARAM_CUTLEV_RANGE_SUBDIV_TYPE, &isSet );
			if ( isSet == 0 )
				{
				UF_UI_write_listing_window("Cut Range sub-divided in equal steps.\n");
				}
				else if ( isSet == 1 )
				{
				UF_UI_write_listing_window("Cut at the Range Bottoms only.\n");
				}

			        /* Set the Global Depth Per Cut. */

			irc = UF_PARAM_set_double_value(objects[jj],UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH, 0.25 );
		    irc = UF_PARAM_ask_double_value(objects[jj],UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH, &isReal );
		     if ( isReal != 0 )
		     {
			   uc4406( "Global Cut Depth for Single Range is set to", isReal );
		     }
		 	       /* Set the Horizontal Top Off. */

			irc = UF_PARAM_ask_int_value(objects[jj],UF_PARAM_CUTLEV_RANGE_TYPE, &isSet );
			 uc4404( "Cut Level range is set to", isSet );
			 if ( isSet == 2 )
				{
				irc = UF_PARAM_set_int_value(objects[jj],UF_PARAM_CUTLEV_TOP_OFF_MODE, 1);
				irc = UF_PARAM_ask_int_value(objects[jj],UF_PARAM_CUTLEV_TOP_OFF_MODE, &isSet );
				}
				if ( isSet == 1 )
				{
				UF_UI_write_listing_window("We top off horizontal surfaces.\n");
				}
				break;

			case 2:
				/* Set a User Defined Cut Range using explicit z-levels. */

			 irc = UF_CUT_LEVELS_set_range_type( objects[jj], UF_PARAM_clv_range_user_defined, NULL );
		     irc = UF_PARAM_ask_int_value(objects[jj],UF_PARAM_CUTLEV_RANGE_TYPE, &isSet );
			 uc4404( "Cut Level range is set to", isSet );
			  if ( isSet == 1 )
			   {
				UF_UI_write_listing_window("Cut Level range is a Single Range.\n");
		       }
			   level_data=NULL;

				irc = UF_OBJ_cycle_by_name( "LOAD_RANGE", &operTag );
				irc = UF_CUT_LEVELS_load( operTag, &level_data );

				/* Loop and add levels using "z" then set local DPC. */

			 for ( ii = 0; ii <=4; ii += 1)
			 {
				uzlevels[ii] = level_data->cut_levels[ii].z_level;
				udlevels[ii] = level_data->cut_levels[ii].local_cut_depth;
			 }
				irc = UF_CUT_LEVELS_add_levels_using_z( objects[jj], 5, uzlevels, 0, NULL );

				if ( irc != 0 )
				 {
					UF_get_fail_message ( irc, message );
					uc4403( message );
				 }
				 for ( ii = 0; ii <=4; ii += 1)
				  {
				   UF_CUT_LEVELS_edit_level_using_z( objects[jj], ii, uzlevels[ii], udlevels[ii], NULL );
				  }

			 irc = UF_PARAM_ask_double_value(objects[jj],UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH, &isReal );
		     if ( isReal != 0 )
		     {
			   uc4406( "Global Cut Depth for User Defined Range is set to", isReal );
		     }
		     irc = UF_PARAM_ask_int_value(objects[jj],UF_PARAM_CUTLEV_RANGE_TYPE, &isSet );
			 							
			 /* Delete the non-machinable cut range. */

			 irc = UF_CUT_LEVELS_delete_level( objects[jj], 5, NULL );
	 
				irc = UF_CUT_LEVELS_free ( &level_data );
				break;

			case 3:
			/* Select the faces for the cut levels. */

			while (TRUE)
            {
                UF_UI_select_with_single_dialog(cue,title,
                                                UF_UI_SEL_SCOPE_NO_CHANGE, init_proc_face, NULL,
                                                &response, &eid, cursor, &view);

                if (response == UF_UI_OBJECT_SELECTED || response == UF_UI_OBJECT_SELECTED_BY_NAME)
                {
                    entity_list[entity_count] = eid;

		    /* Allocate the memory for the geometry item. */

				 UF_allocate_memory(sizeof(entity_list[entity_count]), &irc);
           
					UF_UI_write_listing_window("****************************************\n");
					UF_UI_write_listing_window("Individual Face Tags follow.\n");
					UF_UI_write_listing_window("****************************************\n");
					uc4404( "Seleted face tag is", entity_list[entity_count] );
					UF_UI_write_listing_window("****************************************\n");
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
			
		    /* Set a User Defined Cut Range using face tags. */

			 irc = UF_PARAM_set_double_value(objects[jj],UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH, 0.125 );
			 irc = UF_CUT_LEVELS_set_range_type( objects[jj], UF_PARAM_clv_range_user_defined, NULL );
		     irc = UF_PARAM_ask_int_value(objects[jj],UF_PARAM_CUTLEV_RANGE_TYPE, &isSet );

			  if ( isSet == 1 )
			   {
				UF_UI_write_listing_window("Cut Level Range is a User Defined Range.\n");
		       }
			        /* Add levels using "geom" then set local DPC.*/


				irc = UF_CUT_LEVELS_add_levels_using_geom( objects[jj], entity_count, entity_list, 0.125, NULL );

				if ( irc != 0 )
				 {
					UF_get_fail_message ( irc, message );
					uc4403( message );
					break;
				 }
				 /* Set Range 4 DPC to 0.050. */

				irc = UF_CUT_LEVELS_edit_level_using_geom( objects[jj], 5, entity_list[1], 0.050, NULL );

				if ( irc != 0 )
				 {
					UF_get_fail_message ( irc, message );
					uc4403( message );
					break;
				 }				
				 /* Delete the non-machinable cut range. */


			 irc = UF_CUT_LEVELS_delete_level( objects[jj], 6, NULL );
			
			 irc = UF_PARAM_ask_double_value(objects[jj],UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH, &isReal );
			 
		     if ( isReal != 0 )
		     {
			   uc4406( "Global Cut Depth for User Defined Range is set to", isReal );
		     }
		     irc = UF_PARAM_ask_int_value(objects[jj],UF_PARAM_CUTLEV_RANGE_TYPE, &isSet );
	 
				irc = UF_CUT_LEVELS_free ( &level_data );
				break;

			case 4:
			  /* Set the System Defined Range. */

				irc = UF_CUT_LEVELS_load( objects[jj], NULL );
				irc = UF_CUT_LEVELS_set_range_type( objects[jj], UF_PARAM_clv_range_auto_generate, NULL );
				irc = UF_CUT_LEVELS_free ( NULL );
				irc = UF_PARAM_set_int_value(objects[jj],UF_PARAM_CUTLEV_RANGE_SUBDIV_TYPE, UF_PARAM_clv_range_subdiv_bottoms_only);
				irc = UF_PARAM_set_double_value(objects[jj],UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH, 0.125 );

				/* Delete the non-machinable cut range. */

				irc = UF_CUT_LEVELS_delete_level( objects[jj], 7, NULL );

				irc = UF_PARAM_ask_double_value(objects[jj],UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH, &isReal );
				if ( isReal != 0 )
				{
				uc4406( "Global Cut Depth for System Defined ranges is set to", isReal );
				}
				irc = UF_PARAM_ask_int_value(objects[jj],UF_PARAM_CUTLEV_RANGE_TYPE, &isSet );

				break;

			case 5:
				UF_UI_write_listing_window("Case 5 is the Load Level Data for case 2.\n");
				break;

			default:
				break;
		   }
		   ++kk;
		   ++jj;
		}

 }
	UF_DISP_refresh ();

	printf(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n");

	/* To save part file, uncomment the following. */ 

        /* UF_PART_save(); */

	if( objects[jj] != 0 )
	{
		UF_free( objects);
	}

	return;
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
  
		/* Enable Faces Only*/

	if((UF_UI_set_sel_mask(select,
							UF_UI_SEL_MASK_ENABLE_SPECIFIC,
                           nums, masks)) == 0)
    {
        return (UF_UI_SEL_SUCCESS);
    }
    else
    {
        return (UF_UI_SEL_FAILURE);
    }
}
/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
{
    UF_initialize();

    do_cam_clevel_api();

    UF_terminate();
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
