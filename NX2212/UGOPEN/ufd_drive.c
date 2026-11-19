
/*=============================================================================
                 Copyright (c)  2004 UGS Corp.
                     All Rights Reserved
=============================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This file tests the following API's.                                     *
 *                                                                            *
 *   (1) API for the "Drive Geometry" of the Surface Area Drive Method in     *
 *       a Surface Contouring operation.                                      * 
 *       It involves 2 modules:UF_CAMGEOM & UF_SCOP                           *                                              *
 *                                                                            *
 *   (2) API for the "Drive Path" of the Surface Area Drive mMthod in a       *
 *       Surface Contouring operation.                                        * 
 *       It involves 1 module:   UF_DRPOS                                     *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   To execute this internal User Function program:                          *
 *   Open a part, enter Manufacturing Application, highlight one or           *
 *   more Surface Contour operations (or Groups of them), in the ONT.         *
 *   The results are written to the listing window.                           *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

/***************************** Include Files **********************************/
#include <string.h>

#include <uf.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_ui_ont.h>
#include <uf_obj.h>

#include <uf_cam.h>
#include <uf_camgeom.h>
#include <uf_assem.h>
#include <uf_ui.h>
#include <uf_param.h>
#include <uf_so.h>
#include <uf_disp.h>
#include <uf_scop.h>


