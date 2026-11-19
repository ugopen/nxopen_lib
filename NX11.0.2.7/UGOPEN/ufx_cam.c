/*****************************************************************************
                 Copyright (c)  1999 Unigraphics Solutions, Inc.
                        Unpublished - All Rights Reserved

  
   File Description:
      This file contains an example of using the new (v16.0) CAM User Function
      layer. This program will go through a part generating all of the
      tool paths.
  
      The program will output all messages to a file called ufx_cam.log.
      The program expects the command line arguments to be the part files
      to be processed, e.g.
          ufx_cam part_file1.prt part_file2.prt ...
  
      to link this program:
         uflink ufx_cam
  
  
 *****************************************************************************/

/***************************** Include Files **********************************/
#include <stdarg.h>
#include <stdio.h>
#include <time.h>
#include <string.h>

#include <uf.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_cfi.h>

#include <uf_cam.h>
#include <uf_ncgroup.h>
#include <uf_oper.h>
#include <uf_param.h>
#include <uf_setup.h>
#include <uf_cutter.h>
#include <uf_cfi.h>

/**************************** Private Defines *********************************/
#define ONLY_SPEC_PART   0
#define UNLOAD_ALWAYS    1

/**************************** Static Functions ********************************/

/* Function to issue an error to the logfile if it occurs. */
/*----------------------------------------------------------------------------*/
static void issueError
/*----------------------------------------------------------------------------*/
(
   FILE   *log_file,
   int     ecode,
   char   *format,
   ...
)
{
   va_list   ap;
   char      buffer[133];

   va_start( ap, format );

   if( ecode != 0 )
   {
      UF_get_fail_message( ecode, buffer );
      fprintf( log_file, "Error %d: %s\n", ecode, buffer );
   }
   vfprintf( log_file, format, ap );

   va_end( ap );
}


/* Function to show how to create a new cutter and operation in an existing 
   part.
*/
/*----------------------------------------------------------------------------*/
static void   testCreators
/*----------------------------------------------------------------------------*/
(
   FILE   *log_file,
   char   *part_file
)
{
   int        error, type_count, count;
   logical    worked;
   tag_t      part_tag;
   UF_PART_load_status_t   err_status;
   const char   **subtypes;
   tag_t          new_object;
   const char   **type_names;
           
   worked = TRUE;
   fprintf( log_file, "\nBegin testing creators\n" );

   error = UF_PART_open( part_file, &part_tag, &err_status );
   if( error != 0 )
   {
      issueError( log_file, error, "Error opening file %s\n", part_file );
      fprintf( log_file, "End testing creators\n" );
      return;
   }

   /* Get the list of Object Parameter Templates active in this CAM session */
   error = UF_CAM_opt_ask_types( &type_count, &type_names );

   if( error != 0 )
   {
      issueError( log_file, error, "Error asking opt type names for file %s\n",
                                    part_file );
      fprintf( log_file, "End testing creators\n" );
      return;
   }
   if( type_count < 1 )
   {
      issueError( log_file, 0, "Part file %s has OPT with no types\n",
                               part_file );
      fprintf( log_file, "End testing creators\n" );
      return;
   }
   
   /* Get the list of subtypes for the first OPT type */
   error = UF_CAM_opt_ask_subtypes( type_names[0], UF_CAM_OPT_STYPE_CLS_TOOL,
                                    &count, &subtypes );
   if( error != 0 )
   {
      issueError( log_file, error, "Can not ask subtypes of type "
                   "UF_CAM_OPT_STYPE_CLS_TOOL while testing creators\n"  );
      worked = FALSE;
   }

   if( count < 1 )
   {
      fprintf( log_file, "Part %s has no CUTTER groups to be used as a"
                      " template object. No CUTTER creation done.",
                      part_file );
   }

   /* Create an new cutter object in the current part of the specified type and
    * subtype.
    */
   error = UF_CUTTER_create( (char *)type_names[0], 
                                       (char *)subtypes[0], &new_object );
   if( error != 0 )
   {
      issueError( log_file, error, "Can not create new CUTTER Group\n");
      worked = FALSE;
   }
   UF_free_string_array( count, (char **)subtypes );

   /* Get the list of subtypes for the first OPT type */
   error = UF_CAM_opt_ask_subtypes( type_names[0], UF_CAM_OPT_STYPE_CLS_OPER,
                                    &count, &subtypes );
   if( error != 0 )
   {
      issueError( log_file, error, "Can not ask subtypes of type "
                   "UF_CAM_OPT_STYPE_CLS_OPER while testing creators\n"  );
      worked = FALSE;
   }

   if( count < 1 )
   {
      fprintf( log_file, "Part %s has no OPERATION groups to be used as a"
                      " template object. No OPERATION creation done.",
                      part_file );
   }

   /* Create an new cutter object in the current part of the specified type and
    * subtype.
    */
   error = UF_OPER_create( (char *)type_names[0], 
                                       (char *)subtypes[0], &new_object );
   if( error != 0 )
   {
      issueError( log_file, error, "Can not create new OPERATION Group\n");
      worked = FALSE;
   }
   UF_free_string_array( count, (char **)subtypes );

   UF_free_string_array( type_count, (char **)type_names );

   if( worked == TRUE ) fprintf( log_file, "All creators succeeded\n" );
   else                 fprintf( log_file, "Some creator failed\n" );

   fprintf( log_file, "End testing creators\n" );
   UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
}
      

