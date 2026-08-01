
/*=============================================================================
                   Copyright (c) 2001-2004 Unigraphics Solutions Inc.
                        Unpublished - All Rights Reserved
=============================================================================*/
/*****************************************************************************
 * File Name: ufd_cam_sample.c
 *
 * File Description:
 *   Build a basic CAM setup for the new API programmer. Writes to stdout.
 *
 *   Files: ufd_cam_sample.c ufd_camgeom_ugroup.c ufd_camgeom_ugroup.h
 *
 *   Part file: ufd_create_mfg3.prt located in the CAM sample directory.
 *
 *   Usage: Requires the part file to be open for testing.
 *          Builds a CAM setup with a mill_geom  & mill_area group.
 *          Adds Cavity Mill, Area Mill and Flowcut operation.
 *          Builds and modifies three UG tools.
 *          Calls "camgeom_ugroup" function for user to ident geometry.
 *          Modifies some parameters in each operation.
 *          Generates the tool paths and files the part.
 *
 *
 ******************************************************************************/

/*===========================================================================*/
/*================================ INCLUDES =================================*/
/*===========================================================================*/    

/******************************************* Include Files *******************************************/

#include <string.h>
#include <stdio.h>

#include <uf_cam.h>
#include <uf_disp.h>
#include <uf_ncgroup.h>
#include <uf_oper.h>
#include <uf_obj.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf.h>
#include <uf_param.h>
#include <uf_setup.h>
#include <uf_cutter.h>
#include <uf_ugopenint.h>
#include <uf_param_indices.h>

#include <ufd_camgeom_ugroup.h>

/*#define DEBUG*/

/*********************************************** MAIN ************************************************/

#define GROUP_NAME_MAX_LEN 133

#ifdef DEBUG
static FILE *outFile = NULL;
#endif

#if defined(_WIN32)
static const char *out_filename = "C:\\temp\\ufd_cam_sample_debug.out";
#endif

static int set_tool_param( int jj, tag_t toolTag );

static int cav_mill_param( int numop, tag_t *operTag );

static int flow_cut_param( int numop, tag_t *operTag );

static int area_mill_param( int numop, tag_t *operTag );

extern DllExport void ufusr (
    char   *param  ,            /* <I>
                                   Parameters - <unused>
                                */
    int    *retcod ,            /* <O>
                                   Return Code.  Not used by Internal
                                   UG/Open API.
                                */
    int     param_len           /* <I>
                                   Length of 'param' Argument.  Unigraphics
                                   handles this input for you.
                                */
)