static int UF_CAMGEOM_drive_geom_api
(
 void
)
{ 
	int case__success = 1;
    tag_t                   *objects;
    int                     i, object_count;
    int                     type, subtype;
    int                     item_count = 0;
    int                     num_col, num_row;
    UF_CAMGEOM_item_t       *items;
    UF_CAM_geom_type_t      geom_type;

    if( UF_PART_ask_display_part() == null_tag )
		return( 0 );

    UF_UI_open_listing_window ();
    UF_UI_write_listing_window ("\n");
    UF_UI_write_listing_window ("Testing Drive Geometry API\n");
        
  	/* Get the highlighted/selected objects from Navigation Tool. */
    UF_UI_ONT_ask_selected_nodes( &object_count, &objects ); 
    uc4404 ("Number of ont objects selected =", object_count);
        
    if (object_count == 0)
    {
        UF_free (objects);
	return( 0 );
    }

/* Cycle through all operations, for each Surface Contouring operation with Surface Area Drive method
   and valid Drive Geometry, We perform the following tasks:
   (1) Obtain and display general information of the Drive Geometry.
   (2) For each item in the Drive Geometry list read/write the Application Data.
   (3) Display the evaluated arrays of points on the Drive Geometry. */
    for( i = 0; i < object_count; i++ )
    {
        int drive_method;

        geom_type = UF_CAM_part;
        UF_OBJ_ask_type_and_subtype( objects[i], &type, &subtype );

        /* For our purposes here we are only interested in surface contouring 
           operations using the surface area drive method.  */
        if( type == UF_machining_operation_type)
        {
            if (subtype == UF_mach_vasc_subtype ||
                subtype == UF_mach_surface_contour_subtype)
            {
                UF_PARAM_ask_int_value (objects[i], UF_PARAM_DRIVE_METHOD,
					&drive_method);
                if (drive_method == UF_PARAM_dpm_type_surface)
                    geom_type = UF_CAM_drive;
             
		/*  Display some general information about Drive Geometry  */
		/***********************************************************
		 * UF_CAMGEOM_ask_items
		 ***********************************************************/
		if (geom_type == UF_CAM_drive)
		{
		    UF_CAMGEOM_ask_items(objects[i], geom_type, &item_count, &items);
		    uc4404 ("selected object =", objects[i]);
		    uc4404 ("number of surfaces in the operation =", item_count);                  
		    /***********************************************************
		     * UF_SCOP_ask_row_column_count
		     ***********************************************************/
		    UF_SCOP_ask_row_column_count (objects[i], &num_row, &num_col);
		    uc4404 ("number of rows =", num_row);
		    uc4404 ("number of columns =", num_col);
	
		    /*  this will display the global parameter direction on the surface grid */
		    /***********************************************************
		     * UF_CAMGEOM_display_uv_dirs
		     ***********************************************************/
		    UF_SCOP_display_uv_dirs (objects[i]);
		}
            }
        }

   
	/* For stress test, we will go over every Surface Area Drive, even when the item count may be 0. */
        if (geom_type == UF_CAM_drive)
        {
            UF_CAMGEOM_app_data_t app_data, app_data2;
            int j, ii, kk, k, comparison;
            UF_MODL_SRF_VALUE_t srf_value;
            double uv[2];
            tag_t xyz[3], point_id;
	    tag_t object_in_part = UF_ASSEM_ask_work_part ();

	    /* cycle through all Drive Geometry, for each item display evaluated points
	       and read/write application data */
            for (j = 0; j < item_count; j++)
            {
                tag_t  entity;
			
		/***********************************************************
		 * UF_CAMGEOM_ask_item_entity
		 ***********************************************************/
		UF_CAMGEOM_ask_item_entity(items[j], &entity);
		uc4404 ("surface identifier =", entity);
		
		/**********************************************************************
		 * UF_CAMGEOM_ask/set_item_app_data
		 ***********************************************************************/
		memset (&app_data, 0, sizeof(UF_CAMGEOM_app_data_t));
		memset (&app_data2, 0, sizeof(UF_CAMGEOM_app_data_t));
		UF_CAMGEOM_ask_item_app_data(items[j], &app_data);
		UF_CAMGEOM_set_item_app_data(objects[i], UF_CAM_drive, items[j], &app_data);
		UF_CAMGEOM_ask_item_app_data(items[j], &app_data2);
		comparison = memcmp (&app_data, &app_data2, sizeof(UF_CAMGEOM_app_data_t));
		
	    } /* end of j 'for' loop */
	    
	    /*  this will just display rows of points on the surfaces, using a different
		color for each row.  */
	    for (ii = 0; ii < 11; ii++)
	    {
		for (kk = 0; kk < 11; kk++)
		{
		    uv[0] = (double) num_col * ii / 10.0;
		    uv[1] = (double) num_row * ((double) kk * 0.1);
		    /***********************************************************
		     * UF_SCOP_eval_grid
		     ***********************************************************/
		    UF_SCOP_eval_grid (objects[i], uv, NULL_TAG, &srf_value);
		    
		    /*  this handles the display of the points after the evaluation.  These are
			all existing functions  */
		    for (k = 0; k < 3; k++)
		    {
			UF_SO_create_scalar_double (object_in_part,
						    UF_SO_update_after_modeling,
						    srf_value.srf_pos[k],
						    &xyz[k]);
		    }
		    UF_SO_create_point_3_scalars (object_in_part,
						  UF_SO_update_after_modeling,
						  xyz,
						  &point_id);
		    UF_SO_display (point_id, UF_DISP_ALL_ACTIVE_VIEWS,
				   UF_DISP_USE_SPECIFIED_COLOR, kk);
		} /*  end of kk 'for' loop */
	    } /*  end of ii 'for' loop */

        } /* end of 'if' valid items */
    } /* end of i 'for' loop */

	UF_free (objects);
	return case__success;
}