/* Generate toolpath */
/*----------------------------------------------------------------------------*/
static logical cycleGenerateCb
/*----------------------------------------------------------------------------*/
(
   tag_t   tag,
   void   *data
)
{
   logical  is_group, is_ok, gened;
   char     name[ UF_OPER_MAX_NAME_BUFSIZE ];
   int      ecode;
   FILE    *log_file = *(FILE **)data;

   int      hrs, mins, secs;
   time_t   start_time, end_time;
   double   e_time;

   /* This routine will be called for every item in the program view.  These
      items can either be an NCGROUP, which contains operations, or an 
      operation.  If it is a group, we will skip it, as we only want to
      regenerate operations.
   */
   UF_NCGROUP_is_group( tag, &is_group );
   if( is_group == TRUE ) return( TRUE );

   ecode = UF_OPER_ask_name_from_tag( tag, name );
   if( ecode != 0 )
   {
      issueError( log_file, ecode, "Can not get name of oper tag: %d\n", tag );
      return( TRUE );
   }

   /* Validate the parameters of this Operation. */
   UF_PARAM_check( tag, &is_ok );
   if( is_ok == FALSE ) 
   {
      fprintf( log_file, "Oper tag %d, name: %s failed check.", tag, name );
      return( TRUE );
   }

   fprintf( log_file, "Generating path of Oper tag %d, name %s\n", tag, name );

   start_time = time( NULL );

   /* This actually generates the tool path */
   ecode = UF_PARAM_generate( tag, &gened );
   end_time = time( NULL );
   if( ecode != 0 )
   {
      issueError( log_file, ecode, "Generation failed.\n" );
      return( TRUE );
   }
   if( gened == FALSE )
   {
      issueError( log_file, 0, 
        "Generation did not return an error but returned generation FALSE.\n" );
      return( TRUE );
   }

   e_time = difftime( end_time, start_time );
   hrs = (int)(e_time/3600);
   e_time = e_time - (hrs * 3600);
   mins = (int)(e_time/60);
   secs = (int)(e_time - (mins * 60));

   fprintf( log_file, "%s generation time: %02d:%02d:%02d\n", name,
                      hrs, mins, secs );
   return( TRUE );
}

