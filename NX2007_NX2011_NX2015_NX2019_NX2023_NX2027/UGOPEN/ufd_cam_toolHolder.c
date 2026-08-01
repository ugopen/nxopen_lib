
/*=============================================================================
                        Copyright (c) 2004 UGS Corp.
                            All Rights Reserved
=============================================================================*/
/*****************************************************************************
* File Name: ufd_toolHolder_sample.c
*
* File Description:
*   Show Tool Holder usage for the new API programmer.
*
*   Files: ufd_cam_toolHolder.c ufd_cam_toolHolder.prt
*
*   Part file: ufd_cam_toolHolder.prt located in the CAM sample directory.
*
*   Usage: Requires the part file be active in Manufacturing.
*          Select a "Parent" Node in any of the ONT's views.
*          Execute the program for the following results.
*          Sets the Tool Holder parameters for Cavity Milling's NX3 requirement.
*          Queries the parameters and reports the result to the Information window.
*          Builds a 4-stack holder.
*          Optionally the part file could be saved.
*          
*

******************************************************************************/

/*===========================================================================*/
/*================================ INCLUDES =================================*/
/*===========================================================================*/ 

/******************************************* Include Files *******************************************/

#include <stdio.h>

#include <uf_disp.h>
#include <uf_ncgroup.h>
#include <uf_oper.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_ui_ont.h>
#include <uf.h>
#include <uf_param.h>
#include <uf_cutter.h>
#include <uf_ugopenint.h>
#include <uf_param_indices.h>

#include <uf_camgeom.h>

/*********************************************** MAIN ************************************************/

static FILE *outFile = NULL;

#if defined(_WIN32)
static const char *out_filename = "C:\\temp\\ufd_cam_toolHolder.out";
#endif


static void do_cam_th_api(void)

{
    int irc, ii, knt, isSet;
    int object_count;
    double isReal;
    double th_tool_offset = 0.375;
    double minClr[1] = {1.2};
    double minTlLength[1] = {1.5};
    double stacks[16] = {1.25,.25,0.0,0.125,1.00,.125,0.0,0.0,1.25,.25,0.0,0.0,1.00,2.0,-0.1745,0.0};

    logical getResult;

    tag_t operTag = NULL_TAG;
    tag_t toolTag = NULL_TAG;
    tag_t *objects = NULL;

    UF_CUTTER_holder_section_t stack_data;

    irc = UF_initialize();
    if( irc != 0 )
    {
        printf( "Failed to initialize uf %d\n", irc );
        return;
    }

    if( UF_PART_ask_display_part() != null_tag )
 {
    /* Get the highlighted/selected parent object from the ONT. */

        irc = UF_UI_ONT_ask_selected_nodes( &object_count, &objects ); 

        if (object_count > 0)
        {
            UF_NCGROUP_ask_object_of_name( *objects, "CAVITY_MILL", &operTag );
        
        /* Toggle ON Use Tool Holder. */

         irc = UF_PARAM_set_logical_value(operTag,UF_PARAM_CUT_TL_HOLDER_USAGE, TRUE );
          irc = UF_PARAM_ask_logical_value(operTag,UF_PARAM_CUT_TL_HOLDER_USAGE, &getResult );
           if ( getResult == TRUE )
           {
               UF_UI_open_listing_window( );
               UF_UI_write_listing_window("Tool Holder usage has been toggled ON.\n");
           }
         /* Set and Ask Use Volume Removed data. */

         irc = UF_PARAM_set_int_value(operTag,UF_PARAM_CUT_VOLUME_USAGE, 1);
          irc = UF_PARAM_ask_int_value(operTag,UF_PARAM_CUT_VOLUME_USAGE, &isSet );
           if ( isSet != 0 )
           {
               UF_UI_write_listing_window("Volume usage has been set.\n");
           }                            
        /* Set and Ask Volume Removed usage. */

         irc = UF_PARAM_set_int_value(operTag,UF_PARAM_CUT_VOLUME_ACTUAL, 1);
          irc = UF_PARAM_ask_int_value(operTag,UF_PARAM_CUT_VOLUME_ACTUAL, &isSet );
           if ( isSet != 0 )
           {
               UF_UI_write_listing_window("Volume removal rate will be reported.\n");
           }
        /* Set and Ask Report Minimum Tool Length. */

        irc = UF_PARAM_set_int_value(operTag,UF_PARAM_TL_MIN_LENGTH_USAGE, 1);
         irc = UF_PARAM_ask_int_value(operTag,UF_PARAM_TL_MIN_LENGTH_USAGE, &isSet );
          if ( isSet != 0 )
           {
               UF_UI_write_listing_window("Minimum Tool Length will be reported.\n");
           }                    
           /* Set and Ask Minimum Tool Length. */

        irc = UF_PARAM_set_double_value(operTag,UF_PARAM_TL_MIN_LENGTH, minTlLength[0] );
         irc = UF_PARAM_ask_double_value(operTag,UF_PARAM_TL_MIN_LENGTH_USAGE, &isReal );
          if ( isReal != 0 )
           {
               uc4406( "Minimum Tool Length is set to", minTlLength[0] );
           }
        /* Set and Ask Minimum Clearance between Holder and Part.*/

        irc = UF_PARAM_set_double_value(operTag,UF_PARAM_CLR_MIN, minClr[0] );
         irc = UF_PARAM_ask_double_value(operTag,UF_PARAM_CLR_MIN, &isReal );
          if ( isReal != 0 )
           {
               uc4406( "Minimum Holder to Part Clearance is set to", minClr[0] );
           }
        /* Set and Ask Minimum Required Volume to produce cut. */

        irc = UF_PARAM_set_double_value(operTag,UF_PARAM_CUT_VOLUME_MIN, 5 );
         irc = UF_PARAM_ask_double_value(operTag,UF_PARAM_CUT_VOLUME_MIN, &isReal );
          if ( isReal != 0 )
           {
               uc4406( "Minimum Volume Removal is set to", isReal );
           }
        /* Build a 4-stack holder one-by-one. */

        irc = UF_OPER_ask_cutter_group( operTag, &toolTag );

        irc = UF_PARAM_set_double_value(toolTag, UF_PARAM_TL_HOLDER_OFFSET, th_tool_offset );
        
        for ( ii = 0; ii <=15; ii += 4 )
            {
            stack_data.diameter=stacks[ii];
            stack_data.length=stacks[ii+1];
            stack_data.taper=stacks[ii+2];
            stack_data.corner=stacks[ii+3];

            irc = UF_CUTTER_create_holder_section(toolTag, &stack_data);
                        
            }

        }
            /* Windows file output. */

            irc = UF_CUTTER_ask_section_count(toolTag, &knt );

                uc4404( "Number of holder stacks defined is", knt );

#if defined (_WIN32)
        outFile = fopen(out_filename, "w");
        fprintf(outFile,"Number of holder stacks defined is %d.\n", knt );
#endif
        printf("Number of holder stacks defined is %d\n", knt );

#if defined (_WIN32)
        fclose(outFile);
#endif

 }
    UF_DISP_refresh ();

    printf(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n");

    /* To save the part file, uncomment the following function. */

        /* UF_PART_save(); */

    if( operTag != 0 )
    {
        UF_free( objects);
    }

    return;
}


/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
{
    UF_initialize();

    do_cam_th_api();

    UF_terminate();
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