{
        int type_count = 0; 
        int subtype_count = 0;
    int error_code = 0;
        int ii = 0, jj = 0, kk = 0;
        int ll = 1;
        int uchoice = 0;
        int prog_sub_cnt = 0;
     int mthd_sub_cnt = 0;
    int geom_sub_cnt = 0;
    int tool_sub_cnt = 0;
        int knt = 0;
        int choice = 0;
        int numop = 0;
        int obj_count = 1;
        int istr;

    char const **type_names, **subtype_names = 0; 
        char const **prog_sub_names, **mthd_sub_names, **geom_sub_names, **tool_sub_names; 
        char reason[UF_NCGROUP_MAX_REASON_BUFSIZE];
        char errorstrg[133];
        char getOpnam[GROUP_NAME_MAX_LEN+1];

        char *uTool[3] = {"Tool_1","Tool_2","Tool_3"};

        char *uMethod[3] = {"Roughing","Semi-Finish","Flowcut"};

        char uOper[] [38] = {"CAVITY_MILL","CONTOUR_AREA","FLOWCUT_SINGLE"};

        char *uPrognam = {"UserGroup"};
        
    tag_t *operTag = 0;
        tag_t setupTag;
    tag_t partTag, progTag = NULL_TAG, mthdTag, geomTag = NULL_TAG, toolTag;
        tag_t progRootTag, mthdRootTag, geomRootTag, toolRootTag; 
    tag_t prog_null; 
    tag_t geom_null; 
    tag_t mthd_null; 
    tag_t tool_null;
        tag_t wrkp_tag;

    logical answer;
        logical generate;

        error_code = UF_initialize();
        if( error_code != 0 )
        {
                printf( "Failed to initialize uf %d\n", error_code );
                return;
        }
        partTag =  UF_PART_ask_display_part();
         if ( partTag  != null_tag )
         {
         printf("Part file is open... \n");
          }
         else 
             {
             printf("We create a new part file...\n");

/*                  This will create the part file in the current directory             */
  
             error_code = UF_PART_new( "samplepart", 2, &partTag );
             }
              if( error_code != 0 )
           {
                printf( "Failed to create new part file %d\n", error_code );
                return;
               }

            error_code = UF_CAM_init_session();
           if( error_code != 0 )
        {
                printf( "Failed to initialize the CAM session %d\n", error_code );
                return;
            }

/*         Ask all the template types(part names) in the current CAM session            */

          UF_CAM_opt_ask_types( &type_count, &type_names );

#ifdef DEBUG
#if defined (_WIN32)
        outFile = fopen(out_filename, "w");
#endif
#endif

/*         If the current part has a CAM setup then delete it...INWORK                  */

        UF_SETUP_ask_setup( &setupTag );     
        if( setupTag == 0 )
        {
         printf(" Creating a new setup...\n" );
         UF_SETUP_create( partTag, type_names[1] );
         UF_SETUP_ask_setup( &setupTag );
        }

        for ( knt = 0; knt < type_count; knt++ )

        {
/*                                     Sample for Windows output                        */
#ifdef DEBUG
#if defined (_WIN32)
        fprintf(outFile,"Type %d is %s\n", knt, type_names[knt]);
#endif
        printf("Type %d is %s\n", knt, type_names[knt]);
        printf( "Type count = %d\n", type_count );
#endif
        }
#ifdef DEBUG
#if defined (_WIN32)
        fclose(outFile);
#endif
#endif

/*                                           Operations                                 */

        if( type_count > 0 )
    {
                UF_CAM_opt_ask_subtypes( type_names[1], UF_CAM_OPT_STYPE_CLS_OPER, &subtype_count, 
                                        &subtype_names );
#ifdef DEBUG
                printf( "subtype count = %d\n", subtype_count );
                for ( knt = 0; knt < subtype_count; knt++ )
                printf("SubTypeName(%d) is %s\n", knt, subtype_names[knt]);
#endif
            do 
             {                
                if( subtype_count > 0 )
               {
                        operTag = (tag_t *)UF_allocate_memory( sizeof( operTag ) * subtype_count, &error_code );
                        if ( uchoice == 0 )
                        {
                        choice = uc1603("Choose Cavity Mill as first operation! - Back or Cancel to quit.", 0, uOper, 3);
                        }
                         else
                         {
                          choice = uc1603("Choose Surface Contouring operation! - Back or Cancel to quit.", 0, uOper, 3);
                         }

                        if ( choice == 1 || choice == 2 )
                        {
                            UF_terminate();
                            UF_free( operTag );
                            return;
                        }
                        else
                        {
                        choice = choice - 5;
                        uchoice = 1;
                        }                       
                        for( ii = 0; ii <subtype_count; ii++ )
                        {
                            if( strcmp( subtype_names[ii],uOper[choice] ) == 0 ) 
                            {
                            printf("Choice count is %d\n", choice);
                            UF_OPER_create( (char *) type_names[1], (char *)subtype_names[ii], &operTag[numop] );
                            printf("Created operation %s \n", subtype_names[ii] );
                            printf("Created operation tag number %d \n", operTag[numop] );
                            numop++;
                            }   
                        }
                        
                        printf("Operation count is %d\n", numop);
                }

/*                                            Program Groups                                      */

                UF_CAM_opt_ask_subtypes( type_names[1], UF_CAM_OPT_STYPE_CLS_PROG, &prog_sub_cnt,
                                        &prog_sub_names );
#ifdef DEBUG
                printf( "Progsubcount = %d\n", prog_sub_cnt );
                for ( knt = 0; knt < prog_sub_cnt; knt++ )
                printf("Progsubname %d is %s\n", knt, prog_sub_names[knt]);
#endif
                if( prog_sub_cnt > 0 )
                {
                    if ( numop == 1 )
                    {

/*                                    Create one program group only                              */

                  UF_NCPROG_create( (char *)type_names[1], (char *)prog_sub_names[0], &progTag );
                        UF_OBJ_set_name( progTag, uPrognam );
                    UF_SETUP_ask_program_root( setupTag, &progRootTag );
            UF_NCGROUP_can_accept_member( progRootTag, progTag, &answer, reason );
                     if( answer == TRUE )
                            UF_NCGROUP_accept_member( progRootTag, progTag );
                    }

/*                                      Move the operation into the program                      */

                                  UF_NCGROUP_can_accept_member( progTag, operTag[numop-1], &answer, reason );
                                  if( answer == TRUE )
                                    UF_NCGROUP_accept_member( progTag, operTag[numop-1] );
                else
                {
                            UF_SETUP_ask_program_null( setupTag, &prog_null );
                    UF_NCGROUP_accept_member( prog_null, operTag[numop-1] );
                } 
                }

/*                                    If there are no program templates                           */

                                else if ( numop > 0 )
                               {
                                UF_SETUP_ask_program_null( setupTag, &prog_null );
                                UF_NCGROUP_accept_member( prog_null, operTag[numop-1] );                               
                            }

/*                                            Method Groups                                      */
    
        UF_CAM_opt_ask_subtypes( type_names[1], UF_CAM_OPT_STYPE_CLS_METHOD, &mthd_sub_cnt,
                    &mthd_sub_names );
#ifdef DEBUG
                printf( "Metsubcount = %d\n", mthd_sub_cnt );
                for ( knt = 0; knt < mthd_sub_cnt; knt++ )
                printf("Metsubname %d is %s\n", knt, mthd_sub_names[knt]);
#endif
        if( mthd_sub_cnt > 0 )
        {
            UF_NCMTHD_create( (char *)type_names[1], (char *)mthd_sub_names[0], &mthdTag );
                        UF_OBJ_set_name( mthdTag, uMethod[kk] );            
            UF_SETUP_ask_mthd_root( setupTag, &mthdRootTag );
            UF_NCGROUP_can_accept_member( mthdRootTag, mthdTag, &answer, reason );
            if( answer == TRUE )
                UF_NCGROUP_accept_member( mthdRootTag, mthdTag );


                UF_NCGROUP_can_accept_member( mthdTag, operTag[numop-1], &answer, reason );
                if( answer == TRUE )
                    UF_NCGROUP_accept_member( mthdTag, operTag[numop-1] );
                else            
                               {
                                    UF_SETUP_ask_mthd_null( setupTag, &mthd_null );
                                    UF_NCGROUP_accept_member( mthd_null, operTag[numop-1] );
                            }
                        kk++;
                }
/*                                            Geometry Groups                                      */

        UF_CAM_opt_ask_subtypes( type_names[1], UF_CAM_OPT_STYPE_CLS_GEOM, &geom_sub_cnt,
                                        &geom_sub_names );

#ifdef DEBUG
                printf("Geomsubcnt %d is %s\n", knt, geom_sub_names[knt]);
                for ( knt =0 ; knt < geom_sub_cnt; knt++ )                 
                 printf("Geomsubnam %d is %s\n", knt, geom_sub_names[knt]);
#endif

                if( geom_sub_cnt > 0 )
                 {
                    printf("Currently numop is set to %d\n", numop );
                    if ( choice < 2 )
                      {
                        UF_NCGEOM_create( (char *)type_names[1], (char *)geom_sub_names[ll], &geomTag );
                        UF_SETUP_ask_geom_root( setupTag, &geomRootTag );
                        UF_NCGROUP_ask_object_of_name( geomRootTag, "WORKPIECE", &wrkp_tag );
#ifdef DEBUG
                        printf( "WP tag is %d \n", wrkp_tag );
                        printf("Created the sub-name %s\n", geom_sub_names[ll] );
                        printf( "Sub name tag is %d \n", geomTag );
#endif
                        if ( wrkp_tag != null_tag )
                        {
                         UF_NCGROUP_can_accept_member( wrkp_tag, geomTag, &answer, reason );

                        if( answer == TRUE )

                         UF_NCGROUP_accept_member( wrkp_tag, geomTag );
                        if (strcmp( geom_sub_names[ll],"MILL_GEOM") == 0 ) 
                         {
                          printf("Call ufd_camgeom_ugroup to identify workpiece...\n");
                          printf("Object count passed to workpiece %d\n", obj_count );
                  error_code = ufd_camgeom_ugroup( wrkp_tag, obj_count );
                           if ( error_code != 0 )
                            {
                             printf(" Returns in error...\n");
                            }
                         }

/*                         Else call the geometry routine again for cut area                              */

                          else if (strcmp( geom_sub_names[ll],"MILL_AREA" ) == 0 )
                           {
                            printf("Call ufd_camgeom_ugroup to identify cut area...\n");
                            printf("Object count passed to cut area %d\n", obj_count );
                    error_code = ufd_camgeom_ugroup( geomTag, obj_count );
                             if ( error_code != 0 )
                              {
                               printf(" Returns in error...\n");
                              }
                           }
                        }
                        else  
                        {
                         UF_NCGROUP_can_accept_member( geomRootTag, geomTag, &answer, reason );

                        if( answer == TRUE )

                         UF_NCGROUP_accept_member( geomRootTag, geomTag );

                         else
                         {
                         printf("Failed to add to group because %s \n", reason );
                         }
                        }
                      } 
                              UF_NCGROUP_can_accept_member( geomTag, operTag[numop-1], &answer, reason );

                                if( answer == TRUE )
                                {
                                        UF_NCGROUP_accept_member( geomTag, operTag[numop-1] );
                                }
                else            
                               {
                                UF_SETUP_ask_geom_null( setupTag, &geom_null );
                                UF_NCGROUP_accept_member( geom_null, operTag[numop-1] );                               
                            }
                        ll=3;
                }

/*                                            Machine Tool  Groups                                      */

        UF_CAM_opt_ask_subtypes( type_names[1], UF_CAM_OPT_STYPE_CLS_TOOL, &tool_sub_cnt, 
                    &tool_sub_names );
#ifdef DEBUG
                 for ( knt = 0 ; knt < tool_sub_cnt; knt++ )
                  printf("ToolSubName(%d) is %s\n", knt, tool_sub_names[knt]);
#endif

        if( tool_sub_cnt > 0 )
        {
            UF_CUTTER_create( (char *)type_names[1], (char *)tool_sub_names[0], &toolTag );
                        UF_OBJ_set_name( toolTag, uTool[jj] );
    
            UF_SETUP_ask_mct_root( setupTag, &toolRootTag );
                        UF_NCGROUP_can_accept_member( toolRootTag, toolTag, &answer, reason );

                        if( answer == TRUE )
                                UF_NCGROUP_accept_member( toolRootTag, toolTag );
        

                                UF_NCGROUP_can_accept_member( toolTag, operTag[numop-1], &answer, reason );
                                if( answer == TRUE ) 
                                {
                                        UF_NCGROUP_accept_member( toolTag, operTag[numop-1] );
                                }
                                else
                                {
                                        UF_SETUP_ask_mct_null( setupTag, &tool_null );
                                        UF_NCGROUP_accept_member( tool_null, operTag[numop-1] );
                                }
                        jj++;
                                          /* Set the tool parameters */

                        set_tool_param( jj, toolTag );

                }
#ifdef DEBUG
                printf( "Type count = %d\n", type_count );
                printf( "SubType count = %d\n", subtype_count );
                printf( "Value of numop is %d\n", numop-1 );
#endif

                error_code = UF_OPER_ask_name_from_tag( operTag[numop-1] , getOpnam );
#ifdef DEBUG
                printf("getOpnam returns string %s\n", getOpnam );
#endif

/*               Use calls to UF_PARAM_... to set Depth/Cut and stock in Cavity Mill.      */

                 if( strcmp( getOpnam, "CAVITY_MILL" ) == 0 )

/*                               Call the cavity mill parameter function.                   */

                     cav_mill_param( numop, operTag );
 
                   UF_DISP_refresh ();

                   if( strcmp( getOpnam, "FLOWCUT_SINGLE" ) == 0 )

/*                               Call the flow cut parameter function.                   */

                     {
                      flow_cut_param( numop, operTag );
                     }

                     else
/*                               Call the area mill  parameter function.                   */

                     area_mill_param( numop, operTag );

                       UF_DISP_refresh ();
 
                    error_code = UF_PARAM_generate( operTag[numop-1], &generate );
                     if ( generate != TRUE )
                     {
                       printf(" Logical returns FALSE\n");
                       if ( error_code != 0 )
                        {
                         UF_get_fail_message ( error_code, errorstrg );
                         printf ( "\n Caution - %s\n", errorstrg ); 
                         istr =  strcmp ( errorstrg, "Tool cannot fit into level" );
                         if ( istr == 0 )
                          {
                           printf ( "Cavity Mill operation generated successfully\n" );
                          }
                        }
                     }
                      else
                       {
                        printf ( "\nGenerated the operation %s successfully...\n", getOpnam );
                       }
                       UF_DISP_refresh ();
 
             } while ( choice < 2 ); 

             printf(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n");
       
        }

        UF_DISP_refresh ();

/*                  To save the part file, uncomment the following function call.                 */

/*        UF_PART_save();*/
        if( type_count > 0 )
    {
                UF_free_string_array( type_count, (char **)type_names );
        }
        if( subtype_count > 0 )
        {
                UF_free_string_array( subtype_count, (char **)subtype_names );
        }
        if( operTag != 0 )
        {
                UF_free( operTag );
        }

        return;
}

int ufusr_ask_unload(void)
{
 return (UF_UNLOAD_IMMEDIATELY);
}

static int set_tool_param( int jj, tag_t toolTag )
{
    double toolDia = 0, toolRad = 3;

/*                 Modify the default 5-Parameter Milling Tool         */

        switch( jj )
        {
/*                               Tool No. 1                            */
/*                             Add a 3.0 MM crad                       */
        case 1:
            {
            UF_PARAM_set_double_value( toolTag, UF_PARAM_TL_COR1_RAD, toolRad );
            break;
            }
/*                               Tool No. 2                            */
/*                             Make this a Ball Nose                   */
        case 2:
            {
            UF_PARAM_ask_double_value( toolTag, UF_PARAM_TL_DIAMETER, &toolDia );
            UF_PARAM_set_double_value( toolTag, UF_PARAM_TL_COR1_RAD, toolDia/2 );
            break;
            }
/*                               Tool No. 3                            */
/*                           Define a smaller Ball Nose                */
        case 3:
            {
            UF_PARAM_set_double_value( toolTag, UF_PARAM_TL_DIAMETER, 25.0 );
            UF_PARAM_set_double_value( toolTag, UF_PARAM_TL_COR1_RAD, (25.0/2) );
            break;
            }
        default:
            {
            printf( "Default...\n" );
            }
        }
        return 0;
}

static int cav_mill_param( int numop, tag_t *operTag )
{
/*   int    numop;*/
   double depthPerCut;
   double stockPart;

    UF_PARAM_ask_double_value( operTag[numop-1] , UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH, &depthPerCut);
    printf(" Depth/Cut default is set to %f\n", depthPerCut );
    UF_PARAM_set_double_value( operTag[numop-1] , UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH, 12.000 );
    UF_PARAM_ask_double_value( operTag[numop-1] , UF_PARAM_CUTLEV_GLOBAL_CUT_DEPTH, &depthPerCut );
    printf(" Verify Depth/Cut reset to %f\n", depthPerCut );

    UF_PARAM_ask_double_value( operTag[numop-1] , UF_PARAM_STOCK_PART, &stockPart );
    printf(" Part Stock default is set to %f\n", stockPart );
    UF_PARAM_set_double_value( operTag[numop-1] , UF_PARAM_STOCK_PART, 1.0 );
    UF_PARAM_ask_double_value( operTag[numop-1] , UF_PARAM_STOCK_PART, &stockPart );
    printf(" Verify Part Stock reset to %f\n", stockPart );

    UF_PARAM_set_int_value( operTag[numop-1], 327, UF_PARAM_cut_trace_method_tolerant );
    UF_PARAM_set_int_value( operTag[numop-1], 328, UF_PARAM_cut_ctrl_trim_method_silhoutte );

    return 0;
}

static int flow_cut_param( int numop, tag_t *operTag )
{
    UF_PARAM_disp_tool_t display_data;
    display_data.type = 2;             /* Type = 2 produces 3D tool display in tool path. */
    display_data.frequency = 10;

    UF_PARAM_set_subobj_ptr_value( operTag[numop-1], UF_PARAM_DISP_TOOL , &display_data );
    UF_PARAM_ask_subobj_ptr_value( operTag[numop-1], UF_PARAM_DISP_TOOL , &display_data );
    printf("Display data for tool type returns %d\n", display_data.type );
    printf("Display data for tool frequency returns %d\n", display_data.frequency );

    return 0;
}

static int area_mill_param( int numop, tag_t *operTag )
{

    UF_PARAM_set_int_value( operTag[numop-1],UF_PARAM_CUT_EDGE_TRACE_REMOVAL,UF_PARAM_edge_trace_removal_on );

/*                                           1 = Warning, 2 = Skip, 3 = Retract  */ 

    UF_PARAM_set_int_value( operTag[numop-1],UF_PARAM_AVOIDANCE,UF_PARAM_avoid_stepover ); 
    UF_PARAM_set_int_value( operTag[numop-1],UF_PARAM_CUT_FOLLOW_CHECK_STATUS,UF_PARAM_cut_follow_check_on );

    return 0;
}