/* This function shows how to create a new program group, and to copy
   the parameters from an existing program root to it.
*/
/*----------------------------------------------------------------------------*/
static void   create_new_program_group
/*----------------------------------------------------------------------------*/
(
   FILE   *log_file,
   char   *part_file
)
{
   tag_t         part_tag, obj1;
   logical       ok;
   int           type_count, count, error;
   const char  **subtypes, **type_names;
   UF_PART_load_status_t   err_status;
   tag_t         setup_tag, program_root_tag;
   logical       answer;
   char reason[UF_NCGROUP_MAX_REASON_BUFSIZE];

   ok = TRUE;

   error = UF_PART_open( part_file, &part_tag, &err_status );
   if( error != 0 )
   {
      issueError( log_file, error, "Error opening file %s\n", part_file );
      return;
   }

   /* Now get the unique setup object.  There is one and only one setup 
      object in a part. 
   */
   error = UF_SETUP_ask_setup( &setup_tag );
   if( error != 0 )
   {
      issueError( log_file, error, "Can not get setup from part\n" );
      fprintf( log_file, "End processing part file %s\n", part_file );
      UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
      return;
   }

   /* Get the existing program root in this part.
   */
   error = UF_SETUP_ask_program_root( setup_tag, &program_root_tag );
   if( error != 0 )
   {
      issueError( log_file, error, "Can not get program root from setup\n" );
      fprintf( log_file, "End processing part file %s\n", part_file );
      UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
      return;
   }
  
   /* Now get the name of all the object parameter template types. */ 
   error = UF_CAM_opt_ask_types( &type_count, &type_names );
   if( error != 0 )
   {
      issueError( log_file, error, "Error asking opt type names for file %s\n",
                                    part_file );
      fprintf( log_file, "End misc tests\n" );
      return;
   }
   if( type_count < 1 )
   {
      issueError( log_file, 0, "Part file %s has OPT with no types\n",
                               part_file );
      fprintf( log_file, "End misc tests\n" );
      return;
   }
  
   /* For the first object, get all of the UF_CAM_OPT_STYPE_CLS_PROG
      sub types.
   */ 
   error = UF_CAM_opt_ask_subtypes( type_names[0], UF_CAM_OPT_STYPE_CLS_PROG, 
                                    &count, &subtypes );
   if( count < 1 )
   {
      fprintf( log_file, "Part %s has no Program groups to be used as a"
                         " template object.\n", part_file );
      fprintf( log_file, "End misc tests\n" );
      UF_free_string_array( type_count, (char **)type_names );
      return;
   }

   /* Create a new program group in this part. */
   error = UF_NCPROG_create( (char *)type_names[0], (char *)subtypes[0], 
                             &obj1 );
   if( error != 0 )
   {
      issueError( log_file, error, "Can not create new Program Group\n" );
      fprintf( log_file, "End misc tests\n" );
      UF_free_string_array( type_count, (char **)type_names );
      UF_free_string_array( count, (char **)subtypes );
      return;
   }

   UF_free_string_array( type_count, (char **)type_names );
   UF_free_string_array( count, (char **)subtypes );

   /* Update obj1 with all of the parameters from the existing program
      group. 
   */
   error = UF_PARAM_reinit( obj1, program_root_tag );
   if( error != 0 )
   {
      issueError( log_file, error, "Can not UF_PARAM_reinit\n" );
      ok = FALSE;
   }

   /* Now add the newly created program group back to main program root. */
   error = UF_NCGROUP_can_accept_member( program_root_tag, obj1, &answer,
                                         reason);
   if( error != 0 || !answer )
   {
      issueError( log_file, error, 
                "Program root can not accept member because %s\n", reason );
      ok = FALSE;
   }

   error = UF_NCGROUP_accept_member(program_root_tag, obj1);
   if( error != 0 )
   {
      issueError( log_file, error, "Program root can not accept member \n");
      ok = FALSE;
   }

   if( ok == TRUE ) fprintf( log_file, "All Misc Tests Succeeded.\n" );

   error = UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );

   fprintf( log_file, "End misc tests\n" );

}