static int UF_DRPOS_drive_path_api
(
 void
)
{ 
	int case__success = 1;
    tag_t                   *objects;
    int                     i, object_count;
    int                     type, subtype;
    UF_CAM_geom_type_t      geom_type;


    if( UF_PART_ask_display_part() == null_tag )
		return( 0 );

    UF_UI_open_listing_window ();
    UF_UI_write_listing_window ("\n");
    UF_UI_write_listing_window ("Testing Drive Path API\n");
        
	/* Get the highlighted/selected objects from Navigation Tool. */
    UF_UI_ONT_ask_selected_nodes( &object_count, &objects ); 
    uc4404 ("Number of ont objects selected =", object_count);
        
    if (object_count == 0)
    {
	UF_free (objects);
	return( 0 );
    }

/* Cycle through all operations, for each Surface Contouring operation
   with Surface Area Drive method, We perform the following tasks:
   (1) Obtain and display information of all Drive Points in the Drive Path. */
    for( i = 0; i < object_count; i++ )
    {
        int drive_method;

        geom_type = UF_CAM_part;
        UF_OBJ_ask_type_and_subtype( objects[i], &type, &subtype );

        /* For our purposes here we are only interested in surface contouring 
           operations using the surface area drive method.  */
        if( type == UF_machining_operation_type)
        {
            if (subtype == UF_mach_vasc_subtype ||
                subtype == UF_mach_surface_contour_subtype)
            {
                UF_PARAM_ask_int_value (objects[i], UF_PARAM_DRIVE_METHOD,
                                                &drive_method);
                if (drive_method == UF_PARAM_dpm_type_surface)
                    geom_type = UF_CAM_drive;
            }
        }
                
        if (geom_type == UF_CAM_drive)
        {
            double uv[2];
            tag_t  seid;
            double pos[3], suv[2];
            UF_DRPOS_id_t  drpos;
            int count = 0;

	    /***********************************************************
	     * UF_SCOP_get_next_drive_point
	     ***********************************************************/
	    UF_SCOP_get_next_drive_point (objects[i], &drpos, &count);
            UF_DRPOS_ask_position (drpos, pos);
	    /***********************************************************
	     * UF_DRPOS_ask_grid_params/surface_params/surface_identifier
	     ***********************************************************/
            UF_DRPOS_ask_grid_params (drpos, suv);
            UF_DRPOS_ask_surface_params (drpos, uv);
            UF_DRPOS_ask_surface_identifier (drpos, &seid);
            uc4406 ("tool position ", pos[0]);
            uc4406 ("              ", pos[1]);
            uc4406 ("              ", pos[2]);
            uc4406 ("grid u param = ", suv[0]);
            uc4406 ("grid v param = ", suv[1]);
            uc4406 ("surface u param = ", uv[0]);
            uc4406 ("surface v param = ", uv[1]);
            uc4404 ("surface eid = ", seid);
            uc4403 ("");
	    count++;
	    
	    while (count > 0)
	    {
		/***********************************************************
		 * UF_SCOP_get_next_drive_point
		 ***********************************************************/
		UF_SCOP_get_next_drive_point (objects[i], &drpos,&count);
		if (count > 0)
		{
		    UF_DRPOS_type_t  drpos_type;
		    UF_DRPOS_ask_type (drpos, &drpos_type);
		    if (drpos_type != UF_DRPOS_TYPE_LOCAL_LIFT &&
			drpos_type != UF_DRPOS_TYPE_FINAL_LIFT)
		    {
			UF_DRPOS_ask_position (drpos, pos);
			/***********************************************************
			 * UF_DRPOS_ask_grid_params/surface_params/surface_identifier
			 ***********************************************************/
			UF_DRPOS_ask_grid_params (drpos, suv);
			UF_DRPOS_ask_surface_params (drpos, uv);
			UF_DRPOS_ask_surface_identifier (drpos, &seid);
			uc4406 ("tool position ", pos[0]);
			uc4406 ("              ", pos[1]);
			uc4406 ("              ", pos[2]);
			uc4406 ("grid u param = ", suv[0]);
			uc4406 ("grid v param = ", suv[1]);
			uc4406 ("surface u param = ", uv[0]);
			uc4406 ("surface v param = ", uv[1]);
			uc4404 ("surface eid = ", seid);
			uc4403 ("");
		    }
		}
	    }/* end of while loop */
 
        } /* end of 'if' Drive */
    } /* end of i 'for' loop */

    UF_free (objects);
    return case__success;
}



/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
{
    UF_initialize();

	UF_CAMGEOM_drive_geom_api(); 
	UF_DRPOS_drive_path_api();

    UF_terminate();
}

int ufusr_ask_unload(void)
{
 return (UF_UNLOAD_IMMEDIATELY);
}

