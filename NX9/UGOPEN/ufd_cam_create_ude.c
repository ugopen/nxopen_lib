/*=============================================================================
                 Copyright (c)  2001 Unigraphics Solutions, Inc.
                        Unpublished - All Rights Reserved
=============================================================================*/
/******************************************************************************
 *                                                                            *
 * PROGRAM NAME - ufd_cam_create_ude.c                                        *
 * PART FILE - ufd_cam_create_mfg4.prt                                        *
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *   UF_PARAM_can_accept_ude_set - Yes                                        *
 *   UF_PARAM_ask_udes - No                                                   *
 *   UF_PARAM_delete_all_udes - No                                            *
 *   UF_PARAM_append_ude - Yes                                                *
 *   UF_PARAM_delete_ude - No                                                 *
 *   UF_PARAM_can_accept_ude - Yes                                            *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example requires the open part, a manufacturing setup, and          *
 *   at least one highlighted operation. The UDE options selected from        *
 *   the menu will be created in each selected Node(operation).               *
 *                                                                            *
 *   See the sample program "ufd_cam_maint_ude.c" to edit, read, append       *
 *   or delete existing UDE's.                                                *
 *                                                                            *
 * EVENTS CREATED -                                                           *
 *   "mill_tool_change","spindle","spindle off","coolant" and "coolant off"   *      
 *                                                                            *
 *                                                                     *
 ******************************************************************************/

/***************************** Include Files **********************************/
#include <string.h>
#include <stdio.h>

#include <uf.h>
#include <uf_param.h>
#include <uf_oper.h>
#include <uf_ude.h>
#include <uf_cam.h>
#include <uf_ui.h>
#include <uf_ui_ont.h>
#include <uf_disp.h>
#include <uf_obj.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

#define GROUP_NAME_MAX_LEN 133

static int report( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char    messg[133];
        printf("%s, line %d:  %s\n", file, line, call);
        (UF_get_fail_message(irc, messg)) ?
            printf("    returned a %d\n", irc) :
            printf("    returned error %d:  %s\n", irc, messg);
    }
    return(irc);
}

static char udevents[] [38] = { "mill_tool_change",
                                "spindle",
                                "spindle_off",
                                "coolant",
                                "coolant_off" };

static int  do_camude_api(void)
    
 {
       char
           message[200];   	/* display message buffer */

       char getOpnam[GROUP_NAME_MAX_LEN+1];
      
       int cnt,                 /* loop counter */
           choice,              /* menu response */
           object_count,   	/* number of (nodes)operations identified */
           rcd;                 /* return code */

       tag_t
           *input_tags,    	/* tags of operations identified */
           output_tag;     	/* tag  of current operation selected in the ONT */

       UF_UDE_t
           ude_obj;       	/* UDE object */

       logical
           rsp;           	/* RC to see if the operation accept's UDE's */

/******************************************************************************/

                                /* Present a partial UDE menu to user. */
       while(1)
       {

       choice = uc1603("Select UDE's to create - Back or Cancel to terminate or finish.", 0, udevents, 5);
       if ( choice == 1 || choice == 2 )
        {
           UF_terminate();
           return 0;
        }
       choice = choice - 5;

                                /* Get the number of selected operation objects. */

       UF_CALL(UF_UI_ONT_ask_selected_nodes(&object_count, &input_tags));

                                /* Operation looping with "object_count". */

       for  ( cnt = 0; cnt < object_count; cnt++ ) {

       output_tag = input_tags[cnt];

       UF_CALL(UF_PARAM_can_accept_ude_set(output_tag, UF_UDE_START_SET, &rsp));

                                /* Try to accept a UDE. */

/*       printf("\n You selected ...%s\n", udevents[choice] );*/

       if( choice == 0 || choice == 1 || choice ==  3 ) {

                                /* Append the UDE to the UF_UDE_START_SET */

       UF_CALL(UF_PARAM_can_accept_ude(output_tag, UF_UDE_START_SET, udevents[choice],
                                  &rsp));
                 
       UF_CALL(UF_PARAM_append_ude(output_tag,UF_UDE_START_SET, udevents[choice], &ude_obj));

       }
       else
                                /* Append the UDE to the UF_UDE_END_SET */
       {
       UF_CALL(UF_PARAM_can_accept_ude(output_tag, UF_UDE_END_SET, udevents[choice],
                                  &rsp));
 
       UF_CALL(UF_PARAM_append_ude(output_tag,UF_UDE_END_SET, udevents[choice], &ude_obj));

       }
        switch( choice )
        {
            case 0:                 /* Set the UDE "load_tool_number" 1st integer. */


            rcd = UF_OPER_ask_name_from_tag( output_tag, getOpnam );

            if( strcmp( getOpnam, "CONTOUR_AREA" ) != 0 )
            { 
            UF_CALL(UF_UDE_set_integer(ude_obj, "load_tool_number", 12));
            break;
            }
                                    /* Set the UDE "load_tool_number" 2nd integer. */
             else
             {
            UF_CALL(UF_UDE_set_integer(ude_obj, "load_tool_number", 13));
             break;
             }
            case 1:                 /* Set the UDE "spindle speed to a real. */
                                   
            rcd = UF_OPER_ask_name_from_tag( output_tag, getOpnam );

            if( strcmp( getOpnam, "CONTOUR_AREA" ) != 0 )         
             { 
             UF_CALL(UF_UDE_set_double(ude_obj, "spindle_speed", 1161.0));
             UF_CALL(UF_UDE_set_string(ude_obj, "spindle_direction", "clw"));
             break;
             }
                                     /* Reset the UDE "spindle speed to a real */
             else
             {
             UF_CALL(UF_UDE_set_double(ude_obj, "spindle_speed", 1451.0));
             UF_CALL(UF_UDE_set_string(ude_obj, "spindle_direction", "clw"));
             break;
             }

            case 2:                 /* Set the UDE "spindle text". */

            {        
            UF_CALL(UF_UDE_set_param_toggle(ude_obj, "spindle_text", UF_UDE_PARAM_ACTIVE));
            break;
            } 

            case 3:                 /* Set the UDE "coolant" to "flood". */
   
            {
            UF_CALL(UF_UDE_set_string(ude_obj, "coolant_mode", "flood"));
            break;
            } 

            case 4:                 /* Set the UDE "coolant text". */

            {      
            UF_CALL(UF_UDE_set_param_toggle(ude_obj, "coolant_text", UF_UDE_PARAM_ACTIVE));
            break;
            }

            default:
            {
            printf("Catch all.\n");
            break;
            }
       }
      }
       UF_free(input_tags);
     }
 }
/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)

{
    if (!UF_CALL(UF_initialize()))
    {
    do_camude_api();
    UF_CALL(UF_terminate());
    }
}

int ufusr_ask_unload(void)
{
 return (UF_UNLOAD_IMMEDIATELY);
}