/*----------------------------------------------------------------------------*/
static int   UFX_CAM_test
/*----------------------------------------------------------------------------*/
(
   FILE   *log_file, int argc, char **argv
)
{
   int       ii, count, oks, hrs, mins, secs;
   int       ecode = 0;
   time_t    start_time, end_time;
   time_t    clsf_start_time, clsf_end_time;
   double    e_time;
   char    **filenames;
   logical is_cam_inited = FALSE;

   count = argc - 1;
   filenames = &argv[1];

   /* Check to make sure a file name was passed on the command line */
   if( count == 0 )
   {
      fprintf( log_file, "No part names passed as arguments.\n" );
      fprintf( log_file, "End processing.\n" );
      return( 0 );
   }

   start_time = time( NULL );
   oks = 0;
   for( ii = 0; ii < count; ii++ )
   {
      int     clsf_count;
      char   *part_file, scratch_file[ MAX_FSPEC_BUFSIZE ];
      tag_t   part_tag, setup_tag, program_root_tag;
      UF_PART_load_status_t   err_status;
      const char   **clsf_names;

      part_file = filenames[ii];

      fprintf( log_file, "\nBegin processing part file %s\n", part_file );

      ecode = UF_PART_open( part_file, &part_tag, &err_status );
      if( ecode != 0 )
      {
         issueError( log_file, ecode, "Error opening file %s\n", part_file );
         fprintf( log_file, "End processing part file %s\n", part_file );
         continue;
      }

      /* First initialize CAM.  This must be the first call made prior to any
         UG/Open calls to CAM.  This call requires a part to be open, which
         is why it is inside the loop.  It initializes CAM based upon the
         templates in the file whose name is contained in $UGII_CAM_CONFIG.
      */
      if( is_cam_inited == FALSE )
      {
         ecode = UF_CAM_init_session();
         if( ecode != 0 )
         {
            issueError( log_file, ecode,
                  "Error initializing CAM session using configuration file"
                  " defined by environment variable\n" );
            fprintf( log_file, "End processing part file %s\n", part_file );
            continue;
         }
         is_cam_inited = TRUE;
      }

      /* Now get the unique setup object.  There is one and only one setup 
         object in a part. 
      */
      ecode = UF_SETUP_ask_setup( &setup_tag );
      if( ecode != 0 )
      {
         issueError( log_file, ecode, "Can not get setup from part\n" );
         fprintf( log_file, "End processing part file %s\n", part_file );
         UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
         continue;
      }

      /* generate all programs (operations) in this part/setup.  First
         get the root of the program view tree.
      */
      ecode = UF_SETUP_ask_program_root( setup_tag, &program_root_tag );
      if( ecode != 0 )
      {
         issueError( log_file, ecode, "Can not get program root from setup\n" );
         fprintf( log_file, "End processing part file %s\n", part_file );
         UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
         continue;
      }

      /* Generate tool paths for every operation.  For each member of the
         program view tree, the routine cycleGenerateCb will be called. 
         We could pass any data in the third argument, but for this sample
         program we will pass the log file pointer.  
      */
      ecode = UF_NCGROUP_cycle_members( program_root_tag, cycleGenerateCb,
                                        &log_file );
      if( ecode != 0 )
      {
         issueError( log_file, ecode, "Can not UF_NCGROUP_cycle_members\n" );
         UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
         fprintf( log_file, "End processing part file %s\n", part_file );
         continue;
      }

      /* Now generate a clsf */
      ecode = UF_CAM_opt_ask_clsf_names( &clsf_count, &clsf_names );
      if( clsf_count < 1 )
      {
         issueError( log_file, 0, 
                     "No clsf definitions found in this UG session\n" );
         UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
         fprintf( log_file, "End processing part file %s\n", part_file );
         continue;
      }
      if( ecode != 0 )
      {
         issueError( log_file, ecode, "Can not ask clsfs names\n" );
         UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
         fprintf( log_file, "End processing part file %s\n", part_file );
         continue;
      }

      /* Create a unique filename for the scratch file. */
      ecode = uc4577( scratch_file ); 
      if( ecode < 0 )
      {
         issueError( log_file, ecode, "Can not create a unique filename\n" );
         UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
         fprintf( log_file, "End processing part file %s\n", part_file );
         continue;
      }

      fprintf( log_file, "\nBegin generating clsf %s\n", clsf_names[0] );
      clsf_start_time = time( NULL );
 
      /* Generate a CLSF for all the operations in the setup. */
      ecode = UF_SETUP_generate_clsf( setup_tag, program_root_tag, 
                                      clsf_names[0], scratch_file, 
                                      UF_SETUP_OUTPUT_UNITS_OUTPUT_DEFINED );
      clsf_end_time = time( NULL );

      /* Delete the CLSF output file */
      (void)uc4561( scratch_file, 0 ); 
      UF_free_string_array( clsf_count, (char **)clsf_names );

      if( ecode != 0 )
      {
         issueError( log_file, ecode, "Can not generate program\n" );
         UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
         fprintf( log_file, "End processing part file %s\n", part_file );
         continue;
      }


      e_time = difftime( clsf_end_time, clsf_start_time );
      hrs = (int)(e_time/3600);
      e_time = e_time - (hrs * 3600);
      mins = (int)(e_time/60);
      secs = (int)(e_time - (mins * 60));
      fprintf( log_file, "CLSF Total time: %02d:%02d:%02d\n", hrs, mins, secs );
      fprintf( log_file, "End generating clsf\n" );

      fprintf( log_file, "End processing part file %s\n", part_file );
      UF_PART_close( part_tag, ONLY_SPEC_PART, UNLOAD_ALWAYS );
      oks++;

   }

   fprintf( log_file, "Processed %d part file(s). %d success(es),"
                      " %d failure(s)\n", count, oks, count - oks );

   testCreators( log_file, filenames[0] );
   create_new_program_group( log_file, filenames[0] );

   end_time = time( NULL );
   e_time = difftime( end_time, start_time );
   hrs = (int)(e_time/3600);
   e_time = e_time - (hrs * 3600);
   mins = (int)(e_time/60);
   secs = (int)(e_time - (mins * 60));

   fprintf( log_file, "Total time: %02d:%02d:%02d\n", hrs, mins, secs );
   return( 0 );
}

extern int main(int argc, char **argv)
{
     FILE *log_file = NULL;
     struct tm *ctime;
     time_t clock;
     char buf[30];
     char message[500];
     int i;
     int return_code;

     /* Initialize UG/Open API */
     return_code = UF_initialize();
     if( return_code != 0 )
         return( return_code );

     /* First open the output log file. */
     log_file = fopen("ufx_cam.log","a");

     /* Now write out the time that this program was started. */
     clock = time((time_t *) 0);
     ctime = localtime(&clock);

     strftime(buf, 30, "%H:%M %m/%d/%Y", ctime);
     sprintf(message, "\n\n############ ufx_cam ############ %s \n", buf);
     if ( log_file!= NULL )
     {
         fprintf(log_file, "%s", message);
     }

     /* And now output the command line that was used to run the program. */
     message[0] = '\0';

     for ( i = 1; i < argc; i++ )
     {
         strcat ( message, argv[i] );
         strcat ( message, " " );
     }

     strcat ( message, "\n\n" );
     if ( log_file != NULL )
     {
         fprintf(log_file, "%s", message);
     }

     /* Now generate the tool paths */
     return_code = UFX_CAM_test(log_file, argc, argv);
     return( return_code );
}


