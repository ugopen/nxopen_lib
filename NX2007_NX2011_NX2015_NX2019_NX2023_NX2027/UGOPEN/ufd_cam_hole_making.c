/*=============================================================================
                 Copyright (c)  2002 Unigraphics Solutions, Inc.
                        Unpublished - All Rights Reserved
=============================================================================*/
/******************************************************************************
 *                                                                            *
 * PROGRAM NAME - ufd_cam_hole_making.c                                       *
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the Hole Making modules UG/Open API        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *                                                                            *
 *   The program will open the part cam_holemaking_base_in.prt or             *
 *   cam_holemaking_base_mm.prt from the CAM samples directory and then will  *
 *   set the opt file to be the "hole_making" opt file supplied in the        *
 *   standard installation of UG. It then creats a Feature Geometry group     *
 *   for the feature called "Simple Hole"                          *    
 *                                                                            
 *@@
 *
 ******************************************************************************/


/***************** Include Files *******************************************/
#include <stdio.h>
#include <string.h>

#include <uf.h>
#include <uf_defs.h>
#include <uf_cfi.h>
#include <uf_cam.h>
#include <uf_ncgroup.h>
#include <uf_part.h>
#include <uf_setup.h>
#include <uf_fbm_geom.h>
#include <uf_ui_param.h>

/****************************************************************************/

extern DllExport void ufusr 
(
   char   *param,
   int    *retcode,
   int     param_len
)
{
   int error_code = 0;
   int i = 0, count = 0, part_units;
   char reason[UF_NCGROUP_MAX_REASON_BUFSIZE];
   char *env_trans; 
   char opt_name[ MAX_FSPEC_BUFSIZE ];
   char part_name[ MAX_FSPEC_BUFSIZE ];
   char open_part_name[ MAX_FSPEC_BUFSIZE ] = "";
   char  **feature_names;
   UF_NCFEAT_t *features;
        
   tag_t setupTag = 0, wp_tag = 0;
   tag_t part_tag = 0, geomTag = 0, geomRootTag = 0; 
   logical answer;

   char **criteria_list;
   char                         **criteria_to_consider;
   int                           num_of_classified_sets;
   UF_FBM_GEOM_classified_crit_t classified_sets;
   UF_FBM_GEOM_crit_value_type_t crit_type;
   double                        value;
   UF_PART_load_status_t         load_status;

   *retcode = 0;

   error_code = UF_initialize();
   if( error_code != 0 )
   {
      printf( "Failed to initialize uf %d\n", error_code );
      return;
   }

   criteria_to_consider = (char **)UF_allocate_memory( sizeof( char* ), 
                                                       &error_code );

   criteria_to_consider[0] = (char *)UF_allocate_memory( sizeof( char ) * 132, 
                                                 &error_code );


   /*** This program works with the part files in the CAM samples directory
        so we need to get the path of the directory and the file name
   *****/
   UF_translate_variable( "UGII_CAM_SAMPLES_DIR", &env_trans );
   strcpy( part_name, env_trans );
   strcat( part_name, "cam_holemaking_base_" ); 

   /*** If no part is open then open the part cam_holemaking_base_in.prt
        from the CAM samples directory 
        If not check to see if the units of the open part so that we can open
        the same units part 
   ****/
   if( ( part_tag = UF_PART_ask_display_part() ) == 0 )
   {
       strcat( part_name, "in.prt" ); 
   }
   else
   {
      UF_PART_ask_part_name( part_tag, open_part_name );
      UF_PART_ask_units( part_tag, &part_units );
      if( part_units == UF_PART_ENGLISH )
         strcat( part_name, "in.prt" ); 
      else
         strcat( part_name, "mm.prt" );
   }

   /*** 
        If the file we are trying to open is the currently open file
        then continue on
   ***/
   if( strcmp( open_part_name, part_name ) != 0 )
   {
      UF_PART_open( part_name, &part_tag, &load_status );
   }

   error_code = UF_CAM_init_session();
   if( error_code != 0 )
   {
      printf( "Failed to initialize the CAM session %d\n", error_code );
      return;
   }

   UF_SETUP_ask_setup( &setupTag );
   if( setupTag == 0 )
   {
      return;
   }

   UF_translate_variable( "UGII_CAM_TEMPLATE_SET_DIR", &env_trans );
   strcpy( opt_name, env_trans );
   strcat( opt_name, "hole_making.opt" );
    
   UF_CAM_reinit_opt( opt_name );

   UF_NCGEOM_create( "hole_making", "fbm_geom", &geomTag );
        
   UF_SETUP_ask_geom_root( setupTag, &geomRootTag );
   UF_NCGROUP_ask_object_of_name( geomRootTag, "WORKPIECE",&wp_tag );
   UF_NCGROUP_can_accept_member( wp_tag, geomTag, &answer, reason );
   if( answer == TRUE )
      UF_NCGROUP_accept_member( wp_tag, geomTag );
   else
      return;
        
   UF_FBM_GEOM_ask_list_of_feature_names( geomTag, &count, &feature_names ); 

   if( count > 0 )
      UF_free_string_array( count, feature_names );

   UF_FBM_GEOM_set_feature_name( geomTag, "SIMPLE_HOLE" );

   UF_FBM_GEOM_ask_features( geomTag, &count, &features );

   if( count > 0 )
      UF_free( features );
   else
      return;

   UF_FBM_GEOM_ask_available_criteria(  geomTag, &count, &criteria_list );

   if( count == 0 )
      return;

   strcpy( criteria_to_consider[0], criteria_list[0] );

   UF_FBM_GEOM_classify_by_criteria( geomTag, 1, criteria_to_consider,
                                     &num_of_classified_sets,
                                     &classified_sets );

   UF_FBM_GEOM_ask_type_of_criterion( geomTag, criteria_list[0], &crit_type );

   for( i = 1; i <= num_of_classified_sets; i++ )
   {
      switch( crit_type )
      {
         case UF_FBM_GEOM_crit_value_type_double:
            UF_FBM_GEOM_ask_double_value_of_classified_crit( geomTag, 
                                             criteria_list[0], 
                                             classified_sets, i, &value );
            break;
         default:
            break;
      }
   }
         
   UF_FBM_GEOM_set_classified_features( geomTag, classified_sets, 1 );
     
   return;
}

int ufusr_ask_unload(void)
{
 return (UF_UNLOAD_IMMEDIATELY);
}
